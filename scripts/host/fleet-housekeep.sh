#!/usr/bin/env bash
# fleet-housekeep.sh — lightweight host hygiene checks for fleet-hetzner-nbg1
#
# Reports failed systemd units (including benign-but-noisy ones like
# grub-initrd-fallback.service), zombie count, and root disk pressure.
# Pushover uses the fleet Usage Monitor app token (PUSHOVER_USAGE_API_TOKEN).
#
# Install (Coolify host as root):
#   install -m 0755 scripts/host/fleet-housekeep.sh /usr/local/bin/
#   install -m 0644 scripts/host/fleet-housekeep.{service,timer} /etc/systemd/system/
#   systemctl daemon-reload && systemctl enable --now fleet-housekeep.timer
#
# Env (optional /etc/fleet-housekeep.env):
#   PUSHOVER_USAGE_API_TOKEN / PUSHOVER_APP_TOKEN
#   PUSHOVER_USER_KEY
#   WARN_USED_PCT (default 75)
#   CRIT_USED_PCT (default 85)
#   ZOMBIE_WARN (default 10)
#   STATE_DIR (default /var/lib/fleet-housekeep)
#   IGNORE_FAILED_UNITS (regex, default grub-initrd-fallback)

set -euo pipefail

ROOT_PATH="${ROOT_PATH:-/}"
WARN_USED_PCT="${WARN_USED_PCT:-75}"
CRIT_USED_PCT="${CRIT_USED_PCT:-85}"
ZOMBIE_WARN="${ZOMBIE_WARN:-10}"
STATE_DIR="${STATE_DIR:-/var/lib/fleet-housekeep}"
LOG_TAG="${LOG_TAG:-fleet-housekeep}"
IGNORE_FAILED_UNITS="${IGNORE_FAILED_UNITS:-grub-initrd-fallback}"
NOTIFY_COOLDOWN_SEC="${NOTIFY_COOLDOWN_SEC:-3600}"

if [[ -f /etc/fleet-housekeep.env ]]; then
  # shellcheck disable=SC1091
  set -a; source /etc/fleet-housekeep.env; set +a
fi
PUSHOVER_APP_TOKEN="${PUSHOVER_USAGE_API_TOKEN:-${PUSHOVER_APP_TOKEN:-}}"

mkdir -p "$STATE_DIR"

log() {
  local msg="$*"
  printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$msg"
  if command -v logger >/dev/null 2>&1; then
    logger -t "$LOG_TAG" -- "$msg" || true
  fi
}

notify_ok() {
  local last="$STATE_DIR/last_notify"
  local now_ts last_ts
  now_ts=$(date +%s)
  if [[ -f "$last" ]]; then
    last_ts=$(cat "$last" 2>/dev/null || echo 0)
    if [[ $((now_ts - last_ts)) -lt "$NOTIFY_COOLDOWN_SEC" ]]; then
      return 0
    fi
  fi
  if [[ -z "${PUSHOVER_APP_TOKEN:-}" || -z "${PUSHOVER_USER_KEY:-}" ]]; then
    return 0
  fi
  local title severity body
  title="$1"
  severity="$2"
  body="$3"
  curl -fsS -m 15 \
    --form-string "token=${PUSHOVER_APP_TOKEN}" \
    --form-string "user=${PUSHOVER_USER_KEY}" \
    --form-string "title=${title}" \
    --form-string "message=${body}" \
    --form-string "priority=$([[ "$severity" == crit ]] && echo 1 || echo 0)" \
    https://api.pushover.net/1/messages.json >/dev/null 2>&1 \
    || log "warn: pushover failed"
  echo "$now_ts" >"$last"
}

read_disk() {
  local line
  line=$(df -P "$ROOT_PATH" 2>/dev/null | awk 'NR==2 {print $3, $4, $5}')
  if [[ -z "$line" ]]; then
    log "error: df failed for $ROOT_PATH"
    exit 1
  fi
  local used_k avail_k used_pct_str
  read -r used_k avail_k used_pct_str <<<"$line"
  USED_PCT=${used_pct_str%%%}
  FREE_GB=$(awk -v a="$avail_k" 'BEGIN { printf "%.1f", a/1024/1024 }')
}

list_actionable_failed_units() {
  systemctl --failed --no-legend --no-pager 2>/dev/null | awk '{print $1}' | while IFS= read -r unit; do
    [[ -z "$unit" ]] && continue
    if [[ "$unit" =~ $IGNORE_FAILED_UNITS ]]; then
      continue
    fi
    echo "$unit"
  done
}

count_zombies() {
  ps -eo stat 2>/dev/null | grep -c '^Z' || echo 0
}

main() {
  read_disk
  local failed_units zombies failed_count
  failed_units=$(list_actionable_failed_units | paste -sd, - || true)
  failed_count=$(list_actionable_failed_units | wc -l | tr -d ' ')
  zombies=$(count_zombies)

  local ignored_failed
  ignored_failed=$(systemctl --failed --no-legend --no-pager 2>/dev/null | awk '{print $1}' | grep -E "$IGNORE_FAILED_UNITS" | paste -sd, - || true)

  log "housekeep: disk=${USED_PCT}% free=${FREE_GB}G zombies=${zombies} failed-units=${failed_units:-none} ignored=${ignored_failed:-none}"

  local severity=ok
  local problems=()

  if awk -v u="$USED_PCT" -v c="$CRIT_USED_PCT" 'BEGIN{exit !(u+0 >= c+0)}'; then
    severity=crit
    problems+=("disk=${USED_PCT}% free=${FREE_GB}G")
  elif awk -v u="$USED_PCT" -v w="$WARN_USED_PCT" 'BEGIN{exit !(u+0 >= w+0)}'; then
    severity=warn
    problems+=("disk=${USED_PCT}% free=${FREE_GB}G")
  fi

  if [[ "$zombies" -ge "$ZOMBIE_WARN" ]]; then
    if [[ "$severity" == ok ]]; then severity=warn; fi
    problems+=("zombies=${zombies}")
  fi

  if [[ "$failed_count" -gt 0 ]]; then
    if [[ "$severity" == ok ]]; then severity=warn; fi
    problems+=("failed-units=${failed_units}")
  fi

  printf '%s disk=%s free=%sG zombies=%s failed=%s level=%s\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$USED_PCT" "$FREE_GB" "$zombies" "${failed_units:-}" "$severity" \
    >"$STATE_DIR/last-status"

  if [[ "$severity" != ok ]]; then
    local body
    body="$(hostname) housekeep: $(IFS='; '; echo "${problems[*]}")"
    notify_ok "fleet-housekeep ${severity}" "$severity" "$body"
  fi
}

main "$@"
