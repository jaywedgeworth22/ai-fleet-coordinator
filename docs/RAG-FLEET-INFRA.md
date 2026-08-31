# Fleet RAG infrastructure — self-hosted embeddings + agent vector store

Owner-directed 2026-08-31 (CLAUDE seat, board `7dbd6228`).  This is the knowledge layer
described as "Plan B" in `docs/reviews/2026-08-27-fleet-ops-review.md`: a place for agents
to look up lessons learned, owner preferences, and how our infrastructure is wired, instead
of bulk-loading every protocol document into every session.

Both services run on the shared Hetzner box (16 vCPU / 30 GiB, AMD EPYC Rome) as Coolify
services, bound to the Tailscale mesh only.  Neither is reachable from the public interface.

## What exists

| Service | Coolify UUID | Endpoint (mesh only) | Caps | Auth |
|---|---|---|---|---|
| `qdrant-st` | `ookh0qmlgrbxlwbbe6lolx6g` | `http://100.69.77.26:6333` | 3 CPU / 10 GiB | `api-key` header |
| `tei-bge-m3` | `cday9viyj6mwlfr8egnoknoa` | `http://100.69.77.26:8081` | 6 CPU / 10 GiB | `Authorization: Bearer` |

`tei-bge-m3` is Hugging Face `text-embeddings-inference:cpu-1.8` serving `BAAI/bge-m3`
(1024-dim, CLS pooling, L2-normalized) on CPU via the ONNX backend.  Despite the name,
`qdrant-st` now hosts two collections and is no longer ST-only.

### Collections

| Collection | Points | Purpose |
|---|---|---|
| `socratic-trade` | ~801k | ST RAG mirror copied from Pinecone.  Embedded by **OpenRouter** `baai/bge-m3`.  Read-path only; Pinecone still serves production retrieval. |
| `fleet-agents` | seeded | Agent knowledge: lessons, preferences, infrastructure.  Embedded by the **self-hosted** endpoint. |

`fleet-agents` is 1024-dim cosine, vectors in RAM (the corpus is small), with payload
indexes on `source`, `app`, `category`, `seat`, `doc_id`, `content_hash`, `created_at`, and
a full-text index on `text` so keyword and vector search can be combined.

Suggested payload convention:

```jsonc
{
  "text":        "the chunk",
  "source":      "board | effort-log | apple-note | doc | slack | github-issue",
  "app":         "fleet | socratic-trade | congress-trade | ...",
  "category":    "lesson | preference | infrastructure | decision | runbook",
  "seat":        "CLAUDE | MONET | GROK | CODEX | ...",
  "doc_id":      "stable id of the source document",
  "content_hash":"sha256 of text, also the basis for the point id",
  "created_at":  1756684800000
}
```

Point ids are `uuid5` over the content hash, so re-ingesting unchanged content is idempotent.

## Credentials

Canonical in **Infisical shared / prod**: `TEI_URL`, `TEI_API_KEY`, `TEI_EMBED_MODEL`,
`QDRANT_URL`, `QDRANT_API_KEY`, `QDRANT_FLEET_COLLECTION`.  Coolify generated the two API
keys and holds synced copies; Infisical is the source of truth per the standing rule.

> The shared Infisical project id is **`18f563a3-9c88-454c-96eb-28fc9678f3ba`**.  The id
> previously recorded in `fleet-ops:ATTACK-MAP.md` was stale and 404s for every machine
> identity — corrected in that repo alongside this change.

ST keeps its own `QDRANT_URL` / `QDRANT_API_KEY` in the ST project for the app runtime.
Rotating the Qdrant key means updating both places.

## Using it

`scripts/fleet-rag.py` loads credentials from the environment, falling back to Infisical
shared/prod via the machine identity in `~/.secrets/global-api-keys`.

```bash
python3 scripts/fleet-rag.py stats
python3 scripts/fleet-rag.py search "how do I avoid leaking credentials?" --limit 5
python3 scripts/fleet-rag.py search "vector database" --category infrastructure
python3 scripts/fleet-rag.py ingest notes.jsonl --source doc --app fleet --category lesson
```

`ingest` takes JSON Lines with at least a `text` field; any of the payload fields above may
be set per line and override the command-line defaults.

## Measured behavior

Steady state on 6 vCPU, verified 2026-08-31:

- Single query embed: **120–300 ms**.
- Batched short texts: **~24 texts/sec** (the ONNX backend caps a batch at 8 requests).
- First boot downloads ~2.3 GB of ONNX weights and takes **~9 minutes** to become healthy.
  The weights persist in the `/var/lib/tei-data` bind mount, so redeploys start in ~30 s.
- Resident usage once warm: ~5.7 GiB of its 10 GiB cap, including page cache for the model.

Bulk re-embedding is the one workload to keep off this box: at ~24 texts/sec, re-embedding
the ~800k-vector ST corpus would run for roughly half a day while competing with the
money-path apps for cores.

## Important: the self-hosted endpoint is NOT a drop-in for the ST corpus

Measured before deployment, comparing self-hosted vectors against stored `socratic-trade`
vectors for the identical payload text:

- cosine similarity mean **0.869**, min **0.685** (mismatched-pair control: 0.478)
- self-retrieval with a self-hosted query vector: **Recall@1 64%**, Recall@5 84%
- the same test using the stored vector itself: **Recall@1 88%** (the ceiling is below 100%
  because the corpus contains near-duplicate boilerplate chunks)

So self-hosted `bge-m3` produces vectors in a *related but different* space from whatever
OpenRouter actually serves under `baai/bge-m3`.  Pointing ST queries at this endpoint would
cost roughly a quarter of Recall@1 against the existing corpus.

Consequences:

1. **`fleet-agents` is unaffected** — that corpus is embedded and queried entirely by this
   endpoint, so it is internally consistent and carries no migration risk.
2. **Do not swap ST's embedding provider to this endpoint** without re-embedding the full
   corpus and passing the Recall@8 gate.  ST's `embedSpaceFilterForModel` would also need
   the new model id added to the bge lineage, or every existing vector becomes invisible.
3. The root cause was not isolated.  Both candidates remain open: the ONNX export in the
   `BAAI/bge-m3` repo may differ from the reference weights, or the text stored in the
   payload may not be byte-identical to what was originally sent to the embedder.

## Operational notes

- **Warmup is the memory peak, and it scales with `--max-batch-tokens`.**  At 8192 tokens
  the container was OOM-killed at warmup under an 8 GiB limit, exiting cleanly enough
  (code 137, `OOMKilled=true`) that it looked like a crash loop.  4096 tokens under a
  10 GiB limit is stable.  Raising `--max-batch-tokens` again means raising the cap too.
- Inputs longer than 4096 tokens will be rejected rather than split; `--auto-truncate` is on,
  so over-length single inputs are truncated instead of erroring.
- `/health` is intentionally unauthenticated so Coolify and uptime probes can reach it.
  `/embed` and `/v1/embeddings` require the bearer token.
- Coolify's `${SERVICE_PASSWORD_*}` magic interpolates inside `environment:` but **not**
  inside `command:` — a key passed as a command flag silently becomes an empty string, which
  disables auth.  Pass it as `API_KEY=${SERVICE_PASSWORD_TEIKEY}` in `environment:` instead.

## Not done yet

- Full Plan B ingest (findings.db, the Apple Notes archive, fleet protocol docs).  The
  collection is created and seeded with eight standards entries as a smoke test only.
- A `fleet-recall` MCP server registered in BotFleet's default bot config, so every seat can
  query without shelling out.
- Hybrid search.  The full-text index on `text` exists but `fleet-rag.py` currently issues
  dense-only queries.
- Snapshot/backup cron for the `fleet-agents` collection.
