#!/usr/bin/env python3
"""Fetch pinned public skill sources with sparse checkout and no content execution."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from skills_common import ROUTABLE_STATUSES, load_yaml_json


def run(command: list[str], cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, check=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--apply", action="store_true", help="Replace vendored copies after the pinned snapshot is fetched")
    args = parser.parse_args()
    repo = args.repo.resolve()
    lock = load_yaml_json(repo / "config/skills/skills-lock.yaml")
    with tempfile.TemporaryDirectory(prefix="motiva-skills-") as temporary:
        temp_root = Path(temporary)
        for source_id, source in lock["sources"].items():
            source_skills = [skill for skill in lock["skills"] if skill["source"] == source_id]
            if not source_skills:
                continue
            checkout = temp_root / source_id
            run(["git", "clone", "--filter=blob:none", "--no-checkout", f"https://github.com/{source['repository']}.git", str(checkout)])
            run(["git", "sparse-checkout", "init", "--cone"], checkout)
            sparse_paths = sorted({skill["source_path"] for skill in source_skills})
            if source.get("license_evidence") and "#" not in str(source["license_evidence"]):
                sparse_paths.append(str(source["license_evidence"]))
            run(["git", "sparse-checkout", "set", *sparse_paths], checkout)
            run(["git", "checkout", "--detach", source["commit"]], checkout)
            if not args.apply:
                print(f"Fetched {source_id}@{source['commit']} (dry-run; vendor unchanged)")
                continue
            for skill in source_skills:
                if skill["audit_status"] not in ROUTABLE_STATUSES or not skill.get("vendor_path"):
                    continue
                source_path = checkout / skill["source_path"]
                if not (source_path / "SKILL.md").is_file():
                    raise FileNotFoundError(f"Missing SKILL.md for {skill['id']}")
                destination = repo / skill["vendor_path"]
                if destination.exists():
                    shutil.rmtree(destination)
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(source_path, destination)
        print("Fetch complete. Run audit and verify before activation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
