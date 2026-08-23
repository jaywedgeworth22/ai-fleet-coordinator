#!/usr/bin/env python3
"""Install and sync fleet skills across agent platforms on this machine.

Canonical source (`docs/fleet-skills`) is the Monet / Claude.app pack.
Each platform destination is specialized so Slack tags, Notes names,
branch prefixes, and worktree suffixes match that seat.  Copying Monet
skills into Cursor unchanged made Cursor sign as Monet.
"""

from __future__ import annotations

import os
import shutil
import zipfile

from fleet_skill_identity import platform_installs, specialize_from_monet

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_SKILLS = os.path.join(REPO_ROOT, "docs", "fleet-skills")
ROOT_SKILLS = os.path.join(REPO_ROOT, "skills")


def _skill_names() -> list[str]:
    return sorted(
        d
        for d in os.listdir(DOCS_SKILLS)
        if os.path.isdir(os.path.join(DOCS_SKILLS, d)) and not d.startswith(".")
    )


def main() -> None:
    skill_names = _skill_names()
    print(f"Found {len(skill_names)} fleet skills in {DOCS_SKILLS}:")
    for name in skill_names:
        print(f"  - {name}")

    os.makedirs(ROOT_SKILLS, exist_ok=True)

    for name in skill_names:
        src_md = os.path.join(DOCS_SKILLS, name, "SKILL.md")
        if not os.path.isfile(src_md):
            continue
        with open(src_md, encoding="utf-8") as f:
            monet_src = f.read()

        root_dest = os.path.join(ROOT_SKILLS, name)
        os.makedirs(root_dest, exist_ok=True)
        shutil.copy2(src_md, os.path.join(root_dest, "SKILL.md"))

        zip_path = os.path.join(DOCS_SKILLS, f"{name}.zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(src_md, arcname=os.path.join(name, "SKILL.md"))

        for dest_base, seat in platform_installs():
            dest_dir = os.path.join(dest_base, name)
            os.makedirs(dest_dir, exist_ok=True)
            rendered = specialize_from_monet(monet_src, seat, skill_name=name)
            dest_path = os.path.join(dest_dir, "SKILL.md")
            with open(dest_path, "w", encoding="utf-8") as f:
                f.write(rendered)

    print("\nInstalled specialized fleet skills:")
    for dest, seat in platform_installs():
        print(f"  {seat.tag:8}  {dest}")


if __name__ == "__main__":
    main()
