#!/bin/bash
# Disk janitor — runs every 30 min via launchd (com.jay.disk-janitor).
# Philosophy: BRIEF health check each run; only REDUCE storage when space actually
# gets low, and only by deleting REGENERABLE things (caches, build output, deps on
# long-idle CLEAN worktrees). The ONE thing it removes that `npm ci` won't rebuild is
# an OLD, fully-merged, CLEAN, 7-day-idle git worktree (see the "retire" block) — and
# even that loses nothing in git: `git worktree remove` deletes only the checkout
# directory; the branch ref and its commits remain, so `git worktree add` restores it.
# It never touches a dirty or recently-active worktree, never a standing lane, and only
# ever clears .next/CACHE on prod/dev (never the whole prod build).
# Keep a specific worktree forever:  touch <worktree>/.janitor-keep
# Disable everything:  launchctl bootout gui/$(id -u)/com.jay.disk-janitor
# Log:      ~/.claude-disk-janitor/janitor.log
# Live install: ~/.claude-disk-janitor/janitor.sh (launchd com.jay.disk-janitor).
# After changing this tracked copy: cp scripts/disk-janitor.sh ~/.claude-disk-janitor/janitor.sh && chmod +x ~/.claude-disk-janitor/janitor.sh
# 2026-08-22: all fleet Code repos; standing-lane KEEP_RE; retired-KIMI seat /
# nested / tmp may reap when idle even if unmerged.  Never skip the idle check.
# Do not substring-match "kimi" (that reaps cursor/kimi-audit-def / ST #3044).

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$HOME/.local/bin:$HOME/.npm-global/bin"
# git must never block on a credential prompt (no tty under launchd) or a network stall:
# fail fast instead of hanging the whole tick behind the run-lock.
export GIT_TERMINAL_PROMPT=0 GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=15
HOME_DIR="$HOME"
DIR="$HOME_DIR/.claude-disk-janitor"
LOG="$DIR/janitor.log"
STATE="$DIR/state"
LOCK="$DIR/.lock"
DATA_VOL="/System/Volumes/Data"

# ---- thresholds (GiB free) ----
LOW_FREE=50        # below this -> clear regenerable caches + prod/dev build caches
PRESSURE_FREE=48   # below this -> ALSO reap .next/node_modules on CLEAN worktrees idle > IDLE_HRS
                   # (raised 42->48 on 2026-07-19, owner-directed: reclaim aggressively anytime
                   # free space dips under ~50G rather than waiting for deeper pressure)
DROP_ALERT=6       # free dropped at least this much since last run -> flag it
IDLE_HRS=4         # a worktree is "abandoned" (dep-reapable) after this many hours untouched
PM2_LOG_CAP_MB=50  # truncate any single pm2 log larger than this (pure waste, always)

# ---- old-worktree retirement (removes the whole checkout dir; branch+commits survive) ----
REAP_WORKTREES=${REAP_WORKTREES:-1}   # master switch: 1 = retire old merged worktrees every run, 0 = off
STALE_DAYS=${STALE_DAYS:-7}           # a CLEAN, MERGED/gone worktree untouched this many days is retired
WT_REAP_DRYRUN=${WT_REAP_DRYRUN:-0}   # 1 = only LOG "WOULD-RETIRE ..." and remove nothing (for testing)

REPOS=(
  /Users/jay/Code/Socratic.Trade
  /Users/jay/Code/Congress.Trade
  /Users/jay/Code/Usage-Monitor
  /Users/jay/Code/congress-trading-shared
  /Users/jay/Code/DealDex
  /Users/jay/Code/Personal-Site
  /Users/jay/Code/Autorotate
  /Users/jay/Code/ContactLogo
  /Users/jay/Code/ai-fleet-coordinator
)
# Standing lanes / primaries the janitor must never touch.  Code roots +
# unsuffixed seat checkouts (trading-grok, dealdex-claude, …) + runtimes.
# Suffixed per-lane trees (trading-grok-litestream-cascade) remain reaped
# when merged+idle.  Retired-KIMI seat trees reap when idle (not on a "kimi"
# substring, and never by skipping the idle check).
KEEP_RE="^(/Users/jay/Code/Socratic.Trade|/Users/jay/Code/Congress.Trade|/Users/jay/Code/Usage-Monitor|/Users/jay/Code/congress-trading-shared|/Users/jay/Code/DealDex|/Users/jay/Code/Personal-Site|/Users/jay/Code/Autorotate|/Users/jay/Code/ContactLogo|/Users/jay/Code/ai-fleet-coordinator|/Users/jay/apps/[a-z0-9]+-(claude|codex|live|antigravity|cursor|monet|grok|grok-build|deepseek)|/Users/jay/apps/(grok-acp-runtime|agy-acp-runtime|shellular-runtime|mac-collab|seat-mcp|KIMI-SALVAGE-2026-08-22))$"

# Retired-KIMI seat, nested agent scratch, or /tmp.  Not a substring:
# branch cursor/kimi-audit-def (ST #3044, owner-kept) must not match.
janitor_is_retired_kimi_or_scratch() {
  local wt="$1" br="${2#refs/heads/}"
  case "$br" in
    kimi/*|KIMI/*) return 0 ;;
  esac
  case "$wt" in
    */.claude/worktrees/*|*/.grok/worktrees/*|/private/tmp/*|/tmp/*) return 0 ;;
  esac
  local base="${wt##*/}"
  case "$base" in
    *-kimi|*-kimi-*)
      case "$base" in
        *-claude-*|*-codex-*|*-live-*|*-antigravity-*|*-cursor-*|*-monet-*|*-grok-*|*-grok-build-*|*-deepseek-*)
          return 1 ;;
      esac
      return 0 ;;
  esac
  return 1
}

if [ "${JANITOR_LIB_ONLY:-0}" = "1" ]; then
  return 0 2>/dev/null || exit 0
fi

mkdir -p "$DIR"
# single-run lock (skip this tick if a previous run is still going).
# Steal if the lock dir is older than 2h -- a crash leftover wedged this
# job from 2026-08-11 until 2026-08-16 (every 30min tick exited 0).
if ! mkdir "$LOCK" 2>/dev/null; then
  lock_age=$(( $(date +%s) - $(stat -f %m "$LOCK" 2>/dev/null || echo 0) ))
  if [ "$lock_age" -gt 7200 ]; then
    rmdir "$LOCK" 2>/dev/null || true
    mkdir "$LOCK" 2>/dev/null || exit 0
  else
    exit 0
  fi
fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

now="$(date '+%Y-%m-%d %H:%M')"
freek() { df -k "$DATA_VOL" | tail -1 | awk '{print $4}'; }   # KiB free
gib() { echo $(( ${1:-0} / 1024 / 1024 )); }

duk() { local k; k=$(du -sk "$1" 2>/dev/null | awk '{print $1}'); echo "${k:-0}"; }  # KiB, 0 if absent
# Porcelain output minus UNTRACKED generated build junk (node_modules/.next/build receipts/logs).
# Empty output = safe to treat the worktree as clean for retirement/dep-reap purposes. Any tracked
# modification (' M', 'A ', etc.) or non-generated untracked file still blocks. Added 2026-07-19
# (owner-directed): dozens of long-dead worktrees carried only untracked node_modules/.next and so
# never qualified as clean, pinning ~50M-1G each forever.
wt_blocking_dirt() {
  git -C "$1" status --porcelain 2>/dev/null | grep -vE '^\?\? (node_modules/|\.next/|next-env\.d\.ts$|tsconfig\.tsbuildinfo$|\.DS_Store$|[^ ]*\.log$|data/app\.db(-wal|-shm)?$)'
}

free_k=$(freek); free=$(gib "$free_k")
prev_free=$(sed -n 's/^free=//p' "$STATE" 2>/dev/null); prev_free=${prev_free:-$free}
delta=$(( free - prev_free ))
# Under 50G free, retire merged/clean worktrees after 2 days instead of 7.
# 2026-08-22: janitor only covered ST/CT/CTS so UM/DD/TS/FLEET trees piled up.
if [ "$free" -lt "$LOW_FREE" ] && [ "${STALE_DAYS}" = "7" ]; then
  STALE_DAYS=2
fi

# cheap bucket sizes (bounded dirs only — keeps the run brief)
npm_k=$(duk "$HOME_DIR/.npm"); uv_k=$(duk "$HOME_DIR/.cache/uv")
livec_k=$(duk /Users/jay/apps/trading-live/.next/cache)
codexc_k=$(duk /Users/jay/apps/trading-codex/.next/cache)
pm2_k=$(duk "$HOME_DIR/.pm2/logs")

actions=""

# --- ALWAYS (cheap, pure waste): cap runaway pm2 logs + tidy stale worktree registry ---
n_trunc=$(find "$HOME_DIR/.pm2/logs" -type f -name '*.log' -size +${PM2_LOG_CAP_MB}M 2>/dev/null | wc -l | tr -d ' ')
if [ "${n_trunc:-0}" -gt 0 ]; then
  find "$HOME_DIR/.pm2/logs" -type f -name '*.log' -size +${PM2_LOG_CAP_MB}M -exec sh -c ': > "$1"' _ {} \; 2>/dev/null
  actions="${actions}pm2logs "
fi
for r in "${REPOS[@]}"; do git -C "$r" worktree prune 2>/dev/null; done

# --- ALWAYS: reap leftover vitest temp SQLite DBs (pure waste; grew to 130 GB once) ---
# Every `npm test` run writes per-test-file temp DBs (agentic-*.db/-wal/-shm) into the
# user temp dir and never deletes them; the fleet runs the suite constantly. 6h age
# filter keeps any live/recent test run untouched. getconf resolves the per-login temp
# dir, so this works on both the CLAUDE and MONET macOS accounts.
UT="$(getconf DARWIN_USER_TEMP_DIR 2>/dev/null | sed 's:/*$::')"
if [ -n "$UT" ] && [ -d "$UT" ]; then
  n_tdb=$(find "$UT" -maxdepth 1 -name 'agentic-*' -mmin +360 2>/dev/null | wc -l | tr -d ' ')
  if [ "${n_tdb:-0}" -gt 0 ]; then
    find "$UT" -maxdepth 1 -name 'agentic-*' -mmin +360 -delete 2>/dev/null
    actions="${actions}tmp-testdb(${n_tdb}) "
  fi
fi

# --- ALWAYS: retire OLD, fully-merged, CLEAN, idle worktrees (removes the checkout dir only) ---
# `git worktree remove` deletes ONLY the working directory. The branch ref and every commit it
# points to REMAIN in the repo, so nothing tracked is ever lost — at most a re-`git worktree add`
# is needed to get the checkout back. A worktree qualifies for retirement only if ALL hold:
#   * not a standing lane / primary repo (KEEP_RE) and not a locked worktree
#   * no <worktree>/.janitor-keep opt-out marker
#   * working tree CLEAN ignoring generated junk — no tracked modifications and no untracked
#     files beyond node_modules/.next/build receipts/logs (see wt_blocking_dirt)
#   * no non-generated file modified within STALE_DAYS (genuinely "old" / idle)
#   * its HEAD is already contained in origin's default branch (merge-base --is-ancestor), OR
#     its upstream is [gone] (branch pushed then deleted on origin — the squash-merge signature)
if [ "${REAP_WORKTREES:-0}" = "1" ]; then
  stale_min=$(( STALE_DAYS * 1440 ))
  # Light refresh: fetch ONLY origin/main (keeps merge-base accurate) + prune stale
  # remote-tracking refs (marks squash-merged branches' upstreams [gone]). Avoids the
  # heavy all-branch `fetch --prune` that made ticks crawl on the big repo.
  for r in "${REPOS[@]}"; do
    git -C "$r" fetch origin main -q 2>/dev/null
    git -C "$r" remote prune origin 2>/dev/null
  done
  n_reap=0
  while IFS=$'\t' read -r wt sha br locked; do
    [ -n "$wt" ] && [ -d "$wt" ] || continue
    echo "$wt" | grep -qE "$KEEP_RE" && continue                                   # standing lane / primary
    [ -n "$locked" ] && continue                                                    # git-locked worktree
    [ -e "$wt/.janitor-keep" ] && continue                                          # explicit opt-out
    [ -n "$(wt_blocking_dirt "$wt")" ] && continue                                  # real dirt -> keep (generated junk ignored)
    # Always require idle.  Skipping this (force_stale) deleted a checkout
    # on the next 30-min tick after a clean commit — including ST #3044
    # (branch cursor/kimi-audit-def) and in-session .claude/.grok worktrees.
    [ -n "$(find "$wt" -type f -not -path '*/.git' -not -path '*/.git/*' \
              -not -path '*/node_modules/*' -not -path '*/.next/*' \
              -mmin -$stale_min -print -quit 2>/dev/null)" ] && continue            # active within STALE_DAYS -> keep
    base=$(git -C "$wt" rev-parse --abbrev-ref origin/HEAD 2>/dev/null); base=${base:-origin/main}
    merged=no
    git -C "$wt" merge-base --is-ancestor HEAD "$base" 2>/dev/null && merged=yes
    if [ "$merged" = no ]; then
      href=$(git -C "$wt" symbolic-ref -q HEAD 2>/dev/null)
      [ -n "$href" ] && [ "$(git -C "$wt" for-each-ref --format='%(upstream:track)' "$href" 2>/dev/null)" = "[gone]" ] && merged=yes
    fi
    # Retired-KIMI seat / nested scratch / tmp: eligible when idle even if
    # unmerged.  Seat match only — not substring "kimi".
    if [ "$merged" = no ] && janitor_is_retired_kimi_or_scratch "$wt" "$br"; then
      merged=yes
    fi
    [ "$merged" = yes ] || continue                                                 # unmerged & not gone -> keep
    brn=${br#refs/heads/}
    if [ "${WT_REAP_DRYRUN:-0}" = "1" ]; then
      printf '%s  WOULD-RETIRE worktree %s (branch=%s)\n' "$now" "$wt" "${brn:-detached}" >> "$LOG"
      n_reap=$(( n_reap + 1 )); continue
    fi
    for r in "${REPOS[@]}"; do
      if git -C "$r" worktree remove "$wt" 2>/dev/null; then
        n_reap=$(( n_reap + 1 ))
        printf '%s  RETIRED worktree %s (branch=%s, merged/gone)\n' "$now" "$wt" "${brn:-detached}" >> "$LOG"
        break
      fi
    done
  done < <(
    for r in "${REPOS[@]}"; do
      git -C "$r" worktree list --porcelain 2>/dev/null | awk '
        /^worktree /{ l=$0; sub(/^worktree /,"",l); wt=l; sha=""; br=""; lk="" }
        /^HEAD /{ sha=$2 }
        /^branch /{ l=$0; sub(/^branch /,"",l); br=l }
        /^locked/{ lk="locked" }
        /^$/{ if(wt!=""){ print wt"\t"sha"\t"br"\t"lk; wt="" } }
        END{ if(wt!=""){ print wt"\t"sha"\t"br"\t"lk } }'
    done | sort -u
  )
  [ "$n_reap" -gt 0 ] && actions="${actions}wt-retire(${n_reap}) "
fi

# --- LOW FREE: clear regenerable caches + prod/dev build caches ---
if [ "$free" -lt "$LOW_FREE" ]; then
  if command -v cleanmymac &>/dev/null; then
    cleanmymac clean --force 2>/dev/null || true
    cleanmymac optimize ram 2>/dev/null || true
    actions="${actions}cleanmymac "
  fi
  rm -rf "$HOME_DIR/.npm/_cacache" 2>/dev/null
  rm -rf "$HOME_DIR/.cache/uv" 2>/dev/null
  rm -rf "$HOME_DIR/Library/Caches/ms-playwright/"* 2>/dev/null
  rm -rf "$HOME_DIR/.cache/chrome-devtools-mcp" 2>/dev/null
  rm -rf "$HOME_DIR/Library/Developer/CoreSimulator/Caches"/* 2>/dev/null
  rm -rf /Users/jay/apps/trading-live/.next/cache 2>/dev/null
  rm -rf /Users/jay/apps/trading-codex/.next/cache 2>/dev/null
  actions="${actions}caches "
fi

# --- PRESSURE: reap deps on long-idle CLEAN worktrees (reversible; keeps source+branch) ---
if [ "$free" -lt "$PRESSURE_FREE" ]; then
  idle_min=$(( IDLE_HRS * 60 ))
  for r in "${REPOS[@]}"; do git -C "$r" fetch origin main -q 2>/dev/null; done
  { for r in "${REPOS[@]}"; do git -C "$r" worktree list --porcelain 2>/dev/null | awk '/^worktree /{print $2}'; done; } | sort -u | while read -r wt; do
    [ -d "$wt" ] || continue
    echo "$wt" | grep -qE "$KEEP_RE" && continue
    [ -n "$(wt_blocking_dirt "$wt")" ] && continue                                                                         # real dirt -> skip (generated junk ignored)
    [ -n "$(find "$wt" -type f -not -path '*/.git/*' -not -path '*/node_modules/*' -not -path '*/.next/*' -mmin -$idle_min -print -quit 2>/dev/null)" ] && continue  # active -> skip
    find "$wt" -type d \( -name node_modules -o -name .next -o -name .turbo \) -prune -exec rm -rf {} + 2>/dev/null
  done
  actions="${actions}idle-dep-reap "
fi

[ -z "$actions" ] && actions="none"
after_k=$(freek); after=$(gib "$after_k")
reclaimed=$(( (after_k - free_k) / 1024 / 1024 ))

note=""
[ "$delta" -le "-$DROP_ALERT" ] && note=" DROP(${delta}G since last)"
printf '%s  free=%sG(Δ%+dG) npm=%sG uv=%sG live$=%sG codex$=%sG pm2=%sM  action=%s reclaimed=%sG%s\n' \
  "$now" "$free" "$delta" "$(gib $npm_k)" "$(gib $uv_k)" "$(gib $livec_k)" "$(gib $codexc_k)" "$(( pm2_k/1024 ))" "$actions" "$reclaimed" "$note" >> "$LOG"

# persist state + cap log to last 500 lines
printf 'free=%s\nts=%s\n' "$after" "$now" > "$STATE"
tail -n 500 "$LOG" > "$LOG.tmp" 2>/dev/null && mv "$LOG.tmp" "$LOG"
