#!/usr/bin/env python3
"""Mirror fleet agent skills and rules into Google Drive.

Google Drive for desktop only syncs inside the CloudStorage mount.  Dotfolders
such as ~/.Gemini, ~/.cursor, ~/.claude, and ~/.grok cannot be added to native
sync directly.  This job mirrors the fleet-relevant subtrees into My Drive so
the desktop app backs them up automatically.

Layout under My Drive/fleet-agent-config/:
  gemini/skills/        <- ~/.Gemini/skills (or ~/.gemini/skills)
  cursor/skills/        <- ~/.cursor/skills
  cursor/skills-cursor/ <- ~/.cursor/skills-cursor
  cursor/rules/         <- ~/.cursor/rules
  claude/skills/        <- ~/.claude/skills
  grok/skills/          <- ~/.grok/skills

Also refreshes My Drive/fleet-skills/ from ai-fleet-coordinator docs/fleet-skills
(canonical git catalog + .zip packages for Claude app upload).

Usage:
  python3 scripts/sync-fleet-agent-config-to-gdrive.py
  python3 scripts/sync-fleet-agent-config-to-gdrive.py --list
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

GDRIVE_CANDIDATES = [
    Path("/Users/jay/Google Drive/My Drive"),
    Path("/Users/jay/Library/CloudStorage/GoogleDrive-jaywedgeworth22@gmail.com/My Drive"),
]

HOME = Path.home()
SCRIPT_DIR = Path(__file__).resolve().parent

FLEET_COORDINATOR_CANDIDATES = [
    SCRIPT_DIR.parent,
    Path("/Users/jay/Code/ai-fleet-coordinator"),
    HOME / "Code" / "ai-fleet-coordinator",
]


def fleet_coordinator_root() -> Path | None:
    for root in FLEET_COORDINATOR_CANDIDATES:
        if (root / "docs" / "fleet-skills").is_dir():
            return root
    return None


def docs_fleet_skills_path() -> Path | None:
    root = fleet_coordinator_root()
    if root is None:
        return None
    return root / "docs" / "fleet-skills"
AGENT_CONFIG_ROOT = "fleet-agent-config"
FLEET_SKILLS_ROOT = "fleet-skills"

# First existing home-relative path wins for each Drive destination.
MIRROR_SPECS: list[tuple[str, list[str]]] = [
    ("gemini/skills", [".Gemini/skills", ".gemini/skills"]),
    ("cursor/skills", [".cursor/skills"]),
    ("cursor/skills-cursor", [".cursor/skills-cursor"]),
    ("cursor/rules", [".cursor/rules"]),
    ("claude/skills", [".claude/skills"]),
    ("grok/skills", [".grok/skills"]),
]


def find_gdrive() -> Path:
    for cand in GDRIVE_CANDIDATES:
        if cand.is_dir():
            return cand
    print("Google Drive directory not found on this machine.", file=sys.stderr)
    sys.exit(1)


def resolve_home_source(rel_paths: list[str]) -> Path | None:
    for rel in rel_paths:
        path = HOME / rel
        if path.is_dir():
            return path
    return None


def rsync_mirror(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if shutil.which("rsync"):
        cmd = [
            "rsync",
            "-a",
            "--delete",
            "--exclude",
            ".DS_Store",
            f"{src}/",
            f"{dest}/",
        ]
        subprocess.run(cmd, check=True)
        return

    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(
        src,
        dest,
        ignore=shutil.ignore_patterns(".DS_Store"),
        dirs_exist_ok=True,
    )


def mirror_agent_config(gdrive: Path) -> list[str]:
    root = gdrive / AGENT_CONFIG_ROOT
    root.mkdir(parents=True, exist_ok=True)
    mirrored: list[str] = []

    for dest_rel, home_candidates in MIRROR_SPECS:
        src = resolve_home_source(home_candidates)
        if src is None:
            print(f"skip {dest_rel} (no source under {home_candidates})")
            continue
        dest = root / dest_rel
        print(f"mirror {src} -> {dest}")
        rsync_mirror(src, dest)
        mirrored.append(dest_rel)

    readme = root / "README.md"
    readme.write_text(
        "\n".join(
            [
                "# Fleet agent config mirror",
                "",
                "Mirrored from Mac home dotfolders by",
                "`scripts/sync-fleet-agent-config-to-gdrive.py`",
                "(launchd `com.jay.fleet-gdrive-backup`, daily 06:00).",
                "",
                "Google Drive desktop cannot sync ~/.Gemini / ~/.cursor /",
                "~/.claude / ~/.grok directly.  This folder is the backup copy.",
                "",
                "## Seats mirrored",
                "- `gemini/skills` — Antigravity / Gemini",
                "- `cursor/skills`, `cursor/skills-cursor`, `cursor/rules` — Cursor",
                "- `claude/skills` — Claude Code",
                "- `grok/skills` — Grok",
                "",
                "Canonical fleet skill source in git:",
                "`ai-fleet-coordinator/docs/fleet-skills/`.",
                "Upload packs for Claude.app also land in sibling `fleet-skills/`.",
                "",
            ]
        )
    )
    return mirrored


def mirror_fleet_skills_catalog(gdrive: Path) -> None:
    docs_fleet_skills = docs_fleet_skills_path()
    if docs_fleet_skills is None:
        print(f"skip {FLEET_SKILLS_ROOT} (ai-fleet-coordinator docs/fleet-skills not found)")
        return
    dest = gdrive / FLEET_SKILLS_ROOT
    print(f"mirror {docs_fleet_skills} -> {dest}")
    rsync_mirror(docs_fleet_skills, dest)


def list_planned(gdrive: Path) -> None:
    print(f"Google Drive: {gdrive}")
    print(f"Agent config root: {gdrive / AGENT_CONFIG_ROOT}")
    print(f"Fleet skills catalog: {gdrive / FLEET_SKILLS_ROOT}")
    for dest_rel, home_candidates in MIRROR_SPECS:
        src = resolve_home_source(home_candidates)
        mark = str(src) if src else "missing"
        print(f"  {dest_rel}\t{mark}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="Print planned mirrors and exit")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    gdrive = find_gdrive()
    if args.list:
        list_planned(gdrive)
        return 0

    mirrored = mirror_agent_config(gdrive)
    mirror_fleet_skills_catalog(gdrive)

    if not mirrored and docs_fleet_skills_path() is None:
        print("Nothing mirrored.", file=sys.stderr)
        return 1

    print(
        f"Mirrored {len(mirrored)} agent subtrees to {gdrive / AGENT_CONFIG_ROOT}; "
        f"refreshed {gdrive / FLEET_SKILLS_ROOT}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
