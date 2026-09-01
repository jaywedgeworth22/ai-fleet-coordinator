#!/usr/bin/env python3
"""Sample Mac disk / RAM / CPU and optionally clean + wake BotFleet Housekeeper.

Launchd: com.jay.mac-resource-watch (every 5 min).
On-demand: python3 ~/apps/mac-resource-watch.py --once
Never prints webhook secrets.  Load BOTFLEET_HOUSEKEEPER_WEBHOOK_* from
~/.secrets/botfleet-housekeeper-webhook.env without echoing values.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HOME = Path.home()
STATE_DIR = HOME / ".claude-disk-janitor"
STATE_FILE = STATE_DIR / "resource-watch-state.json"
LOG_FILE = HOME / "Library" / "Logs" / "mac-resource-watch.log"
SECRET_FILE = HOME / ".secrets" / "botfleet-housekeeper-webhook.env"
CLEANUP = HOME / "apps" / "mac-auto-cleanup.sh"
JANITOR = HOME / ".claude-disk-janitor" / "janitor.sh"

# Defaults: start reclaiming before the old 50G janitor cliff.  Overnight
# 6-13G drops in 30 min were blowing through that floor.
DISK_FREE_WARN_GB = float(os.environ.get("RESOURCE_DISK_WARN_GB", "80"))
DISK_FREE_CRIT_GB = float(os.environ.get("RESOURCE_DISK_CRIT_GB", "50"))
DISK_DROP_ALERT_GB = float(os.environ.get("RESOURCE_DISK_DROP_GB", "6"))
SWAP_USED_PCT = float(os.environ.get("RESOURCE_SWAP_USED_PCT", "80"))
SWAP_TOTAL_GB = float(os.environ.get("RESOURCE_SWAP_TOTAL_GB", "8"))
LOAD1_THRESHOLD = float(os.environ.get("RESOURCE_LOAD1", "16"))
CPU_ENABLED = os.environ.get("RESOURCE_CPU", "1") not in {"0", "false", "no"}
COOLDOWN_SEC = int(os.environ.get("RESOURCE_COOLDOWN_SEC", "2700"))


def log(msg: str) -> None:
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')}  {msg}"
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")
    try:
        raw = LOG_FILE.read_text(encoding="utf-8").splitlines()
        if len(raw) > 800:
            LOG_FILE.write_text("\n".join(raw[-800:]) + "\n", encoding="utf-8")
    except OSError:
        pass


def _run(cmd: list[str], timeout: int = 20) -> str:
    try:
        return subprocess.check_output(cmd, text=True, timeout=timeout, stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return ""


def sample() -> dict:
    df = _run(["/bin/df", "-k", "/System/Volumes/Data"]) or _run(["/bin/df", "-k", "/"])
    disk_free_gb = disk_used_pct = 0.0
    for line in df.splitlines()[1:]:
        parts = line.split()
        if len(parts) >= 5:
            avail_k = float(parts[3])
            cap = parts[4].rstrip("%")
            disk_free_gb = avail_k / 1024 / 1024
            try:
                disk_used_pct = float(cap)
            except ValueError:
                disk_used_pct = 0.0
            break

    vm = _run(["/usr/sbin/sysctl", "-n", "vm.swapusage"])
    swap_total_gb = swap_used_gb = 0.0
    m = re.search(r"total\s*=\s*([\d.]+)M.*?used\s*=\s*([\d.]+)M", vm)
    if m:
        swap_total_gb = float(m.group(1)) / 1024
        swap_used_gb = float(m.group(2)) / 1024
    swap_used_pct = (swap_used_gb / swap_total_gb * 100) if swap_total_gb else 0.0

    up = _run(["/usr/bin/uptime"])
    load1 = load5 = load15 = 0.0
    lm = re.search(r"load averages?:\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)", up)
    if lm:
        load1, load5, load15 = (float(lm.group(i)) for i in (1, 2, 3))

    return {
        "at": int(time.time()),
        "disk_free_gb": round(disk_free_gb, 2),
        "disk_used_pct": round(disk_used_pct, 1),
        "swap_total_gb": round(swap_total_gb, 2),
        "swap_used_gb": round(swap_used_gb, 2),
        "swap_used_pct": round(swap_used_pct, 1),
        "load1": round(load1, 2),
        "load5": round(load5, 2),
        "load15": round(load15, 2),
    }


def evaluate(s: dict, prev_free: float | None) -> list[dict]:
    hits: list[dict] = []
    free = s["disk_free_gb"]
    if free <= DISK_FREE_CRIT_GB:
        hits.append({"metric": "disk_free_gb", "severity": "critical", "threshold": DISK_FREE_CRIT_GB, "cmp": "below", "value": free})
    elif free <= DISK_FREE_WARN_GB:
        hits.append({"metric": "disk_free_gb", "severity": "warn", "threshold": DISK_FREE_WARN_GB, "cmp": "below", "value": free})
    if prev_free is not None:
        drop = prev_free - free
        if drop >= DISK_DROP_ALERT_GB:
            hits.append({"metric": "disk_drop_gb", "severity": "warn", "threshold": DISK_DROP_ALERT_GB, "cmp": "above", "value": round(drop, 2)})
    if s["swap_used_pct"] >= SWAP_USED_PCT or s["swap_total_gb"] >= SWAP_TOTAL_GB:
        hits.append({
            "metric": "swap",
            "severity": "critical" if s["swap_used_pct"] >= 90 else "warn",
            "threshold": SWAP_USED_PCT,
            "cmp": "above",
            "value": s["swap_used_pct"],
            "swap_total_gb": s["swap_total_gb"],
        })
    if CPU_ENABLED and s["load1"] >= LOAD1_THRESHOLD:
        hits.append({"metric": "load_1m", "severity": "warn", "threshold": LOAD1_THRESHOLD, "cmp": "above", "value": s["load1"]})
    return hits


def load_state() -> dict:
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    tmp.replace(STATE_FILE)


def load_webhook_env() -> tuple[str, str]:
    """Return (url, secret).  Never print either."""
    url = os.environ.get("BOTFLEET_HOUSEKEEPER_WEBHOOK_URL", "").strip()
    secret = os.environ.get("BOTFLEET_HOUSEKEEPER_WEBHOOK_SECRET", "").strip()
    if SECRET_FILE.is_file():
        for line in SECRET_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("BOTFLEET_HOUSEKEEPER_WEBHOOK_URL=") and not url:
                url = line.split("=", 1)[1].strip().strip('"')
            elif line.startswith("BOTFLEET_HOUSEKEEPER_WEBHOOK_SECRET=") and not secret:
                secret = line.split("=", 1)[1].strip().strip('"')
    return url, secret


def run_cleanup(pressure: bool) -> int:
    env = os.environ.copy()
    env["PATH"] = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:" + env.get("PATH", "")
    args = ["/bin/bash", str(CLEANUP)]
    if pressure:
        args.append("--pressure")
        env["MAC_CLEANUP_PRESSURE"] = "1"
    rc = 0
    if CLEANUP.is_file():
        try:
            rc = subprocess.call(args, env=env, timeout=900)
        except (subprocess.TimeoutExpired, OSError) as exc:
            log(f"cleanup timeout/error: {exc}")
            rc = 1
    if pressure and JANITOR.is_file():
        try:
            subprocess.call(["/bin/bash", str(JANITOR)], env=env, timeout=900)
        except (subprocess.TimeoutExpired, OSError) as exc:
            log(f"janitor timeout/error: {exc}")
    if pressure:
        cmm = _run(["/usr/bin/which", "cleanmymac"]).strip() or "/opt/homebrew/bin/cleanmymac"
        if Path(cmm).is_file():
            subprocess.call([cmm, "clean", "--force"], timeout=600)
            subprocess.call([cmm, "optimize", "ram"], timeout=120)
    return rc


def fire_webhook(hits: list[dict], sample_data: dict, cleaned: bool) -> bool:
    url, secret = load_webhook_env()
    if not url or not secret:
        log("webhook skipped: missing BOTFLEET_HOUSEKEEPER_WEBHOOK_* (len url=%s secret=%s)" % (
            len(url), len(secret)))
        return False
    event = hits[0]["metric"]
    if event.startswith("disk"):
        event_name = "resource.disk"
    elif event.startswith("swap"):
        event_name = "resource.ram"
    elif event.startswith("load"):
        event_name = "resource.cpu"
    else:
        event_name = "resource.pressure"
    payload = {
        "event": event_name,
        "task": (
            "Host resource pressure.  Run the Housekeeper cleanup playbook now.  "
            "Do not only report.  Regenerable caches and CleanMyMac are in scope."
        ),
        "hits": hits,
        "sample": sample_data,
        "cleanup_already_ran": cleaned,
        "playbook": [
            "bash /Users/jay/apps/mac-auto-cleanup.sh --pressure",
            "bash /Users/jay/.claude-disk-janitor/janitor.sh",
            "cleanmymac clean --force && cleanmymac optimize ram",
        ],
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {secret}",
            "X-BotFleet-Event": event_name,
            "Idempotency-Key": f"resource-{sample_data['at']}-{event_name}",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=8, context=ssl.create_default_context()) as resp:
            log(f"webhook {event_name} http={resp.status} hits={[h['metric'] for h in hits]}")
            return 200 <= resp.status < 300
    except urllib.error.HTTPError as exc:
        log(f"webhook http={exc.code} (secret_len={len(secret)})")
        return False
    except Exception as exc:
        log(f"webhook error: {type(exc).__name__}")
        return False


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--once", action="store_true")
    p.add_argument("--clean", action="store_true", help="run cleanup even without a hit")
    p.add_argument("--no-webhook", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    s = sample()
    state = load_state()
    prev_free = state.get("disk_free_gb")
    hits = evaluate(s, prev_free)
    log(
        f"free={s['disk_free_gb']}G used={s['disk_used_pct']}% "
        f"swap={s['swap_used_gb']}/{s['swap_total_gb']}G ({s['swap_used_pct']}%) "
        f"load={s['load1']}/{s['load5']}/{s['load15']} hits={[h['metric'] for h in hits] or 'none'}"
    )

    pressure = any(h.get("severity") == "critical" for h in hits) or any(
        h["metric"] in {"disk_free_gb", "disk_drop_gb"} for h in hits
    )
    should_clean = args.clean or bool(hits)
    cleaned = False
    if should_clean and not args.dry_run:
        rc = run_cleanup(pressure=pressure or any(h["metric"] == "disk_free_gb" for h in hits))
        cleaned = rc == 0
        s_after = sample()
        log(f"after_clean free={s_after['disk_free_gb']}G swap={s_after['swap_used_gb']}G load={s_after['load1']}")
        s = s_after

    now = int(time.time())
    last_fire = int(state.get("last_webhook_at") or 0)
    fire = bool(hits) and not args.no_webhook and not args.dry_run
    if fire and (now - last_fire) < COOLDOWN_SEC:
        log(f"webhook cooldown {COOLDOWN_SEC - (now - last_fire)}s remaining")
        fire = False
    fired = False
    if fire:
        fired = fire_webhook(hits, s, cleaned)
        if fired:
            state["last_webhook_at"] = now

    state.update({"disk_free_gb": s["disk_free_gb"], "sample": s, "hits": hits, "ts": now})
    save_state(state)
    return 0 if not hits or cleaned or fired else 1


if __name__ == "__main__":
    sys.exit(main())
