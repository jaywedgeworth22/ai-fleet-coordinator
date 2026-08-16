# Mac local processes (owner machine)

**This is the master list.**  Every always-on job, scheduled job, login item,
and installed helper script that agents create on Jay's Mac lives here.
Not Coolify.  Not GitHub-hosted runners.  Not a one-shot `npm exec` from an
interactive session.

- Live: `/Users/jay/apps/MAC-LOCAL-PROCESSES.md`
- GitHub: https://github.com/jaywedgeworth22/ai-fleet-coordinator/blob/main/docs/MAC-LOCAL-PROCESSES.md
- Apple Note: `⭐️ Background Jobs Master List` (Coding, pinned; owner-renamed 2026-08-16)
- Binding rule: `/Users/jay/apps/AGENT-SYNC.md` § Mac local processes

Last inventory: Sat, Aug 15, 2026 11:51pm CT (Grok, launchd pass).  Parent
restarted dumped pm2 jobs.  This pass checked launchd always-on + on-demand
helpers (not the pm2 jobs).  Note title `⭐️ Background Jobs Master List`.

**How to read the Kind column**

- **Always-on** — supposed to stay up across logout/reboot (KeepAlive or a
  login resurrect).  If it is down, that is a bug unless the row says Disabled.
- **Scheduled** — launchd/cron fires it; it is not a long-lived daemon.
- **On-demand** — installed helper.  Agents run it by hand.  It must not linger.

---

## Binding rule (every agent, every platform, forever)

If you **create, change, load, bootout, or retire** any of the following, you
**must** update this file **and** the Apple Note in the same change
(`~/apps/apple-notes-coding.sh --update "⭐️ Background Jobs Master List"`
— prefer `--update` on that exact title; do not mint a second note):

- `~/Library/LaunchAgents/*.plist` (and `/Library/LaunchAgents` /
  `LaunchDaemons` if you touch those)
- `crontab` / login items
- `pm2` KeepAlive jobs (`pm2 start` / `delete` / `save`)
- Any helper script under `~/apps`, `~/.claude-*`, `~/vision-worker`,
  `~/actions-runner`, or similar that other agents are expected to run

Do **not** add a process "just for this session" and leave it.  If it survives
logout or reboot, it belongs here.  If you retire one, mark it **Retired** —
do not delete the row.

Cloud / no-Mac agents: do not invent LaunchAgents.  Describe the job in the
PR and leave a Mac seat to install + list it.

Never register a daemon from `~/.npm/_npx/…`.  `mac-auto-cleanup.sh` wipes
that tree and the job crash-loops (Shellular did this 42,703× on 2026-08-13).
Install to `~/apps/<tool>-runtime` instead.

---

## Always-on (supposed to stay up)

Live-checked Sat, Aug 15, 2026 11:51pm CT.

| Name | Kind | What it is | Live now |
|---|---|---|---|
| `com.jay.claude-remote-control` | Always-on | Phone / claude.ai steering.  Monet / Renoir / Claude all look like `claude`.  Do not SIGKILL because you see no TTY. | **Up** (pid 3077) |
| `com.jay.agy-acp` | Always-on | Antigravity ACP websocket on port 8765. | **Up** (pid 1896) |
| `com.jay.xcode-health` | Always-on | Xcode / runner health.  Binds `127.0.0.1:8791` (not 8788).  Public name `xcode.jays.services`. | **Up** (pid 1879).  Local `/health` 200.  Public 200 via `Jay's Tunnel`. |
| `com.congress.trade.vision-worker` | Always-on | CT local vision worker for scanned PTRs.  Secrets from `~/.secrets/`. | **Up** (pid 40656, logging ~45s).  last-exit **-15** is a stale prior SIGTERM (`runs=2`); `immediate reason = inefficient` is App Nap/energy, not down.  Do not kickstart. |
| `com.cursor.slack-sync` | Always-on | Cursor seat's #agent-sync Socket Mode inbox. | **Up** (pid 1887) |
| `homebrew.mxcl.moshi-hook` | Always-on | Vendor/local hook server (`moshi-hook serve`). | **Up** (pid 1900) |
| `actions.runner…mac-xcode26-congress` | Always-on | GitHub Actions Mac runner for Congress.Trade. | **Up** (pid 1902) |
| `actions.runner…mac-xcode26-socratic` | Always-on | GitHub Actions Mac runner for Socratic.Trade. | **Up** (pid 1897) |
| `actions.runner…mac-xcode26-usage` | Always-on | GitHub Actions Mac runner for Usage-Monitor. | **Up** (pid 1878) |
| `com.cloudflare.cloudflared` | Always-on | System LaunchDaemon.  Named tunnel `Jay's Tunnel`.  Hosts scout / agent-sync / xcode.jays.services. | **Up** (pid 835, root).  Do not mint a TryCloudflare hostname.  Do not change `SENATE_RELAY_URL`. |
| `com.PM2` | Login one-shot | `pm2 resurrect` at login (`LaunchOnlyOnce`).  Plist ProgramArguments is `/opt/homebrew/bin/pm2 resurrect` (old `~/.npm/_npx/…` path is gone). | **Enabled.**  Bootstrapped 2026-08-15 23:49; process exits and leaves `launchctl list` (expected).  `/tmp/com.PM2.err` still holds the Aug 13 vanished-path line; that run is stale. |
| **pm2 `shellular`** | Always-on | Phone → this Mac (Shellular).  Pinned install: `~/apps/shellular-runtime` (v0.0.52).  **Not** launchd — `com.jay.shellular` is **disabled** (it fought pm2, 218 restarts). | **Up** (pm2 pid 73612) |
| **pm2 `scout`** | Always-on | Senate/House scout on the Mac.  Must start with stdin `/dev/null` (`bash -lc 'exec …/run-scout.sh </dev/null'`).  A raw `pm2 start run-scout.sh --interpreter bash` hangs in bash `reader_loop` because pm2's unix-socket stdin breaks the secrets heredoc. | **Up** (node congress-scout.mjs; restarted 2026-08-16) |
| **pm2 `senate-relay`** | Always-on | Local Senate eFD relay (`127.0.0.1:8899`) for `scout.jays.services`. | **Up** — local `/health` 200 |
| **pm2 `senate-tunnel`** | Always-on | Watcher only — does **not** run cloudflared.  Named tunnel `Jay's Tunnel` is the system cloudflared. | **Up** (watcher); public `https://scout.jays.services/health` 200 |
| **pm2 `agent-sync-push`** | Always-on | Slack Socket Mode fan-out + `POST /post` for #agent-sync. | **Up** — `http://127.0.0.1:8787/health` 200 |
| **pm2 `code-main-keeper`** | Always-on | Keeps `~/Code/*` integration trees on `origin/main` (ff-only). | **Up** |
| `com.jay.imessage-grok` | Always-on (intended) | Grok inbox for iMessage group Grok - Socratic Trade.  Reads `chat.db`.  Plist now calls Xcode `Python.app` (not `/usr/bin/python3`). | launchd **disabled** (FDA).  Aqua orphan **Up** (pid 81696, `ppid=1`, this is the intended listener — do not kill as a leak).  launchd-spawned `Python.app` still gets `authorization denied` on `chat.db`.  Owner: System Settings → Privacy & Security → Full Disk Access → allow that `Python.app` for background, then `launchctl enable gui/501/com.jay.imessage-grok` and bootstrap.  Do not load until then (KeepAlive would crash-loop every 10s). |
| `com.jay.shellular` | Disabled | Old launchd wrapper (`npx shellular start`).  Disabled 2026-08-12.  Do not re-enable while pm2 owns it. | **Disabled** |

---

## Scheduled (fires, then exits)

| Name | Cadence | What it is |
|---|---|---|
| `com.jay.disk-janitor` | every 30 min | Regenerable-cache + idle-worktree cleanup when disk is tight. |
| `com.jay.merge-shepherd` | every 30 min | `gh pr update-branch` so bot merges still retrigger verify. |
| `com.jays.mac-server-watchdog` | every 120 s | Mac heartbeat → Usage Monitor + local self-heal. |
| `com.jays.antigravity-usage-collector` | every 4 h | Antigravity quota → Usage Monitor ingest (via Infisical). |
| `com.jay.mac-cleanup` | 03:00 daily | Broader cache / DerivedData / old session prune.  **Wipes `~/.npm/_npx`.** |
| `com.github.domt4.homebrew-autoupdate` | daily | Homebrew autoupdate.  Vendor. |
| `com.google.GoogleUpdater.wake` | hourly | Google updater wake.  Vendor. |
| `com.macpaw.CleanMyMac5.Updater` | every 6 h | CleanMyMac updater.  Vendor. |
| cron `41 9 * * *` | 09:41 daily | `~/apps/check-hetzner-cx43.sh` — watch for a cheaper 8-vCPU Hetzner target. |

---

## On-login / one-shot launchd

| Name | Kind | What it is |
|---|---|---|
| `com.jay.ios-ship-now` | One-shot at login | GUI-session TestFlight ship (needs login keychain).  KeepAlive false.  Last exit **1** from the 2026-08-13 login run: `rcs st=1 ct=1 um=0 ul=0`.  Socratic archive failed (`Tab` iOS 18 APIs / type-check).  Congress dirty worktree.  Not a stale lock (`archive.lockdir` absent).  Later TF than 1.0.14 exists (local seq ST 65 / CT 66).  Do not re-fire from this job. |
| `com.jay.provider-knob-sync` | Scheduled (30 min) | `scripts/sync-provider-knobs.sh --apply`.  File still starts with a template XML comment so Python `plistlib` fails, but launchd accepted it.  **Not** always-on — `StartInterval=1800`, `RunAtLoad=false`. | **Loaded.**  116 runs, last exit 0 (in-sync / monitor-unreachable).  Do not invent a KeepAlive job.  Leftover: `SLACK_BOT_TOKEN` is stored in the LaunchAgent env (move to `~/.secrets/` later). |

Login items (Aqua, user apps — not agent-owned): Wallspace, GeminiAppLauncher, Devly, Kimi, Google Drive, Dockspace.

---

## On-demand helpers (able to be run; must not stay up)

These are the installed scripts agents actually invoke.  They are **not**
daemons.  If you add another one that other seats should use, list it here.
Worktree one-offs (`~/apps/congress-grok-*`, `trading-grok-*`) are **not**
listed — those die with the branch.

| Path | What it is |
|---|---|
| `~/apps/apple-notes-coding.sh` | Create/update/pin Coding notes. |
| `~/apps/agent-sync-poll.py` | One-pass #agent-sync read (session start). |
| `~/apps/agent-sync-websocket.py` | Local Slack post helper (needs slack_sdk). |
| `~/apps/agent-sync/consumer.mjs` | Slack Socket Mode consumer (session attach). |
| `~/apps/slack-sync.sh` | Bot-token Slack read/post without MCP. |
| `~/apps/mac-status.sh` | One-screen launchd + pm2 status. |
| `~/apps/cursor-slack-ws-sync.py` | Cursor #agent-sync Socket Mode inbox (also launchd). |
| `~/apps/imessage-grok-listen.py` | Grok iMessage group listener.  launchd disabled until FDA; Aqua orphan is the live process. |
| `~/apps/xcode-health/xcode-health-server.py` | xcode.jays.services health (also launchd). |
| `~/vision-worker/run-vision-worker.sh` | CT scanned-PTR vision worker (also launchd). |
| `~/vision-worker/worker.py` | Vision worker body. |
| `~/apps/ios-fleet/ship-testflight.sh` | Archive + upload one iOS app to TestFlight. |
| `~/apps/ios-fleet/ship-all.sh` | Sequential TestFlight ship for the fleet. |
| `~/apps/ios-fleet/ship-now-gui.sh` | GUI-session ship (same as the login LaunchAgent). |
| `~/apps/ios-fleet/asc-api.mjs` | App Store Connect API helper (JWT, no secret print). |
| `~/apps/ios-fleet/block-xcode-project-writes.py` | Guard against hand-editing `.pbxproj`. |
| `~/apps/ios-fleet/fix-runner-aqua-session.sh` | Re-attach Mac Xcode runners to Aqua. |
| `~/apps/code-main-keeper.sh` | One-shot ff-only `~/Code/*` → origin/main. |
| `~/apps/code-main-keeper-daemon.sh` | Loop wrapper (meant to be the pm2 job). |
| `~/apps/check-hetzner-cx43.sh` | One-shot Hetzner type check (also cron). |
| `~/apps/mac-auto-cleanup.sh` | One-shot cleanup (also 03:00 LaunchAgent). |
| `~/.claude-disk-janitor/janitor.sh` | Disk janitor body (also launchd every 30 min). |
| `~/.claude-merge-shepherd/run.sh` | Merge-shepherd body (also launchd every 30 min). |
| `~/Code/Usage-Monitor/scripts/ops/mac-server-watchdog.sh` | Mac heartbeat (also launchd every 120 s). |
| `~/Code/Usage-Monitor/scripts/antigravity-usage-collector.mjs` | AG quota collector (also launchd every 4 h). |
| `~/Code/Socratic.Trade/scripts/sync-provider-knobs.sh` | Provider-knob sync.  launchd job is scheduled every 30 min (template comment still breaks `plistlib`). |
| `~/apps/codex-coordination-audit.py` | Audit/bootstrap Codex coordination wiring. |
| `~/Code/Congress.Trade/scout/run-scout.sh` | Senate/House scout (also pm2). |
| `~/Code/Congress.Trade/scout/run-senate-relay.sh` | Senate relay (also pm2). |
| `~/Code/Congress.Trade/scout/run-senate-tunnel.sh` | Senate tunnel (also pm2). |
| `~/apps/agent-sync-push/start.sh` | #agent-sync relay (also pm2). |
| `~/apps/mcp-servers/*-launch.sh` | Per-session MCP launchers.  Die with the parent. |
| `~/apps/congress-publish.sh` | **Stale** — still SSHes the decommissioned Oracle box.  Do not run.  Use Coolify / `app/scripts/ship.sh`. |
| `~/apps/socratic-publish.sh` | **Stale** — Oracle.  Do not run. |
| `~/apps/trading-publish.sh` | **Stale** — Oracle.  Do not run. |
| `~/apps/usage-publish.sh` | **Stale** — Oracle.  Do not run. |
| `~/apps/sync-post-pr-626.py` | One-off leftover.  Do not run. |

## Vendor / login-item (not agent-owned)

Always-on or scheduled, but agents did not install them.  Do not kill or
"clean up" these.

| Name | Kind | What it is |
|---|---|---|
| Wallspace, GeminiAppLauncher, Devly, Kimi, Google Drive, Dockspace | Login item | Aqua apps. |
| `io.tailscale.ipn.macsys.login-item-helper` | Always-on | Tailscale. |
| `com.macpaw.CleanMyMac5.{Menu,HealthMonitor,Updater}` | Always-on / scheduled | CleanMyMac. |
| `com.microsoft.update.agent` | Scheduled | Microsoft updater. |
| `com.anthropic.claudefordesktop.ShipIt` | Scheduled | Claude Desktop updater. |
| `com.fiplab.mc3loginhelper` | Always-on | Memory Clean login helper. |
| `com.github.domt4.homebrew-autoupdate` | Scheduled | Homebrew autoupdate (also listed above). |
| `com.google.GoogleUpdater.wake` | Scheduled | Google updater (also listed above). |

---

## Retired / not loaded

| Item | State |
|---|---|
| `~/apps/com.jay.code-main-keeper.plist` | Template on disk; **not** in LaunchAgents.  Sibling `*.retired-launchd`. |
| `com.jay.shellular` | launchd **disabled** 2026-08-12.  Replaced by pm2 + `~/apps/shellular-runtime`. |
| `actions.runner…trading-live-mac` | Old Mac CI label.  Still in disabled-list as enabled-but-unused.  **Banned** for GitHub Actions jobs. |

---

## Not in this list (on purpose)

- Interactive `grok` / `claude` / `codex` / `cursor` terminals
- Per-session MCP children (`npm exec` MCP servers).  Those die with the parent.
  Orphans with `ppid=1` are leaks — kill those, not KeepAlive jobs.
- Coolify / Hetzner app containers
- iOS Simulator
- Apple system LaunchAgents

---

## How to add a row

1. Prefer `~/Library/LaunchAgents/com.jay.<name>.plist` or a `~/apps/<tool>-runtime` + pm2 job.
2. Label, program path, KeepAlive / interval, log path, one-line purpose, Kind.
3. Never put secrets in the plist.  Inject via Infisical or `~/.secrets/` at runtime, value-blind.
4. Update **this file first**, then `--update` the Apple Note, then the coordinator repo mirror.
5. Do not duplicate the full table into every app's AGENTS.md — point here.

```bash
launchctl print gui/$(id -u)/<Label>
launchctl kickstart -k gui/$(id -u)/<Label>
launchctl bootout gui/$(id -u)/<Label>
pm2 status
bash ~/apps/mac-status.sh
```
