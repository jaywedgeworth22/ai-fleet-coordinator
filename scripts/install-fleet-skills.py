#!/usr/bin/env python3
"""
Install and sync fleet skills across all agent platforms on this machine
(Antigravity/Gemini, Cursor, Claude Code, etc.).
"""

import os
import shutil
import zipfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_SKILLS = os.path.join(REPO_ROOT, "docs", "fleet-skills")
ROOT_SKILLS = os.path.join(REPO_ROOT, "skills")

DESTINATIONS = [
    os.path.expanduser("~/.gemini/skills"),
    os.path.expanduser("~/.cursor/skills"),
    os.path.expanduser("~/.claude/skills"),
]

def main():
    skill_names = [
        d for d in os.listdir(DOCS_SKILLS)
        if os.path.isdir(os.path.join(DOCS_SKILLS, d)) and not d.startswith(".")
    ]
    
    print(f"Found {len(skill_names)} fleet skills in {DOCS_SKILLS}:")
    for name in sorted(skill_names):
        print(f"  - {name}")

    os.makedirs(ROOT_SKILLS, exist_ok=True)

    for name in skill_names:
        src_skill_dir = os.path.join(DOCS_SKILLS, name)
        src_skill_md = os.path.join(src_skill_dir, "SKILL.md")
        if not os.path.exists(src_skill_md):
            continue

        # 1. Mirror to root skills/
        root_dest = os.path.join(ROOT_SKILLS, name)
        os.makedirs(root_dest, exist_ok=True)
        shutil.copy2(src_skill_md, os.path.join(root_dest, "SKILL.md"))

        # 2. Build .zip in docs/fleet-skills/
        zip_path = os.path.join(DOCS_SKILLS, f"{name}.zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(src_skill_md, arcname=os.path.join(name, "SKILL.md"))

        # 3. Install to all destination platforms
        for dest_base in DESTINATIONS:
            dest_dir = os.path.join(dest_base, name)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy2(src_skill_md, os.path.join(dest_dir, "SKILL.md"))

    print("\n✅ Successfully installed and refreshed fleet skills across:")
    for dest in DESTINATIONS:
        print(f"  ✓ {dest}")

if __name__ == "__main__":
    main()
