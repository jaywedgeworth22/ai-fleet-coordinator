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


def _session() -> str:
    return open(SESSION, encoding="utf-8").read()


class SpecializeTests(unittest.TestCase):
    def test_cursor_is_not_monet(self) -> None:
        out = specialize_from_monet(_session(), SEATS["cursor"], skill_name="session-start")
        self.assertIn("AGENT_SEAT=CURSOR", out)
        self.assertNotIn("AGENT_SEAT=MONET", out)
        self.assertIn("[CURSOR]", out)
        self.assertNotIn("AGENT_SEAT=MONET", out)
        self.assertIn("cursor/<slug>", out)
        self.assertIn("GROK-BOT", out)
        self.assertNotIn("two different Claude accounts", out)
        self.assertIn("This install is for `CURSOR`", out)

    def test_ag_suffix_is_antigravity(self) -> None:
        out = specialize_from_monet(_session(), SEATS["ag"], skill_name="session-start")
        self.assertIn("AGENT_SEAT=AG", out)
        self.assertIn("ag/<slug>", out)
        self.assertIn("trading-antigravity", out)
        self.assertNotIn("trading-monet", out)

    def test_codex_grok_renoir_deepseek_tags(self) -> None:
        mapping = {
            "codex": "CODEX",
            "grok": "GROK",
            "renoir": "RENOIR",
            "deepseek": "DEEPSEEK",
            "grok-bot": "GROK-BOT",
            "grok-build": "GROK-BUILD",
            "claude": "CLAUDE",
        }
        src = _session()
        for key, tag in mapping.items():
            out = specialize_from_monet(src, SEATS[key], skill_name="session-start")
            self.assertIn(f"AGENT_SEAT={tag}", out, key)
            self.assertNotIn("AGENT_SEAT=MONET", out, key)

    def test_kimi_retired_banner(self) -> None:
        out = specialize_from_monet(_session(), SEATS["kimi"], skill_name="session-start")
        self.assertIn("[KIMI]", out)
        self.assertIn("Retired seat", out)

    def test_claude_shared_pin(self) -> None:
        out = specialize_from_monet(
            _session(), SEATS["claude_shared"], skill_name="session-start"
        )
        self.assertIn("Shared `~/.claude/skills`", out)
        self.assertIn("RENOIR", out)
        self.assertIn("MONET, CLAUDE, or RENOIR", out)

    def test_sentence_gap_keeps_protocol_name(self) -> None:
        src = open(GAP, encoding="utf-8").read()
        out = specialize_from_monet(src, SEATS["cursor"], skill_name="sentence-gap")
        self.assertTrue(
            "Monet portable" in out or "Monet's portable" in out,
            out[:600],
        )


if __name__ == "__main__":
    unittest.main()
