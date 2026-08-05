#!/usr/bin/env python3
"""Check for upstream changes without replacing pinned vendor content."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from skills_common import load_yaml_json, write_yaml_json


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Explicitly authorize a read-only upstream check")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    if not args.check:
        parser.error("Updates are never checked implicitly; pass --check")
    repo = args.repo.resolve()
    lock = load_yaml_json(repo / "config/skills/skills-lock.yaml")
    changes: list[dict[str, object]] = []
    for source_id, source in lock["sources"].items():
        repository = source["repository"]
        result = subprocess.run(
            ["git", "ls-remote", f"https://github.com/{repository}.git", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        latest = result.stdout.split()[0]
        changes.append(
            {
                "source": source_id,
                "repository": repository,
                "pinned_commit": source["commit"],
                "observed_head": latest,
                "update_available": latest != source["commit"],
                "requires_new_static_audit": latest != source["commit"],
                "vendor_modified": False,
            }
        )
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "changes": changes}
    write_yaml_json(repo / "reports/skills/update-candidates.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
