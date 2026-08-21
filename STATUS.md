# Status

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
