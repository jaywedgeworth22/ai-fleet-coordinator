#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
fail() { echo "FAIL $*" >&2; exit 1; }
[ -f "$ROOT/mac-resource-watch.py" ] || fail "missing mac-resource-watch.py"
[ -f "$ROOT/mac-resource-watch.sh" ] || fail "missing mac-resource-watch.sh"
[ -f "$ROOT/launchd/com.jay.mac-resource-watch.plist" ] || fail "missing plist"
python3 -m py_compile "$ROOT/mac-resource-watch.py" || fail "py_compile"
bash -n "$ROOT/mac-resource-watch.sh" || fail "bash -n wrapper"
if ! grep -q 'BOTFLEET_HOUSEKEEPER_WEBHOOK' "$ROOT/mac-resource-watch.py"; then
  fail "watch must load Housekeeper webhook env"
fi
if grep -nE 'print\(.*(secret|whsec_|TOKEN)' "$ROOT/mac-resource-watch.py"; then
  fail "must not print webhook secrets"
fi
echo OK
