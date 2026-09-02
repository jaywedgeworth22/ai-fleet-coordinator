"""Source generator tests: a temp findings.db with the real schema shape, files on disk, notes."""
from __future__ import annotations

import json
import os
import pathlib
import sqlite3
import stat
import tempfile
import unittest
from unittest import mock

from fleet_rag import notes_export, sources
from fleet_rag.notes_export import html_to_text, strip_title_line

FINDINGS_DDL = """
CREATE TABLE findings (
    id TEXT PRIMARY KEY, app TEXT NOT NULL, external_uid TEXT, source TEXT, title TEXT NOT NULL,
    severity TEXT, category TEXT, surface TEXT, description TEXT, recommended_fix TEXT,
    status TEXT NOT NULL DEFAULT 'open', addressed_by TEXT, resolution TEXT,
    created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
    source_kind TEXT NOT NULL DEFAULT 'review-finding', source_url TEXT, repo TEXT, reported_by TEXT,
    location TEXT, env TEXT, writeback_at TEXT, UNIQUE(app, external_uid));
CREATE TABLE comments (
    id TEXT PRIMARY KEY, finding_id TEXT NOT NULL REFERENCES findings(id), author TEXT NOT NULL,
    text TEXT NOT NULL, created_at TEXT NOT NULL, location TEXT, env TEXT);
"""


def make_db(path: pathlib.Path) -> None:
    con = sqlite3.connect(path)
    con.executescript(FINDINGS_DDL)
    con.execute(
        "INSERT INTO findings (id, app, title, severity, description, recommended_fix, status, "
        "created_at, updated_at, source_kind, reported_by) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        ("aaaa1111", "congress-trade", "No account deletion path", "P0", "Users cannot delete.",
         "Add delete_account.", "open", "2026-08-20T01:57:12.791030+00:00",
         "2026-08-20T01:57:12.791030+00:00", "review-finding", "Claude (Mac)"))
    con.execute(
        "INSERT INTO findings (id, app, title, severity, description, status, addressed_by, resolution, "
        "created_at, updated_at, source_kind) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        ("bbbb2222", "API-Usage-Monitor", "Snapshot scheduler late", "P1", "Rows scheduled in the past.",
         "completed", "GROK", "Landed in #123.", "2026-08-21T03:00:00+00:00",
         "2026-08-22T08:42:11.038241+00:00", "effort-row"))
    con.execute(
        "INSERT INTO findings (id, app, title, description, status, created_at, updated_at, source_kind) "
        "VALUES (?,?,?,?,?,?,?,?)",
        ("cccc3333", "dealdex", "Issue with effort key",
         "Body line.\n\n<!-- effort-key: 0123456789abcdef0123456789abcdef01234567 -->\nMore.",
         "open", "2026-08-24T00:00:00+00:00", "2026-08-24T00:00:00+00:00", "github-issue"))
    con.execute("INSERT INTO comments (id, finding_id, author, text, created_at) VALUES (?,?,?,?,?)",
                ("c2", "aaaa1111", "GROK", "Second comment.", "2026-08-23T10:00:00+00:00"))
    con.execute("INSERT INTO comments (id, finding_id, author, text, created_at) VALUES (?,?,?,?,?)",
                ("c1", "aaaa1111", "CLAUDE", "First comment.", "2026-08-22T10:00:00+00:00"))
    con.commit()
    con.close()


class BoardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.db = pathlib.Path(self.tmp.name) / "findings.db"
        make_db(self.db)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_docs(self) -> None:
        docs = {d.doc_id: d for d in sources.iter_board(self.db)}
        self.assertEqual(set(docs), {"board/aaaa1111", "board/bbbb2222", "board/cccc3333"})
        c = docs["board/cccc3333"]
        self.assertNotIn("effort-key", c.text_markdown)
        self.assertIn("Body line.\n\nMore.", c.text_markdown)
        self.assertEqual(c.seat, "FLEET")
        a = docs["board/aaaa1111"]
        self.assertEqual(a.source, "board")
        self.assertEqual(a.category, "finding")
        self.assertEqual(a.app, "congress-trade")
        self.assertEqual(a.seat, "CLAUDE")
        self.assertEqual(a.title, "No account deletion path")
        self.assertTrue(a.url.startswith("https://mac.jays.services/board"))
        self.assertEqual(a.created_at_ms, sources.parse_ts_ms("2026-08-20T01:57:12.791030+00:00"))
        # updated_at is the last comment, and comments come in chronological order
        self.assertEqual(a.updated_at_ms, sources.parse_ts_ms("2026-08-23T10:00:00+00:00"))
        self.assertLess(a.text_markdown.index("First comment."), a.text_markdown.index("Second comment."))
        for needle in ("# No account deletion path", "Severity: P0", "## Description", "Users cannot delete.",
                       "## Recommended fix", "### CLAUDE — 2026-08-22T10:00:00+00:00", "Board id: aaaa1111"):
            self.assertIn(needle, a.text_markdown)
        b = docs["board/bbbb2222"]
        self.assertEqual(b.category, "lesson")
        self.assertEqual(b.app, "usage-monitor")
        self.assertEqual(b.seat, "GROK")
        self.assertIn("## Resolution\n\nLanded in #123.", b.text_markdown)
        self.assertEqual(b.updated_at_ms, sources.parse_ts_ms("2026-08-22T08:42:11.038241+00:00"))

    def test_limit_and_missing_db(self) -> None:
        self.assertEqual(len(list(sources.iter_board(self.db, limit=2))), 2)
        with self.assertRaises(FileNotFoundError):
            list(sources.iter_board(self.db.with_name("nope.db")))


class FileSourceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_effort_logs(self) -> None:
        (self.root / "SOCRATIC-TRADE-EFFORT-LOG.md").write_text("# ST log\n\n## Deployed\n- x\n")
        (self.root / "API-USAGE-MONITOR-EFFORT-LOG.md").write_text("# UM log\n")
        (self.root / "EFFORT-LOG-PROTOCOL.md").write_text("# Protocol\n")
        docs = {d.doc_id: d for d in sources.iter_effort_logs(self.root)}
        self.assertEqual(set(docs), {"effort-log/SOCRATIC-TRADE", "effort-log/API-USAGE-MONITOR",
                                     "effort-log/PROTOCOL"})
        self.assertEqual(docs["effort-log/SOCRATIC-TRADE"].app, "socratic-trade")
        self.assertEqual(docs["effort-log/API-USAGE-MONITOR"].app, "usage-monitor")
        self.assertEqual(docs["effort-log/PROTOCOL"].app, "fleet")
        d = docs["effort-log/SOCRATIC-TRADE"]
        self.assertEqual((d.source, d.category, d.seat, d.title), ("effort-log", "lesson", "FLEET", "ST log"))
        self.assertGreater(d.created_at_ms, 0)

    def test_docs_filters(self) -> None:
        repo = self.root / "repo"
        (repo / "docs" / "reviews").mkdir(parents=True)
        (repo / "docs" / "backups").mkdir()
        (repo / "node_modules" / "x").mkdir(parents=True)
        (repo / ".claude" / "skills" / "s1").mkdir(parents=True)
        (repo / "README.md").write_text("# Fleet coordinator\n\nhello\n")
        (repo / "docs" / "A.md").write_text("# A\n\nbody\n")
        (repo / "docs" / "reviews" / "2026-raw-dump.md").write_text("# raw\n")
        (repo / "docs" / "reviews" / "2026-review.md").write_text("# review\n")
        (repo / "docs" / "backups" / "old.md").write_text("# old\n")
        (repo / "docs" / "big.md").write_text("x" * (sources.DOC_MAX_BYTES + 1))
        (repo / "node_modules" / "x" / "README.md").write_text("# nm\n")
        (repo / ".claude" / "skills" / "s1" / "SKILL.md").write_text("---\nname: s1\n---\n# S1\n")
        extra = self.root / "AGENT-SYNC.md"
        extra.write_text("# Agent sync\n")
        docs = {d.path: d for d in sources.iter_docs(repo, self.root / "missing-ops", [extra])}
        names = {pathlib.Path(p).name for p in docs}
        self.assertEqual(names, {"README.md", "A.md", "2026-review.md", "SKILL.md", "AGENT-SYNC.md"})
        skill = docs[str(repo / ".claude" / "skills" / "s1" / "SKILL.md")]
        self.assertEqual(skill.category, "runbook")
        self.assertEqual(docs[str(repo / "docs" / "A.md")].category, "doc")
        # not a git repo -> no url, local doc id, mtime dates
        a = docs[str(repo / "docs" / "A.md")]
        self.assertEqual(a.url, "")
        self.assertTrue(a.doc_id.startswith("doc/local/"))
        self.assertGreater(a.created_at_ms, 0)
        self.assertEqual(a.title, "A")

    def test_skills_dedupe(self) -> None:
        for d in ("claude", "cursor"):
            (self.root / d / "same").mkdir(parents=True)
            (self.root / d / "same" / "SKILL.md").write_text("---\nname: same\n---\n# Same skill\n")
        (self.root / "cursor" / "only").mkdir()
        (self.root / "cursor" / "only" / "SKILL.md").write_text("# Only\n")
        docs = list(sources.iter_skills([self.root / "claude", self.root / "cursor"]))
        self.assertEqual(sorted(d.doc_id for d in docs), ["skill/claude/same", "skill/cursor/only"])
        self.assertTrue(all(d.category == "runbook" and d.seat == "FLEET" for d in docs))
        self.assertEqual(docs[0].title, "same")
        # same directory name, different content -> two docs with tree-unique ids (no collision)
        (self.root / "cursor" / "same" / "SKILL.md").write_text("---\nname: same\n---\n# Same skill, edited\n")
        docs = list(sources.iter_skills([self.root / "claude", self.root / "cursor"]))
        self.assertEqual(sorted(d.doc_id for d in docs),
                         ["skill/claude/same", "skill/cursor/only", "skill/cursor/same"])
        self.assertEqual(len({d.doc_id for d in docs}), len(docs))
        # the real trees map to claude / cursor
        self.assertEqual(sources.skill_tree(pathlib.Path.home() / ".claude" / "skills"), "claude")
        self.assertEqual(sources.skill_tree(pathlib.Path.home() / ".cursor" / "skills"), "cursor")
        self.assertEqual(sources.skill_tree(self.root / "claude"), "claude")

    def test_memory(self) -> None:
        proj = self.root / "projects" / "-Users-jay-Code-Socratic-Trade" / "memory"
        proj.mkdir(parents=True)
        (proj / "MEMORY.md").write_text("# index\n")
        (proj / "pref.md").write_text("---\nname: pref\nmetadata:\n  type: feedback\n---\n\nOwner wants X.\n")
        (proj / "infra.md").write_text("---\nname: infra\ntype: reference\n---\n\nQdrant lives at Y.\n")
        (proj / "plain.md").write_text("# Plain\n\nno frontmatter\n")
        codex = self.root / "codex"
        codex.mkdir()
        (codex / "MEMORY.md").write_text("# Task group\n\nscope: x\n")
        docs = {d.doc_id: d for d in sources.iter_memory(self.root / "projects", codex)}
        self.assertEqual(set(docs), {"memory/claude/code-socratic-trade/pref.md",
                                     "memory/claude/code-socratic-trade/infra.md",
                                     "memory/claude/code-socratic-trade/plain.md",
                                     "memory/codex/MEMORY.md"})
        self.assertEqual(docs["memory/claude/code-socratic-trade/pref.md"].category, "preference")
        self.assertEqual(docs["memory/claude/code-socratic-trade/infra.md"].category, "infrastructure")
        self.assertEqual(docs["memory/claude/code-socratic-trade/plain.md"].category, "lesson")
        self.assertEqual(docs["memory/claude/code-socratic-trade/pref.md"].app, "socratic-trade")
        self.assertEqual(docs["memory/claude/code-socratic-trade/pref.md"].seat, "CLAUDE")
        self.assertEqual(docs["memory/codex/MEMORY.md"].seat, "CODEX")
        self.assertEqual(docs["memory/claude/code-socratic-trade/plain.md"].title, "Plain")


class NoteTests(unittest.TestCase):
    def test_title_parse(self) -> None:
        self.assertEqual(sources.parse_note_title("[UM, Grok] TestFlight"), ("usage-monitor", "GROK"))
        self.assertEqual(sources.parse_note_title("[ST, CT, Monet] digests"), ("socratic-trade", "MONET"))
        self.assertEqual(sources.parse_note_title("[FLEET, Claude] review"), ("fleet", "CLAUDE"))
        self.assertEqual(sources.parse_note_title("[CTS, Antigravity] x"), ("congress-trading-shared", "AG"))
        self.assertEqual(sources.parse_note_title("[BF, AG] y"), ("botfleet", "AG"))
        self.assertEqual(sources.parse_note_title("[DD, Cursor] z"), ("dealdex", "CURSOR"))
        self.assertEqual(sources.parse_note_title("[Codex] z"), ("fleet", "CODEX"))
        self.assertEqual(sources.parse_note_title("New Note"), ("fleet", "FLEET"))

    def test_html_to_text(self) -> None:
        html = ('<div><b><span style="font-size: 24px">[UM, Grok] Title</span></b></div>'
                '<style>.x{}</style><div>Tue, Sep 1, 3:01pm</div><div><br></div>'
                '<div>Line one &amp; two.</div><ul><li>alpha</li><li>beta</li></ul><p>End.</p>')
        text = html_to_text(html)
        self.assertIn("[UM, Grok] Title\nTue, Sep 1, 3:01pm", text)
        self.assertIn("Line one & two.", text)
        self.assertIn("- alpha\n- beta", text)
        self.assertNotIn(".x{}", text)
        self.assertEqual(strip_title_line(text, "[UM, Grok] Title").split("\n")[0], "Tue, Sep 1, 3:01pm")
        # entities are decoded exactly once: a literal "&amp;amp;" in a note is "&amp;" as text
        self.assertEqual(html_to_text("<div>a &amp;amp; b &lt;tag&gt;</div>"), "a &amp; b <tag>")

    def test_iter_apple_notes(self) -> None:
        recs = [
            {"id": "x-coredata://ABC/ICNote/p1", "name": "[ST, Monet] Plan", "created": "2026-08-09T15:52:00",
             "modified": "2026-08-10T09:00:00", "text": "[ST, Monet] Plan\nSun, Aug 9, 3:52pm\n\nBody text long enough."},
            {"id": "x-coredata://ABC/ICNote/p2", "name": "New Note", "created": "", "modified": "", "text": "New Note"},
        ]
        docs = list(sources.iter_apple_notes(recs))
        self.assertEqual(len(docs), 1)
        d = docs[0]
        self.assertEqual(d.doc_id, "note/ABC/ICNote/p1")
        self.assertEqual((d.source, d.category, d.app, d.seat), ("apple-note", "note", "socratic-trade", "MONET"))
        self.assertTrue(d.text_markdown.startswith("Sun, Aug 9"))
        self.assertGreater(d.updated_at_ms, d.created_at_ms)


class NotesCacheTests(unittest.TestCase):
    META = [{"id": "x-coredata://ABC/ICNote/p1", "name": "[ST, Monet] Plan", "modified": "2026-08-10T09:00:00",
             "created": "2026-08-09T15:52:00"},
            {"id": "x-coredata://ABC/ICNote/p2", "name": "Gone", "modified": "2026-08-11T09:00:00",
             "created": "2026-08-11T09:00:00"}]
    BODY = ('<div>[ST, Monet] Plan</div><div>Sun, Aug 9, 3:52pm</div><div>Deploy with '
            'SLACK_TOKEN=xoxb-123456789012-abcdefghijkl and go.</div>')

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.cache = pathlib.Path(self.tmp.name) / "cache" / "notes"
        self.range_calls: list[tuple[int, int]] = []
        self.byid_calls: list[list[str]] = []

        def fake_range(start, end, folder, account):  # noqa: ANN001
            self.range_calls.append((start, end))
            return {self.META[0]["id"]: self.BODY}       # p2's body never comes back

        def fake_by_id(ids):  # noqa: ANN001
            self.byid_calls.append(list(ids))
            return {}

        self.patches = [
            mock.patch.object(notes_export, "list_notes", lambda folder, account: [dict(m) for m in self.META]),
            mock.patch.object(notes_export, "_fetch_bodies_range", fake_range),
            mock.patch.object(notes_export, "_fetch_bodies_by_id", fake_by_id),
        ]
        for p in self.patches:
            p.start()

    def tearDown(self) -> None:
        for p in self.patches:
            p.stop()
        self.tmp.cleanup()

    def test_cache_holds_only_scrubbed_text_with_private_modes(self) -> None:
        logs: list[str] = []
        recs = notes_export.export_notes(cache_dir=self.cache, log=logs.append)
        self.assertEqual(len(recs), 2)
        rec = recs[0]
        self.assertEqual(rec["v"], notes_export.CACHE_VERSION)
        self.assertNotIn("html", rec)
        self.assertNotIn("xoxb-", rec["text"])
        self.assertIn("[REDACTED:slack-token]", rec["text"])
        self.assertIn("slack-token", rec["scrubbed"])
        self.assertTrue(rec["text"].startswith("[ST, Monet] Plan\nSun, Aug 9"))
        self.assertEqual(set(rec), {"id", "name", "modified", "created", "text", "v", "scrubbed"})
        # on disk: dir 0700, file 0600, and the raw body never touched the disk
        self.assertEqual(stat.S_IMODE(self.cache.stat().st_mode), 0o700)
        files = sorted(self.cache.glob("*.json"))
        self.assertEqual(len(files), 1)                  # p2 (no body) is NOT cached
        self.assertEqual(stat.S_IMODE(files[0].stat().st_mode), 0o600)
        raw = files[0].read_text()
        self.assertNotIn("xoxb-", raw)
        self.assertNotIn("<div>", raw)
        self.assertEqual(json.loads(raw), rec)
        self.assertEqual(recs[1]["text"], "")
        self.assertTrue(any("did not come back" in l for l in logs))
        self.assertEqual(self.byid_calls, [[self.META[1]["id"]]])
        # second export: p1 served from cache, p2 asked for again
        self.range_calls.clear()
        recs2 = notes_export.export_notes(cache_dir=self.cache)
        self.assertEqual(recs2[0], rec)
        self.assertEqual(self.range_calls, [(2, 2)])

    def test_old_cache_records_are_invalidated_and_rewritten(self) -> None:
        self.cache.mkdir(parents=True)
        old = self.cache / f"{notes_export.safe_id(self.META[0]['id'])}.json"
        old.write_text(json.dumps({**self.META[0], "html": self.BODY, "text": "raw unscrubbed xoxb-123456789012-abcdefghijkl"}))
        os.chmod(old, 0o644)
        self.assertEqual(list(notes_export.iter_cached(self.cache)), [])      # v1 never served
        recs = notes_export.export_notes(cache_dir=self.cache)
        self.assertEqual(self.range_calls, [(1, 2)])                           # re-fetched (p2 never cached)
        self.assertEqual(recs[0]["v"], notes_export.CACHE_VERSION)
        self.assertNotIn("html", json.loads(old.read_text()))
        self.assertEqual(stat.S_IMODE(old.stat().st_mode), 0o600)
        self.assertEqual([r["id"] for r in notes_export.iter_cached(self.cache)], [self.META[0]["id"]])

    def test_iter_apple_notes_falls_back_to_cache(self) -> None:
        notes_export.export_notes(cache_dir=self.cache)
        logs: list[str] = []
        sources.take_warnings()

        def unavailable(log=None):  # noqa: ANN001
            raise notes_export.NotesUnavailable("automation denied")

        with mock.patch.object(notes_export, "export_notes", unavailable), \
                mock.patch.object(notes_export, "CACHE_DIR", self.cache):
            docs = list(sources.iter_apple_notes(log=logs.append))
        self.assertEqual([d.doc_id for d in docs], ["note/ABC/ICNote/p1"])
        self.assertEqual(docs[0].seat, "MONET")
        self.assertNotIn("xoxb-", docs[0].text_markdown)
        self.assertTrue(docs[0].text_markdown.startswith("Sun, Aug 9"))
        warnings = sources.take_warnings()
        self.assertEqual(len(warnings), 1)
        self.assertIn("automation denied", warnings[0])
        self.assertIn("served 1 cached notes", warnings[0])
        self.assertTrue(any("WARNING" in l and "automation denied" in l for l in logs))
        self.assertEqual(sources.take_warnings(), [])


class HelperTests(unittest.TestCase):
    def test_slugs(self) -> None:
        self.assertEqual(sources.app_slug("Congress-Trade"), "congress-trade")
        self.assertEqual(sources.app_slug("CONGRESS-SHARED"), "congress-trading-shared")
        self.assertEqual(sources.app_slug(""), "fleet")
        self.assertEqual(sources.seat_tag("monet"), "MONET")
        self.assertEqual(sources.seat_tag("GB-CONDUCTOR"), "GB-CONDUCTOR")
        self.assertEqual(sources.seat_tag(None), "FLEET")
        self.assertEqual(sources.project_slug("-Users-jay-Code-ai-fleet-coordinator"), "code-ai-fleet-coordinator")
        self.assertEqual(sources.app_from_project("code-congress-trading-shared"), "congress-trading-shared")
        self.assertEqual(sources.app_from_project("code-congress-trade-app"), "congress-trade")

    def test_parse_ts(self) -> None:
        self.assertEqual(sources.parse_ts_ms("2026-08-31T22:00:00Z"), 1788213600000)
        self.assertEqual(sources.parse_ts_ms("2026-08-31T22:00:00+00:00"), 1788213600000)
        self.assertEqual(sources.parse_ts_ms("garbage"), 0)
        self.assertEqual(sources.parse_ts_ms(None), 0)


if __name__ == "__main__":
    unittest.main()
