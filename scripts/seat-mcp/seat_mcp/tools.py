"""MCP tools:  seat_launch, seat_status, seat_reply, seat_result.

Async jobs only.  seat_launch returns a jobId immediately.
"""

from __future__ import annotations

from typing import Any

from . import grok_tui, jobs
from .config import DEFAULT_CWD, IMPLEMENTED_SEATS, TEST_SEATS, WEDGE_SEC
from .runner import launch_async
from .seats import SeatError, stuff_prior, validate_cwd, validate_tui_cwd

JsonDict = dict[str, Any]


def _opts(raw: Any) -> JsonDict:
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise SeatError("opts must be an object")
    # Never accept a permission / sandbox mode.  v1 DeepSeek is read-only.
    forbidden = {"mode", "permissionMode", "permission_mode", "sandbox", "dshPermissionMode"}
    hit = [k for k in raw if k in forbidden]
    if hit:
        raise SeatError("mode is not a parameter.  DeepSeek v1 is always read-only.")
    return dict(raw)


def seat_launch(arguments: JsonDict) -> JsonDict:
    seat = str(arguments.get("seat") or "").strip()
    prompt = arguments.get("prompt")
    if not seat:
        raise SeatError("seat is required")
    if not isinstance(prompt, str) or not prompt.strip():
        raise SeatError("prompt is required")
    opts = _opts(arguments.get("opts"))
    if seat == "grok-tui":
        cwd = _tui_cwd(arguments.get("cwd"), opts.get("sessionId") or opts.get("session_id"))
    else:
        cwd = validate_cwd(arguments.get("cwd"))

    if seat == "deepseek" and (opts.get("sessionId") or opts.get("session_id")):
        raise SeatError(
            "DSH headless cannot resume a session.  "
            "Official path is one submitted task.  "
            "Pass opts.priorJobId to stuff prior text into a new one-shot, "
            "or omit sessionId."
        )
    if seat == "grok-tui" and not (opts.get("sessionId") or opts.get("session_id")):
        raise SeatError(
            "grok-tui requires opts.sessionId.  Call grok_sessions_list first."
        )

    prior_id = opts.get("priorJobId") or opts.get("prior_job_id")
    launch_prompt = prompt.strip()
    session_carry = opts.get("sessionId") or opts.get("session_id")
    if prior_id:
        prior = jobs.load_job(str(prior_id))
        if seat == "deepseek" or not session_carry:
            launch_prompt = stuff_prior(
                str(prior.get("prompt") or ""),
                str(prior.get("text") or ""),
                prompt.strip(),
            )
        if seat == "grok" and not session_carry and prior.get("sessionId"):
            opts = dict(opts)
            opts["sessionId"] = prior.get("sessionId")

    rec = jobs.new_record(
        seat=seat,
        prompt=launch_prompt,
        cwd=cwd,
        opts=opts,
        prior_job_id=str(prior_id) if prior_id else None,
    )
    launch_async(rec["jobId"])
    return {"jobId": rec["jobId"]}


def seat_status(arguments: JsonDict) -> JsonDict:
    job_id = str(arguments.get("jobId") or arguments.get("job_id") or "").strip()
    if not job_id:
        raise SeatError("jobId is required")
    rec = jobs.load_job(job_id)
    return jobs.status_view(rec, WEDGE_SEC)


def seat_reply(arguments: JsonDict) -> JsonDict:
    """Read current text, or launch a follow-up when `prompt` is set.

    Follow-up is async:  returns a new jobId.  DeepSeek follow-up is a new
    one-shot with prior text stuffed.  Grok follow-up uses session/prompt.
    """
    job_id = str(arguments.get("jobId") or arguments.get("job_id") or "").strip()
    if not job_id:
        raise SeatError("jobId is required")
    rec = jobs.load_job(job_id)
    follow = arguments.get("prompt")
    if follow is None or (isinstance(follow, str) and not follow.strip()):
        return {
            "jobId": rec.get("jobId"),
            "state": rec.get("state"),
            "text": rec.get("text") or "",
        }
    if not isinstance(follow, str):
        raise SeatError("prompt must be a string")
    seat = str(rec.get("seat") or "")
    opts: JsonDict = {}
    if seat in {"grok", "grok-tui"} and rec.get("sessionId"):
        opts["sessionId"] = rec.get("sessionId")
    elif seat == "deepseek":
        opts["priorJobId"] = job_id
    else:
        opts["priorJobId"] = job_id
    timeout = (rec.get("opts") or {}).get("timeoutSec")
    if timeout:
        opts["timeoutSec"] = timeout
    effort = (rec.get("opts") or {}).get("effort")
    if effort:
        opts["effort"] = effort
    return seat_launch(
        {
            "seat": seat,
            "prompt": follow,
            "cwd": rec.get("cwd"),
            "opts": opts,
        }
    )


def _tui_cwd(cwd, session_id) -> str:
    if cwd:
        return validate_tui_cwd(cwd)
    sid = str(session_id or "").strip()
    if sid:
        for row in grok_tui.load_active():
            if row.get("sessionId") == sid and row.get("cwd"):
                return validate_tui_cwd(str(row["cwd"]))
    return validate_tui_cwd(str(DEFAULT_CWD))


def grok_sessions_list(arguments: JsonDict) -> JsonDict:
    cwd = arguments.get("cwd")
    cwd_s = str(cwd).strip() if isinstance(cwd, str) and cwd.strip() else None
    return grok_tui.list_sessions(cwd_s)


def grok_session_peek(arguments: JsonDict) -> JsonDict:
    session_id = str(arguments.get("sessionId") or arguments.get("session_id") or "").strip()
    if not session_id:
        raise SeatError("sessionId is required")
    cwd_s = _tui_cwd(arguments.get("cwd"), session_id)
    return grok_tui.peek_session(session_id, cwd_s)


def grok_session_prompt(arguments: JsonDict) -> JsonDict:
    """Async follow-up into a live TUI session.  Returns jobId immediately."""
    session_id = str(arguments.get("sessionId") or arguments.get("session_id") or "").strip()
    prompt = arguments.get("prompt")
    if not session_id:
        raise SeatError("sessionId is required")
    if not isinstance(prompt, str) or not prompt.strip():
        raise SeatError("prompt is required")
    cwd = arguments.get("cwd")
    opts = _opts(arguments.get("opts"))
    opts["sessionId"] = session_id
    return seat_launch(
        {
            "seat": "grok-tui",
            "prompt": prompt.strip(),
            "cwd": cwd,
            "opts": opts,
        }
    )


def seat_result(arguments: JsonDict) -> JsonDict:
    job_id = str(arguments.get("jobId") or arguments.get("job_id") or "").strip()
    if not job_id:
        raise SeatError("jobId is required")
    rec = jobs.load_job(job_id)
    return jobs.result_view(rec)


TOOL_IMPL = {
    "seat_launch": seat_launch,
    "seat_status": seat_status,
    "seat_reply": seat_reply,
    "seat_result": seat_result,
    "grok_sessions_list": grok_sessions_list,
    "grok_session_peek": grok_session_peek,
    "grok_session_prompt": grok_session_prompt,
}


def tool_schemas() -> list[JsonDict]:
    seat_desc = (
        "Seat to run.  deepseek (dsh --profile headless, read-only), "
        "grok (new session on grok-acp 127.0.0.1:12419), "
        "or grok-tui (inject into a live Mac Grok TUI via the shared leader; "
        "requires opts.sessionId).  Test adapters:  _echo, _sleep."
    )
    return [
        {
            "name": "seat_launch",
            "description": (
                "Start an async seat job.  Returns jobId immediately.  "
                "Poll seat_status, then seat_reply / seat_result.  "
                "DeepSeek is always DSH_PERMISSION_MODE=read-only.  "
                "There is no mode parameter."
            ),
            "inputSchema": {
                "type": "object",
                "properties": {
                    "seat": {
                        "type": "string",
                        "description": seat_desc,
                    },
                    "prompt": {"type": "string", "description": "Task text."},
                    "cwd": {
                        "type": "string",
                        "description": "Must exist under /Users/jay/Code or /Users/jay/apps.",
                    },
                    "opts": {
                        "type": "object",
                        "description": (
                            "Optional.  effort:  quick|deep (deepseek temp --patch only).  "
                            "timeoutSec.  sessionId (grok follow-up or grok-tui attach).  "
                            "priorJobId (stuff prior text; required for deepseek follow-up)."
                        ),
                        "properties": {
                            "effort": {"type": "string", "enum": ["quick", "deep"]},
                            "timeoutSec": {"type": "integer", "minimum": 1, "maximum": 900},
                            "sessionId": {"type": "string"},
                            "priorJobId": {"type": "string"},
                        },
                    },
                },
                "required": ["seat", "prompt"],
            },
        },
        {
            "name": "seat_status",
            "description": "Job state, elapsedMs, heartbeat (working vs wedged), partialTail.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "jobId": {"type": "string"},
                },
                "required": ["jobId"],
            },
        },
        {
            "name": "seat_reply",
            "description": (
                "Without prompt:  current assistant text.  "
                "With prompt:  async follow-up, returns new jobId.  "
                "DeepSeek follow-up is a new one-shot with prior text stuffed "
                "(headless cannot resume)."
            ),
            "inputSchema": {
                "type": "object",
                "properties": {
                    "jobId": {"type": "string"},
                    "prompt": {"type": "string", "description": "Optional follow-up.  Starts a new job."},
                },
                "required": ["jobId"],
            },
        },
        {
            "name": "seat_result",
            "description": "Snapshot:  text, exitCode, sessionId, stats, artifacts.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "jobId": {"type": "string"},
                },
                "required": ["jobId"],
            },
        },
        {
            "name": "grok_sessions_list",
            "description": (
                "List Mac Grok TUI chats on the shared leader.  "
                "live=true means ~/.grok/active_sessions.json currently has that id.  "
                "Use grok_session_prompt to inject a follow-up.  "
                "Do not start a second grok-acp."
            ),
            "inputSchema": {
                "type": "object",
                "properties": {
                    "cwd": {
                        "type": "string",
                        "description": "Optional filter cwd for session/list.",
                    },
                },
            },
        },
        {
            "name": "grok_session_peek",
            "description": (
                "session/load a live TUI chat and return any streamed text.  "
                "Does not send a prompt."
            ),
            "inputSchema": {
                "type": "object",
                "properties": {
                    "sessionId": {"type": "string"},
                    "cwd": {"type": "string"},
                },
                "required": ["sessionId"],
            },
        },
        {
            "name": "grok_session_prompt",
            "description": (
                "Inject a prompt into a live Grok TUI session via the shared "
                "leader.  Returns jobId immediately.  Poll seat_status then "
                "seat_result.  Prefer a session with live=true from "
                "grok_sessions_list.  Does not create a new grok-acp session."
            ),
            "inputSchema": {
                "type": "object",
                "properties": {
                    "sessionId": {"type": "string"},
                    "prompt": {"type": "string"},
                    "cwd": {"type": "string"},
                    "opts": {
                        "type": "object",
                        "properties": {
                            "timeoutSec": {"type": "integer", "minimum": 1, "maximum": 900},
                        },
                    },
                },
                "required": ["sessionId", "prompt"],
            },
        },
    ]


# Keep the tuples imported so a future list tool can mention them.
_ = (IMPLEMENTED_SEATS, TEST_SEATS)
