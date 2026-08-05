#!/usr/bin/env python3
"""Validate the first-party Motiva-Grass Agent Skills."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

EXPECTED = [
    "motiva-work-selector", "motiva-jira-ticket-executor", "motiva-ticket-orchestrator",
    "motiva-repository-context", "motiva-architecture-guard", "motiva-dataset-governance",
    "motiva-physical-data-gate", "motiva-inference-contract", "motiva-ml-experiment",
    "motiva-ml-evaluation-gate", "motiva-model-release-gate", "motiva-design-system-guardian",
    "motiva-security-privacy-gate", "motiva-quality-gate",
    "motiva-documentation-maintainer", "motiva-release-manager",
]
SECTIONS = [
    "Objetivo", "Quando usar", "Quando não usar", "Entradas obrigatórias", "Ordem de leitura",
    "Skills próprias e públicas", "Ferramentas", "Pré-condições", "Procedimento",
    "Atualizações no Jira", "Comentários no Jira", "Evidências", "Saídas", "Bloqueios",
    "Gates humanos", "Ações proibidas", "Falhas e recuperação", "Modo sem Jira",
    "Checklist de conclusão", "Exemplo de ativação", "Exemplo de não ativação",
]
SCENARIO_CLASSES = {
    "activate", "do-not-activate", "valid-input", "incomplete-input", "blocked",
    "human-gate", "tool-failure", "jira-unavailable", "partial-result",
    "prohibited-action", "public-unavailable", "rule-conflict",
    "insufficient-info", "no-evidence",
}
SHARED = {
    "PROJECT_CONTEXT.md", "JIRA_WORKFLOW.md", "LABELS_AND_PRIORITIES.md",
    "PUBLIC_SKILL_ROUTING.md", "HUMAN_GATES.md", "PROHIBITED_ACTIONS.md",
    "EVIDENCE_STANDARD.md", "ERROR_TAXONOMY.md", "GLOSSARY.md",
}
TEMPLATES = {
    "jira-start-comment.md", "jira-progress-comment.md", "jira-blocked-comment.md",
    "jira-review-comment.md", "jira-completion-comment.md", "jira-skills-section.md",
    "bug-report.md", "pull-request.md", "adr.md", "technical-spike.md",
    "experiment-report.md", "data-card.md", "model-card.md", "go-no-go.md",
    "release-notes.md",
}


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    base = root / ".agents" / "skills"
    motiva = base / "motiva"
    actual = {p.name for p in motiva.iterdir() if p.is_dir() and p.name != "motiva-web-guidelines-snapshot"}
    if actual != set(EXPECTED):
        errors.append("first-party skill set differs: " + repr(sorted(actual ^ set(EXPECTED))))

    for name in EXPECTED:
        skill = motiva / name
        md = skill / "SKILL.md"
        if not md.is_file():
            errors.append(name + ": missing SKILL.md")
            continue
        text = md.read_text(encoding="utf-8")
        match = re.match(r"^---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n", text)
        if not match:
            errors.append(name + ": invalid frontmatter")
        elif match.group(1) != name or len(match.group(2).strip()) < 40:
            errors.append(name + ": invalid name or description")
        for section in SECTIONS:
            if "\n## " + section + "\n" not in text:
                errors.append(name + ": missing section " + section)
        if "TODO" in text or "[TODO" in text:
            errors.append(name + ": unresolved TODO")

        metadata = skill / "agents" / "openai.yaml"
        if not metadata.is_file():
            errors.append(name + ": missing agents/openai.yaml")
        else:
            raw = metadata.read_text(encoding="utf-8")
            for key in ("display_name:", "short_description:", "default_prompt:"):
                if key not in raw:
                    errors.append(name + ": metadata missing " + key)
            if "$" + name not in raw:
                errors.append(name + ": default_prompt must mention skill")
            short_match = re.search(r'^\s*short_description:\s*(".*")\s*$', raw, re.MULTILINE)
            if not short_match:
                errors.append(name + ": short_description must be quoted")
            else:
                short = json.loads(short_match.group(1))
                if not 25 <= len(short) <= 64:
                    errors.append(name + ": short_description length must be 25..64")

        scenarios_path = skill / "tests" / "scenarios.yaml"
        if not scenarios_path.is_file():
            errors.append(name + ": missing scenarios")
        else:
            try:
                data = json.loads(scenarios_path.read_text(encoding="utf-8"))
                scenarios = data["scenarios"]
                classes = {item["class"] for item in scenarios}
                if len(scenarios) != 14 or classes != SCENARIO_CLASSES:
                    errors.append(name + ": scenarios must cover the 14 required classes")
            except (ValueError, KeyError, TypeError) as exc:
                errors.append(name + ": invalid scenarios: " + str(exc))

    shared = base / "shared"
    templates = base / "templates"
    missing_shared = sorted(SHARED - {p.name for p in shared.iterdir() if p.is_file()}) if shared.exists() else sorted(SHARED)
    missing_templates = sorted(TEMPLATES - {p.name for p in templates.iterdir() if p.is_file()}) if templates.exists() else sorted(TEMPLATES)
    if missing_shared:
        errors.append("missing shared references: " + repr(missing_shared))
    if missing_templates:
        errors.append("missing templates: " + repr(missing_templates))

    manifest_path = base / "skills-manifest.yaml"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        entries = {item["id"]: item for item in manifest["first_party"]}
        for name in EXPECTED:
            item = entries.get(name)
            if not item or item.get("status") != "VALIDATED" or not re.fullmatch(r"\d+\.\d+\.\d+", item.get("version", "")):
                errors.append(name + ": invalid manifest entry")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append("invalid manifest: " + str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    result = {"ok": not errors, "errors": errors, "validated_skills": len(EXPECTED)}
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else ("PASS" if not errors else "\n".join(errors)))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
