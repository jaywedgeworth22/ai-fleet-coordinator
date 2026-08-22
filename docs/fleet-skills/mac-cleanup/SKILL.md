---
name: mac-cleanup
description: Optimize Mac workstation disk space by cleaning Xcode symbols, unavailable simulators, and package caches. Worktree retirement stays with disk-janitor. Use when checking disk health or regenerable caches.
---

# Mac Disk Cleanup Skill (ALL AGENTS)

Regenerable Mac caches and aged transcripts only.  Worktree retirement is `scripts/disk-janitor.sh` (idle + clean + KEEP_RE).  Do not wipe live checkouts.  Do not SSH Coolify from this job.

## How to Run the Cleanup

### 1. Direct Command (All Platforms)
Any agent (Antigravity, Grok, Claude, Cursor, Codex) or operator can execute the unified cleanup script directly:

```bash
bash /Users/jay/apps/mac-auto-cleanup.sh
```

Or using the CLI shortcut (available in `zsh` and `bash`):
```bash
mac-auto-cleanup
```

After changing the tracked copy: `cp scripts/mac-auto-cleanup.sh ~/apps/mac-auto-cleanup.sh && chmod +x ~/apps/mac-auto-cleanup.sh`.

### 2. What It Cleans (Safe & Idempotent)

1. **Xcode Developer Caches**:
   - Cleans `~/Library/Developer/Xcode/iOS DeviceSupport` symbols.
   - Cleans `~/Library/Developer/Xcode/DerivedData` build caches.
   - Prunes unavailable simulators only (`xcrun simctl delete unavailable`).  Does not wipe `CoreSimulator/Devices`.
2. **Package Manager Caches**:
   - `npm cache clean --force` and `~/.npm/_npx`
   - `pnpm store prune`
   - `yarn cache clean`
   - `brew cleanup -s`
3. **Spotlight PipelineStorage Journals**:
   - Truncates oversized Apple Intelligence / CoreSpotlight `PipelineStorage` journals.
4. **Agent Session Transcripts**:
   - Prunes Grok session transcripts older than 7 days (`~/.grok/sessions`).
   - Prunes old Codex archived sessions (`~/.codex/archived_sessions`).
   - Prunes old Antigravity brain conversation folders older than 7 days (`~/.gemini/antigravity/brain`).
5. **Not this script**:
   - Live git worktrees, `~/.grok/worktrees`, `~/.claude/worktrees`, or `~/apps` standing lanes.  That is disk-janitor.
   - Coolify / Hetzner Docker.  Host cron and `box-disk-hygiene.sh` (no volume prune).

## Scheduled Automation
- **Mac LaunchAgent**: `~/Library/LaunchAgents/com.jay.mac-cleanup.plist` runs automatically every 4 hours (`StartInterval: 14400`).
- **Disk janitor**: `com.jay.disk-janitor` every 30 min owns idle/clean worktree retirement.

## Quick Status Check
To view live disk space and system process health:
```bash
ms
# or
bash ~/apps/mac-status.sh
```
