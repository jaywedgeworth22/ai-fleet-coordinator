"""Unit tests for fleet_rag.recall_api, fleet_rag.eval, and the recall CLI against an in-process
fake backend.

    cd scripts && python3 -m unittest fleet_rag.tests.test_recall -v
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import io
import json
import os
import pathlib
import tempfile
import unittest
from unittest import mock

from fleet_rag import eval as ev
from fleet_rag import recall_api
from fleet_rag.core import FleetRagError, build_point, content_hash, point_id
from fleet_rag.recall_api import FakeQdrant

SEAMS = ("load_config", "embed", "embedder_healthy", "Qdrant", "gitleaks_flagged", "gitleaks_available")
META_EXCLUDE = {"key": "source", "match": {"value": "meta"}}


def add_fake_point(text: str, **payload) -> dict:
    base = {"source": "doc", "app": "fleet", "category": "doc", "seat": "CLAUDE", "doc_id": "x/y",
            "chunk_index": 0, "chunk_count": 1, "heading": "", "title": "", "url": "", "path": "",
            "created_at": 1756684800000, "updated_at": 1756684800000, "ingest_run": "fake"}
    pt = build_point(text, {**base, **payload})
    FakeQdrant.points.append({"id": pt["id"], "payload": pt["payload"]})
    return pt


class RecallBase(unittest.TestCase):
    def setUp(self):
        # Fresh fakes for every test; the module-level seams are restored afterwards.
        self._saved = {k: getattr(recall_api, k) for k in SEAMS}
        recall_api.install_fake_backend()
        self.env = mock.patch.dict(os.environ, {}, clear=False)
        self.env.start()
        os.environ.pop("AGENT_SEAT", None)

    def tearDown(self):
        self.env.stop()
        for k, v in self._saved.items():
            setattr(recall_api, k, v)
        recall_api.reset_config_cache()


class BuildFilterTests(RecallBase):
    def test_no_filters_still_excludes_meta(self):
        self.assertEqual(recall_api.build_filter(), {"must_not": [META_EXCLUDE]})

    def test_match_fields(self):
        flt = recall_api.build_filter(category="lesson", app="fleet", source="doc", seat="CLAUDE")
        self.assertEqual(flt, {"must_not": [META_EXCLUDE], "must": [
            {"key": "category", "match": {"value": "lesson"}},
            {"key": "app", "match": {"value": "fleet"}},
            {"key": "source", "match": {"value": "doc"}},
            {"key": "seat", "match": {"value": "CLAUDE"}},
        ]})

    def test_since_days_range_alone(self):
        flt = recall_api.build_filter(since_days=7, now=10_000_000_000)
        self.assertEqual(flt, {"must_not": [META_EXCLUDE],
                               "must": [{"key": "created_at",
                                         "range": {"gte": 10_000_000_000 - 7 * 86_400_000}}]})

    def test_since_days_combined_with_match(self):
        flt = recall_api.build_filter(app="fleet", since_days=1, now=5_000_000_000)
        self.assertEqual(flt["must"][0], {"key": "app", "match": {"value": "fleet"}})
        self.assertEqual(flt["must"][1], {"key": "created_at", "range": {"gte": 5_000_000_000 - 86_400_000}})
        self.assertEqual(flt["must_not"], [META_EXCLUDE])

    def test_since_days_must_be_positive_int(self):
        for bad in (0, -3, "7", 1.5, True):
            with self.assertRaises(FleetRagError):
                recall_api.build_filter(since_days=bad)

    def test_meta_exclude_is_a_fresh_dict_each_call(self):
        a = recall_api.build_filter()
        a["must_not"][0]["match"]["value"] = "tampered"
        self.assertEqual(recall_api.build_filter()["must_not"], [META_EXCLUDE])


class SearchTests(RecallBase):
    def test_hits_have_contract_shape_and_hybrid_mode(self):
        res = recall_api.recall_search("leaking credentials handoff file", limit=3)
        self.assertEqual(res["mode"], "hybrid")
        self.assertTrue(res["hits"])
        hit = res["hits"][0]
        for f in ("score", "text") + recall_api.HIT_FIELDS:
            self.assertIn(f, hit)
        self.assertIn("List names only", hit["text"])
        vector, terms, limit, flt = FakeQdrant.calls[-1]
        self.assertEqual(limit, 3)
        self.assertEqual(flt, {"must_not": [META_EXCLUDE]})
        self.assertIn("credentials", terms)

    def test_filters_and_since_days_reach_qdrant(self):
        before = recall_api.now_ms()
        recall_api.recall_search("vector database", category="infrastructure", app="Fleet",
                                 seat="claude", since_days=30)
        _, _, _, flt = FakeQdrant.calls[-1]
        keys = [c["key"] for c in flt["must"]]
        self.assertEqual(keys, ["category", "app", "seat", "created_at"])
        self.assertEqual(flt["must"][1]["match"]["value"], "fleet")    # app lowercased
        self.assertEqual(flt["must"][2]["match"]["value"], "CLAUDE")   # seat uppercased
        gte = flt["must"][3]["range"]["gte"]
        self.assertTrue(before - 30 * 86_400_000 - 5000 <= gte <= before - 30 * 86_400_000 + 5000)
        self.assertEqual(flt["must_not"], [META_EXCLUDE])

    def test_stopword_only_query_falls_back_to_dense(self):
        res = recall_api.recall_search("is it", limit=2)
        self.assertEqual(res["mode"], "dense")
        self.assertEqual(FakeQdrant.calls[-1][1], [])
        self.assertEqual(FakeQdrant.calls[-1][3], {"must_not": [META_EXCLUDE]})

    def test_ingest_sentinel_never_returned(self):
        # A source="meta" point whose text matches the query better than anything else.
        add_fake_point("handoff credentials leaking leaking leaking names only", source="meta",
                       app="fleet", doc_id="meta/ingest-run")
        for kwargs in ({}, {"app": "fleet"}, {"since_days": 3650}, {"category": "preference"}):
            res = recall_api.recall_search("handoff credentials leaking names", limit=10, **kwargs)
            self.assertTrue(res["hits"], kwargs)
            self.assertNotIn("meta", [h["source"] for h in res["hits"]], kwargs)
            self.assertNotIn("meta/ingest-run", [h["doc_id"] for h in res["hits"]], kwargs)
            self.assertEqual(FakeQdrant.calls[-1][3]["must_not"], [META_EXCLUDE], kwargs)
        # Even asking for it by source is refused (meta is not a searchable source).
        with self.assertRaisesRegex(FleetRagError, "source must be one of"):
            recall_api.recall_search("anything", source="meta")

    def test_bad_arguments(self):
        with self.assertRaises(FleetRagError):
            recall_api.recall_search("   ")
        with self.assertRaises(FleetRagError):
            recall_api.recall_search("x", limit=0)
        with self.assertRaises(FleetRagError):
            recall_api.recall_search("x", limit=recall_api.MAX_LIMIT + 1)

    def test_non_string_filters_rejected(self):
        for field in ("category", "app", "source", "seat"):
            for bad in (1, 1.5, True, ["doc"], {"a": 1}):
                with self.assertRaisesRegex(FleetRagError, f"{field} must be a string", msg=(field, bad)):
                    recall_api.recall_search("x", **{field: bad})
        self.assertEqual(FakeQdrant.calls, [])

    def test_category_and_source_enumerated(self):
        with self.assertRaisesRegex(FleetRagError, r"category must be one of .*lesson\|preference.*finding") as cm:
            recall_api.recall_search("x", category="bogus")
        self.assertIn("'bogus'", str(cm.exception))
        with self.assertRaisesRegex(FleetRagError, r"source must be one of .*board\|effort-log.*agent-contribution"):
            recall_api.recall_search("x", source="slack")
        self.assertEqual(FakeQdrant.calls, [])
        # Every listed value is accepted; blank means "no filter".
        for c in recall_api.CATEGORIES:
            recall_api.recall_search("x", category=c)
        for s in recall_api.SOURCES:
            recall_api.recall_search("x", source=s)
        recall_api.recall_search("x", category="", source="  ", app="", seat=None)
        self.assertEqual(FakeQdrant.calls[-1][3], {"must_not": [META_EXCLUDE]})


class StatsTests(RecallBase):
    def test_stats_shape(self):
        res = recall_api.recall_stats()
        self.assertEqual(res["collection"], "fleet-agents-fake")
        self.assertEqual(res["status"], "green")
        self.assertEqual(res["points"], 3)
        self.assertTrue(res["embedder_healthy"])
        self.assertEqual(list(res["by_source"]), list(recall_api.SOURCES))
        self.assertEqual(res["by_source"]["doc"], 3)
        self.assertEqual(res["by_source"]["board"], 0)
        self.assertEqual(res["by_app"], {"fleet": 3, "other": 0})

    def test_by_app_other_bucket_reconciles(self):
        add_fake_point("a point for an app nobody registered", app="new-app")
        add_fake_point("the ingest sentinel", source="meta", app="", doc_id="meta/run")
        add_fake_point("a socratic point", app="socratic-trade")
        res = recall_api.recall_stats()
        self.assertEqual(res["points"], 6)
        self.assertEqual(res["by_app"], {"fleet": 3, "socratic-trade": 1, "other": 2})
        self.assertEqual(sum(res["by_app"].values()), res["points"])
        self.assertEqual(list(res["by_app"])[-1], "other")


GOOD = ("pm2 start does not re-read env from the ecosystem file; restart with --update-env "
        "or delete and start the app again so the cached PATH is replaced.")


class ContributeTests(RecallBase):
    def test_too_short(self):
        with self.assertRaisesRegex(FleetRagError, "too short"):
            recall_api.recall_contribute("short note", "lesson", seat="CLAUDE")

    def test_too_long(self):
        with self.assertRaisesRegex(FleetRagError, "too long"):
            recall_api.recall_contribute("x" * 4001, "lesson", seat="CLAUDE")

    def test_bad_category(self):
        with self.assertRaisesRegex(FleetRagError, "category"):
            recall_api.recall_contribute(GOOD, "finding", seat="CLAUDE")

    def test_missing_seat(self):
        with self.assertRaisesRegex(FleetRagError, "seat"):
            recall_api.recall_contribute(GOOD, "lesson")

    def test_seat_from_env(self):
        os.environ["AGENT_SEAT"] = "grok"
        res = recall_api.recall_contribute(GOOD, "lesson")
        self.assertTrue(res["doc_id"].startswith("contrib/GROK/"))

    def test_bad_app_and_url(self):
        with self.assertRaisesRegex(FleetRagError, "app"):
            recall_api.recall_contribute(GOOD, "lesson", app="Socratic Trade", seat="CLAUDE")
        with self.assertRaisesRegex(FleetRagError, "url"):
            recall_api.recall_contribute(GOOD, "lesson", seat="CLAUDE", url="ftp://x")

    def test_non_string_fields_rejected(self):
        cases = {"category": [1, ["lesson"], None], "app": [1, ["fleet"]], "seat": [7, ["CLAUDE"]],
                 "title": [3, {"t": 1}], "url": [5, ["https://x"]]}
        for field, bads in cases.items():
            for bad in bads:
                kwargs = {"seat": "CLAUDE", field: bad}
                cat = kwargs.pop("category", "lesson")
                with self.assertRaisesRegex(FleetRagError, f"{field} must be", msg=(field, bad)):
                    recall_api.recall_contribute(GOOD, cat, **kwargs)
        self.assertEqual(FakeQdrant.upserts, [])

    def test_success_payload_schema_v2(self):
        res = recall_api.recall_contribute(GOOD, "runbook", app="fleet", seat="CLAUDE",
                                           title="pm2 env cache", url="https://example.com/pr/1")
        self.assertEqual(res["status"], "completed")
        self.assertEqual(res["scrubbed"], [])
        self.assertEqual(res["id"], point_id(content_hash(GOOD)))
        self.assertRegex(res["doc_id"], r"^contrib/CLAUDE/\d{4}-\d{2}-\d{2}/[0-9a-f]{8}$")
        self.assertTrue(res["doc_id"].endswith(content_hash(GOOD)[:8]))
        (point,), = FakeQdrant.upserts
        p = point["payload"]
        self.assertEqual(p["source"], "agent-contribution")
        self.assertEqual(p["category"], "runbook")
        self.assertEqual(p["seat"], "CLAUDE")
        self.assertEqual(p["title"], "pm2 env cache")
        self.assertEqual(p["url"], "https://example.com/pr/1")
        self.assertEqual((p["chunk_index"], p["chunk_count"]), (0, 1))
        self.assertEqual(p["created_at"], p["updated_at"])
        self.assertEqual(p["text"], GOOD)
        self.assertNotIn("scrubbed", p)
        self.assertEqual(len(point["vector"]), 4)
        for f in ("heading", "path", "content_hash", "embed_model", "ingest_run"):
            self.assertIn(f, p)

    def test_scrub_applied_and_reported(self):
        leaky = ("Use GITHUB_TOKEN=ghp_" + "A" * 36 + " for the API call and keep "
                 "SLACK_TOKEN=xoxb-1234567890-abcdefghijk out of the transcript.")
        res = recall_api.recall_contribute(leaky, "lesson", seat="CLAUDE")
        self.assertIn("github-token", res["scrubbed"])
        self.assertIn("slack-token", res["scrubbed"])
        (point,), = FakeQdrant.upserts
        text = point["payload"]["text"]
        self.assertNotIn("ghp_", text)
        self.assertNotIn("xoxb-", text)
        self.assertIn("[REDACTED:", text)
        self.assertEqual(point["payload"]["scrubbed"], res["scrubbed"])
        self.assertEqual(point["id"], point_id(content_hash(text)))  # id is over the SCRUBBED text

    def test_gitleaks_gate_refuses(self):
        recall_api.gitleaks_flagged = lambda path, timeout=300: {1}
        with self.assertRaisesRegex(FleetRagError, "refusing"):
            recall_api.recall_contribute(GOOD, "lesson", seat="CLAUDE")
        self.assertEqual(FakeQdrant.upserts, [])

    def test_gitleaks_gate_fails_closed_when_it_raises(self):
        class GitleaksError(RuntimeError):
            pass

        seen: list[str] = []

        def boom(path, timeout=300):
            seen.append(path)
            raise GitleaksError("gitleaks exited 2: /tmp/x.json: not found")

        recall_api.gitleaks_flagged = boom
        with self.assertRaisesRegex(FleetRagError, r"refusing.*gitleaks.*GitleaksError") as cm:
            recall_api.recall_contribute(GOOD, "lesson", seat="CLAUDE")
        self.assertNotIn("/tmp/x.json", str(cm.exception))   # class only, never the message
        self.assertEqual(FakeQdrant.upserts, [])
        self.assertEqual(len(seen), 1)
        self.assertFalse(os.path.exists(seen[0]))              # our temp jsonl is gone

        # Any other exception class from the gate refuses too.
        def oserr(path, timeout=300):
            raise OSError("disk")

        recall_api.gitleaks_flagged = oserr
        with self.assertRaisesRegex(FleetRagError, r"refusing.*OSError"):
            recall_api.recall_contribute(GOOD, "lesson", seat="CLAUDE")
        self.assertEqual(FakeQdrant.upserts, [])

    def test_temp_jsonl_unlinked_on_success(self):
        seen: list[str] = []

        def record(path, timeout=300):
            seen.append(path)
            self.assertTrue(os.path.exists(path))
            with open(path, encoding="utf-8") as fh:
                self.assertIn(GOOD[:30], fh.read())
            return set()

        recall_api.gitleaks_flagged = record
        res = recall_api.recall_contribute(GOOD, "lesson", seat="CLAUDE")
        self.assertEqual(res["scrubbed"], [])
        self.assertEqual(len(seen), 1)
        self.assertFalse(os.path.exists(seen[0]))

    def test_gitleaks_unavailable_is_reported_not_fatal(self):
        calls: list[str] = []
        recall_api.gitleaks_available = lambda: False
        recall_api.gitleaks_flagged = lambda path, timeout=300: calls.append(path) or set()
        res = recall_api.recall_contribute(GOOD, "lesson", seat="CLAUDE")
        self.assertEqual(res["scrubbed"], ["gitleaks-unavailable"])
        self.assertEqual(calls, [])                                # gitleaks never invoked
        (point,), = FakeQdrant.upserts
        self.assertNotIn("scrubbed", point["payload"])            # marker is not a redaction kind

        FakeQdrant.upserts.clear()
        leaky = "Keep SLACK_TOKEN=xoxb-1234567890-abcdefghijk out of the transcript when you paste logs."
        res = recall_api.recall_contribute(leaky, "lesson", seat="CLAUDE")
        self.assertEqual(res["scrubbed"], ["slack-token", "gitleaks-unavailable"])
        (point,), = FakeQdrant.upserts
        self.assertEqual(point["payload"]["scrubbed"], ["slack-token"])

    def test_contribute_needs_write_config(self):
        calls = []

        def fake_load(need_write=False, extra=()):
            calls.append(need_write)
            if need_write:
                raise FleetRagError("missing credentials: QDRANT_API_KEY")
            return {"QDRANT_URL": "http://fake", "QDRANT_FLEET_COLLECTION": "c", "TEI_URL": "http://f",
                    "TEI_API_KEY": "k", "QDRANT_READONLY_API_KEY": "r"}
        recall_api.load_config = fake_load
        with self.assertRaisesRegex(FleetRagError, "QDRANT_API_KEY"):
            recall_api.recall_contribute(GOOD, "lesson", seat="CLAUDE")
        self.assertEqual(calls, [True])


class ConfigCacheTests(RecallBase):
    def test_read_then_write_then_read_reuses_write(self):
        calls = []

        def fake_load(need_write=False, extra=()):
            calls.append(need_write)
            return {"QDRANT_URL": "u", "QDRANT_FLEET_COLLECTION": "c", "TEI_URL": "t", "TEI_API_KEY": "k",
                    **({"QDRANT_API_KEY": "w"} if need_write else {})}
        recall_api.load_config = fake_load
        recall_api.reset_config_cache()
        recall_api.get_config(False)
        recall_api.get_config(False)
        recall_api.get_config(True)
        recall_api.get_config(False)
        self.assertEqual(calls, [False, True])

    def test_key_mode(self):
        self.assertEqual(recall_api.key_mode({"QDRANT_READONLY_API_KEY": "r", "QDRANT_API_KEY": "w"}), "read-only")
        self.assertEqual(recall_api.key_mode({"QDRANT_API_KEY": "w"}), "write")
        self.assertEqual(recall_api.key_mode({}), "none")


class EvalMatchTests(unittest.TestCase):
    HIT = {"doc_id": "doc/ai-fleet-coordinator/docs/RAG-FLEET-INFRA.md", "text": "Set --max-batch-tokens lower."}

    def test_prefix_only(self):
        self.assertTrue(ev.matches({"expect_doc_id_prefix": "doc/ai-fleet-coordinator/"}, self.HIT))
        self.assertFalse(ev.matches({"expect_doc_id_prefix": "doc/local/"}, self.HIT))

    def test_text_only_str_or_list_case_insensitive(self):
        self.assertTrue(ev.matches({"expect_text_contains": "MAX-BATCH-TOKENS"}, self.HIT))
        self.assertTrue(ev.matches({"expect_text_contains": ["nope", "lower."]}, self.HIT))
        self.assertFalse(ev.matches({"expect_text_contains": ["nope", ""]}, self.HIT))

    def test_both_present_both_must_hold(self):
        both = {"expect_doc_id_prefix": "doc/ai-fleet-coordinator/", "expect_text_contains": ["max-batch-tokens"]}
        self.assertTrue(ev.matches(both, self.HIT))
        self.assertFalse(ev.matches({**both, "expect_doc_id_prefix": "doc/local/"}, self.HIT))
        self.assertFalse(ev.matches({**both, "expect_text_contains": ["warmup"]}, self.HIT))

    def test_neither_never_matches(self):
        self.assertFalse(ev.matches({}, self.HIT))
        self.assertFalse(ev.matches({"expect_text_contains": []}, self.HIT))

    def test_shipped_golden_loads_and_prefixes_follow_sources_convention(self):
        rows = ev.load_golden()
        self.assertGreaterEqual(len(rows), 30)
        prefixes = [r["expect_doc_id_prefix"] for r in rows if r.get("expect_doc_id_prefix")]
        self.assertTrue(prefixes)                                   # the prefix path stays exercised
        for prefix in prefixes:
            self.assertRegex(prefix, r"^(doc|skill|board|effort-log|memory|note|contrib)/[^/]+/.+", prefix)

    def test_run_eval_scores_with_and_semantics(self):
        rows = [
            {"query": "q1", "expect_doc_id_prefix": "doc/a/", "expect_text_contains": ["alpha"]},
            {"query": "q2", "expect_text_contains": ["beta"]},
            {"query": "q3", "expect_doc_id_prefix": "doc/c/"},
        ]
        answers = {
            "q1": [{"doc_id": "doc/a/x", "text": "not it"}, {"doc_id": "doc/b/x", "text": "alpha"},
                   {"doc_id": "doc/a/y", "text": "ALPHA here"}],
            "q2": [{"doc_id": "z", "text": "beta"}],
            "q3": [{"doc_id": "doc/x/1", "text": ""}],
        }
        with tempfile.TemporaryDirectory() as d:
            golden = pathlib.Path(d) / "g.jsonl"
            golden.write_text("".join(json.dumps(r) + "\n" for r in rows))
            res = ev.run_eval(k=3, golden=golden, search=lambda q, limit: {"hits": answers[q][:limit]})
        self.assertEqual(res["n"], 3)
        self.assertAlmostEqual(res["recall_at_1"], 1 / 3)        # only q2 at rank 1
        self.assertAlmostEqual(res["recall_at_k"], 2 / 3)        # q1 at rank 3 (first hit with BOTH), q3 miss
        self.assertAlmostEqual(res["mrr"], (1 / 3 + 1) / 3)
        self.assertEqual([m["query"] for m in res["misses"]], ["q3"])


def load_cli():
    path = pathlib.Path(__file__).resolve().parents[2] / "recall"
    loader = importlib.machinery.SourceFileLoader("recall_cli_under_test", str(path))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


class CliTests(RecallBase):
    @classmethod
    def setUpClass(cls):
        cls.cli = load_cli()

    def test_normalize_argv_only_prepends_search_without_a_subcommand(self):
        n = self.cli.normalize_argv
        self.assertEqual(n([]), [])
        self.assertEqual(n(["how do I avoid leaking credentials"]), ["search", "how do I avoid leaking credentials"])
        self.assertEqual(n(["pm2 dump poisoned", "--since-days", "90"]),
                         ["search", "pm2 dump poisoned", "--since-days", "90"])
        self.assertEqual(n(["stats"]), ["stats"])
        self.assertEqual(n(["stats", "--json"]), ["stats", "--json"])
        self.assertEqual(n(["--json", "stats"]), ["--json", "stats"])            # subcommand later in argv
        self.assertEqual(n(["contribute", "-", "--category", "lesson"]), ["contribute", "-", "--category", "lesson"])
        self.assertEqual(n(["ingest", "--all"]), ["ingest", "--all"])
        self.assertEqual(n(["ingest", "--source", "doc", "--dry-run"]),
                         ["ingest", "--source", "doc", "--dry-run"])
        self.assertEqual(n(["--help"]), ["--help"])
        self.assertEqual(n(["-h"]), ["-h"])
        # A subcommand name AFTER "--" is query text, not a subcommand.
        self.assertEqual(n(["--", "stats"]), ["search", "--", "stats"])
        self.assertEqual(n(["--limit", "3", "--", "doctor"]), ["search", "--limit", "3", "--", "doctor"])
        self.assertEqual(n(["search", "--", "doctor"]), ["search", "--", "doctor"])

    def test_ingest_forwards_to_pipeline(self):
        seen: list[list[str]] = []

        def fake_main(argv=None):
            seen.append(list(argv or []))
            return 0

        import fleet_rag.ingest as ing
        with mock.patch.object(ing, "main", fake_main):
            rc = self.cli.main(["ingest", "--source", "doc", "--dry-run", "--limit", "2"])
            rc2 = self.cli.main(["ingest"])
        self.assertEqual(rc, 0)
        self.assertEqual(rc2, 0)
        self.assertEqual(seen, [["--source", "doc", "--dry-run", "--limit", "2"], ["--all"]])

    def test_query_that_looks_like_a_subcommand_after_dashdash(self):
        # `recall -- stats` searches for the literal word "stats" (argparse strips the "--").
        buf = io.StringIO()
        with mock.patch("sys.stdout", buf):
            rc = self.cli.main(["--limit", "2", "--json", "--", "stats"])
        self.assertIn(rc, (0, 1))
        self.assertEqual(FakeQdrant.calls[-1][1], ["stats"])

    def test_contribute_text_sources(self):
        ct = self.cli.contribute_text
        self.assertEqual(ct("plain text", None), "plain text")
        self.assertEqual(ct("-", None, stdin=io.StringIO("from stdin")), "from stdin")
        self.assertEqual(ct(None, "-", stdin=io.StringIO("from stdin 2")), "from stdin 2")
        self.assertEqual(ct("-", "-", stdin=io.StringIO("both dash")), "both dash")
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / "lesson.md"
            f.write_text("from file\n", encoding="utf-8")
            self.assertEqual(ct(None, str(f)), "from file\n")
            with self.assertRaisesRegex(FleetRagError, "not two of them"):
                ct("plain", str(f))
            with self.assertRaisesRegex(FleetRagError, "cannot read --file"):
                ct(None, str(pathlib.Path(d) / "missing.md"))
        with self.assertRaisesRegex(FleetRagError, "needs text"):
            ct(None, None)

    def test_contribute_via_file_and_stdin_end_to_end(self):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / "lesson.txt"
            f.write_text(GOOD, encoding="utf-8")
            buf = io.StringIO()
            with mock.patch("sys.stdout", buf):
                rc = self.cli.main(["contribute", "--file", str(f), "--category", "lesson",
                                    "--seat", "CLAUDE", "--json"])
        self.assertEqual(rc, 0)
        self.assertIn('"doc_id": "contrib/CLAUDE/', buf.getvalue())
        self.assertEqual(FakeQdrant.upserts[-1][0]["payload"]["text"], GOOD)

        buf = io.StringIO()
        with mock.patch("sys.stdout", buf), mock.patch("sys.stdin", io.StringIO(GOOD + "\n")):
            rc = self.cli.main(["contribute", "-", "--category", "runbook", "--seat", "GROK"])
        self.assertEqual(rc, 0)
        self.assertIn("stored contrib/GROK/", buf.getvalue())
        self.assertEqual(len(FakeQdrant.upserts), 2)

    def test_contribute_without_text_is_a_usage_error(self):
        err = io.StringIO()
        with mock.patch("sys.stderr", err):
            rc = self.cli.main(["contribute", "--category", "lesson", "--seat", "CLAUDE"])
        self.assertEqual(rc, 2)
        self.assertIn("needs text", err.getvalue())
        self.assertEqual(FakeQdrant.upserts, [])

    def test_help_recommends_file_for_credentials(self):
        self.assertIn("--file", self.cli.__doc__)
        self.assertIn("credential", self.cli.__doc__)
        self.assertIn("stdin", self.cli.__doc__)


if __name__ == "__main__":
    unittest.main()
