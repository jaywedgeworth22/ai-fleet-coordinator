#!/usr/bin/env bash
# Dock / Spotlight launcher for the local DeepSeek Harness web UI.
# Never opens Terminal.app.  Reuses pm2 dsh-web on 127.0.0.1:3080.
# Tracked: ai-fleet-coordinator/scripts/dsh-runtime/open-harness.sh
set -euo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

URL="${DSH_WEB_URL:-http://127.0.0.1:3080/}"
LOG="${HOME}/Library/Logs/dsh-harness-open.log"
ECO="${HOME}/apps/pm2-ecosystem.config.cjs"
mkdir -p "$(dirname "$LOG")"

up() {
  curl -sf -o /dev/null --max-time 2 "$URL"
}

if ! up; then
  {
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) starting dsh-web"
    if [[ -f "$ECO" ]] && command -v pm2 >/dev/null 2>&1; then
      pm2 start "$ECO" --only dsh-web --update-env || true
    fi
    if ! up && [[ -x "${HOME}/apps/dsh-runtime/start-web.sh" ]]; then
      # Hidden: nohup, no tty.  start-web.sh execs dsh; do not wait on it.
      nohup "${HOME}/apps/dsh-runtime/start-web.sh" >>"$LOG" 2>&1 &
    fi
  } >>"$LOG" 2>&1
  for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
    up && break
    sleep 0.4
  done
fi

# Chrome --app is a dedicated window (no tab strip, no Terminal).
# `open -na` goes through Launch Services so it works from the Dock.
if [[ -d "/Applications/Google Chrome.app" ]]; then
  open -na "Google Chrome" --args --app="$URL"
  exit 0
fi
open "$URL"
exit 0
