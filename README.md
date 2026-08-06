# AI Fleet Coordinator

This repository contains a framework for operating a fully autonomous multi-agent AI software engineering team. It provides the protocols, scripts, and CI workflows necessary for multiple AI agents (like Claude, Codex, Antigravity, and Cursor) to collaborate in separate parallel git worktrees, communicate over Slack, manage a shared effort board, and safely auto-merge their work.

## Core Concepts

1. **Agent Lanes:** Every agent operates in its own dedicated, persistent git worktree (`~/apps/project-claude`, `~/apps/project-codex`, etc.). They never overwrite each other's uncommitted work.
2. **Slack Synchronization (`#agent-sync`):** Agents coordinate their actions, announce when they are running a full CI gate (`gating now`), and claim tasks by reading and posting to a designated Slack channel.
3. **The Effort Log:** A shared markdown Kanban board (`EFFORT-LOG-PROTOCOL.md`) acts as the central source of truth for task allocation.
4. **Safe Landings (`land.sh`):** Agents don't push directly to `main`. They use a strict script that verifies the build locally, pushes to a feature branch, and creates an auto-merging PR.
5. **Fleet daily digest + calendars:** day-by-day HTML/Markdown of merged PRs, issue churn, and effort-board rows, plus two ICS feeds (daily all-day outline + per-commit activity). Hosted on GitHub Pages (see below).
6. **Apple Notes for owner review (2026-08-05):** plans, designs, reviews, and other owner-facing documents also go into Apple Notes folder **`Coding`**, pinned at the top. Helper: `scripts/apple-notes-coding.sh` (or `~/apps/apple-notes-coding.sh`). Full rule in `AGENT-SYNC.md`.

## Setup

1. **Create the Agent Lanes:**
   Run `./scripts/setup-agent-lanes.sh <base_path>` to create the isolated Git worktrees for your agents.
2. **Initialize Slack Sync:**
   Run `./scripts/setup-slack-sync.sh` and provide a Slack Bot Token to allow agents to coordinate.
3. **Apply the Rules:**
   Copy `TEMPLATE-AGENTS.md` to your own project's `AGENTS.md` and customize it. Ensure all agents are instructed to read it.
4. **Setup GitHub Actions:**
   Copy the contents of `github-workflows-template/workflows` to your project's `.github/workflows` folder to enable automatic PR updating and (optionally) Sentry CI reporting.
5. **(Optional) Run Fleet Monitor:**
   Use the `fleet-sentry-monitor` PM2 ecosystem to track the health of your agent background processes.
6. **Subscribe to the fleet daily digest / calendars** (optional):
   See the next section.

## Fleet daily digest (HTML + Markdown + ICS)

Day-by-day outline of fleet work: **merged PRs**, **issues opened/closed**, and
**effort-board** bullets (`docs/EFFORT-LOG.md` mirrors, or live boards under
`EFFORT_LOG_DIR` when building locally). Built by
`scripts/build-fleet-daily-digest.py` and refreshed every 6 hours by
`.github/workflows/fleet-activity-site.yml`, which also rebuilds the per-commit
activity ICS and deploys the site to **GitHub Pages**.

### Hosted URLs

| Artifact | URL |
|----------|-----|
| **HTML site** | https://jaywedgeworth22.github.io/ai-fleet-coordinator/ |
| **Markdown** | https://jaywedgeworth22.github.io/ai-fleet-coordinator/digest.md |
| **ICS — daily outline** (all-day “what shipped”) | https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/daily-digest.ics |
| **ICS — per-commit activity** | https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/agent-activity.ics |

Raw-from-`main` fallbacks (no Pages required):

```text
https://raw.githubusercontent.com/jaywedgeworth22/ai-fleet-coordinator/main/calendar/daily-digest.ics
https://raw.githubusercontent.com/jaywedgeworth22/ai-fleet-coordinator/main/calendar/agent-activity.ics
https://raw.githubusercontent.com/jaywedgeworth22/ai-fleet-coordinator/main/site/digest.md
```

### Subscribe (Apple / Google / Outlook)

**Recommended:** daily outline ICS (one all-day event per day with PR/issue/effort summary).

**Apple Calendar (iOS):** Calendar → Calendars → Add Calendar → Add Subscription Calendar → paste HTTPS URL → Find.

**Google Calendar (web):** Other calendars → + → From URL → paste URL.

**Google Calendar (iOS):** Google's mobile "Add Subscription Calendar" is picky; if it says *Validation failed*, add the same URL on [calendar.google.com](https://calendar.google.com) (web) instead — mobile will then show the subscribed calendar.

CDN alternate for the commit feed (sometimes validates more cleanly on mobile):

```text
https://cdn.jsdelivr.net/gh/jaywedgeworth22/ai-fleet-coordinator@main/calendar/agent-activity.ics
```

### Enable GitHub Pages (one-time)

Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
The workflow uses `actions/deploy-pages`. First successful run after that publishes
the site URL above.

### Optional: private repo coverage

Default `GITHUB_TOKEN` sees public repos only. To include private fleet repos
(e.g. `Congress.Trade`), add a fine-grained PAT (read-only Contents + Issues on
those repos) as Actions secret **`FLEET_GITHUB_TOKEN`**.

### Local rebuild

```bash
export GITHUB_TOKEN="$(gh auth token)"   # or FLEET_GITHUB_TOKEN
export EFFORT_LOG_DIR=/Users/jay/apps    # optional: live effort boards
python3 scripts/build-agent-calendar.py
python3 scripts/build-fleet-daily-digest.py
# outputs: site/index.html, site/digest.md, calendar/daily-digest.ics
```

ICS line-folding uses `scripts/ics_utils.py` (RFC 5545 octet folding) so Apple/
Google accept long DESCRIPTION lines.

## License
Apache-2.0
