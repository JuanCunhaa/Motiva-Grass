#!/usr/bin/env python3
"""Verify vendored public skills without executing their content."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from skills_common import file_manifest, load_yaml_json, parse_frontmatter, tree_sha256, write_yaml_json


def verify(repo: Path, lock_path: Path) -> dict[str, object]:
    lock = load_yaml_json(lock_path)
    failures: list[dict[str, str]] = []
    checked = 0
    for skill in lock.get("skills", []):
        if not skill.get("vendored"):
            continue
        checked += 1
        skill_id = str(skill["id"])
        vendor_path = repo / str(skill["vendor_path"])
        if not vendor_path.is_dir():
            failures.append({"skill": skill_id, "code": "MISSING_DIRECTORY", "detail": str(vendor_path)})
            continue
        actual_files = file_manifest(vendor_path)
        expected_files = skill.get("files", [])
        actual_by_path = {item["path"]: item for item in actual_files}
        expected_by_path = {item["path"]: item for item in expected_files}
        for missing in sorted(set(expected_by_path) - set(actual_by_path)):
            failures.append({"skill": skill_id, "code": "MISSING_FILE", "detail": missing})
        for extra in sorted(set(actual_by_path) - set(expected_by_path)):
            failures.append({"skill": skill_id, "code": "EXTRA_FILE", "detail": extra})
        for relative in sorted(set(actual_by_path) & set(expected_by_path)):
            if actual_by_path[relative] != expected_by_path[relative]:
                failures.append({"skill": skill_id, "code": "HASH_OR_SIZE_MISMATCH", "detail": relative})
        actual_tree = tree_sha256(actual_files)
        if actual_tree != skill.get("tree_sha256"):
            failures.append({"skill": skill_id, "code": "TREE_HASH_MISMATCH", "detail": actual_tree})
        skill_file = vendor_path / "SKILL.md"
        try:
            frontmatter = parse_frontmatter(skill_file)
            if frontmatter["name"] != skill.get("frontmatter_name"):
                failures.append({"skill": skill_id, "code": "FRONTMATTER_NAME_MISMATCH", "detail": frontmatter["name"]})
        except (OSError, ValueError) as exc:
            failures.append({"skill": skill_id, "code": "INVALID_FRONTMATTER", "detail": str(exc)})
    for source_id, source in lock.get("sources", {}).items():
        commit = str(source.get("commit", ""))
        if len(commit) != 40 or any(character not in "0123456789abcdef" for character in commit.lower()):
            failures.append({"skill": source_id, "code": "INVALID_SOURCE_COMMIT", "detail": commit})
    return {
        "schema_version": 1,
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "lockfile": str(lock_path.relative_to(repo)),
        "checked_vendored_skills": checked,
        "passed": not failures,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--lock", type=Path, default=Path("config/skills/skills-lock.yaml"))
    parser.add_argument("--output", type=Path, default=Path("reports/skills/integrity-results.json"))
    args = parser.parse_args()
    repo = args.repo.resolve()
    lock_path = args.lock if args.lock.is_absolute() else repo / args.lock
    output = args.output if args.output.is_absolute() else repo / args.output
    result = verify(repo, lock_path)
    write_yaml_json(output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
