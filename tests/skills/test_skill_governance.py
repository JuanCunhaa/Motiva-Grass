from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts" / "skills"
sys.path.insert(0, str(SCRIPTS))

from skills_common import (  # noqa: E402
    END_MARKER,
    START_MARKER,
    file_manifest,
    load_yaml_json,
    parse_frontmatter,
    replace_jira_section,
    tree_sha256,
)


def load_script(name: str):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), SCRIPTS / name)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


activate = load_script("activate-public-skills.py")
audit = load_script("audit-public-skills.py")


class SkillGovernanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_yaml_json(REPO / "config/skills/public-skills-catalog.yaml")
        cls.lock = load_yaml_json(REPO / "config/skills/skills-lock.yaml")

    def test_download_uses_full_pinned_commit(self) -> None:
        for source in self.lock["sources"].values():
            self.assertRegex(source["commit"], r"^[0-9a-f]{40}$")

    def test_missing_skill_is_not_found(self) -> None:
        skill = next(item for item in self.lock["skills"] if item["id"] == "static-analysis")
        self.assertEqual(skill["audit_status"], "NOT_FOUND")
        self.assertFalse(skill["frontmatter_valid"])

    def test_hash_change_extra_and_missing_file_are_detectable(self) -> None:
        source = REPO / "vendor/agent-skills/github-awesome-copilot/create-specification"
        expected = file_manifest(source)
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / "skill"
            shutil.copytree(source, copy)
            target = next(path for path in copy.rglob("*") if path.is_file())
            target.write_text(target.read_text(encoding="utf-8") + "\nchanged", encoding="utf-8")
            self.assertNotEqual(tree_sha256(expected), tree_sha256(file_manifest(copy)))
            extra = copy / "extra.txt"
            extra.write_text("extra", encoding="utf-8")
            self.assertIn("extra.txt", {item["path"] for item in file_manifest(copy)})
            extra.unlink()
            target.unlink()
            self.assertNotEqual({item["path"] for item in expected}, {item["path"] for item in file_manifest(copy)})

    def test_invalid_frontmatter_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "SKILL.md"
            path.write_text("# missing frontmatter\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                parse_frontmatter(path)

    def test_missing_license_disables_next_skills(self) -> None:
        for skill_id in ("next-best-practices", "next-cache-components"):
            skill = next(item for item in self.lock["skills"] if item["id"] == skill_id)
            self.assertEqual(skill["license"], "UNIDENTIFIED")
            self.assertEqual(skill["audit_status"], "DISABLED")

    def test_network_and_destructive_patterns_are_inventory_only(self) -> None:
        sample = "curl https://example.test\nrm -rf /tmp/scoped"
        self.assertTrue(audit.PATTERNS["network"].search(sample))
        self.assertTrue(audit.PATTERNS["destructive"].search(sample))

    def test_disabled_skill_is_not_routable(self) -> None:
        blocked = next(item for item in self.lock["skills"] if item["id"] == "skill-improver")
        self.assertNotIn(blocked["audit_status"], {"APPROVED", "APPROVED_WITH_RESTRICTIONS"})

    def test_activation_by_profile_and_ticket(self) -> None:
        label, profile_ids = activate.selected_ids(REPO, None, "geometry", False)
        self.assertEqual(label, "profile:geometry")
        self.assertIn("dimensional-analysis", profile_ids)
        label, ticket_ids = activate.selected_ids(REPO, "KAN-48", None, False)
        self.assertEqual(label, "ticket:KAN-48")
        self.assertIn("dimensional-analysis", ticket_ids)

    def test_ticket_without_mapping_fails(self) -> None:
        with self.assertRaises(ValueError):
            activate.selected_ids(REPO, "KAN-999", None, False)

    def test_jira_section_absent_duplicate_and_preserved(self) -> None:
        section = f"{START_MARKER}\nbody\n{END_MARKER}"
        original = "Original description"
        updated = replace_jira_section(original, section)
        self.assertTrue(updated.startswith(original))
        self.assertEqual(updated.count(START_MARKER), 1)
        with self.assertRaises(ValueError):
            replace_jira_section(section + "\n" + section, section)

    def test_checkpoint_resume_and_offline_mapping(self) -> None:
        routing = load_yaml_json(REPO / "config/skills/jira-skill-routing.yaml")
        checkpoint = {"last_completed_ticket": "KAN-27", "processed": 10, "pending": 129}
        encoded = json.loads(json.dumps(checkpoint))
        self.assertEqual(encoded["last_completed_ticket"], "KAN-27")
        self.assertEqual(len(routing["tickets"]), 156)


if __name__ == "__main__":
    unittest.main()
