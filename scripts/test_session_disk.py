#!/usr/bin/env python3
"""Tests for generic Grok TUI drive helpers.  No live inject."""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path

LIVE = Path("/Users/jay/apps/grok-acp-runtime")
sys.path.insert(0, str(LIVE))

from session_disk import (  # noqa: E402
    enrich_sessions,
    peek_summary,
    peek_tail,
    prefix_prompt,
    turn_state,
)

LIVE_ID = "01a04521-e2e0-7403-9c44-cb8ee340330b"


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

    def test_enrich_adds_turn_state(self) -> None:
        rows = enrich_sessions([{"sessionId": LIVE_ID, "cwd": "/Users/jay/Code"}])
        self.assertTrue(rows)
        self.assertIn("turnState", rows[0])
        self.assertTrue(rows[0].get("live"))


class DriveCliTests(unittest.TestCase):
    def test_grok_drive_has_generic_commands(self) -> None:
        src = (LIVE / "grok-drive.py").read_text(encoding="utf-8")
        for needle in ("await", "tail", "cancel", "--queue", "--from-name", "--await-reply", "Not Grok-Bot-only"):
            self.assertIn(needle, src)


if __name__ == "__main__":
    unittest.main()
