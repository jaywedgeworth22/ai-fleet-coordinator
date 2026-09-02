#!/usr/bin/env bash
# Exercise scripts/install-fleet-rag.sh against a throwaway $HOME and a throwaway fake
# checkout, so no real config on this Mac is touched.
#
#   cd scripts && bash fleet_rag/tests/test_installer.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS="$(cd "$HERE/../.." && pwd)"
INSTALLER="$SCRIPTS/install-fleet-rag.sh"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/fleet-rag-install-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT

FAKE_HOME="$TMP/home"
FAKE_REPO="$TMP/repo"
FAILS=0

pass() { printf 'ok   - %s\n' "$1"; }
fail() { printf 'FAIL - %s\n' "$1"; FAILS=$((FAILS + 1)); }
assert() {  # assert <desc> <command...>
  local desc="$1"; shift
  if "$@"; then pass "$desc"; else fail "$desc"; fi
}

# -- fake checkout: the real installer plus the real fleet_rag package, plus stub entry points
mkdir -p "$FAKE_REPO/scripts/seat-mcp/seat_mcp"
cp "$INSTALLER" "$FAKE_REPO/scripts/install-fleet-rag.sh"
cp -R "$SCRIPTS/fleet_rag" "$FAKE_REPO/scripts/fleet_rag"
mkdir -p "$FAKE_REPO/scripts/fleet_rag/__pycache__"
touch "$FAKE_REPO/scripts/fleet_rag/__pycache__/junk.pyc"
for f in recall fleet-recall-mcp.py fleet-rag.py; do
  if [[ -f "$SCRIPTS/$f" ]]; then cp "$SCRIPTS/$f" "$FAKE_REPO/scripts/$f"; else printf '#!/usr/bin/env python3\nprint("stub %s")\n' "$f" > "$FAKE_REPO/scripts/$f"; fi
done
printf '# stub\n' > "$FAKE_REPO/scripts/seat-mcp/seat_mcp/tools.py"
printf '# stub\n' > "$FAKE_REPO/scripts/seat-mcp/seat_mcp/recall_bridge.py"

# -- fake HOME with minimal configs
mkdir -p "$FAKE_HOME/.cursor" "$FAKE_HOME/.codex" "$FAKE_HOME/.grok" "$FAKE_HOME/apps/mac-collab"
cat > "$FAKE_HOME/.claude.json" <<'EOF'
{
  "numStartups": 3,
  "mcpServers": {
    "github": {"command": "sh", "args": ["/x/github.sh"]}
  },
  "projects": {"/Users/jay/Code/x": {"allowedTools": []}}
}
EOF
cat > "$FAKE_HOME/.codex/config.toml" <<'EOF'
model = "gpt-5"

[mcp_servers.x]
command = "npx"
args = [ "-y", "x-mcp" ]
enabled = true
EOF
cat > "$FAKE_HOME/.grok/config.toml" <<'EOF'
[cli]
theme = "dark"

[mcp_servers.seat-mcp]
command = "sh"
args = ["/x/seat-mcp-launch.sh"]
enabled = true

[permission]
allow = ["bash"]
EOF
: > "$FAKE_HOME/.cursor/mcp.json"
# stale symlink that must be replaced
ln -s "$FAKE_HOME/nowhere/recall" "$FAKE_HOME/apps/mac-collab/recall"

run() { HOME="$FAKE_HOME" bash "$FAKE_REPO/scripts/install-fleet-rag.sh" "$@"; }

snapshot() {  # <label>: copy every config for later diffing (distinct names; two are config.toml)
  local d="$TMP/snap-$1"
  mkdir -p "$d"
  cp "$FAKE_HOME/.claude.json" "$d/claude.json"
  cp "$FAKE_HOME/.codex/config.toml" "$d/codex.toml"
  cp "$FAKE_HOME/.grok/config.toml" "$d/grok.toml"
  cp "$FAKE_HOME/.cursor/mcp.json" "$d/cursor.json"
  [[ -f "$FAKE_HOME/.gemini/config/mcp_config.json" ]] && cp "$FAKE_HOME/.gemini/config/mcp_config.json" "$d/gemini.json" || true
}
snap_name() {  # map a $HOME-relative config path to its snapshot file name
  case "$1" in
    .claude.json) echo claude.json ;;
    .codex/config.toml) echo codex.toml ;;
    .grok/config.toml) echo grok.toml ;;
    .cursor/mcp.json) echo cursor.json ;;
  esac
}

json_has() {  # <file> <server> -> 0 if present
  python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));sys.exit(0 if sys.argv[2] in d.get("mcpServers",{}) else 1)' "$1" "$2"
}
json_get() {  # <file> <dotted path>
  python3 -c 'import json,sys;d=json.load(open(sys.argv[1]))
for k in sys.argv[2].split("."): d=d[k]
print(json.dumps(d,sort_keys=True))' "$1" "$2"
}

echo "== dry-run writes nothing"
snapshot before
run --dry-run > "$TMP/dry.out"
assert "dry-run mentions planned-add" grep -q 'planned-add' "$TMP/dry.out"
assert "dry-run leaves ~/.claude.json untouched" cmp -s "$FAKE_HOME/.claude.json" "$TMP/snap-before/claude.json"
assert "dry-run does not create ~/apps/fleet-rag" test ! -e "$FAKE_HOME/apps/fleet-rag/recall"
assert "dry-run does not create gemini config" test ! -e "$FAKE_HOME/.gemini/config/mcp_config.json"

echo "== first install"
run --with-seat-mcp > "$TMP/run1.out"
assert "fleet_rag package installed" test -f "$FAKE_HOME/apps/fleet-rag/fleet_rag/core.py"
assert "tests dir excluded from install" test ! -e "$FAKE_HOME/apps/fleet-rag/fleet_rag/tests"
assert "__pycache__ excluded from install" test ! -e "$FAKE_HOME/apps/fleet-rag/fleet_rag/__pycache__"
assert "recall is executable" test -x "$FAKE_HOME/apps/fleet-rag/recall"
assert "mcp server is executable" test -x "$FAKE_HOME/apps/fleet-rag/fleet-recall-mcp.py"
assert "state/cache/logs created" test -d "$FAKE_HOME/apps/fleet-rag/state" -a -d "$FAKE_HOME/apps/fleet-rag/cache" -a -d "$FAKE_HOME/apps/fleet-rag/logs"
assert "stale symlink replaced" test "$(readlink "$FAKE_HOME/apps/mac-collab/recall")" = "$FAKE_HOME/apps/fleet-rag/recall"
assert "PATH symlink ~/.local/bin/recall" test "$(readlink "$FAKE_HOME/.local/bin/recall")" = "$FAKE_HOME/apps/fleet-rag/recall"
assert "grok-acp config absent is not created" test ! -e "$FAKE_HOME/apps/grok-acp-runtime/acp-home-config.toml"
assert "seat-mcp files copied" test -f "$FAKE_HOME/apps/seat-mcp/seat_mcp/recall_bridge.py" -a -f "$FAKE_HOME/apps/seat-mcp/seat_mcp/tools.py"
assert "pm2 restart printed, not run" grep -q 'pm2 restart seat-mcp' "$TMP/run1.out"

assert "claude.json: fleet-recall added" json_has "$FAKE_HOME/.claude.json" fleet-recall
assert "claude.json: existing github server preserved" json_has "$FAKE_HOME/.claude.json" github
assert "claude.json: unrelated keys preserved" test "$(json_get "$FAKE_HOME/.claude.json" numStartups)" = "3"
assert "claude.json: projects preserved" test "$(json_get "$FAKE_HOME/.claude.json" 'projects./Users/jay/Code/x.allowedTools')" = "[]"
assert "claude.json: command is python3" test "$(json_get "$FAKE_HOME/.claude.json" mcpServers.fleet-recall.command)" = '"python3"'
assert "claude.json: args point at installed server" test "$(json_get "$FAKE_HOME/.claude.json" mcpServers.fleet-recall.args)" = "[\"$FAKE_HOME/apps/fleet-rag/fleet-recall-mcp.py\"]"
assert "claude.json: backup made" bash -c "ls '$FAKE_HOME'/.claude.json.bak-fleet-rag-* >/dev/null 2>&1"
assert "cursor mcp.json: fleet-recall added to empty file" json_has "$FAKE_HOME/.cursor/mcp.json" fleet-recall
assert "gemini config created with fleet-recall" json_has "$FAKE_HOME/.gemini/config/mcp_config.json" fleet-recall
assert "codex toml: block added once" test "$(grep -c '^\[mcp_servers.fleet-recall\]' "$FAKE_HOME/.codex/config.toml")" = "1"
assert "codex toml: existing block preserved" grep -q '^\[mcp_servers.x\]' "$FAKE_HOME/.codex/config.toml"
assert "codex toml: model line preserved" grep -q '^model = "gpt-5"' "$FAKE_HOME/.codex/config.toml"
assert "grok toml: block added once" test "$(grep -c '^\[mcp_servers.fleet-recall\]' "$FAKE_HOME/.grok/config.toml")" = "1"
assert "grok toml: enabled key used" bash -c "awk '/^\[mcp_servers.fleet-recall\]/{f=1;next} /^\[/{f=0} f' '$FAKE_HOME/.grok/config.toml' | grep -q '^enabled = true'"
assert "grok toml: seat-mcp block preserved" grep -q '^\[mcp_servers.seat-mcp\]' "$FAKE_HOME/.grok/config.toml"
assert "grok toml: trailing [permission] preserved" grep -q '^allow = \["bash"\]' "$FAKE_HOME/.grok/config.toml"
assert "no token-looking strings written" bash -c "! grep -Eiq 'token|secret|bearer' '$FAKE_HOME/.cursor/mcp.json' '$FAKE_HOME/.gemini/config/mcp_config.json'"

echo "== second install is a no-op"
snapshot after1
run > "$TMP/run2.out"
for f in .claude.json .codex/config.toml .grok/config.toml .cursor/mcp.json; do
  assert "second run leaves $f byte-identical" cmp -s "$FAKE_HOME/$f" "$TMP/snap-after1/$(snap_name "$f")"
done
assert "second run: gemini byte-identical" cmp -s "$FAKE_HOME/.gemini/config/mcp_config.json" "$TMP/snap-after1/gemini.json"
assert "second run reports unchanged for every config" test "$(grep -c ': unchanged$' "$TMP/run2.out")" = "5"
assert "second run makes no new backups" test "$(ls "$FAKE_HOME"/.claude.json.bak-fleet-rag-* | wc -l | tr -d ' ')" = "1"
assert "codex toml still has exactly one block" test "$(grep -c '^\[mcp_servers.fleet-recall\]' "$FAKE_HOME/.codex/config.toml")" = "1"

echo "== uninstall restores"
run --uninstall > "$TMP/run3.out"
if json_has "$FAKE_HOME/.claude.json" fleet-recall; then fail "claude.json: fleet-recall removed"; else pass "claude.json: fleet-recall removed"; fi
assert "claude.json: github still present" json_has "$FAKE_HOME/.claude.json" github
assert "claude.json: content equals pre-install (modulo formatting)" test "$(json_get "$FAKE_HOME/.claude.json" mcpServers)" = "$(json_get "$TMP/snap-before/claude.json" mcpServers)"
assert "codex toml restored byte-for-byte" cmp -s "$FAKE_HOME/.codex/config.toml" "$TMP/snap-before/codex.toml"
assert "grok toml restored byte-for-byte" cmp -s "$FAKE_HOME/.grok/config.toml" "$TMP/snap-before/grok.toml"
assert "grok toml: block removed" bash -c "! grep -q '^\[mcp_servers.fleet-recall\]' '$FAKE_HOME/.grok/config.toml'"
assert "grok toml: [permission] survives removal" grep -q '^allow = \["bash"\]' "$FAKE_HOME/.grok/config.toml"
assert "grok toml: seat-mcp survives removal" grep -q '^\[mcp_servers.seat-mcp\]' "$FAKE_HOME/.grok/config.toml"
if json_has "$FAKE_HOME/.gemini/config/mcp_config.json" fleet-recall; then fail "gemini: removed"; else pass "gemini: removed"; fi
assert "symlink removed" test ! -e "$FAKE_HOME/apps/mac-collab/recall" -a ! -L "$FAKE_HOME/apps/mac-collab/recall"
assert "PATH symlink removed" test ! -e "$FAKE_HOME/.local/bin/recall" -a ! -L "$FAKE_HOME/.local/bin/recall"
assert "installed code removed" test ! -e "$FAKE_HOME/apps/fleet-rag/fleet_rag"
assert "state dir kept on uninstall" test -d "$FAKE_HOME/apps/fleet-rag/state"

echo "== refuses to clobber a real file at the symlink path"
rm -rf "$FAKE_HOME/apps/mac-collab/recall"; printf 'real\n' > "$FAKE_HOME/apps/mac-collab/recall"
if run > "$TMP/run4.out" 2>&1; then fail "real file at symlink path refused"; else pass "real file at symlink path refused"; fi
assert "real file untouched" test "$(cat "$FAKE_HOME/apps/mac-collab/recall")" = "real"

echo
if [[ "$FAILS" -eq 0 ]]; then
  echo "ALL PASS (test_installer.sh)"
else
  echo "$FAILS FAILURE(S) (test_installer.sh)"
  exit 1
fi
