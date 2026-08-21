---
name: apple-notes
description: Write owner-facing Apple Notes in the iCloud Coding folder — plans, designs, reviews, handoffs, rollouts, living Completion notes. Use whenever Monet produces something the owner needs to read, not only when they say "Notes." Title [APP, Monet] … with a refreshed timestamp.
---

# Apple Notes (MONET)

Mac only.  Cloud sessions: skip Notes, say so, leave the handoff in the PR.

Notes.app does not render raw Markdown.  The helper converts MD → HTML.  Pass `--html` only when you already have Notes-safe HTML.

## Helper

```bash
/Users/jay/apps/apple-notes-coding.sh "Title" "plain body"
/Users/jay/apps/apple-notes-coding.sh "Title" --html /path/to/body.html
/Users/jay/apps/apple-notes-coding.sh --update "Title" "body"
/Users/jay/apps/apple-notes-coding.sh --update "Title" --html /path/to/body.html
/Users/jay/apps/apple-notes-coding.sh --pin-only "Exact Title"
/Users/jay/apps/apple-notes-coding.sh --unpin-only "Exact Title"
```

Also: `--notify` / `--pushover`, `--needs-owner` / `--action-required`, `--summary "one sentence"`, `--pr "18"`.

Default is headless pin via the `Pin Coding Note` shortcut (no focus steal).  Do not `APPLE_NOTES_ACTIVATE=1` unless the owner is sitting at the Mac.

## Title

```
[APP, Monet] short topic
```

- Acronyms first, then `Monet` (Title Case, not `MONET`).
- Multi-app: `[ST, CT, Monet] …` (impact order).
- No date in the title.  No word "session".  Do not repeat the title as an H1 in the body.

| Acronym | App |
|---------|-----|
| UM | Usage-Monitor |
| ST | Socratic.Trade |
| CT | Congress.Trade |
| CTS | congress-trading-shared |
| DD | DealDex |
| PS | Personal-Site |
| FLEET | cross-app / infra / policy |

## Second body row

The helper injects/refreshes:

```
Sun, Aug 9, 3:52pm · PR #18
```

Local Mac time, no leading zeros, lowercase am/pm.  Refresh on every `--update`.

Then: type line (`Completion` / `Plan` / `Review` / `Design` / `Handoff` / `Rollout` / `Incident` / `Fleet change` / `Work log`), then content.

HTML: `<h2>` never `<h1>`; `<ul>/<li>`; `<b>`; `<div><br></div>` spacers.  Blank line between sections **and** bullets (owner reads on iPhone).

Order: `Needs owner` first when applicable, then Problem → What was done → Decisions → Next steps.

Two ASCII spaces between sentences in the body file you pass the helper.

## When

Do Notes: plans, design docs, reviews, handoffs, rollouts, **Completion / work-complete** for anything the owner might ask about.

Skip: pure `#agent-sync` chatter, effort-board row edits, routine commit messages, peer-only PR nits.

Open a living work note when substantial work starts.  Always Completion at the end.  Update in place; unpin stale Completion notes when the lane closes (`--unpin-only`).

Background-jobs inventory note is `⭐️ Background Jobs Master List` — refresh that title exactly when `MAC-LOCAL-PROCESSES.md` changes.

## Canon

- `/Users/jay/apps/AGENT-SYNC.md` § Apple Notes
- Skills: `closeout`, `owner-copy`
