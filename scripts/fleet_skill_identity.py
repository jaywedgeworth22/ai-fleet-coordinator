#!/usr/bin/env python3
"""Specialize Monet-canonical fleet SKILL.md text for a destination seat.

docs/fleet-skills stays the Monet / Claude.app upload pack.  Platform installs
must rewrite Slack tags, Notes names, branch prefixes, and worktree suffixes
or Cursor (and peers) will sign as Monet.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

IDENTITY_TOKEN = "@@SEAT_IDENTITY_PARAGRAPH@@"
YOU_ARE_TOKEN = "@@SEAT_YOU_ARE@@"
SEAT_LINE_TOKEN = "@@SEAT_BRANCH_LINE@@"
NEVER_PUSH_TOKEN = "@@SEAT_NEVER_PUSH@@"


@dataclass(frozen=True)
class Seat:
    tag: str
    notes: str
    prefix: str
    suffix: str
    dest: str
    mode: str
    identity_paragraph: str


CURSOR_IDENTITY = (
    "This pack is for the **CURSOR** seat (Cursor IDE, Auto, and Cursor cloud "
    "agents that run as Cursor).  Tag `[CURSOR]`.  Notes name `Cursor`.  "
    "Branches `cursor/<slug>` only.  Worktrees `~/apps/<prefix>-cursor`.  "
    "Never post Slack as `[MONET]`, `[CLAUDE]`, or `[GROK]`.  A skill copied "
    "from the Monet pack is not your name — this install is.  Pin "
    "`AGENT_SEAT=CURSOR`.  Incident: 2026-08-23 Cursor inherited Monet identity "
    "from an unspecialized skill copy."
)

AG_IDENTITY = (
    "This pack is for **AG** (Antigravity / Gemini).  Tag `[AG]`.  Notes name "
    "`AG`.  Branches `ag/<slug>` (keep `agent/antigravity` only if the lane "
    "already uses it).  Worktrees `~/apps/<prefix>-antigravity`.  Never sign "
    "as Monet or Cursor.  Pin `AGENT_SEAT=AG`."
)

CODEX_IDENTITY = (
    "This pack is for **CODEX**.  Tag `[CODEX]`.  Notes name `Codex`.  "
    "Branches `codex/<slug>` only.  Worktrees `~/apps/<prefix>-codex`.  "
    "Never sign as Monet.  Pin `AGENT_SEAT=CODEX`."
)

GROK_IDENTITY = (
    "This pack is for the **GROK** Mac TUI / CLI seat.  Tag `[GROK]`.  "
    "Notes name `Grok`.  Branches `grok/<slug>` only.  Worktrees "
    "`~/apps/<prefix>-grok`.  GROK-BUILD is a different seat "
    "(`grok-build/`, `~/apps/<prefix>-grok-build`).  `~/.grok` is shared; pin "
    "`AGENT_SEAT=GROK` unless this session is GROK-BUILD.  Never sign as Monet."
)

MONET_PACK_LINE = (
    "This pack is for the **MONET** Claude account.  Tag `[MONET]`.  "
    "Notes name `Monet`.  Branches `monet/<slug>` only."
)

MONET_CLAUDE_SHARED_PARA = (
    "CLAUDE and MONET are two different Claude accounts.  Local `~/.claude` "
    "(hooks, memory, skills) is shared.  The worktree folder is **not** a seat "
    "signal.  Pin `AGENT_SEAT=MONET`.  If the owner did not name Monet and the "
    "worktree is anonymous, **ask** — do not default to CLAUDE.  Incident: "
    "2026-07-05 CLAUDE↔MONET ping-pong from inferred seats."
)

CLAUDE_SHARED_BANNER = (
    "> **Shared `~/.claude/skills`.** Monet and Claude both load this directory.  "
    "Do not treat the word Monet in examples as proof of your seat.  Pin "
    "`AGENT_SEAT` / `AGENT_TAG` to `MONET` or `CLAUDE` from the logged-in "
    "account before Slack or `board --by`.  Branches `monet/` vs `claude/`.  "
    "Worktrees `~/apps/<prefix>-monet` vs `~/apps/<prefix>-claude`.  Cursor, "
    "Grok, Codex, and AG have their own skill dirs and must not take identity "
    "from here.\n\n"
)

SEATS: dict[str, Seat] = {
    "cursor": Seat(
        "CURSOR", "Cursor", "cursor", "cursor",
        "~/.cursor/skills", "exclusive", CURSOR_IDENTITY,
    ),
    "ag": Seat(
        "AG", "AG", "ag", "antigravity",
        "~/.gemini/skills", "exclusive", AG_IDENTITY,
    ),
    "codex": Seat(
        "CODEX", "Codex", "codex", "codex",
        "~/.codex/skills", "exclusive", CODEX_IDENTITY,
    ),
    "grok": Seat(
        "GROK", "Grok", "grok", "grok",
        "~/.grok/skills", "exclusive", GROK_IDENTITY,
    ),
    "claude_shared": Seat(
        "MONET", "Monet", "monet", "monet",
        "~/.claude/skills", "claude_shared", MONET_PACK_LINE,
    ),
}

IDENTITY_SKILL_NAMES = {
    "session-start",
    "board-ops",
    "closeout",
    "apple-notes",
    "land-lane",
    "pickup-seat",
    "owner-copy",
    "secret-handoff",
    "deploy-verify",
    "ios-ship",
    "unstick-pr",
    "codex-triage",
    "fleet-coordination",
}

_PROTECT = [
    ("Monet's portable", "@@PORTABLE1@@"),
    ("Monet portable", "@@PORTABLE2@@"),
    ("Monet's protocol", "@@PORTABLE3@@"),
    ("Socratic.Trade-monet", "@@LANE1@@"),
    ("agent/monet", "@@LANE2@@"),
    ("CLAUDE↔MONET", "@@INCIDENT@@"),
    ("Monet, Renoir, and Claude Code", "@@PS1@@"),
    ("Monet/Renoir/Claude", "@@PS2@@"),
]


def _protect(text: str) -> str:
    for src, tok in _PROTECT:
        text = text.replace(src, tok)
    return text


def _unprotect(text: str) -> str:
    for src, tok in _PROTECT:
        text = text.replace(tok, src)
    return text


def _install_banner(seat: Seat) -> str:
    return (
        f"> **This install is for `{seat.tag}`.** Slack `[{seat.tag}]`.  "
        f"Notes `{seat.notes}`.  Branches `{seat.prefix}/`.  Worktrees "
        f"`~/apps/<app>-{seat.suffix}`.  Do not inherit another seat's tag "
        f"from a shared Monet template.\n\n"
    )


def _insert_after_first_heading(text: str, block: str) -> str:
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return "".join(lines[: i + 1] + ["\n", block] + lines[i + 1 :])
    return block + text


def _stash_identity_source(text: str) -> str:
    text = text.replace(MONET_PACK_LINE + "\n\n" + MONET_CLAUDE_SHARED_PARA, IDENTITY_TOKEN)
    text = text.replace(MONET_PACK_LINE, IDENTITY_TOKEN)
    text = text.replace(MONET_CLAUDE_SHARED_PARA, "")
    text = text.replace("You are **MONET**.  Keep `monet/` branches.", YOU_ARE_TOKEN)
    text = text.replace(
        "Seat: **MONET**.  Branch: `monet/<slug>`.  Never `claude/`.",
        SEAT_LINE_TOKEN,
    )
    text = text.replace("Seat: **MONET**.  Branch: `monet/<slug>`.", SEAT_LINE_TOKEN)
    text = text.replace(
        "Never open or push `claude/*` from a Monet session.",
        NEVER_PUSH_TOKEN,
    )
    return text


def _unstash_identity(text: str, seat: Seat) -> str:
    text = text.replace(IDENTITY_TOKEN, seat.identity_paragraph)
    text = text.replace(
        YOU_ARE_TOKEN,
        f"You are **{seat.tag}**.  Keep `{seat.prefix}/` branches.",
    )
    text = text.replace(
        SEAT_LINE_TOKEN,
        f"Seat: **{seat.tag}**.  Branch: `{seat.prefix}/<slug>`.  "
        f"Never `claude/`.  Never `monet/`.",
    )
    text = text.replace(
        NEVER_PUSH_TOKEN,
        f"Never open or push `claude/*` or `monet/*` from a {seat.notes} "
        f"session.  Only `{seat.prefix}/`.",
    )
    return text


def specialize_from_monet(text: str, seat: Seat, skill_name: str = "") -> str:
    if seat.mode == "claude_shared":
        out = _insert_after_first_heading(text, CLAUDE_SHARED_BANNER)
        out = out.replace(
            "AGENT_SEAT=MONET",
            'AGENT_SEAT="${AGENT_SEAT:?set MONET or CLAUDE}"',
        )
        out = out.replace(
            "AGENT_TAG=MONET",
            'AGENT_TAG="${AGENT_SEAT:?set MONET or CLAUDE}"',
        )
        out = out.replace("--by MONET", '--by "$AGENT_SEAT"')
        out = out.replace("--mine MONET", '--mine "$AGENT_SEAT"')
        return out

    text = _stash_identity_source(text)
    text = _protect(text)

    ordered = [
        ("AGENT_SEAT=MONET", f"AGENT_SEAT={seat.tag}"),
        ("AGENT_TAG=MONET", f"AGENT_TAG={seat.tag}"),
        ("SLACK_AGENT_NAME=MONET", f"SLACK_AGENT_NAME={seat.tag}"),
        ("--by MONET", f"--by {seat.tag}"),
        ("--mine MONET", f"--mine {seat.tag}"),
        ("[MONET->", f"[{seat.tag}->"),
        ("[MONET]", f"[{seat.tag}]"),
        ("`[MONET`", f"`[{seat.tag}`"),
        ("**MONET**", f"**{seat.tag}**"),
        ("(MONET)", f"({seat.tag})"),
        ("# Session start (MONET)", f"# Session start ({seat.tag})"),
        ("# Pick up a seat (MONET)", f"# Pick up a seat ({seat.tag})"),
        ("# Closeout (MONET)", f"# Closeout ({seat.tag})"),
        ("# Apple Notes (MONET)", f"# Apple Notes ({seat.tag})"),
        ("# THE BOARD (MONET)", f"# THE BOARD ({seat.tag})"),
        ("# Land a feature branch (MONET)", f"# Land a feature branch ({seat.tag})"),
        ("# Owner-facing copy (MONET)", f"# Owner-facing copy ({seat.tag})"),
        ("# Secret handoff (MONET)", f"# Secret handoff ({seat.tag})"),
        ("# Deploy verification (MONET)", f"# Deploy verification ({seat.tag})"),
        ("# iOS agent loop (MONET)", f"# iOS agent loop ({seat.tag})"),
        ("# Unstick a blocked PR (MONET)", f"# Unstick a blocked PR ({seat.tag})"),
        ("# Review-thread triage (MONET)", f"# Review-thread triage ({seat.tag})"),
        ("monet/<slug>", f"{seat.prefix}/<slug>"),
        ("monet/fix", f"{seat.prefix}/fix"),
        ("`monet/", f"`{seat.prefix}/"),
        (" monet/", f" {seat.prefix}/"),
        ("-b monet/", f"-b {seat.prefix}/"),
        ("@ monet/", f"@ {seat.prefix}/"),
        ("-monet-", f"-{seat.suffix}-"),
        ("-monet`", f"-{seat.suffix}`"),
        ("-monet ", f"-{seat.suffix} "),
        ("-monet\n", f"-{seat.suffix}\n"),
        ("-monet (", f"-{seat.suffix} ("),
        ("Monet worktree", f"{seat.notes} worktree"),
        ("Monet session", f"{seat.notes} session"),
        ("every Monet", f"every {seat.notes}"),
        ("Start every Monet", f"Start every {seat.notes}"),
        ("Finish a Monet", f"Finish a {seat.notes}"),
        ("Land a Monet", f"Land a {seat.notes}"),
        ("whenever Monet", f"whenever {seat.notes}"),
        ("Notes name `Monet`", f"Notes name `{seat.notes}`"),
        ("then `Monet`", f"then `{seat.notes}`"),
        ("[APP, Monet]", f"[APP, {seat.notes}]"),
        ("(Monet):", f"({seat.notes}):"),
        ("Monet (not Claude)", f"{seat.notes} (not another seat)"),
        ("Monet — never skip", f"{seat.notes} — never skip"),
    ]
    for old, new in ordered:
        text = text.replace(old, new)

    text = text.replace("MONET", seat.tag)
    text = text.replace("Monet", seat.notes)
    text = _unstash_identity(text, seat)
    text = _unprotect(text)

    if skill_name in IDENTITY_SKILL_NAMES:
        text = _insert_after_first_heading(text, _install_banner(seat))
    return text


def platform_installs() -> list[tuple[str, Seat]]:
    return [
        (os.path.expanduser("~/.cursor/skills"), SEATS["cursor"]),
        (os.path.expanduser("~/.gemini/skills"), SEATS["ag"]),
        (os.path.expanduser("~/.claude/skills"), SEATS["claude_shared"]),
        (os.path.expanduser("~/.codex/skills"), SEATS["codex"]),
        (os.path.expanduser("~/.grok/skills"), SEATS["grok"]),
    ]
