#!/usr/bin/env python3
"""Validate the complete Jira-to-skill routing matrix."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROUTABLE = {"APPROVED", "APPROVED_WITH_RESTRICTIONS"}
EXPECTED_KEYS = {"KAN-" + str(number) for number in range(1, 157)}


def duplicates(values: list[str]) -> set[str]:
    seen: set[str] = set()
    return {value for value in values if value in seen or seen.add(value) is None and False}


def validate(root: Path, mapping_path: Path | None = None) -> list[str]:
    errors: list[str] = []
    mapping_path = mapping_path or root / "config" / "skills" / "jira-skill-routing.yaml"
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    catalog = json.loads((root / "config" / "skills" / "public-skills-catalog.yaml").read_text(encoding="utf-8"))
    manifest = json.loads((root / ".agents" / "skills" / "skills-manifest.yaml").read_text(encoding="utf-8"))

    public = {item["id"]: item["audit_status"] for item in catalog["skills"]}
    own = {item["id"] for item in manifest["first_party"]}
    tickets = mapping.get("tickets", {})
    if set(tickets) != EXPECTED_KEYS:
        errors.append("ticket set differs from KAN-1..KAN-156")

    for key, ticket in tickets.items():
        own_ids = [item["id"] for item in ticket.get("own_required", [])]
        public_ids = [item["id"] for item in ticket.get("public_required", [])]
        conditional_ids = [item["id"] for item in ticket.get("conditional", [])]
        if len(own_ids) != len(set(own_ids)):
            errors.append(key + ": duplicate own_required")
        if len(public_ids) != len(set(public_ids)):
            errors.append(key + ": duplicate public_required")
        if len(conditional_ids) != len(set(conditional_ids)):
            errors.append(key + ": duplicate conditional")
        for item in ticket.get("own_required", []):
            if item["id"] not in own or item.get("status") != "VALIDATED":
                errors.append(key + ": invalid own skill " + item["id"])
        for skill_id in public_ids:
            if public.get(skill_id) not in ROUTABLE:
                errors.append(key + ": unroutable public skill " + skill_id)
        for item in ticket.get("conditional", []):
            skill_id = item["id"]
            if item.get("kind") == "own":
                if skill_id not in own:
                    errors.append(key + ": nonexistent conditional own skill " + skill_id)
            elif public.get(skill_id) not in ROUTABLE:
                errors.append(key + ": unroutable conditional skill " + skill_id)
            if not item.get("condition"):
                errors.append(key + ": conditional without condition " + skill_id)
        order = ticket.get("execution_order", [])
        for required in ("motiva-jira-ticket-executor", "motiva-ticket-orchestrator"):
            if required not in order:
                errors.append(key + ": execution order missing " + required)
        if not ticket.get("specific_restrictions"):
            errors.append(key + ": missing specific_restrictions")
        if ticket.get("confidence") not in {"HIGH", "MEDIUM", "LOW"}:
            errors.append(key + ": invalid confidence")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--mapping", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors = validate(args.root.resolve(), args.mapping)
    result = {"ok": not errors, "errors": errors, "tickets": 156}
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else ("PASS" if not errors else "\n".join(errors)))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
