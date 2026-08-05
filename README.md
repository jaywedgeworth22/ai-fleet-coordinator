# AI Fleet Coordinator

This repository contains a framework for operating a fully autonomous multi-agent AI software engineering team. It provides the protocols, scripts, and CI workflows necessary for multiple AI agents (like Claude, Codex, Antigravity, and Cursor) to collaborate in separate parallel git worktrees, communicate over Slack, manage a shared effort board, and safely auto-merge their work.

## Core Concepts

1. **Agent Lanes:** Every agent operates in its own dedicated, persistent git worktree (`~/apps/project-claude`, `~/apps/project-codex`, etc.). They never overwrite each other's uncommitted work.
2. **Slack Synchronization (`#agent-sync`):** Agents coordinate their actions, announce when they are running a full CI gate (`gating now`), and claim tasks by reading and posting to a designated Slack channel.
3. **The Effort Log:** A shared markdown Kanban board (`EFFORT-LOG-PROTOCOL.md`) acts as the central source of truth for task allocation.
4. **Safe Landings (`land.sh`):** Agents don't push directly to `main`. They use a strict script that verifies the build locally, pushes to a feature branch, and creates an auto-merging PR.
5. **Agent Activity Calendar:** A public ICS feed of recent fleet commits for Apple/Google Calendar subscription (see below).
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
6. **Subscribe to the agent activity calendar** (optional):
   See the next section.

## Agent activity calendar (ICS)

Permanent calendar feed of recent **merged/pushed commits** across the fleet
(`Socratic.Trade`, `Congress.Trade`, `Usage-Monitor`, `congress-trading-shared`,
`ai-fleet-coordinator`). Built by `scripts/build-agent-calendar.py` and refreshed
every 6 hours by `.github/workflows/agent-calendar.yml`.

### Subscribe (Apple / Google / Outlook)

Use this **HTTPS** URL (not a temporary Grok preview host):

```text
https://raw.githubusercontent.com/jaywedgeworth22/ai-fleet-coordinator/main/calendar/agent-activity.ics
```

Alternate CDN (sometimes validates more cleanly on mobile):

```text
https://cdn.jsdelivr.net/gh/jaywedgeworth22/ai-fleet-coordinator@main/calendar/agent-activity.ics
```

**Apple Calendar (iOS):** Calendar → Calendars → Add Calendar → Add Subscription Calendar → paste URL → Find.

**Google Calendar (web):** Other calendars → + → From URL → paste URL.

**Google Calendar (iOS):** Google's mobile "Add Subscription Calendar" is picky; if it says *Validation failed*, add the same URL on [calendar.google.com](https://calendar.google.com) (web) instead — mobile will then show the subscribed calendar.

### Optional: private repo coverage

Default `GITHUB_TOKEN` sees public repos only. To include private fleet repos
(e.g. `Congress.Trade`), add a fine-grained PAT (read-only Contents on those
repos) as Actions secret **`FLEET_GITHUB_TOKEN`**.

### Local rebuild

```bash
export GITHUB_TOKEN=ghp_...   # or FLEET_GITHUB_TOKEN
python3 scripts/build-agent-calendar.py
```

## License
Apache-2.0
