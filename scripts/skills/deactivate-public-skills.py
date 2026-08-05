#!/usr/bin/env python3
"""Remove only public skills recorded as active by Motiva-Grass."""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path

from skills_common import ensure_within, load_yaml_json, write_yaml_json


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.resolve()
    root = repo / ".agents/skills/public"
    state_path = repo / ".agents/runtime/active-skills.json"
    state = load_yaml_json(state_path) if state_path.exists() else {"active": []}
    removed: list[str] = []
    for item in state.get("active", []):
        skill_id = str(item["id"])
        destination = ensure_within(root, root / skill_id)
        if destination.exists():
            shutil.rmtree(destination)
            removed.append(skill_id)
    write_yaml_json(
        state_path,
        {"schema_version": 1, "deactivated_at": datetime.now(timezone.utc).isoformat(), "active": []},
    )
    print(f"Deactivated {len(removed)} public skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
