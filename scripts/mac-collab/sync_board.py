#!/usr/bin/env python3
"""Keep the mac-collab findings tool synchronized with every app's live
effort-log board and every repo's GitHub issues.

Reuses the board-parsing model from each repo's own
scripts/sync-effort-issues.py (heading classification by keyword, top-level
bullet = new item, indented continuation lines fold into the item body).

Run standalone for a one-off sync, or via run_forever() as the pm2-managed
recurring job ("always synchronized").

Usage:
    python3 sync_board.py --dry-run   # print counts, POST nothing
    python3 sync_board.py             # one sync pass
    python3 sync_board.py --loop      # sync every SYNC_INTERVAL_S forever (pm2 entrypoint)
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE_URL = os.environ.get("MAC_COLLAB_URL", "http://127.0.0.1:8792")
SECRETS = Path.home() / ".secrets" / "mac-collab.env"
APPS = Path.home() / "apps"
SYNC_INTERVAL_S = 600  # 10 minutes
CLOSED_ISSUE_LOOKBACK_DAYS = 30

# app slug -> (live board path, github "owner/repo" or None)
APP_REGISTRY = {
    "socratic-trade": (APPS / "TRADING-EFFORT-LOG.md", "jaywedgeworth22/Socratic.Trade"),
    "congress-trading-shared": (APPS / "CONGRESS-SHARED-EFFORT-LOG.md", "jaywedgeworth22/congress-trading-shared"),
    "usage-monitor": (APPS / "API-USAGE-MONITOR-EFFORT-LOG.md", "jaywedgeworth22/Usage-Monitor"),
    "congress-trade": (APPS / "CONGRESS-TRADE-EFFORT-LOG.md", "jaywedgeworth22/Congress.Trade"),
    "dealdex": (APPS / "DEALDEX-EFFORT-LOG.md", "jaywedgeworth22/DealDex"),
    "personal-site": (APPS / "PERSONAL-SITE-EFFORT-LOG.md", "jaywedgeworth22/Personal-Site"),
    "fleet-infra": (APPS / "FLEET-INFRA-EFFORT-LOG.md", None),
    "topspin": (APPS / "TOPSPIN-EFFORT-LOG.md", "jaywedgeworth22/TopSpin"),
}

# --- effort-board parsing (mirrors each repo's scripts/sync-effort-issues.py) ---

SECTION_KEYWORDS = [
    ("deployed", "deployed"),
    ("completed", "completed"),
    ("recently closed", "completed"),
    ("recently completed", "completed"),
    ("historical", "completed"),
    ("archive", "completed"),
    ("closed", "completed"),
    ("in progress", "in-progress"),
    ("active", "in-progress"),
    ("planned", "planned"),
    ("reserved", "planned"),
]
PLACEHOLDER_RE = re.compile(
    r"^\(?\s*(none|n/?a\b.*|seeded empty.*|add rows here.*|record the.*|see rollout notes.*)\s*\)?\.?$",
    re.IGNORECASE,
)
BULLET_RE = re.compile(r"^[-*]\s+(.*)$")
BUCKET_TO_STATUS = {"planned": "open", "in-progress": "in_progress", "completed": "completed", "deployed": "deployed"}


class BoardItem:
    def __init__(self, bucket: str, first_line: str):
        self.bucket = bucket
        self.first_line = first_line
        self.body_lines: list[str] = []

    @property
    def normalized_key_text(self) -> str:
        text = re.sub(r"[*_`]", "", self.first_line)
        return re.sub(r"\s+", " ", text).strip().lower()

    @property
    def key(self) -> str:
        return hashlib.sha1(self.normalized_key_text.encode("utf-8")).hexdigest()

    @property
    def body(self) -> str:
        return "\n".join(self.body_lines)

    @property
    def display_title(self) -> str:
        """A headline, not the whole bullet.

        Effort-log rows are frequently a full paragraph on one line. The
        convention is that the lead is bolded --
        `**2026-08-17 - GROK - IN PROGRESS - Effort-board hygiene.** rest...` --
        so prefer that bolded lead; otherwise fall back to the first sentence,
        then to a hard character clamp. The untruncated text still goes into
        the item's description, so nothing is lost.
        """
        text = re.sub(r"\s+", " ", self.first_line).strip()
        m = re.match(r"\*\*(.+?)\*\*", text)
        if m and len(m.group(1)) >= 12:
            lead = m.group(1).strip()
        else:
            plain = re.sub(r"[*_`]", "", text)
            m2 = re.match(r"(.{20,160}?[.!?])(?:\s|$)", plain)
            lead = m2.group(1).strip() if m2 else plain
        lead = re.sub(r"[*_`]", "", lead).strip(" -—:")
        if len(lead) > 160:
            lead = lead[:157].rstrip() + "..."
        return lead or text[:160]


def classify_heading(heading_text: str) -> str | None:
    lowered = heading_text.strip().lower()
    for keyword, bucket in SECTION_KEYWORDS:
        if keyword in lowered:
            return bucket
    return None


def parse_board(text: str) -> list[BoardItem]:
    items: list[BoardItem] = []
    current_bucket: str | None = None
    current_item: BoardItem | None = None

    for raw_line in text.splitlines():
        heading_match = re.match(r"^##\s+(.*)$", raw_line)
        if heading_match:
            if current_item is not None:
                items.append(current_item)
                current_item = None
            current_bucket = classify_heading(heading_match.group(1))
            continue

        if current_bucket is None:
            continue

        bullet_match = BULLET_RE.match(raw_line)
        if bullet_match:
            if current_item is not None:
                items.append(current_item)
                current_item = None
            content = bullet_match.group(1).strip()
            if PLACEHOLDER_RE.match(content):
                continue
            current_item = BoardItem(bucket=current_bucket, first_line=content)
            continue

        if current_item is not None:
            stripped = raw_line.strip()
            if stripped == "":
                continue
            if raw_line.startswith((" ", "\t")):
                current_item.body_lines.append(stripped)

    if current_item is not None:
        items.append(current_item)

    return items


# --- GitHub issues ---

def gh_issue_list(repo: str, extra_args: list[str]) -> list[dict]:
    cmd = [
        "gh", "issue", "list", "--repo", repo, "--limit", "500",
        "--json", "number,title,url,state,stateReason,updatedAt,labels,body",
        *extra_args,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"WARN: gh issue list failed for {repo}: {result.stderr.strip()}", file=sys.stderr)
        return []
    return json.loads(result.stdout)


def fetch_repo_issues(repo: str) -> list[dict]:
    open_issues = gh_issue_list(repo, ["--state", "open"])
    since = (datetime.now(timezone.utc) - timedelta(days=CLOSED_ISSUE_LOOKBACK_DAYS)).strftime("%Y-%m-%d")
    closed_recent = gh_issue_list(repo, ["--search", f"is:closed closed:>={since}"])
    return open_issues + closed_recent


def issue_status(issue: dict) -> str:
    if issue["state"] == "OPEN":
        return "open"
    reason = (issue.get("stateReason") or "").upper()
    if reason == "NOT_PLANNED":
        return "wontfix"
    return "completed"


# --- mac-collab API client ---

def load_token() -> str:
    env = os.environ.get("MAC_COLLAB_TOKEN", "").strip()
    if env:
        return env
    if SECRETS.is_file():
        for line in SECRETS.read_text().splitlines():
            s = line.strip()
            if s.startswith("export "):
                s = s[7:]
            if s.startswith("MAC_COLLAB_TOKEN="):
                return s.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def post_finding(token: str, payload: dict) -> dict:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/findings", data=body, method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


# --- one sync pass ---

def sync_once(dry_run: bool = False) -> None:
    effort_payloads = []
    issue_payloads = []

    for app, (board_path, repo) in APP_REGISTRY.items():
        if board_path.is_file():
            items = parse_board(board_path.read_text(encoding="utf-8", errors="replace"))
            for item in items:
                effort_payloads.append({
                    "app": app,
                    "external_uid": f"effort-{item.key}",
                    "source": f"{app} live effort board",
                    "title": item.display_title,
                    "severity": None,
                    "category": None,
                    "surface": None,
                    # Full untruncated bullet + any indented continuation lines.
                    "description": "\n\n".join(x for x in (item.first_line, item.body) if x),
                    "recommended_fix": None,
                    "status": BUCKET_TO_STATUS[item.bucket],
                    "source_kind": "effort-row",
                    "source_url": None,
                    "repo": repo,
                })
        else:
            print(f"WARN: live board missing for {app}: {board_path}", file=sys.stderr)

        if repo:
            for issue in fetch_repo_issues(repo):
                labels = [l["name"] for l in issue.get("labels", []) if l["name"] != "effort-board"]
                issue_payloads.append({
                    "app": app,
                    "external_uid": f"issue-{repo}-{issue['number']}",
                    "source": f"{repo} GitHub issues",
                    "title": issue["title"][:500],
                    "severity": None,
                    "category": labels[0] if labels else None,
                    "surface": None,
                    "description": (issue.get("body") or "")[:4000],
                    "recommended_fix": None,
                    "status": issue_status(issue),
                    "source_kind": "github-issue",
                    "source_url": issue["url"],
                    "repo": repo,
                })

    print(f"Parsed {len(effort_payloads)} effort-board items, {len(issue_payloads)} GitHub issues (open + closed<{CLOSED_ISSUE_LOOKBACK_DAYS}d).")

    if dry_run:
        from collections import Counter
        print("Effort rows by app:", dict(Counter(p["app"] for p in effort_payloads)))
        print("Issues by app:", dict(Counter(p["app"] for p in issue_payloads)))
        return

    token = load_token()
    if not token:
        print("ERROR: MAC_COLLAB_TOKEN not found", file=sys.stderr)
        return

    errors = 0
    for payload in effort_payloads + issue_payloads:
        try:
            post_finding(token, payload)
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            print(f"ERROR posting {payload['external_uid']}: {e}", file=sys.stderr)
            errors += 1
    print(f"Synced. errors={errors}")


def run_forever() -> None:
    while True:
        try:
            sync_once()
        except Exception as e:  # keep the loop alive across transient errors
            print(f"sync_once failed: {e}", file=sys.stderr)
        time.sleep(SYNC_INTERVAL_S)


if __name__ == "__main__":
    if "--loop" in sys.argv:
        run_forever()
    else:
        sync_once(dry_run="--dry-run" in sys.argv)
