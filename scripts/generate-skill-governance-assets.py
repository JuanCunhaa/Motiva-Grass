#!/usr/bin/env python3
"""Generate shared references, templates, catalog and manifest."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"

REFERENCES = {
    "PROJECT_CONTEXT.md": """# Contexto do Motiva-Grass

Jira define objetivo, escopo, owner, prioridade, dependências e estado. AGENTS.md e PROJECT_RULEBOOK.md definem precedência. docs/DOCUMENTATION_INDEX.md aponta as fontes canônicas.

O repositório atual contém governança e documentação; nenhum manifesto comprova ainda stack de produto. Um ticket usa uma branch e um PR. Preservar mudanças alheias, manter documentação no mesmo PR e nunca inventar evidência.
""",
    "JIRA_WORKFLOW.md": """# Workflow Jira

1. Ler ticket, pai, KAN-1, KAN-20 e dependências.
2. Validar DoR e comentar início antes de Em andamento.
3. Comentar somente mudança material, marco longo, bloqueio, handoff, revisão e conclusão.
4. Usar Tarefas pendentes para não iniciado, DoR incompleta ou bloqueio total; Em andamento para atividade real; Em análise para entrega e PR completos; Concluído somente após DoD.
5. Não alterar título, prioridade, owner, pai, links, labels, critérios ou estimativa sem autorização.
6. Sem Jira, produzir handoff pendente e não alegar leitura ou atualização.
""",
    "LABELS_AND_PRIORITIES.md": """# Labels e prioridades

Na primeira frente executável de KAN-1, ordenar por priority-p0, priority-p1 e priority-p2. Não inventar, remover ou promover prioridade. Bloqueio real usa Flagged igual a Impediment e label blocked-* conforme a política. owner, links Blocks, dependências e trabalho concorrente fazem parte da seleção.
""",
    "PUBLIC_SKILL_ROUTING.md": """# Roteamento de skills públicas

Ativar somente APPROVED ou APPROVED_WITH_RESTRICTIONS. Condicional exige prova. Limites: 3 a 7 principais, até 4 condicionais e 12 totais. DISABLED e NOT_FOUND nunca recebem substituição silenciosa. Vendor é imutável; normas e skills Motiva-Grass prevalecem.

Conflitos: usar motiva-web-guidelines-snapshot, não busca web ao vivo; não assumir React, Next.js ou Vercel; next-best-practices e next-cache-components estão desabilitadas; static-analysis não existe como skill raiz.
""",
    "HUMAN_GATES.md": """# Gates humanos

Parar a parte afetada diante de licença, negócio, mudança relevante de escopo, ação ou medição física, credencial/admin, custo, produção, risco aceito, dado real restrito, promoção de modelo ou release. Registrar decisor, ação, escopo, ambiente e evidência da aprovação, nunca o segredo. Continuar apenas trabalho independente, seguro e reversível.
""",
    "PROHIBITED_ACTIONS.md": """# Ações proibidas

- Inventar execução, métrica, medição, aprovação, hash ou evidência.
- Expor segredo, dado pessoal, mídia privada, dataset restrito, peso ou saída identificável.
- Alterar produção, publicar, promover, criar custo, coletar ou operar equipamento sem gate.
- Reescrever histórico, descartar mudança alheia, mesclar ou fazer push em main.
- Modificar vendor, ativar skill bloqueada ou substituir skill inexistente.
- Tratar fixture como dado real ou usar teste para tuning.
""",
    "EVIDENCE_STANDARD.md": """# Padrão de evidência

Registrar ticket, artefato ou hash, versão, ambiente, comando ou workflow, dados permitidos, horário, resultado e caminho do artefato. Relacionar critério a evidência. Falha, omissão e teste não executado ficam explícitos. Parcial lista feito, ausente, motivo, impacto e continuação. Inconclusivo não equivale a PASS.
""",
    "ERROR_TAXONOMY.md": """# Taxonomia de erros

- INPUT_GAP: entrada obrigatória ausente.
- DOR_BLOCKED: pré-condição ou dependência impede início.
- HUMAN_GATE: ação protegida aguarda aprovação.
- TOOL_FAILURE: ferramenta falhou sem confirmar efeito.
- RULE_CONFLICT: normas de mesma precedência conflitam.
- EVIDENCE_GAP: conclusão sem prova suficiente.
- PARTIAL: trabalho independente concluído e restante delimitado.
- PROHIBITED: ação solicitada viola regra.
""",
    "GLOSSARY.md": """# Glossário

DoR é Definition of Ready. DoD é Definition of Done. Gate humano é decisão externa antes de ação protegida. Skill própria aplica normas Motiva-Grass. Skill pública é snapshot auditado em vendor. Perfil é conjunto inicial por domínio. Condicional exige prova. Artefato exato tem versão ou hash. Inconclusivo não é PASS nem FAIL. Handoff registra feito, pendente, risco e próxima ação.
""",
}

TEMPLATES = {
    "jira-start-comment.md": """## Início

- Feito: DoR, dependências, gates e escopo revalidados.
- Evidência: [fontes e branch].
- Próximo passo: [ação].
- Risco ou bloqueio: [detalhe].
- Executor: [executor].
""",
    "jira-progress-comment.md": """## Progresso material

- Feito: [marco].
- Evidência: [comando ou artefato].
- Próximo passo: [ação].
- Risco ou bloqueio: [detalhe].
- Executor: [executor].
""",
    "jira-blocked-comment.md": """## Bloqueio

- Feito: [trabalho independente].
- Evidência: [referência].
- Bloqueio e impacto: [causa].
- Ação necessária: [decisor e ação].
- Condição de retomada: [evidência esperada].
""",
    "jira-review-comment.md": """## Pronto para análise

- Escopo entregue: [resumo].
- Critérios e evidências: [mapeamento].
- Testes: [comandos, resultados e omissões].
- PR: [link].
- Riscos e rollback: [detalhes].
""",
    "jira-completion-comment.md": """## Conclusão

- Entrega: [resumo].
- PR ou merge: [link e hash].
- Evidências e checks: [referências].
- Documentação: [arquivos].
- Riscos residuais e rollback: [detalhes].
""",
    "jira-skills-section.md": """<!-- MOTIVA-SKILLS:INÍCIO -->
## Skills recomendadas para execução

- Perfil: [perfil]
- Orquestradora: motiva-ticket-orchestrator
- Próprias obrigatórias: [lista]
- Públicas obrigatórias: [lista]
- Condicionais e condições: [lista]
- Ordem: [lista]
- Evidências: [lista]
- Gates humanos: [lista]
- Restrições específicas: [lista]
- Confiança: [HIGH, MEDIUM ou LOW]
- Referência central: config/skills/jira-skill-routing.yaml
- Atualizado em: [ISO-8601]
<!-- MOTIVA-SKILLS:FIM -->
""",
    "bug-report.md": """# Bug

## Observado
[comportamento e impacto]

## Esperado
[contrato]

## Reprodução
[ambiente, versão, dados e passos]

## Evidências
[logs sanitizados e artefatos]

## Hipóteses
[separar de causa confirmada]

## Risco e rollback
[detalhes]
""",
    "pull-request.md": """# Escopo
[resumo e ticket]

# Critérios
[mapeamento]

# Arquivos e contratos
[lista]

# Testes e resultados
[comandos, ambiente e omissões]

# Evidências e documentação
[links]

# Impactos, riscos, gates e rollback
[detalhes]
""",
    "adr.md": """# ADR NNNN — Título

- Status: Proposed
- Data: YYYY-MM-DD
- Ticket: KAN-N

## Contexto
[fatos]

## Decisão
[decisão]

## Alternativas
[opções]

## Consequências
[impactos]

## Migração e rollback
[plano]
""",
    "technical-spike.md": """# Spike técnico

## Pergunta e hipótese
[conteúdo]

## Escopo e timebox
[limites]

## Método e evidências
[passos, ambiente e resultados]

## Resultado
[SUPPORTED, NOT_SUPPORTED ou INCONCLUSIVE]

## Recomendação e lacunas
[próximo passo]
""",
    "experiment-report.md": """# Relatório de experimento

## Hipótese e baseline
[conteúdo]

## Código, dados e ambiente
[commits, versões, splits, seed e hardware]

## Configuração e critérios
[definidos antes do run]

## Runs, inclusive falhas
[tabela]

## Resultados, limitações e conclusão
[SUPPORTED, NOT_SUPPORTED, INCONCLUSIVE ou FAILED]
""",
    "data-card.md": """# Data Card

## Identidade e finalidade
[versão e uso]

## Proveniência, licença e retenção
[detalhes]

## Schema, transformações e splits
[detalhes]

## Qualidade, leakage, vieses e limitações
[detalhes]

## Checksums, acesso e owner
[detalhes]
""",
    "model-card.md": """# Model Card

## Identidade do artefato
[modelo, hash e código]

## Uso pretendido e proibido
[detalhes]

## Dados e avaliação
[versões, métricas e slices]

## Limitações e inconclusivos
[detalhes]

## Segurança, licença, rollback e monitoramento
[detalhes]
""",
    "go-no-go.md": """# Decisão GO ou NO-GO

- Candidate ou artefato: [versão e hash]
- Decisão: [GO, NO-GO ou BLOCKED]

## Gates e evidências
[tabela]

## Riscos, rollback e monitoramento
[detalhes]

## Aprovação
[decisor, ação, escopo e evidência, sem segredo]
""",
    "release-notes.md": """# Release notes

## Versão e candidate
[versão, hash e data]

## Mudanças por ticket
[lista]

## Compatibilidade, migração e limitações
[detalhes]

## Segurança, dados e modelos
[impactos]

## Rollback e suporte
[passos e owner]
""",
}

FIRST_PARTY = [
    "motiva-work-selector",
    "motiva-jira-ticket-executor",
    "motiva-ticket-orchestrator",
    "motiva-repository-context",
    "motiva-architecture-guard",
    "motiva-dataset-governance",
    "motiva-physical-data-gate",
    "motiva-inference-contract",
    "motiva-ml-experiment",
    "motiva-ml-evaluation-gate",
    "motiva-model-release-gate",
    "motiva-design-system-guardian",
    "motiva-security-privacy-gate",
    "motiva-quality-gate",
    "motiva-documentation-maintainer",
    "motiva-release-manager",
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    for name, content in REFERENCES.items():
        write(SKILLS_ROOT / "shared" / name, content)
    for name, content in TEMPLATES.items():
        write(SKILLS_ROOT / "templates" / name, content)

    catalog = json.loads((ROOT / "config" / "skills" / "public-skills-catalog.yaml").read_text(encoding="utf-8"))
    public_index = {
        "schema_version": 1,
        "catalog": "config/skills/public-skills-catalog.yaml",
        "skills": [
            {"id": item["id"], "status": item["audit_status"], "vendor_path": item.get("vendor_path")}
            for item in catalog["skills"]
        ],
    }
    write(SKILLS_ROOT / "public" / "skills-index.yaml", json.dumps(public_index, ensure_ascii=False, indent=2) + "\n")

    entries = [
        {"id": name, "version": "1.0.0", "status": "VALIDATED", "path": ".agents/skills/motiva/" + name}
        for name in FIRST_PARTY
    ]
    entries.append({
        "id": "motiva-web-guidelines-snapshot",
        "version": "1.0.0",
        "status": "VALIDATED",
        "path": ".agents/skills/motiva/motiva-web-guidelines-snapshot",
    })
    manifest = {
        "schema_version": 2,
        "generated_at": "2026-08-05T12:00:00-03:00",
        "public_catalog": "config/skills/public-skills-catalog.yaml",
        "routing": "config/skills/jira-skill-routing.yaml",
        "public_skill_count": 41,
        "first_party_skill_count": 16,
        "wrapper_skill_count": 1,
        "first_party": entries,
    }
    write(SKILLS_ROOT / "skills-manifest.yaml", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    rows = "\n".join("| " + name + " | 1.0.0 | VALIDATED |" for name in FIRST_PARTY)
    skill_catalog = """# Catálogo de Agent Skills

## Resumo

- Skills próprias implementadas e validadas: 16.
- Wrapper local validado: motiva-web-guidelines-snapshot.
- Skills públicas auditadas: 41; estados e restrições ficam em config/skills/public-skills-catalog.yaml.
- Vendor público é imutável e fixado por config/skills/skills-lock.yaml.

## Skills próprias

| Skill | Versão | Status |
|---|---|---|
""" + rows + """
| motiva-web-guidelines-snapshot | 1.0.0 | VALIDATED |

A versão estruturada está em skills-manifest.yaml e o roteamento em config/skills/jira-skill-routing.yaml.
"""
    write(SKILLS_ROOT / "SKILL_CATALOG.md", skill_catalog)

    routing = """# Roteamento de Skills

1. Validar ticket, pai, KAN-1, KAN-20, DoR, dependências e gates.
2. Carregar motiva-jira-ticket-executor e motiva-ticket-orchestrator.
3. Ler config/skills/jira-skill-routing.yaml e ativar próprias obrigatórias.
4. Ativar pública somente se catálogo permitir e condição estiver comprovada.
5. Bloquear DISABLED, NOT_FOUND e alias inexistente.
6. Registrar conjunto mínimo em .agents/runtime/active-skills.json e desativar após o ticket.

Normas e skills locais prevalecem. Usar motiva-web-guidelines-snapshot no lugar da diretriz ao vivo. Não assumir React, Next.js, Vercel ou Hugging Face apenas pelo perfil.
"""
    write(SKILLS_ROOT / "SKILL_ROUTING.md", routing)

    changelog = """# Changelog das Agent Skills

## 2026-08-05 — 1.0.0

- Implementadas 16 skills próprias com metadados e 14 cenários cada.
- Criadas referências e templates compartilhados.
- Promovido o roteamento de planned para VALIDATED.
- Mantido motiva-web-guidelines-snapshot como wrapper offline.
- Mantido o vendor público imutável.
"""
    write(SKILLS_ROOT / "CHANGELOG.md", changelog)


if __name__ == "__main__":
    main()
