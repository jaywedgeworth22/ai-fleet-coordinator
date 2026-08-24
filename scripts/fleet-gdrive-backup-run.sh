#!/usr/bin/env bash
# Daily fleet backup: git repos + agent dotfolder skills/rules mirror.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
/usr/bin/python3 "$HERE/backup-fleet-to-gdrive.py" "$@"
/usr/bin/python3 "$HERE/sync-fleet-agent-config-to-gdrive.py"
