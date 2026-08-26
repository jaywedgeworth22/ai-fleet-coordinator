#!/bin/bash
# Mac Automated Maintenance Script
# Safely prunes developer caches, Xcode symbols, unavailable simulators,
# package manager caches, old agent logs, and triggers remote Hetzner Docker cleanup.
# Does not reap git worktrees or live ~/.grok/worktrees (disk-janitor owns that).

set -u

echo "[$(date)] Starting Mac automated cleanup..."

# 1. Clean Xcode iOS DeviceSupport symbols, DerivedData, and Simulator Devices
if [ -d "$HOME/Library/Developer/Xcode/iOS DeviceSupport" ]; then
    echo "Pruning Xcode iOS DeviceSupport..."
    rm -rf "$HOME/Library/Developer/Xcode/iOS DeviceSupport"/* 2>/dev/null || true
fi

if [ -d "$HOME/Library/Developer/Xcode/DerivedData" ]; then
    echo "Pruning Xcode DerivedData..."
    rm -rf "$HOME/Library/Developer/Xcode/DerivedData"/* 2>/dev/null || true
fi

if [ -d "$HOME/Library/Developer/CoreSimulator/Caches" ]; then
    echo "Pruning CoreSimulator Caches..."
    rm -rf "$HOME/Library/Developer/CoreSimulator/Caches"/* 2>/dev/null || true
fi

# Never rm -rf Devices/*.  That deletes every simulator (installed apps,
# container data, in-progress ios-debug / TestFlight archives).  2026-08-12
# left CoreSimulator live because iOS needs it.  Only drop unavailable runtimes.
if command -v xcrun &>/dev/null; then
    echo "Pruning unavailable simulators..."
    xcrun simctl shutdown all 2>/dev/null || true
    xcrun simctl delete unavailable 2>/dev/null || true
fi

# 2. Package Managers Caches
if command -v npm &>/dev/null; then
    echo "Pruning NPM cache..."
    npm cache clean --force 2>/dev/null || true
    rm -rf "$HOME/.npm/_npx" 2>/dev/null || true
fi

if command -v pnpm &>/dev/null; then
    echo "Pruning PNPM store..."
    pnpm store prune 2>/dev/null || true
fi

if command -v yarn &>/dev/null; then
    echo "Pruning Yarn cache..."
    yarn cache clean 2>/dev/null || true
fi

if command -v brew &>/dev/null; then
    echo "Running Homebrew cleanup..."
    brew cleanup -s 2>/dev/null || true
fi

# 2b. Spotlight PipelineStorage journals
SPOT_PIPE="$HOME/Library/Metadata/CoreSpotlight/DocumentProcessing/PipelineStorage"
if [ -d "$SPOT_PIPE" ]; then
    echo "Pruning Spotlight PipelineStorage journals..."
    killall knowledgeconstructiond corespotlightd mds_stores 2>/dev/null || true
    rm -rf "$SPOT_PIPE/LSSR5EventsandordersUrgent/Journals"
    mkdir -p "$SPOT_PIPE/LSSR5EventsandordersUrgent/Journals"
    rm -f "$SPOT_PIPE/StateStore.db" "$SPOT_PIPE/StateStore.db-wal" "$SPOT_PIPE/StateStore.db-shm"
fi

# 3. Agent caches.  Do not wipe ~/.grok/worktrees — those are live Grok
# checkouts.  com.jay.disk-janitor already retires idle nested scratch.
echo "Pruning agent archived sessions..."
rm -rf "$HOME/.codex/archived_sessions"/* 2>/dev/null || true
rm -rf "$HOME/.npm/_npx" 2>/dev/null || true

# Prune Grok sessions older than 7 days
if [ -d "$HOME/.grok/sessions" ]; then
    echo "Pruning Grok sessions older than 7 days..."
    python3 - "$HOME/.grok/sessions" <<'PY'
import os, shutil, sys, time
from pathlib import Path
root = Path(sys.argv[1])
now = time.time()
cutoff = 7 * 86400
removed = 0
for dirpath, dirnames, filenames in os.walk(root, topdown=False):
    p = Path(dirpath)
    name = p.name
    if not (name.startswith("019") and len(name) >= 20):
        continue
    names = set(filenames)
    if "updates.jsonl" not in names and "chat_history.jsonl" not in names:
        continue
    try:
        newest = max((os.path.getmtime(os.path.join(dirpath, f)) for f in filenames), default=0)
    except OSError:
        continue
    if now - newest > cutoff:
        shutil.rmtree(p, ignore_errors=True)
        removed += 1
print(f"removed {removed} old grok sessions")
PY
fi

# Safe cleanup of old brain directories in Antigravity keeping current directory if present
if [ -d "$HOME/.gemini/antigravity/brain" ]; then
    find "$HOME/.gemini/antigravity/brain" -mindepth 1 -maxdepth 1 -type d -mtime +7 -exec rm -rf {} + 2>/dev/null || true
fi

# 3b. Reap node_modules and .next from suffixed/inactive feature worktrees in ~/apps/
echo "Pruning duplicate build caches on suffixed feature worktrees..."
python3 <<'PY'
import os, glob, shutil, re
KEEP_RE = re.compile(
    r"^/Users/jay/apps/[a-z0-9]+-(claude|codex|live|antigravity|cursor|monet|grok|grok-build|deepseek)$|"
    r"^/Users/jay/apps/(grok-acp-runtime|agy-acp-runtime|shellular-runtime|mac-collab|senate-relay-runtime|scout-runtime|dsh-runtime)$|"
    r"^/Users/jay/Code/.*$"
)
for wt in glob.glob('/Users/jay/apps/*'):
    if not os.path.isdir(wt) or KEEP_RE.match(wt):
        continue
    for sub in ['node_modules', '.next', '.turbo']:
        target = os.path.join(wt, sub)
        if os.path.isdir(target):
            shutil.rmtree(target, ignore_errors=True)
PY

# 4. Worktrees are owned by com.jay.disk-janitor (clean + idle, never forced).
# The #95 reaper treated detached HEAD as merged (empty-string word match
# hits every branch already in main) and then force-deleted the checkout,
# including in-session trees #93 was just fixed to keep.

# 5. Remote Hetzner Coolify maintenance trigger
if ssh -o ConnectTimeout=3 -o BatchMode=yes coolify "exit 0" 2>/dev/null; then
    echo "Triggering remote Hetzner Coolify maintenance..."
    ssh -o ConnectTimeout=5 coolify "/etc/cron.daily/coolify-auto-maintenance" >> /dev/null 2>&1 || true
fi

echo "[$(date)] Mac cleanup completed successfully."
