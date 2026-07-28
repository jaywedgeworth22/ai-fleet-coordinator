#!/usr/bin/env python3
"""Shared #agent-sync poller — one pass; any agent, own cursor.

Usage:  AGENT_TAG=CODEX /usr/bin/python3 ~/apps/agent-sync-poll.py
   or:  /usr/bin/python3 ~/apps/agent-sync-poll.py CODEX

Prints one line per NEW message not authored by you (matched on your tag
prefix), then advances your private cursor. Run it in a 20-60s loop for a
realtime watcher, or single-pass at turn/session start for turn-based agents.
Token comes from ~/.secrets/agent-sync.env (never printed).
Protocol: ~/apps/AGENT-SYNC.md
"""
import json, os, sys, urllib.request, urllib.parse

ENV_FILE = "~/.secrets/agent-sync.env"
CHANNEL = "C0BEZDJDNKV"
THREAD = "1783180934.001309"

tag = (os.environ.get("AGENT_TAG") or (sys.argv[1] if len(sys.argv) > 1 else "")).strip().upper()
if not tag:
    print("ERR no AGENT_TAG (env var or argv[1])"); sys.exit(1)

STATE_DIR = os.path.expanduser("~/.agent-sync")
os.makedirs(STATE_DIR, exist_ok=True)
CURSOR = os.path.join(STATE_DIR, f"{tag}-cursor.txt")

tok = ""
try:
    for line in open(ENV_FILE):
        line = line.strip()
        if line.startswith("SLACK_MONET_TOKEN=") or line.startswith("AGENT_SYNC_TOKEN=") or line.startswith("SLACK_BOT_TOKEN="):
            tok = line.split("=", 1)[1]
except FileNotFoundError:
    print(f"ERR env file missing: {ENV_FILE}"); sys.exit(1)
if not tok:
    print("ERR no token line in env file"); sys.exit(1)


def slack(method, params):
    qs = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"https://slack.com/api/{method}?{qs}",
                                 headers={"Authorization": "Bearer " + tok})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)


cur = "0"
if os.path.exists(CURSOR):
    cur = open(CURSOR).read().strip() or "0"

msgs = []
try:
    h = slack("conversations.history", {"channel": CHANNEL, "oldest": cur, "limit": 50})
    if not h.get("ok"):
        print("ERR " + h.get("error", "unknown")); sys.exit(0)
    msgs += h.get("messages", [])
    t = slack("conversations.replies", {"channel": CHANNEL, "ts": THREAD, "oldest": cur, "limit": 50})
    if t.get("ok"):
        msgs += t.get("messages", [])
except Exception as exc:
    print("ERR " + type(exc).__name__); sys.exit(0)

fresh = {}
for m in msgs:
    ts = m.get("ts")
    if ts and float(ts) > float(cur):
        fresh[ts] = m
if not fresh:
    sys.exit(0)

# Self-filter per AGENT-SYNC.md "Self-message filtering convention" (2026-07-08): bodies are
# repo-FIRST ("repo: <project> | [TAG->...]"), so match the tag as a SUBSTRING in the first 80
# chars — startswith never fires. Multi-session seats set AGENT_SYNC_NO_SELF_FILTER=1 (a tag
# filter would also hide their sibling sessions' messages).
own = (f"[{tag}", f"⟦{tag}")
no_self_filter = os.environ.get("AGENT_SYNC_NO_SELF_FILTER") == "1"
for ts in sorted(fresh, key=float):
    text = (fresh[ts].get("text") or "").replace("\n", " ¶ ")
    if text.strip() and (no_self_filter or not any(m in text[:80] for m in own)):
        print(f"SYNC[{ts}] {text[:600]}", flush=True)
open(CURSOR, "w").write(max(fresh, key=float))
