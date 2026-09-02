#!/usr/bin/env python3
"""fleet-recall-service -- Hetzner-side HTTP front for the fleet-agents corpus.

Stdlib only.  One ThreadingHTTPServer that imports fleet_rag.recall_api and exposes:

  GET  /health               no auth   {ok, version, collection, points, backend_ok}
  GET  /recall/stats         bearer    recall_stats()
  POST /recall/search        bearer    recall_search(**body)
  POST /recall/contribute    bearer    recall_contribute(**body)   (seat REQUIRED)
  POST /mcp                  bearer    streamable-HTTP JSON-RPC: initialize,
                                       notifications/*, ping, tools/list, tools/call,
                                       server/discover (same framing as seat-mcp)

Auth is `Authorization: Bearer <RECALL_API_TOKEN>` on everything except /health, compared in
constant time.  Configuration comes from the environment only (see REQUIRED_ENV); the process
never reads ~/.secrets.  Logs go to stdout and never include bodies, tokens, or query strings.

The service exists so cloud seats and phones reach recall even while the Mac is asleep: it runs
on the Coolify box next to Qdrant and TEI (both reachable over the host's Tailscale address).
Set RECALL_FAKE=1 to serve recall_api's in-process fake corpus (tests, smoke checks).
"""
from __future__ import annotations

import hmac
import json
import os
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import urlparse

# The service dir sits next to the fleet_rag package (scripts/ in the repo, /app in the
# container), so the parent directory is the import root.
_HERE = os.path.dirname(os.path.realpath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from fleet_rag import __version__ as _RAG_VERSION  # noqa: E402
from fleet_rag import recall_api  # noqa: E402
from fleet_rag.core import FleetRagError  # noqa: E402

SERVICE_VERSION = "1.0.0"
SERVER_NAME = "fleet-recall-service"
MCP_PATH = "/mcp"
RECALL_PATHS = ("/recall/stats", "/recall/search", "/recall/contribute")
PROTOCOL_VERSIONS = ("2024-11-05", "2025-03-26", "2025-06-18", "2025-11-25", "2026-07-28")
DEFAULT_PROTOCOL = "2025-11-25"
MAX_BODY = 2_000_000
HEALTH_CACHE_S = 30.0

REQUIRED_ENV = ("QDRANT_URL", "QDRANT_API_KEY", "QDRANT_FLEET_COLLECTION", "TEI_URL", "TEI_API_KEY")
OPTIONAL_ENV = ("QDRANT_READONLY_API_KEY", "TEI_EMBED_MODEL")

JsonDict = dict[str, Any]

# --------------------------------------------------------------------------- tool contract

TOOLS: list[JsonDict] = [
    {
        "name": "recall_search",
        "description": (
            "Search the fleet's shared knowledge corpus (lessons, owner preferences, infrastructure "
            "facts, decisions, runbooks, board findings, effort logs, Apple Notes, fleet docs).  Use it "
            "BEFORE re-deriving a lesson, guessing an owner preference, or debugging infrastructure "
            "another seat has already documented.  Hybrid dense + keyword search; filter by category, "
            "app, source, seat, or recency.  Read-only."),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Natural-language question or keywords."},
                "limit": {"type": "integer", "minimum": 1, "maximum": recall_api.MAX_LIMIT, "default": 5},
                "category": {"type": "string", "enum": list(recall_api.CATEGORIES),
                             "description": "Restrict to one category."},
                "app": {"type": "string", "description": "Lowercase app slug, e.g. fleet, socratic-trade."},
                "source": {"type": "string", "enum": list(recall_api.SOURCES)},
                "seat": {"type": "string", "description": "Uppercase seat tag, e.g. CLAUDE, GROK."},
                "since_days": {"type": "integer", "minimum": 1,
                               "description": "Only content created in the last N days."},
            },
            "required": ["query"],
        },
    },
    {
        "name": "recall_stats",
        "description": (
            "Collection health and point counts by source and app.  Use it to check the corpus is "
            "reachable before relying on recall_search, or to see which sources have been ingested."),
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "recall_contribute",
        "description": (
            "Store one reusable piece of knowledge for every other seat: a lesson learned, an owner "
            "preference, an infrastructure fact, a decision, or a runbook step.  Use it AFTER you learn "
            "something reusable that is not already in the corpus (search first).  40..4000 chars, "
            "secrets are scrubbed and the scrub kinds returned; text that still looks like a secret is "
            "refused.  seat is REQUIRED on this surface (a cloud caller has no AGENT_SEAT)."),
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "minLength": recall_api.CONTRIB_MIN,
                         "maxLength": recall_api.CONTRIB_MAX},
                "category": {"type": "string", "enum": list(recall_api.CONTRIB_CATEGORIES)},
                "app": {"type": "string", "default": "fleet"},
                "seat": {"type": "string", "description": "Your uppercase seat tag (required)."},
                "title": {"type": "string"},
                "url": {"type": "string", "description": "Source link (PR, board item, doc), optional."},
            },
            "required": ["text", "category", "seat"],
        },
    },
]

_ALLOWED_ARGS = {t["name"]: set(t["inputSchema"]["properties"]) for t in TOOLS}
_REQUIRED_ARGS = {t["name"]: list(t["inputSchema"].get("required", [])) for t in TOOLS}


def _int(args: JsonDict, key: str) -> None:
    val = args.get(key)
    if key not in args or val is None or val == "":
        args.pop(key, None)
        return
    if isinstance(val, bool):
        raise FleetRagError(f"{key} must be an integer")
    try:
        args[key] = int(val)
    except (TypeError, ValueError):
        raise FleetRagError(f"{key} must be an integer") from None


def call_tool(name: str, args: JsonDict) -> JsonDict:
    """Validate the argument set and dispatch to recall_api.  KeyError for an unknown tool."""
    if name not in _ALLOWED_ARGS:
        raise KeyError(name)
    if not isinstance(args, dict):
        raise FleetRagError("arguments must be an object")
    args = dict(args)
    unknown = set(args) - _ALLOWED_ARGS[name]
    if unknown:
        raise FleetRagError("unknown argument(s): " + ", ".join(sorted(unknown)))
    missing = [k for k in _REQUIRED_ARGS[name] if args.get(k) is None and k != "seat"]
    if missing:
        raise FleetRagError("missing required argument(s): " + ", ".join(missing))
    if name == "recall_search":
        _int(args, "limit")
        _int(args, "since_days")
        return recall_api.recall_search(**args)
    if name == "recall_stats":
        return recall_api.recall_stats()
    seat = args.get("seat")
    if not isinstance(seat, str) or not seat.strip():
        # Never fall back to the service process's own AGENT_SEAT for a remote caller.
        raise FleetRagError("seat is required on this surface (cloud callers have no AGENT_SEAT); "
                            "pass your uppercase seat tag, e.g. GROK, CURSOR, CLAUDE")
    return recall_api.recall_contribute(**args)


# --------------------------------------------------------------------------- health

_health_lock = threading.Lock()
_health_cache: dict[str, Any] = {"at": 0.0, "value": None}


def _backend_snapshot() -> JsonDict:
    """Collection name and live point count, cached for HEALTH_CACHE_S.  Never raises."""
    now = time.monotonic()
    with _health_lock:
        if _health_cache["value"] is not None and now - _health_cache["at"] < HEALTH_CACHE_S:
            return dict(_health_cache["value"])
    snap: JsonDict = {"collection": os.environ.get("QDRANT_FLEET_COLLECTION") or None,
                      "points": None, "backend_ok": False}
    try:
        cfg = recall_api.get_config(need_write=False)
        q = recall_api.Qdrant(cfg)
        info = q.info()
        snap = {"collection": q.collection, "points": int(info.get("points_count", 0)), "backend_ok": True}
    except Exception as e:  # noqa: BLE001 - class only, never the message (it may name hosts)
        snap["error"] = type(e).__name__
    with _health_lock:
        _health_cache.update(at=now, value=dict(snap))
    return snap


def reset_health_cache() -> None:
    with _health_lock:
        _health_cache.update(at=0.0, value=None)


def health_payload() -> JsonDict:
    return {"ok": True, "name": SERVER_NAME, "version": SERVICE_VERSION, "fleet_rag": _RAG_VERSION,
            **_backend_snapshot(), "mcp": MCP_PATH, "recall": list(RECALL_PATHS)}


# --------------------------------------------------------------------------- MCP

def _json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, ensure_ascii=True) + "\n").encode("utf-8")


def _rpc_error(rid: Any, code: int, message: str) -> JsonDict:
    return {"jsonrpc": "2.0", "id": rid, "error": {"code": code, "message": message}}


def handle_rpc(msg: JsonDict) -> JsonDict | None:
    """One JSON-RPC message -> response dict, or None for a notification."""
    method = msg.get("method")
    rid = msg.get("id")
    is_notification = "id" not in msg
    params = msg.get("params")
    if params is None:
        params = {}
    elif not isinstance(params, dict):
        return None if is_notification else _rpc_error(rid, -32602, "params must be an object")
    if not isinstance(method, str) or not method:
        return None if is_notification else _rpc_error(rid, -32600, "invalid request")

    def ok(result: Any) -> JsonDict:
        return {"jsonrpc": "2.0", "id": rid, "result": result}

    if method == "initialize":
        requested = params.get("protocolVersion")
        version = requested if isinstance(requested, str) and requested in PROTOCOL_VERSIONS else DEFAULT_PROTOCOL
        return ok({
            "protocolVersion": version,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVICE_VERSION},
            "instructions": (
                "Fleet RAG over the fleet-agents corpus.  Search before re-deriving a lesson; "
                "contribute after you learn something reusable.  Tools: recall_search, "
                "recall_stats, recall_contribute (seat required).  REST twins: GET /recall/stats, "
                "POST /recall/search, POST /recall/contribute with the same bearer."),
        })
    if method == "server/discover":
        return ok({"protocolVersions": list(PROTOCOL_VERSIONS),
                   "capabilities": {"tools": {"listChanged": False}},
                   "serverInfo": {"name": SERVER_NAME, "version": SERVICE_VERSION},
                   "tools": TOOLS})
    if method == "ping":
        return ok({})
    if method == "tools/list":
        return ok({"tools": TOOLS})
    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments")
        if args is None:
            args = {}
        if not isinstance(args, dict):
            return _rpc_error(rid, -32602, "arguments must be an object")
        try:
            data = call_tool(str(name), args)
        except KeyError:
            return _rpc_error(rid, -32602, f"unknown tool: {name}")
        except FleetRagError as e:
            return ok({"content": [{"type": "text", "text": str(e)}], "isError": True})
        except Exception as e:  # noqa: BLE001 - keep serving; report the class only
            log(f"tools/call {name} failed: {type(e).__name__}")
            return ok({"content": [{"type": "text", "text": f"{name} failed: {type(e).__name__}"}],
                       "isError": True})
        return ok({"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=True)}],
                   "structuredContent": data, "isError": False})
    if method.startswith("notifications/"):
        return None if is_notification else ok({})
    if is_notification:
        return None
    return _rpc_error(rid, -32601, f"method not found: {method}")


# --------------------------------------------------------------------------- auth / logging

def bearer_ok(header: str | None, token: str) -> bool:
    """Constant-time check of `Authorization: Bearer <token>`."""
    if not header or not token:
        return False
    parts = header.split(None, 1)
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return False
    got = parts[1].strip()
    if len(got) != len(token):
        hmac.compare_digest(token, token)
        return False
    return hmac.compare_digest(got, token)


def log(msg: str) -> None:
    ts = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
    sys.stdout.write(f"{ts}Z {SERVER_NAME}: {msg}\n")
    sys.stdout.flush()


# --------------------------------------------------------------------------- handler

class RecallHandler(BaseHTTPRequestHandler):
    server_version = f"{SERVER_NAME}/{SERVICE_VERSION}"
    sys_version = ""
    token = ""
    protocol_version = "HTTP/1.1"

    # -- plumbing
    def log_message(self, fmt: str, *args: Any) -> None:  # noqa: D401 - BaseHTTPRequestHandler hook
        # Path only (no query string), no headers, no bodies.
        pass

    def _send(self, code: int, body: bytes, ctype: str = "application/json",
              extra: list[tuple[str, str]] | None = None) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for k, v in extra or []:
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD" and body:
            self.wfile.write(body)
        log(f"{self.command} {urlparse(self.path).path} {code}")

    def _unauthorized(self) -> None:
        self._send(401, _json_bytes({"ok": False, "error": "unauthorized"}),
                   extra=[("WWW-Authenticate", "Bearer")])

    def _auth_ok(self) -> bool:
        return bearer_ok(self.headers.get("Authorization"), self.token)

    def _read_body(self) -> bytes | None:
        try:
            length = int(self.headers.get("Content-Length", "0") or 0)
        except ValueError:
            length = 0
        if length < 0 or length > MAX_BODY:
            self._send(413, _json_bytes({"ok": False, "error": "payload too large"}))
            return None
        return self.rfile.read(length) if length else b""

    def _read_json_object(self) -> JsonDict | None:
        raw = self._read_body()
        if raw is None:
            return None
        try:
            msg = json.loads(raw.decode("utf-8") or "{}")
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send(400, _json_bytes({"ok": False, "error": "parse error"}))
            return None
        if not isinstance(msg, dict):
            self._send(400, _json_bytes({"ok": False, "error": "body must be a JSON object"}))
            return None
        return msg

    def _not_found(self) -> None:
        self._send(404, _json_bytes({"ok": False, "error": "not found"}))

    # -- REST
    def _recall_rest(self, name: str, args: JsonDict) -> None:
        try:
            data = call_tool(name, args)
        except FleetRagError as e:
            self._send(400, _json_bytes({"ok": False, "error": str(e)}))
            return
        except Exception as e:  # noqa: BLE001
            log(f"{name} failed: {type(e).__name__}")
            self._send(502, _json_bytes({"ok": False, "error": f"{name} failed: {type(e).__name__}"}))
            return
        self._send(200, _json_bytes({"ok": True, **data}))

    # -- verbs
    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path in ("/health", "/"):
            self._send(200, _json_bytes(health_payload()))
            return
        if path == "/recall/stats":
            if not self._auth_ok():
                self._unauthorized()
                return
            self._recall_rest("recall_stats", {})
            return
        if path == MCP_PATH:
            if not self._auth_ok():
                self._unauthorized()
                return
            # No standalone SSE stream in v1; the spec allows 405.
            self._send(405, _json_bytes({"ok": False, "error": "sse not offered"}),
                       extra=[("Allow", "POST")])
            return
        if path in RECALL_PATHS:
            self._send(405, _json_bytes({"ok": False, "error": "use POST"}), extra=[("Allow", "POST")])
            return
        self._not_found()

    def do_HEAD(self) -> None:
        self.do_GET()

    def do_DELETE(self) -> None:
        path = urlparse(self.path).path
        if path != MCP_PATH:
            self._not_found()
            return
        if not self._auth_ok():
            self._unauthorized()
            return
        self._send(405, _json_bytes({"ok": False, "error": "sessions are not server-owned"}))

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path in RECALL_PATHS:
            if not self._auth_ok():
                self._unauthorized()
                return
            msg = self._read_json_object()
            if msg is None:
                return
            self._recall_rest("recall_" + path.rsplit("/", 1)[-1], msg)
            return
        if path != MCP_PATH:
            self._not_found()
            return
        if not self._auth_ok():
            self._unauthorized()
            return
        raw = self._read_body()
        if raw is None:
            return
        try:
            msg = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send(400, _json_bytes(_rpc_error(None, -32700, "parse error")))
            return
        if not isinstance(msg, dict):
            self._send(400, _json_bytes(_rpc_error(None, -32600, "invalid request")))
            return
        header_method = self.headers.get("Mcp-Method") or self.headers.get("MCP-Method")
        if header_method and msg.get("method") and header_method != msg.get("method"):
            self._send(400, _json_bytes(_rpc_error(msg.get("id"), -32600, "Mcp-Method mismatch")))
            return
        proto = self.headers.get("MCP-Protocol-Version") or self.headers.get("Mcp-Protocol-Version")
        if proto and proto not in PROTOCOL_VERSIONS:
            self._send(400, _json_bytes(_rpc_error(msg.get("id"), -32600, "unsupported MCP-Protocol-Version")))
            return
        result = handle_rpc(msg)
        extra: list[tuple[str, str]] = []
        if msg.get("method") == "initialize" and result and "result" in result:
            extra.append(("MCP-Session-Id", uuid.uuid4().hex))
        if result is None:
            self._send(202, b"", extra=extra)
            return
        self._send(200, _json_bytes(result), extra=extra)


# --------------------------------------------------------------------------- lifecycle

def make_server(host: str, port: int, token: str) -> ThreadingHTTPServer:
    """Build (but do not run) the server.  Tests bind 127.0.0.1:0 and serve in a thread."""
    handler = type("BoundRecallHandler", (RecallHandler,), {"token": token})
    httpd = ThreadingHTTPServer((host, port), handler)
    httpd.allow_reuse_address = True
    httpd.daemon_threads = True
    return httpd


def env_report() -> tuple[list[str], list[str]]:
    """(present, missing) required env NAMES.  Values are never returned."""
    present = [k for k in REQUIRED_ENV if os.environ.get(k)]
    missing = [k for k in REQUIRED_ENV if not os.environ.get(k)]
    return present, missing


def main(argv: list[str] | None = None) -> int:
    token = os.environ.get("RECALL_API_TOKEN", "").strip()
    if not token:
        log("RECALL_API_TOKEN is not set; refusing to start")
        return 2
    if os.environ.get("RECALL_FAKE") == "1":
        recall_api.install_fake_backend()
        log("serving the FAKE in-process corpus (RECALL_FAKE=1)")
    else:
        present, missing = env_report()
        optional = [k for k in OPTIONAL_ENV if os.environ.get(k)]
        log("env present: " + ", ".join(present + optional))
        if missing:
            log("env MISSING: " + ", ".join(missing) + " (tools will fail until set)")
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8080"))
    httpd = make_server(host, port, token)
    log(f"listening on {host}:{port}  mcp={MCP_PATH}  recall={','.join(RECALL_PATHS)}  "
        f"service={SERVICE_VERSION} fleet_rag={_RAG_VERSION}")
    try:
        httpd.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
