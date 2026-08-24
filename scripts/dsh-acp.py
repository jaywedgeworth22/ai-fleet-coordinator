#!/usr/bin/env python3
"""ACP stdio bridge for DeepSeek Harness (Shellular spawn).

Stdout is JSON-RPC only.  Drives `dsh --profile headless`.  Auth comes from
the process env or ~/.dsh/.credentials.yaml — never from agents.json.

Phone clients cannot answer Harness interactive approval prompts.  Default
DSH_PERMISSION_MODE is danger-full-access (approval: never), matching
agy-acp-turbo's auto-approve posture for Shellular.

Tracked copy: ai-fleet-coordinator/scripts/dsh-acp.py
Live install: ~/apps/dsh-runtime/dsh-acp.py
"""

from __future__ import annotations

import datetime
import json
import os
import subprocess
import sys
import threading
import time
import uuid
from pathlib import Path
from typing import Any

_RUNTIME_ROOT = Path(
    os.environ.get("DSH_RUNTIME_ROOT", "/Users/jay/apps/dsh-runtime"),
)
DSH_BIN = os.environ.get("DSH_BIN", str(_RUNTIME_ROOT / "node_modules/.bin/dsh"))
DSH_HOME = os.environ.get("DSH_HOME", os.path.expanduser("~/.dsh"))
DEFAULT_TIMEOUT_SEC = int(os.environ.get("DSH_ACP_TIMEOUT_SEC", "300"))
DEFAULT_PERMISSION_MODE = os.environ.get("DSH_PERMISSION_MODE", "danger-full-access")

JsonDict = dict[str, Any]


def _load_key_from_dsh_credentials() -> None:
    if os.environ.get("DEEPSEEK_API_KEY"):
        return
    cred = Path.home() / ".dsh" / ".credentials.yaml"
    if not cred.is_file():
        return
    try:
        text = cred.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key_name = ""
        val = ""
        if ":" in line:
            key_name, val = line.split(":", 1)
        elif "=" in line:
            key_name, val = line.split("=", 1)
        else:
            continue
        name = key_name.strip().lower().replace("-", "_")
        if name in {"api_key", "apikey", "deepseek_api_key", "token"}:
            val = val.strip().strip("'").strip('"')
            if val:
                os.environ["DEEPSEEK_API_KEY"] = val
                return


_load_key_from_dsh_credentials()

out_lock = threading.Lock()
sessions: dict[str, JsonDict] = {}
active_procs: dict[str, subprocess.Popen[str]] = {}
active_lock = threading.Lock()


def write(payload: JsonDict) -> None:
    raw = json.dumps(payload, ensure_ascii=True, separators=(",", ":")) + "\n"
    with out_lock:
        sys.stdout.write(raw)
        sys.stdout.flush()


def reply(req_id: Any, result: JsonDict) -> None:
    write({"jsonrpc": "2.0", "id": req_id, "result": result})


def fail(req_id: Any, message: str, code: int = -32000) -> None:
    write(
        {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": code, "message": message},
        }
    )


def notify(method: str, params: JsonDict) -> None:
    write({"jsonrpc": "2.0", "method": method, "params": params})


def emit_text(session_id: str, text: str) -> None:
    if not text:
        return
    notify(
        "session/update",
        {
            "sessionId": session_id,
            "update": {
                "sessionUpdate": "agent_message_chunk",
                "content": {"type": "text", "text": text},
            },
        },
    )


def extract_prompt_text(prompt: Any) -> str:
    parts: list[str] = []
    if isinstance(prompt, str):
        return prompt.strip()
    if not isinstance(prompt, list):
        return ""
    for item in prompt:
        if isinstance(item, str):
            parts.append(item)
        elif isinstance(item, dict) and item.get("type") == "text":
            parts.append(str(item.get("text") or ""))
    return "\n".join(parts).strip()


def modes_block() -> JsonDict:
    return {
        "currentModeId": "agent",
        "availableModes": [
            {"id": "agent", "name": "Agent"},
            {"id": "plan", "name": "Plan"},
            {"id": "ask", "name": "Ask"},
        ],
    }


def _drain_stderr(proc: subprocess.Popen[str], session_id: str) -> None:
    stderr = proc.stderr
    if stderr is None:
        return
    try:
        for line in stderr:
            stripped = line.strip()
            if stripped:
                emit_text(session_id, f"[stderr] {stripped}\n")
    except (OSError, ValueError):
        pass


def _clear_active(session_id: str, proc: subprocess.Popen[str]) -> None:
    with active_lock:
        current = active_procs.get(session_id)
        if current is proc:
            active_procs.pop(session_id, None)


def cancel_session(session_id: str) -> bool:
    with active_lock:
        proc = active_procs.get(session_id)
    if proc is None:
        return False
    try:
        proc.kill()
    except OSError:
        return False
    return True


def handle_prompt(req_id: Any, session_id: str, prompt_text: str, cwd: str) -> None:
    env = os.environ.copy()
    env["DSH_HOME"] = DSH_HOME
    env.setdefault("DSH_PERMISSION_MODE", DEFAULT_PERMISSION_MODE)
    cmd = [DSH_BIN, "--profile", "headless", prompt_text]
    workdir = cwd if os.path.isdir(cwd) else None
    proc: subprocess.Popen[str] | None = None
    try:
        proc = subprocess.Popen(
            cmd,
            cwd=workdir,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
        with active_lock:
            active_procs[session_id] = proc
        stderr_thread = threading.Thread(
            target=_drain_stderr,
            args=(proc, session_id),
            daemon=True,
        )
        stderr_thread.start()
        assert proc.stdout is not None
        deadline = time.monotonic() + DEFAULT_TIMEOUT_SEC
        for line in proc.stdout:
            emit_text(session_id, line)
            if time.monotonic() > deadline:
                emit_text(
                    session_id,
                    f"\n[dsh-acp] Timed out after {DEFAULT_TIMEOUT_SEC}s.\n",
                )
                proc.kill()
                break
        try:
            proc.wait(timeout=max(0, deadline - time.monotonic()))
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=5)
        stderr_thread.join(timeout=2)
        if proc.returncode not in (0, None, -9, -15):
            err_tail = ""
            if proc.stderr is not None:
                try:
                    err_tail = proc.stderr.read().strip()
                except (OSError, ValueError):
                    pass
            emit_text(
                session_id,
                err_tail or f"dsh exited with code {proc.returncode}",
            )
        reply(req_id, {"stopReason": "endTurn"})
    except Exception as exc:
        emit_text(session_id, f"Execution error: {exc}\n")
        reply(req_id, {"stopReason": "endTurn"})
    finally:
        if proc is not None:
            _clear_active(session_id, proc)


def list_dsh_sessions() -> list[JsonDict]:
    sess_root = Path(DSH_HOME) / "sessions"
    if not sess_root.is_dir():
        return []
    items: list[JsonDict] = []
    try:
        for dir_entry in sess_root.iterdir():
            if not dir_entry.is_dir() or dir_entry.name == "acp":
                continue
            raw_path = dir_entry.name.strip("-").replace("-", "/")
            cwd = "/" + raw_path if raw_path else str(Path.home())
            for sess_dir in dir_entry.iterdir():
                if not sess_dir.is_dir():
                    continue
                sess_id = sess_dir.name
                try:
                    mtime = sess_dir.stat().st_mtime
                    dt = datetime.datetime.fromtimestamp(
                        mtime,
                        tz=datetime.timezone.utc,
                    ).isoformat()
                except OSError:
                    dt = None
                repo_name = Path(cwd).name if Path(cwd).name else "DeepSeek"
                display_title = f"{repo_name}: {sess_id.replace('session-', '')[:8]}"
                items.append(
                    {
                        "sessionId": sess_id,
                        "cwd": cwd,
                        "title": display_title,
                        "updatedAt": dt,
                    }
                )
    except Exception:
        pass
    items.sort(key=lambda x: x.get("updatedAt") or "", reverse=True)
    return items[:50]


def main() -> None:
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue
        method = req.get("method")
        req_id = req.get("id")
        params = req.get("params") if isinstance(req.get("params"), dict) else {}

        if method == "initialize":
            version = params.get("protocolVersion", 1)
            reply(
                req_id,
                {
                    "protocolVersion": version,
                    "agentCapabilities": {
                        "loadSession": True,
                        "promptCapabilities": {
                            "image": False,
                            "audio": False,
                            "embeddedContext": True,
                        },
                        "sessionCapabilities": {
                            "list": {},
                        },
                    },
                    "agentInfo": {
                        "name": "deepseek-harness-acp",
                        "version": "1.2.0",
                    },
                    "authMethods": [],
                },
            )
        elif method == "authenticate":
            reply(req_id, {})
        elif method == "session/list":
            reply(req_id, {"sessions": list_dsh_sessions()})
        elif method == "session/new":
            sess_id = str(uuid.uuid4())
            cwd = params.get("cwd") if isinstance(params.get("cwd"), str) else os.getcwd()
            sessions[sess_id] = {"cwd": cwd}
            reply(req_id, {"sessionId": sess_id, "modes": modes_block()})
        elif method == "session/load":
            sess_id = str(params.get("sessionId") or uuid.uuid4())
            cwd = params.get("cwd") if isinstance(params.get("cwd"), str) else os.getcwd()
            sessions[sess_id] = {"cwd": cwd}
            reply(req_id, {"sessionId": sess_id, "modes": modes_block()})
        elif method == "session/prompt":
            sess_id = str(params.get("sessionId") or "")
            text = extract_prompt_text(params.get("prompt"))
            if not text:
                fail(req_id, "empty prompt")
                continue
            record = sessions.setdefault(sess_id, {"cwd": os.getcwd()})
            cwd = str(record.get("cwd") or os.getcwd())
            thread = threading.Thread(
                target=handle_prompt,
                args=(req_id, sess_id, text, cwd),
                daemon=True,
            )
            thread.start()
        elif method == "session/cancel":
            sess_id = str(params.get("sessionId") or "")
            cancelled = cancel_session(sess_id)
            if req_id is not None:
                reply(req_id, {"cancelled": cancelled})
        elif method == "ping":
            reply(req_id, {})
        elif req_id is not None:
            reply(req_id, {})


if __name__ == "__main__":
    main()
