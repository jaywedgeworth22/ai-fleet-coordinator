"""fleet-recall-service (scripts/fleet-recall-service/server.py) against the in-process fake corpus.

    cd scripts && python3 -m unittest fleet_rag.tests.test_service -v

The server binds 127.0.0.1:0 in a thread; recall_api.install_fake_backend() replaces every
network seam, so no credentials, no Qdrant, no TEI, no gitleaks.
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import threading
import unittest
from unittest import mock
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from fleet_rag import recall_api
from fleet_rag.recall_api import FakeQdrant

SERVICE_DIR = pathlib.Path(__file__).resolve().parents[2] / "fleet-recall-service"
SERVER_PY = SERVICE_DIR / "server.py"
TOKEN = "test-token-0123456789"
GOOD_TEXT = ("pm2 start does not re-read env from the ecosystem file; restart with --update-env "
             "so the cached PATH is replaced.")


def _load_server():
    loader = importlib.machinery.SourceFileLoader("fleet_recall_service_server", str(SERVER_PY))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


server = _load_server()


class _ServiceCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        recall_api.install_fake_backend()
        cls._log = mock.patch.object(server, "log", lambda msg: None)
        cls._log.start()
        cls.httpd = server.make_server("127.0.0.1", 0, TOKEN)
        host, port = cls.httpd.server_address[:2]
        cls.base = f"http://{host}:{port}"
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, kwargs={"poll_interval": 0.1}, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls._log.stop()

    def setUp(self) -> None:
        recall_api.install_fake_backend()
        server.reset_health_cache()
        os.environ.pop("AGENT_SEAT", None)

    def request(self, method: str, path: str, body=None, token: str | None = TOKEN,
                headers: dict | None = None, raw: bytes | None = None):
        data = raw if raw is not None else (None if body is None else json.dumps(body).encode())
        hdrs = {"Content-Type": "application/json", **(headers or {})}
        if token is not None:
            hdrs["Authorization"] = "Bearer " + token
        req = Request(self.base + path, data=data, method=method, headers=hdrs)
        try:
            with urlopen(req, timeout=10) as resp:
                payload = resp.read()
                return resp.status, dict(resp.headers), (json.loads(payload) if payload else None)
        except HTTPError as e:
            with e:
                payload = e.read()
            return e.code, dict(e.headers), (json.loads(payload) if payload else None)

    def rpc(self, method: str, params=None, rid: int | None = 1, headers: dict | None = None, token=TOKEN):
        msg: dict = {"jsonrpc": "2.0", "method": method}
        if rid is not None:
            msg["id"] = rid
        if params is not None:
            msg["params"] = params
        return self.request("POST", "/mcp", msg, token=token, headers=headers)


class HealthTests(_ServiceCase):
    def test_health_is_public_and_reports_backend(self):
        status, headers, body = self.request("GET", "/health", token=None)
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        self.assertEqual(body["name"], "fleet-recall-service")
        self.assertEqual(body["version"], server.SERVICE_VERSION)
        self.assertEqual(body["collection"], "fleet-agents-fake")
        self.assertEqual(body["points"], 3)
        self.assertTrue(body["backend_ok"])
        self.assertEqual(body["recall"], list(server.RECALL_PATHS))
        self.assertEqual(body["mcp"], "/mcp")
        self.assertEqual(headers.get("Cache-Control"), "no-store")

    def test_root_and_head_health(self):
        status, _, body = self.request("GET", "/", token=None)
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        req = Request(self.base + "/health", method="HEAD")
        with urlopen(req, timeout=10) as resp:
            self.assertEqual(resp.status, 200)
            self.assertEqual(resp.read(), b"")

    def test_health_survives_backend_failure(self):
        class Boom(FakeQdrant):
            def info(self):
                raise ConnectionError("down")
        with mock.patch.object(recall_api, "Qdrant", Boom):
            status, _, body = self.request("GET", "/health", token=None)
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        self.assertFalse(body["backend_ok"])
        self.assertIsNone(body["points"])
        self.assertEqual(body["error"], "ConnectionError")
        self.assertNotIn("down", json.dumps(body))

    def test_health_count_is_cached(self):
        self.request("GET", "/health", token=None)
        FakeQdrant.points.append({"id": "extra", "payload": {"source": "doc", "text": "x"}})
        _, _, body = self.request("GET", "/health", token=None)
        self.assertEqual(body["points"], 3)          # cached snapshot
        server.reset_health_cache()
        _, _, body = self.request("GET", "/health", token=None)
        self.assertEqual(body["points"], 4)


class AuthTests(_ServiceCase):
    def test_missing_token_is_401_everywhere_but_health(self):
        for method, path in (("GET", "/recall/stats"), ("POST", "/recall/search"),
                             ("POST", "/recall/contribute"), ("POST", "/mcp"), ("GET", "/mcp"),
                             ("DELETE", "/mcp")):
            status, headers, body = self.request(method, path, {"query": "x"}, token=None)
            self.assertEqual(status, 401, (method, path))
            self.assertEqual(headers.get("WWW-Authenticate"), "Bearer")
            self.assertEqual(body, {"ok": False, "error": "unauthorized"})

    def test_wrong_token_is_401(self):
        for bad in ("nope", TOKEN[:-1], TOKEN + "x", TOKEN.upper()):
            status, _, _ = self.request("GET", "/recall/stats", token=bad)
            self.assertEqual(status, 401, bad)
        status, _, _ = self.request("GET", "/recall/stats", token=None, headers={"Authorization": "Basic " + TOKEN})
        self.assertEqual(status, 401)
        status, _, _ = self.request("GET", "/recall/stats", token=None, headers={"Authorization": TOKEN})
        self.assertEqual(status, 401)

    def test_right_token_is_200(self):
        status, _, body = self.request("GET", "/recall/stats")
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        status, _, _ = self.request("GET", "/recall/stats", token=None, headers={"Authorization": "BEARER " + TOKEN})
        self.assertEqual(status, 200)                # scheme is case-insensitive

    def test_bearer_ok_helper(self):
        self.assertTrue(server.bearer_ok("Bearer " + TOKEN, TOKEN))
        self.assertFalse(server.bearer_ok("Bearer " + TOKEN, ""))
        self.assertFalse(server.bearer_ok("", TOKEN))
        self.assertFalse(server.bearer_ok(None, TOKEN))
        self.assertFalse(server.bearer_ok("Bearer", TOKEN))
        self.assertFalse(server.bearer_ok("Bearer " + TOKEN[:-1], TOKEN))


class RestTests(_ServiceCase):
    def test_stats(self):
        status, _, body = self.request("GET", "/recall/stats")
        self.assertEqual(status, 200)
        self.assertEqual(body["collection"], "fleet-agents-fake")
        self.assertEqual(body["points"], 3)
        self.assertEqual(body["by_source"]["doc"], 3)
        self.assertTrue(body["embedder_healthy"])
        # POST works too (seat-mcp parity).
        status, _, body2 = self.request("POST", "/recall/stats", {})
        self.assertEqual(status, 200)
        self.assertEqual(body2["points"], 3)

    def test_search(self):
        status, _, body = self.request("POST", "/recall/search",
                                       {"query": "leaking credentials handoff", "limit": "2", "app": "fleet"})
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        self.assertEqual(body["mode"], "hybrid")
        self.assertEqual(len(body["hits"]), 2)
        self.assertIn("global-api-keys", body["hits"][0]["text"])
        # recall_api may over-fetch for grouping / rerank; the contract is the returned hit count
        # (asserted above) and the filter that reached Qdrant.
        _, terms, limit, flt = FakeQdrant.calls[-1]
        self.assertGreaterEqual(limit, 2)
        self.assertIn({"key": "source", "match": {"value": "meta"}}, flt["must_not"])
        self.assertIn({"key": "app", "match": {"value": "fleet"}}, flt["must"])

    def test_search_errors(self):
        status, _, body = self.request("POST", "/recall/search", {})
        self.assertEqual(status, 400)
        self.assertFalse(body["ok"])
        self.assertIn("query", body["error"])
        status, _, body = self.request("POST", "/recall/search", {"query": "x", "limit": "lots"})
        self.assertEqual(status, 400)
        self.assertIn("limit", body["error"])
        status, _, body = self.request("POST", "/recall/search", {"query": "x", "bogus": 1})
        self.assertEqual(status, 400)
        self.assertIn("bogus", body["error"])
        status, _, body = self.request("POST", "/recall/search", {"query": "x", "category": "nope"})
        self.assertEqual(status, 400)
        self.assertIn("category", body["error"])
        status, _, body = self.request("POST", "/recall/search", raw=b"not json")
        self.assertEqual(status, 400)
        self.assertEqual(body["error"], "parse error")
        status, _, body = self.request("POST", "/recall/search", raw=b"[1,2]")
        self.assertEqual(status, 400)
        self.assertIn("object", body["error"])
        status, _, _ = self.request("GET", "/recall/search")
        self.assertEqual(status, 405)

    def test_contribute_requires_seat_and_ignores_process_agent_seat(self):
        os.environ["AGENT_SEAT"] = "SERVERSEAT"
        try:
            status, _, body = self.request("POST", "/recall/contribute", {"text": GOOD_TEXT, "category": "lesson"})
        finally:
            os.environ.pop("AGENT_SEAT", None)
        self.assertEqual(status, 400)
        self.assertIn("seat is required", body["error"])
        self.assertEqual(FakeQdrant.upserts, [])

    def test_contribute_round_trip(self):
        status, _, body = self.request("POST", "/recall/contribute",
                                       {"text": GOOD_TEXT, "category": "lesson", "seat": "cursor",
                                        "app": "fleet", "title": "pm2 env", "url": "https://example.com/pr/1"})
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        self.assertTrue(body["doc_id"].startswith("contrib/CURSOR/"))
        self.assertEqual(body["status"], "completed")
        self.assertEqual(len(FakeQdrant.upserts), 1)
        stored = FakeQdrant.upserts[0][0]["payload"]
        self.assertEqual(stored["seat"], "CURSOR")
        self.assertEqual(stored["source"], "agent-contribution")
        self.assertEqual(stored["url"], "https://example.com/pr/1")
        status, _, again = self.request("POST", "/recall/search", {"query": "update-env", "source": "agent-contribution"})
        self.assertEqual(status, 200)
        self.assertEqual(len(again["hits"]), 1)
        self.assertEqual(again["hits"][0]["seat"], "CURSOR")

    def test_contribute_validation(self):
        status, _, body = self.request("POST", "/recall/contribute", {"text": "too short", "category": "lesson", "seat": "X"})
        self.assertEqual(status, 400)
        self.assertIn("too short", body["error"])
        status, _, body = self.request("POST", "/recall/contribute", {"text": GOOD_TEXT, "category": "doc", "seat": "X"})
        self.assertEqual(status, 400)
        self.assertIn("category", body["error"])

    def test_backend_failure_is_502_class_only(self):
        class Boom(FakeQdrant):
            def query_hybrid(self, *a, **k):
                raise RuntimeError("secret-ish detail http://10.0.0.1")
        with mock.patch.object(recall_api, "Qdrant", Boom):
            status, _, body = self.request("POST", "/recall/search", {"query": "anything at all"})
        self.assertEqual(status, 502)
        self.assertEqual(body["error"], "recall_search failed: RuntimeError")

    def test_unknown_paths_and_payload_limit(self):
        status, _, body = self.request("GET", "/nope")
        self.assertEqual(status, 404)
        status, _, _ = self.request("POST", "/recall/nope", {})
        self.assertEqual(status, 404)
        status, _, body = self.request("POST", "/recall/search", token=TOKEN,
                                       headers={"Content-Length": str(server.MAX_BODY + 1)}, raw=b"")
        self.assertEqual(status, 413)


class McpTests(_ServiceCase):
    def test_initialize_sets_session_id_and_echoes_known_version(self):
        status, headers, body = self.rpc("initialize", {"protocolVersion": "2025-03-26", "capabilities": {},
                                                        "clientInfo": {"name": "t", "version": "0"}})
        self.assertEqual(status, 200)
        self.assertEqual(body["id"], 1)
        res = body["result"]
        self.assertEqual(res["protocolVersion"], "2025-03-26")
        self.assertEqual(res["serverInfo"]["name"], "fleet-recall-service")
        self.assertEqual(res["capabilities"], {"tools": {"listChanged": False}})
        self.assertIn("recall_search", res["instructions"])
        sid = headers.get("MCP-Session-Id")
        self.assertTrue(sid and len(sid) == 32)
        # Unknown / missing protocol version falls back to the default.
        _, _, body = self.rpc("initialize", {"protocolVersion": "1999-01-01"})
        self.assertEqual(body["result"]["protocolVersion"], server.DEFAULT_PROTOCOL)
        _, _, body = self.rpc("initialize", {})
        self.assertEqual(body["result"]["protocolVersion"], server.DEFAULT_PROTOCOL)

    def test_notification_is_202_with_no_body(self):
        status, headers, body = self.rpc("notifications/initialized", rid=None)
        self.assertEqual(status, 202)
        self.assertIsNone(body)
        self.assertNotIn("MCP-Session-Id", headers)

    def test_ping_list_discover(self):
        _, _, body = self.rpc("ping", rid=7)
        self.assertEqual(body, {"jsonrpc": "2.0", "id": 7, "result": {}})
        _, _, body = self.rpc("tools/list", rid=8)
        tools = body["result"]["tools"]
        self.assertEqual([t["name"] for t in tools], ["recall_search", "recall_stats", "recall_contribute"])
        for t in tools:
            self.assertEqual(t["inputSchema"]["type"], "object")
            self.assertTrue(t["description"])
        self.assertEqual(tools[0]["inputSchema"]["required"], ["query"])
        self.assertEqual(tools[2]["inputSchema"]["required"], ["text", "category", "seat"])
        _, _, body = self.rpc("server/discover", rid=9)
        self.assertEqual(body["result"]["protocolVersions"], list(server.PROTOCOL_VERSIONS))
        self.assertEqual(len(body["result"]["tools"]), 3)

    def test_tools_call_stats_search_contribute(self):
        _, _, body = self.rpc("tools/call", {"name": "recall_stats"}, rid=2)
        res = body["result"]
        self.assertFalse(res["isError"])
        self.assertEqual(res["structuredContent"]["points"], 3)
        self.assertEqual(json.loads(res["content"][0]["text"])["points"], 3)

        _, _, body = self.rpc("tools/call", {"name": "recall_search",
                                             "arguments": {"query": "leaking credentials handoff", "limit": "2"}}, rid=3)
        res = body["result"]
        self.assertFalse(res["isError"])
        self.assertEqual(res["structuredContent"]["mode"], "hybrid")
        self.assertEqual(len(res["structuredContent"]["hits"]), 2)

        _, _, body = self.rpc("tools/call", {"name": "recall_contribute",
                                             "arguments": {"text": GOOD_TEXT, "category": "lesson", "seat": "GROK"}}, rid=4)
        res = body["result"]
        self.assertFalse(res["isError"])
        self.assertTrue(res["structuredContent"]["doc_id"].startswith("contrib/GROK/"))

        _, _, body = self.rpc("tools/call", {"name": "recall_search",
                                             "arguments": {"query": "update-env", "source": "agent-contribution"}}, rid=5)
        self.assertEqual(body["result"]["structuredContent"]["hits"][0]["seat"], "GROK")

    def test_tools_call_errors(self):
        _, _, body = self.rpc("tools/call", {"name": "recall_contribute",
                                             "arguments": {"text": GOOD_TEXT, "category": "lesson"}}, rid=2)
        self.assertTrue(body["result"]["isError"])
        self.assertIn("seat is required", body["result"]["content"][0]["text"])
        _, _, body = self.rpc("tools/call", {"name": "recall_contribute",
                                             "arguments": {"text": "too short", "category": "lesson", "seat": "X"}}, rid=3)
        self.assertTrue(body["result"]["isError"])
        self.assertIn("too short", body["result"]["content"][0]["text"])
        _, _, body = self.rpc("tools/call", {"name": "nope", "arguments": {}}, rid=4)
        self.assertEqual(body["error"]["code"], -32602)
        _, _, body = self.rpc("tools/call", {"name": "recall_search", "arguments": [1]}, rid=5)
        self.assertEqual(body["error"]["code"], -32602)
        _, _, body = self.rpc("tools/call", {"name": "recall_search", "arguments": {"query": "x", "bogus": 1}}, rid=6)
        self.assertTrue(body["result"]["isError"])
        self.assertIn("bogus", body["result"]["content"][0]["text"])
        _, _, body = self.rpc("resources/list", rid=7)
        self.assertEqual(body["error"]["code"], -32601)
        _, _, body = self.rpc("tools/list", params=[1, 2], rid=8)
        self.assertEqual(body["error"]["code"], -32602)

    def test_framing_errors(self):
        status, _, body = self.request("POST", "/mcp", raw=b"not json")
        self.assertEqual(status, 400)
        self.assertEqual(body["error"]["code"], -32700)
        status, _, body = self.request("POST", "/mcp", raw=b"[1]")
        self.assertEqual(status, 400)
        self.assertEqual(body["error"]["code"], -32600)
        status, _, body = self.rpc("ping", headers={"Mcp-Method": "tools/list"})
        self.assertEqual(status, 400)
        self.assertIn("Mcp-Method", body["error"]["message"])
        status, _, body = self.rpc("ping", headers={"MCP-Protocol-Version": "1999-01-01"})
        self.assertEqual(status, 400)
        self.assertIn("MCP-Protocol-Version", body["error"]["message"])
        status, _, body = self.rpc("ping", headers={"MCP-Protocol-Version": "2025-11-25"})
        self.assertEqual(status, 200)
        status, _, body = self.request("GET", "/mcp")
        self.assertEqual(status, 405)
        status, _, body = self.request("DELETE", "/mcp")
        self.assertEqual(status, 405)

    def test_backend_failure_in_tool_reports_class_only(self):
        class Boom(FakeQdrant):
            def info(self):
                raise RuntimeError("api-key=abc")
        with mock.patch.object(recall_api, "Qdrant", Boom):
            _, _, body = self.rpc("tools/call", {"name": "recall_stats"}, rid=2)
        self.assertTrue(body["result"]["isError"])
        self.assertEqual(body["result"]["content"][0]["text"], "recall_stats failed: RuntimeError")


class ProcessTests(unittest.TestCase):
    """The real entry point: refuses to start without a token, serves the fake corpus with one."""

    def test_refuses_without_token(self):
        env = {k: v for k, v in os.environ.items() if k != "RECALL_API_TOKEN"}
        proc = subprocess.run([sys.executable, str(SERVER_PY)], env=env, capture_output=True, text=True, timeout=30)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("RECALL_API_TOKEN is not set", proc.stdout)

    def test_fake_mode_serves_health_and_logs_no_token(self):
        import socket
        import time
        with socket.socket() as s:
            s.bind(("127.0.0.1", 0))
            port = s.getsockname()[1]
        env = {**os.environ, "RECALL_API_TOKEN": TOKEN, "RECALL_FAKE": "1", "HOST": "127.0.0.1", "PORT": str(port)}
        proc = subprocess.Popen([sys.executable, str(SERVER_PY)], env=env, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)
        try:
            deadline = time.time() + 15
            body = None
            while time.time() < deadline:
                try:
                    with urlopen(f"http://127.0.0.1:{port}/health", timeout=2) as r:
                        body = json.loads(r.read())
                        break
                except OSError:
                    time.sleep(0.2)
            self.assertIsNotNone(body, "server did not come up")
            self.assertEqual(body["points"], 3)
            req = Request(f"http://127.0.0.1:{port}/recall/stats", headers={"Authorization": "Bearer " + TOKEN})
            with urlopen(req, timeout=5) as r:
                self.assertEqual(json.loads(r.read())["points"], 3)
        finally:
            proc.terminate()
            out, _ = proc.communicate(timeout=10)
        self.assertIn("FAKE", out)
        self.assertIn("listening on 127.0.0.1", out)
        self.assertNotIn(TOKEN, out)
        self.assertNotIn("Bearer", out)


if __name__ == "__main__":
    unittest.main()
