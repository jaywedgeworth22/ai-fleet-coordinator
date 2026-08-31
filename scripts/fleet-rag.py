#!/usr/bin/env python3
"""Query and ingest the fleet-agents knowledge corpus.

Credentials come from the environment when set, otherwise from Infisical shared/prod via the
machine identity in ~/.secrets/global-api-keys.  Values are never printed.

    fleet-rag.py stats
    fleet-rag.py search "how do I avoid leaking credentials?" --limit 5
    fleet-rag.py search "vector database" --category infrastructure
    fleet-rag.py ingest notes.jsonl --source doc --app fleet --category lesson

See docs/RAG-FLEET-INFRA.md.
"""
import argparse
import hashlib
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request
import uuid

INFISICAL_API = "https://app.infisical.com/api"
SHARED_PROJECT = "18f563a3-9c88-454c-96eb-28fc9678f3ba"
SHARED_ENV = "prod"
HANDOFF = pathlib.Path.home() / ".secrets" / "global-api-keys"
NAMESPACE = uuid.UUID("00000000-0000-0000-0000-00000000fee7")
NEEDED = ("TEI_URL", "TEI_API_KEY", "QDRANT_URL", "QDRANT_API_KEY", "QDRANT_FLEET_COLLECTION")


def _http(url, body=None, headers=None, method=None, timeout=180):
    req = urllib.request.Request(
        url,
        data=(json.dumps(body).encode() if body is not None else None),
        method=method or ("POST" if body is not None else "GET"),
        headers={"Content-Type": "application/json", **(headers or {})},
    )
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def _identity(prefix):
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


def load_config():
    """Environment first, then Infisical shared/prod.  Returns a dict of the NEEDED keys."""
    cfg = {k: os.environ[k] for k in NEEDED if os.environ.get(k)}
    if len(cfg) == len(NEEDED):
        return cfg
    for prefix in ("INFISICAL_SHARED", "INFISICAL_AUTOMATION"):
        cid, csec = _identity(prefix)
        if not cid or not csec:
            continue
        try:
            tok = _http(f"{INFISICAL_API}/v1/auth/universal-auth/login",
                        {"clientId": cid, "clientSecret": csec})["accessToken"]
            got = _http(f"{INFISICAL_API}/v3/secrets/raw?workspaceId={SHARED_PROJECT}"
                        f"&environment={SHARED_ENV}&secretPath=%2F",
                        headers={"Authorization": f"Bearer {tok}"})
        except (urllib.error.HTTPError, urllib.error.URLError, KeyError):
            continue
        for s in got.get("secrets", []):
            if s["secretKey"] in NEEDED:
                cfg.setdefault(s["secretKey"], s["secretValue"])
        if len(cfg) == len(NEEDED):
            return cfg
    missing = [k for k in NEEDED if k not in cfg]
    sys.exit(f"missing credentials: {', '.join(missing)} "
             f"(set them in the environment or in Infisical shared/prod)")


def embed(cfg, texts):
    out = []
    for i in range(0, len(texts), 8):           # ONNX backend caps a batch at 8
        out += _http(f"{cfg['TEI_URL'].rstrip('/')}/embed",
                     {"inputs": texts[i:i + 8], "truncate": True},
                     {"Authorization": f"Bearer {cfg['TEI_API_KEY']}"})
    return out


def qdrant(cfg, path, body=None, method=None):
    return _http(f"{cfg['QDRANT_URL'].rstrip('/')}{path}", body,
                 {"api-key": cfg["QDRANT_API_KEY"]}, method)


def cmd_stats(cfg, args):
    coll = cfg["QDRANT_FLEET_COLLECTION"]
    info = qdrant(cfg, f"/collections/{coll}")["result"]
    print(f"collection : {coll}")
    print(f"status     : {info['status']}")
    print(f"points     : {info['points_count']}")
    print(f"dimension  : {info['config']['params']['vectors']['size']} "
          f"({info['config']['params']['vectors']['distance']})")
    print(f"indexed    : {', '.join(sorted(info.get('payload_schema', {})))}")
    # /health answers 200 with an empty body, so check the status rather than parsing JSON.
    try:
        with urllib.request.urlopen(f"{cfg['TEI_URL'].rstrip('/')}/health", timeout=30) as r:
            print(f"embedder   : {'healthy' if r.status == 200 else 'status ' + str(r.status)}")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"embedder   : UNREACHABLE ({type(e).__name__})")


def cmd_search(cfg, args):
    must = []
    for field in ("category", "app", "source", "seat"):
        value = getattr(args, field)
        if value:
            must.append({"key": field, "match": {"value": value}})
    body = {"vector": embed(cfg, [args.query])[0], "limit": args.limit,
            "with_payload": True}
    if must:
        body["filter"] = {"must": must}
    hits = qdrant(cfg, f"/collections/{cfg['QDRANT_FLEET_COLLECTION']}/points/search",
                  body)["result"]
    if not hits:
        print("no matches")
        return
    for h in hits:
        p = h.get("payload", {})
        tags = "/".join(x for x in (p.get("category"), p.get("app"), p.get("source")) if x)
        print(f"\n[{h['score']:.4f}] {tags}  ({p.get('doc_id', '-')})")
        text = p.get("text", "")
        print("  " + (text if args.full else text[:400] + ("..." if len(text) > 400 else "")))


def cmd_ingest(cfg, args):
    rows = []
    with open(args.file, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                sys.exit(f"{args.file}:{n}: not valid JSON")
            if not row.get("text", "").strip():
                sys.exit(f"{args.file}:{n}: missing 'text'")
            rows.append(row)
    if not rows:
        sys.exit("nothing to ingest")

    vectors = embed(cfg, [r["text"] for r in rows])
    points = []
    for row, vec in zip(rows, vectors):
        digest = hashlib.sha256(row["text"].encode()).hexdigest()
        payload = {
            "text": row["text"],
            "source": row.get("source", args.source),
            "app": row.get("app", args.app),
            "category": row.get("category", args.category),
            "seat": row.get("seat", args.seat),
            "doc_id": row.get("doc_id", args.doc_id or pathlib.Path(args.file).stem),
            "content_hash": digest,
            "created_at": int(row.get("created_at", args.created_at)),
            "embed_model": "BAAI/bge-m3-selfhosted",
        }
        points.append({"id": str(uuid.uuid5(NAMESPACE, digest)),
                       "vector": vec, "payload": payload})

    if args.dry_run:
        print(f"would upsert {len(points)} points into "
              f"{cfg['QDRANT_FLEET_COLLECTION']} (no write performed)")
        return
    status = qdrant(cfg, f"/collections/{cfg['QDRANT_FLEET_COLLECTION']}/points?wait=true",
                    {"points": points}, method="PUT").get("status")
    print(f"upserted {len(points)} points: {status}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("stats", help="collection and embedder health")

    s = sub.add_parser("search", help="semantic search over the corpus")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=5)
    s.add_argument("--category")
    s.add_argument("--app")
    s.add_argument("--source")
    s.add_argument("--seat")
    s.add_argument("--full", action="store_true", help="print whole chunks, not excerpts")

    i = sub.add_parser("ingest", help="upsert JSON Lines rows (idempotent by content hash)")
    i.add_argument("file")
    i.add_argument("--source", default="doc")
    i.add_argument("--app", default="fleet")
    i.add_argument("--category", default="lesson")
    i.add_argument("--seat", default=os.environ.get("AGENT_SEAT", "CLAUDE"))
    i.add_argument("--doc-id", dest="doc_id")
    i.add_argument("--created-at", dest="created_at", type=int, default=0,
                   help="epoch ms; defaults to 0 so ingests stay reproducible")
    i.add_argument("--dry-run", action="store_true")

    args = ap.parse_args()
    cfg = load_config()
    {"stats": cmd_stats, "search": cmd_search, "ingest": cmd_ingest}[args.cmd](cfg, args)


if __name__ == "__main__":
    main()
