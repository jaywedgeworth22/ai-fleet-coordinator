# Mac local processes (owner machine)

**This is the master list.**  Every always-on job, scheduled job, login item,
and installed helper script that agents create on Jay's Mac lives here.
Not Coolify.  Not GitHub-hosted runners.  Not a one-shot `npm exec` from an
interactive session.

- Live: `/Users/jay/apps/MAC-LOCAL-PROCESSES.md`
- GitHub: https://github.com/jaywedgeworth22/ai-fleet-coordinator/blob/main/docs/MAC-LOCAL-PROCESSES.md
- Apple Note: `⭐️ Background Jobs Master List` (Coding, pinned; owner-renamed 2026-08-16)
- Binding rule: `/Users/jay/apps/AGENT-SYNC.md` § Mac local processes

Last inventory: Tue, Aug 18, 2026 (Grok).  12 pm2 jobs online.  **pm2 `grok-leader`**
is the shared Grok backend (`~/.grok/leader.sock`).  **pm2 `grok-acp`** is
`127.0.0.1:12419` for Conductor new sessions (`--no-leader serve` — `--leader serve`
does not bind).  Shellular Grok + new TUI join the leader.  List/load:
`python3 ~/apps/grok-acp-runtime/leader-client.py list`.
Slack inbox is multi-seat (`com.jay.slack-agent-inbox`).
Scout uses local `http://127.0.0.1:8899/fetch-ptr` (same session as
production).  `com.PM2` re-bootstrapped.  Claude remote-control up.
Ecosystem: `~/apps/pm2-ecosystem.config.cjs`.  Status: `bash ~/apps/mac-status.sh`.
Down/restart log: `~/Library/Logs/mac-process-watch.log`.  Watch restarts
always-on jobs (pm2 resurrect / ecosystem start, launchd kickstart/bootstrap)
and keeps scheduled timers **loaded** (does not kickstart idle).  Steals
stale disk-janitor / merge-shepherd run-locks older than 2h.  4-per-hour
backoff.  `MAC_PROCESS_WATCH_RESTART=0` is log-only.

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

Live-checked Sun, Aug 16, 2026.

| Name | Kind | What it is | Live now |
|---|---|---|---|
| `com.jay.claude-remote-control` | Always-on | Phone / claude.ai steering.  Monet / Renoir / Claude all look like `claude`.  Do not SIGKILL because you see no TTY. | **Up** (pid 3077) |
| **pm2 `agy-acp`** | Always-on | Antigravity ACP on `:8765`.  Pinned `~/apps/agy-acp-runtime` (not npx).  Moved off launchd 2026-08-16. | **Up** |
| **pm2 `grok-leader`** | Always-on | Shared Grok backend.  `~/.grok/bin/grok agent --always-approve leader --no-exit-on-disconnect`.  Socket `~/.grok/leader.sock`.  Shellular and new TUI (`[cli] use_leader = true`) attach here so a phone/bot can `session/list` + `session/load` local chats.  Added 2026-08-18. | **Up** |
| **pm2 `grok-acp`** | Always-on | Grok ACP WebSocket on `127.0.0.1:12419` (`/ws`).  Pinned `~/apps/grok-acp-runtime`.  Native `~/.grok/bin/grok agent --always-approve --no-leader serve`.  **Never bind `:2419`**.  `--leader serve` does not listen — use `grok-leader` + `leader-client.py` to control existing chats.  Token in `~/.secrets/grok-acp.env` (never print).  Added 2026-08-18. | **Up** |
| **pm2 `xcode-health`** | Always-on | `127.0.0.1:8791`.  Public `xcode.jays.services`.  Moved off launchd 2026-08-16. | **Up** — `/health` 200 |
| **pm2 `mac-collab`** | Always-on | `127.0.0.1:8792`.  Public `mac.jays.services`.  `/health` and `/board` open (board is a static shell — no data — the JS on it prompts for the token); `/files`, `/files/<name>`, and all `/findings*` routes need `Authorization: Bearer $MAC_COLLAB_TOKEN` from `~/.secrets/mac-collab.env` (never print).  File allowlist: live `*-EFFORT-LOG.md`, protocol, AGENT-SYNC, MAC-LOCAL-PROCESSES.  **Shared findings tool (added 2026-08-19):** SQLite-backed `GET/POST /findings`, `GET/PATCH /findings/<id>`, `GET/POST /findings/<id>/comments` — any agent (including cloud agents with no Mac filesystem access) can list, file, mark addressed (`status`: open/in_progress/addressed/wontfix/duplicate), and comment on findings from a review.  Human/agent browser view at `/board` (filter by app/status/severity, inline status change + comment).  Findings DB: `~/apps/mac-collab/findings.db` (not git-tracked — Mac-local state).  Seeded 2026-08-19 with 467 Congress.Trade + 45 Socratic.Trade findings from that day's full-app reviews (`~/apps/mac-collab/import_ct_review.py` / `import_st_review.py`, re-runnable, idempotent on `external_uid`).  Effort-board rows point at the tool rather than duplicating detail; the existing one-way `docs/EFFORT-LOG.md` → GitHub Issues sync (unchanged) carries those rows into Issues as normal. | **Up** — `/health` 200 |
| **pm2 `vision-worker`** | Always-on | CT scanned-PTR worker.  Moved off launchd 2026-08-16. | **Up**.  Exhausted docs `H-2026-9116257/58` skipped after 3 `transcription_failed`. |
| **pm2 `cursor-slack-sync`** | Always-on | Cursor #agent-sync inbox.  Moved off launchd 2026-08-16. | **Up** — connected |
| `homebrew.mxcl.moshi-hook` | Always-on | Vendor/local hook server (`moshi-hook serve`). | **Up** (pid 1900) |
| `actions.runner…mac-xcode26-congress` | Always-on | GitHub Actions Mac runner for Congress.Trade. | **Up** (pid 1902) |
| `actions.runner…mac-xcode26-socratic` | Always-on | GitHub Actions Mac runner for Socratic.Trade. | **Up** (pid 1897) |
| `actions.runner…mac-xcode26-usage` | Always-on | GitHub Actions Mac runner for Usage-Monitor. | **Up** (pid 1878) |
| `com.cloudflare.cloudflared` | Always-on | System LaunchDaemon.  Named tunnel `Jay's Tunnel`.  Hosts scout / agent-sync / xcode / **mac.jays.services**.  Ingress v8. | **Up** (pid 835, root).  Do not mint a TryCloudflare hostname.  Do not change `SENATE_RELAY_URL`. |
| `com.PM2` | Login one-shot | `pm2 resurrect` at login (`pm2.jay.plist`, `LaunchOnlyOnce`).  Logs: `~/Library/Logs/com.PM2.*.log`. | **Loaded** 2026-08-16 (was missing from launchctl).  Exits after resurrect (expected). |
| **pm2 `shellular`** | Always-on | Phone → this Mac (Shellular).  Pinned install: `~/apps/shellular-runtime` (v0.0.52).  **Not** launchd — `com.jay.shellular` is **disabled**.  Grok Build spawn (`~/.shellular/agents.json`): `~/.grok/bin/grok agent --always-approve --leader stdio`.  `--always-approve` / `--leader` are `agent` flags — **never** after `stdio`. | **Up** |
| **pm2 `scout`** | Always-on | Senate/House scout on the Mac.  Must start with stdin `/dev/null` (`bash -lc 'exec …/run-scout.sh </dev/null'`).  Senate discovery uses local `SENATE_RELAY_URL=http://127.0.0.1:8899` (do not hairpin `scout.jays.services`).  A raw `pm2 start run-scout.sh --interpreter bash` hangs in bash `reader_loop` because pm2's unix-socket stdin breaks the secrets heredoc. | **Up** (restarted 2026-08-16 3:36pm CT onto local relay) |
| **pm2 `senate-relay`** | Always-on | Local Senate eFD relay (`127.0.0.1:8899`) for `scout.jays.services`. | **Up** — local `/health` 200 |
| **pm2 `senate-tunnel`** | Always-on | Watcher only — does **not** run cloudflared.  Named tunnel `Jay's Tunnel` is the system cloudflared. | **Up** (watcher); public `https://scout.jays.services/health` 200 |
| **pm2 `agent-sync-push`** | Always-on | Slack Socket Mode fan-out + `POST /post` for #agent-sync. | **Up** — `http://127.0.0.1:8787/health` 200 |
| **pm2 `code-main-keeper`** | Always-on | Keeps `~/Code/*` integration trees on `origin/main` (ff-only). | **Up** |
| `com.jay.slack-agent-inbox` | Always-on | Slack DM inbox for **any** agent seat (Grok / Claude / Codex / Cursor / Antigravity / Kimi).  Prefix or `/use`.  Start script sources `~/.secrets/agent-sync.env` (token not in the plist).  Replaces the Grok-only `slack-grok-listen.py` orphan. | **Up** (launchd KeepAlive, 2026-08-17) |
| `com.jay.imessage-grok` | Always-on (intended) | Grok inbox for iMessage group Grok - Socratic Trade.  Reads `chat.db`.  Plist now calls Xcode `Python.app` (not `/usr/bin/python3`). | launchd **disabled** (FDA).  Aqua orphan **Up** (pid 81696, `ppid=1`, this is the intended listener — do not kill as a leak).  launchd-spawned `Python.app` still gets `authorization denied` on `chat.db`.  Owner: System Settings → Privacy & Security → Full Disk Access → allow that `Python.app` for background, then `launchctl enable gui/501/com.jay.imessage-grok` and bootstrap.  Do not load until then (KeepAlive would crash-loop every 10s). |
| `com.jay.shellular` | Disabled | Old launchd wrapper (`npx shellular start`).  Disabled 2026-08-12.  Do not re-enable while pm2 owns it. | **Disabled** |
| `com.jay.agy-acp` / `com.jay.xcode-health` / `com.congress.trade.vision-worker` / `com.cursor.slack-sync` | Retired launchd | Replaced by the pm2 jobs of the same name.  Labels **disabled**.  Plists left on disk. | **Disabled** |

---

## Scheduled (fires, then exits)

| Name | Cadence | What it is |
|---|---|---|
| `com.jay.disk-janitor` | every 30 min | Regenerable-cache + idle-worktree cleanup when disk is tight.  Steal a run-lock older than 2h (a leftover lock had wedged every tick 2026-08-11..16). |
| `com.jay.merge-shepherd` | every 30 min | `gh pr update-branch` so bot merges still retrigger verify.  Same 2h stale-lock steal (wedged 2026-07-14..16). |
| `com.jay.mac-process-watch` | every 120 s | Always-on restarter + scheduled-timer keeper.  pm2 via `~/.pm2/pm2.pid` + `kill -0` (do not pgrep -f).  launchd always-on: bootstrap / kickstart.  Scheduled: bootstrap if not-loaded; **idle is OK**.  Never bootstrap `com.jay.ios-ship-now` or `com.PM2`.  Steals janitor/shepherd locks >2h.  Checks trigger script paths exist.  Backoff 4/hour.  `MAC_PROCESS_WATCH_RESTART=0` = log-only. |
| `com.jays.mac-server-watchdog` | every 120 s | Mac heartbeat → Usage Monitor + local self-heal. |
| `com.jays.antigravity-usage-collector` | every 4 h | Antigravity quota → Usage Monitor ingest (via Infisical). |
| `com.jay.mac-cleanup` | 03:00 daily | Broader cache / DerivedData / old session prune.  **Wipes `~/.npm/_npx`.** |
| `com.github.domt4.homebrew-autoupdate` | daily | Homebrew autoupdate.  Vendor. |
| `com.google.GoogleUpdater.wake` | hourly | Google updater wake.  Vendor. |
| `com.macpaw.CleanMyMac5.Updater` | every 6 h | CleanMyMac updater.  Vendor. |
| cron `41 9 * * *` | 09:41 daily | `~/apps/check-hetzner-cx43.sh` — cheaper 8-vCPU than live `159792099` (`cx43` / `nbg1-dc3`).  Does **not** HIT on cx43 itself (already running).  Old hel1 id `149429403` retired.  curl `--max-time 20`. |

---

## On-login / one-shot launchd

| Name | Kind | What it is |
|---|---|---|
| `com.jay.ios-ship-now` | One-shot at login | GUI-session TestFlight ship (needs login keychain).  KeepAlive false.  Last exit **1** from the 2026-08-13 login run: `rcs st=1 ct=1 um=0 ul=0`.  Socratic archive failed (`Tab` iOS 18 APIs / type-check).  Congress dirty worktree.  Not a stale lock (`archive.lockdir` absent).  Later TF than 1.0.14 exists (local seq ST 65 / CT 66).  Do not re-fire from this job. |
| `com.jay.provider-knob-sync` | Scheduled (30 min) | `scripts/sync-provider-knobs.sh --apply`.  File still starts with a template XML comment so Python `plistlib` fails, but launchd accepted it.  **Not** always-on — `StartInterval=1800`, `RunAtLoad=false`.  **Loaded:** 116 runs, last exit 0 (in-sync / monitor-unreachable).  Do not invent a KeepAlive job.  Leftover: `SLACK_BOT_TOKEN` is stored in the LaunchAgent env (move to `~/.secrets/` later). |

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
| `~/apps/mac-status.sh` | One-screen pm2 + launchd + down-watch.  **This is the command.** |
| `~/apps/pm2-ecosystem.config.cjs` | pm2 definitions for the 12 always-on fleet jobs. |
| `~/apps/mac-process-watch.sh` | Scheduled down-watch + always-on restarter (also launchd).  Tracked copy: `ai-fleet-coordinator/scripts/mac-process-watch.sh`. |
| `~/apps/agy-acp-runtime` | Pinned `@rebornix/stdio-to-ws` for `agy-acp`. |
| `~/apps/grok-acp-runtime` | Pinned Grok ACP adapter.  localhost `127.0.0.1:12419` only.  Never `:2419`. |
| `~/apps/grok-acp-runtime/leader.sh` | pm2 `grok-leader` entry.  Shared backend on `~/.grok/leader.sock`. |
| `~/apps/grok-acp-runtime/leader-client.py` | `handshake` / `list` / `load` over leader stdio (no extra packages). |
| `~/apps/grok-acp-runtime/start.sh` | pm2 `grok-acp` entry: `--no-leader serve --bind 127.0.0.1:12419`.  Sources `~/.secrets/grok-acp.env`. |
| `~/apps/grok-acp-runtime/acp-client.py` | Conductor WebSocket client for **new** sessions on `:12419`. |
| `~/apps/grok-acp-runtime/README.md` | Leader + Conductor + Shellular attach notes. |
| `~/apps/cursor-slack-ws-sync.py` | Cursor #agent-sync Socket Mode inbox (also launchd). |
| `~/apps/imessage-grok-listen.py` | Grok iMessage group listener.  launchd disabled until FDA; Aqua orphan is the live process. |
| `~/apps/slack-agent-listen.py` | Slack DM multi-seat inbox.  Also launchd `com.jay.slack-agent-inbox`. |
| `~/apps/slack-agent-listen-start.sh` | launchd entry: sources agent-sync.env, execs the inbox. |
| `~/apps/slack-grok-listen.py` | Wrapper that execs `slack-agent-listen.py` (old Grok-only name). |
| `~/apps/slack-agent-inbox.md` | How to DM any seat from Slack. |
| `~/apps/xcode-health/xcode-health-server.py` | xcode.jays.services health (also launchd). |
| `~/apps/mac-collab/mac-collab-server.py` | mac.jays.services collab reads (effort logs + protocol) + shared findings tool (`/findings`, `/board`). Token `~/.secrets/mac-collab.env`. SQLite: `~/apps/mac-collab/findings.db`. |
| `~/apps/mac-collab/import_ct_review.py`, `import_st_review.py` | One-off (re-runnable, idempotent) importers that POST a review's findings into the mac-collab findings tool. |
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
| `~/apps/check-hetzner-cx43.sh` | Daily cheaper-8-vCPU watch for live host `159792099` (also cron). |
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
