#!/usr/bin/env bash
# Start pm2 dsh-web if http://127.0.0.1:3080 is down.  No Terminal, no browser.
set -euo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
URL="${DSH_WEB_URL:-http://127.0.0.1:3080/}"
ECO="${HOME}/apps/pm2-ecosystem.config.cjs"
LOG="${HOME}/Library/Logs/dsh-harness-open.log"
mkdir -p "$(dirname "$LOG")"

up() { curl -sf -o /dev/null --max-time 2 "$URL"; }
up && exit 0

{
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ensure-web starting dsh-web"
  if [[ -f "$ECO" ]] && command -v pm2 >/dev/null 2>&1; then
    pm2 start "$ECO" --only dsh-web --update-env || true
  fi
  if ! up && [[ -x "${HOME}/apps/dsh-runtime/start-web.sh" ]]; then
    nohup "${HOME}/apps/dsh-runtime/start-web.sh" >>"$LOG" 2>&1 &
  fi
} >>"$LOG" 2>&1

for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
  up && exit 0
  sleep 0.4
done
exit 1
