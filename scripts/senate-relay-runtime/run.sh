#!/usr/bin/env bash
# Mac origin for scout.jays.services. Do not hairpin SENATE_RELAY_URL.
# Secret is sourced only when SENATE_RELAY_REQUIRE=1 so production can
# start sending the header before this origin fail-closes.
set -euo pipefail
cd "$(dirname "$0")"
if [[ "${SENATE_RELAY_REQUIRE:-0}" == "1" && -f "${HOME}/.secrets/senate-relay.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "${HOME}/.secrets/senate-relay.env"
  set +a
fi
PORT="${1:-8899}"
exec /Users/jay/.deno/bin/deno run --allow-net --allow-env senate-relay.ts "$PORT"
