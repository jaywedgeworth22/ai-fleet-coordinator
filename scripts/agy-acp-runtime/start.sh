#!/bin/bash
# agy-acp over stdio-to-ws, loopback only.
# Packaged stdio-to-ws has no --host; the runtime dist is patched to honor
# AGY_ACP_BIND (default 127.0.0.1). Public acp.jays.services is Access-wrapped.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
export AGY_ACP_BIND="${AGY_ACP_BIND:-127.0.0.1}"
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
exec /opt/homebrew/bin/node "$ROOT/node_modules/.bin/stdio-to-ws" \
  --persist --grace-period 604800 --port "${AGY_ACP_PORT:-8765}" \
  /usr/local/bin/agy-acp
