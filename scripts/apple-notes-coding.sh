#!/usr/bin/env bash
# Create (or update) an Apple Note in the iCloud "Coding" folder and try to pin it.
# Owner preference 2026-08-05: coding notes always go to Coding + pin to top.
# Owner 2026-08-09: title + timestamp shape (ALL apps, ALL agents):
#
#   Title:  "[APP, Agent] short topic"   e.g. "[UM, Grok] TestFlight first ship"
#           Multi-app: "[ST, CT, Grok] …"  Acronyms: UM ST CT CTS FLEET
#   Row 2:  "Sun, Aug 9, 3:52pm"         local create/update stamp (auto-injected)
#
# Usage:
#   apple-notes-coding.sh "Title" "Plain body text"
#   apple-notes-coding.sh "Title" --html /path/to/body.html
#   apple-notes-coding.sh --update "Title" "Plain body text"   # refreshes timestamp
#   apple-notes-coding.sh --update "Title" --html /path/to/body.html
#   echo "body" | apple-notes-coding.sh "Title"
#   apple-notes-coding.sh --pin-only "Exact Note Title"
#
# Pin requires macOS Accessibility for osascript/Terminal (System Settings >
# Privacy & Security > Accessibility). Folder placement always works via AppleScript.
# Canonical policy: /Users/jay/apps/AGENT-SYNC.md § Apple Notes.

set -euo pipefail

MODE=create
TITLE=""
if [[ "${1:-}" == "--pin-only" ]]; then
  MODE=pin
  shift || true
  TITLE="${1:-}"
  shift || true
elif [[ "${1:-}" == "--update" ]]; then
  MODE=update
  shift || true
  TITLE="${1:-}"
  shift || true
else
  TITLE="${1:-}"
  shift || true
fi

if [[ -z "$TITLE" ]]; then
  echo "usage: $0 [--update|--pin-only] \"Title\" [body | --html path]" >&2
  exit 2
fi

if [[ "$MODE" == "pin" ]]; then
  NOTE_ID=$(osascript -e "tell application \"Notes\" to get id of note \"$TITLE\" of folder \"Coding\" of account \"iCloud\"" 2>/dev/null || true)
  [[ -n "$NOTE_ID" ]] || { echo "pin-only: note not found in Coding: $TITLE" >&2; exit 3; }
  SKIP_BODY=1
else
  SKIP_BODY=0
fi

# Markdown → HTML for Notes.app (no external deps). Notes does not render MD.
# Supports: #/##/### headings, **bold**, *italic*, `code`, [text](url),
# -/* bullets, 1. numbered lists, blank-line paragraphs, --- hr.
_md_to_html() {
  # Always read markdown from stdin (avoids argv size/quoting issues).
  python3 - <<'PY'
import html, re, sys

def inline(s: str) -> str:
    s = html.escape(s)
    # links [text](url) — after escape brackets still match
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        s,
    )
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"(?<!_)_([^_]+)_(?!_)", r"<i>\1</i>", s)
    return s

text = sys.stdin.read()
# normalize newlines
text = text.replace("\r\n", "\n").replace("\r", "\n")
lines = text.split("\n")
out = []
i = 0
in_ul = False
in_ol = False

def close_lists():
    global in_ul, in_ol
    if in_ul:
        out.append("</ul>")
        in_ul = False
    if in_ol:
        out.append("</ol>")
        in_ol = False

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    # blank
    if stripped == "":
        close_lists()
        i += 1
        continue

    # fenced code block
    if stripped.startswith("```"):
        close_lists()
        i += 1
        code_lines = []
        while i < len(lines) and not lines[i].strip().startswith("```"):
            code_lines.append(lines[i])
            i += 1
        if i < len(lines):
            i += 1  # closing fence
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
        continue

    # hr
    if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
        close_lists()
        out.append("<hr>")
        i += 1
        continue

    # headings
    m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
    if m:
        close_lists()
        level = min(len(m.group(1)), 4)  # Notes-friendly h1–h4
        out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
        i += 1
        continue

    # unordered list
    m = re.match(r"^[-*+]\s+(.*)$", stripped)
    if m:
        if in_ol:
            out.append("</ol>")
            in_ol = False
        if not in_ul:
            out.append("<ul>")
            in_ul = True
        out.append(f"<li>{inline(m.group(1))}</li>")
        i += 1
        continue

    # ordered list
    m = re.match(r"^\d+[.)]\s+(.*)$", stripped)
    if m:
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if not in_ol:
            out.append("<ol>")
            in_ol = True
        out.append(f"<li>{inline(m.group(1))}</li>")
        i += 1
        continue

    # paragraph (merge consecutive non-blank non-special lines)
    close_lists()
    para = [stripped]
    i += 1
    while i < len(lines):
        s2 = lines[i].strip()
        if s2 == "" or s2.startswith("#") or s2.startswith("```") or re.match(r"^[-*+]\s+", s2) or re.match(r"^\d+[.)]\s+", s2) or re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", s2):
            break
        para.append(s2)
        i += 1
    out.append("<p>" + inline(" ".join(para)) + "</p>")

close_lists()
print("<div>" + "".join(out) + "</div>")
PY
}

BODY_HTML=""
if [[ "$SKIP_BODY" == "0" ]]; then
if [[ "${1:-}" == "--html" ]]; then
  HTML_PATH="${2:-}"
  [[ -n "$HTML_PATH" && -f "$HTML_PATH" ]] || { echo "missing --html file" >&2; exit 2; }
  BODY_HTML=$(cat "$HTML_PATH")
elif [[ -n "${1:-}" ]]; then
  BODY_TEXT="$1"
  BODY_HTML=$(printf '%s' "$BODY_TEXT" | _md_to_html)
elif [[ ! -t 0 ]]; then
  BODY_TEXT=$(cat)
  BODY_HTML=$(printf '%s' "$BODY_TEXT" | _md_to_html)
else
  BODY_HTML="<div></div>"
fi

# Title shape check + ensure second-row timestamp (owner 2026-08-09).
# Title: "[APP, Agent] topic" — multi-app OK. Body first line: "Sun, Aug 9, 3:52pm".
# Do NOT put a second markdown # Title in the body — that doubles the title in Notes.
if ! printf '%s' "$TITLE" | grep -Eq '^\[[^]]+\][[:space:]]+'; then
  echo "warning: title should start with [APP, Agent] e.g. \"[UM, Grok] topic\" (got: $TITLE)" >&2
fi
if printf '%s' "$TITLE" | grep -Eiq 'session'; then
  echo "warning: do not put 'session' in Apple Note titles" >&2
fi

BODY_HTML=$(printf '%s' "$BODY_HTML" | /usr/bin/python3 -c "
import sys, re, html
from datetime import datetime
body = sys.stdin.read()
now = datetime.now()
# Sun, Aug 9, 3:52pm — no leading zero on day/hour (portable; avoid %-I)
_h = now.hour % 12 or 12
stamp = (
    now.strftime('%a, %b ')
    + str(now.day)
    + ', '
    + str(_h)
    + ':'
    + now.strftime('%M')
    + now.strftime('%p').lower()
)

def strip_outer_div(s):
    s = s.strip()
    if s.startswith('<div>') and s.endswith('</div>'):
        return s[5:-6]
    return s

inner = strip_outer_div(body).lstrip()
m = re.match(
    r'^(?:<p>)?\s*'
    r'(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun), '
    r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) '
    r'\d{1,2}, \d{1,2}:\d{2}[ap]m'
    r'\s*(?:</p>)?\s*',
    inner,
    re.I,
)
if m:
    inner = inner[m.end():]
stamp_p = '<p>' + html.escape(stamp) + '</p><div><br></div>'
sys.stdout.write('<div>' + stamp_p + inner + '</div>')
")

FULL_HTML=$(/usr/bin/python3 -c '
import html, sys
title = sys.argv[1]
body = sys.argv[2]
print("<h1>" + html.escape(title) + "</h1>" + body)
' "$TITLE" "$BODY_HTML")

TMP=$(mktemp /tmp/apple-note.XXXXXX)
printf '%s' "$FULL_HTML" >"$TMP"
trap 'rm -f "$TMP"' EXIT

if [[ "$MODE" == "update" ]]; then
  NOTE_ID=$(TITLE="$TITLE" TMP="$TMP" osascript <<'EOF'
set noteTitle to system attribute "TITLE"
set htmlPath to POSIX file (system attribute "TMP")
set htmlBody to read htmlPath as «class utf8»
tell application "Notes"
  set codingFolder to missing value
  try
    set codingFolder to folder "Coding" of account "iCloud"
  end try
  if codingFolder is missing value then
    tell account "iCloud"
      set codingFolder to make new folder with properties {name:"Coding"}
    end tell
  end if
  set targetNote to missing value
  try
    set targetNote to note noteTitle of codingFolder
  end try
  if targetNote is missing value then
    -- create if missing
    set targetNote to make new note at codingFolder with properties {body:htmlBody}
  else
    set body of targetNote to htmlBody
  end if
  show targetNote
  activate
  return id of targetNote
end tell
EOF
)
  echo "updated note id=$NOTE_ID in folder Coding title=$TITLE"
else
  NOTE_ID=$(osascript <<EOF
set htmlPath to POSIX file "$TMP"
set htmlBody to read htmlPath as «class utf8»

tell application "Notes"
  set codingFolder to missing value
  try
    set codingFolder to folder "Coding" of account "iCloud"
  end try
  if codingFolder is missing value then
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
fi
fi

# Best-effort pin via GUI (needs Accessibility for System Events).
# Deterministic selection: re-`show` the exact note by id, then menu-click, with retries —
# the old version pinned whatever happened to be selected, which failed (or could pin the
# wrong note) whenever creation focus was lost (2026-08-08 fix).
PIN_RESULT=$(NOTE_ID="$NOTE_ID" osascript <<'EOF' 2>&1 || true
set noteId to system attribute "NOTE_ID"
set pinned to false
repeat with attempt from 1 to 3
  tell application "Notes"
    try
      show note id noteId
    end try
    activate
  end tell
  delay (0.5 * attempt + 0.4)
  tell application "System Events"
    tell process "Notes"
      repeat with menuName in {"File", "Note", "Edit"}
        try
          if exists menu item "Unpin Note" of menu menuName of menu bar 1 then
            set pinned to true
            exit repeat
          end if
        end try
        try
          set mi to menu item "Pin Note" of menu menuName of menu bar 1
          if enabled of mi then
            click mi
            set pinned to true
            exit repeat
          end if
        end try
      end repeat
    end tell
  end tell
  if pinned then exit repeat
end repeat
if pinned then
  return "pinned"
else
  return "pin-menu-not-found"
end if
EOF
)

if [[ "$PIN_RESULT" == "pinned" ]]; then
  echo "pinned: yes"
elif echo "$PIN_RESULT" | grep -qi 'assistive access\|not allowed'; then
  echo "pinned: no (grant Accessibility to Terminal/iTerm/osascript, or right-click note → Pin Note)"
else
  echo "pinned: no ($PIN_RESULT) — right-click note in list → Pin Note"
fi
