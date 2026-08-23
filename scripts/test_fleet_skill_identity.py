#!/usr/bin/env python3
"""Tests for per-seat fleet skill identity specialization."""

from __future__ import annotations

import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from fleet_skill_identity import SEATS, specialize_from_monet  # noqa: E402

SESSION = os.path.join(ROOT, "docs", "fleet-skills", "session-start", "SKILL.md")
GAP = os.path.join(ROOT, "docs", "fleet-skills", "sentence-gap", "SKILL.md")


class SpecializeTests(unittest.TestCase):
    def test_cursor_does_not_keep_monet_tag(self) -> None:
        src = open(SESSION, encoding="utf-8").read()
        out = specialize_from_monet(src, SEATS["cursor"], skill_name="session-start")
        self.assertIn("AGENT_SEAT=CURSOR", out)
        self.assertNotIn("AGENT_SEAT=MONET", out)
        self.assertIn("[CURSOR]", out)
        self.assertNotIn("AGENT_TAG=MONET", out)
        self.assertIn("Never post Slack as `[MONET]`", out)
        self.assertIn("cursor/<slug>", out)
        self.assertNotIn("two different Claude accounts", out)
        self.assertIn("Never post Slack as `[MONET]`", out)
        self.assertIn("This install is for `CURSOR`", out)

    def test_sentence_gap_keeps_portable_protocol_name(self) -> None:
        src = open(GAP, encoding="utf-8").read()
        out = specialize_from_monet(src, SEATS["cursor"], skill_name="sentence-gap")
        self.assertTrue(
            "Monet portable" in out or "Monet's portable" in out or "Monet portable" in out,
            out[:500],
        )

    def test_claude_shared_banner_and_pin(self) -> None:
        src = open(SESSION, encoding="utf-8").read()
        out = specialize_from_monet(src, SEATS["claude_shared"], skill_name="session-start")
        self.assertIn("Shared `~/.claude/skills`", out)
        self.assertIn("MONET or CLAUDE", out)

    def test_ag_worktree_suffix_differs_from_prefix(self) -> None:
        src = open(SESSION, encoding="utf-8").read()
        out = specialize_from_monet(src, SEATS["ag"], skill_name="session-start")
        self.assertIn("ag/<slug>", out)
        self.assertIn("trading-antigravity", out)
        self.assertNotIn("trading-monet", out)


if __name__ == "__main__":
    unittest.main()
