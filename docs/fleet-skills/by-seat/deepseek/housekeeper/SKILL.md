---
name: housekeeper
description: Mac and Hetzner disk/RAM/CPU housekeeping. Run safe cleanup scripts, CleanMyMac CLI, and wake BotFleet Housekeeper on resource-threshold triggers. Use when disk is tight, swap is high, load is elevated, the owner asks to free space, or the Housekeeper / GB-HOUSEKEEPER role is on duty.
---

# Housekeeper (disk, RAM, CPU)

> **This install is for `DEEPSEEK`.** Slack `[DEEPSEEK]`.  Notes `DeepSeek`.  Branches `deepseek/`.  Worktrees `~/apps/<app>-deepseek`.  Do not inherit another seat's tag from a shared template.


Act on regenerable waste.  Do not only report.  Ask before deleting anything that `npm ci` / a rebuild cannot restore.

## Immediate commands

```bash
df -h / /System/Volumes/Data
sysctl vm.swapusage
uptime
bash /Users/jay/apps/mac-status.sh
python3 /Users/jay/apps/mac-resource-watch.py --once
```

Safe reclaim (idempotent):

```bash
bash /Users/jay/apps/mac-auto-cleanup.sh --pressure
bash /Users/jay/.claude-disk-janitor/janitor.sh
cleanmymac clean --force
cleanmymac optimize ram
```

`mac-auto-cleanup` already calls CleanMyMac when the CLI is on PATH.  Disk janitor owns idle/merged worktree retirement.  Never `rm -rf` `CoreSimulator/Devices`, never `simctl shutdown all`, never wipe `~/.grok/worktrees`.

## Thresholds that must wake this role

These are the live defaults for `com.jay.mac-resource-watch` (every 5 min):

| Signal | Wake when | Immediate action |
|---|---|---|
| Disk free | ≤ 80G warn, ≤ 50G critical | cleanup + janitor + CleanMyMac |
| Disk drop | ≥ 6G since last sample | same, even if still above 80G |
| Swap | used ≥ 80% or total ≥ 8G | `cleanmymac optimize ram` |
| Load 1m | ≥ 16 (optional, on by default) | report hogs; do not SIGKILL `com.jay.claude-remote-control` |

The watch runs the safe scripts itself, then POSTs BotFleet Housekeeper webhook `resource.disk` / `resource.ram` / `resource.cpu` / `resource.pressure`.  Cooldown 45 min.  Secret file `~/.secrets/botfleet-housekeeper-webhook.env` (never print).

## BotFleet Housekeeper

Bot id `d43849b8-5eeb-452b-ac4e-ed4724343838`.  Routines at 09:00 / 15:00 / 21:00 plus the resource webhook.  First-class resource triggers live on Automations → Resources (disk free, RAM/swap, optional CPU).  Local webhook receiver `127.0.0.1:8800`.  BotFleet server `127.0.0.1:8799`.

When this wake includes a resource payload: start with that pressure.  Re-run the playbook.  Report before/after disk, swap, load, and what was deleted.

Ask before: user Documents/photos, secrets, live dirty worktrees, CoreSimulator Devices, in-session `~/.grok/worktrees`, anything with `.janitor-keep`.  Do not persist TCPMSS.  Do not change sysctl or network settings.  Do not extra-ship.  Do not Slack unless kicking grok at a repo or after a completed app update.

## Grok Bot Housekeeper (`GB-HOUSEKEEPER`)

Cloud cannot `df` this Mac.  Drive the Mac instead:

```bash
# seat-mcp / grok-drive: inject into an idle Mac Grok TUI
python3 ~/apps/grok-acp-runtime/grok-drive.py --help
```

Or hop via `https://agents.jays.services/mcp` (`drive-grok-tui` skill) and inject:

`Run python3 /Users/jay/apps/mac-resource-watch.py --once then report disk free, swap, load, and what cleanup did.`

Do not skip that hop and invent a cloud-side `du`.

## Hetzner

If SSH `coolify` works: `/etc/cron.daily/coolify-auto-maintenance` (already called from `mac-auto-cleanup.sh`).  Do not treat Coolify API status as disk truth — `df` the host.
