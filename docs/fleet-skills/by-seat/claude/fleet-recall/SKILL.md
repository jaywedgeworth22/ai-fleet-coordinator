---
name: fleet-recall
description: >-
  Search the fleet's shared knowledge corpus (board resolutions, Apple Notes, effort logs, protocol docs, seat memories) before re-deriving a lesson, and contribute a reusable lesson after you learn one.  Use at the start of any task that smells familiar (an incident, a deploy gotcha, an owner preference), whenever a peer says "we solved this before", and at closeout.  Backed by the self-hosted fleet-agents Qdrant collection on the Hetzner box.
---

# Fleet recall

The fleet has one shared memory: the `fleet-agents` collection in the self-hosted Qdrant on the
Hetzner box, embedded by the self-hosted bge-m3 endpoint.  It holds every board row with its
resolution, the Apple Notes archive, every effort log, the fleet protocol docs, the skills, and
each seat's memory files, refreshed nightly by the BotFleet bot Oracle.  Canonical doc:
`docs/RAG-FLEET-INFRA.md` in ai-fleet-coordinator.

## When to use it

- **Before** diagnosing anything that looks like it has happened before (pm2 orphan ports,
  Coolify deploy stalls, Pinecone/Qdrant quirks, TestFlight rejections, owner formatting rules).
- **Before** asking the owner a question that a past ruling probably answers.
- **After** you learn something reusable: a gotcha, a measured number, an owner preference, a
  runbook step.  Contribute it once, in one paragraph, with the app and category set.

## How

Mac seats (Claude, Codex, Cursor, Grok, Antigravity, Monet) have the `fleet-recall` MCP server
registered, so call the tools directly:

- `recall_search(query, limit, category, app, source, seat, since_days)`
- `recall_contribute(text, category, app, seat, title, url)`
- `recall_stats()`

The same tools are on the CLI (on PATH via `~/.local/bin/recall` and `~/apps/mac-collab/recall`, like `board`):

```bash
recall "pm2 orphan holds port"
recall "how do we rotate the Coolify token" --app fleet --limit 3
recall contribute "TEI warmup memory scales with --max-batch-tokens; 4096 under 10 GiB is stable." --category lesson --app fleet
recall stats
recall doctor
```

Cloud seats (Cursor cloud, Codex cloud, Claude cloud, Grok Bot personas) reach the same three
tools through the fleet MCP gateway at `https://agents.jays.services/mcp` (Cloudflare Access +
bearer, see `docs/fleet-skills/drive-grok-tui`).  Nothing else on the internet can reach the
corpus; both services bind to the Tailscale mesh only.

## Rules

- **Search first, then act.**  A hit with a board id or a note title is a lead, not a verdict:
  open the source (board show, the note, the doc) before relying on it.
- **Contribute lessons, not logs.**  40 to 4,000 characters, one idea, with `category` one of
  `lesson | preference | infrastructure | decision | runbook` and the app slug.  Do not paste
  transcripts, secrets, or anything a scrub would have to redact.  Contributions are scrubbed
  and gitleaks-gated, but the corpus is fleet-wide memory, so write it the way you would write a
  board resolution.
- **Contribute every reusable lesson.**  Owner 2026-09-02: `recall_contribute` is the highest-yield write path — the seat that just burned tokens on a trap is the only one that knows.  Search first so you corroborate rather than duplicate.  One idea, 40–4000 chars, category `lesson | preference | infrastructure | decision | runbook`.  Optional `url` is provenance, not a gate.  Board / Notes / effort logs / docs still hold facts that already have a home; they are not a reason to skip the lesson.
- **Do not bulk-ingest chat transcripts as lessons.**  Chat mining is a rare infra/policy scan (owner rulings, environment shifts).  Agents contribute lessons themselves; token-waste is often invisible in the thread.
- **Do not point Socratic.Trade's embed provider at the fleet endpoint.**  The two embedding
  spaces are not compatible (measured 2026-08-31; see the canonical doc).
- Two spaces between sentences in anything you contribute; it is owner-facing text.
