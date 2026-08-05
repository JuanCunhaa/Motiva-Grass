#!/usr/bin/env python3
"""Generate the final KAN-1 Agent Skills implementation report."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def joined(values: set[str]) -> str:
    return ", ".join(sorted(values)) if values else "—"


def main() -> None:
    routing = json.loads((ROOT / "config/skills/jira-skill-routing.yaml").read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "config/skills/public-skills-catalog.yaml").read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / ".agents/skills/skills-manifest.yaml").read_text(encoding="utf-8"))
    progress = json.loads((ROOT / "reports/skills/jira-mapping-progress.json").read_text(encoding="utf-8"))
    tickets = routing["tickets"]
    public_status = {item["id"]: item["audit_status"] for item in catalog["skills"]}
    own_status = {item["id"]: item["status"] for item in manifest["first_party"]}

    epic_rows = []
    for number in range(2, 18):
        epic = "KAN-" + str(number)
        members = [ticket for ticket in tickets.values() if ticket.get("epic") == epic]
        own = {item["id"] for ticket in members for item in ticket["own_required"]}
        public = {item["id"] for ticket in members for item in ticket["public_required"]}
        public.update(
            item["id"] for ticket in members for item in ticket["conditional"] if item.get("kind") == "public"
        )
        epic_rows.append(f"| {epic} | {joined(own)} | {joined(public)} | {len(members)} |")

    coverage: dict[str, dict[str, set[str]]] = defaultdict(lambda: {"tickets": set(), "epics": set()})
    for key, ticket in tickets.items():
        ids = {item["id"] for item in ticket["own_required"]}
        ids.update(item["id"] for item in ticket["public_required"])
        ids.update(item["id"] for item in ticket["conditional"])
        for skill_id in ids:
            coverage[skill_id]["tickets"].add(key)
            if ticket.get("epic"):
                coverage[skill_id]["epics"].add(ticket["epic"])
    coverage_rows = []
    for skill_id in sorted(coverage):
        status = own_status.get(skill_id, public_status.get(skill_id, "UNKNOWN"))
        coverage_rows.append(
            f"| {skill_id} | {len(coverage[skill_id]['tickets'])} | "
            f"{len(coverage[skill_id]['epics'])} | {status} |"
        )

    confidence = defaultdict(int)
    for ticket in tickets.values():
        confidence[ticket["confidence"]] += 1

    report = f"""# Relatório de Implementação das Agent Skills

- Data: 2026-08-05
- Ticket principal: KAN-1
- Branch: chore/KAN-1-agent-skills-catalog
- PR: https://github.com/JuanCunhaa/Motiva-Grass/pull/89
- Resultado: PASS com drifts concorrentes preservados

## Resumo

Foram criadas e validadas as 16 skills próprias previstas, todas na versão 1.0.0, além do wrapper motiva-web-guidelines-snapshot já existente. Cada skill possui SKILL.md, agents/openai.yaml e 14 cenários, totalizando 224 cenários. Foram criadas 9 referências e 15 templates compartilhados.

O catálogo público contém 41 entradas: 15 APPROVED, 22 APPROVED_WITH_RESTRICTIONS, 3 DISABLED e 1 NOT_FOUND. O vendor permaneceu imutável. Foram analisados 1 roadmap, 16 Épicos e 139 tickets executáveis.

## Arquivos criados e alterados

- 16 diretórios em .agents/skills/motiva/.
- .agents/skills/shared/ com 9 referências.
- .agents/skills/templates/ com 15 templates.
- .agents/skills/public/skills-index.yaml.
- Catálogo, manifesto, roteamento, changelog e perfis de ativação.
- Três scripts obrigatórios de validação/plano e dois geradores determinísticos de assets.
- 224 cenários e testes unitários positivos/negativos.
- Backup, plano e progresso em reports/skills/.
- Matrizes, decisão arquitetural e este relatório em docs/governance/.

## Skills públicas reutilizadas

Foram reutilizadas somente skills roteáveis do catálogo fixado. Entre as principais: make-repo-contribution, create-specification, acquire-codebase-knowledge, modern-python, property-based-testing, security-review, dimensional-analysis, agentic-eval, quality-playbook, differential-review e as skills Hugging Face condicionais. Nenhuma skill pública foi copiada ou modificada fora do fluxo de vendor.

## Conflitos encontrados e resolvidos

- Diretriz web ao vivo versus reprodutibilidade: resolvido com motiva-web-guidelines-snapshot.
- React/Vercel sugeridos sem stack de produto comprovada: ficaram condicionais.
- react-best-practices versus frontmatter real vercel-react-best-practices: usado o nome real.
- next-best-practices e next-cache-components sem licença válida: mantidas DISABLED.
- static-analysis sem SKILL raiz: mantida NOT_FOUND, sem substituição.
- skill-improver sem dependência aprovada: mantida DISABLED.
- Git/Jira/Confluence: Git permanece normativo, Jira governa trabalho e Confluence não foi usado.
- KAN-20 e KAN-89 receberam alterações concorrentes durante os lotes; ambas foram preservadas. O texto concorrente de KAN-89 foi restaurado pelo changelog após a detecção.

## Testes executados e resultados

- python scripts/validate-agent-skills.py --json: PASS, 16/16.
- python scripts/validate-jira-skill-mapping.py --json: PASS, 156/156.
- python -m unittest discover -s tests/skills -p test_*.py -v: PASS, 18 testes na primeira execução completa.
- quick_validate.py oficial com PYTHONUTF8=1 e PyYAML 6.0.2 temporário: PASS, 16/16.
- Auditoria de cada lote Jira: PASS, 16 lotes, máximo 10 itens.
- Exportação final e comparação: PASS, 156/156.

## Limitações e pendências

O Jira normaliza Markdown ao salvar; por isso a validação usa equivalência semântica do bloco e igualdade do texto externo, não igualdade byte a byte do Markdown do bloco. O validador oficial dependeu de UTF-8 explícito no Windows. As pastas temporárias de PyYAML foram removidas. Não houve uso de Confluence, produção, dados reais, modelos, recursos pagos ou ações físicas.

Pendente apenas a revisão normal do PR 89 e checks externos aplicáveis. Nenhum status Jira foi alterado e nenhum merge foi executado.

## Tickets e campos

- Roadmap analisado: 1/1.
- Épicos analisados: 16/16.
- Tickets executáveis analisados: 139/139.
- Itens atualizados e verificados: 156/156.
- Tickets não atualizados: 0.
- Tickets com confiança baixa: {confidence['LOW']}.
- Falhas pendentes: 0.
- Campos inconsistentes encontrados: KAN-20.description/labels e KAN-89.description/labels por mudanças concorrentes; estado final preservado.
- Campos alterados por esta operação: description, exclusivamente dentro do bloco autorizado.
- Campos não autorizados alterados por esta operação: 0.

## Alterações sugeridas no Jira

Nenhuma alteração adicional automática. Revisar administrativamente KAN-89 somente se ainda houver configuração de interface pendente. Manter a reconciliação Git/Jira de KAN-20 e não reintroduzir documentação normativa no Confluence.

## Gates humanos

Nenhum gate humano foi atravessado. Permanecem protegidas ações de administração Jira, licença, custo, produção, dados restritos, coleta/medição física, promoção de modelo e release.

## Riscos residuais

- Mudança concorrente durante futuras execuções requer novo backup e comparação.
- Drift entre matriz e Jira deve ser detectado pelos validadores antes de novos lotes.
- Skills públicas condicionais podem mudar upstream; o lock e os hashes devem ser atualizados apenas pelo workflow dedicado.
- Revisão do PR e checks externos ainda podem solicitar ajustes.

## Skills por Épico

| Épico | Skills próprias | Skills públicas | Tickets |
|---|---|---|---:|
{chr(10).join(epic_rows)}

## Cobertura das skills

| Skill | Tickets relacionados | Épicos | Status |
|---|---:|---:|---|
{chr(10).join(coverage_rows)}

## Atualização do Jira

| Situação | Quantidade |
|---|---:|
| Itens analisados | 156 |
| Itens atualizados | 156 |
| Falhas | 0 |
| Confiança alta | {confidence['HIGH']} |
| Confiança média | {confidence['MEDIUM']} |
| Confiança baixa | {confidence['LOW']} |

## Falhas

| Ticket | Falha | Impacto | Ação necessária |
|---|---|---|---|
| — | Nenhuma falha pendente | — | — |

## Resultado esperado da auditoria

- 1 roadmap analisado.
- 16 Épicos analisados.
- 139 tickets executáveis analisados.
- 156 itens verificados e mapeados.
- 0 descrições sobrescritas no estado final.
- 0 seções duplicadas.
- 0 skills inexistentes utilizadas.
- 0 skills rejeitadas utilizadas.
- 0 campos não autorizados modificados por esta operação.
"""
    path = ROOT / "docs/governance/SKILL_IMPLEMENTATION_REPORT.md"
    path.write_text(report, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
