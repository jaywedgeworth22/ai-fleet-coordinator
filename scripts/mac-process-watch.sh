#!/bin/bash
# Check expected Mac always-on jobs.  Restart the ones that are down.
# Scheduled; must not stay up.  Writes only names and status - never env
# or secret values.
#
#   bash ~/apps/mac-process-watch.sh
#   MAC_PROCESS_WATCH_RESTART=0 bash ~/apps/mac-process-watch.sh   # log only
#   tail -f ~/Library/Logs/mac-process-watch.log
#
# launchd: com.jay.mac-process-watch every 120s.
# Tracked copy: ai-fleet-coordinator/scripts/mac-process-watch.sh
# Live copy launchd runs: ~/apps/mac-process-watch.sh
#
# Restarts (always-on only):
#   - pm2 daemon dead or 3+ jobs missing -> pm2 resurrect (uses ~/.pm2/dump.pm2)
#   - one/two pm2 jobs down -> pm2 restart, or pm2 start ecosystem --only
#   - launchd always-on not-loaded -> bootstrap plist (if not disabled)
#   - launchd always-on loaded, no pid -> kickstart (not -k)
# Does NOT touch: disabled labels (com.jay.shellular, com.jay.imessage-grok,
# retired launchd), scheduled/one-shot jobs, com.PM2, cloudflared (root).
# Backoff: at most 4 restarts per key per hour.  After that, log SKIP.

set -uo pipefail

LOG="${HOME}/Library/Logs/mac-process-watch.log"
CMDLOG="${HOME}/Library/Logs/mac-process-watch.cmd.log"
STATE="${HOME}/Library/Logs/mac-process-watch.state"
LOCKDIR="${HOME}/Library/Logs/mac-process-watch.lockdir"
ECOSYSTEM="${HOME}/apps/pm2-ecosystem.config.cjs"
DUMP="${HOME}/.pm2/dump.pm2"
STAMP="$(date '+%Y-%m-%d %H:%M:%S')"
NOW="$(date +%s)"
RESTART="${MAC_PROCESS_WATCH_RESTART:-1}"
MAX_RESTARTS=4
WINDOW_SEC=3600
LOCK_STALE_SEC=180
mkdir -p "$(dirname "$LOG")"

expect_pm2=(
  shellular
  scout
  senate-relay
  senate-tunnel
  agent-sync-push
  code-main-keeper
  vision-worker
  xcode-health
  cursor-slack-sync
  agy-acp
)

# "label plist-basename"  (plists live in ~/Library/LaunchAgents)
expect_launchd=(
  "com.jay.claude-remote-control com.jay.claude-remote-control.plist"
  "homebrew.mxcl.moshi-hook homebrew.mxcl.moshi-hook.plist"
  "actions.runner.jaywedgeworth22-Congress.Trade.mac-xcode26-congress actions.runner.jaywedgeworth22-Congress.Trade.mac-xcode26-congress.plist"
  "actions.runner.jaywedgeworth22-Socratic.Trade.mac-xcode26-socratic actions.runner.jaywedgeworth22-Socratic.Trade.mac-xcode26-socratic.plist"
  "actions.runner.jaywedgeworth22-Usage-Monitor.mac-xcode26-usage actions.runner.jaywedgeworth22-Usage-Monitor.mac-xcode26-usage.plist"
)

log() {
  echo "$STAMP  $*" >>"$LOG"
}

# mkdir lock.  Steal if older than LOCK_STALE_SEC (crash leftover).
if ! mkdir "$LOCKDIR" 2>/dev/null; then
  lock_mtime="$(stat -f %m "$LOCKDIR" 2>/dev/null || echo 0)"
  if [ $((NOW - lock_mtime)) -gt "$LOCK_STALE_SEC" ]; then
    rmdir "$LOCKDIR" 2>/dev/null || true
    if ! mkdir "$LOCKDIR" 2>/dev/null; then
      exit 0
    fi
  else
    exit 0
  fi
fi
trap 'rmdir "$LOCKDIR" 2>/dev/null || true' EXIT

# Return 0 if this key may restart; increment count.  1 = backoff.
allow_restart() {
  key="$1"
  start=""
  count=0
  tmp="${STATE}.tmp.$$"
  : >"$tmp"
  if [ -f "$STATE" ]; then
    while IFS= read -r line || [ -n "$line" ]; do
      [ -z "$line" ] && continue
      k="${line%% *}"
      rest="${line#* }"
      s="${rest%% *}"
      c="${rest#* }"
      if [ "$k" = "$key" ]; then
        start="$s"
        count="$c"
      else
        printf '%s\n' "$line" >>"$tmp"
      fi
    done <"$STATE"
  fi
  if [ -z "$start" ] || [ $((NOW - start)) -ge "$WINDOW_SEC" ]; then
    start="$NOW"
    count=0
  fi
  if [ "$count" -ge "$MAX_RESTARTS" ]; then
    printf '%s %s %s\n' "$key" "$start" "$count" >>"$tmp"
    mv "$tmp" "$STATE"
    return 1
  fi
  count=$((count + 1))
  printf '%s %s %s\n' "$key" "$start" "$count" >>"$tmp"
  mv "$tmp" "$STATE"
  return 0
}

try_restart() {
  key="$1"
  shift
  if [ "$RESTART" != "1" ]; then
    log "SKIP  $key  restart=off"
    return 1
  fi
  if ! allow_restart "$key"; then
    log "SKIP  $key  backoff=${MAX_RESTARTS}/${WINDOW_SEC}s"
    return 1
  fi
  {
    echo "----- ${STAMP} ${key} -----"
    "$@"
  } >>"$CMDLOG" 2>&1
  if [ $? -eq 0 ]; then
    log "RESTART  $key  ok"
    return 0
  fi
  log "FAIL  $key  cmd-failed"
  return 1
}

pm2_daemon_up() {
  pgrep -f 'PM2 v.*God Daemon' >/dev/null 2>&1
}

pm2_status_of() {
  name="$1"
  json="$2"
  printf '%s' "$json" | python3 -c '
import json,sys
name=sys.argv[1]
try:
    data=json.load(sys.stdin)
except Exception:
    print("unknown")
    raise SystemExit
for p in data:
    if p.get("name")==name:
        print((p.get("pm2_env") or {}).get("status") or "unknown")
        raise SystemExit
print("missing")
' "$name"
}

launchd_disabled() {
  label="$1"
  uid="$2"
  launchctl print-disabled "gui/${uid}" 2>/dev/null | grep -F "\"${label}\"" | grep -q '=> disabled'
}

down=0
did_pm2_bulk=0
uid="$(id -u)"

# --- pm2 ---
if ! pm2_daemon_up; then
  down=1
  log "DOWN  pm2:daemon  status=missing"
  if [ ! -f "$DUMP" ]; then
    log "FAIL  pm2:resurrect  no-dump"
  else
    try_restart "pm2:resurrect" pm2 resurrect
    did_pm2_bulk=1
  fi
else
  pm2_json="$(pm2 jlist 2>/dev/null || echo '[]')"
  missing_names=""
  missing_n=0
  restart_names=""
  for name in "${expect_pm2[@]}"; do
    status="$(pm2_status_of "$name" "$pm2_json")"
    if [ "$status" = "online" ]; then
      continue
    fi
    down=1
    log "DOWN  pm2:$name  status=$status"
    if [ "$status" = "stopped" ] || [ "$status" = "errored" ] || [ "$status" = "stopping" ]; then
      restart_names="${restart_names}${name} "
    else
      missing_names="${missing_names}${name} "
      missing_n=$((missing_n + 1))
    fi
  done

  if [ "$missing_n" -ge 3 ]; then
    if [ -f "$DUMP" ]; then
      try_restart "pm2:resurrect" pm2 resurrect
      did_pm2_bulk=1
    else
      log "FAIL  pm2:resurrect  no-dump"
    fi
  fi

  if [ "$did_pm2_bulk" -eq 0 ]; then
    for name in $restart_names; do
      try_restart "pm2:$name" pm2 restart "$name"
    done
    for name in $missing_names; do
      if [ -f "$ECOSYSTEM" ]; then
        try_restart "pm2:$name" pm2 start "$ECOSYSTEM" --only "$name"
      else
        log "FAIL  pm2:$name  no-ecosystem"
      fi
    done
  fi
fi

# --- launchd always-on ---
for spec in "${expect_launchd[@]}"; do
  label="${spec%% *}"
  plist_name="${spec#* }"
  plist="${HOME}/Library/LaunchAgents/${plist_name}"

  if launchd_disabled "$label" "$uid"; then
    log "SKIP  launchd:$label  disabled"
    continue
  fi

  if ! launchctl print "gui/${uid}/${label}" >/dev/null 2>&1; then
    down=1
    log "DOWN  launchd:$label  status=not-loaded"
    if [ -f "$plist" ]; then
      try_restart "launchd:$label" launchctl bootstrap "gui/${uid}" "$plist"
    else
      log "FAIL  launchd:$label  no-plist"
    fi
    continue
  fi

  pid="$(launchctl print "gui/${uid}/${label}" 2>/dev/null | awk '/^[[:space:]]*pid = / {print $3; exit}')"
  if [ -z "${pid:-}" ] || [ "$pid" = "0" ]; then
    down=1
    log "DOWN  launchd:$label  status=no-pid"
    try_restart "launchd:$label" launchctl kickstart "gui/${uid}/${label}"
  fi
done

if [ "$down" -eq 0 ]; then
  # Quiet when healthy - one heartbeat line an hour at most.
  last="$(tail -n 1 "$LOG" 2>/dev/null || true)"
  case "$last" in
    *"OK    all expected jobs online"*)
      last_hour="${last:0:13}"
      now_hour="${STAMP:0:13}"
      if [ "$last_hour" = "$now_hour" ]; then
        exit 0
      fi
      ;;
  esac
  log "OK    all expected jobs online"
fi
