#!/usr/bin/env python3
"""Build the deterministic skills lock from audited snapshots and vendor copies."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

from skills_common import file_manifest, load_yaml_json, parse_frontmatter, tree_sha256, write_yaml_json

SOURCE_WORKTREES = {
    "github-awesome-copilot": "github-awesome-copilot",
    "vercel-next-skills": "vercel-next-skills",
    "vercel-agent-skills": "vercel-agent-skills",
    "trailofbits": "trailofbits",
    "huggingface": "huggingface",
}
SCRIPT_SUFFIXES = {".py", ".sh", ".ps1", ".js", ".mjs", ".cjs", ".ts"}


def static_metadata(root: Path) -> dict[str, object]:
    network = 0
    shell = 0
    executables: list[str] = []
    dependencies: set[str] = set()
    tools: set[str] = set()
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        relative = path.relative_to(root).as_posix()
        if path.suffix.lower() in SCRIPT_SUFFIXES:
            executables.append(relative)
        if path.stat().st_size > 3_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        network += len(re.findall(r"https?://|\bcurl\b|\bwget\b|fetch\(|requests\.|urllib|git\s+clone", text, re.I))
        shell += len(re.findall(r"```(?:bash|sh|shell|powershell|cmd)|subprocess\.|os\.system|child_process", text, re.I))
        for name in re.findall(r"\b(git|python3?|node|npm|npx|pnpm|uv|pytest|semgrep|codeql|hf|vercel|playwright)\b", text, re.I):
            tools.add(name.lower())
        for name in re.findall(r"\b(?:pip install|uv add|npm install|pnpm add)\s+([A-Za-z0-9_.@/-]+)", text, re.I):
            dependencies.add(name)
    return {
        "dependencies": sorted(dependencies),
        "tools_required": sorted(tools),
        "network_references": network,
        "shell_command_blocks": shell,
        "scripts_executable": executables,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--catalog", type=Path, default=Path("config/skills/public-skills-catalog.yaml"))
    parser.add_argument("--audit-root", type=Path, default=Path(".tmp-skills-audit"))
    parser.add_argument("--output", type=Path, default=Path("config/skills/skills-lock.yaml"))
    args = parser.parse_args()
    repo = args.repo.resolve()
    catalog = load_yaml_json(repo / args.catalog)
    audit_root = repo / args.audit_root
    skills: list[dict[str, object]] = []
    for item in catalog["skills"]:
        source_root = audit_root / SOURCE_WORKTREES[item["source"]]
        audit_path = source_root / item["source_path"]
        downloaded = audit_path.is_dir()
        entries = file_manifest(audit_path) if downloaded else []
        frontmatter_name = None
        upstream_version = None
        frontmatter_valid = False
        skill_file = audit_path / "SKILL.md"
        if skill_file.is_file():
            try:
                frontmatter = parse_frontmatter(skill_file)
                frontmatter_name = frontmatter["name"]
                frontmatter_valid = True
                version_match = re.search(r"(?m)^\s*version:\s*[\"']?([^\"'\r\n]+)", skill_file.read_text(encoding="utf-8"))
                upstream_version = version_match.group(1).strip() if version_match else None
            except ValueError:
                pass
        vendor_path = repo / item["vendor_path"] if item.get("vendor_path") else None
        vendored = bool(vendor_path and vendor_path.is_dir())
        vendor_entries = file_manifest(vendor_path) if vendored and vendor_path else []
        if vendored and vendor_entries != entries:
            raise ValueError(f"Vendor copy differs from audited snapshot: {item['id']}")
        metadata = static_metadata(audit_path) if downloaded else {
            "dependencies": [], "tools_required": [], "network_references": 0,
            "shell_command_blocks": 0, "scripts_executable": []
        }
        enriched = dict(item)
        enriched.update(
            {
                "repository": catalog["sources"][item["source"]]["repository"],
                "commit": catalog["sources"][item["source"]]["commit"],
                "license": catalog["sources"][item["source"]]["license"],
                "downloaded": downloaded,
                "vendored": vendored,
                "frontmatter_valid": frontmatter_valid,
                "frontmatter_name_observed": frontmatter_name,
                "upstream_version": upstream_version,
                "file_count": len(entries),
                "tree_sha256": tree_sha256(entries),
                "files": entries,
                "audit_date": "2026-08-05",
                "auditor": "Codex",
                **metadata,
            }
        )
        skills.append(enriched)
    lock = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generated_by": "Codex",
        "hash_algorithm": "sha256(path NUL size NUL file_sha256 LF, sorted by path)",
        "sources": catalog["sources"],
        "skills": skills,
    }
    write_yaml_json(repo / args.output, lock)
    write_yaml_json(
        repo / ".agents/skills/skills-manifest.yaml",
        {
            "schema_version": 1,
            "lockfile": "config/skills/skills-lock.yaml",
            "catalog": "config/skills/public-skills-catalog.yaml",
            "routing": "config/skills/jira-skill-routing.yaml",
            "public_skill_count": len(skills),
            "own_skill_count": 17,
        },
    )
    print(f"Locked {len(skills)} public skill entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
