# Monet account — fleet skills (upload pack)

Updated **2026-08-20** for the **MONET** Claude account skill library.

These are fleet-ops skills for every app (Socratic.Trade, Congress.Trade, Usage Monitor,
congress-trading-shared, DealDex, Personal-Site, ai-fleet-coordinator / fleet-infra), not
Socratic.Trade-only.  The July 2026 copies in this folder were ST-shaped (retired Coolify
UUID `m1os7ijf31bg3fanil152e4b`, retired box IPs, no THE BOARD, no Apple Notes, mixed
`COOLIFY_API_TOKEN`) and would have taught Monet the wrong production topology.

Git-tracked copy: `ai-fleet-coordinator` `docs/fleet-skills/` (branch `grok/monet-fleet-skills`).
ST `Socratic.Trade/.claude/skills/` remains the older CLI convenience copies for that repo —
do not treat those as the Monet app library.

## Why this is a manual upload

The Claude **app** skill list is account-scoped and cloud-synced.  It is not the same as
CLI file-based skills in `<repo>/.claude/skills/` or `~/.claude/skills/`.  Dropping a
`SKILL.md` in a repo never registers it with the app.  Upload to **this account's** skill
library (MONET login).  CLAUDE is a different account with a separate library — do not
assume a Monet upload appears there.

## Skills in this pack

### Core loop (use every session)

| Skill | When |
|-------|------|
| `session-start` | Session start / resume / app switch — poll, board, Monet worktree, triple-claim |
| `board-ops` | THE BOARD (`board` CLI, `mac.jays.services/board`) |
| `closeout` | End of a unit — board + effort log + Slack + Notes |
| `secret-handoff` | Before any credential-adjacent command |
| `owner-copy` | Any human-readable paragraph (two spaces, light theme, no agent names in ASC) |
| `sentence-gap` | Always-on visible double sentence gap (Monet portable protocol — `&nbsp;` in Markdown chat) |
| `apple-notes` | Owner-facing plans / reviews / Completion notes |

### Land and babysit (original five, rewritten)

| Skill | When |
|-------|------|
| `land-lane` | Commit / PR / merge a Monet branch (apps with and without `land.sh`) |
| `unstick-pr` | PR will not merge (phantom conflicts, threads, CI) |
| `codex-triage` | Unresolved review threads (Codex, Bugbot, humans) |
| `pickup-seat` | Owner-directed cap/abandon handoff |
| `deploy-verify` | After merge/deploy — current Hetzner UUIDs, Vercel, PS non-auto-deploy |

### iOS

| Skill | When |
|-------|------|
| `ios-ship` | `xcodebuild` / `simctl` / TestFlight — never Xcode MCP |

Each skill is a **folder** and a `.zip` so either upload dialog works.  Zip layout is
`<skill-name>/SKILL.md`.

## Monet identity (all skills assume this)

- Slack / board tag: `[MONET]` / `--by MONET`
- Notes name: `Monet`
- Branches: `monet/<slug>` only — never `claude/`
- Pin `AGENT_SEAT=MONET` (local `~/.claude` is shared with CLAUDE)
- Worktrees: `~/apps/<prefix>-monet` — never `~/Code/<repo>`

## Upload steps (MONET login)

1. Claude app **Settings → Capabilities → Skills** (or claude.ai → Settings → Capabilities → Skills).
2. **Create / Upload skill**.
3. Upload each skill folder or its `.zip`.  Enable all.
4. Do this on the **MONET** login.  Repeat on CLAUDE only if you want the same pack there
   (swap the seat tag/prefix in your head; the procedures are fleet-wide).

## After upload

Canon still lives on disk.  If a skill and a file disagree, the file wins:

- `/Users/jay/apps/AGENT-SYNC.md`
- `/Users/jay/apps/EFFORT-LOG-PROTOCOL.md`
- `/Users/jay/apps/COOLIFY.md`
- `/Users/jay/apps/FLEET-UI-COPY.md`
- `/Users/jay/Code/ai-fleet-coordinator/fleet-apps.json`
- The app's `AGENTS.md`

## What changed vs 2026-07-13

- Fleet-wide (7 apps), not `socratictrade.com` only
- THE BOARD is the first claim surface
- Apple Notes + two-space / light-theme / CT timestamps
- Secret grep trap + Coolify `SERVER_STATS` vs `AGENTS`
- Current Coolify UUIDs and `167.233.254.55` (Hetzner cutover 2026-08-07)
- Personal-Site / DealDex Vercel paths; PS merge ≠ live
- Review triage covers Bugbot, not only Codex
- iOS loop without Xcode MCP
- `land.sh` is optional; never run from `~/Code/<repo>`
