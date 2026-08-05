#!/usr/bin/env python3
"""Normalize routing and generate an idempotent Jira description update plan."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

START = "<!-- MOTIVA-SKILLS:INÍCIO -->"
END = "<!-- MOTIVA-SKILLS:FIM -->"
STAMP = "2026-08-05T12:00:00-03:00"
CONTEXT_PROFILES = {"architecture", "contracts", "infrastructure", "computer-vision", "geometry"}
PROFILE_RESTRICTIONS = {
    "physical-data": ["Não executar ação, coleta ou medição física sem gate humano."],
    "ml-training": ["Não iniciar GPU, Job pago, upload ou publicação sem gate humano."],
    "ml-evaluation": ["Não usar test set para tuning nem aprovar resultado inconclusivo."],
    "model-release": ["Não promover ou publicar modelo sem avaliação, Model Card, rollback e aprovação."],
    "release": ["Não publicar, taguear, mesclar ou alterar produção sem gate humano."],
    "frontend-design": ["Usar o snapshot web fixado; não buscar diretriz ao vivo nem expor dados em captura."],
    "security": ["Não expor segredos nem aceitar risco sem autoridade."],
    "devsecops": ["Não alterar settings, proteção ou secrets sem autorização."],
}


def sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def replace_section(description: str, section: str) -> str:
    starts = description.count("MOTIVA-SKILLS:INÍCIO")
    ends = description.count("MOTIVA-SKILLS:FIM")
    if starts != ends or starts > 1:
        raise ValueError("invalid MOTIVA-SKILLS marker count")
    if starts == 0:
        return description.rstrip() + "\n\n" + section + "\n"
    pattern = re.compile(
        r"(?ms)^[^\n]*MOTIVA-SKILLS:INÍCIO[^\n]*\n.*?^[^\n]*MOTIVA-SKILLS:FIM[^\n]*$"
    )
    updated, count = pattern.subn(section, description)
    if count != 1:
        raise ValueError("unable to isolate MOTIVA-SKILLS block")
    return updated


def dedupe(items: list[dict]) -> list[dict]:
    result: list[dict] = []
    seen: set[str] = set()
    for item in items:
        if item["id"] not in seen:
            seen.add(item["id"])
            result.append(item)
    return result


def normalize_routing(data: dict) -> dict:
    for key, ticket in data["tickets"].items():
        own = dedupe(ticket.get("own_required", []))
        for item in own:
            item["status"] = "VALIDATED"
        if ticket.get("profile") in CONTEXT_PROFILES and not any(item["id"] == "motiva-repository-context" for item in own):
            own.insert(2, {
                "id": "motiva-repository-context",
                "status": "VALIDATED",
                "reason": "Mapear normas, contratos e arquivos afetados antes de implementar.",
            })
        ticket["own_required"] = own
        ticket["public_required"] = dedupe(ticket.get("public_required", []))
        ticket["conditional"] = dedupe(ticket.get("conditional", []))

        order: list[str] = []
        for item in ["motiva-jira-ticket-executor", "motiva-ticket-orchestrator"] + ticket.get("execution_order", []):
            if item not in order:
                order.append(item)
        for item in own:
            if item["id"] not in order:
                order.insert(min(2, len(order)), item["id"])
        ticket["execution_order"] = order
        restrictions = PROFILE_RESTRICTIONS.get(ticket.get("profile"), [])
        if not restrictions:
            restrictions = ["Preservar escopo e campos do ticket; não executar ações protegidas sem gate aplicável."]
        ticket["specific_restrictions"] = restrictions
        ticket["analyzed_at"] = STAMP
    data["schema_version"] = 2
    data["generated_at"] = STAMP
    return data


def render_block(ticket: dict) -> str:
    own = ", ".join(item["id"] for item in ticket["own_required"]) or "nenhuma"
    public = ", ".join(item["id"] for item in ticket["public_required"]) or "nenhuma"
    conditional = "; ".join(
        item["id"] + " — " + item["condition"] for item in ticket.get("conditional", [])
    ) or "nenhuma"
    order = " → ".join(ticket["execution_order"])
    evidence = "; ".join(ticket.get("evidence", [])) or "conforme o ticket e o padrão central"
    gates = "; ".join(ticket.get("human_gates", [])) or "nenhum gate específico identificado"
    restrictions = "; ".join(ticket["specific_restrictions"])
    return f"""{START}
## Skills recomendadas para execução

- Perfil: {ticket["profile"]}
- Orquestradora: motiva-ticket-orchestrator
- Próprias obrigatórias: {own}
- Públicas obrigatórias: {public}
- Condicionais e condições: {conditional}
- Ordem: {order}
- Evidências: {evidence}
- Gates humanos: {gates}
- Restrições específicas: {restrictions}
- Confiança: {ticket["confidence"]}
- Referência central: config/skills/jira-skill-routing.yaml
- Atualizado em: {STAMP}
{END}"""


def generate_plan(routing: dict, backup: dict) -> dict:
    issues = backup.get("issues", backup)
    by_key = {item["key"]: item for item in issues}
    updates = []
    for number in range(1, 157):
        key = "KAN-" + str(number)
        issue = by_key[key]
        old = issue.get("description")
        if old is None:
            old = issue.get("fields", {}).get("description")
        old = old or ""
        block = render_block(routing["tickets"][key])
        new = replace_section(old, block)
        updates.append({
            "key": key,
            "old_description_sha256": sha(old),
            "new_description_sha256": sha(new),
            "changed": old != new,
            "reason": "replace-or-add-idempotent-MOTIVA-SKILLS-block",
            "description": new,
        })
    return {
        "schema_version": 1,
        "generated_at": STAMP,
        "ticket_count": len(updates),
        "batch_size": 10,
        "updates": updates,
    }


def enrich_backup(backup: dict) -> dict:
    for issue in backup["issues"]:
        fields = issue["fields"]
        description = fields.get("description") or ""
        issue["description_sha256"] = sha(description)
        issue["fields_sha256"] = sha(
            json.dumps(fields, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        )
    backup["hash_algorithm"] = "sha256"
    return backup


def write_matrix(root: Path, routing: dict) -> None:
    lines = [
        "# Matriz Jira → Agent Skills",
        "",
        "Gerada deterministicamente de config/skills/jira-skill-routing.yaml em 2026-08-05.",
        "",
        "| Ticket | Épico | Perfil | Próprias obrigatórias | Públicas obrigatórias | Condicionais | Gate | Confiança |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for key, ticket in routing["tickets"].items():
        own = ", ".join(item["id"] for item in ticket["own_required"]) or "—"
        public = ", ".join(item["id"] for item in ticket["public_required"]) or "—"
        conditional = ", ".join(item["id"] for item in ticket["conditional"]) or "—"
        gate = "Sim" if ticket.get("human_gates") else "Não"
        link = f"[{key}](https://gp16-motiva.atlassian.net/browse/{key})"
        lines.append(
            f"| {link} | {ticket.get('epic') or '—'} | {ticket['profile']} | "
            f"{own} | {public} | {conditional} | {gate} | {ticket['confidence']} |"
        )
    path = root / "docs" / "governance" / "JIRA_SKILL_ROUTING_MATRIX.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--routing", type=Path)
    parser.add_argument("--backup", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write-routing", action="store_true")
    parser.add_argument("--hash-backup", action="store_true")
    parser.add_argument("--write-matrix", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    routing_path = args.routing or root / "config" / "skills" / "jira-skill-routing.yaml"
    routing = normalize_routing(json.loads(routing_path.read_text(encoding="utf-8")))
    if args.write_routing:
        routing_path.write_text(json.dumps(routing, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    if args.write_matrix:
        write_matrix(root, routing)
    if args.hash_backup:
        if not args.backup:
            parser.error("--hash-backup requires --backup")
        backup_data = enrich_backup(json.loads(args.backup.read_text(encoding="utf-8")))
        args.backup.write_text(
            json.dumps(backup_data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    if args.backup:
        plan = generate_plan(routing, json.loads(args.backup.read_text(encoding="utf-8")))
        output = args.output or root / "reports" / "skills" / "jira-skill-update-plan.yaml"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(json.dumps({"tickets": plan["ticket_count"], "output": str(output)}, ensure_ascii=False))
    else:
        print(json.dumps({"tickets": len(routing["tickets"]), "routing_normalized": args.write_routing}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
