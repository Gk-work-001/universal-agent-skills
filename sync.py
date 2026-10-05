#!/usr/bin/env python3
"""
Universal Agent Skills Synchronizer
Exports and syncs platform-agnostic skills to any AI IDE or Agent:
Cursor, Windsurf, Claude Code, GitHub Copilot, Cline/Roo Code, Antigravity.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent / "skills"

def parse_frontmatter(content: str):
    """Simple YAML frontmatter parser."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    frontmatter_text = parts[1]
    body = parts[2]
    meta = {}
    for line in frontmatter_text.splitlines():
        line = line.strip()
        if ":" in line:
            key, val = line.split(":", 1)
            meta[key.strip()] = val.strip()
    return meta, body

def list_skills():
    skills = []
    for s in SKILLS_DIR.iterdir():
        if s.is_dir() and (s / "SKILL.md").exists():
            content = (s / "SKILL.md").read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(content)
            skills.append((s.name, meta.get("description", "No description")))
    return skills

def sync_to_cursor(target_root: Path, skills):
    rules_dir = target_root / ".cursor" / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)
    for skill_name, _ in skills:
        src = SKILLS_DIR / skill_name / "SKILL.md"
        dest = rules_dir / f"{skill_name}.mdc"
        content = src.read_text(encoding="utf-8")
        dest.write_text(content, encoding="utf-8")
        print(f" [+] Exported to Cursor: {dest.relative_to(target_root)}")

def sync_to_windsurf(target_root: Path, skills):
    dest = target_root / ".windsurfrules"
    existing = dest.read_text(encoding="utf-8") if dest.exists() else ""
    append_chunks = []
    for skill_name, _ in skills:
        marker = f"<!-- SKILL: {skill_name} -->"
        if marker not in existing:
            content = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
            append_chunks.append(f"\n{marker}\n{content}\n")
    if append_chunks:
        with open(dest, "a", encoding="utf-8") as f:
            f.write("\n".join(append_chunks))
        print(f" [+] Exported to Windsurf: {dest.name}")

def sync_to_copilot(target_root: Path, skills):
    dest_dir = target_root / ".github"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "copilot-instructions.md"
    existing = dest.read_text(encoding="utf-8") if dest.exists() else ""
    append_chunks = []
    for skill_name, _ in skills:
        marker = f"<!-- SKILL: {skill_name} -->"
        if marker not in existing:
            content = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
            append_chunks.append(f"\n{marker}\n{content}\n")
    if append_chunks:
        with open(dest, "a", encoding="utf-8") as f:
            f.write("\n".join(append_chunks))
        print(f" [+] Exported to Copilot: {dest.relative_to(target_root)}")

def sync_to_claude(target_root: Path, skills):
    dest = target_root / "CLAUDE.md"
    existing = dest.read_text(encoding="utf-8") if dest.exists() else ""
    append_chunks = []
    for skill_name, _ in skills:
        marker = f"<!-- SKILL: {skill_name} -->"
        if marker not in existing:
            content = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
            append_chunks.append(f"\n{marker}\n{content}\n")
    if append_chunks:
        with open(dest, "a", encoding="utf-8") as f:
            f.write("\n".join(append_chunks))
        print(f" [+] Exported to Claude Code: {dest.name}")

def sync_to_cline(target_root: Path, skills):
    dest = target_root / ".clinerules"
    existing = dest.read_text(encoding="utf-8") if dest.exists() else ""
    append_chunks = []
    for skill_name, _ in skills:
        marker = f"<!-- SKILL: {skill_name} -->"
        if marker not in existing:
            content = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
            append_chunks.append(f"\n{marker}\n{content}\n")
    if append_chunks:
        with open(dest, "a", encoding="utf-8") as f:
            f.write("\n".join(append_chunks))
        print(f" [+] Exported to Cline: {dest.name}")

def sync_to_antigravity(target_root: Path, skills):
    dest_dir = target_root / ".agent" / "skills"
    dest_dir.mkdir(parents=True, exist_ok=True)
    for skill_name, _ in skills:
        src = SKILLS_DIR / skill_name
        dest = dest_dir / skill_name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        print(f" [+] Exported to Antigravity / Agents: {dest.relative_to(target_root)}")

def main():
    parser = argparse.ArgumentParser(description="Sync universal skills to any AI IDE or Agent.")
    parser.add_argument("--target", choices=["cursor", "windsurf", "copilot", "claude", "cline", "antigravity", "all"], default="all")
    parser.add_argument("--dest", type=str, default=".", help="Target project root directory")
    parser.add_argument("--list", action="store_true", help="List available skills")
    args = parser.parse_args()

    skills = list_skills()
    if args.list:
        print("\nAvailable Universal Agent Skills:")
        for name, desc in skills:
            print(f"  • {name}: {desc[:80]}...")
        return

    dest = Path(args.dest).resolve()
    print(f"[*] Syncing skills to: {dest} (Target: {args.target})")

    if args.target in ("cursor", "all"):
        sync_to_cursor(dest, skills)
    if args.target in ("windsurf", "all"):
        sync_to_windsurf(dest, skills)
    if args.target in ("copilot", "all"):
        sync_to_copilot(dest, skills)
    if args.target in ("claude", "all"):
        sync_to_claude(dest, skills)
    if args.target in ("cline", "all"):
        sync_to_cline(dest, skills)
    if args.target in ("antigravity", "all"):
        sync_to_antigravity(dest, skills)

    print("\n[✔] Synchronization complete!")

if __name__ == "__main__":
    main()
