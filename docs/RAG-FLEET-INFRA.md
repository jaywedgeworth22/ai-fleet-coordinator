# Fleet RAG infrastructure — self-hosted embeddings + the shared agent memory

Owner-directed 2026-08-31 (stand-up, board `7dbd6228`) and 2026-09-01 (make it fully operational
and reachable from every platform, boards `17f4547c` `9c75471c` `c799b564` `0f9a13b1`), CLAUDE
seat.  This is the knowledge layer described as "Plan B" in
`docs/reviews/2026-08-27-fleet-ops-review.md`: one place every agent, on every platform, can look
up lessons learned, owner preferences, how the infrastructure is wired, and what a past board row
resolved — and contribute to — instead of bulk-loading every protocol document into every session.

Both services run on the shared Hetzner box (`host.jays.services`, 16 vCPU / 30 GiB) as Coolify
services, bound to the Tailscale mesh only.  Neither is reachable from the public interface.

## What exists

| Service | Coolify UUID | Endpoint (mesh only) | Caps | Auth |
|---|---|---|---|---|
| `qdrant-st` | `ookh0qmlgrbxlwbbe6lolx6g` | `http://100.69.77.26:6333` | 4 CPU / 12 GiB | `api-key` header (write key, or the read-only key for reads) |
| `tei-bge-m3` | `cday9viyj6mwlfr8egnoknoa` | `http://100.69.77.26:8081` | 6 CPU / 10 GiB | `Authorization: Bearer` |

`tei-bge-m3` is Hugging Face `text-embeddings-inference:cpu-1.8` serving `BAAI/bge-m3`
(1024-dim, CLS pooling, L2-normalized) on CPU via the ONNX backend.  Despite the name,
`qdrant-st` hosts two collections and is no longer ST-only.

### Collections

| Collection | Points | Purpose |
|---|---|---|
| `socratic-trade` | ~801k | ST RAG, copied from Pinecone.  Embedded by **OpenRouter** `baai/bge-m3`.  **Serving ST production reads since 2026-08-31** (board `9e19673a`, stage 1 read-path cutover). |
| `fleet-agents` | grows nightly | The shared agent memory.  Embedded by the **self-hosted** endpoint. |

`fleet-agents` is 1024-dim cosine, vectors in RAM, with payload indexes on `source`, `app`,
`category`, `seat`, `doc_id`, `content_hash`, `created_at`, and a full-text index on `text` so
keyword and vector search are fused (see *Search*).

### Payload schema (v2)

Every point carries:

```jsonc
{
  "text":         "[Title › Section]\nthe chunk",
  "source":       "board | effort-log | apple-note | doc | skill | memory | chat-log | agent-contribution | meta",
  "app":          "fleet | socratic-trade | congress-trade | usage-monitor | dealdex | botfleet | ...",
  "category":     "lesson | preference | infrastructure | decision | runbook | finding | note | doc",
  "seat":         "CLAUDE | MONET | GROK | CODEX | AG | CURSOR | OWNER | FLEET",
  "doc_id":       "board/<uuid> | note/<id> | doc/<repo>/<path> | effort-log/<APP> | memory/<seat>/<file> | skill/<name> | chat/<platform>/<id>[#partN] | contrib/<SEAT>/<date>/<hash8>",
  "chunk_index":  0, "chunk_count": 3,
  "heading":      "Title › Section", "title": "...", "url": "https://...", "path": "/Users/jay/...",
  "created_at":   1788213600000, "updated_at": 1788213600000,
  "content_hash": "sha256 of text", "embed_model": "BAAI/bge-m3-selfhosted",
  "ingest_run":   "20260901T203000Z", "scrubbed": ["github-token"]
}
```

Point ids are `uuid5` over the content hash, so identical text anywhere collapses to one point
and re-ingesting unchanged content is a no-op.  One extra point, `doc_id = meta/ingest-status`
(`source = meta`), is the ingest sentinel described under *Health rows*; search excludes it.

## Sources (what gets ingested)

| Source | Where it comes from | Notes |
|---|---|---|
| `board` | `~/apps/mac-collab/findings.db` (title, body, resolution, status, severity, comments) | category `lesson` when resolved, else `finding`; url is the board |
| `apple-note` | every note in the iCloud folder **Coding**, exported by AppleScript without stealing focus, cached by modification date | app and seat parsed from the `[APP, Agent]` title convention |
| `doc` | markdown in fleet app repos under `~/Code` (`README.md`, `AGENTS.md`, `STATUS.md`, `CLAUDE.md`, `docs/**/*.md`), plus the broader walk of ai-fleet-coordinator and fleet-ops, top-level `~/apps/*.md` except effort logs, `~/.claude/CLAUDE.md`, `~/.grok/docs/**/*.md`, and `~/.grok/skills/**/SKILL.md` | GitHub blob URL when the file is in a repo.  Skip `node_modules`, `.git`, backups, dist, build, vendor, and `reviews/raw`.  Deduped by resolved path. |
| `effort-log` | `~/apps/*-EFFORT-LOG.md` and the protocol | one doc per file, app from the filename |
| `skill` | `~/.claude/skills/*/SKILL.md`, `~/.cursor/skills/*/SKILL.md` | deduped by content |
| `memory` | `~/.claude/projects/*/memory/*.md`, `~/.codex/memories/*.md` | the per-seat silos, so their lessons are shared |
| `chat-log` | parsed agent transcripts: Claude `~/.claude/projects/**/*.jsonl`, Grok `~/.grok/sessions/**/chat_history.jsonl` (and `transcript.md` if jsonl is missing), Cursor `~/.cursor/projects/**/agent-transcripts/**/*.jsonl`, Codex `~/.codex/sessions/**/*.jsonl`, Gemini `~/.gemini/**/*.jsonl` when the file is a chat | User and assistant text only.  Skip tool results, queue-operation, mode-only lines, events.jsonl, permission toml, system_prompt.txt, lock files, and `~/.secrets`.  One Doc per session under ~80k chars, else `chat/<platform>/<id>#partN`.  Category `preference` when the chunk is clearly an owner ruling, else `lesson`. |
| `agent-contribution` | `recall contribute` / `recall_contribute` | scrubbed, gitleaks-gated, 40–4,000 chars |

Every chunk goes through the secret scrub (`scripts/fleet_rag/scrub.py`: well-known token shapes,
assignment patterns, basic-auth URLs) and then a gitleaks gate over the staged rows; anything
gitleaks still flags is dropped and counted in the run report.  Documents are chunked with a
markdown-aware chunker (~1,600 chars, 200 overlap, heading trail prepended) so a fragment still
carries its section context.

## Search

Hybrid: the query is embedded, and Qdrant's Query API fuses two prefetches with reciprocal
rank fusion — plain dense, and dense restricted to points whose full-text index matches any of
the query's keyword terms.  Filters on `category` / `app` / `source` / `seat` and a `since_days`
window are exact-match payload filters.  A golden set (`scripts/fleet_rag/golden.jsonl`) and
`recall eval` report Recall@1 / Recall@5 / MRR so drift is measurable.

## Using it

### From a Mac seat (Claude, Codex, Cursor, Grok, Antigravity, Monet)

The `fleet-recall` MCP server is registered in every CLI's global MCP config by
`scripts/install-fleet-rag.sh` (stdio, `python3 ~/apps/fleet-rag/fleet-recall-mcp.py`, no
tokens in any config file).  Tools:

- `recall_search(query, limit=5, category?, app?, source?, seat?, since_days?)`
- `recall_contribute(text, category, app="fleet", seat, title?, url?)`
- `recall_stats()`

The CLI is `recall`, on PATH through `~/.local/bin/recall` (and `~/apps/mac-collab/recall`) like `board`:

```bash
recall "pm2 orphan holds port"                       # ranked hits with source, date, board id / url
recall "rotate the Coolify token" --app fleet --limit 3 --since-days 60
recall contribute "TEI warmup memory scales with --max-batch-tokens; 4096 under 10 GiB is stable." --category lesson --app fleet
recall stats            # points, by source / app, embedder health
recall doctor           # credentials found (names only), key mode, service health
recall eval --k 5       # golden-set retrieval quality
recall ingest --all     # what the nightly routine runs (idempotent, resumable)
```

`scripts/fleet-rag.py` remains as the thin compatibility CLI (`stats` / `search` / `ingest`).

### From BotFleet bots

BotFleet's Claude driver imports `~/.claude.json` `mcpServers`, and the Codex and Grok drivers
read their CLIs' global configs, so Mac-side bots get the three tools once the installer has
run.  Oracle owns the ongoing work (see *Routines*).

iOS / a phone / a bot that is not on this Mac should use the public hop below, not stdio
Python.  Do not paste Infisical keys into a BotFleet room.

### From any other device (cloud seats, phone, Claude Code Cloud, Cursor cloud)

`seat-mcp` is the public hop.  Cloudflare Access + bearer.  Health is public;
tools require `Authorization: Bearer` (`SEAT_MCP_TOKEN`) and the Access service-token
headers when you are not already on the Mac.

| Surface | How |
|---|---|
| Mac CLI (Claude, Codex, Cursor, Grok, AG, Monet) | stdio MCP `fleet-recall` (installer) or `recall` CLI |
| BotFleet on this Mac | inherits that stdio MCP from the engine config |
| Cursor cloud / Claude Code Cloud / Grok Bot | remote MCP `https://agents.jays.services/mcp` — see `scripts/seat-mcp/mcp.example.json` |
| Anything that can HTTP | REST: `GET https://agents.jays.services/recall/stats`, `POST .../recall/search`, `POST .../recall/contribute` (same auth) |
| iOS BotFleet | same REST or remote MCP; the companion talks to the Mac harness when the Mac is the computer, otherwise the public hop |

MCP tools on `/mcp`: `recall_search`, `recall_stats`, `recall_contribute` (`seat` is required
for contributions).  REST bodies are the same JSON as the MCP arguments.  The process still
runs on the Mac and reaches Qdrant over Tailscale.  If the Mac is asleep, cloud/phone RAG
waits; a Hetzner sidecar is the follow-up so that hop is not load-bearing.

```bash
# REST, from any network that can reach agents.jays.services
curl -sS https://agents.jays.services/recall/stats \
  -H "Authorization: Bearer $SEAT_MCP_TOKEN" \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET"

curl -sS https://agents.jays.services/recall/search \
  -H "Authorization: Bearer $SEAT_MCP_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query":"handoff file grep trap","limit":3}'
```

## Credentials

Canonical in **Infisical shared / prod** (project `18f563a3-9c88-454c-96eb-28fc9678f3ba`):
`TEI_URL`, `TEI_API_KEY`, `TEI_EMBED_MODEL`, `QDRANT_URL`, `QDRANT_API_KEY`,
`QDRANT_READONLY_API_KEY`, `QDRANT_FLEET_COLLECTION`.  Coolify holds synced copies; Infisical is
the source of truth per the standing rule.

- **Read/write split.**  `QDRANT_READONLY_API_KEY` is loaded by `qdrant-st` as
  `QDRANT__SERVICE__READ_ONLY_API_KEY` and is what search / stats / eval use.  Only ingest and
  `contribute` use the write key.  Until the service has restarted with the new key, the client
  falls back to the write key on a 401/403 so reads never break.
- Every client loads credentials from the environment first, then from Infisical via the machine
  identity in `~/.secrets/global-api-keys`.  Values are never printed.

ST keeps its own `QDRANT_URL` / `QDRANT_API_KEY` in the ST project for the app runtime.  Rotating
the Qdrant write key means updating both places.

## Routines (BotFleet bot Oracle, owner direction 2026-09-01)

| Routine | Schedule | What it does |
|---|---|---|
| Fleet RAG nightly ingest | daily 02:30 local | `recall ingest --all`, reads `~/apps/fleet-rag/state/last-run.json`, retries once, files a P1 on the board on repeated failure |
| Fleet RAG weekly health + recall eval | Sundays 06:30 local | `recall doctor` / `stats` / `eval`, confirms yesterday's snapshot exists locally and in B2, files a P1 on regressions |

Routines live in `~/.botfleet/routines.json` and are managed through BotFleet's loopback API
(`POST http://127.0.0.1:8799/api/routines`).  Create payload: `name`, `prompt`, `botId`
(Oracle `79a3a7f8-e35f-4604-9e41-54e4af28c04a`), `runOn: maus`, `schedule`, `durationMinutes`.

## Backup

`/etc/cron.d/fleet-qdrant` on the box runs `/usr/local/sbin/fleet-qdrant-snapshot.sh` daily at
03:20 UTC (tracked here under `scripts/hetzner/`).  It asks Qdrant for a consistent snapshot of
each collection, moves the file off the storage volume to `/data/backups/qdrant/<collection>/`,
checksums it, copies it to Backblaze B2 (`jays-socratic-trade-eu/qdrant/socratic-trade`,
`jays-fleet-shared-eu/qdrant/fleet-agents`), keeps two locally and fourteen days remotely.  The
API key is read from the running container's environment at run time and never written to disk.
A full `socratic-trade` snapshot is ~6.4 GB and takes about a minute to create.

## Health rows

`/usr/local/sbin/fleet-health-verify.sh` (every 15 minutes, pages through the existing
rate-limited Pushover path on FAIL) now calls `fleet-qdrant-health.sh`, which fails when:

- the latest local snapshot of either collection is older than 36 hours, or
- the **ingest sentinel** (`doc_id = meta/ingest-status`, written by every ingest run with
  `updated_at` and `ok`) is older than 30 hours or its last run failed.

The sentinel is the dead-man switch for the Oracle routine: if BotFleet stops running it, the
box pages.  No credential leaves the box for this check.

## Measured behavior

Steady state on 6 vCPU, verified 2026-08-31:

- Single query embed: **120–300 ms**.
- Batched short texts: **~24 texts/sec** (the ONNX backend caps a batch at 8 requests).
- First boot downloads ~2.3 GB of ONNX weights and takes **~9 minutes** to become healthy.
  The weights persist in the `/var/lib/tei-data` bind mount, so redeploys start in ~30 s.
- Resident usage once warm: ~5.7 GiB of its 10 GiB cap, including page cache for the model.

Bulk re-embedding is the one workload to keep off this box: at ~24 texts/sec, re-embedding
the ~800k-vector ST corpus would run for roughly half a day while competing with the
money-path apps for cores.  The nightly fleet ingest only embeds changed chunks.

## Important: the self-hosted endpoint is NOT a drop-in for the ST corpus

Measured before deployment, comparing self-hosted vectors against stored `socratic-trade`
vectors for the identical payload text:

- cosine similarity mean **0.869**, min **0.685** (mismatched-pair control: 0.478)
- self-retrieval with a self-hosted query vector: **Recall@1 64%**, Recall@5 84%
- the same test using the stored vector itself: **Recall@1 88%** (the ceiling is below 100%
  because the corpus contains near-duplicate boilerplate chunks)

So self-hosted `bge-m3` produces vectors in a *related but different* space from whatever
OpenRouter actually serves under `baai/bge-m3`.  Pointing ST queries at this endpoint would
cost roughly a quarter of Recall@1 against the existing corpus.  Tracked as board `b99cba29`.

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
- Inputs longer than 4096 tokens are truncated rather than split by TEI; the chunker keeps
  every chunk far below that.
- `/health` is intentionally unauthenticated so Coolify and uptime probes can reach it.
  `/embed` and `/v1/embeddings` require the bearer token.
- Coolify's `${SERVICE_PASSWORD_*}` magic interpolates inside `environment:` but **not**
  inside `command:` — a key passed as a command flag silently becomes an empty string, which
  disables auth.  Pass it as `API_KEY=${SERVICE_PASSWORD_TEIKEY}` in `environment:` instead.
- Qdrant restarts cold: the first deep ST queries after a restart can hit the 15 s timeout
  (bounded, `lookup_failed`); `QDRANT_QUERY_TIMEOUT_MS=60000` is set on ST for that reason.
  Restart `qdrant-st` outside market hours only.

## Files

- `scripts/fleet_rag/` — `core` (creds, embed, Qdrant client), `scrub`, `chunk`, `sources`,
  `ingest`, `notes_export`, `recall_api`, `health`, `eval`, `golden.jsonl`, `tests/`
- `scripts/recall` — the CLI; `scripts/fleet-recall-mcp.py` — the stdio MCP server
- `scripts/fleet-rag.py` — compatibility CLI
- `scripts/install-fleet-rag.sh` — installs to `~/apps/fleet-rag`, symlinks `recall`, registers
  the MCP server in every CLI config (`--dry-run`, `--uninstall`, `--with-seat-mcp`)
- `scripts/seat-mcp/seat_mcp/recall_bridge.py` — the cloud-facing tools
- `scripts/hetzner/fleet-qdrant-snapshot.sh`, `fleet-qdrant-health.sh`, `fleet-qdrant.cron`
- `docs/fleet-skills/fleet-recall/SKILL.md` — the skill every seat loads
