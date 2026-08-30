#!/usr/bin/env python3
"""Grok ACP WebSocket client for Conductor.

Uses the always-on grok-acp adapter on 127.0.0.1:12419 (--no-leader serve).
Empty mcpServers means "use config.toml" unless grok-acp is running from
its stripped GROK_HOME (acp-home), in which case empty means no MCPs.
Pass --mcp-server NAME to expand names from ~/.grok/config.toml.

Never prints GROK_AGENT_SECRET or MCP env/header values.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

import websockets

from mcp_catalog import CatalogError, expand_names

HOST = "127.0.0.1"
PORT = 12419
WS_PATH = "/ws"
SECRET_FILE = Path.home() / ".secrets" / "grok-acp.env"


def load_secret() -> str:
    if not SECRET_FILE.is_file():
        sys.exit(f"missing {SECRET_FILE}")
    secret = ""
    for line in SECRET_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("GROK_AGENT_SECRET="):
            secret = line.split("=", 1)[1].strip().strip("'\"")
            break
    if not secret:
        sys.exit("GROK_AGENT_SECRET empty")
    return secret


class AcpClient:
    def __init__(self, ws):
        self.ws = ws
        self._next_id = 1
        self._pending = {}

    def _id(self) -> int:
        n = self._next_id
        self._next_id += 1
        return n

    async def request(self, method: str, params, timeout: float = 60.0):
        req_id = self._id()
        fut = asyncio.get_event_loop().create_future()
        self._pending[req_id] = fut
        await self.ws.send(json.dumps({"jsonrpc": "2.0", "id": req_id, "method": method, "params": params}))
        return await asyncio.wait_for(fut, timeout=timeout)

    async def pump(self, collect_updates=False):
        updates = []
        async for raw in self.ws:
            if not raw:
                continue
            if raw == "ping":
                continue
            try:
                msg = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if "id" in msg and msg["id"] in self._pending:
                fut = self._pending.pop(msg["id"])
                if "error" in msg:
                    fut.set_exception(RuntimeError(json.dumps(msg["error"])))
                else:
                    fut.set_result(msg.get("result", {}))
                if not collect_updates:
                    return
            elif collect_updates and msg.get("method") == "session/update":
                updates.append(msg)
                # keep going until the matching session/prompt result arrives
            if collect_updates and not self._pending:
                return updates
        if collect_updates:
            return updates

    async def initialize(self):
        pump = asyncio.create_task(self.pump())
        result = await self.request(
            "initialize",
            {
                "protocolVersion": 1,
                "clientInfo": {"name": "conductor-grok-acp", "version": "1"},
                "clientCapabilities": {
                    "fs": {"readTextFile": True, "writeTextFile": True},
                    "terminal": True,
                },
            },
            timeout=45.0,
        )
        await pump
        return result

    async def session_new(self, cwd: str, mcp_servers=None):
        pump = asyncio.create_task(self.pump())
        result = await self.request(
            "session/new",
            {
                "cwd": cwd,
                "mcpServers": mcp_servers or [],
                "_meta": {"yoloMode": True},
            },
            timeout=45.0,
        )
        await pump
        return result

    async def session_list(self, cwd: str | None = None):
        pump = asyncio.create_task(self.pump())
        params = {}
        if cwd:
            params["cwd"] = cwd
        result = await self.request("session/list", params, timeout=45.0)
        await pump
        return result

    async def session_load(self, session_id: str, cwd: str, mcp_servers=None):
        pump = asyncio.create_task(self.pump())
        result = await self.request(
            "session/load",
            {
                "sessionId": session_id,
                "cwd": cwd,
                "mcpServers": mcp_servers or [],
                "_meta": {"yoloMode": True},
            },
            timeout=45.0,
        )
        await pump
        return result

    async def session_prompt(self, session_id: str, text: str, timeout: float = 180.0):
        pump = asyncio.create_task(self.pump(collect_updates=True))
        req = asyncio.create_task(
            self.request(
                "session/prompt",
                {"sessionId": session_id, "prompt": [{"type": "text", "text": text}]},
                timeout=timeout,
            )
        )
        try:
            result, updates = await asyncio.gather(req, pump)
        except Exception:
            pump.cancel()
            raise
        chunks = []
        for msg in updates or []:
            upd = (msg.get("params") or {}).get("update") or {}
            if upd.get("sessionUpdate") == "agent_message_chunk":
                chunks.append(((upd.get("content") or {}).get("text")) or "")
        return result, "".join(chunks)


def _mcp_from_args(args) -> list:
    names = list(args.mcp_server or [])
    joined = getattr(args, "mcp_servers", None)
    if joined:
        names.extend(part.strip() for part in str(joined).split(",") if part.strip())
    try:
        return expand_names(names)
    except CatalogError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)


async def run(args):
    secret = load_secret()
    mcp_servers = _mcp_from_args(args) if args.cmd in {"new", "load"} else []
    url = f"ws://{HOST}:{PORT}{WS_PATH}?server-key={secret}"
    async with websockets.connect(url, additional_headers={"Authorization": f"Bearer {secret}"}, open_timeout=10) as ws:
        client = AcpClient(ws)
        init = await client.initialize()
        if args.cmd == "handshake":
            print(json.dumps({
                "ok": True,
                "listen": f"127.0.0.1:{PORT}",
                "path": WS_PATH,
                "protocolVersion": init.get("protocolVersion"),
                "agent": (init.get("agentInfo") or init.get("agent") or {}),
            }, indent=2))
            return
        cwd = args.cwd or os.getcwd()
        if args.cmd == "list":
            listed = await client.session_list(cwd if args.cwd else None)
            sessions = listed.get("sessions") or []
            slim = []
            for s in sessions:
                slim.append({
                    "sessionId": s.get("sessionId"),
                    "cwd": s.get("cwd"),
                    "title": s.get("title"),
                    "updatedAt": s.get("updatedAt"),
                })
            print(json.dumps({"ok": True, "count": len(slim), "sessions": slim}, indent=2))
            return
        if args.cmd == "new":
            sess = await client.session_new(cwd, mcp_servers)
            session_id = sess.get("sessionId")
            text = ""
            if args.prompt:
                _, text = await client.session_prompt(session_id, args.prompt)
            print(json.dumps({
                "sessionId": session_id,
                "cwd": cwd,
                "mcpCount": len(mcp_servers),
                "mcpNames": [s.get("name") for s in mcp_servers],
                "text": text,
            }, indent=2))
            return
        if args.cmd == "load":
            if not args.session_id:
                sys.exit("--session-id required")
            loaded = await client.session_load(args.session_id, cwd, mcp_servers)
            text = ""
            if args.prompt:
                _, text = await client.session_prompt(args.session_id, args.prompt)
            print(json.dumps({
                "ok": True,
                "sessionId": args.session_id,
                "cwd": cwd,
                "mcpCount": len(mcp_servers),
                "mcpNames": [s.get("name") for s in mcp_servers],
                "loaded": {k: loaded.get(k) for k in ("sessionId", "cwd") if k in loaded},
                "text": text,
            }, indent=2))
            return
        if args.cmd == "prompt":
            if not args.session_id:
                sys.exit("--session-id required")
            if not args.prompt:
                sys.exit("--prompt required")
            result, text = await client.session_prompt(args.session_id, args.prompt)
            print(json.dumps({"sessionId": args.session_id, "text": text, "result": result}, indent=2))
            return


def main():
    p = argparse.ArgumentParser(description="Conductor client for local grok-acp")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("handshake", help="initialize only — no session, no model turn")
    def _add_mcp_flags(p):
        p.add_argument(
            "--mcp-server",
            action="append",
            default=[],
            help="MCP server name from ~/.grok/config.toml (repeatable)",
        )
        p.add_argument(
            "--mcp-servers",
            default="",
            help="Comma-separated MCP server names from ~/.grok/config.toml",
        )

    n = sub.add_parser("new", help="session/new, optional first prompt")
    n.add_argument("--cwd", default="/Users/jay")
    n.add_argument("--prompt")
    _add_mcp_flags(n)
    ls = sub.add_parser("list", help="session/list — local chats on the shared leader")
    ls.add_argument("--cwd", default="")
    ld = sub.add_parser("load", help="session/load an existing local chat, optional prompt")
    ld.add_argument("--session-id", required=True)
    ld.add_argument("--cwd", default="/Users/jay")
    ld.add_argument("--prompt")
    _add_mcp_flags(ld)
    pr = sub.add_parser("prompt", help="session/prompt follow-up")
    pr.add_argument("--session-id", required=True)
    pr.add_argument("--prompt", required=True)
    pr.add_argument("--cwd", default="/Users/jay")
    args = p.parse_args()
    try:
        asyncio.get_event_loop().run_until_complete(run(args))
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
