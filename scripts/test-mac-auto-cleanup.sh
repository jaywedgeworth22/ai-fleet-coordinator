#!/bin/bash
# Contract: mac-auto-cleanup must not force-reap live checkouts or simulators.
# #95 shipped three data-loss paths on a 4h launchd tick:
#   * rm -rf ~/.grok/worktrees/*  (in-session Grok checkouts)
#   * git worktree remove --force + grep -Fw "" on detached HEAD
#   * rm -rf CoreSimulator/Devices/*  (every simulator, not unavailable-only)
# Worktree retirement stays on disk-janitor (#93).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="${ROOT}/mac-auto-cleanup.sh"

fail() { echo "FAIL $*" >&2; exit 1; }

[ -f "$SCRIPT" ] || fail "missing $SCRIPT"

code_lines() { grep -nE "$1" "$SCRIPT" | grep -vE '^[^:]+:[[:space:]]*#' || true; }

if [ -n "$(code_lines 'CoreSimulator/Devices"/\*')" ]; then
  fail "must not rm -rf CoreSimulator/Devices/* (wipes every simulator)"
fi

if [ -n "$(code_lines '\.grok/worktrees"/\*')" ]; then
  fail "must not rm -rf ~/.grok/worktrees/* (in-session Grok checkouts)"
fi

if [ -n "$(code_lines 'worktree remove --force')" ]; then
  fail "must not git worktree remove --force (deletes dirty trees)"
fi

if [ -n "$(code_lines 'grep -Fw')" ]; then
  fail "empty-string word match on detached HEAD matches every merged branch"
fi

if ! grep -q 'agent-sync-push' "$SCRIPT"; then
  fail "mac-auto-cleanup.sh must preserve agent-sync-push runtime"
fi

if ! grep -q 'is_git_worktree' "$SCRIPT" || ! grep -q 'wt_has_blocking_dirt' "$SCRIPT" || ! grep -q 'wt_is_active' "$SCRIPT"; then
  fail "mac-auto-cleanup.sh must enforce worktree, dirt, and idle checks before reaping dependencies"
fi

bash -n "$SCRIPT" || fail "bash -n failed"

echo OK
