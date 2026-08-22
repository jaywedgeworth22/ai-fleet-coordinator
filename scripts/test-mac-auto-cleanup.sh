#!/bin/bash
# Contract: mac-auto-cleanup must not delete live checkouts or poke Coolify.
# #95 wiped ~/.grok/worktrees and force-removed any ~/Code worktree whose
# branch grepped in `git branch --merged main` (empty/`main`/standing lanes).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="${ROOT}/mac-auto-cleanup.sh"

fail() { echo "FAIL $*" >&2; exit 1; }

[ -f "$SCRIPT" ] || fail "missing $SCRIPT"

if grep -nE '^[[:space:]]*rm[[:space:]]+-rf[[:space:]]+"?\$HOME/\.grok/worktrees' "$SCRIPT"; then
  fail "must not wipe ~/.grok/worktrees (in-session GROK checkouts)"
fi
if grep -nE '^[[:space:]]*[^#[:space:]].*worktree remove --force' "$SCRIPT"; then
  fail "must not git worktree remove --force (deletes dirty standing lanes)"
fi
if grep -nE '^[[:space:]]*[^#[:space:]].*branch --merged' "$SCRIPT"; then
  fail "must not classify worktrees via branch --merged (false-positive main/empty)"
fi
if grep -nE '^[[:space:]]*rm[[:space:]].*CoreSimulator/Devices' "$SCRIPT"; then
  fail "must not wipe live CoreSimulator devices"
fi
if grep -nE '^[[:space:]]*[^#[:space:]].*(coolify-auto-maintenance|docker system prune)' "$SCRIPT"; then
  fail "must not SSH Coolify or volume-prune from this Mac job"
fi
if ! grep -nE 'disk-janitor' "$SCRIPT"; then
  fail "must point worktree retirement at disk-janitor.sh"
fi

echo OK
