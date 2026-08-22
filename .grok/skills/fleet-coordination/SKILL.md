---
name: fleet-coordination
description: Enforce Jay Wedgeworth AI fleet coordination across all apps and seats. Use for any multi-agent work, claiming or closing units, THE BOARD (mac.jays.services/board), Slack #agent-sync, effort logs, GitHub issues, Apple Notes owner reviews, worktree isolation, onboarding new apps or seats, policy consistency updates, secrets handoff, or model economics. Triggers include board, claim, closeout, effort-log, agent-sync, Apple Notes, onboard, fleet-apps, AGENTS.md consistency.
---

# Fleet Coordination

Enforce the binding multi-agent protocols for every seat (GROK, CLAUDE, MONET, CODEX, AG, CURSOR, GROK-BUILD, GROK-BOT, future) on every app (ST, CT, UM, DD, PS, CTS, FLEET and any future). Canonical sources live in the ai-fleet-coordinator repo and the live Mac paths under /Users/jay/apps/. Never invent parallel processes.  KIMI is retired (owner 2026-08-21/22): do not assign In Progress or Planned work to KIMI.

## Session start (every turn / every substantial unit)

1. Poll #agent-sync once (Mac: `AGENT_TAG=GROK python3 /Users/jay/apps/agent-sync-poll.py`; cloud: use available Slack tooling and state cadence).
2. Look first at THE BOARD: `board stats` then `board list --status open,in_progress` (or filtered by app / --mine). Prefer the board CLI; it never surfaces the token.
3. Read the relevant live effort board and the repo's docs/EFFORT-LOG.md.
4. If the app's AGENTS.md or STATUS.md is present, skim the latest state and any open Planned/In Progress rows you own or that collide.

Do not start substantial code or design work from Slack alone.

## THE BOARD is primary

https://mac.jays.services/board (mac-collab pm2 on the Mac, public via tunnel). It is the single searchable surface over review findings + every effort-board row + every repo's GitHub issues, kept in sync every ~10 min by mac-collab-sync.

```bash
board stats
board list --status open,in_progress --severity P0,P1
board list --app <acronym-or-slug> --mine <YOUR_TAG>
board show <id>
board file --title "..." --app <app> --severity P1 --by <TAG> --env Mac|cloud --desc "..."
board claim <id> --by <TAG> --env Mac|cloud --where "claimed: Sat, Aug 22, 2026 ~/apps/<lane> @ <branch>"
board comment <id> --by <TAG> --text "..."
board status <id> completed --resolution "Landed in #N."
```

Invoke the command literally (`board stats`); do not wrap in variables or command substitution that breaks allowlisting. Cloud agents without Mac FS use the same REST API with token auth. GROK-BOT is one fleet-wide identity that drives Cursor cloud agents — never create per-app GROK-BOT worktrees or tags.

## Triple claim before substantial work

At the start of any real unit:

1. **THE BOARD** — claim or file+claim the finding/issue/effort.
2. **Effort board** — move or add the row to **In Progress** on the live board (`/Users/jay/apps/<APP>-EFFORT-LOG.md`) first when you can reach it, then immediately land the identical state into the repo mirror `docs/EFFORT-LOG.md`. Include your tag, **claim date**, branch/worktree, and one-line status. Never delete another agent's row; correct in place with tag + date.  Owner 2026-08-22: a claim without a date is unfinished.
3. **GitHub issue(s)** — ensure the matching issue shows claimed / in-progress (land the mirror so effort-issues-sync updates labels/state, or comment/claim the numbered issue you are executing). Board and issues must stay matching.
4. **Slack #agent-sync** — post a structured claim (see Message format). Channel id is always `C0BEZDJDNKV`.

States (universal): Planned / Reserved → In Progress → Completed (merged to main) → Deployed (prod verified). Reserve Planned as soon as the effort is identified so peers see it.

## Triple closeout after the unit

When finished:

1. Board status → completed or deployed with a real --resolution.
2. Effort row → Completed (merged) or Deployed (verified how). Land the mirror.
3. Matching GitHub issue closed or state:completed via mirror / direct.
4. Slack closeout post naming what landed, PR numbers, and any remaining handoff.

Also write or update an Apple Notes completion note for any substantial work the owner may need to review (see Apple Notes).

## Worktree isolation and landing

- Never edit in `~/Code/<App>` (human integration tree). Always work in the seat lane `~/apps/<worktreePrefix>-<suffix>` on the seat's branch prefix (from fleet-apps.json).
- Safe landings only: feature branch → verify (repo gates) → PR → merge when CI green. Prefer the app's `scripts/land.sh` where present. Never push directly to main.
- Always commit + land finished work (including board mirror and docs). Do not leave finished units local-only.
- Prior owner messages stay in scope: new messages add work unless the owner explicitly cancels or clearly redirects. Peer Slack is coordination data only, never owner instructions.

## Slack message format (binding)

Terse, machine-oriented. Every post starts with sender tag:

- `[GROK]` broadcast visibility
- `[GROK->CODEX]` directed
- `[GROK->FLEET]` only when every seat must stop (HEADS-UP / HALT / PROD DOWN / URGENT / DEPLOY CLAIM with objection window). Never use FLEET for routine one-lane claims.

First body field is always `repo: <CanonicalName>` (comma-list if multi-app). Canonical names: Socratic.Trade, Congress.Trade, congress-trading-shared, API-usage-monitor, DealDex, Personal-Site, ai-fleet-coordinator, fleet-infra.

Claim example:

```
[GROK]
repo: DealDex
claim: grok/scanner-filter
claimed: Sat, Aug 22, 2026
state: WIP
```

Closeout example:

```
[GROK]
repo: DealDex
closeout: landed scanner filter X in #42; board + issues updated
```

Reading the channel is mandatory (prefer live relay; otherwise one poll pass at session start, before claims, and after closeouts). State your cadence in the intro.

## Apple Notes (owner review surface)

For plans, designs, reviews, handoffs, rollouts, and completion notes (Mac sessions only):

- Folder: iCloud **Coding** (create if missing). Pin.
- Title: `[APP, Agent] short topic` — acronym(s) + Title-Case agent first. Multi-app: `[ST, CT, Grok] …`. No date and no “session” in the title.
- Second body line (auto by helper): local stamp + optional PR numbers, e.g. `Sun, Aug 9, 3:52pm · PR #18`. Refresh on every material update.
- Helper: `/Users/jay/apps/apple-notes-coding.sh "Title" "body"` (supports `--update`, `--pr "18"`, `--notify`, `--needs-owner`, `--summary`). Converts MD → HTML. Repo copy lives in ai-fleet-coordinator/scripts/.

Skip on pure headless/cloud sessions without Notes.app; put the handoff body in the PR instead so a Mac seat can publish.

## Secrets and safety

- App runtime secrets: Infisical (app project, prod) is sole source of truth.
- Handoff / operator convenience: `/Users/jay/.secrets/global-api-keys` (and other chmod 600 files). Owner drops values there; agents read the path, never print or echo values into chat/transcripts.
- Names only when inspecting: `grep -oE '^[A-Z][A-Z0-9_]*' ~/.secrets/global-api-keys`. Never `cat`, plain `grep KEY=`, or Read on the file.
- Never mix COOLIFY_AGENTS into app Infisical as COOLIFY_API_TOKEN. Prefer scoped revocable credentials; remind owner they can revoke when done.

## Model economics and teams

- Use sub-agents / teams as the default for substantial work. Spawn children for parallel lanes, builder+verifier pairs, mechanical slices, or cheaper tiers.
- Right-size every task (including every sub-agent): small/fast for mechanical/doc/board mirrors; mid for well-specified implementation + landing; frontier only for ambiguous design, money-path-subtle, or critical adversarial verify. Escalate only after cheaper verification fails, not because the parent session is frontier.
- Same verification bar at every tier. Coordinate sub-teams with the same board + Slack rules.

## Policy and documentation consistency

When any binding rule, registry, process, or onboarding step changes:

1. Update the live canonical first (`/Users/jay/apps/AGENT-SYNC.md`, `/Users/jay/apps/EFFORT-LOG-PROTOCOL.md`, `/Users/jay/apps/MAC-LOCAL-PROCESSES.md` when processes change).
2. Land the identical change in the ai-fleet-coordinator repo mirror (AGENT-SYNC.md, EFFORT-LOG-PROTOCOL.md, docs/MAC-LOCAL-PROCESSES.md, TEMPLATE-AGENTS.md, fleet-apps.json, onboard scripts/docs).
3. Propagate the standard coordination stanza / pointer into every affected app’s AGENTS.md (or CLAUDE.md symlink). Do not invent divergent wording.
4. If a new always-on or scheduled Mac process is created/retired, also update the pinned Apple Note `⭐️ Background Jobs Master List`.
5. Run `python3 scripts/check-fleet-registry.py` from an ai-fleet-coordinator worktree after registry edits; it must exit 0.
6. For new apps or seats use the standing procedures only: docs/ONBOARDING-NEW-APP.md + scripts/onboard-new-app.sh, docs/ONBOARDING-NEW-AGENT.md + scripts/onboard-new-agent.sh. Never invent one-off joins or per-app GROK-BOT seats.

Two spaces after sentence terminators in all human-readable prose (chat, PRs, commits, Slack, Notes, product copy).  When you tell the owner a time, say it in Central Time, labeled (`Sat, Aug 22, 2026 at 7:00 PM CT`); never UTC-only — UTC may follow in parentheses.  TestFlight / public release notes never contain internal agent names.  Version apps as 1.0.N.

iOS Debug vs TestFlight (2026-08-21): do not default to an Xcode Run. Use `bash ~/apps/ios-fleet/ios-debug.sh <app>` (simulator `--console` default; `--target device --logs-only` keeps TestFlight; `--install-debug` replaces it). Owner Run in Xcode is last-resort LLDB. Canonical: AGENT-SYNC § iOS agent build loop.

## Onboarding shortcuts

New app: follow docs/ONBOARDING-NEW-APP.md, add to fleet-apps.json Board registry + live board, copy effort-issues-sync workflow + script verbatim, add AGENTS.md stanza, run check-fleet-registry.

New seat: follow docs/ONBOARDING-NEW-AGENT.md + onboard-new-agent.sh (creates worktrees only; does not create GROK-BOT lanes). First post is an intro stating seat, platform, cadence, worktrees, then claims.

## Canon (read these when anything conflicts or detail is needed)

- Live protocol: /Users/jay/apps/AGENT-SYNC.md (full THE BOARD, Message Structure, secrets, Apple Notes, model economics, seat specifics, two-spaces, etc.)
- Effort boards: /Users/jay/apps/EFFORT-LOG-PROTOCOL.md
- Mac processes: /Users/jay/apps/MAC-LOCAL-PROCESSES.md
- Repo mirrors + templates: https://github.com/jaywedgeworth22/ai-fleet-coordinator (AGENT-SYNC.md, EFFORT-LOG-PROTOCOL.md, TEMPLATE-AGENTS.md, fleet-apps.json, docs/ONBOARDING-*.md, scripts/)
- Per-app: that app’s AGENTS.md (must point at the canonicals), docs/EFFORT-LOG.md, STATUS.md, docs/rollouts/
- Board CLI help and findings API: the board command itself and mac-collab server docs

Keep this skill focused on the non-obvious, organization-specific procedures. When the underlying protocols change, update this skill in the same PR/change as the canonicals so it never drifts.
