# Mac local processes (owner machine)

**Canonical live list** of LaunchAgents, cron, login items, and other
always-on or scheduled jobs on Jay's Mac.  Not Coolify, not GitHub Actions
hosted runners, not a one-shot `npm exec` from an interactive agent session.

- Live: `/Users/jay/apps/MAC-LOCAL-PROCESSES.md`
- GitHub: https://github.com/jaywedgeworth22/ai-fleet-coordinator/blob/main/docs/MAC-LOCAL-PROCESSES.md
- Binding rule: `/Users/jay/apps/AGENT-SYNC.md` § Mac local processes

Last inventory: Fri, Aug 14, 2026 (Grok).

---

## Binding rule (every agent, every platform)

If you **create, change, load, bootout, or retire** any of the following on
this Mac, you **must** update this file in the same change (live copy first,
then the coordinator repo mirror):

- `~/Library/LaunchAgents/*.plist` (and `/Library/LaunchAgents` / `LaunchDaemons` if you touch those)
- `crontab`
- Login items
- `pm2` / `launchd` KeepAlive wrappers
- Periodic helper scripts that run without a human in the terminal

Do **not** add a process "just for this session" and leave it.  If it survives
logout or reboot, it belongs here.  If you retire one, mark it **Retired** —
do not delete the row.

Cloud / no-Mac agents: do not invent LaunchAgents.  Note the intended job in
the PR and leave a Mac seat to install + list it.

---

## How to add a row

1. Prefer `~/Library/LaunchAgents/com.jay.<name>.plist` or `com.jays.<name>.plist`.
2. Label, program path, KeepAlive / interval, log path, and a one-line purpose.
3. Never put secrets in the plist.  Inject via Infisical or `~/.secrets/` at
   runtime, value-blind.
4. Update this file + `~/apps/AGENT-SYNC.md` is already the pointer — do not
   duplicate the full table into AGENTS.md files.
5. Land the coordinator mirror in the same PR when you can reach that repo.

Manage:

```bash
launchctl print gui/$(id -u)/<Label>
launchctl kickstart -k gui/$(id -u)/<Label>   # restart
launchctl bootout gui/$(id -u)/<Label>        # stop (KeepAlive jobs will stay down until bootstrap)
```

---

## Always-on (KeepAlive or RunAtLoad service)

| Label | What | Notes |
|-------|------|--------|
| `com.jay.claude-remote-control` | `/Users/jay/.local/bin/claude remote-control` | Phone / claude.ai steering.  CWD `~/Code/Socratic.Trade` (must be a trusted dir).  **KeepAlive + RunAtLoad** — launchd restarts it if it dies.  Monet, Renoir, and Claude Code all show as `claude` in `ps`.  Log: `~/.claude/remote-control.log`.  Installed 2026-07-08.  Do **not** SIGKILL this because you do not see an interactive Claude TTY. |
| `com.jay.agy-acp` | `npx @rebornix/stdio-to-ws` → `agy-acp` | Antigravity ACP websocket bridge.  KeepAlive. |
| `com.jay.xcode-health` | `~/apps/xcode-health/xcode-health-server.py` | Xcode / runner health at xcode.jays.services.  KeepAlive. |
| `com.jay.shellular` | `npx shellular start` | Shellular runtime.  KeepAlive. |
| `com.congress.trade.vision-worker` | `~/vision-worker/run-vision-worker.sh` | CT vision worker.  KeepAlive.  Secrets from `~/.secrets/`, never printed. |
| `com.cursor.slack-sync` | `~/apps/cursor-slack-ws-sync.py` | Cursor #agent-sync Socket Mode inbox.  KeepAlive. |
| `actions.runner…mac-xcode26-usage` | `~/actions-runner/usage/runsvc.sh` | GitHub Actions Mac runner (Usage-Monitor). |
| `actions.runner…mac-xcode26-socratic` | `~/actions-runner/socratic/runsvc.sh` | GitHub Actions Mac runner (Socratic.Trade). |
| `actions.runner…mac-xcode26-congress` | `~/actions-runner/congress/runsvc.sh` | GitHub Actions Mac runner (Congress.Trade). |
| `com.PM2` (`pm2.jay.plist`) | `pm2 resurrect` | PM2 resurrect on login.  As of 2026-08-14 the process list was empty. |
| `homebrew.mxcl.moshi-hook` | Homebrew `moshi-hook serve` | Vendor/local hook server.  KeepAlive. |

---

## Periodic / one-shot LaunchAgents

| Label | Cadence | Script | Purpose |
|-------|---------|--------|---------|
| `com.jay.disk-janitor` | every 30 min | `~/.claude-disk-janitor/janitor.sh` | Regenerable-cache + idle-worktree cleanup when disk is tight. |
| `com.jay.merge-shepherd` | every 30 min | `~/.claude-merge-shepherd/run.sh` | `gh pr update-branch` so bot merges still retrigger verify.  Log: `~/.claude-merge-shepherd/shepherd.log`. |
| `com.jays.mac-server-watchdog` | every 120 s | `Usage-Monitor/scripts/ops/mac-server-watchdog.sh` | Mac heartbeat → UM `/api/ingest/mac-heartbeat` + local self-heal. |
| `com.jays.antigravity-usage-collector` | every 4 h | `infisical run` → node collector | Antigravity quota → UM ingest. |
| `com.jay.mac-cleanup` | calendar | `~/apps/mac-auto-cleanup.sh` | Broader cache / DerivedData / old session prune. |
| `com.jay.ios-ship-now` | RunAtLoad, KeepAlive **false** | `~/apps/ios-fleet/ship-now-gui.sh` | One-shot GUI-session TestFlight ship (needs login keychain). |
| `com.jay.provider-knob-sync` | (plist is a **TEMPLATE** with an XML comment; `plistlib` will not load it) | — | Not an active job until someone installs a real plist.  Do not treat as running. |

Vendor (do not manage unless asked): Homebrew autoupdate (daily), GoogleUpdater (hourly), CleanMyMac updater (6 h).

---

## Cron

| Schedule | Script | Purpose |
|----------|--------|---------|
| `41 9 * * *` | `~/apps/check-hetzner-cx43.sh` | Watch for a cheaper 8-vCPU Hetzner upgrade target for `host.jays.services`. |

---

## Login items (Aqua)

GeminiAppLauncher, Devly, Kimi, Google Drive.

---

## Retired / not loaded

| Item | State |
|------|--------|
| `~/apps/com.jay.code-main-keeper.plist` | On disk as a template; **not** in `~/Library/LaunchAgents`.  Sibling `*.retired-launchd` marks it retired. |

---

## Not in this list (on purpose)

- Interactive `grok` / `claude` / `codex` / `cursor` terminals
- Per-session MCP children (`npm exec @sentry/mcp-server`, toolbox, etc.).  Those must die with the parent.  Orphans with `ppid=1` are leaks — kill those, not launchd KeepAlive jobs.
- Coolify / Hetzner app containers
- iOS Simulator

---

## Claude-family note

`claude remote-control` is the Mac half of phone steering.  Monet and Renoir
are Claude-family seats and show up as `claude` in the process list.  The
installed job is **always-on KeepAlive**, not "only while a TTY Claude is
open."  If remote control is "hosed" on the phone:

```bash
pgrep -fl "claude remote-control"
launchctl kickstart -k gui/$(id -u)/com.jay.claude-remote-control
tail -50 ~/.claude/remote-control.log
```

Do not boot it out because an inventory pass did not see an interactive session.
