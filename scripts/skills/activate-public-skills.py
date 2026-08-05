#!/usr/bin/env python3
"""Activate only audited public skills for a Jira ticket or profile."""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path

from skills_common import ROUTABLE_STATUSES, ensure_within, load_yaml_json, write_yaml_json


def selected_ids(repo: Path, ticket: str | None, profile: str | None, include_conditional: bool) -> tuple[str, list[str]]:
    if ticket:
        routing = load_yaml_json(repo / "config/skills/jira-skill-routing.yaml")
        entry = routing.get("tickets", {}).get(ticket.upper())
        if not entry:
            raise ValueError(f"Ticket has no mapping: {ticket}")
        result = [item["id"] for item in entry.get("public_required", [])]
        if include_conditional:
            result.extend(item["id"] for item in entry.get("conditional", []) if item.get("kind") == "public")
        return f"ticket:{ticket.upper()}", list(dict.fromkeys(result))
    profiles = load_yaml_json(repo / "config/skills/activation-profiles.yaml").get("profiles", {})
    entry = profiles.get(str(profile))
    if not entry:
        raise ValueError(f"Unknown profile: {profile}")
    result = list(entry.get("public_required", []))
    if include_conditional:
        result.extend(entry.get("public_conditional", []))
    return f"profile:{profile}", list(dict.fromkeys(result))


def main() -> int:
    parser = argparse.ArgumentParser()
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--ticket")
    selection.add_argument("--profile")
    parser.add_argument("--include-conditional", action="store_true")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.resolve()
    source_label, ids = selected_ids(repo, args.ticket, args.profile, args.include_conditional)
    lock = load_yaml_json(repo / "config/skills/skills-lock.yaml")
    by_id = {skill["id"]: skill for skill in lock["skills"]}
    destination_root = repo / ".agents/skills/public"
    destination_root.mkdir(parents=True, exist_ok=True)
    active: list[dict[str, str]] = []
    for skill_id in ids:
        skill = by_id.get(skill_id)
        if not skill:
            raise ValueError(f"Skill is absent from lockfile: {skill_id}")
        if skill["audit_status"] not in ROUTABLE_STATUSES or not skill.get("vendored"):
            raise ValueError(f"Skill is not activatable: {skill_id} ({skill['audit_status']})")
        source = ensure_within(repo / "vendor/agent-skills", repo / skill["vendor_path"])
        destination = ensure_within(destination_root, destination_root / skill_id)
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
        active.append({"id": skill_id, "tree_sha256": skill["tree_sha256"]})
    write_yaml_json(
        repo / ".agents/runtime/active-skills.json",
        {
            "schema_version": 1,
            "activated_at": datetime.now(timezone.utc).isoformat(),
            "selection": source_label,
            "conditional_included": args.include_conditional,
            "active": active,
        },
    )
    print(f"Activated {len(active)} public skills for {source_label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
