#!/bin/bash
# Always-on local Grok ACP WebSocket.  127.0.0.1 only.
# Isolated serve (`--no-leader`) so this process actually binds :12419.
# `grok agent --leader serve` does not listen; list/load of local chats
# goes through pm2 `grok-leader` + leader-client.py / Shellular `--leader stdio`.
# Bind 12419 — NOT 2419.
set -euo pipefail

SECRET_FILE="${HOME}/.secrets/grok-acp.env"
if [[ ! -f "$SECRET_FILE" ]]; then
  echo "missing $SECRET_FILE (GROK_AGENT_SECRET)" >&2
  exit 1
fi
set -a
# shellcheck disable=SC1090
source "$SECRET_FILE"
set +a
if [[ -z "${GROK_AGENT_SECRET:-}" ]]; then
  echo "GROK_AGENT_SECRET empty in $SECRET_FILE" >&2
  exit 1
fi

export GROK_DISABLE_AUTOUPDATER=1
# Conductor sessions pick MCPs per job.  Do not inherit the TUI kitchen sink
# (~/.grok/config.toml + plugins + Claude/Cursor).  Auth is a symlink only.
export GROK_CLAUDE_MCPS_ENABLED=0
export GROK_CURSOR_MCPS_ENABLED=0
export GROK_MANAGED_MCPS_ENABLED=0
HERE="$(cd "$(dirname "$0")" && pwd)"
ACP_HOME="${HERE}/acp-home"
ACP_CONFIG_SRC="${HERE}/acp-home-config.toml"
mkdir -p "$ACP_HOME"
if [[ -f "$ACP_CONFIG_SRC" ]]; then
  cp "$ACP_CONFIG_SRC" "${ACP_HOME}/config.toml"
  chmod 600 "${ACP_HOME}/config.toml" 2>/dev/null || true
fi
# Auth + folder trust from the real home.  Never copy secret files into git.
if [[ -f "${HOME}/.grok/auth.json" ]]; then
  ln -sfn "${HOME}/.grok/auth.json" "${ACP_HOME}/auth.json"
fi
if [[ -f "${HOME}/.grok/trusted_folders.toml" ]]; then
  ln -sfn "${HOME}/.grok/trusted_folders.toml" "${ACP_HOME}/trusted_folders.toml"
fi
export GROK_HOME="$ACP_HOME"

# grok prints the serve token on stderr.  Redact it before pm2 logs it.
redact() {
  /usr/bin/python3 -u -c '
import os, sys
sec = os.environ.get("GROK_AGENT_SECRET", "").encode()
for chunk in sys.stdin.buffer:
    if sec:
        chunk = chunk.replace(sec, b"<redacted>")
    sys.stdout.buffer.write(chunk)
    sys.stdout.buffer.flush()
'
}

# Stay as the pm2 parent so the redact pipe survives.  grok is the child.
# Use the native CLI, not Homebrew's node wrapper (`/opt/homebrew/bin/grok`).
# `--always-approve` is an `agent` flag, before the subcommand (not after `serve`).
/Users/jay/.grok/bin/grok agent --always-approve --no-leader serve --bind 127.0.0.1:12419 2> >(redact)
