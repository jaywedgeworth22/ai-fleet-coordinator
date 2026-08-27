# grok-acp-runtime

Always-on **localhost-only** Grok ACP.

- `pm2 grok-leader` — shared backend, `~/.grok/leader.sock`, `--always-approve --no-exit-on-disconnect`.  When a TUI already holds the socket, `leader.sh` exits 75 and pm2 parks the job `stopped` (`stop_exit_codes: [75]`).  Do not `pm2 restart grok-leader` while `/usr/sbin/lsof ~/.grok/leader.sock` shows a live grok.
- `pm2 grok-acp` — WebSocket `127.0.0.1:12419` (`--no-leader serve`).  `--leader serve` does **not** bind a port.
- Shellular Grok Build: `~/.grok/bin/grok agent --always-approve --leader stdio`
- New local `grok` TUI: `[cli] use_leader = true` in `~/.grok/config.toml`
- List/load chats: `python3 ~/apps/grok-acp-runtime/leader-client.py list`
- Drive a **live TUI** chat: `python3 ~/apps/grok-acp-runtime/grok-drive.py list` then `prompt --session-id ID --cwd DIR --prompt "…"`
- Bind is loopback only.  Never `:2419`.

Auth token lives in `~/.secrets/grok-acp.env` (`GROK_AGENT_SECRET`).
Never print it.  Clients send it as:

- `Authorization: Bearer <token>`, or
- query `?server-key=<token>`

## Conductor: start a session and send a follow-up

```bash
# 1) confirm the adapter is up
lsof -nP -iTCP:12419 -sTCP:LISTEN
pm2 show grok-acp

# 2) new session + first prompt (prints sessionId)
python3 /Users/jay/apps/grok-acp-runtime/acp-client.py new \
  --cwd /Users/jay \
  --prompt "Your first message"

# 3) follow-up on that session
python3 /Users/jay/apps/grok-acp-runtime/acp-client.py prompt \
  --session-id <SESSION_ID> \
  --prompt "Your follow-up"
```

Handshake-only check (no model turn):

```bash
python3 /Users/jay/apps/grok-acp-runtime/leader-client.py handshake
python3 /Users/jay/apps/grok-acp-runtime/leader-client.py list
python3 /Users/jay/apps/grok-acp-runtime/leader-client.py load \
  --session-id <SESSION_ID> --cwd /Users/jay/Code
python3 /Users/jay/apps/grok-acp-runtime/grok-drive.py list
python3 /Users/jay/apps/grok-acp-runtime/grok-drive.py peek \
  --session-id <SESSION_ID> --cwd /Users/jay/Code
```

`acp-client.py` is the Conductor WebSocket helper for **new** sessions on `:12419`.  It needs the `websockets` package.  Local chat control uses `leader-client.py` / `grok-drive.py` (stdio, stdlib only).  `prompt` injects into an existing TUI and does **not** set `yoloMode` on that chat.

## What this can and cannot do

- Can list every Grok session on disk and `session/load` one (always-approve).
- New TUI / Shellular Grok join the shared leader.  A TUI already running before the leader started is listed, but is not live-attached until that TUI restarts.
- Cannot screenshot a terminal.  Do not bind `:2419`.  Do not `session/load` a chat that is mid-turn in another window unless you intend to share it.

## Restart

```bash
pm2 start /Users/jay/apps/pm2-ecosystem.config.cjs --only grok-acp
pm2 save
```
