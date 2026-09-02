#!/usr/bin/env bash
# Install the fleet-rag tooling on this Mac and register the fleet-recall MCP server
# for every platform.  Idempotent.  Honors $HOME so tests can redirect it.
#
# What it does:
#   1. Copies scripts/fleet_rag/ (no tests, no __pycache__), scripts/recall,
#      scripts/fleet-recall-mcp.py and scripts/fleet-rag.py from this checkout into
#      $HOME/apps/fleet-rag/ and creates state/ cache/ logs/ there.
#   2. Symlinks $HOME/apps/mac-collab/recall and $HOME/.local/bin/recall
#      -> $HOME/apps/fleet-rag/recall  (board is ~/.local/bin/board; agent shells also
#      prepend ~/apps/mac-collab).
#   3. Registers a stdio MCP server "fleet-recall"
#        {command: "python3", args: ["$HOME/apps/fleet-rag/fleet-recall-mcp.py"]}
#      in ~/.claude.json, ~/.cursor/mcp.json, ~/.gemini/config/mcp_config.json,
#      ~/.codex/config.toml and ~/.grok/config.toml.  Never writes a token anywhere.
#   4. With --with-seat-mcp, also copies seat_mcp/tools.py + recall_bridge.py into
#      $HOME/apps/seat-mcp/seat_mcp/ and prints the pm2 restart command (does not run it).
#   5. With --hooks, copies scripts/hooks/fleet-recall-session-start.sh and
#      fleet-recall-stop.py into $HOME/.claude/hooks/ and appends one matcher entry each to
#      hooks.SessionStart and hooks.Stop in $HOME/.claude/settings.json (backup first; existing
#      entries untouched; idempotent).  --uninstall removes only those two entries and files.
#   6. Prints a summary table of what changed.
#
# Usage:
#   bash scripts/install-fleet-rag.sh                # install / refresh
#   bash scripts/install-fleet-rag.sh --dry-run      # print the plan, write nothing
#   bash scripts/install-fleet-rag.sh --uninstall    # remove only what this script added
#   bash scripts/install-fleet-rag.sh --with-seat-mcp
#   bash scripts/install-fleet-rag.sh --hooks        # also install the Claude Code hooks
#
# On-demand helper (not a background job).  Canonical doc: docs/RAG-FLEET-INFRA.md.
set -euo pipefail

DRY=0
UNINSTALL=0
WITH_SEAT=0
WITH_HOOKS=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=1 ;;
    --uninstall) UNINSTALL=1 ;;
    --with-seat-mcp) WITH_SEAT=1 ;;
    --hooks) WITH_HOOKS=1 ;;
    -h|--help)
      sed -n '2,30p' "$0"
      exit 0
      ;;
    *)
      echo "unknown arg: $arg" >&2
      exit 2
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SRC="$REPO_ROOT/scripts"
HOME_DIR="${HOME:?HOME must be set}"
DST="$HOME_DIR/apps/fleet-rag"
LINK="$HOME_DIR/apps/mac-collab/recall"
BIN_LINK="$HOME_DIR/.local/bin/recall"
SEAT_DST="$HOME_DIR/apps/seat-mcp/seat_mcp"
MCP_SERVER="$DST/fleet-recall-mcp.py"
SERVER_NAME="fleet-recall"
MARK="# managed by scripts/install-fleet-rag.sh (fleet-recall)"
TS="$(date +%Y%m%d%H%M%S)"

CLAUDE_JSON="$HOME_DIR/.claude.json"
CURSOR_JSON="$HOME_DIR/.cursor/mcp.json"
GEMINI_JSON="$HOME_DIR/.gemini/config/mcp_config.json"
CODEX_TOML="$HOME_DIR/.codex/config.toml"
GROK_TOML="$HOME_DIR/.grok/config.toml"
ACP_TOML="$HOME_DIR/apps/grok-acp-runtime/acp-home-config.toml"
HOOKS_DIR="$HOME_DIR/.claude/hooks"
SETTINGS_JSON="$HOME_DIR/.claude/settings.json"
HOOK_START="fleet-recall-session-start.sh"
HOOK_STOP="fleet-recall-stop.py"

PY="$(command -v python3)"
SUMMARY=()

say() { printf '%s\n' "$*"; }
note() { SUMMARY+=("$1|$2"); }

mode_word() {
  if [[ "$DRY" -eq 1 ]]; then printf 'plan'; else printf 'did'; fi
}

# ---------------------------------------------------------------- step 1: files

install_files() {
  local missing=0
  for f in fleet_rag recall fleet-recall-mcp.py fleet-rag.py; do
    if [[ ! -e "$SRC/$f" ]]; then
      say "MISSING $SRC/$f (this checkout is incomplete; the install would fail)"
      missing=1
    fi
  done
  if [[ "$DRY" -eq 1 ]]; then
    say "plan: rsync --delete $SRC/fleet_rag/ -> $DST/fleet_rag/ (excluding tests, __pycache__)"
    say "plan: copy recall, fleet-recall-mcp.py, fleet-rag.py -> $DST/ (chmod +x recall, mcp server)"
    say "plan: mkdir -p $DST/{state,cache,logs}"
    note "$DST" "planned"
    return 0
  fi
  if [[ "$missing" -eq 1 ]]; then
    say "refusing to install from an incomplete checkout" >&2
    exit 1
  fi
  mkdir -p "$DST/state" "$DST/cache" "$DST/logs"
  rsync -a --delete --exclude 'tests' --exclude '__pycache__' --exclude '*.pyc' \
    "$SRC/fleet_rag/" "$DST/fleet_rag/"
  cp -p "$SRC/recall" "$DST/recall"
  cp -p "$SRC/fleet-recall-mcp.py" "$DST/fleet-recall-mcp.py"
  cp -p "$SRC/fleet-rag.py" "$DST/fleet-rag.py"
  chmod +x "$DST/recall" "$DST/fleet-recall-mcp.py" "$DST/fleet-rag.py"
  say "installed $DST (fleet_rag/, recall, fleet-recall-mcp.py, fleet-rag.py, state/ cache/ logs/)"
  note "$DST" "installed"
}

uninstall_files() {
  if [[ "$DRY" -eq 1 ]]; then
    say "plan: remove $DST/fleet_rag/, recall, fleet-recall-mcp.py, fleet-rag.py (keep state/ cache/ logs/)"
    note "$DST" "planned-remove"
    return 0
  fi
  if [[ -d "$DST" ]]; then
    rm -rf "$DST/fleet_rag" "$DST/recall" "$DST/fleet-recall-mcp.py" "$DST/fleet-rag.py"
    say "removed code from $DST (state/ cache/ logs/ kept; delete by hand if unwanted)"
    note "$DST" "removed"
  else
    note "$DST" "absent"
  fi
}

# ---------------------------------------------------------------- step 2: symlink

install_one_link() {
  local link="$1"
  local target="$DST/recall"
  if [[ -L "$link" ]]; then
    local cur
    cur="$(readlink "$link")"
    if [[ "$cur" == "$target" ]]; then
      say "symlink ok: $link -> $target"
      note "$link" "ok"
      return 0
    fi
    if [[ "$DRY" -eq 1 ]]; then
      say "plan: replace symlink $link ($cur) -> $target"
      note "$link" "planned"
      return 0
    fi
    ln -sfn "$target" "$link"
    say "replaced symlink $link -> $target (was $cur)"
    note "$link" "replaced"
    return 0
  fi
  if [[ -e "$link" ]]; then
    say "REFUSING: $link exists and is a real file, not a symlink.  Move it aside first." >&2
    note "$link" "refused"
    [[ "$DRY" -eq 1 ]] || exit 1
    return 0
  fi
  if [[ "$DRY" -eq 1 ]]; then
    say "plan: symlink $link -> $target"
    note "$link" "planned"
    return 0
  fi
  mkdir -p "$(dirname "$link")"
  ln -s "$target" "$link"
  say "symlinked $link -> $target"
  note "$link" "added"
}

uninstall_one_link() {
  local link="$1"
  local target="$DST/recall"
  if [[ -L "$link" && "$(readlink "$link")" == "$target" ]]; then
    if [[ "$DRY" -eq 1 ]]; then
      say "plan: remove symlink $link"
      note "$link" "planned-remove"
    else
      rm -f "$link"
      say "removed symlink $link"
      note "$link" "removed"
    fi
  else
    note "$link" "not-ours"
  fi
}

install_link() { install_one_link "$LINK"; install_one_link "$BIN_LINK"; }
uninstall_link() { uninstall_one_link "$LINK"; uninstall_one_link "$BIN_LINK"; }

# ---------------------------------------------------------------- step 3: JSON configs

# json_cfg <path> <add|remove> <create-if-missing 0|1>
# Prints one of: added | unchanged | removed | absent | skipped-not-ours | planned-add | planned-remove
json_cfg() {
  local path="$1" action="$2" create="$3"
  "$PY" - "$path" "$action" "$create" "$DRY" "$SERVER_NAME" "$MCP_SERVER" "$TS" <<'PY'
import json, os, sys, tempfile, shutil
path, action, create, dry, name, server, ts = sys.argv[1:8]
dry = dry == "1"
entry = {"command": "python3", "args": [server]}
if not os.path.exists(path):
    if action == "remove":
        print("absent"); sys.exit(0)
    if create != "1":
        print("absent"); sys.exit(0)
    data = {"mcpServers": {}}
    existed = False
else:
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    data = json.loads(raw) if raw.strip() else {}
    existed = True
if not isinstance(data, dict):
    print("skipped-not-object"); sys.exit(0)
servers = data.get("mcpServers")
if servers is None:
    servers = {}
if not isinstance(servers, dict):
    print("skipped-bad-mcpServers"); sys.exit(0)
current = servers.get(name)
if action == "add":
    if current == entry:
        print("unchanged"); sys.exit(0)
    if current is not None and current != entry:
        # Someone registered a different fleet-recall by hand; leave it alone.
        print("skipped-foreign"); sys.exit(0)
    if dry:
        print("planned-add"); sys.exit(0)
    servers[name] = entry
    data["mcpServers"] = servers
else:
    if current is None:
        print("absent"); sys.exit(0)
    if current != entry:
        print("skipped-not-ours"); sys.exit(0)
    if dry:
        print("planned-remove"); sys.exit(0)
    del servers[name]
    data["mcpServers"] = servers
os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
if existed:
    shutil.copy2(path, f"{path}.bak-fleet-rag-{ts}")
fd, tmp = tempfile.mkstemp(prefix=".fleet-rag.", dir=os.path.dirname(path) or ".")
with os.fdopen(fd, "w", encoding="utf-8") as fh:
    json.dump(data, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
if existed:
    try:
        os.chmod(tmp, os.stat(path).st_mode & 0o777)
    except OSError:
        pass
else:
    os.chmod(tmp, 0o600)
os.replace(tmp, path)
print("added" if action == "add" else "removed")
PY
}

# ---------------------------------------------------------------- step 3: TOML configs

# toml_cfg <path> <add|remove> <extra-line or "">
# Appends a marked [mcp_servers.fleet-recall] block only when none exists; remove deletes
# only the block this script added (identified by the marker line).  Never rewrites the rest.
toml_cfg() {
  local path="$1" action="$2" extra="$3"
  "$PY" - "$path" "$action" "$extra" "$DRY" "$SERVER_NAME" "$MCP_SERVER" "$TS" "$MARK" <<'PY'
import json, os, re, shutil, sys
path, action, extra, dry, name, server, ts, mark = sys.argv[1:9]
dry = dry == "1"
header = f"[mcp_servers.{name}]"
if not os.path.exists(path):
    print("absent"); sys.exit(0)
with open(path, encoding="utf-8") as fh:
    text = fh.read()
lines = text.split("\n")
has_header = any(l.strip() == header for l in lines)
if action == "add":
    if has_header:
        print("unchanged"); sys.exit(0)
    if dry:
        print("planned-add"); sys.exit(0)
    block = [mark, header, 'command = "python3"', "args = [" + json.dumps(server) + "]"]
    if extra:
        block.append(extra)
    new = text
    if new and not new.endswith("\n"):
        new += "\n"
    if new and not new.endswith("\n\n"):
        new += "\n"
    new += "\n".join(block) + "\n"
else:
    if not has_header:
        print("absent"); sys.exit(0)
    # Find our marker; the block runs from the marker to the next table header or EOF.
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == mark and i + 1 < len(lines) and lines[i + 1].strip() == header)
    except StopIteration:
        print("skipped-not-ours"); sys.exit(0)
    end = start + 2
    while end < len(lines) and not re.match(r"^\s*\[", lines[end]):
        end += 1
    # Also drop the single blank separator line we added before the block.
    if start > 0 and lines[start - 1].strip() == "":
        start -= 1
    if dry:
        print("planned-remove"); sys.exit(0)
    new = "\n".join(lines[:start] + lines[end:])
    if not new.endswith("\n"):
        new += "\n"
shutil.copy2(path, f"{path}.bak-fleet-rag-{ts}")
tmp = f"{path}.fleet-rag.tmp"
with open(tmp, "w", encoding="utf-8") as fh:
    fh.write(new)
try:
    os.chmod(tmp, os.stat(path).st_mode & 0o777)
except OSError:
    pass
os.replace(tmp, path)
print("added" if action == "add" else "removed")
PY
}

register_all() {
  local action="$1" r
  r="$(json_cfg "$CLAUDE_JSON" "$action" 0)";  say "$CLAUDE_JSON: $r";  note "$CLAUDE_JSON" "$r"
  r="$(json_cfg "$CURSOR_JSON" "$action" 0)";  say "$CURSOR_JSON: $r";  note "$CURSOR_JSON" "$r"
  r="$(json_cfg "$GEMINI_JSON" "$action" 1)";  say "$GEMINI_JSON: $r";  note "$GEMINI_JSON" "$r"
  r="$(toml_cfg "$CODEX_TOML" "$action" "")";  say "$CODEX_TOML: $r";  note "$CODEX_TOML" "$r"
  # Grok's existing [mcp_servers.X] blocks use command / args / enabled.
  r="$(toml_cfg "$GROK_TOML" "$action" "enabled = true")"; say "$GROK_TOML: $r"; note "$GROK_TOML" "$r"
  # grok-acp stripped home (Conductor / Shellular).  Absent until grok-acp-runtime is installed.
  r="$(toml_cfg "$ACP_TOML" "$action" "enabled = true")"; say "$ACP_TOML: $r"; note "$ACP_TOML" "$r"
}

# ---------------------------------------------------------------- step 4: seat-mcp

install_seat_mcp() {
  local files=(tools.py recall_bridge.py)
  for f in "${files[@]}"; do
    if [[ ! -f "$SRC/seat-mcp/seat_mcp/$f" ]]; then
      say "MISSING $SRC/seat-mcp/seat_mcp/$f" >&2
      [[ "$DRY" -eq 1 ]] || exit 1
    fi
  done
  if [[ "$DRY" -eq 1 ]]; then
    say "plan: copy seat_mcp/{tools.py,recall_bridge.py} -> $SEAT_DST/"
    note "$SEAT_DST" "planned"
  else
    mkdir -p "$SEAT_DST"
    for f in "${files[@]}"; do
      cp -p "$SRC/seat-mcp/seat_mcp/$f" "$SEAT_DST/$f"
    done
    say "installed $SEAT_DST/{tools.py,recall_bridge.py}"
    note "$SEAT_DST" "installed"
  fi
  say "next: pm2 restart seat-mcp   # not run by this script"
}

# ---------------------------------------------------------------- step 5: Claude Code hooks

# settings_hooks <add|remove>
# Appends exactly one matcher entry to hooks.SessionStart and hooks.Stop (identified by the
# hook file name in the command), or removes only those.  Every other key and entry is kept
# byte-for-byte in content (the file is re-serialized with indent 2).
# Prints: added | unchanged | removed | absent | skipped-not-object | planned-add | planned-remove
settings_hooks() {
  local action="$1"
  "$PY" - "$SETTINGS_JSON" "$action" "$DRY" "$HOOKS_DIR" "$HOOK_START" "$HOOK_STOP" "$TS" <<'PY'
import json, os, shutil, sys, tempfile
path, action, dry, hooks_dir, start, stop, ts = sys.argv[1:8]
dry = dry == "1"
ours = {
    "SessionStart": {"matcher": "startup|resume",
                     "hooks": [{"type": "command", "command": f"{hooks_dir}/{start}",
                                "timeout": 5, "statusMessage": "Fleet recall corpus"}]},
    "Stop": {"hooks": [{"type": "command", "command": f"python3 {hooks_dir}/{stop}", "timeout": 10}]},
}
names = {"SessionStart": start, "Stop": stop}

def is_ours(entry, fname):
    return isinstance(entry, dict) and any(
        isinstance(h, dict) and fname in str(h.get("command", "")) for h in entry.get("hooks") or [])

if not os.path.exists(path):
    if action == "remove":
        print("absent"); sys.exit(0)
    data, existed = {}, False
else:
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    data = json.loads(raw) if raw.strip() else {}
    existed = True
if not isinstance(data, dict):
    print("skipped-not-object"); sys.exit(0)
hooks = data.get("hooks")
if hooks is None:
    hooks = {}
if not isinstance(hooks, dict):
    print("skipped-bad-hooks"); sys.exit(0)
changed = False
for event, entry in ours.items():
    arr = hooks.get(event)
    if arr is None:
        arr = []
    if not isinstance(arr, list):
        print("skipped-bad-hooks"); sys.exit(0)
    have = [e for e in arr if is_ours(e, names[event])]
    if action == "add":
        if not have:
            arr = arr + [entry]; changed = True
        hooks[event] = arr
    elif have:
        arr = [e for e in arr if not is_ours(e, names[event])]; changed = True
        if arr:
            hooks[event] = arr
        else:
            hooks.pop(event, None)      # we were the only entry: restore the pre-install shape
if not changed:
    print("unchanged" if action == "add" else "absent"); sys.exit(0)
if dry:
    print("planned-add" if action == "add" else "planned-remove"); sys.exit(0)
if hooks:
    data["hooks"] = hooks
else:
    data.pop("hooks", None)
os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
if existed:
    shutil.copy2(path, f"{path}.bak-fleet-rag-{ts}")
fd, tmp = tempfile.mkstemp(prefix=".fleet-rag.", dir=os.path.dirname(path) or ".")
with os.fdopen(fd, "w", encoding="utf-8") as fh:
    json.dump(data, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
if existed:
    try:
        os.chmod(tmp, os.stat(path).st_mode & 0o777)
    except OSError:
        pass
else:
    os.chmod(tmp, 0o600)
os.replace(tmp, path)
print("added" if action == "add" else "removed")
PY
}

install_hooks() {
  local f r
  for f in "$HOOK_START" "$HOOK_STOP"; do
    if [[ ! -f "$SRC/hooks/$f" ]]; then
      say "MISSING $SRC/hooks/$f" >&2
      [[ "$DRY" -eq 1 ]] || exit 1
    fi
  done
  if [[ "$DRY" -eq 1 ]]; then
    say "plan: copy hooks/{$HOOK_START,$HOOK_STOP} -> $HOOKS_DIR/ (chmod +x)"
    note "$HOOKS_DIR" "planned"
  else
    mkdir -p "$HOOKS_DIR"
    for f in "$HOOK_START" "$HOOK_STOP"; do
      cp -p "$SRC/hooks/$f" "$HOOKS_DIR/$f"
      chmod +x "$HOOKS_DIR/$f"
    done
    say "installed $HOOKS_DIR/{$HOOK_START,$HOOK_STOP}"
    note "$HOOKS_DIR" "installed"
  fi
  r="$(settings_hooks add)"; say "$SETTINGS_JSON: $r"; note "$SETTINGS_JSON" "$r"
}

uninstall_hooks() {
  local f r
  r="$(settings_hooks remove)"; say "$SETTINGS_JSON: $r"; note "$SETTINGS_JSON" "$r"
  local any=0
  for f in "$HOOK_START" "$HOOK_STOP"; do
    if [[ -f "$HOOKS_DIR/$f" ]]; then
      any=1
      if [[ "$DRY" -eq 1 ]]; then
        say "plan: remove $HOOKS_DIR/$f"
      else
        rm -f "$HOOKS_DIR/$f"
        say "removed $HOOKS_DIR/$f"
      fi
    fi
  done
  if [[ "$any" -eq 0 ]]; then note "$HOOKS_DIR" "absent"
  elif [[ "$DRY" -eq 1 ]]; then note "$HOOKS_DIR" "planned-remove"
  else note "$HOOKS_DIR" "removed"; fi
}

# ---------------------------------------------------------------- main

if [[ "$DRY" -eq 1 ]]; then say "== fleet-rag installer: DRY RUN (nothing written) =="; fi
if [[ "$UNINSTALL" -eq 1 ]]; then
  say "== fleet-rag installer: uninstall =="
  register_all remove
  uninstall_hooks
  uninstall_link
  uninstall_files
else
  say "== fleet-rag installer: install =="
  install_files
  install_link
  register_all add
  if [[ "$WITH_SEAT" -eq 1 ]]; then
    install_seat_mcp
  else
    say "seat-mcp: skipped (pass --with-seat-mcp to refresh $SEAT_DST)"
    note "$SEAT_DST" "skipped"
  fi
  if [[ "$WITH_HOOKS" -eq 1 ]]; then
    install_hooks
  else
    say "hooks: skipped (pass --hooks to install the Claude Code SessionStart/Stop hooks)"
    note "$HOOKS_DIR" "skipped"
  fi
fi

say ""
say "== summary ($(mode_word)) =="
printf '%-60s %s\n' "target" "result"
printf '%-60s %s\n' "------" "------"
for row in "${SUMMARY[@]}"; do
  printf '%-60s %s\n' "${row%%|*}" "${row#*|}"
done
if [[ "$UNINSTALL" -eq 0 && "$DRY" -eq 0 ]]; then
  say ""
  say "next: restart Claude Code / Cursor / Gemini / Codex / Grok sessions so they pick up '$SERVER_NAME'."
fi
