# Status

Updated: 2026-08-22 (CURSOR — agent config Google Drive mirror)

## 2026-08-22 CURSOR — mirror fleet agent skills to Google Drive

Google Drive desktop cannot sync `~/.Gemini` / `~/.cursor` / `~/.claude` / `~/.grok`
natively.  Added `scripts/sync-fleet-agent-config-to-gdrive.py` and extended the daily
`com.jay.fleet-gdrive-backup` runner to refresh `My Drive/fleet-agent-config/` and
`My Drive/fleet-skills/`.  Live copy `~/apps/fleet-gdrive-backup/`.  Branch
`cursor/agent-config-gdrive-sync`.

Updated: 2026-08-22 (GROK — owner-facing times are Central Time)

## 2026-08-22 GROK — tell the owner times in Central, never UTC-only

Owner: always say Central Time when telling him a time.  AGENT-SYNC /
FLEET-UI-COPY / owner-copy / onboarding strengthened.  `00:00 UTC` is 7:00 PM
CT the previous calendar day in CDT.  Board `4289393c`.  Branch
`grok/owner-times-ct`.

Updated: 2026-08-22 (GROK — disk prune + Kimi salvage)

## 2026-08-22 GROK — Mac disk prune, Kimi salvage, janitor coverage

Owner: more disk, old worktrees any app, heavy Kimi prune, extract 1–2wk leftovers, Mac+Hetzner health.  Janitor now covers all fleet Code repos.  Salvage in `~/apps/KIMI-SALVAGE-2026-08-22/`.  ST #3044 kept open.  Board `a4417d6f`.  Branch `grok/disk-prune-kimi`.

Updated: 2026-08-22 (GROK — board.jays.services redirect)

## 2026-08-22 GROK — board.jays.services → /board

Cloudflare Single Redirect 302 + proxied `AAAA 100::`.  Canonical URL stays `https://mac.jays.services/board`.  Short link `https://board.jays.services`.  Board `b89c8330`.  Branch `grok/board-redirect`.

Updated: 2026-08-21 (GROK — iOS Debug vs TestFlight)

## 2026-08-21 GROK — iOS Debug vs TestFlight

Owner: do Xcode-console debug autonomously.  Helper `~/apps/ios-fleet/ios-debug.sh`.  Policy in AGENT-SYNC § iOS agent build loop.  Board `cbc1edeb`.  Branch `grok/ios-device-debug`.

Updated: 2026-08-21 (GROK — grok-leader lock-held restart storm)

## 2026-08-21 GROK — grok-leader lock-held restart storm

`ms` grok-leader `errored` 355 restarts: this TUI holds `~/.grok/leader.sock`.
Watch skip used bare `lsof`; launchd PATH omitted `/usr/sbin`.  Stopped the
job.  Watch + plist PATH + `leader.sh` exit 75.  ios-ship-now exit-1 is the
2026-08-13 login leftover.  Board `0095ae36`.  Branch `grok/leader-lock`.

Updated: 2026-08-21 (GROK — Mac + Hetzner recovery)

## 2026-08-21 GROK — Mac + Hetzner recovery

Watch: jlist-timeout dump-safe restore; HTTP /health bounce; Shellular ioreg/Connected.  Host: `fleet-health-recover@socratic-app` and `@usage-monitor` active; verify cron Pushover.  Branch `grok/mac-hetzner-recovery`.  Board `21c68868`.

Updated: 2026-08-21 (GROK — Apple Notes HTML sentence gap)

## 2026-08-21 GROK — Apple Notes HTML sentence gap

Notes.app collapses two ASCII spaces.  `--html` bodies must use `Sentence.&nbsp; Next`.  Helper converts leftover `.  ` / `!  ` / `?  ` (not inside code/pre).  Branch `grok/notes-html-nbsp`.

Updated: 2026-08-21 (GROK — Apple Notes section spacing)

## 2026-08-21 GROK — Apple Notes section spacing

Helper MD converter was dropping blank lines, so Coding notes looked packed.  Now emits `<div><br></div>` between sections and bullets.  Prefer `--html` with explicit spacers.  Live copy `~/apps/apple-notes-coding.sh`.  Branch `grok/notes-section-spacing`.

Live fleet-infra board: `~/apps/FLEET-INFRA-EFFORT-LOG.md`.  Repo mirror: `docs/EFFORT-LOG.md`.

## 2026-08-20 GROK — Monet Desktop fleet-skills pack

Rewrote `~/Desktop/fleet-skills` for the MONET Claude.app library and landed a
git copy at `docs/fleet-skills/`.  Five original skills are fleet-wide (current
Hetzner Coolify UUIDs, THE BOARD, secret grep trap).  Added session-start,
board-ops, closeout, secret-handoff, apple-notes, owner-copy, ios-ship.
Owner still uploads on the MONET login.  Board `f78464cb`.  Rollout:
`docs/rollouts/2026-08-20-monet-fleet-skills.md`.

## 2026-08-20 CURSOR — Cross-app coordination follow-ups (pointer)

Socratic.Trade audit #2802 follow-ups are in ST PR #2941, Congress.Trade #2064, Usage-Monitor #1245.  Pins still CTS v2.5.2.  Pin-check is fail-closed but not a required merge check.  DealDex stays protocol-only / Vercel.
