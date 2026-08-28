#!/usr/bin/env python3
"""Friendly CLI for Grok Bot / Conductor to drive Mac Grok sessions.

list / peek / prompt  → shared leader (live TUI chats)
new                   → grok-acp :12419 (new session, not the TUI)

Never prints GROK_AGENT_SECRET or SEAT_MCP_TOKEN.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEADER = HERE / "leader-client.py"
ACP = HERE / "acp-client.py"
PY = "/usr/bin/python3"
ACTIVE = Path.home() / ".grok" / "active_sessions.json"


def run_json(argv, timeout):
    proc = subprocess.run(
        argv,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    blob = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    data = None
    src = blob or err
    if src:
        try:
            data = json.loads(src)
        except json.JSONDecodeError:
            start = src.find("{")
            try:
                data = json.loads(src[start:] if start >= 0 else src)
            except json.JSONDecodeError:
                data = {"ok": False, "error": src[:800]}
    if data is None:
        data = {"ok": False, "error": "empty helper output", "exitCode": proc.returncode}
    if proc.returncode != 0 and data.get("ok") is not False:
        data = dict(data)
        data["ok"] = False
        data.setdefault("exitCode", proc.returncode)
    return data, proc.returncode


def load_active():
    if not ACTIVE.is_file():
        return []
    try:
        raw = json.loads(ACTIVE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    if not isinstance(raw, list):
        return []
    out = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        sid = item.get("session_id") or item.get("sessionId")
        if not sid:
            continue
        out.append({
            "sessionId": str(sid),
            "cwd": item.get("cwd"),
            "pid": item.get("pid"),
            "openedAt": item.get("opened_at") or item.get("openedAt"),
            "live": True,
        })
    return out


def merge_live(sessions):
    active = {a["sessionId"]: a for a in load_active()}
    merged = []
    seen = set()
    for s in sessions:
        sid = s.get("sessionId")
        row = dict(s)
        if sid in active:
            row["live"] = True
            row["pid"] = active[sid].get("pid")
            row["openedAt"] = active[sid].get("openedAt")
            seen.add(sid)
        else:
            row.setdefault("live", False)
        merged.append(row)
    for sid, a in active.items():
        if sid not in seen:
            merged.append({
                "sessionId": sid,
                "cwd": a.get("cwd"),
                "title": None,
                "updatedAt": a.get("openedAt"),
                "live": True,
                "pid": a.get("pid"),
                "openedAt": a.get("openedAt"),
                "note": "in active_sessions.json; leader list missed it",
            })
    return merged


def cmd_list(args):
    argv = [PY, str(LEADER), "list"]
    if args.cwd:
        argv.extend(["--cwd", args.cwd])
    data, code = run_json(argv, timeout=25)
    sessions = merge_live(data.get("sessions") or [])
    out = {
        "ok": bool(data.get("ok", code == 0)),
        "count": len(sessions),
        "sessions": sessions,
    }
    if data.get("error"):
        out["leaderError"] = data.get("error")
        # Still useful: live TUI rows from the json file.
        if sessions:
            out["ok"] = True
            out["partial"] = True
    print(json.dumps(out, indent=2))
    return 0 if out.get("ok") else 1


def cmd_peek(args):
    argv = [PY, str(LEADER), "peek", "--session-id", args.session_id, "--cwd", args.cwd]
    data, code = run_json(argv, timeout=50)
    print(json.dumps(data, indent=2))
    return code


def cmd_prompt(args):
    argv = [
        PY, str(LEADER), "prompt",
        "--session-id", args.session_id,
        "--cwd", args.cwd,
        "--prompt", args.prompt,
        "--timeout", str(args.timeout),
    ]
    if getattr(args, "wait", False):
        argv.append("--wait")
    data, code = run_json(argv, timeout=float(args.timeout) + 20)
    print(json.dumps(data, indent=2))
    return code


def cmd_new(args):
    argv = [PY, str(ACP), "new", "--cwd", args.cwd, "--prompt", args.prompt]
    data, code = run_json(argv, timeout=float(args.timeout) + 20)
    print(json.dumps(data, indent=2))
    return code


def main():
    p = argparse.ArgumentParser(description="Drive Mac Grok TUI / grok-acp sessions")
    sub = p.add_subparsers(dest="cmd", required=True)
    ls = sub.add_parser("list", help="live TUI chats via the shared leader")
    ls.add_argument("--cwd", default="")
    pk = sub.add_parser("peek")
    pk.add_argument("--session-id", required=True)
    pk.add_argument("--cwd", default="/Users/jay")
    pr = sub.add_parser("prompt", help="inject a follow-up into a live TUI chat (returns when queued)")
    pr.add_argument("--session-id", required=True)
    pr.add_argument("--prompt", required=True)
    pr.add_argument("--cwd", default="/Users/jay")
    pr.add_argument("--timeout", type=float, default=12.0)
    pr.add_argument("--wait", action="store_true", help="wait for the TUI turn to finish")
    nw = sub.add_parser("new", help="new grok-acp session on :12419 (not the TUI)")
    nw.add_argument("--prompt", required=True)
    nw.add_argument("--cwd", default="/Users/jay/apps")
    nw.add_argument("--timeout", type=float, default=180.0)
    args = p.parse_args()
    if args.cmd == "list":
        raise SystemExit(cmd_list(args))
    if args.cmd == "peek":
        raise SystemExit(cmd_peek(args))
    if args.cmd == "prompt":
        raise SystemExit(cmd_prompt(args))
    if args.cmd == "new":
        raise SystemExit(cmd_new(args))


if __name__ == "__main__":
    try:
        main()
    except subprocess.TimeoutExpired:
        print(json.dumps({"ok": False, "error": "helper timed out"}), file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(1)
