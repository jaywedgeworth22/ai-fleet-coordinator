"""The recall tool contract: recall_search / recall_stats / recall_contribute.

One implementation shared by the `recall` CLI, the `fleet-recall-mcp.py` stdio server, and
the seat-mcp tools, so every surface has exactly the same semantics.  Functions return plain
dicts and raise FleetRagError on user errors (bad arguments, missing credentials).  Nothing in
this module prints; callers decide how to render.

Backend seams: the module-level names `load_config`, `embed`, `embedder_healthy`, `Qdrant`,
`gitleaks_flagged`, and `gitleaks_available` are what the functions call, so a test (or the
FLEET_RECALL_FAKE=1 hook, see `install_fake_backend`) can replace them without touching the
live services.
"""
from __future__ import annotations

import datetime
import json
import os
import re
import shutil
import tempfile
from typing import Any

from . import core
from .core import FleetRagError, build_point, content_hash, match_filter, now_ms, query_terms
from .scrub import gitleaks_flagged as _real_gitleaks_flagged
from .scrub import scrub

# Seams (monkeypatch these in tests; install_fake_backend() swaps them all at once).
load_config = core.load_config
embed = core.embed
embedder_healthy = core.embedder_healthy
Qdrant = core.Qdrant
gitleaks_flagged = _real_gitleaks_flagged


def _real_gitleaks_available() -> bool:
    return bool(shutil.which("gitleaks"))


gitleaks_available = _real_gitleaks_available

SOURCES = ("board", "effort-log", "apple-note", "doc", "skill", "memory", "chat-log",
           "agent-contribution")
CATEGORIES = ("lesson", "preference", "infrastructure", "decision", "runbook", "finding", "note", "doc")
CONTRIB_CATEGORIES = ("lesson", "preference", "infrastructure", "decision", "runbook")
KNOWN_APPS = ("fleet", "socratic-trade", "congress-trade", "congress-trading-shared", "usage-monitor",
              "dealdex", "botfleet", "personal-site", "fleet-ops", "autorotate", "contactlogo")
HIT_FIELDS = ("source", "app", "category", "seat", "doc_id", "chunk_index", "heading", "title",
              "url", "path", "created_at")

# The ingest orchestrator stores its run sentinel as a point with source="meta".  It is never
# a search result: every search filter carries this must_not clause.
META_SOURCE = "meta"


def meta_exclude() -> dict:
    """Fresh must_not condition for the ingest sentinel (fresh so callers cannot share state)."""
    return {"key": "source", "match": {"value": META_SOURCE}}

# Marker appended to recall_contribute()["scrubbed"] when gitleaks is not installed, so callers
# can see that only the regex scrub ran.
GITLEAKS_UNAVAILABLE = "gitleaks-unavailable"

MAX_LIMIT = 50
CONTRIB_MIN = 40
CONTRIB_MAX = 4000
DAY_MS = 86_400_000

_APP_RE = re.compile(r"^[a-z0-9][a-z0-9\-]{0,63}$")
_SEAT_RE = re.compile(r"^[A-Z][A-Z0-9_\-]{0,31}$")

_CACHE: dict[str, dict[str, str]] = {}


# --------------------------------------------------------------------------- config

def get_config(need_write: bool = False) -> dict[str, str]:
    """Cached credentials.  A write-capable config also satisfies later read requests."""
    if "write" in _CACHE:
        return _CACHE["write"]
    if not need_write and "read" in _CACHE:
        return _CACHE["read"]
    cfg = load_config(need_write=need_write)
    _CACHE["write" if need_write else "read"] = cfg
    return cfg


def reset_config_cache() -> None:
    _CACHE.clear()


def key_mode(cfg: dict[str, str]) -> str:
    """Which Qdrant key reads will use: read-only, write (no read-only key present), or none."""
    if cfg.get("QDRANT_READONLY_API_KEY"):
        return "read-only"
    if cfg.get("QDRANT_API_KEY"):
        return "write"
    return "none"


# --------------------------------------------------------------------------- validation

def _opt_str(name: str, value: Any) -> str | None:
    """Optional string argument: None / blank -> None; any non-str -> FleetRagError."""
    if value is None:
        return None
    if not isinstance(value, str):
        raise FleetRagError(f"{name} must be a string, not {type(value).__name__}")
    value = value.strip()
    return value or None


def _one_of(name: str, value: str | None, allowed: tuple[str, ...]) -> str | None:
    if value is not None and value not in allowed:
        raise FleetRagError(f"{name} must be one of " + "|".join(allowed) + f" (got {value!r})")
    return value


# --------------------------------------------------------------------------- search

def build_filter(category: str | None = None, app: str | None = None, source: str | None = None,
                 seat: str | None = None, since_days: int | None = None,
                 now: int | None = None) -> dict:
    """Exact-match filter on the four enumerated fields plus a created_at lower bound.

    Always excludes the ingest sentinel (source="meta"), so the result is never None.
    """
    flt = match_filter(category=category, app=app, source=source, seat=seat) or {}
    must = list(flt.get("must", []))
    if since_days is not None:
        if not isinstance(since_days, int) or isinstance(since_days, bool) or since_days <= 0:
            raise FleetRagError("since_days must be a positive integer")
        gte = (now if now is not None else now_ms()) - since_days * DAY_MS
        must.append({"key": "created_at", "range": {"gte": gte}})
    out: dict[str, Any] = {"must_not": [meta_exclude()]}
    if must:
        out["must"] = must
    return out


def _hit(raw: dict) -> dict:
    p = raw.get("payload") or {}
    out: dict[str, Any] = {"score": round(float(raw.get("score", 0.0)), 4), "text": p.get("text", "")}
    for f in HIT_FIELDS:
        out[f] = p.get(f, 0 if f in ("chunk_index", "created_at") else "")
    return out


def recall_search(query: str, limit: int = 5, category: str | None = None, app: str | None = None,
                  source: str | None = None, seat: str | None = None,
                  since_days: int | None = None) -> dict:
    """Hybrid (dense + keyword, RRF) search over the fleet-agents corpus.

    Returns {"hits": [...], "mode": "hybrid"|"dense"}.  Read-only key when available.
    """
    if not isinstance(query, str) or not query.strip():
        raise FleetRagError("query must be a non-empty string")
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= MAX_LIMIT:
        raise FleetRagError(f"limit must be an integer between 1 and {MAX_LIMIT}")
    category = _one_of("category", _opt_str("category", category), CATEGORIES)
    source = _one_of("source", _opt_str("source", source), SOURCES)
    app = _opt_str("app", app)
    seat = _opt_str("seat", seat)
    if seat:
        seat = seat.upper()
    if app:
        app = app.lower()
    flt = build_filter(category, app, source, seat, since_days)
    cfg = get_config(need_write=False)
    vector = embed(cfg, [query.strip()])[0]
    terms = query_terms(query)
    raw = Qdrant(cfg).query_hybrid(vector, terms, limit, flt)
    return {"hits": [_hit(r) for r in raw], "mode": "hybrid" if terms else "dense"}


# --------------------------------------------------------------------------- stats

def recall_stats() -> dict:
    """Collection status plus counts by source and by app.

    by_app always carries an "other" bucket (points whose app is not in KNOWN_APPS, including
    the ingest sentinel), so sum(by_app.values()) == points.
    """
    cfg = get_config(need_write=False)
    q = Qdrant(cfg)
    info = q.info()
    by_source = {s: q.count(match_filter(source=s)) for s in SOURCES}
    by_app = {}
    for a in KNOWN_APPS:
        n = q.count(match_filter(app=a))
        if n:
            by_app[a] = n
    by_app["other"] = q.count({"must_not": [{"key": "app", "match": {"any": list(KNOWN_APPS)}}]})
    return {
        "collection": q.collection,
        "status": info.get("status", "?"),
        "points": info.get("points_count", 0),
        "embedder_healthy": bool(embedder_healthy(cfg)),
        "by_source": by_source,
        "by_app": by_app,
    }


# --------------------------------------------------------------------------- contribute

def _still_secret(text: str) -> bool:
    """True when gitleaks still flags the scrubbed text.

    Fails CLOSED: if gitleaks cannot deliver a verdict (scrub.GitleaksError or any other
    exception from the gate) a FleetRagError is raised so the caller refuses the contribution.
    Only call this when gitleaks_available() is true.
    """
    path: str | None = None
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False, encoding="utf-8") as fh:
            fh.write(json.dumps({"text": text}) + "\n")
            path = fh.name
        try:
            return bool(gitleaks_flagged(path))
        except FleetRagError:
            raise
        except Exception as e:  # noqa: BLE001 - GitleaksError or anything else: refuse, class only
            raise FleetRagError("refusing: the gitleaks gate could not verify the scrubbed text "
                                f"({type(e).__name__}); nothing was stored") from None
    finally:
        if path:
            try:
                os.unlink(path)
            except OSError:
                pass


def recall_contribute(text: str, category: str, app: str = "fleet", seat: str | None = None,
                      title: str | None = None, url: str | None = None) -> dict:
    """Store one reusable lesson / preference / infrastructure fact / decision / runbook.

    Guardrails: 40..4000 chars after strip, category from CONTRIB_CATEGORIES, seat required
    (falls back to $AGENT_SEAT), secrets scrubbed and reported, refused if gitleaks still
    flags the scrubbed text or cannot run.  When gitleaks is not installed the regex scrub
    alone is applied and "gitleaks-unavailable" is appended to the returned scrubbed list.
    Requires the write key.
    """
    if not isinstance(text, str):
        raise FleetRagError("text must be a string")
    text = text.strip()
    if len(text) < CONTRIB_MIN:
        raise FleetRagError(f"text too short: {len(text)} chars (minimum {CONTRIB_MIN})")
    if len(text) > CONTRIB_MAX:
        raise FleetRagError(f"text too long: {len(text)} chars (maximum {CONTRIB_MAX})")
    if not isinstance(category, str):
        raise FleetRagError(f"category must be a string, not {type(category).__name__}")
    if category not in CONTRIB_CATEGORIES:
        raise FleetRagError("category must be one of " + "|".join(CONTRIB_CATEGORIES))
    seat = (_opt_str("seat", seat) or os.environ.get("AGENT_SEAT") or "").strip().upper()
    if not seat:
        raise FleetRagError("seat is required (pass seat=... or set AGENT_SEAT)")
    if not _SEAT_RE.match(seat):
        raise FleetRagError("seat must be an uppercase tag like CLAUDE or GROK-BOT")
    app = (_opt_str("app", app) or "fleet").lower()
    if not _APP_RE.match(app):
        raise FleetRagError("app must be a lowercase slug like fleet or socratic-trade")
    title = _opt_str("title", title) or ""
    url = _opt_str("url", url) or ""
    if url and not re.match(r"^https?://", url):
        raise FleetRagError("url must start with http:// or https://")

    clean, kinds = scrub(text)
    reported = list(kinds)
    if gitleaks_available():
        if _still_secret(clean):
            raise FleetRagError("refusing: text still looks like it contains a secret after scrubbing")
    else:
        reported.append(GITLEAKS_UNAVAILABLE)

    cfg = get_config(need_write=True)
    ts = now_ms()
    day = datetime.datetime.fromtimestamp(ts / 1000, datetime.timezone.utc).strftime("%Y-%m-%d")
    doc_id = f"contrib/{seat}/{day}/{content_hash(clean)[:8]}"
    payload: dict[str, Any] = {
        "source": "agent-contribution",
        "app": app,
        "category": category,
        "seat": seat,
        "doc_id": doc_id,
        "chunk_index": 0,
        "chunk_count": 1,
        "heading": "",
        "title": title,
        "url": url,
        "path": "",
        "created_at": ts,
        "updated_at": ts,
        "ingest_run": f"contrib-{day}",
    }
    if kinds:
        payload["scrubbed"] = kinds
    point = build_point(clean, payload)
    point["vector"] = embed(cfg, [clean])[0]
    status = Qdrant(cfg).upsert([point])
    return {"id": point["id"], "doc_id": doc_id, "scrubbed": reported, "status": status}


# --------------------------------------------------------------------------- fake backend

class FakeQdrant:
    """In-memory stand-in with the subset of core.Qdrant the recall functions use.

    The store is class-level so a server process and its tests see one collection.  Every
    query_hybrid / search_dense call is appended to `calls` as (vector, terms, limit, filter).
    Filters support must / must_not / should, nested filters, match value / any / text, and
    range gte, which is the subset the recall functions and core.Qdrant.query_hybrid emit.
    """

    points: list[dict] = []
    calls: list[tuple] = []
    upserts: list[list[dict]] = []

    def __init__(self, cfg: dict[str, str], collection: str | None = None):
        self.collection = collection or cfg.get("QDRANT_FLEET_COLLECTION", "fleet-agents-fake")

    @classmethod
    def reset(cls, seed: bool = True) -> None:
        cls.points, cls.calls, cls.upserts = [], [], []
        if seed:
            cls.points.extend(_fake_seed())

    def healthz(self) -> bool:
        return True

    def info(self) -> dict:
        return {"status": "green", "points_count": len(self.points), "payload_schema": {}}

    @classmethod
    def _cond(cls, p: dict, cond: dict) -> bool:
        if any(k in cond for k in ("must", "must_not", "should")):
            return cls._matches(p, cond)
        val = p["payload"].get(cond.get("key"))
        if "match" in cond:
            m = cond["match"]
            if "value" in m:
                return val == m["value"]
            if "any" in m:
                return val in m["any"]
            if "text" in m:
                return str(m["text"]).lower() in str(val or "").lower()
        if "range" in cond:
            return isinstance(val, (int, float)) and val >= cond["range"]["gte"]
        return True

    @classmethod
    def _matches(cls, p: dict, flt: dict | None) -> bool:
        if not flt:
            return True
        if not all(cls._cond(p, c) for c in flt.get("must", [])):
            return False
        if any(cls._cond(p, c) for c in flt.get("must_not", [])):
            return False
        should = flt.get("should") or []
        return not should or any(cls._cond(p, c) for c in should)

    def count(self, flt: dict | None = None, exact: bool = True) -> int:
        return sum(1 for p in self.points if self._matches(p, flt))

    def search_dense(self, vector: list[float], limit: int = 5, flt: dict | None = None) -> list[dict]:
        return self.query_hybrid(vector, [], limit, flt)

    def query_hybrid(self, vector: list[float], terms: list[str], limit: int = 5,
                     flt: dict | None = None, prefetch_limit: int | None = None) -> list[dict]:
        FakeQdrant.calls.append((vector, terms, limit, flt))
        scored = []
        for p in self.points:
            if not self._matches(p, flt):
                continue
            low = p["payload"].get("text", "").lower()
            overlap = sum(1 for t in terms if t in low)
            scored.append({"id": p["id"], "score": round(0.5 + 0.1 * overlap, 4), "payload": p["payload"]})
        scored.sort(key=lambda h: -h["score"])
        return scored[:limit]

    def upsert(self, points: list[dict], wait: bool = True) -> str:
        FakeQdrant.upserts.append(points)
        ids = {p["id"] for p in points}
        FakeQdrant.points = [p for p in self.points if p["id"] not in ids] + [
            {"id": p["id"], "payload": p["payload"]} for p in points]
        return "completed"


def _fake_seed() -> list[dict]:
    rows = [
        ("Never grep, cat, or Read ~/.secrets/global-api-keys for KEY=value lines - that prints "
         "secret values into the transcript.  List names only.", "preference", "fleet"),
        ("The fleet vector database runs as Coolify service qdrant-st on the shared Hetzner box, "
         "bound to the Tailscale mesh address on port 6333.", "infrastructure", "fleet"),
        ("Commit and land finished work without waiting to be asked; unpushed work is invisible "
         "to peer agents and gets redone.", "preference", "fleet"),
    ]
    out = []
    for i, (text, cat, app) in enumerate(rows):
        pt = build_point(text, {"source": "doc", "app": app, "category": cat, "seat": "CLAUDE",
                                "doc_id": "seed/fleet-standards", "chunk_index": i, "chunk_count": 1,
                                "heading": "", "title": "Fleet standards seed", "url": "", "path": "",
                                "created_at": 1756684800000, "updated_at": 1756684800000,
                                "ingest_run": "fake"})
        out.append({"id": pt["id"], "payload": pt["payload"]})
    return out


def install_fake_backend(seed: bool = True) -> None:
    """Point every seam at in-process fakes (no network, no credentials, no gitleaks)."""
    global load_config, embed, embedder_healthy, Qdrant, gitleaks_flagged, gitleaks_available
    FakeQdrant.reset(seed=seed)
    load_config = lambda need_write=False, extra=(): {  # noqa: E731
        "TEI_URL": "http://fake", "TEI_API_KEY": "fake", "QDRANT_URL": "http://fake",
        "QDRANT_FLEET_COLLECTION": "fleet-agents-fake", "QDRANT_API_KEY": "fake",
        "QDRANT_READONLY_API_KEY": "fake"}
    embed = lambda cfg, texts: [[0.0] * 4 for _ in texts]  # noqa: E731
    embedder_healthy = lambda cfg: True  # noqa: E731
    Qdrant = FakeQdrant
    gitleaks_flagged = lambda path, timeout=300: set()  # noqa: E731
    gitleaks_available = lambda: True  # noqa: E731
    reset_config_cache()
