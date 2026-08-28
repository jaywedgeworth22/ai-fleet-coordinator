#!/usr/bin/env python3
"""Tests for generic Grok TUI drive helpers.  No live inject into this TUI."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
DISK = REPO / "scripts" / "grok-acp-runtime"
sys.path.insert(0, str(DISK))

from session_disk import (  # noqa: E402
    enrich_sessions,
    is_self_session,
    peek_summary,
    peek_tail,
    poll_after_inject,
    poll_until_idle,
    prefix_prompt,
    turn_state,
)

LIVE_ID = "01a04521-e2e0-7403-9c44-cb8ee340330b"
DRIVE = DISK / "grok-drive.py"


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


class PrefixTests(unittest.TestCase):
    def test_default_remote(self) -> None:
        os.environ.pop("AGENT_TAG", None)
        os.environ.pop("AGENT_SEAT", None)
        self.assertTrue(prefix_prompt("hello", None).startswith("[from: remote]"))

    def test_named(self) -> None:
        self.assertEqual(prefix_prompt("hello", "CLAUDE"), "[from: CLAUDE] hello")

    def test_idempotent(self) -> None:
        once = prefix_prompt("hello", "CURSOR")
        self.assertEqual(prefix_prompt(once, "CURSOR"), once)


class DiskTests(unittest.TestCase):
    def test_peek_live(self) -> None:
        out = peek_summary(LIVE_ID)
        self.assertTrue(out.get("ok"), out)
        self.assertEqual(out.get("cwd"), "/Users/jay/Code")
        self.assertIn(out.get("turnState"), {"idle", "working", "needs-input", "unknown"})

    def test_tail_live(self) -> None:
        out = peek_tail(LIVE_ID, lines=3)
        self.assertTrue(out.get("ok"), out)
        self.assertIsInstance(out.get("tail"), list)

    def test_turn_state_shape(self) -> None:
        st = turn_state(LIVE_ID)
        self.assertEqual(st.get("sessionId"), LIVE_ID)
        self.assertIn(st.get("turnState"), {"idle", "working", "needs-input", "unknown"})
        self.assertTrue(st.get("live"))
        self.assertIn("pendingTool", st)

    def test_enrich_adds_turn_state(self) -> None:
        rows = enrich_sessions([{"sessionId": LIVE_ID, "cwd": "/Users/jay/Code"}])
        self.assertTrue(rows)
        self.assertIn("turnState", rows[0])
        self.assertTrue(rows[0].get("live"))


class DriveCliTests(unittest.TestCase):
    def test_grok_drive_has_generic_commands(self) -> None:
        src = DRIVE.read_text(encoding="utf-8")
        for needle in (
            "await",
            "tail",
            "cancel",
            "--queue",
            "--from-name",
            "--await-reply",
            "--self",
            "poll_after_inject",
            "Not Grok-Bot-only",
        ):
            self.assertIn(needle, src)

    def test_self_guard_refuses_own_session(self) -> None:
        env = os.environ.copy()
        env["GROK_SESSION_ID"] = "self-session-id"
        proc = subprocess.run(
            [
                "/usr/bin/python3",
                str(DRIVE),
                "prompt",
                "--session-id",
                "self-session-id",
                "--cwd",
                "/Users/jay/apps",
                "--prompt",
                "should-not-inject",
            ],
            capture_output=True,
            text=True,
            env=env,
            timeout=10,
            check=False,
        )
        data = json.loads(proc.stdout or "{}")
        self.assertEqual(proc.returncode, 3)
        self.assertFalse(data.get("ok"))
        self.assertTrue(data.get("self"))
        self.assertIn("GROK_SESSION_ID", data.get("error") or "")

    def test_self_guard_off_when_env_unset(self) -> None:
        self.assertFalse(is_self_session("self-session-id"))


class AfterInjectTests(unittest.TestCase):
    def test_skips_preexisting_idle(self) -> None:
        states = [
            {
                "turnState": "idle",
                "turnStartedAt": 1.0,
                "turnEndedAt": 1.5,
                "pendingTool": None,
                "phase": None,
            },
            {
                "turnState": "working",
                "turnStartedAt": 2.0,
                "turnEndedAt": 1.5,
                "pendingTool": None,
                "phase": None,
            },
            {
                "turnState": "idle",
                "turnStartedAt": 2.0,
                "turnEndedAt": 3.0,
                "pendingTool": None,
                "phase": None,
            },
        ]
        it = iter(states)

        def fake_state(_sid: str):
            try:
                return next(it)
            except StopIteration:
                return states[-1]

        with patch("session_disk.turn_state", side_effect=fake_state), patch(
            "session_disk.peek_summary",
            return_value={"ok": True, "text": "done"},
        ):
            out = poll_after_inject("x", before_started=1.0, timeout=2.0, interval=0.0)
        self.assertEqual(out.get("await"), "idle")
        self.assertTrue(out.get("sawNewTurn"))
        self.assertEqual(out.get("turnStartedAt"), 2.0)

    def test_timeout_if_no_new_turn(self) -> None:
        idle = {
            "turnState": "idle",
            "turnStartedAt": 1.0,
            "turnEndedAt": 1.5,
            "pendingTool": None,
            "phase": None,
        }
        with patch("session_disk.turn_state", return_value=idle), patch(
            "session_disk.peek_summary",
            return_value={"ok": True, "text": "old"},
        ):
            out = poll_after_inject("x", before_started=1.0, timeout=0.05, interval=0.01)
        self.assertEqual(out.get("await"), "timeout")
        self.assertFalse(out.get("sawNewTurn"))

    def test_poll_until_idle_returns_immediately_when_idle(self) -> None:
        idle = {
            "turnState": "idle",
            "turnStartedAt": 1.0,
            "turnEndedAt": 1.5,
            "pendingTool": None,
            "phase": None,
        }
        with patch("session_disk.turn_state", return_value=idle), patch(
            "session_disk.peek_summary",
            return_value={"ok": True, "text": "now"},
        ):
            out = poll_until_idle("x", timeout=2.0, interval=0.0)
        self.assertEqual(out.get("await"), "idle")


class PendingToolTests(unittest.TestCase):
    def test_unresolved_permission(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            sid = "sess-perm"
            d = root / "cwd" / sid
            d.mkdir(parents=True)
            now = _iso_now()
            events = [
                {"ts": now, "type": "turn_started"},
                {"ts": now, "type": "permission_requested", "tool_name": "run_terminal_command"},
                {"ts": now, "type": "phase_changed", "phase": "permission_prompt"},
            ]
            (d / "events.jsonl").write_text(
                "\n".join(json.dumps(e) for e in events) + "\n", encoding="utf-8"
            )
            (d / "summary.json").write_text(
                json.dumps({
                    "info": {"cwd": "/Users/jay/apps"},
                    "last_turn_summary": "waiting",
                    "generated_title": "perm",
                }),
                encoding="utf-8",
            )
            (root / "active.json").write_text(
                json.dumps([{"session_id": sid, "cwd": "/Users/jay/apps", "pid": 1}]),
                encoding="utf-8",
            )
            with patch("session_disk.SESSIONS_ROOT", root), patch(
                "session_disk.ACTIVE_SESSIONS", root / "active.json"
            ):
                st = turn_state(sid)
                peek = peek_summary(sid)
            self.assertEqual(st.get("turnState"), "needs-input")
            self.assertEqual(st.get("pendingTool"), "run_terminal_command")
            self.assertEqual(peek.get("pendingTool"), "run_terminal_command")

    def test_resolved_permission_clears(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            sid = "sess-ok"
            d = root / "cwd" / sid
            d.mkdir(parents=True)
            now = _iso_now()
            events = [
                {"ts": now, "type": "turn_started"},
                {"ts": now, "type": "permission_requested", "tool_name": "read_file"},
                {
                    "ts": now,
                    "type": "permission_resolved",
                    "tool_name": "read_file",
                    "decision": "allow",
                },
                {"ts": now, "type": "turn_ended"},
            ]
            (d / "events.jsonl").write_text(
                "\n".join(json.dumps(e) for e in events) + "\n", encoding="utf-8"
            )
            (d / "summary.json").write_text(
                json.dumps({"info": {"cwd": "/Users/jay/apps"}}),
                encoding="utf-8",
            )
            with patch("session_disk.SESSIONS_ROOT", root), patch(
                "session_disk.ACTIVE_SESSIONS", root / "none.json"
            ):
                st = turn_state(sid)
            self.assertIsNone(st.get("pendingTool"))
            self.assertEqual(st.get("turnState"), "idle")


class InstallScriptTests(unittest.TestCase):
    def test_bash_syntax(self) -> None:
        script = REPO / "scripts" / "install-grok-tui-drive.sh"
        self.assertTrue(script.is_file())
        proc = subprocess.run(
            ["bash", "-n", str(script)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_dry_run_mentions_dest(self) -> None:
        script = REPO / "scripts" / "install-grok-tui-drive.sh"
        proc = subprocess.run(
            ["bash", str(script), "--dry-run"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("grok-drive.py", proc.stdout)
        self.assertIn("seat-mcp-launch.sh", proc.stdout)
        src = script.read_text(encoding="utf-8")
        self.assertIn("refusing pm2 restart", src)
        self.assertIn("never a second bind", src)

    def test_launchers_tracked(self) -> None:
        launch = REPO / "scripts" / "mcp-servers" / "seat-mcp-launch.sh"
        proxy = REPO / "scripts" / "mcp-servers" / "seat-mcp-stdio-proxy.py"
        self.assertTrue(launch.is_file())
        self.assertTrue(proxy.is_file())
        src = proxy.read_text(encoding="utf-8")
        self.assertIn("SEAT_MCP_TOKEN", src)
        self.assertIn("127.0.0.1:8793", src)
        self.assertNotIn("print(token", src)


if __name__ == "__main__":
    unittest.main()
