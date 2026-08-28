# seat-mcp (v1.2)

Async Mac seat jobs over streamable HTTP MCP.  Not a synchronous `dsh_reply` tool.

Listen:  `127.0.0.1:8793` (`POST /mcp`).  Loopback only.  Public hop is Cloudflare Access on `https://agents.jays.services/mcp` (owner-approved 2026-08-26).  Bearer still required.  Cloud agents (Grok Bot, Cursor cloud, Claude Code Cloud) use that URL — they cannot run `grok-drive.py` on the VM.

Token:  `~/.secrets/seat-mcp.env` (`SEAT_MCP_TOKEN`).  chmod 600.  Never print it.  Never put it in `~/.shellular/agents.json` or git.

Job records:  `~/.seat-mcp/jobs/<jobId>.json` (atomic write + ring-buffered tail).  Multi-seat:  do not use `~/.dsh/mcp-jobs`.

## Tools

- `seat_launch(seat, prompt, cwd, opts)` → `{jobId}`
- `seat_status(jobId)` → `{state, elapsedMs, heartbeat, partialTail}`
- `seat_reply(jobId)` → `{text}` (optional `prompt` starts an async follow-up and returns a new `{jobId}`)
- `seat_result(jobId)` → `{text, exitCode, sessionId, stats, artifacts}`
- `grok_sessions_list` → live TUI chats (`live`, `turnState`, `pendingTool`)
- `grok_session_peek(sessionId, cwd?)` → disk `summary.json`, no `session/load`, no prompt
- `grok_session_tail(sessionId, lines?)` → last N `updates.jsonl` chunks
- `grok_session_prompt(sessionId, prompt, cwd?, from?, queue?, self?)` → `{jobId}` (seat `grok-tui`)
- `grok_session_await(sessionId, timeoutSec?)` → disk poll until idle / needs-input
- `grok_session_cancel(sessionId)` → best-effort `session/cancel` notification

Heartbeat tells working vs wedged.  Timeout kills the process GROUP, not just the parent pid.

## Seats

v1.1 implements three production seats.  Shellular has no local HTTP API:  we may read `~/.shellular/agents.json` for names, but spawning is our job.

### deepseek

`/Users/jay/apps/dsh-runtime/dsh.sh --profile headless <prompt>`

Default sandbox:  `DSH_PERMISSION_MODE=read-only`.  There is no mode parameter.  Never default `danger-full-access`.  Do not use `npx @deepseek-ai/dsh`.  Do not edit `~/.dsh/settings-headless.yaml`.

Optional `opts.effort`:

- `quick`:  temp `--patch` YAML only (`deepseek-v4-flash` / `low`)
- `deep`:  temp `--patch` YAML only (`deepseek-v4-pro` / `high`)

DSH headless is one submitted task.  It cannot resume.  `seat_reply` with a follow-up prompt starts a new one-shot with prior text stuffed.  Passing `opts.sessionId` on deepseek is an error.

### grok

Prefer the existing helper:

`/usr/bin/python3 /Users/jay/apps/grok-acp-runtime/acp-client.py new --cwd DIR --prompt "…"`

Follow-up:  `acp-client.py prompt --session-id ID --prompt "…"`.

`grok-acp` is `127.0.0.1:12419` only (never 2419).  Do not start a second serve.  If helpers are missing and a stdio spawn is required, the command is `grok agent --always-approve stdio` (flag before `stdio`).

### grok-tui

Attach to a **live Mac Grok TUI** chat via the shared leader (`leader-client.py` / `grok-drive.py`).  Requires `opts.sessionId` from `grok_sessions_list`.  Does not create a new `:12419` session.  cwd may be anywhere under `/Users/jay` (the chat already exists).  Do not set a permission mode.

### cwd

New spawns (`deepseek`, `grok`) must exist under `/Users/jay/Code` or `/Users/jay/apps`.  `grok-tui` attach may use the live chat's cwd anywhere under `/Users/jay`.  Workspace-write allowlisting waits; v1 DeepSeek is read-only.

Test adapters (not for Conductor production):  `_echo`, `_sleep`.

## Start

```bash
/Users/jay/apps/seat-mcp/start.sh
```

`ecosystem.snippet.cjs` is a pm2 fragment.  Do not `pm2 start` / `pm2 save` from a one-off dsh or npx session.

## Conductor:  curl

Load the token into the environment without printing it:

```bash
set -a
source /Users/jay/.secrets/seat-mcp.env
set +a
BASE=http://127.0.0.1:8793/mcp
AUTH="Authorization: Bearer $SEAT_MCP_TOKEN"
```

Health (no token):

```bash
curl -sS http://127.0.0.1:8793/health
```

Initialize:

```bash
curl -sS -X POST "$BASE" \
  -H "$AUTH" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-11-25","capabilities":{},"clientInfo":{"name":"conductor","version":"1"}}}'
```

Launch (returns `jobId` immediately):

```bash
curl -sS -X POST "$BASE" \
  -H "$AUTH" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"seat_launch","arguments":{"seat":"deepseek","prompt":"reply with the single word pong","cwd":"/Users/jay/apps","opts":{"effort":"quick"}}}}'
```

Status / reply / result (replace JOBID):

```bash
curl -sS -X POST "$BASE" -H "$AUTH" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"seat_status","arguments":{"jobId":"JOBID"}}}'

curl -sS -X POST "$BASE" -H "$AUTH" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"seat_reply","arguments":{"jobId":"JOBID"}}}'

curl -sS -X POST "$BASE" -H "$AUTH" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":5,"method":"tools/call","params":{"name":"seat_result","arguments":{"jobId":"JOBID"}}}'
```

Grok launch:

```bash
curl -sS -X POST "$BASE" -H "$AUTH" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":6,"method":"tools/call","params":{"name":"seat_launch","arguments":{"seat":"grok","prompt":"reply with the single word pong","cwd":"/Users/jay/apps"}}}'
```

Grok TUI attach:

```bash
curl -sS -X POST "$BASE" -H "$AUTH" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":7,"method":"tools/call","params":{"name":"grok_sessions_list","arguments":{}}}'
```

## What v1.2 does not do

- answering a TUI permission prompt from outside (surface `pendingTool`; the operator decides)
- cwd allowlist for DeepSeek workspace-write
- Shellular spawn / `npx @deepseek-ai/dsh` / TryCloudflare
- putting tokens in `mcp.json` literals (use env placeholders)

After merging AFL, refresh live copies:

```bash
bash scripts/install-grok-tui-drive.sh --restart-seat-mcp
```
