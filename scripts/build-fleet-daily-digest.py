#!/usr/bin/env python3
"""Build a day-by-day fleet activity digest: Markdown, HTML, and all-day ICS.

Sources (GitHub API + effort-log files when present):
  - Merged pull requests
  - Issues opened / closed / reopened
  - Effort-board bullets from each repo's docs/EFFORT-LOG.md (and live-style
    names when mirrored under docs/)

Outputs (under site/ and calendar/):
  site/index.html          — browsable day outline
  site/digest.md           — same content as Markdown
  calendar/daily-digest.ics — one all-day VEVENT per day (subscribe in Apple/Google)

Env:
  GITHUB_TOKEN / FLEET_GITHUB_TOKEN
  FLEET_OWNER (default jaywedgeworth22)
  FLEET_REPOS (comma list)
  DIGEST_LOOKBACK_DAYS (default 21)
  DIGEST_TZ (default America/Chicago)  — day bucketing only
  SITE_OUT (default site)
  ICS_OUT (default calendar/daily-digest.ics)
  SITE_BASE_URL (optional, e.g. https://jaywedgeworth22.github.io/ai-fleet-coordinator/)
  EFFORT_LOG_DIR (optional local dir of live boards, e.g. /Users/jay/apps)
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

# Allow `python3 scripts/build-fleet-daily-digest.py` from repo root
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ics_utils import ics_escape, join_ics  # noqa: E402

DEFAULT_REPOS = [
    "Socratic.Trade",
    "Congress.Trade",
    "Usage-Monitor",
    "congress-trading-shared",
    "ai-fleet-coordinator",
]

# Live machine boards (optional local override via EFFORT_LOG_DIR)
LIVE_EFFORT_FILES = {
    "Usage-Monitor": "API-USAGE-MONITOR-EFFORT-LOG.md",
    "Socratic.Trade": "SOCRATIC-TRADE-EFFORT-LOG.md",
    "Congress.Trade": "CONGRESS-TRADE-EFFORT-LOG.md",
    "congress-trading-shared": "CONGRESS-SHARED-EFFORT-LOG.md",
    "ai-fleet-coordinator": "FLEET-INFRA-EFFORT-LOG.md",
}

DONE_SECTIONS = frozenset(
    {
        "deployed",
        "completed",
        "done",
        "shipped",
        "closed",
        "complete",
    }
)
ACTIVE_SECTIONS = frozenset(
    {
        "in progress",
        "progress",
        "blocked",
        "waiting",
        "planned",
    }
)


@dataclass
class DayBucket:
    day: date
    merged_prs: list[dict[str, Any]] = field(default_factory=list)
    issues_opened: list[dict[str, Any]] = field(default_factory=list)
    issues_closed: list[dict[str, Any]] = field(default_factory=list)
    effort_lines: list[dict[str, str]] = field(default_factory=list)

    def is_empty(self) -> bool:
        return not (
            self.merged_prs
            or self.issues_opened
            or self.issues_closed
            or self.effort_lines
        )

    def counts_line(self) -> str:
        return (
            f"{len(self.merged_prs)} PRs merged · "
            f"{len(self.issues_opened)} issues opened · "
            f"{len(self.issues_closed)} issues closed · "
            f"{len(self.effort_lines)} effort rows"
        )


def env_int(name: str, default: int) -> int:
    raw = os.environ.get(name, "").strip()
    return int(raw) if raw else default


def token() -> str:
    t = (
        os.environ.get("FLEET_GITHUB_TOKEN", "").strip()
        or os.environ.get("GITHUB_TOKEN", "").strip()
    )
    if not t:
        raise SystemExit("error: set GITHUB_TOKEN or FLEET_GITHUB_TOKEN")
    return t


def gh_get(url: str, tok: str) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {tok}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ai-fleet-coordinator-daily-digest",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def gh_get_text(url: str, tok: str) -> str | None:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github.raw",
            "Authorization": f"Bearer {tok}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ai-fleet-coordinator-daily-digest",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        body = e.read().decode("utf-8", errors="replace")[:200]
        print(f"warn: GET {url} HTTP {e.code}: {body}", file=sys.stderr)
        return None
    except Exception as e:  # noqa: BLE001
        print(f"warn: GET {url} failed: {e}", file=sys.stderr)
        return None


def gh_list(url: str, tok: str, max_pages: int = 8) -> list[dict[str, Any]]:
    """Paginate a GitHub list endpoint (Link headers optional; stop on short page)."""
    items: list[dict[str, Any]] = []
    for page in range(1, max_pages + 1):
        sep = "&" if "?" in url else "?"
        page_url = f"{url}{sep}page={page}&per_page=100"
        try:
            data = gh_get(page_url, tok)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")[:300]
            print(f"warn: list HTTP {e.code}: {body}", file=sys.stderr)
            break
        except Exception as e:  # noqa: BLE001
            print(f"warn: list failed: {e}", file=sys.stderr)
            break
        if not isinstance(data, list):
            break
        items.extend(data)
        if len(data) < 100:
            break
    return items


def parse_iso(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def to_local_day(dt: datetime, tz: ZoneInfo) -> date:
    return dt.astimezone(tz).date()


def fetch_merged_prs(
    owner: str, repos: list[str], since: date, tok: str, tz: ZoneInfo
) -> list[tuple[date, dict[str, Any]]]:
    """List closed PRs via REST (avoids Search API secondary rate limits)."""
    out: list[tuple[date, dict[str, Any]]] = []
    since_dt = datetime.combine(since, datetime.min.time(), tzinfo=tz)
    for repo in repos:
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/pulls"
            f"?state=closed&sort=updated&direction=desc"
        )
        for it in gh_list(url, tok, max_pages=10):
            merged = parse_iso(it.get("merged_at"))
            if not merged:
                continue
            if merged < since_dt.astimezone(timezone.utc) and to_local_day(merged, tz) < since:
                # list is updated-desc; once we are well before since on updated_at, stop
                updated = parse_iso(it.get("updated_at"))
                if updated and to_local_day(updated, tz) < since:
                    break
                continue
            if to_local_day(merged, tz) < since:
                continue
            out.append(
                (
                    to_local_day(merged, tz),
                    {
                        "repo": repo,
                        "number": it.get("number"),
                        "title": (it.get("title") or "").strip(),
                        "url": it.get("html_url") or "",
                        "user": ((it.get("user") or {}).get("login") or ""),
                        "when": merged,
                    },
                )
            )
    return out


def fetch_issue_churn(
    owner: str, repos: list[str], since: date, tok: str, tz: ZoneInfo
) -> tuple[list[tuple[date, dict[str, Any]]], list[tuple[date, dict[str, Any]]]]:
    """List issues via REST since= (created/updated filter); bucket by created/closed day."""
    opened: list[tuple[date, dict[str, Any]]] = []
    closed: list[tuple[date, dict[str, Any]]] = []
    since_iso = datetime.combine(since, datetime.min.time(), tzinfo=timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    for repo in repos:
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/issues"
            f"?state=all&since={since_iso}&sort=updated&direction=desc"
        )
        for it in gh_list(url, tok, max_pages=10):
            if it.get("pull_request"):
                continue
            created = parse_iso(it.get("created_at"))
            closed_at = parse_iso(it.get("closed_at"))
            base = {
                "repo": repo,
                "number": it.get("number"),
                "title": (it.get("title") or "").strip(),
                "url": it.get("html_url") or "",
                "state": it.get("state") or "",
            }
            if created and to_local_day(created, tz) >= since:
                opened.append(
                    (to_local_day(created, tz), {**base, "when": created})
                )
            if closed_at and to_local_day(closed_at, tz) >= since:
                closed.append(
                    (to_local_day(closed_at, tz), {**base, "when": closed_at})
                )
    return opened, closed


_DATE_IN_LINE = re.compile(
    r"(20\d{2}-\d{2}-\d{2})|"
    r"(20\d{2}/\d{2}/\d{2})|"
    r"\b(20\d{2}-\d{2}-\d{2}T)"
)
_BULLET = re.compile(r"^\s*-\s+")
_HEADING = re.compile(r"^#{1,3}\s+(.+?)\s*$")
_STATUS_WORDS = (
    "merged",
    "complete",
    "completed",
    "deployed",
    "done",
    "shipped",
    "live",
    "closed",
    "in pr",
    "progress",
    "host done",
    "live verified",
)


def parse_effort_log(text: str, repo: str, since: date, tz: ZoneInfo) -> list[tuple[date, dict[str, str]]]:
    """Heuristic: board bullets under Deployed/Completed (and active WIP with status words)."""
    rows: list[tuple[date, dict[str, str]]] = []
    today = datetime.now(tz).date()
    section = ""
    for line in text.splitlines():
        hm = _HEADING.match(line)
        if hm:
            section = hm.group(1).strip().lower()
            continue
        if not _BULLET.match(line):
            continue
        if line.lstrip().startswith("- _") or "board closeout" in line.lower():
            continue
        low = line.lower()
        in_done = any(s in section for s in DONE_SECTIONS)
        in_active = any(s in section for s in ACTIVE_SECTIONS)
        has_status = any(k in low for k in _STATUS_WORDS)
        if in_done:
            pass
        elif in_active and has_status:
            pass
        elif not section and has_status:
            pass
        else:
            continue
        body = re.sub(r"^\s*-\s+", "", line).strip()
        if len(body) < 20:
            continue
        day = today
        m = _DATE_IN_LINE.search(body)
        if m:
            raw = (m.group(1) or m.group(2) or "")[:10].replace("/", "-")
            try:
                day = date.fromisoformat(raw)
            except ValueError:
                pass
        if day < since:
            continue
        prefix = ""
        if in_done:
            prefix = "[done] "
        elif in_active:
            prefix = "[wip] "
        rows.append(
            (
                day,
                {
                    "repo": repo,
                    "text": (prefix + body)[:400],
                    "section": section or "unknown",
                },
            )
        )
    if len(rows) > 120:
        rows = sorted(rows, key=lambda r: r[0], reverse=True)[:120]
    return rows


def fetch_effort_rows(
    owner: str, repos: list[str], since: date, tok: str, tz: ZoneInfo
) -> list[tuple[date, dict[str, str]]]:
    out: list[tuple[date, dict[str, str]]] = []
    effort_dir = os.environ.get("EFFORT_LOG_DIR", "").strip()
    for repo in repos:
        text: str | None = None
        source = ""
        if effort_dir:
            live_name = LIVE_EFFORT_FILES.get(repo)
            if live_name:
                p = Path(effort_dir) / live_name
                if p.is_file():
                    text = p.read_text(encoding="utf-8", errors="replace")
                    source = str(p)
        if text is None:
            for path in ("docs/EFFORT-LOG.md", "EFFORT-LOG.md"):
                url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
                text = gh_get_text(url, tok)
                if text:
                    source = f"{repo}/{path}"
                    break
        if text:
            rows = parse_effort_log(text, repo, since, tz)
            print(f"  effort {source}: {len(rows)} bullets")
            out.extend(rows)
        else:
            print(f"  effort {repo}: (none found)")
    return out


def bucket_all(
    prs: list[tuple[date, dict[str, Any]]],
    opened: list[tuple[date, dict[str, Any]]],
    closed: list[tuple[date, dict[str, Any]]],
    effort: list[tuple[date, dict[str, str]]],
) -> dict[date, DayBucket]:
    buckets: dict[date, DayBucket] = {}

    def b(d: date) -> DayBucket:
        if d not in buckets:
            buckets[d] = DayBucket(day=d)
        return buckets[d]

    for d, item in prs:
        b(d).merged_prs.append(item)
    for d, item in opened:
        b(d).issues_opened.append(item)
    for d, item in closed:
        b(d).issues_closed.append(item)
    for d, item in effort:
        b(d).effort_lines.append(item)

    for day in buckets.values():
        day.merged_prs.sort(key=lambda x: (x["repo"], x.get("number") or 0))
        day.issues_opened.sort(key=lambda x: (x["repo"], x.get("number") or 0))
        day.issues_closed.sort(key=lambda x: (x["repo"], x.get("number") or 0))
    return buckets


def day_summary_title(day: DayBucket) -> str:
    n = len(day.merged_prs)
    o = len(day.issues_opened)
    c = len(day.issues_closed)
    return f"Fleet: {n} merged · {o} opened · {c} closed"


def day_description(day: DayBucket) -> str:
    lines = [day.counts_line(), ""]
    if day.merged_prs:
        lines.append("Merged PRs:")
        for p in day.merged_prs[:40]:
            lines.append(f"- [{p['repo']}#{p['number']}] {p['title']}")
        if len(day.merged_prs) > 40:
            lines.append(f"  … +{len(day.merged_prs) - 40} more")
        lines.append("")
    if day.issues_closed:
        lines.append("Issues closed:")
        for p in day.issues_closed[:30]:
            lines.append(f"- [{p['repo']}#{p['number']}] {p['title']}")
        lines.append("")
    if day.issues_opened:
        lines.append("Issues opened:")
        for p in day.issues_opened[:30]:
            lines.append(f"- [{p['repo']}#{p['number']}] {p['title']}")
        lines.append("")
    if day.effort_lines:
        lines.append("Effort board:")
        for e in day.effort_lines[:25]:
            # strip markdown bold markers for ICS
            t = re.sub(r"\*+", "", e["text"])[:200]
            lines.append(f"- [{e['repo']}] {t}")
    return "\n".join(lines).strip()


def build_markdown(days: list[DayBucket], generated: datetime, tz: ZoneInfo, base_url: str) -> str:
    lines = [
        "# AI Fleet — daily activity digest",
        "",
        f"_Generated {generated.astimezone(tz).strftime('%Y-%m-%d %H:%M %Z')} · timezone {tz.key}_",
        "",
        "Sources: merged PRs, issues opened/closed, effort-board bullets (`docs/EFFORT-LOG.md`).",
        "",
    ]
    if base_url:
        lines.append(f"- **HTML:** {base_url.rstrip('/')}/")
        lines.append(f"- **ICS (daily outline):** {base_url.rstrip('/')}/calendar/daily-digest.ics")
        lines.append(
            f"- **ICS (per-commit activity):** {base_url.rstrip('/')}/calendar/agent-activity.ics"
        )
        lines.append("")
    for day in days:
        if day.is_empty():
            continue
        lines.append(f"## {day.day.isoformat()}")
        lines.append("")
        lines.append(f"*{day.counts_line()}*")
        lines.append("")
        if day.merged_prs:
            lines.append("### Merged PRs")
            lines.append("")
            for p in day.merged_prs:
                lines.append(
                    f"- **{p['repo']}** [#{p['number']}]({p['url']}): {p['title']}"
                    + (f" _(by {p['user']})_" if p.get("user") else "")
                )
            lines.append("")
        if day.issues_closed:
            lines.append("### Issues closed")
            lines.append("")
            for p in day.issues_closed:
                lines.append(f"- **{p['repo']}** [#{p['number']}]({p['url']}): {p['title']}")
            lines.append("")
        if day.issues_opened:
            lines.append("### Issues opened")
            lines.append("")
            for p in day.issues_opened:
                lines.append(f"- **{p['repo']}** [#{p['number']}]({p['url']}): {p['title']}")
            lines.append("")
        if day.effort_lines:
            lines.append("### Effort board")
            lines.append("")
            for e in day.effort_lines:
                lines.append(f"- **{e['repo']}**: {e['text']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_html(days: list[DayBucket], generated: datetime, tz: ZoneInfo, base_url: str) -> str:
    esc = html.escape
    gen = esc(generated.astimezone(tz).strftime("%Y-%m-%d %H:%M %Z"))
    ics_daily = esc((base_url.rstrip("/") + "/calendar/daily-digest.ics") if base_url else "calendar/daily-digest.ics")
    ics_act = esc(
        (base_url.rstrip("/") + "/calendar/agent-activity.ics") if base_url else "../calendar/agent-activity.ics"
    )
    md_href = "digest.md"

    sections: list[str] = []
    for day in days:
        if day.is_empty():
            continue
        blocks: list[str] = []

        def list_block(title: str, items: list[dict[str, Any]], kind: str) -> None:
            if not items:
                return
            lis = []
            for p in items:
                repo = esc(str(p.get("repo", "")))
                num = esc(str(p.get("number", "")))
                title_t = esc(str(p.get("title", "")))
                url = esc(str(p.get("url", "#")))
                lis.append(
                    f'<li><span class="repo">{repo}</span> '
                    f'<a href="{url}">#{num}</a>: {title_t}</li>'
                )
            blocks.append(
                f'<h3>{esc(title)}</h3><ul class="{kind}">' + "".join(lis) + "</ul>"
            )

        list_block("Merged PRs", day.merged_prs, "prs")
        list_block("Issues closed", day.issues_closed, "closed")
        list_block("Issues opened", day.issues_opened, "opened")
        if day.effort_lines:
            el = []
            for e in day.effort_lines:
                el.append(
                    f'<li><span class="repo">{esc(e["repo"])}</span>: '
                    f'{esc(e["text"])}</li>'
                )
            blocks.append("<h3>Effort board</h3><ul class=\"effort\">" + "".join(el) + "</ul>")

        sections.append(
            f'<section class="day" id="{day.day.isoformat()}">'
            f"<h2>{day.day.isoformat()}</h2>"
            f'<p class="meta">{esc(day.counts_line())}</p>'
            + "".join(blocks)
            + "</section>"
        )

    body = "\n".join(sections) if sections else "<p>No activity in the lookback window.</p>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>AI Fleet — daily activity</title>
  <style>
    :root {{
      --bg: #0f1419;
      --card: #1a2332;
      --text: #e7ecf3;
      --muted: #8b9bb4;
      --accent: #f59e0b;
      --link: #7dd3fc;
      --border: #2a3548;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 1.5rem clamp(1rem, 4vw, 2.5rem) 3rem;
      max-width: 52rem;
      margin-inline: auto;
    }}
    h1 {{ font-size: 1.6rem; margin: 0 0 0.35rem; letter-spacing: -0.02em; }}
    h2 {{ font-size: 1.2rem; margin: 0 0 0.35rem; color: var(--accent); }}
    h3 {{ font-size: 0.95rem; margin: 1rem 0 0.4rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }}
    .lede {{ color: var(--muted); margin: 0 0 1.25rem; }}
    .links {{ display: flex; flex-wrap: wrap; gap: 0.75rem 1.25rem; margin-bottom: 1.75rem; font-size: 0.95rem; }}
    a {{ color: var(--link); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .day {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1rem 1.15rem 1.15rem;
      margin-bottom: 1rem;
    }}
    .meta {{ color: var(--muted); font-size: 0.9rem; margin: 0 0 0.5rem; }}
    ul {{ margin: 0.25rem 0 0; padding-left: 1.15rem; }}
    li {{ margin: 0.2rem 0; }}
    .repo {{
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--bg);
      background: var(--accent);
      border-radius: 4px;
      padding: 0.05rem 0.4rem;
      margin-right: 0.25rem;
      vertical-align: middle;
    }}
    footer {{ margin-top: 2rem; color: var(--muted); font-size: 0.85rem; }}
    code {{ font-size: 0.85em; background: #0a0e14; padding: 0.1em 0.35em; border-radius: 4px; }}
  </style>
</head>
<body>
  <h1>AI Fleet — daily activity</h1>
  <p class="lede">Merged PRs, issue churn, and effort-board rows · generated {gen}</p>
  <nav class="links">
    <a href="{md_href}">Markdown</a>
    <a href="{ics_daily}">ICS — daily outline</a>
    <a href="{ics_act}">ICS — per-commit activity</a>
  </nav>
  {body}
  <footer>
    Built by <code>scripts/build-fleet-daily-digest.py</code> in
    <code>ai-fleet-coordinator</code>. Subscribe to the daily ICS in Apple Calendar
    (Add Subscription Calendar) or Google Calendar (From URL).
  </footer>
</body>
</html>
"""


def build_daily_ics(days: list[DayBucket], now: datetime, base_url: str) -> str:
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Jay Wedgeworth//AI Fleet Daily Digest//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:AI Fleet — Daily Digest",
        "X-WR-CALDESC:One all-day entry per day: merged PRs, issues opened/closed, effort board. Hosted by ai-fleet-coordinator.",
        "X-WR-TIMEZONE:America/Chicago",
        "REFRESH-INTERVAL;VALUE=DURATION:PT6H",
        "X-PUBLISHED-TTL:PT6H",
    ]
    for day in days:
        if day.is_empty():
            continue
        d = day.day
        next_d = d + timedelta(days=1)
        # VALUE=DATE all-day: DTEND is exclusive next day
        uid = f"fleet-daily-{d.isoformat()}@ai-fleet-coordinator"
        url = f"{base_url.rstrip('/')}/#{d.isoformat()}" if base_url else ""
        lines.extend(
            [
                "BEGIN:VEVENT",
                f"UID:{uid}",
                f"DTSTAMP:{now.astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
                f"DTSTART;VALUE=DATE:{d.strftime('%Y%m%d')}",
                f"DTEND;VALUE=DATE:{next_d.strftime('%Y%m%d')}",
                f"SUMMARY:{ics_escape(day_summary_title(day))}",
                f"DESCRIPTION:{ics_escape(day_description(day))}",
            ]
        )
        if url:
            lines.append(f"URL:{url}")
        lines.extend(
            [
                "CATEGORIES:fleet-daily,agent-activity",
                "STATUS:CONFIRMED",
                "TRANSP:TRANSPARENT",
                "END:VEVENT",
            ]
        )
    lines.append("END:VCALENDAR")
    return join_ics(lines)


def main() -> int:
    owner = os.environ.get("FLEET_OWNER", "jaywedgeworth22").strip() or "jaywedgeworth22"
    repos_raw = os.environ.get("FLEET_REPOS", "").strip()
    repos = [r.strip() for r in repos_raw.split(",") if r.strip()] or DEFAULT_REPOS
    lookback = env_int("DIGEST_LOOKBACK_DAYS", 21)
    tz_name = os.environ.get("DIGEST_TZ", "America/Chicago").strip() or "America/Chicago"
    tz = ZoneInfo(tz_name)
    site_out = Path(os.environ.get("SITE_OUT", "site"))
    ics_out = Path(os.environ.get("ICS_OUT", "calendar/daily-digest.ics"))
    base_url = os.environ.get("SITE_BASE_URL", "").strip()
    # Default GitHub Pages URL if not set
    if not base_url:
        base_url = f"https://{owner}.github.io/ai-fleet-coordinator"

    tok = token()
    now = datetime.now(timezone.utc)
    since = (now.astimezone(tz).date() - timedelta(days=lookback))

    print(f"owner={owner} repos={repos} since={since} tz={tz_name}")
    print("fetching merged PRs…")
    prs = fetch_merged_prs(owner, repos, since, tok, tz)
    print(f"  {len(prs)} merged PRs")
    print("fetching issue churn…")
    opened, closed = fetch_issue_churn(owner, repos, since, tok, tz)
    print(f"  {len(opened)} opened, {len(closed)} closed")
    print("fetching effort boards…")
    effort = fetch_effort_rows(owner, repos, since, tok, tz)
    print(f"  {len(effort)} effort bullets")

    buckets = bucket_all(prs, opened, closed, effort)
    days = sorted(buckets.values(), key=lambda d: d.day, reverse=True)

    site_out.mkdir(parents=True, exist_ok=True)
    ics_out.parent.mkdir(parents=True, exist_ok=True)

    md = build_markdown(days, now, tz, base_url)
    html_doc = build_html(days, now, tz, base_url)
    ics_body = build_daily_ics(days, now, base_url)

    (site_out / "digest.md").write_text(md, encoding="utf-8")
    (site_out / "index.html").write_text(html_doc, encoding="utf-8")
    # GitHub Pages: disable Jekyll so dotted paths / raw ICS serve as-is
    (site_out / ".nojekyll").write_text("", encoding="utf-8")
    ics_out.write_bytes(ics_body.encode("utf-8"))

    # Copies under site/ so Pages hosts HTML + both ICS feeds from one root
    cal_site = site_out / "calendar"
    cal_site.mkdir(parents=True, exist_ok=True)
    (cal_site / "daily-digest.ics").write_bytes(ics_body.encode("utf-8"))
    agent_ics = Path("calendar/agent-activity.ics")
    if agent_ics.is_file():
        (cal_site / "agent-activity.ics").write_bytes(agent_ics.read_bytes())

    n_days = sum(1 for d in days if not d.is_empty())
    print(f"wrote {site_out / 'index.html'}")
    print(f"wrote {site_out / 'digest.md'}")
    print(f"wrote {ics_out} ({n_days} day events)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
