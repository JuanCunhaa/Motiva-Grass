from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


skills_validator = load("validate-agent-skills.py")
mapping_validator = load("validate-jira-skill-mapping.py")
planner = load("generate-jira-skill-update-plan.py")


class FirstPartySkillTests(unittest.TestCase):
    def test_repository_skills_are_valid(self) -> None:
        self.assertEqual(skills_validator.validate(ROOT), [])

    def test_missing_required_section_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            clone = Path(temp)
            shutil.copytree(ROOT / ".agents", clone / ".agents")
            shutil.copytree(ROOT / "config", clone / "config")
            target = clone / ".agents/skills/motiva/motiva-quality-gate/SKILL.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace("\n## Evidências\n", "\n## Evidências removidas\n"),
                encoding="utf-8",
            )
            errors = skills_validator.validate(clone)
            self.assertTrue(any("missing section Evidências" in item for item in errors))

    def test_repository_mapping_is_valid(self) -> None:
        self.assertEqual(mapping_validator.validate(ROOT), [])

    def test_unroutable_public_skill_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            mapping = json.loads((ROOT / "config/skills/jira-skill-routing.yaml").read_text(encoding="utf-8"))
            mapping["tickets"]["KAN-1"]["public_required"].append({"id": "skill-improver", "reason": "negative test"})
            path = Path(temp) / "mapping.json"
            path.write_text(json.dumps(mapping), encoding="utf-8")
            errors = mapping_validator.validate(ROOT, path)
            self.assertTrue(any("unroutable public skill skill-improver" in item for item in errors))

    def test_normalization_is_deterministic_and_deduplicates(self) -> None:
        source = json.loads((ROOT / "config/skills/jira-skill-routing.yaml").read_text(encoding="utf-8"))
        once = planner.normalize_routing(copy.deepcopy(source))
        twice = planner.normalize_routing(copy.deepcopy(once))
        self.assertEqual(once, twice)
        own = once["tickets"]["KAN-150"]["own_required"]
        self.assertEqual(len(own), len({item["id"] for item in own}))
        self.assertTrue(all(item["status"] == "VALIDATED" for item in own))

    def test_replace_section_preserves_content_and_is_idempotent(self) -> None:
        original = "Título\n\nCritérios originais"
        section = planner.START + "\nnovo\n" + planner.END
        first = planner.replace_section(original, section)
        second = planner.replace_section(first, section)
        self.assertEqual(first, second)
        self.assertTrue(first.startswith(original))
        with self.assertRaises(ValueError):
            planner.replace_section(section + "\n" + section, section)

    def test_plan_has_all_tickets_and_preserves_text_outside_block(self) -> None:
        routing = planner.normalize_routing(
            json.loads((ROOT / "config/skills/jira-skill-routing.yaml").read_text(encoding="utf-8"))
        )
        backup = {"issues": [{"key": "KAN-" + str(i), "description": "Descrição " + str(i)} for i in range(1, 157)]}
        plan = planner.generate_plan(routing, backup)
        self.assertEqual(plan["ticket_count"], 156)
        self.assertEqual(len(plan["updates"]), 156)
        self.assertTrue(plan["updates"][0]["description"].startswith("Descrição 1"))
        self.assertEqual(plan["updates"][0]["description"].count(planner.START), 1)


if __name__ == "__main__":
    unittest.main()
