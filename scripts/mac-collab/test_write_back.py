#!/usr/bin/env python3
"""Unit tests for surgical effort-log edits and inbound status merge."""
from __future__ import annotations

import hashlib
import importlib.util
import re
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

import write_back as wb

_SERVER_PATH = Path(__file__).resolve().parent / "mac-collab-server.py"
_SPEC = importlib.util.spec_from_file_location("mac_collab_server", _SERVER_PATH)
assert _SPEC and _SPEC.loader
server = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(server)


def sha(line: str) -> str:
    text = re.sub(r"[*_`]", "", line)
    normalized = re.sub(r"\s+", " ", text).strip().lower()
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()


SAMPLE = """# Effort log

Preamble stays.

## Changelog of this log
- 2026-08-21 — CURSOR: a changelog line that is not a status bucket.

## In Progress
- **Keep me in progress.** extra words
- **Move me.** this bullet should move

A non-bullet note under In Progress must survive.

## Completed
- **Already done.**
"""


class SurgicalMoveTests(unittest.TestCase):
    def test_move_preserves_surroundings(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "log.md"
            path.write_text(SAMPLE)
            key = sha("**Move me.** this bullet should move")
            changed = wb.move_bullet_in_file(path, key, "completed", dry_run=False)
            self.assertTrue(changed)
            text = path.read_text()
            self.assertIn("## Changelog of this log", text)
            self.assertIn("Preamble stays.", text)
            self.assertIn("A non-bullet note under In Progress must survive.", text)
            self.assertIn("- **Keep me in progress.** extra words", text)
            # moved bullet now under Completed, still a bullet
            completed = text.split("## Completed", 1)[1]
            self.assertIn("**Move me.** this bullet should move", completed)
            inprog = text.split("## In Progress", 1)[1].split("## Completed", 1)[0]
            self.assertNotIn("**Move me.**", inprog)

    def test_move_is_noop_when_already_there(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "log.md"
            path.write_text(SAMPLE)
            key = sha("**Already done.**")
            changed = wb.move_bullet_in_file(path, key, "completed", dry_run=False)
            self.assertFalse(changed)
            self.assertEqual(path.read_text(), SAMPLE)

    def test_changelog_heading_not_classified(self):
        self.assertIsNone(wb.classify_heading("Changelog of this log"))
        self.assertEqual(wb.classify_heading("Planned / Reserved"), "planned")
        self.assertEqual(wb.classify_heading("Recently completed"), "completed")

    def test_agent_report_append_and_marker(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "log.md"
            path.write_text(SAMPLE)
            finding = {
                "id": "abc123",
                "title": "Filed from board",
                "reported_by": "GROK",
                "resolution": "",
            }
            changed = wb.append_agent_report_to_file(
                path, finding, "in-progress", dry_run=False
            )
            self.assertTrue(changed)
            text = path.read_text()
            self.assertIn("<!-- wb-agent-report:abc123 -->", text)
            changed2 = wb.append_agent_report_to_file(
                path, finding, "in-progress", dry_run=False
            )
            self.assertFalse(changed2)


class LastRunAdvanceTests(unittest.TestCase):
    def test_clean_pass_advances(self):
        self.assertTrue(wb.should_advance_last_run(0))

    def test_timeout_does_not_advance(self):
        self.assertFalse(wb.should_advance_last_run(1))


class UpsertStatusTests(unittest.TestCase):
    def test_omitted_status_keeps_existing(self):
        self.assertEqual(
            server.resolve_upsert_status("in_progress", "open", False, "github-issue", None),
            "in_progress",
        )

    def test_github_open_does_not_unclaim(self):
        # Concrete trigger: board claim → GH still OPEN → sync POSTs open.
        self.assertEqual(
            server.resolve_upsert_status("in_progress", "open", True, "github-issue", None),
            "in_progress",
        )

    def test_github_closed_does_not_clobber_deployed(self):
        self.assertEqual(
            server.resolve_upsert_status("deployed", "completed", True, "github-issue", None),
            "deployed",
        )

    def test_github_close_still_completes_a_claim(self):
        self.assertEqual(
            server.resolve_upsert_status("in_progress", "completed", True, "github-issue", None),
            "completed",
        )

    def test_github_reopen_still_reopens(self):
        self.assertEqual(
            server.resolve_upsert_status("completed", "open", True, "github-issue", None),
            "open",
        )

    def test_effort_row_open_can_overwrite_claim_after_grace(self):
        # File section is a real copy.  After grace, inbound may win.
        self.assertEqual(
            server.resolve_upsert_status("in_progress", "open", True, "effort-row", None),
            "open",
        )

    def test_grace_protects_effort_row_claim(self):
        now = datetime.now(timezone.utc)
        wb_at = (now - timedelta(seconds=60)).isoformat()
        self.assertEqual(
            server.resolve_upsert_status(
                "in_progress", "open", True, "effort-row", wb_at, now
            ),
            "in_progress",
        )

    def test_expired_grace_allows_effort_row_overwrite(self):
        now = datetime.now(timezone.utc)
        wb_at = (now - timedelta(seconds=server.WRITEBACK_GRACE_S + 1)).isoformat()
        self.assertEqual(
            server.resolve_upsert_status(
                "in_progress", "open", True, "effort-row", wb_at, now
            ),
            "open",
        )


if __name__ == "__main__":
    unittest.main()
