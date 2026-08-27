---
name: drive-grok-tui
description: Drive live Mac Grok TUI sessions from Grok Bot (Cursor cloud [GB-<NAME>] seats) or local Cursor. List chats on the shared leader, peek, and inject a follow-up via seat-mcp. Use when a GB seat must steer a Mac Grok terminal, attach to an existing grok TUI, or send a prompt into a session with live=true.
---

# Drive Mac Grok TUI sessions

Mac Grok TUI (`[GROK]`) chats join `~/.grok/leader.sock`.  Grok Bot does **not**
spawn a second `grok-acp` on `:12419` to talk to those chats.  Attach through
seat-mcp.

## Tools (preferred)

HTTP MCP: `https://agents.jays.services/mcp` (Cloudflare Access service token
**and** `Authorization: Bearer $SEAT_MCP_TOKEN`).  Local: `http://127.0.0.1:8793/mcp`
with Bearer only.

Never put tokens in git or in `mcp.json` literals.  Cloud: Cursor dashboard env
`SEAT_MCP_TOKEN`, `CF_ACCESS_CLIENT_ID`, `CF_ACCESS_CLIENT_SECRET` from
`~/.secrets/seat-mcp.env` and `~/.secrets/agents-jays-services-access-service-token.env`
(names only; never print values).

1. `grok_sessions_list` — rows with `live=true` are the current TUI.
2. `grok_session_prompt` `{sessionId, prompt, cwd?}` → `{jobId}`.
3. `seat_status` / `seat_result` until `succeeded` / `failed` / `timeout`.
4. Optional `grok_session_peek` — load, no prompt.

`seat_launch` with `seat: "grok-tui"` and `opts.sessionId` is the same attach.
`seat: "grok"` is a **new** session on `:12419`, not the TUI.

## CLI on the Mac

```bash
python3 ~/apps/grok-acp-runtime/grok-drive.py list
python3 ~/apps/grok-acp-runtime/grok-drive.py peek --session-id ID --cwd DIR
python3 ~/apps/grok-acp-runtime/grok-drive.py prompt --session-id ID --cwd DIR --prompt "..."
```

Do not start a second `grok agent serve`.  Do not bind `:2419`.  Do not
`session/load` a chat that is mid-turn unless you intend to queue.

## Cursor HTTP MCP fragment (env placeholders only)

```json
{
  "mcpServers": {
    "seat-mcp": {
      "url": "https://agents.jays.services/mcp",
      "headers": {
        "Authorization": "Bearer ${SEAT_MCP_TOKEN}",
        "CF-Access-Client-Id": "${CF_ACCESS_CLIENT_ID}",
        "CF-Access-Client-Secret": "${CF_ACCESS_CLIENT_SECRET}"
      }
    }
  }
}
```

On this Mac, `url` may be `http://127.0.0.1:8793/mcp` and the CF-Access headers
are omitted.

## Identity

Sign as your `[GB-<NAME>]` role (or `[CURSOR]` on the local IDE).  Never
`[GROK-BOT]`.  The TUI you are driving stays `[GROK]`.
