"""Run a seat job in a new process group with heartbeat and timeout.

Kill the process GROUP on timeout, not just the parent pid.
"""

from __future__ import annotations

import os
import select
import subprocess
import threading
import time
from datetime import datetime, timezone
from typing import Any

from .config import HEARTBEAT_SEC, KILL_GRACE_SEC
from . import jobs
from .seats import SeatError, parse_output, plan_spawn

JsonDict = dict[str, Any]


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def launch_async(job_id: str) -> None:
    thread = threading.Thread(target=run_job, args=(job_id,), name="seat-job-%s" % job_id[:8], daemon=True)
    thread.start()


def run_job(job_id: str) -> None:
    rec = jobs.load_job(job_id)
    jobs.update_job(job_id, state="running", startedAt=_now_iso(), heartbeatAt=_now_iso())
    try:
        plan = plan_spawn(rec)
    except SeatError as exc:
        jobs.update_job(
            job_id,
            state="failed",
            error=str(exc),
            finishedAt=_now_iso(),
            heartbeatAt=_now_iso(),
        )
        return
    except Exception as exc:
        jobs.update_job(
            job_id,
            state="failed",
            error="spawn plan failed:  %s" % exc,
            finishedAt=_now_iso(),
            heartbeatAt=_now_iso(),
        )
        return

    argv = list(plan["argv"])
    env = plan["env"]
    timeout_sec = float(plan["timeoutSec"])
    parse = str(plan.get("parse") or "plain")
    merge_stderr = bool(plan.get("merge_stderr", True))
    cwd = rec.get("cwd") or None

    stdout_dest = subprocess.PIPE
    stderr_dest = subprocess.STDOUT if merge_stderr else subprocess.PIPE

    try:
        proc = subprocess.Popen(
            argv,
            cwd=cwd,
            env=env,
            stdout=stdout_dest,
            stderr=stderr_dest,
            start_new_session=True,
        )
    except Exception as exc:
        jobs.update_job(
            job_id,
            state="failed",
            error="spawn failed:  %s" % exc,
            finishedAt=_now_iso(),
            heartbeatAt=_now_iso(),
        )
        return

    pgid = proc.pid
    jobs.update_job(
        job_id,
        state="running",
        pid=proc.pid,
        pgid=pgid,
        startedAt=_now_iso(),
        heartbeatAt=_now_iso(),
    )

    stop_hb = threading.Event()

    def _heartbeat() -> None:
        while not stop_hb.wait(HEARTBEAT_SEC):
            try:
                cur = jobs.load_job(job_id)
                stats = dict(cur.get("stats") or {})
                stats["elapsedMs"] = jobs.elapsed_ms(cur)
                jobs.update_job(job_id, heartbeatAt=_now_iso(), stats=stats)
            except Exception:
                pass

    hb_thread = threading.Thread(target=_heartbeat, name="seat-hb-%s" % job_id[:8], daemon=True)
    hb_thread.start()

    buf = bytearray()
    err_buf = bytearray()
    timed_out = False
    deadline = time.time() + timeout_sec
    stdout_fd = proc.stdout.fileno() if proc.stdout is not None else None
    stderr_fd = proc.stderr.fileno() if proc.stderr is not None else None

    try:
        while True:
            remaining = deadline - time.time()
            if remaining <= 0:
                timed_out = True
                jobs.kill_process_group(pgid, grace_sec=KILL_GRACE_SEC)
                break
            watch = []
            if stdout_fd is not None:
                watch.append(stdout_fd)
            if stderr_fd is not None:
                watch.append(stderr_fd)
            if not watch:
                if proc.poll() is not None:
                    break
                time.sleep(min(0.2, remaining))
                continue
            ready, _, _ = select.select(watch, [], [], min(0.5, remaining))
            for fd in ready:
                try:
                    chunk = os.read(fd, 4096)
                except OSError:
                    chunk = b""
                if not chunk:
                    if fd == stdout_fd:
                        stdout_fd = None
                    if fd == stderr_fd:
                        stderr_fd = None
                    continue
                if fd == stderr_fd and not merge_stderr:
                    err_buf.extend(chunk)
                    # Keep stderr in the ring tail only.
                    tail_src = buf + b"\n[stderr]\n" + err_buf
                else:
                    buf.extend(chunk)
                    tail_src = bytes(buf)
                    if err_buf:
                        tail_src = tail_src + b"\n[stderr]\n" + bytes(err_buf)
                stats = {"elapsedMs": jobs.elapsed_ms(jobs.load_job(job_id)), "bytesOut": len(buf)}
                jobs.update_job(
                    job_id,
                    partialTail=jobs.ring_tail(tail_src),
                    heartbeatAt=_now_iso(),
                    stats=stats,
                )
            if proc.poll() is not None and stdout_fd is None and stderr_fd is None:
                break
            if proc.poll() is not None and not ready:
                # Drain whatever is left, then exit the loop.
                continue
        try:
            proc.wait(timeout=2)
        except Exception:
            jobs.kill_process_group(pgid, grace_sec=KILL_GRACE_SEC)
            try:
                proc.wait(timeout=2)
            except Exception:
                pass
    finally:
        stop_hb.set()

    stdout_text = buf.decode("utf-8", errors="replace")
    session_hint = None
    opts = rec.get("opts") if isinstance(rec.get("opts"), dict) else {}
    if opts.get("sessionId") or opts.get("session_id"):
        session_hint = str(opts.get("sessionId") or opts.get("session_id"))
    text, session_id = parse_output(parse, stdout_text, session_hint)
    exit_code = proc.returncode
    finished = _now_iso()
    stats = {"elapsedMs": jobs.elapsed_ms({**jobs.load_job(job_id), "finishedAt": finished}), "bytesOut": len(buf)}
    tail_src = bytes(buf)
    if err_buf:
        tail_src = tail_src + b"\n[stderr]\n" + bytes(err_buf)

    if timed_out:
        jobs.update_job(
            job_id,
            state="timeout",
            text=text,
            sessionId=session_id,
            exitCode=exit_code if exit_code is not None else -9,
            finishedAt=finished,
            heartbeatAt=finished,
            partialTail=jobs.ring_tail(tail_src),
            stats=stats,
            error="timed out after %ss; process group killed" % int(timeout_sec),
            pid=None,
            pgid=None,
        )
        _cleanup_patch(job_id)
        return

    state = "succeeded" if exit_code == 0 else "failed"
    error = None
    if state == "failed":
        err_txt = err_buf.decode("utf-8", errors="replace").strip()
        error = err_txt or ("exit %s" % exit_code)
    jobs.update_job(
        job_id,
        state=state,
        text=text,
        sessionId=session_id,
        exitCode=exit_code,
        finishedAt=finished,
        heartbeatAt=finished,
        partialTail=jobs.ring_tail(tail_src),
        stats=stats,
        error=error,
        pid=None,
        pgid=None,
    )
    _cleanup_patch(job_id)


def _cleanup_patch(job_id: str) -> None:
    from .config import JOBS_DIR

    path = JOBS_DIR / ("%s.patch.yml" % job_id)
    try:
        if path.is_file():
            path.unlink()
    except OSError:
        pass
