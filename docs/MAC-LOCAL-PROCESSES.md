# Mac local processes (owner machine)

**This is the master list.**  Every always-on job, scheduled job, login item,
and installed helper script that agents create on Jay's Mac lives here.
Not Coolify.  Not GitHub-hosted runners.  Not a one-shot `npm exec` from an
interactive session.

- Live: `/Users/jay/apps/MAC-LOCAL-PROCESSES.md`
- GitHub: https://github.com/jaywedgeworth22/ai-fleet-coordinator/blob/main/docs/MAC-LOCAL-PROCESSES.md
- Apple Note: `⭐️ Background Jobs Master List` (Coding, pinned; owner-renamed 2026-08-16)
- Binding rule: `/Users/jay/apps/AGENT-SYNC.md` § Mac local processes

Last inventory: Sat, Aug 22, 2026 ~6:25am CT (Grok).  Disk janitor now walks all fleet Code repos (was ST/CT/CTS only), protects unsuffixed standing lanes + runtimes, reaps clean kimi-named / nested / `/tmp` trees, and uses 2-day idle when free < 50G.  Live `~/.claude-disk-janitor/janitor.sh`; tracked `scripts/disk-janitor.sh`.  `mac-collab-writeback` is in the ecosystem (15 pm2 apps) and watch expected list.  Hardened after the first-run loop (updated_at from sync POSTs → gh close/reopen of ~1700 issues/cycle; lossy md re-render).  Writeback now bootstraps an applied-status map, edits live logs surgically, uses REST + current-state check for Issues, and does not git-commit `~/Code/<repo>`.  Tracked copies: `ai-fleet-coordinator/scripts/mac-process-watch.sh` + `scripts/pm2-ecosystem.config.cjs` + `scripts/mac-collab/write_back.py` + `scripts/grok-leader.sh` + `scripts/mac-status.sh` + `scripts/disk-janitor.sh`.  Command of record: `bash ~/apps/mac-status.sh`.
**pm2 `grok-leader`** is the shared Grok backend (`~/.grok/leader.sock`).  **pm2 `grok-acp`** is
`127.0.0.1:12419` for Conductor new sessions (`--no-leader serve` — `--leader serve`
does not bind).  Shellular Grok + new TUI join the leader.  List/load:
`python3 ~/apps/grok-acp-runtime/leader-client.py list`.
Slack inbox is multi-seat (`com.jay.slack-agent-inbox`).
Scout uses local `http://127.0.0.1:8899/fetch-ptr` (same session as
production).  `com.PM2` re-bootstrapped.  Claude remote-control up.
Ecosystem: `~/apps/pm2-ecosystem.config.cjs`.  Status: `bash ~/apps/mac-status.sh`.
Down/restart log: `~/Library/Logs/mac-process-watch.log`.  Watch times out `pm2 jlist` at 8s (wedged RPC used to hang the whole 120s loop), resurrects God if needed, and kills Shellular if the process is up but the cloud relay is dead (1006 / handshake).  Also expects `grok-leader` + `mac-collab` + `mac-collab-sync`.  When 3+ jobs are missing, watch **resurrects only if the dump still lists the expected names**; a one-job leftover dump is treated as poison and watch runs `pm2 start ~/apps/pm2-ecosystem.config.cjs` then `pm2 save`.  Watch restarts
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

## Fleet recovery lessons (read before touching pm2)

Written after the **2026-08-21 total-degradation incident** (Grok restore, Claude
root-cause).  The Mac did **not** run out of disk (~108GB free) — it ran out of CPU
and RAM on a 16GB box, and then a poisoned pm2 dump kept the fleet from coming back.

**Memory, not disk, is what takes this box down.**  Load hit ~800 with swap at
12.4GB/14.3GB and ~400k pageouts.  `JetsamEvent-2026-08-21-021055` shows the memory
killer firing with Cursor Helper Renderer as the largest process, alongside
`shutdown_stall_2026-08-21-020046` and two dirty reboots (01:58, 02:04) with no
`.panic` file.  Under that pressure every stdio MCP server times out at 30s, the pm2
God RPC wedges, and jobs crash-loop — none of which is the individual job's fault.
Check `sysctl vm.swapusage` and `uptime` **before** debugging any single service.

**`pm2 kill` and `pm2 save` write the LIVE list over `~/.pm2/dump.pm2`.**  If the live
list is a subset, the dump is poisoned and `pm2 resurrect` can never restore the rest.
That is what happened: a DeepSeek `dsh`/`npx` session in `~/Code/Congress.Trade` started
a fresh God holding only `vision-worker` at 00:35, and the 01:05 and 01:40 kills wrote
that one-job list over the dump.  **Never `pm2 save` unless `pm2 list` shows the full 14
jobs**, and never save from a one-off `npx`/`dsh` session.  The previous good list
survives in `~/.pm2/dump.pm2.bak` — copy it aside before any pm2 surgery
(`~/.pm2/dump.pm2.golden-14apps.20260821` is the 2026-08-21 snapshot).

**`pm2 start` does NOT re-read `env` from the ecosystem file.**  pm2 caches an app's
environment on first start and replays it forever.  On 2026-08-21 Shellular crash-looped
on `/bin/sh: ioreg: command not found` — `node-machine-id` shells out to
`ioreg -rd1 -c IOPlatformExpertDevice` — because the cached PATH had no `/usr/sbin`,
even though `pm2-ecosystem.config.cjs` sets `/usr/sbin:/sbin` correctly.  Editing the
config alone changes nothing.  Use `pm2 restart <app> --update-env`, or
`pm2 delete <app> && pm2 start "$ECOSYSTEM" --only <app>`.  Verify against the LIVE env,
never the file: `pm2 jlist` → `pm2_env.env.PATH`.

**Two pm2 installs shadow each other.**  `/usr/local/bin/pm2` (7.0.1, node 24) precedes
`/opt/homebrew/bin/pm2` (7.0.3, node 26) on PATH, which yields "In-memory PM2 is
out-of-date" and a CLI that cannot drive the running God.  Prefer the explicit
`/opt/homebrew/bin/pm2`, or run `pm2 update` — but note `pm2 update` restarts every job
from the CURRENT dump, so confirm the dump is not poisoned first.

**`mac-process-watch.sh` cannot recover a poisoned dump.**  When 3+ jobs are missing it
runs `pm2 resurrect` only, and never falls through to
`pm2 start "$ECOSYSTEM" --only <name>` the way the one/two-missing path does.  Combined
with the 4-restarts/hour backoff, the watch then stops even attempting the useless
resurrect — which is why nothing self-healed overnight.  **Open follow-up:** make the
bulk path verify the expected names actually came back and start any stragglers from the
ecosystem file, and skip dump-on-kill when the live list is a subset.

**All 15 jobs are already in `~/apps/pm2-ecosystem.config.cjs`**, `mac-collab-sync`
and `mac-collab-writeback` included — so recovery never needs a hand-rolled
`pm2 start`.  Restore with `pm2 start ~/apps/pm2-ecosystem.config.cjs` and only
then `pm2 save`.

**`grok-leader` vs a live Grok TUI:** if `/usr/sbin/lsof ~/.grok/leader.sock` shows a `grok-*` TUI holding the socket, **`pm2 stop grok-leader`** (not `pm2 kill`).  `mac-process-watch` skips restart while that socket is bound (`SKIP pm2:grok-leader lock-held`) and `pm2 stop`s an `errored` storm.  Bare `lsof` is a no-op when PATH lacks `/usr/sbin` (LaunchAgent 2026-08-21: 355 restarts).  `leader.sh` exits 75 when the lock is held; ecosystem `stop_exit_codes: [75]`.  Leaving the pm2 job `errored` burns CPU on a restart storm.  Start pm2 `grok-leader` again only after the TUI exits and the socket is free.  Do not `pm2 kill` the whole daemon to "fix" a lock conflict.

**`~/.pm2/pm2.log` grows unbounded** — it reached **230MB** by 2026-08-21, which makes
every read of it slow.  Read it with `grep -a … | tail`, and rotate it when it gets big.

**Agent worktrees belong in `~/apps/*`, never `~/Code/*`.**  `code-main-keeper` (pm2,
every ~60s) deliberately returns every top-level `~/Code/*` checkout to `origin/main` —
those trees are the human review / integration base, so "open in Xcode" always builds
the landed product.  On a non-main branch with a clean tree it soft-checkouts main and
fast-forwards.  It is safe by design (never hard-resets, never force-checkouts, never
discards commits absent from `origin/main`), but a worktree created at
`~/Code/<repo>-<seat>` jumps back to main the moment your tree goes clean, which reads
exactly like lost work if you have not pushed yet.  Push early, and put the worktree
under `~/apps/`.

---

## Always-on (supposed to stay up)

Live-checked Fri, Aug 21, 2026 ~2:25am CT.

| Name | Kind | What it is | Live now |
|---|---|---|---|
| `com.jay.claude-remote-control` | Always-on | Phone / claude.ai steering.  Monet / Renoir / Claude all look like `claude`.  Do not SIGKILL because you see no TTY. | **Up** (pid 3077) |
| **pm2 `agy-acp`** | Always-on | Antigravity ACP on `127.0.0.1:8765` (loopback bind persisted by `bind-loopback.cjs` via `node -r`, not a `node_modules` edit).  `start.sh` child is `agy-acp-turbo.sh` (same turbo policy as Shellular).  Disconnect grace is 300s, not 7 days.  Public `acp.jays.services` is WAF-blocked (Access is not enabled on the Usage.Jays.Services account).  Phone/Conductor uses Shellular, not this hostname. | **Up** |
| **pm2 `grok-leader`** | Always-on when socket free | Shared Grok backend.  `~/.grok/bin/grok agent --always-approve leader --no-exit-on-disconnect`.  Socket `~/.grok/leader.sock`.  Shellular and new TUI (`[cli] use_leader = true`) attach here so a phone/bot can `session/list` + `session/load` local chats.  Added 2026-08-18.  `leader.sh` exits 75 when the socket is already bound; ecosystem `stop_exit_codes: [75]`. | **Stopped 2026-08-21 18:11 CT** — this TUI (pid 12360) spawned leader pid 76260 at 15:43.  355 restarts then `errored` because watch lock-held used bare `lsof` and launchd PATH had no `/usr/sbin`.  `pm2 stop grok-leader`.  Watch now uses `/usr/sbin/lsof`.  `pm2 start grok-leader` after TUI exits. |
| **pm2 `grok-acp`** | Always-on | Grok ACP WebSocket on `127.0.0.1:12419` (`/ws`).  Pinned `~/apps/grok-acp-runtime`.  Native `~/.grok/bin/grok agent --always-approve --no-leader serve`.  **Never bind `:2419`**.  `--leader serve` does not listen — use `grok-leader` + `leader-client.py` to control existing chats.  Token in `~/.secrets/grok-acp.env` (never print).  Added 2026-08-18. | **Up** |
| **pm2 `xcode-health`** | Always-on | `127.0.0.1:8791`.  Public `xcode.jays.services`.  Moved off launchd 2026-08-16.  **Orphan-holds-port self-heal (2026-08-21, Cursor):** `_bind_or_reclaim()` matches mac-collab — on `EADDRINUSE` SIGTERM a holder only when it is another `xcode-health-server.py` that fails an 8s `/health` probe (SIGKILL after 15s); a healthy sibling or any other process is left alone and the start exits 3.  The 2026-08-21 degradation had this job at 2678 restarts against an orphan that was still serving 200. | **Up** — `/health` 200 (pm2-owned) |
| **pm2 `mac-collab`** | Always-on | `127.0.0.1:8792`.  Public `mac.jays.services` (THE BOARD + markdown `/files`).  Token `~/.secrets/mac-collab.env`.  **Does not serve `global-api-keys`.** Names-only: `GET /files/key-names`. Timing-safe compare + 401 rate limit. `board show/status` accepts unique 8-char id prefixes. Live `~/apps/MAC-LOCAL-PROCESSES.md` on the allowlist. Autorotate board synced. | **Up** — `/health` 200 (orphan held `:8792` twice on 2026-08-20: 1:09am, and 19:50-22:06 which crash-looped pm2 ~24k times into a 28MB error log; rotated to `mac-collab-error.log.20260820-eaddrinuse-loop.gz`) |
| **pm2 `mac-collab-sync`** | Always-on | Board reconciler (effort logs + GitHub issues → mac-collab).  Not the HTTP server.  Also snapshots `~/apps/mac-collab/findings.db` to `~/apps/mac-collab/backups/findings-YYYYMMDD.db` (14-day keep).  Runs can overlap: seen 2 concurrent on 2026-08-20 because `gh issue list` calls were hitting their 60s timeout (`network is unreachable`) and a run outlived the interval.  Not the cause of that day's outage, but it doubles the POST load on the board server. | **Up** |
| **pm2 `mac-collab-writeback`** | Always-on | **Reverse-sync: board writes → live effort-log files + GitHub Issues.**  Surgical bullet moves in `~/apps/*-EFFORT-LOG.md`; REST close/reopen of Issues only when GH state differs.  Does **not** git-commit `~/Code/<repo>` (branch protection; Code trees are the integration base).  Trigger is an applied-status map plus `updated_at` (server no longer bumps `updated_at` on no-op sync POSTs).  First pass bootstraps the map and writes nothing.  Grace: stamps `writeback_at`; sync omits `status` for 15 min (effort-row **and** github-issue).  Cursor: `~/apps/mac-collab/writeback_cursor.json`.  Script: `~/apps/mac-collab/write_back.py --loop`.  In ecosystem (Grok 2026-08-22).  Added 2026-08-22 (AG); hardened 2026-08-22 (Grok) after a first-run loop closed/reopened ~1700 issues per cycle. | **Up** after harden restart |
| **pm2 `vision-worker`** | Always-on | CT scanned-PTR worker.  Moved off launchd 2026-08-16.  Grok CLI solo pass first (`--cwd grok-cwd`, medium effort, JSON schema, turns scaled 4+2*pages); on miss cascade Qwen3-VL 8B/30B (page images) then Gemini 3.7 Flash then grok-4.5.  Env `OPENROUTER_CASCADE_MODELS`.  Scripts `~/vision-worker/{worker.py,run-vision-worker.sh,grok-cwd/}`.  Hand-copied from #2165 (`70855495`) 2026-08-21 11:05pm CT.  `pm2 start ecosystem --only vision-worker`; exec cwd `~/vision-worker` (not the repo). | **Up** |
| **pm2 `cursor-slack-sync`** | Always-on | Cursor #agent-sync inbox.  Moved off launchd 2026-08-16. | **Up** — connected |
| `homebrew.mxcl.moshi-hook` | Always-on | Vendor/local hook server (`moshi-hook serve`). | **Up** (pid 1900) |
| `actions.runner…mac-xcode26-congress` | Always-on | GitHub Actions Mac runner for Congress.Trade. | **Up** (pid 1902) |
| `actions.runner…mac-xcode26-socratic` | Always-on | GitHub Actions Mac runner for Socratic.Trade. | **Up** (pid 1897) |
| `actions.runner…mac-xcode26-usage` | Always-on | GitHub Actions Mac runner for Usage-Monitor. | **Up** (pid 1878) |
| `com.cloudflare.cloudflared` | Always-on | System LaunchDaemon.  Named tunnel `Jay's Tunnel`.  Hosts scout / agent-sync / xcode.jays.services. | **Up** (pid 835, root).  Do not mint a TryCloudflare hostname.  Do not change `SENATE_RELAY_URL`. |
| `com.PM2` | Login one-shot | `pm2 resurrect` at login (`pm2.jay.plist`, `LaunchOnlyOnce`).  Logs: `~/Library/Logs/com.PM2.*.log`. | Re-bootstrapped Fri, Aug 21 2026.  `LaunchOnlyOnce` exits after resurrect and can drop out of `launchctl print` — that is expected.  Plist stays in LaunchAgents.  Do not invent a KeepAlive PM2 daemon. |
| **pm2 `shellular`** | Always-on | Phone → this Mac (Shellular).  Pinned install: `~/apps/shellular-runtime` (v0.0.52).  **Not** launchd — `com.jay.shellular` is **disabled**.  Grok Build spawn (`~/.shellular/agents.json`): `~/.grok/bin/grok agent --always-approve --leader stdio`.  `--always-approve` / `--leader` are `agent` flags — **never** after `stdio`. | **Up** |
| **pm2 `scout`** | Always-on | Senate/House scout on the Mac.  Wrapper `~/apps/scout-runtime/run-scout.sh` (Bearer `SENATE_RELAY_SECRET` for local `:8899`; Code checkout is on another branch and would 401).  Must start with stdin `/dev/null`.  Senate discovery uses local `SENATE_RELAY_URL=http://127.0.0.1:8899` (do not hairpin `scout.jays.services`). | **Up** |
| **pm2 `senate-relay`** | Always-on | Local Senate eFD relay (`127.0.0.1:8899`) for `scout.jays.services`. Live code: `~/apps/senate-relay-runtime` (not the `~/Code/Congress.Trade` checkout — `code-main-keeper` would wipe an overlay). POST `/fetch-ptr` and `/fetch-doc` require `Bearer $SENATE_RELAY_SECRET` (`SENATE_RELAY_REQUIRE=1`, live 2026-08-21 after CT #2152). `/health` stays public. | **Up** — local `/health` 200 |
| **pm2 `senate-tunnel`** | Always-on | Watcher only — does **not** run cloudflared.  Named tunnel `Jay's Tunnel` is the system cloudflared. | **Up** (watcher); public `https://scout.jays.services/health` 200 |
| **pm2 `agent-sync-push`** | Always-on | Slack Socket Mode fan-out + `POST /post` + authenticated WebSocket (same `AGENT_SYNC_POST_TOKEN`). | **Up** — `http://127.0.0.1:8787/health` 200 |
| **pm2 `code-main-keeper`** | Always-on | Keeps `~/Code/*` integration trees on `origin/main` (ff-only). | **Up** |
| `com.jay.slack-agent-inbox` | Always-on | Slack DM inbox for **any** agent seat (Grok / Claude / Codex / Cursor / Antigravity / Kimi).  Prefix or `/use`.  Start script sources `~/.secrets/agent-sync.env` (token not in the plist).  Replaces the Grok-only `slack-grok-listen.py` orphan. | **Up** (launchd KeepAlive, 2026-08-17) |
| `com.jay.imessage-grok` | Always-on (intended) | Grok inbox for iMessage group Grok - Socratic Trade.  Reads `chat.db`.  Plist now calls Xcode `Python.app` (not `/usr/bin/python3`). | launchd **disabled** (FDA).  Aqua orphan **Up** (pid 81696, `ppid=1`, this is the intended listener — do not kill as a leak).  launchd-spawned `Python.app` still gets `authorization denied` on `chat.db`.  Owner: System Settings → Privacy & Security → Full Disk Access → allow that `Python.app` for background, then `launchctl enable gui/501/com.jay.imessage-grok` and bootstrap.  Do not load until then (KeepAlive would crash-loop every 10s). |
| `com.jay.shellular` | Disabled | Old launchd wrapper (`npx shellular start`).  Disabled 2026-08-12.  Do not re-enable while pm2 owns it. | **Disabled** |
| `com.jay.agy-acp` / `com.jay.xcode-health` / `com.congress.trade.vision-worker` / `com.cursor.slack-sync` | Retired launchd | Replaced by the pm2 jobs of the same name.  Labels **disabled**.  Plists left on disk. | **Disabled** |

---

## Scheduled (fires, then exits)

| Name | Cadence | What it is |
|---|---|---|
| `com.jay.disk-janitor` | every 30 min | Regenerable-cache + idle-worktree cleanup when disk is tight.  Walks all fleet Code repos (2026-08-22).  Kimi-named / nested `.claude/worktrees` / `/tmp` scratch reaped when clean.  `STALE_DAYS=2` under 50G free.  Steal a run-lock older than 2h (a leftover lock had wedged every tick 2026-08-11..16). |
| `com.jay.merge-shepherd` | every 30 min | `gh pr update-branch` so bot merges still retrigger verify.  Same 2h stale-lock steal (wedged 2026-07-14..16). |
| `com.jay.mac-process-watch` | every 120 s | Always-on restarter + scheduled-timer keeper.  pm2 via `~/.pm2/pm2.pid` + `kill -0` (do not pgrep -f).  launchd always-on: bootstrap / kickstart.  Scheduled: bootstrap if not-loaded; **idle is OK**.  Never bootstrap `com.jay.ios-ship-now` or `com.PM2`.  Steals janitor/shepherd locks >2h.  Checks trigger script paths exist.  Backoff 4/hour.  `MAC_PROCESS_WATCH_RESTART=0` = log-only. |
| `com.jays.mac-server-watchdog` | every 120 s | Mac heartbeat → Usage Monitor + local self-heal. |
| `com.jays.antigravity-usage-collector` | every 4 h | Antigravity quota → Usage Monitor ingest (via Infisical). |
| `com.jays.codex-usage-collector` | every 15 min | Codex CLI session JSONL tokens → Usage Monitor ingest (estimated API-equivalent).  On-demand: `npm run codex:collect -- --dry-run`. |
| `com.jays.grok-usage-collector` | every 15 min | Grok Build `updates.jsonl` turn_completed tokens + costUsdTicks → Usage Monitor ingest (estimated API-equivalent).  On-demand: `npm run grok:collect -- --dry-run`. |
| `com.jays.copilot-usage-collector` | every 15 min | Copilot CLI `session-state/*/events.jsonl` shutdown modelMetrics tokens → Usage Monitor ingest (estimated API-equivalent).  On-demand: `npm run copilot:collect -- --dry-run`. |
| `com.jay.mac-cleanup` | every 4 h (14400s) | Safe developer cache, Xcode iOS DeviceSupport/DerivedData, unavailable simulators only (`simctl delete unavailable`), agent session prune, and remote Hetzner Coolify docker prune.  **Wipes `~/.npm/_npx`.**  Does **not** reap git worktrees or wipe `~/.grok/worktrees` — that is `com.jay.disk-janitor`. |
| `com.jay.fleet-gdrive-backup` | daily 06:00 local | Zip `~/Code` git repos to Google Drive `Website & App Source Backups - YYYY-MM-DD` **and** mirror fleet agent skills/rules into `My Drive/fleet-agent-config/` plus refresh `My Drive/fleet-skills/`.  List = `fleet-apps.json` plus extra Code checkouts (code-main-keeper skip list).  Live `~/apps/fleet-gdrive-backup/run.sh`.  Tracked `scripts/backup-fleet-to-gdrive.py` + `scripts/sync-fleet-agent-config-to-gdrive.py` + `scripts/launchd/com.jay.fleet-gdrive-backup.plist`.  GitHub 90-day artifacts: coordinator `.github/workflows/backup-repos.yml`.  **Scheduled, not always-on.** |
| `com.github.domt4.homebrew-autoupdate` | daily | Homebrew autoupdate.  Vendor. |
| `com.google.GoogleUpdater.wake` | hourly | Google updater wake.  Vendor. |
| `com.macpaw.CleanMyMac5.Updater` | every 6 h | CleanMyMac updater.  Vendor. |
| cron `41 9 * * *` | 09:41 daily | `~/apps/check-hetzner-cx43.sh` — cheaper 8-vCPU than live `159792099` (`cx43` / `nbg1-dc3`).  Does **not** HIT on cx43 itself (already running).  Old hel1 id `149429403` retired.  curl `--max-time 20`. |

---

## On-login / one-shot launchd

| Name | Kind | What it is |
|---|---|---|
| `com.jay.ios-ship-now` | One-shot at login | GUI-session TestFlight ship (needs login keychain).  KeepAlive false.  Last exit **1** from the 2026-08-13 login run: `rcs st=1 ct=1 um=0 ul=0`.  Socratic archive failed (`Tab` iOS 18 APIs / type-check).  Congress dirty worktree.  Not a stale lock (`archive.lockdir` absent).  Later TF than 1.0.14 exists (local seq ST 65 / CT 66).  Do not re-fire from this job. |
| `com.jay.provider-knob-sync` | Scheduled (30 min) | `~/apps/provider-knob-sync-start.sh` → `scripts/sync-provider-knobs.sh --apply`.  Slack token lives in `~/.secrets/provider-knob-sync.env` (not the LaunchAgent env).  **Not** always-on — `StartInterval=1800`, `RunAtLoad=false`.  Do not invent a KeepAlive job. |

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
| `~/apps/mac-status.sh` | One-screen pm2 + launchd + down-watch.  **This is the command.**  Run it as the alias **`ms`** (`.zshrc:29`) — the alias is how people actually find it.  Annotates TUI-held `leader.sock` and the `ios-ship-now` login leftover. |
| `~/Code/ai-fleet-coordinator/scripts/install-fleet-skills.py` | On-demand.  Installs fleet skills into `~/.gemini/skills`, `~/.cursor/skills`, `~/.claude/skills`, `~/.codex/skills`, and `~/.grok/skills`, specializing Slack tag / Notes name / branch prefix / worktree suffix per seat. |
| `~/apps/fleet-gdrive-backup/run.sh` | Also on-demand.  Same Drive backup as launchd `com.jay.fleet-gdrive-backup` (repo zips + agent-config mirror).  `--list` prints the repo set.  `--only Repo` zips one app.  Tracked `scripts/backup-fleet-to-gdrive.py` + `scripts/sync-fleet-agent-config-to-gdrive.py`. |
| `~/apps/cursor-mac-process-hook.sh` | On-demand.  Fast pm2 always-on check (8s cap, fail open, no secrets).  Cursor `sessionStart` user hook (`~/.cursor/hooks/mac-process-check.sh`) calls this and injects `additional_context` when jobs are down. |
| `~/apps/cursor-chat-surfaces/` | On-demand.  Grok Bot / Shellular Cursor → desktop Agents Window + iOS.  Grok Bot is already Cloud Agents (open Agents Window; Filter → Source → SDK if hidden).  Shellular id `cursor` is the cloud bridge (`session/list` = Cloud Agents, never execs `cursor-agent`).  id `cursor-local` is `cursor_acp_noauth_shim.py` wrapping `cursor-agent acp` (strips `authMethods` so iOS 0.0.43 does not show Authentication required).  Command: `~/apps/cursor-chat-surfaces/cursor-chat-surfaces status`.  Canonical: `docs/CURSOR-CHAT-SURFACES.md`.  Key: `CURSOR_SYNC_API_KEY` in `~/.secrets/global-api-keys`.  Do **not** add this to the 14 always-on pm2 jobs. |
| `~/apps/dsh-runtime/` | On-demand.  Pinned DeepSeek Harness (`@deepseek-ai/dsh`).  **Never `npx @deepseek-ai/dsh`** — that poisoned pm2.  `dsh.sh` is the CLI (`dsh web`).  `dsh-acp.sh` is Shellular id `deepseek` (ACP stdio; `dsh acp` is not a command).  Auth: `~/.dsh/.credentials.yaml`, not `agents.json`.  **Shellular iOS hang fix:** headless Harness defaults to `approval: ask` under `workspace-write`; phone clients cannot answer tool approvals.  `dsh-acp.sh` exports `DSH_PERMISSION_MODE=danger-full-access` (auto-approve, same posture as `agy-acp-turbo`).  Tracked bridge: `scripts/dsh-acp.py` + `scripts/dsh-acp.sh`. |
| `~/apps/cursor-chat-surfaces/cursor-machine-worker.sh` | On-demand.  `agent worker start --name jay-mac` so Cloud Agents can run tools on this Mac.  Only when `CURSOR_BRIDGE_ON_MAC=1`. |
| `~/apps/pm2-ecosystem.config.cjs` | pm2 definitions for the 14 always-on fleet jobs (incl. `mac-collab-sync`). |
| `~/apps/mac-process-watch.sh` | Scheduled down-watch + always-on restarter (also launchd).  Tracked copy: `ai-fleet-coordinator/scripts/mac-process-watch.sh`. |
| `~/apps/agy-acp-runtime` | Pinned `@rebornix/stdio-to-ws` for `agy-acp`.  Tracked `start.sh` + `bind-loopback.cjs` keep listen on `AGY_ACP_BIND` / `127.0.0.1` after `npm i`. |
| `~/apps/agy-acp-runtime/agy-acp-turbo.sh` | Turbo Antigravity ACP wrapper (`AGY_EXTRA_ARGS` + `--skip-naration`).  Both pipes: Shellular id `agy` (`~/.local/bin/agy-acp-turbo`) and pm2 `:8765` (`start.sh` child). |
| `~/apps/agy-acp-runtime/agy-acp-list-wrapper.sh` | Optional Shellular-only NDJSON proxy in front of turbo.  Advertises `sessionCapabilities.list` and answers `session/list` from `~/.gemini/antigravity-cli` files.  Does **not** replace `start.sh`.  Live `agents.json` stays on the Mac. |
| `~/apps/grok-acp-runtime` | Pinned Grok ACP adapter.  localhost `127.0.0.1:12419` only.  Never `:2419`. |
| `~/apps/grok-acp-runtime/leader.sh` | pm2 `grok-leader` entry.  Shared backend on `~/.grok/leader.sock`.  Exits 75 when the socket is already bound.  Tracked copy: `ai-fleet-coordinator/scripts/grok-leader.sh`. |
| `~/apps/grok-acp-runtime/leader-client.py` | `handshake` / `list` / `load` / `peek` / `prompt` over leader stdio (no extra packages).  Tracked `scripts/grok-acp-runtime/leader-client.py`. |
| `~/apps/grok-acp-runtime/grok-drive.py` | Friendly Grok Bot CLI: `list` (merges `active_sessions.json` `live=true`), `peek`, `prompt` (TUI), `new` (`:12419`). |
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
| `~/vision-worker/run-vision-worker.sh` | CT scanned-PTR vision worker (also launchd). |
| `~/vision-worker/worker.py` | Vision worker body.  **Hand-copied deploy** of `Congress.Trade/services/vision-worker/worker.py` — merging a PR does **not** ship it.  After any vision-worker PR merges: `cp` the repo file here, `python3 -m py_compile`, run `python3 -m unittest discover -s ~/vision-worker -p 'test_worker.py'`, then `pm2 restart vision-worker --update-env`.  Drifted 31 commits behind `main` on 2026-08-21 because this was undocumented. |
| `~/apps/ios-fleet/ios-debug.sh` | On-demand.  Xcode-console equivalent without opening Xcode: simulator `simctl launch --console` + `log stream`, or device `devicectl` launch / screenshot + `log collect`.  `--target device --install-debug` replaces TestFlight for that bundle.  `--logs-only` does not.  Tracked copy: `ai-fleet-coordinator/scripts/ios-debug.sh`.  Canonical: AGENT-SYNC § iOS agent build loop (2026-08-21). |
| `~/apps/ios-fleet/ship-testflight.sh` | Archive + upload one iOS app to TestFlight.  Consults `build-window.sh` and re-execs itself under `nice -n 10` when the answer is `background`.  Never blocked, only deprioritised.  `IOS_SHIP_RENICED` guards against a re-exec loop; `IOS_SHIP_PRIORITY=normal` forces full speed. |
| `~/apps/ios-fleet/build-window.sh` | On-demand.  Decides iOS ship PRIORITY on this shared Mac; prints `normal` or `background`, always exit 0.  **socratic**: prefers X:15-X:45 (strategy runs own X:00-X:15, X:45-X:00 is buffer), unrestricted 20:00-06:00 local.  **congress**: any time unless CT has a non-zero `ingestion_backlog` on its public health route.  Others unconstrained.  FAILS OPEN to `normal` on any error - a broken check must never degrade a ship.  Inherited by `ship-all.sh` and `ship-now-gui.sh` since both call `ship-testflight.sh`.  Tune with `IOS_SHIP_WINDOW_START_MIN` / `_END_MIN` / `IOS_SHIP_QUIET_START_HOUR` / `_END_HOUR`. |
| `~/apps/ios-fleet/ship-all.sh` | Sequential TestFlight ship for the fleet. |
| `~/apps/ios-fleet/ship-now-gui.sh` | GUI-session ship (same as the login LaunchAgent). |
| `~/apps/ios-fleet/asc-api.mjs` | App Store Connect API helper (JWT, no secret print). |
| `~/apps/ios-fleet/block-xcode-project-writes.py` | Guard against hand-editing `.pbxproj`. |
| `~/apps/ios-fleet/fix-runner-aqua-session.sh` | Re-attach Mac Xcode runners to Aqua. |
| `~/apps/code-main-keeper.sh` | One-shot ff-only `~/Code/*` → origin/main. |
| `~/apps/code-main-keeper-daemon.sh` | Loop wrapper (meant to be the pm2 job). |
| `~/apps/check-hetzner-cx43.sh` | Daily cheaper-8-vCPU watch for live host `159792099` (also cron). |
| `~/apps/mac-auto-cleanup.sh` | One-shot cleanup (also 03:00 LaunchAgent). |
| `~/.claude-disk-janitor/janitor.sh` | Disk janitor body (also launchd every 30 min).  Tracked copy `ai-fleet-coordinator/scripts/disk-janitor.sh`. |
| `~/.claude-merge-shepherd/run.sh` | Merge-shepherd body (also launchd every 30 min). |
| `~/Code/Usage-Monitor/scripts/ops/mac-server-watchdog.sh` | Mac heartbeat (also launchd every 120 s). |
| `~/Code/Usage-Monitor/scripts/antigravity-usage-collector.mjs` | AG quota collector (also launchd every 4 h). |
| `~/Code/Usage-Monitor/scripts/codex-usage-collector.mjs` | Codex session JSONL collector (also launchd every 15 min once bootstrapped). |
| `~/Code/Usage-Monitor/scripts/grok-usage-collector.mjs` | Grok Build updates.jsonl collector (also launchd every 15 min once bootstrapped). |
| `~/Code/Usage-Monitor/scripts/copilot-usage-collector.mjs` | Copilot CLI session JSONL collector (also launchd every 15 min once bootstrapped). |
| `~/Code/Socratic.Trade/scripts/sync-provider-knobs.sh` | Provider-knob sync.  launchd job is scheduled every 30 min (template comment still breaks `plistlib`). |
| `~/apps/codex-coordination-audit.py` | Audit/bootstrap Codex coordination wiring. |
| `~/apps/scout-runtime/run-scout.sh` | Live Mac scout wrapper. Sends Bearer to local senate-relay. State files stay in `~/Code/Congress.Trade/scout`. |
| `~/Code/Congress.Trade/scout/run-scout.sh` | Git copy in whatever checkout is there. Do not point pm2 at it while that tree is off main. |
| `~/Code/Congress.Trade/scout/run-senate-relay.sh` | Git copy. Live Mac origin is `~/apps/senate-relay-runtime/run.sh`. |
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

### pm2 orphan-holds-port recovery (2026-08-21, CLAUDE)

**Symptom.** One or more pm2 apps sit `errored` with a large `restart_time`, their
error log repeats `Address already in use` / `EADDRINUSE` / Deno `AddrInUse (os error 48)`,
and `pm2 jlist` / `pm2 restart` time out.

**Cause.** When the pm2 God daemon dies without reaping its children (memory pressure,
jetsam, a crash), the children are reparented to launchd and keep their listening socket.
The pm2-managed replacement can then never bind, so pm2 restart-loops it forever.  Nothing
inside that loop can clear the orphan.

**Recovery** (script: `~/apps/mac-collab/`-independent, see the CLAUDE rollout note):

1. `launchctl bootout gui/$(id -u)/com.jay.mac-process-watch` -- pause the watchdog so its
   own `pm2 resurrect` cannot race the repair.  **Re-arm it afterwards with `launchctl
   bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.jay.mac-process-watch.plist`.**
2. Record God's pid (`~/.pm2/pm2.pid`) and `pgrep -P <god>` BEFORE signalling anything --
   once the parent dies the survivors reparent and you lose the list.
3. `pm2 kill`, then SIGTERM (SIGKILL after ~6s) every recorded child plus every listener on
   a fleet port.  **Fleet ports: 8765 agy-acp, 8791 xcode-health, 8792 mac-collab,
   8899 senate-relay, 12419 grok-acp.**  Missing a port here is how senate-relay stayed
   broken through the first pass of this repair (238 restarts against an orphan deno on 8899).
4. `rm -f ~/.pm2/{rpc.sock,pub.sock,pm2.pid}` -- stale IPC is why a freshly started God
   still answers nothing.
5. `pm2 resurrect` (from `~/.pm2/dump.pm2`), then `pm2 jlist` to confirm 14/14 online.
6. `pm2 reset all` so the next crash-loop is visible against a zero baseline, then `pm2 save`.

**Do not** SIGKILL God first and sort it out afterwards -- that is precisely how the orphans
are created.
