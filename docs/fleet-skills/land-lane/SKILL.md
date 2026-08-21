---
name: land-lane
description: Land a Monet feature branch to main across the fleet — seat worktree, docs, verification gate, PR, auto-merge, then closeout. Use when finishing a unit, opening a PR, merging, or when the owner says land/ship/commit/push. Never wait for the owner to ask. Covers apps with and without scripts/land.sh.
---

# Land a feature branch (MONET)

Always-commit is standing policy.  After each coherent finished unit: commit → push → PR → merge when CI is green.  A remote branch with no PR is unfinished.  Pause only for force-push, prod data wipe, or live-key revoke.

Seat: **MONET**.  Branch: `monet/<slug>`.  Never `claude/`.  Never land from `~/Code/<repo>` or from branch `main`.

## Preconditions

1. You are in your Monet worktree (`~/apps/<prefix>-monet` or `~/apps/<prefix>-monet-<lane>`).  See `session-start`.
2. `git status` is clean except `.env.local` / `.dev.vars` (never commit those).
3. `git config user.email` is `12656028+jaywedgeworth22@users.noreply.github.com`.

```bash
git config user.email "12656028+jaywedgeworth22@users.noreply.github.com"
```

## Docs before the PR

1. Live effort board → In Progress with honest status; mirror `docs/EFFORT-LOG.md` in the same commit (fleet-infra has no mirror).
2. `STATUS.md` stanza: what landed, next action.
3. `docs/rollouts/YYYY-MM-DD-slug.md` — summary, why, files, verification commands actually run, follow-ups.
4. Substantial owner-facing work: living Apple Note via the `apple-notes` skill, title `[APP, Monet] …`.

Prose (commit body, PR body, rollout, Notes): two ASCII spaces between sentences.  Chat replies to the owner use `&nbsp;` plus a space.  See `owner-copy`.

## Gate

### Apps with `scripts/land.sh` (Socratic.Trade, ai-fleet-coordinator)

Homebrew default `node` may be v26.  ST `better-sqlite3` is Node 24 (MODULE_VERSION 137).  Confirm `node --version` is v24.x:

```bash
export PATH=/opt/homebrew/opt/node@24/bin:$PATH
node --version
PATH=/opt/homebrew/opt/node@24/bin:$PATH bash scripts/land.sh
```

The script (idempotent) refuses the integration worktree and branch `main`, refuses a dirty tree, fetches, refuses auto-merge on stale file overlap with `origin/main`, merges `origin/main`, runs `npx tsc --noEmit` → `npm test` → `npm run build`, pushes, opens a PR.

ST `land.sh` may still mention a retired path (`~/Code/Agentic Trading`).  The binding keepout is **any** `~/Code/<repo>` checkout.

If it dies on missing `workflow` OAuth scope (branch touched `.github/workflows/*`):

```bash
gh auth refresh -h github.com -s workflow
bash scripts/land.sh
```

### Apps without `land.sh` (CT, UM, CTS, DealDex, Personal-Site)

Same shape, run the app's own verify from `AGENTS.md`:

```bash
git fetch origin
git merge origin/main --no-edit
# then that repo's gate — do not invent `npm test` on a static-only tree
git push -u origin HEAD
gh pr create --fill
```

Personal-Site: `site/` is the TanStack Start source (see current README).  `AGENTS.md` may still say "static snapshot / do not invent npm test" — verify against README + the tree in front of you.  Preserve About copy `Earlier work included` and the Doximity `/profiles/…/view` URL; the daily mirror workflow will revert them if you drop them.

CTS is a consumed library: "prod" is a published tag, not a Coolify app.

`STATUS.md` / `PLAN.md` / `docs/EFFORT-LOG.md` often carry `merge=union` in `.gitattributes`.  Additive board edits usually combine.  Never delete another agent's row while resolving.  Up to 3 land attempts are fine.

## Arm auto-merge

```bash
gh pr merge <N> --squash --auto
```

Not `--admin`.  Branch protection is `enforce_admins: true` plus conversation resolution.  Unresolved review threads block forever.  Use `codex-triage` / `unstick-pr`.

If the box is gating several lanes, post `[MONET] gating now` with `repo:` (not `FLEET` unless you need every seat).

## After merge

- Board row: **Completed** means merged to `main`, not "PR opened."
- **Deployed** only after the app's production target is verified (`deploy-verify`).
- Merge to `main` auto-deploys ST / CT / UM on Coolify and DealDex on Vercel.  Do not double-trigger.  Personal-Site live origin is Vercel behind Cloudflare and is **not** "merge = live" — do not mint a second Vercel project.
- Closeout: `closeout` skill.

## Do not

- `LAND_SKIP_VERIFY` / `LAND_FORCE_PUSH` as an agent.  Humans only.
- Force-push shared history.
- Park a finished green PR "just in case."
- Claim Completed while threads are unresolved.

## Canon

- `/Users/jay/apps/AGENT-SYNC.md` — Always commit + land; merge requirements; branch/worktree naming
- App `AGENTS.md` Pre-Commit / Handoff + Verify before claiming done
- `scripts/land.sh` when present
- Skills: `session-start`, `unstick-pr`, `codex-triage`, `deploy-verify`, `closeout`, `owner-copy`
