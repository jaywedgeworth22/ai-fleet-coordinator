# AI Fleet Coordinator

This repository contains a framework for operating a fully autonomous multi-agent AI software engineering team. It provides the protocols, scripts, and CI workflows necessary for multiple AI agents (like Claude, Codex, Antigravity, and Cursor) to collaborate in separate parallel git worktrees, communicate over Slack, manage a shared effort board, and safely auto-merge their work.

## Core Concepts

1. **Agent Lanes:** Every agent operates in its own dedicated, persistent git worktree (`~/apps/project-claude`, `~/apps/project-codex`, etc.). They never overwrite each other's uncommitted work.
2. **Slack Synchronization (`#agent-sync`):** Agents coordinate their actions, announce when they are running a full CI gate (`gating now`), and claim tasks by reading and posting to a designated Slack channel.
3. **The Effort Log:** A shared markdown Kanban board (`EFFORT-LOG-PROTOCOL.md`) acts as the central source of truth for task allocation.
4. **Safe Landings (`land.sh`):** Agents don't push directly to `main`. They use a strict script that verifies the build locally, pushes to a feature branch, and creates an auto-merging PR.

## Setup

1. **Create the Agent Lanes:**
   Run `./scripts/setup-agent-lanes.sh <base_path>` to create the isolated Git worktrees for your agents.
2. **Initialize Slack Sync:**
   Run `./scripts/setup-slack-sync.sh` and provide a Slack Bot Token to allow agents to coordinate.
3. **Apply the Rules:**
   Copy `TEMPLATE-AGENTS.md` to your own project's `AGENTS.md` and customize it. Ensure all agents are instructed to read it.
4. **Setup GitHub Actions:**
   Copy the contents of `.github/workflows` to your project to enable automatic PR updating and (optionally) Sentry CI reporting.
5. **(Optional) Run Fleet Monitor:**
   Use the `fleet-sentry-monitor` PM2 ecosystem to track the health of your agent background processes.

## License
MIT
