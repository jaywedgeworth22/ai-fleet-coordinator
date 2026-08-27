#!/bin/bash
# seat-mcp v1.  Streamable HTTP on 127.0.0.1:8793 only.
# Do not mint a tunnel.  Do not npx dsh.  Token stays in ~/.secrets/seat-mcp.env.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
SECRET="${HOME}/.secrets/seat-mcp.env"
JOBS="${HOME}/.seat-mcp/jobs"

mkdir -p "${HOME}/.secrets" "${JOBS}"
chmod 700 "${HOME}/.seat-mcp" "${JOBS}" 2>/dev/null || true

# Create the token file if missing.  Never echo the token.
/opt/homebrew/bin/python3 - <<'PY'
from pathlib import Path
import os, secrets
p = Path.home() / ".secrets" / "seat-mcp.env"
p.parent.mkdir(mode=0o700, exist_ok=True)
if not p.is_file():
    p.write_text("SEAT_MCP_TOKEN=" + secrets.token_urlsafe(32) + "\n", encoding="utf-8")
os.chmod(p, 0o600)
PY

set -a
# shellcheck disable=SC1090
source "$SECRET"
set +a
if [[ -z "${SEAT_MCP_TOKEN:-}" ]]; then
  echo "SEAT_MCP_TOKEN empty in $SECRET" >&2
  exit 1
fi

export PYTHONUNBUFFERED=1
cd "$ROOT"
exec /opt/homebrew/bin/python3 -u -m seat_mcp
