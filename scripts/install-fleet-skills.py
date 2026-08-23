#!/usr/bin/env python3
"""Install fleet skills to every agent platform, specialized per seat.

Canonical source: docs/fleet-skills (Monet / Claude.app pack).
Home dirs and docs/fleet-skills/by-seat/<seat>/ get rewritten identity.
"""

from __future__ import annotations

import os
import shutil
import zipfile

from fleet_skill_identity import (
    SEATS,
    catalog_seats,
    platform_installs,
    specialize_from_monet,
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_SKILLS = os.path.join(REPO_ROOT, "docs", "fleet-skills")
ROOT_SKILLS = os.path.join(REPO_ROOT, "skills")
BY_SEAT = os.path.join(DOCS_SKILLS, "by-seat")


def _skill_names() -> list[str]:
    return sorted(
        d
        for d in os.listdir(DOCS_SKILLS)
        if os.path.isdir(os.path.join(DOCS_SKILLS, d))
        and not d.startswith(".")
        and d != "by-seat"
    )


def _write_skill(path: str, body: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)


def _zip_skill(zip_path: str, skill_name: str, md_path: str) -> None:
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(md_path, arcname=os.path.join(skill_name, "SKILL.md"))


def main() -> None:
    skill_names = _skill_names()
    print(f"Found {len(skill_names)} fleet skills in {DOCS_SKILLS}:")
    for name in skill_names:
        print(f"  - {name}")

    os.makedirs(ROOT_SKILLS, exist_ok=True)
    os.makedirs(BY_SEAT, exist_ok=True)

    sources: dict[str, str] = {}
    for name in skill_names:
        src_md = os.path.join(DOCS_SKILLS, name, "SKILL.md")
        if not os.path.isfile(src_md):
            continue
        with open(src_md, encoding="utf-8") as f:
            sources[name] = f.read()
        root_dest = os.path.join(ROOT_SKILLS, name)
        os.makedirs(root_dest, exist_ok=True)
        shutil.copy2(src_md, os.path.join(root_dest, "SKILL.md"))
        _zip_skill(os.path.join(DOCS_SKILLS, f"{name}.zip"), name, src_md)

    for dest_base, seat in platform_installs():
        for name, monet_src in sources.items():
            rendered = specialize_from_monet(monet_src, seat, skill_name=name)
            dest_dir = os.path.join(dest_base, name)
            os.makedirs(dest_dir, exist_ok=True)
            _write_skill(os.path.join(dest_dir, "SKILL.md"), rendered)

    for seat in catalog_seats():
        key = seat.seat_key or seat.tag.lower()
        seat_root = os.path.join(BY_SEAT, key)
        for name, monet_src in sources.items():
            rendered = specialize_from_monet(monet_src, seat, skill_name=name)
            md_path = os.path.join(seat_root, name, "SKILL.md")
            _write_skill(md_path, rendered)
            _zip_skill(os.path.join(seat_root, f"{name}.zip"), name, md_path)

    print("\nHome-dir installs:")
    for dest, seat in platform_installs():
        print(f"  {seat.tag:12}  {dest}")
    print("\nUpload packs: docs/fleet-skills/by-seat/<seat>/")
    for seat in catalog_seats():
        print(f"  {seat.tag:12}  {seat.seat_key}")


if __name__ == "__main__":
    main()
