"""Credentials, HTTP, embeddings, and a small Qdrant client for the fleet-agents corpus.

Credentials come from the environment when set, otherwise from Infisical shared/prod via the
machine identity in ~/.secrets/global-api-keys.  Values are never printed or logged.

Read vs write: if QDRANT_READONLY_API_KEY is available it is used for every read path
(search / scroll / count / stats); QDRANT_API_KEY is used only for upsert / delete.  Callers
that only read may pass need_write=False so a machine without the write key still works.
"""
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any, Iterable

INFISICAL_API = "https://app.infisical.com/api"
SHARED_PROJECT = "18f563a3-9c88-454c-96eb-28fc9678f3ba"
SHARED_ENV = "prod"
HANDOFF = pathlib.Path.home() / ".secrets" / "global-api-keys"
NAMESPACE = uuid.UUID("00000000-0000-0000-0000-00000000fee7")

READ_KEYS = ("TEI_URL", "TEI_API_KEY", "QDRANT_URL", "QDRANT_FLEET_COLLECTION")
WRITE_KEYS = ("QDRANT_API_KEY",)
OPTIONAL_KEYS = ("QDRANT_READONLY_API_KEY", "TEI_EMBED_MODEL")
ALL_KEYS = READ_KEYS + WRITE_KEYS + OPTIONAL_KEYS

EMBED_MODEL_TAG = "BAAI/bge-m3-selfhosted"
EMBED_BATCH = 8          # the ONNX backend caps a batch at 8 requests
DEFAULT_TIMEOUT = 120
RETRIES = 4


class FleetRagError(RuntimeError):
    pass


# --------------------------------------------------------------------------- HTTP

def http_json(url: str, body: Any = None, headers: dict | None = None, method: str | None = None,
              timeout: int = DEFAULT_TIMEOUT, retries: int = RETRIES) -> Any:
    """JSON request with bounded retries on 429 / 5xx / connection errors.  Never logs bodies."""
    data = json.dumps(body).encode() if body is not None else None
    method = method or ("POST" if body is not None else "GET")
    last: Exception | None = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=data, method=method,
                                     headers={"Content-Type": "application/json", **(headers or {})})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                return json.loads(raw) if raw.strip() else {}
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(min(2 ** attempt, 10))
                continue
            detail = ""
            try:
                detail = e.read(400).decode(errors="replace")
            except Exception:  # noqa: BLE001
                pass
            raise FleetRagError(f"HTTP {e.code} from {_host(url)}{urllib.parse.urlparse(url).path}: {detail}") from None
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = e
            if attempt < retries:
                time.sleep(min(2 ** attempt, 10))
                continue
            raise FleetRagError(f"{type(e).__name__} reaching {_host(url)}") from None
    raise FleetRagError(f"request failed: {type(last).__name__}")


def _host(url: str) -> str:
    return urllib.parse.urlparse(url).netloc


# --------------------------------------------------------------------------- credentials

def _identity(prefix: str) -> tuple[str | None, str | None]:
    if not HANDOFF.exists():
        return None, None
    cid = csec = None
    for line in HANDOFF.read_text().splitlines():
        m = re.match(rf"^{prefix}_CLIENT_ID=(.*)$", line)
        if m:
            cid = m.group(1).strip().strip('"').strip("'")
        m = re.match(rf"^{prefix}_CLIENT_SECRET=(.*)$", line)
        if m:
            csec = m.group(1).strip().strip('"').strip("'")
    return cid, csec


def infisical_login() -> str | None:
    """Return a short-lived Infisical access token via the shared machine identity, or None."""
    for prefix in ("INFISICAL_SHARED", "INFISICAL_AUTOMATION"):
        cid, csec = _identity(prefix)
        if not cid or not csec:
            continue
        try:
            return http_json(f"{INFISICAL_API}/v1/auth/universal-auth/login",
                             {"clientId": cid, "clientSecret": csec}, retries=1)["accessToken"]
        except (FleetRagError, KeyError):
            continue
    return None


def load_config(need_write: bool = False, extra: Iterable[str] = ()) -> dict[str, str]:
    """Environment first, then Infisical shared/prod.  Returns the keys that were found.

    Raises FleetRagError listing the missing required keys (never their values).
    """
    wanted = list(ALL_KEYS) + [k for k in extra if k not in ALL_KEYS]
    cfg = {k: os.environ[k] for k in wanted if os.environ.get(k)}
    required = list(READ_KEYS) + (list(WRITE_KEYS) if need_write else []) + list(extra)
    if all(k in cfg for k in required) and all(k in cfg for k in OPTIONAL_KEYS if k in wanted):
        return cfg
    tok = infisical_login()
    if tok:
        try:
            got = http_json(f"{INFISICAL_API}/v3/secrets/raw?workspaceId={SHARED_PROJECT}"
                            f"&environment={SHARED_ENV}&secretPath=%2F",
                            headers={"Authorization": f"Bearer {tok}"}, retries=1)
            for s in got.get("secrets", []):
                if s["secretKey"] in wanted:
                    cfg.setdefault(s["secretKey"], s["secretValue"])
        except FleetRagError:
            pass
    missing = [k for k in required if k not in cfg]
    if missing:
        raise FleetRagError("missing credentials: " + ", ".join(missing)
                            + " (set them in the environment or in Infisical shared/prod)")
    return cfg


# --------------------------------------------------------------------------- embeddings

def embed(cfg: dict[str, str], texts: list[str]) -> list[list[float]]:
    """Embed texts with the self-hosted bge-m3 endpoint.  Over-length inputs are truncated."""
    out: list[list[float]] = []
    base = cfg["TEI_URL"].rstrip("/")
    hdr = {"Authorization": f"Bearer {cfg['TEI_API_KEY']}"}
    for i in range(0, len(texts), EMBED_BATCH):
        out += http_json(f"{base}/embed", {"inputs": texts[i:i + EMBED_BATCH], "truncate": True}, hdr)
    return out


def embedder_healthy(cfg: dict[str, str]) -> bool:
    try:
        with urllib.request.urlopen(f"{cfg['TEI_URL'].rstrip('/')}/health", timeout=30) as r:
            return r.status == 200
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError):
        return False


# --------------------------------------------------------------------------- ids / text

def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def point_id(digest: str) -> str:
    return str(uuid.uuid5(NAMESPACE, digest))


def now_ms() -> int:
    return int(time.time() * 1000)


_STOP = set("""a an and are as at be but by for from has have how i if in into is it its of on or
that the their there these this to was what when where which who why will with you your our we
do does did not no yes can could should would may might must me my""".split())


def query_terms(query: str, max_terms: int = 8) -> list[str]:
    """Keyword terms for the full-text side of hybrid search: lowercase, no stopwords, >2 chars."""
    seen: list[str] = []
    for tok in re.findall(r"[A-Za-z0-9_][A-Za-z0-9_\-./]{2,}", query.lower()):
        tok = tok.strip(".-/")
        if len(tok) < 3 or tok in _STOP or tok in seen:
            continue
        seen.append(tok)
        if len(seen) >= max_terms:
            break
    return seen


# --------------------------------------------------------------------------- Qdrant

class Qdrant:
    """Minimal REST client scoped to one collection.  Reads use the read-only key when present."""

    def __init__(self, cfg: dict[str, str], collection: str | None = None):
        self.base = cfg["QDRANT_URL"].rstrip("/")
        self.collection = collection or cfg["QDRANT_FLEET_COLLECTION"]
        self._read_key = cfg.get("QDRANT_READONLY_API_KEY") or cfg.get("QDRANT_API_KEY")
        self._write_key = cfg.get("QDRANT_API_KEY")
        if not self._read_key:
            raise FleetRagError("no Qdrant key available for reads")

    # -- plumbing
    def _call(self, path: str, body: Any = None, method: str | None = None, write: bool = False,
              timeout: int = DEFAULT_TIMEOUT) -> Any:
        key = self._write_key if write else self._read_key
        if write and not key:
            raise FleetRagError("QDRANT_API_KEY (write key) not available on this machine")
        try:
            return http_json(f"{self.base}{path}", body, {"api-key": key}, method, timeout=timeout)
        except FleetRagError as e:
            # A staged read-only key that the server has not loaded yet answers 401/403.
            # Fall back to the write key for the rest of this process instead of failing reads.
            if (not write and self._write_key and key != self._write_key
                    and ("HTTP 401" in str(e) or "HTTP 403" in str(e))):
                self._read_key = self._write_key
                return http_json(f"{self.base}{path}", body, {"api-key": self._write_key}, method,
                                 timeout=timeout)
            raise

    def _cpath(self, suffix: str = "") -> str:
        return f"/collections/{self.collection}{suffix}"

    # -- reads
    def healthz(self) -> bool:
        try:
            with urllib.request.urlopen(f"{self.base}/healthz", timeout=30) as r:
                return r.status == 200
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError):
            return False

    def info(self) -> dict:
        return self._call(self._cpath())["result"]

    def count(self, flt: dict | None = None, exact: bool = True) -> int:
        body: dict[str, Any] = {"exact": exact}
        if flt:
            body["filter"] = flt
        return self._call(self._cpath("/points/count"), body)["result"]["count"]

    def scroll(self, flt: dict | None = None, limit: int = 256, with_payload: Any = True,
               with_vector: bool = False):
        """Yield points matching the filter, paging through the collection."""
        offset = None
        while True:
            body: dict[str, Any] = {"limit": limit, "with_payload": with_payload, "with_vector": with_vector}
            if flt:
                body["filter"] = flt
            if offset is not None:
                body["offset"] = offset
            res = self._call(self._cpath("/points/scroll"), body)["result"]
            for p in res.get("points", []):
                yield p
            offset = res.get("next_page_offset")
            if offset is None:
                break

    def search_dense(self, vector: list[float], limit: int = 5, flt: dict | None = None) -> list[dict]:
        body: dict[str, Any] = {"vector": vector, "limit": limit, "with_payload": True}
        if flt:
            body["filter"] = flt
        return self._call(self._cpath("/points/search"), body)["result"]

    def query_hybrid(self, vector: list[float], terms: list[str], limit: int = 5,
                     flt: dict | None = None, prefetch_limit: int | None = None) -> list[dict]:
        """Dense + keyword fusion via the Query API.

        Two prefetches — plain dense, and dense restricted to points whose full-text index matches
        any of the keyword terms — fused with reciprocal rank fusion.  Falls back to plain dense
        search when there are no usable terms.
        """
        if not terms:
            return self.search_dense(vector, limit, flt)
        pl = prefetch_limit or max(limit * 4, 20)
        kw_filter: dict[str, Any] = {"should": [{"key": "text", "match": {"text": t}} for t in terms]}
        if flt:
            kw_filter = {"must": [flt, kw_filter]}
        prefetch = [
            {"query": vector, "limit": pl, **({"filter": flt} if flt else {})},
            {"query": vector, "limit": pl, "filter": kw_filter},
        ]
        body = {"prefetch": prefetch, "query": {"fusion": "rrf"}, "limit": limit, "with_payload": True}
        return self._call(self._cpath("/points/query"), body)["result"]["points"]

    # -- writes
    def upsert(self, points: list[dict], wait: bool = True) -> str:
        if not points:
            return "ok"
        res = self._call(self._cpath(f"/points?wait={'true' if wait else 'false'}"),
                         {"points": points}, method="PUT", write=True, timeout=300)
        return res.get("status", "?")

    def delete_by_filter(self, flt: dict, wait: bool = True) -> str:
        res = self._call(self._cpath(f"/points/delete?wait={'true' if wait else 'false'}"),
                         {"filter": flt}, method="POST", write=True, timeout=300)
        return res.get("status", "?")

    def delete_ids(self, ids: list[str], wait: bool = True) -> str:
        if not ids:
            return "ok"
        res = self._call(self._cpath(f"/points/delete?wait={'true' if wait else 'false'}"),
                         {"points": ids}, method="POST", write=True, timeout=300)
        return res.get("status", "?")

    def set_payload(self, ids: list[str], payload: dict, wait: bool = True) -> str:
        res = self._call(self._cpath(f"/points/payload?wait={'true' if wait else 'false'}"),
                         {"points": ids, "payload": payload}, method="POST", write=True)
        return res.get("status", "?")

    def snapshot(self) -> dict:
        return self._call(self._cpath("/snapshots"), {}, method="POST", write=True, timeout=600)["result"]


# --------------------------------------------------------------------------- filters

def match_filter(**fields: str | None) -> dict | None:
    """Exact-match filter on payload fields; None values are skipped."""
    must = [{"key": k, "match": {"value": v}} for k, v in fields.items() if v]
    return {"must": must} if must else None


def build_point(text: str, payload: dict) -> dict:
    """Payload plus deterministic id; the caller supplies the vector afterwards."""
    digest = content_hash(text)
    return {"id": point_id(digest), "payload": {**payload, "text": text, "content_hash": digest,
                                                 "embed_model": EMBED_MODEL_TAG}}


def eprint(*a: Any) -> None:
    print(*a, file=sys.stderr, flush=True)
