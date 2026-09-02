#!/usr/bin/env python3
"""Close live Grok TUI chats idle longer than 12h.

session/close unloads that chat's MCP tool processes.  Disk history
(summary.json / updates.jsonl) is not deleted.  Resume via /resume
(or grok --resume ID) — tools come back on the next turn.

Never closes working, needs-input, pendingTool, or $GROK_SESSION_ID.
Optional --reap-orphans SIGTERMs MCP children whose GROK_SESSION_ID is
no longer live and whose session is missing or also idle >12h.
Override hours with GROK_IDLE_UNLOAD_HOURS or --max-age-hours.

On-demand:
  python3 ~/apps/grok-acp-runtime/grok-idle-unload.py --dry-run
  python3 ~/apps/grok-acp-runtime/grok-idle-unload.py

Hourly launchd: com.jay.grok-idle-unload
"""
from __future__ import annotations

import argparse
import json
import os
import re
import signal
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from session_disk import (  # noqa: E402
    DEFAULT_IDLE_UNLOAD_SEC,
    enrich_sessions,
    find_session_dir,
    idle_age_seconds,
    load_active,
    peek_summary,
    select_idle_unload,
    self_session_id,
    unload_skip_reason,
)

LEADER = HERE / "leader-client.py"
PY = "/usr/bin/python3"
SESSION_ID_RE = re.compile(
    r"(?:^|\s)GROK_SESSION_ID=([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})(?:\s|$)"
)
JsonDict = dict[str, Any]


def _run_leader(argv: list[str], timeout: float) -> JsonDict:
    proc = subprocess.run(
        argv,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    blob = (proc.stdout or "").strip() or (proc.stderr or "").strip()
    data: JsonDict
    try:
        data = json.loads(blob[blob.find("{") :] if blob.find("{") >= 0 else blob)
    except json.JSONDecodeError:
        data = {"ok": False, "error": blob[:800] or "empty helper output"}
    if proc.returncode != 0 and data.get("ok") is not False:
        data = dict(data)
        data["ok"] = False
        data.setdefault("exitCode", proc.returncode)
    return data


def list_sessions() -> list[JsonDict]:
    data = _run_leader([PY, str(LEADER), "list"], timeout=25)
    return enrich_sessions(data.get("sessions") or [])


def close_session(session_id: str, cwd: str) -> JsonDict:
    argv = [PY, str(LEADER), "close", "--session-id", session_id, "--cwd", cwd or "/Users/jay"]
    data = _run_leader(argv, timeout=20)
    data["diskKept"] = find_session_dir(session_id) is not None
    if not data.get("diskKept"):
        data["ok"] = False
        data["error"] = "session/close removed disk history — unexpected"
    return data


def _ps_pid_ppid_comm() -> list[tuple[int, int, str]]:
    out = subprocess.check_output(["ps", "-axo", "pid=,ppid=,comm="], text=True)
    rows: list[tuple[int, int, str]] = []
    for line in out.splitlines():
        parts = line.split(None, 2)
        if len(parts) < 3:
            continue
        try:
            rows.append((int(parts[0]), int(parts[1]), parts[2]))
        except ValueError:
            continue
    return rows


def leader_pid() -> int | None:
    # Match the leader argv without dumping env (secrets live on some children).
    try:
        out = subprocess.check_output(
            ["ps", "-axo", "pid=,command="],
            text=True,
        )
    except subprocess.CalledProcessError:
        return None
    for line in out.splitlines():
        if "grok agent" in line and "leader" in line and "grok-idle-unload" not in line:
            pid_s = line.split(None, 1)[0]
            try:
                return int(pid_s)
            except ValueError:
                continue
    return None


def _descendants(root: int) -> list[int]:
    by_ppid: dict[int, list[int]] = {}
    for pid, ppid, _comm in _ps_pid_ppid_comm():
        by_ppid.setdefault(ppid, []).append(pid)
    out: list[int] = []
    stack = [root]
    seen = {root}
    while stack:
        p = stack.pop()
        for child in by_ppid.get(p, []):
            if child in seen:
                continue
            seen.add(child)
            out.append(child)
            stack.append(child)
    return out


def grok_session_id_from_pid(pid: int) -> str | None:
    """Read GROK_SESSION_ID from a process env.  Never logs the command line."""
    try:
        out = subprocess.check_output(
            ["ps", "eww", "-p", str(pid), "-o", "command="],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    m = SESSION_ID_RE.search(out)
    return m.group(1) if m else None


def reap_orphan_mcp(
    *,
    live_ids: set[str],
    now: float,
    max_idle_sec: float,
    dry_run: bool,
) -> list[JsonDict]:
    lead = leader_pid()
    if lead is None:
        return []
    actions: list[JsonDict] = []
    for pid in _descendants(lead):
        sid = grok_session_id_from_pid(pid)
        if not sid or sid in live_ids:
            continue
        peek = peek_summary(sid)
        age = idle_age_seconds(peek, now) if peek.get("ok") else max_idle_sec + 1
        missing = not peek.get("ok")
        if not missing and age < max_idle_sec:
            continue
        rec: JsonDict = {
            "pid": pid,
            "sessionId": sid,
            "missingSessionDir": missing,
            "idleSec": int(age),
            "action": "sigterm" if not dry_run else "would_sigterm",
        }
        if not dry_run:
            try:
                os.kill(pid, signal.SIGTERM)
                rec["ok"] = True
            except ProcessLookupError:
                rec["ok"] = True
                rec["action"] = "already_gone"
            except PermissionError as exc:
                rec["ok"] = False
                rec["error"] = str(exc)
        else:
            rec["ok"] = True
        actions.append(rec)
    return actions


def main() -> int:
    p = argparse.ArgumentParser(description="Unload MCP on Grok chats idle >12h without deleting them")
    p.add_argument("--dry-run", action="store_true")
    env_hours = os.environ.get("GROK_IDLE_UNLOAD_HOURS", "").strip()
    default_hours = DEFAULT_IDLE_UNLOAD_SEC / 3600.0
    if env_hours:
        try:
            parsed = float(env_hours)
            if parsed > 0:
                default_hours = parsed
        except ValueError:
            pass
    p.add_argument("--max-age-hours", type=float, default=default_hours)
    p.add_argument("--reap-orphans", action="store_true", default=True)
    p.add_argument("--no-reap-orphans", action="store_false", dest="reap_orphans")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    max_idle_sec = float(args.max_age_hours) * 3600.0
    if max_idle_sec <= 0:
        max_idle_sec = float(DEFAULT_IDLE_UNLOAD_SEC)
    now = time.time()
    self_id = self_session_id()
    rows = list_sessions()
    skipped = []
    for row in rows:
        reason = unload_skip_reason(
            row, now=now, max_idle_sec=max_idle_sec, self_id=self_id
        )
        if reason:
            skipped.append({
                "sessionId": row.get("sessionId"),
                "reason": reason,
                "live": bool(row.get("live")),
                "turnState": row.get("turnState"),
                "idleSec": int(idle_age_seconds(row, now)),
            })
    candidates = select_idle_unload(
        rows, now=now, max_idle_sec=max_idle_sec, self_id=self_id
    )
    closed: list[JsonDict] = []
    for row in candidates:
        sid = str(row.get("sessionId"))
        rec: JsonDict = {
            "sessionId": sid,
            "title": row.get("title"),
            "idleSec": int(idle_age_seconds(row, now)),
            "cwd": row.get("cwd"),
        }
        if args.dry_run:
            rec["action"] = "would_close"
            rec["ok"] = True
            rec["diskKept"] = find_session_dir(sid) is not None
        else:
            rec["action"] = "session/close"
            rec.update(close_session(sid, str(row.get("cwd") or "/Users/jay")))
        closed.append(rec)

    live_ids = {a["sessionId"] for a in load_active()}
    if self_id:
        live_ids.add(self_id)
    orphans: list[JsonDict] = []
    if args.reap_orphans:
        orphans = reap_orphan_mcp(
            live_ids=live_ids,
            now=now,
            max_idle_sec=max_idle_sec,
            dry_run=args.dry_run,
        )

    out = {
        "ok": all(r.get("ok") is not False for r in closed + orphans),
        "dryRun": bool(args.dry_run),
        "maxAgeHours": args.max_age_hours,
        "selfSessionId": self_id or None,
        "listed": len(rows),
        "closed": closed,
        "skipped": skipped,
        "orphans": orphans,
    }
    print(json.dumps(out, indent=2))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired:
        print(json.dumps({"ok": False, "error": "helper timed out"}), file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(1)
