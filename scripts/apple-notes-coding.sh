#!/usr/bin/env bash
# Create (or update) an Apple Note in the iCloud "Coding" folder and try to pin it.
# Owner preference 2026-08-05: coding notes always go to Coding + pin to top.
#
# Usage:
#   apple-notes-coding.sh "Title" "Plain body text"
#   apple-notes-coding.sh "Title" --html /path/to/body.html
#   echo "body" | apple-notes-coding.sh "Title"
#
# Pin requires macOS Accessibility for osascript/Terminal (System Settings >
# Privacy & Security > Accessibility). Folder placement always works via AppleScript.

set -euo pipefail

TITLE="${1:-}"
if [[ -z "$TITLE" ]]; then
  echo "usage: $0 \"Title\" [body | --html path]" >&2
  exit 2
fi
shift || true

BODY_HTML=""
if [[ "${1:-}" == "--html" ]]; then
  HTML_PATH="${2:-}"
  [[ -n "$HTML_PATH" && -f "$HTML_PATH" ]] || { echo "missing --html file" >&2; exit 2; }
  BODY_HTML=$(cat "$HTML_PATH")
elif [[ -n "${1:-}" ]]; then
  # Escape for AppleScript string
  BODY_TEXT="$1"
  BODY_HTML=$(python3 -c 'import html,sys; print("<div>"+html.escape(sys.argv[1]).replace("\n","<br>")+"</div>")' "$BODY_TEXT")
elif [[ ! -t 0 ]]; then
  BODY_TEXT=$(cat)
  BODY_HTML=$(python3 -c 'import html,sys; print("<div>"+html.escape(sys.stdin.read()).replace("\n","<br>")+"</div>")' <<<"$BODY_TEXT")
else
  BODY_HTML="<div></div>"
fi

# Build full HTML note: first line becomes the title in Notes
FULL_HTML=$(python3 -c '
import html, sys
title = sys.argv[1]
body = sys.argv[2]
print("<h1>" + html.escape(title) + "</h1>" + body)
' "$TITLE" "$BODY_HTML")

# Write body to temp for osascript (avoid shell quoting hell)
TMP=$(mktemp /tmp/apple-note-XXXXXX.html)
printf '%s' "$FULL_HTML" >"$TMP"
trap 'rm -f "$TMP"' EXIT

NOTE_ID=$(osascript <<EOF
set htmlPath to POSIX file "$TMP"
set htmlBody to read htmlPath as «class utf8»

tell application "Notes"
  set codingFolder to missing value
  try
    set codingFolder to folder "Coding" of account "iCloud"
  end try
  if codingFolder is missing value then
    -- create Coding under iCloud if missing
    tell account "iCloud"
      set codingFolder to make new folder with properties {name:"Coding"}
    end tell
  end if

  set newNote to make new note at codingFolder with properties {body:htmlBody}
  show newNote
  activate
  return id of newNote
end tell
EOF
)

echo "created note id=$NOTE_ID in folder Coding"

# Best-effort pin via GUI (needs Accessibility for System Events)
PIN_RESULT=$(osascript <<'EOF' 2>&1 || true
tell application "Notes" to activate
delay 0.6
tell application "System Events"
  tell process "Notes"
    set pinned to false
    -- Try File menu then Note menu
    repeat with menuName in {"File", "Note", "Edit"}
      try
        set mi to menu item "Pin Note" of menu menuName of menu bar 1
        if enabled of mi then
          click mi
          set pinned to true
          exit repeat
        end if
      end try
      -- already pinned?
      try
        if exists menu item "Unpin Note" of menu menuName of menu bar 1 then
          set pinned to true
          exit repeat
        end if
      end try
    end repeat
    if pinned then
      return "pinned"
    else
      return "pin-menu-not-found"
    end if
  end tell
end tell
EOF
)

if [[ "$PIN_RESULT" == "pinned" ]]; then
  echo "pinned: yes"
elif echo "$PIN_RESULT" | grep -qi 'assistive access\|not allowed'; then
  echo "pinned: no (grant Accessibility to Terminal/iTerm/osascript, or right-click note → Pin Note)"
else
  echo "pinned: no ($PIN_RESULT) — right-click note in list → Pin Note"
fi
