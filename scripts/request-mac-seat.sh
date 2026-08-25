#!/usr/bin/env bash
# request-mac-seat.sh — cloud agent files a needs-mac GitHub issue for Mac xcodebuild work.
#
# Cloud agents cannot run xcodebuild.  File a structured needs-mac issue, post to
# #agent-sync, and let the Mac launchd poller (mac-seat-claim.sh) pick it up.
#
# Usage:
#   ./scripts/request-mac-seat.sh \
#     --repo Socratic.Trade \
#     --title "Verify iOS archive on cursor/ios-fix" \
#     --prompt "Run xcodebuild for ST iOS.  Branch cursor/ios-fix in ~/apps/trading-cursor-ios-fix." \
#     --by GB-COMPILER \
#     --agent grok \
#     --branch cursor/ios-fix \
#     --worktree ~/apps/trading-cursor-ios-fix
#
# Options:
#   --repo REPO          GitHub repo name or owner/repo (required)
#   --title TEXT         Issue title without the [needs-mac] prefix (required)
#   --prompt TEXT        Initial prompt for the Mac local agent (required)
#   --by TAG             Cloud seat tag, e.g. GB-COMPILER or CURSOR (required)
#   --agent grok|cursor  Local agent to spawn on the Mac (default: grok)
#   --branch NAME        Git branch the Mac seat should use
#   --worktree PATH      Worktree path on Jay's Mac (~/apps/...)
#   --reason TEXT        Why Mac is needed (default: xcodebuild)
#   --board-id ID        Optional THE BOARD item id to link
#   --no-slack           Skip agent-sync tunnel post
#   --dry-run            Print actions without creating the issue
#   -h, --help           Show this help

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FLEET_APPS="${REPO_ROOT}/fleet-apps.json"
OWNER="${GITHUB_OWNER:-jaywedgeworth22}"
AGENT_SYNC_POST_URL="${AGENT_SYNC_POST_URL:-https://agent-sync.jays.services/post}"
AGENT_SYNC_ENV="${AGENT_SYNC_ENV:-$HOME/.secrets/agent-sync.env}"

REPO=""
TITLE=""
PROMPT=""
BY=""
AGENT="grok"
BRANCH=""
WORKTREE=""
REASON="xcodebuild"
BOARD_ID=""
NO_SLACK=0
DRY_RUN=0

usage() {
  sed -n '2,29p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-0}"
}

run() {
  if [ "$DRY_RUN" -eq 1 ]; then
    printf 'DRY:'; printf ' %q' "$@"; printf '\n'
  else
    "$@"
  fi
}

die() {
  echo "request-mac-seat: $*" >&2
  exit 1
}

normalize_repo() {
  local raw="$1"
  if [[ "$raw" == */* ]]; then
    echo "$raw"
    return
  fi
  echo "${OWNER}/${raw}"
}

while [ $# -gt 0 ]; do
  case "$1" in
    --repo) REPO="${2:-}"; shift 2 ;;
    --title) TITLE="${2:-}"; shift 2 ;;
    --prompt) PROMPT="${2:-}"; shift 2 ;;
    --by) BY="${2:-}"; shift 2 ;;
    --agent) AGENT="${2:-}"; shift 2 ;;
    --branch) BRANCH="${2:-}"; shift 2 ;;
    --worktree) WORKTREE="${2:-}"; shift 2 ;;
    --reason) REASON="${2:-}"; shift 2 ;;
    --board-id) BOARD_ID="${2:-}"; shift 2 ;;
    --no-slack) NO_SLACK=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) usage 0 ;;
    *) die "unknown arg: $1 (try --help)" ;;
  esac
done

[ -n "$REPO" ] || die "--repo is required"
[ -n "$TITLE" ] || die "--title is required"
[ -n "$PROMPT" ] || die "--prompt is required"
[ -n "$BY" ] || die "--by is required"

case "$AGENT" in
  grok|cursor) ;;
  *) die "--agent must be grok or cursor" ;;
esac

FULL_REPO="$(normalize_repo "$REPO")"
REPO_NAME="${FULL_REPO##*/}"
ISSUE_TITLE="[needs-mac] ${TITLE}"

read -r -d '' ISSUE_BODY <<EOF || true
Cloud seat **${BY}** needs a Mac local agent for **${REASON}**.

<!-- needs-mac:v1
agent=${AGENT}
by=${BY}
repo=${REPO_NAME}
branch=${BRANCH}
worktree=${WORKTREE}
reason=${REASON}
board_id=${BOARD_ID}
-->

| Field | Value |
| --- | --- |
| agent | \`${AGENT}\` |
| cloud seat | \`${BY}\` |
| repo | \`${REPO_NAME}\` |
| branch | \`${BRANCH:-<unspecified>}\` |
| worktree | \`${WORKTREE:-<unspecified>}\` |
| reason | \`${REASON}\` |
| board | \`${BOARD_ID:-<none>}\` |

### Prompt

${PROMPT}

### Notes

- Mac poller: \`mac-seat-claim.sh\` (launchd \`com.jay.mac-seat-watch\`).
- Spawn uses Shellular-host argv: Grok \`grok -p\`, Cursor \`cursor-agent -p\` — not Shellular phone ACP.
- grok-acp stays on \`127.0.0.1:12419\` only.  Never \`:2419\`.
- Do **not** close this issue until the Mac seat posts results.  Scripts never claim compile passed.
EOF

echo "== request-mac-seat =="
echo "repo:     ${FULL_REPO}"
echo "title:    ${ISSUE_TITLE}"
echo "agent:    ${AGENT}"
echo "by:       ${BY}"
echo "reason:   ${REASON}"
[ -n "$BRANCH" ] && echo "branch:   ${BRANCH}"
[ -n "$WORKTREE" ] && echo "worktree: ${WORKTREE}"
[ "$DRY_RUN" -eq 1 ] && echo "mode:     dry-run"

if ! command -v gh >/dev/null 2>&1; then
  die "gh CLI is required to file the needs-mac issue"
fi

run gh issue create \
  --repo "$FULL_REPO" \
  --title "$ISSUE_TITLE" \
  --body "$ISSUE_BODY" \
  --label "needs-mac"

if [ "$NO_SLACK" -eq 0 ] && [ -f "$AGENT_SYNC_ENV" ]; then
  POST_TOKEN=""
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in
      AGENT_SYNC_POST_TOKEN=*) POST_TOKEN="${line#AGENT_SYNC_POST_TOKEN=}" ;;
    esac
  done < "$AGENT_SYNC_ENV"
  POST_TOKEN="${POST_TOKEN%\"}"
  POST_TOKEN="${POST_TOKEN#\"}"
  POST_TOKEN="${POST_TOKEN%\'}"
  POST_TOKEN="${POST_TOKEN#\'}"

  if [ -n "$POST_TOKEN" ]; then
    SLACK_TEXT="repo: ${REPO_NAME} | [${BY}->MAC] needs-mac ${REASON}: ${TITLE}"
    [ -n "$BRANCH" ] && SLACK_TEXT="${SLACK_TEXT} | branch ${BRANCH}"
    [ -n "$WORKTREE" ] && SLACK_TEXT="${SLACK_TEXT} | ${WORKTREE}"
    SLACK_TEXT="${SLACK_TEXT} | agent ${AGENT}"
    if [ "$DRY_RUN" -eq 1 ]; then
      printf 'DRY: curl -sS -X POST %q -H Authorization: Bearer <redacted> -d %q\n' \
        "$AGENT_SYNC_POST_URL" "{\"text\":\"${SLACK_TEXT}\",\"username\":\"${BY}\"}"
    else
      export SLACK_TEXT BY
      curl -fsS -X POST "$AGENT_SYNC_POST_URL" \
        -H "Authorization: Bearer ${POST_TOKEN}" \
        -H "Content-Type: application/json" \
        -d "$(python3 - <<'PY'
import json, os
print(json.dumps({"text": os.environ["SLACK_TEXT"], "username": os.environ["BY"]}))
PY
)" >/dev/null || echo "request-mac-seat: agent-sync post failed (issue still filed)" >&2
    fi
  fi
fi

echo "request-mac-seat: filed needs-mac issue on ${FULL_REPO}"
