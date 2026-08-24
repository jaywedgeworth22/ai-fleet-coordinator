#!/usr/bin/env python3
"""Tests for per-seat fleet skill identity specialization."""

from __future__ import annotations

import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from fleet_skill_identity import SEATS, specialize_from_monet, specialize_universal  # noqa: E402

SESSION = os.path.join(ROOT, "docs", "fleet-skills", "session-start", "SKILL.md")
GAP = os.path.join(ROOT, "docs", "fleet-skills", "sentence-gap", "SKILL.md")
NOTES = os.path.join(ROOT, "docs", "fleet-skills", "apple-notes", "SKILL.md")
COORD = os.path.join(ROOT, "docs", "fleet-skills", "fleet-coordination", "SKILL.md")


def _session() -> str:
    with open(SESSION, encoding="utf-8") as f:
        return f.read()


def _notes() -> str:
    with open(NOTES, encoding="utf-8") as f:
        return f.read()


def _coord() -> str:
    with open(COORD, encoding="utf-8") as f:
        return f.read()


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

    def test_ag_notes_name_is_antigravity(self) -> None:
        out = specialize_from_monet(_notes(), SEATS["ag"], skill_name="apple-notes")
        self.assertIn("[APP, Antigravity]", out)
        self.assertNotIn("[APP, AG]", out)
        self.assertIn("then `Antigravity` (Title Case", out)

    def test_cursor_and_grok_notes_names(self) -> None:
        out_cur = specialize_from_monet(_notes(), SEATS["cursor"], skill_name="apple-notes")
        self.assertIn("[APP, Cursor]", out_cur)
        out_grok = specialize_from_monet(_notes(), SEATS["grok"], skill_name="apple-notes")
        self.assertIn("[APP, Grok]", out_grok)
        out_codex = specialize_from_monet(_notes(), SEATS["codex"], skill_name="apple-notes")
        self.assertIn("[APP, Codex]", out_codex)

    def test_fleet_coordination_seats_table_preserved(self) -> None:
        out = specialize_from_monet(_coord(), SEATS["ag"], skill_name="fleet-coordination")
        self.assertIn("Antigravity / Gemini: `[AG]`", out)
        self.assertIn("Monet: `[MONET]`", out)
        self.assertIn("Cursor: `[CURSOR]`", out)
        self.assertIn("Codex: `[CODEX]`", out)
        self.assertNotIn("AG: `[AG]`", out)

    def test_specialize_universal(self) -> None:
        out_sess = specialize_universal(_session(), skill_name="session-start")
        self.assertIn("AGENT_TAG=<YOUR_TAG>", out_sess)
        self.assertIn("AGENT_SEAT=<YOUR_SEAT>", out_sess)
        self.assertIn("<seat>/<slug>", out_sess)
        self.assertNotIn("AGENT_SEAT=MONET", out_sess)

        out_not = specialize_universal(_notes(), skill_name="apple-notes")
        self.assertIn("[APP, Agent]", out_not)
        self.assertNotIn("[APP, Monet]", out_not)

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
        with open(GAP, encoding="utf-8") as f:
            src = f.read()
        out = specialize_from_monet(src, SEATS["cursor"], skill_name="sentence-gap")
        self.assertTrue(
            "Monet portable" in out or "Monet's portable" in out,
            out[:600],
        )

    def test_quoted_description_folds_for_fx(self) -> None:
        out = specialize_from_monet(
            _session(), SEATS["codex"], skill_name="session-start"
        )
        self.assertIn("description: >-", out.split("---")[1])
        self.assertNotIn('description: Start', out.split("---")[1])
        self.assertIn("just a small fix.", out)

    def test_fx_seat_is_not_cursor(self) -> None:
        self.assertEqual(SEATS["fx"].tag, "FX")
        self.assertTrue(SEATS["fx"].dest.endswith("/.fx/skills") or "fx/skills" in SEATS["fx"].dest)
        out = specialize_from_monet(
            _session(), SEATS["fx"], skill_name="session-start"
        )
        self.assertIn("AGENT_SEAT=FX", out)
        self.assertNotIn("AGENT_SEAT=CURSOR", out)
        self.assertIn("[FX]", out)

    def test_fold_unwraps_quoted_yaml_string(self) -> None:
        from fleet_skill_identity import fold_yaml_description

        src = (
            "---\n"
            'name: cloudflare-one\n'
            'description: "Guides Cloudflare One \\"Zero Trust\\" work."\n'
            "---\n\n"
            "# Cloudflare One\n"
        )
        out = fold_yaml_description(src)
        self.assertIn("description: >-", out)
        self.assertIn('Guides Cloudflare One "Zero Trust" work.', out)
        self.assertNotIn('description: "', out)


if __name__ == "__main__":
    unittest.main()

