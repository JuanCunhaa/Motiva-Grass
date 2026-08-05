#!/usr/bin/env python3
"""Generate the first-party Motiva-Grass Agent Skills deterministically."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".agents" / "skills" / "motiva"

SKILLS = {
    "motiva-work-selector": {
        "title": "Motiva Work Selector",
        "desc": "Select the next executable Motiva-Grass Jira ticket from KAN-1 using readiness, dependency, priority, ownership, gate, and concurrent-work rules. Use before starting backlog work or when the current ticket becomes fully blocked.",
        "domain": "seleção de um único ticket executável na primeira frente aberta de KAN-1",
        "canon": "docs/governance/DEFINITION_OF_READY.md, docs/governance/JIRA_WORKFLOW_POLICY.md e ../../shared/LABELS_AND_PRIORITIES.md",
        "skills": "Entregar a decisão a $motiva-jira-ticket-executor e $motiva-ticket-orchestrator; usar create-specification apenas para lacunas formalizáveis.",
        "gate": "A seleção não vale como aprovação de qualquer gate do ticket.",
        "ban": "Não reordenar roadmap, alterar prioridade, assumir lacunas ou selecionar múltiplos tickets.",
        "activate": "Qual é o próximo ticket executável do roadmap?",
        "no": "Execute KAN-42, quando a seleção já foi dada e permanece válida.",
        "short": "Seleciona o próximo trabalho executável do roadmap",
    },
    "motiva-jira-ticket-executor": {
        "title": "Motiva Jira Ticket Executor",
        "desc": "Execute one Motiva-Grass Jira ticket with state, comment, evidence, branch, commit, and PR traceability. Use when a selected ticket must be enforced from Definition of Ready through review or completion.",
        "domain": "execução de um ticket Jira do início ao handoff, com estado, branch, PR e evidências coerentes",
        "canon": "CONTRIBUTING.md, ../../shared/JIRA_WORKFLOW.md e ../../shared/EVIDENCE_STANDARD.md",
        "skills": "Coordenar com $motiva-ticket-orchestrator; usar make-repo-contribution para Git/PR e as skills do domínio roteado.",
        "gate": "Parar licença, custo, produção, dado restrito, ação física, promoção de modelo e release.",
        "ban": "Não executar vários tickets no PR, inventar evidência, alterar campos não autorizados ou mesclar sem revisão.",
        "activate": "Implemente KAN-42 até PR.",
        "no": "Liste os próximos tickets possíveis.",
        "short": "Executa tickets Jira com rastreabilidade e evidências",
    },
    "motiva-ticket-orchestrator": {
        "title": "Motiva Ticket Orchestrator",
        "desc": "Coordinate preconditions, skill routing, human gates, handoffs, and partial progress for one Motiva-Grass Jira ticket. Use for cross-domain tickets or any execution needing ordered safeguards.",
        "domain": "orquestração da sequência mínima de skills, dependências, gates e handoffs de um ticket",
        "canon": "../../shared/PUBLIC_SKILL_ROUTING.md, ../../shared/HUMAN_GATES.md e ../../shared/ERROR_TAXONOMY.md",
        "skills": "Começar por $motiva-jira-ticket-executor; ativar apenas próprias obrigatórias e públicas aprovadas com condição comprovada.",
        "gate": "Registrar decisor, ação, escopo e evidência, nunca o segredo.",
        "ban": "Não ativar todas as skills, contornar gate, simular ferramenta ou expandir escopo.",
        "activate": "Orquestre KAN-89 entre Jira, documentação e validação.",
        "no": "Corrija um typo local sem dependências.",
        "short": "Orquestra precondições, gates e handoffs do ticket",
    },
    "motiva-repository-context": {
        "title": "Motiva Repository Context",
        "desc": "Map the ticket-scoped Motiva-Grass repository context, canonical rules, ownership boundaries, and affected contracts. Use before implementation when relevant files or governing documents are not yet known.",
        "domain": "mapeamento focal das regras, arquivos, contratos, owners e alterações alheias relevantes ao ticket",
        "canon": "docs/DOCUMENTATION_INDEX.md, docs/architecture/REPOSITORY_ARCHITECTURE.md e docs/architecture/FOLDER_STRUCTURE.md",
        "skills": "Usar acquire-codebase-knowledge somente para mapeamento amplo; esta skill cobre descoberta focal por ticket.",
        "gate": "Leitura não autoriza dado restrito, produção ou sistema externo.",
        "ban": "Não modificar arquivos, descartar mudanças alheias ou inferir stack que os manifestos não comprovem.",
        "activate": "Mapeie o contexto necessário para KAN-73.",
        "no": "Explique uma função cujo contexto completo já foi fornecido.",
        "short": "Mapeia contexto e normas canônicas do repositório",
    },
    "motiva-architecture-guard": {
        "title": "Motiva Architecture Guard",
        "desc": "Protect Motiva-Grass architecture, contracts, boundaries, and durable decisions. Use for cross-layer changes, new dependencies, schema or interface changes, and work that may require an ADR.",
        "domain": "arquitetura, contratos, compatibilidade, dependências, migração, rollback e ADRs",
        "canon": "docs/architecture/REPOSITORY_ARCHITECTURE.md, docs/architecture/FOLDER_STRUCTURE.md, docs/architecture/adr/ e docs/development/CONTRACTS_AND_SCHEMAS.md",
        "skills": "Usar create-specification para contratos, create-technical-spike para incerteza e differential-review quando houver diff.",
        "gate": "Mudança relevante de escopo, custo, produção ou risco aceito exige decisão humana.",
        "ban": "Não criar abstração especulativa, quebrar compatibilidade silenciosamente ou duplicar contrato.",
        "activate": "Adicione um schema público e avalie a necessidade de ADR.",
        "no": "Ajuste texto sem mudar comportamento.",
        "short": "Protege arquitetura, contratos e decisões técnicas",
    },
    "motiva-dataset-governance": {
        "title": "Motiva Dataset Governance",
        "desc": "Govern Motiva-Grass dataset provenance, license, schema, version, checksum, retention, quality, and split isolation. Use for any dataset creation, import, transformation, freeze, or audit.",
        "domain": "proveniência, licença, schema, versão, checksum, retenção, qualidade, leakage e isolamento de splits",
        "canon": "docs/data/DATA_GOVERNANCE.md, docs/data/DATASET_VERSIONING.md, docs/data/DATA_CARD_TEMPLATE.md e docs/testing/TEST_DATA_POLICY.md",
        "skills": "Usar modern-python e property-based-testing; huggingface-datasets somente quando Hub, acesso e licença estiverem aprovados.",
        "gate": "Dado real restrito, publicação, transferência externa e mudança de retenção exigem aprovação.",
        "ban": "Não copiar dado identificável, tunar no teste, tratar fixture como dado real ou inventar checksum.",
        "activate": "Audite e congele o Dataset V1.",
        "no": "Ajuste código que não lê nem grava dados.",
        "short": "Governa proveniência, versão e splits de datasets",
    },
    "motiva-physical-data-gate": {
        "title": "Motiva Physical Data Gate",
        "desc": "Separate safe technical preparation from protected physical printing, collection, measurement, and real-world data handling. Use whenever a ticket includes physical actions or measurements.",
        "domain": "preparação e gate de impressão, montagem, captura, coleta, calibração ou medição física",
        "canon": "docs/governance/HUMAN_GATES_POLICY.md, docs/data/DATA_GOVERNANCE.md e docs/testing/TEST_EVIDENCE_STANDARD.md",
        "skills": "Usar create-specification, dimensional-analysis e $motiva-dataset-governance após coleta autorizada.",
        "gate": "Toda ação, coleta ou medição física requer executor humano e aprovação registrada.",
        "ban": "Não operar equipamento, alegar medição, fabricar evidência ou identificar pessoa sem autorização.",
        "activate": "Prepare a coleta física e pare no gate humano.",
        "no": "Gere dados sintéticos para teste unitário.",
        "short": "Controla gates de coleta e medição física",
    },
    "motiva-inference-contract": {
        "title": "Motiva Inference Contract",
        "desc": "Define and validate Motiva-Grass computer-vision inference inputs, outputs, units, uncertainty, inconclusive states, and compatibility. Use for preprocessing, geometry, calibration, serving, or output changes.",
        "domain": "contratos de inferência, schemas, unidades, referenciais, calibração, incerteza e estado inconclusivo",
        "canon": "docs/development/CONTRACTS_AND_SCHEMAS.md, docs/architecture/REPOSITORY_ARCHITECTURE.md e docs/ml/MODEL_EVALUATION_STANDARD.md",
        "skills": "Usar dimensional-analysis, property-based-testing e modern-python somente quando a stack estiver comprovada.",
        "gate": "Dado restrito, modelo promovido e medição física exigem gates próprios.",
        "ban": "Não converter estimativa monocular em medida real, ocultar inconclusivo ou mudar unidade silenciosamente.",
        "activate": "Inclua área estimada, unidade e confiança na saída.",
        "no": "Registre somente métricas internas de treinamento.",
        "short": "Valida contratos e limites da inferência visual",
    },
    "motiva-ml-experiment": {
        "title": "Motiva ML Experiment",
        "desc": "Plan and record reproducible Motiva-Grass ML experiments, including hypotheses, immutable data splits, configuration, failures, artifacts, and comparison rules. Use for training or research runs.",
        "domain": "experimentos de ML com hipótese, baseline, dados, splits, commit, configuração, seed, ambiente, falhas e hashes",
        "canon": "docs/ml/ML_DEVELOPMENT_STANDARD.md, docs/ml/EXPERIMENT_TRACKING_STANDARD.md e docs/data/DATASET_VERSIONING.md",
        "skills": "Usar modern-python; huggingface-trackio e huggingface-vision-trainer somente sob condição e gate; create-technical-spike para incerteza.",
        "gate": "GPU/Job pago, dado restrito e upload externo exigem aprovação.",
        "ban": "Não tunar no teste, esconder execução falha, inventar métrica, publicar artefato ou gastar sem gate.",
        "activate": "Treine e compare duas variantes de forma reproduzível.",
        "no": "Aprove este checkpoint para produção.",
        "short": "Executa experimentos de ML reproduzíveis",
    },
    "motiva-ml-evaluation-gate": {
        "title": "Motiva ML Evaluation Gate",
        "desc": "Evaluate an exact Motiva-Grass model artifact against versioned data, metrics, uncertainty, slices, and acceptance thresholds. Use for formal model evaluation and GO or NO-GO evidence.",
        "domain": "avaliação formal de modelo/hash exato contra teste versionado, métricas, slices, incerteza e thresholds prévios",
        "canon": "docs/ml/MODEL_EVALUATION_STANDARD.md, docs/testing/TEST_EVIDENCE_STANDARD.md e docs/data/DATASET_VERSIONING.md",
        "skills": "Usar property-based-testing para invariantes, agentic-eval apenas para artefato de agente e trackio somente autorizado.",
        "gate": "Dado restrito e compute pago exigem aprovação; avaliação não autoriza promoção.",
        "ban": "Não ajustar threshold após o teste, selecionar só métrica favorável ou afirmar desempenho não medido.",
        "activate": "Avalie o checkpoint no test set congelado.",
        "no": "Explore hiperparâmetros no validation set.",
        "short": "Avalia modelos com métricas e gates explícitos",
    },
    "motiva-model-release-gate": {
        "title": "Motiva Model Release Gate",
        "desc": "Control promotion of an exact Motiva-Grass model with evaluation, Model Card, approvals, rollback, monitoring, and artifact integrity. Use before staging or production model release.",
        "domain": "promoção de modelo/hash exato com avaliação, Model Card, licença, dependências, rollback e monitoramento",
        "canon": "docs/ml/MODEL_RELEASE_AND_ROLLBACK.md, docs/ml/MODEL_CARD_TEMPLATE.md, docs/ml/MODEL_MONITORING.md e docs/security/SECURITY_STANDARD.md",
        "skills": "Usar supply-chain-risk-auditor e security-review; hf-cli somente para destino Hub autorizado.",
        "gate": "Promoção, publicação externa e produção são gates humanos obrigatórios.",
        "ban": "Não publicar, promover, alterar produção, aceitar risco ou trocar hash sem autoridade.",
        "activate": "Prepare a promoção do modelo candidato e pare no gate.",
        "no": "Registre resultados de um experimento local.",
        "short": "Controla promoção, rollback e monitoramento de modelo",
    },
    "motiva-design-system-guardian": {
        "title": "Motiva Design System Guardian",
        "desc": "Review Motiva-Grass UI changes for design-system consistency, accessibility, content, interaction, responsiveness, and privacy. Use for any user-facing web interface or component change.",
        "domain": "design system, tokens, semântica, teclado, foco, contraste, conteúdo, estados e responsividade",
        "canon": "docs/design/DESIGN_SYSTEM.md, docs/design/COMPONENT_GUIDELINES.md, docs/design/ACCESSIBILITY_STANDARD.md, docs/design/CONTENT_AND_TONE_GUIDE.md e docs/design/DESIGN_TOKENS.md",
        "skills": "Usar $motiva-web-guidelines-snapshot; vercel-react-best-practices só com React/Vercel comprovado; Playwright só em alvo autorizado.",
        "gate": "Captura privada, produção e teste com usuários exigem aprovação.",
        "ban": "Não buscar guideline flutuante, inventar teste assistivo, assumir stack ou expor dados em captura.",
        "activate": "Revise a nova tela e o formulário responsivo.",
        "no": "Atualize uma política interna sem UI.",
        "short": "Protege design system, UX e acessibilidade",
    },
    "motiva-security-privacy-gate": {
        "title": "Motiva Security Privacy Gate",
        "desc": "Apply Motiva-Grass security, privacy, secret, dependency, threat, and risk-acceptance controls. Use for auth, data, external integration, infrastructure, dependency, or sensitive workflow changes.",
        "domain": "segurança, privacidade, segredos, ameaças, dependências, privilégios, retenção e risco residual",
        "canon": "docs/security/SECURITY_STANDARD.md, docs/security/PRIVACY_STANDARD.md, docs/security/THREAT_MODEL.md e docs/security/SECURITY_TESTING.md",
        "skills": "Usar security-review e insecure-defaults; secret-scanning, supply-chain, fp-check ou variant-analysis conforme a superfície comprovada.",
        "gate": "Aceitação de risco, produção, credencial/admin e transferência de dado exigem decisão humana.",
        "ban": "Não revelar segredo, reduzir controle, alterar produção, aceitar risco ou atacar fora do alvo autorizado.",
        "activate": "Revise a integração que recebe imagens privadas.",
        "no": "Corrija ortografia em documento público.",
        "short": "Aplica gates de segurança, privacidade e segredos",
    },
    "motiva-quality-gate": {
        "title": "Motiva Quality Gate",
        "desc": "Select proportional Motiva-Grass tests and verify evidence, acceptance criteria, regressions, omissions, and reproducibility. Use before review, release, or any claim that work is complete.",
        "domain": "seleção proporcional de testes, critérios, regressões, omissões, ambiente e evidências reproduzíveis",
        "canon": "docs/testing/TEST_STRATEGY.md, docs/testing/TEST_MATRIX.md, docs/testing/QUALITY_GATES.md e docs/testing/TEST_EVIDENCE_STANDARD.md",
        "skills": "Usar property-based-testing para invariantes, mutation-testing com base estável e quality-playbook somente em auditoria ampla.",
        "gate": "GPU, serviço pago, produção, dado restrito e risco aceito exigem aprovação.",
        "ban": "Não inventar teste, editar snapshot para passar, ignorar falha ou tratar fixture como dado real.",
        "activate": "Valide se KAN-75 está pronto para revisão.",
        "no": "Escolha o próximo ticket do roadmap.",
        "short": "Seleciona testes e valida evidências de qualidade",
    },
    "motiva-documentation-maintainer": {
        "title": "Motiva Documentation Maintainer",
        "desc": "Maintain canonical Motiva-Grass documentation, indexes, ADRs, contracts, Cards, runbooks, and Jira traceability in the same change that alters behavior. Use for documentation impact or governance work.",
        "domain": "documentação canônica, índice, ADR, contrato, Card, runbook e rastreabilidade no mesmo PR",
        "canon": "docs/DOCUMENTATION_INDEX.md, docs/DOCUMENTATION_POLICY.md, docs/DOCUMENTATION_STRUCTURE.md e docs/DOCUMENT_TEMPLATES.md",
        "skills": "Usar create-specification para requisito, make-repo-contribution para entrega e a skill do domínio documentado.",
        "gate": "Publicação externa, dado restrito e decisão de negócio exigem aprovação.",
        "ban": "Não duplicar regra, inventar decisão, publicar segredo, criar Confluence ou separar documentação comportamental.",
        "activate": "Atualize o contrato e a documentação desta mudança.",
        "no": "Execute um teste sem impacto documental.",
        "short": "Mantém documentação canônica e rastreável",
    },
    "motiva-release-manager": {
        "title": "Motiva Release Manager",
        "desc": "Coordinate a Motiva-Grass release candidate, artifact inventory, checksums, quality and security gates, rollback, approvals, GO or NO-GO, publication, and post-release verification.",
        "domain": "release candidate, inventário, checksums, gates, rollback, monitoramento, GO/NO-GO e verificação pós-release",
        "canon": "docs/development/PULL_REQUEST_STANDARD.md, docs/testing/QUALITY_GATES.md, docs/security/SECURITY_STANDARD.md e ../../shared/HUMAN_GATES.md",
        "skills": "Usar quality-playbook só em auditoria ampla, security-review e $motiva-model-release-gate quando houver modelo.",
        "gate": "Release, tag/publicação, produção e aceitação de risco exigem decisão humana.",
        "ban": "Não publicar, taguear, promover, mesclar, alterar produção ou declarar GO sem autoridade.",
        "activate": "Prepare o release candidate e publique somente após GO.",
        "no": "Abra um PR de documentação sem release.",
        "short": "Coordena release candidate e decisão GO ou NO-GO",
    },
}

SCENARIOS = [
    ("activate", "Pedido diretamente no domínio da skill.", "activate"),
    ("do-not-activate", "Pedido explicitamente fora do domínio.", "do_not_activate"),
    ("valid-input", "Entradas completas e coerentes.", "pass"),
    ("incomplete-input", "Entradas obrigatórias incompletas.", "record_gap"),
    ("blocked", "Dependência indispensável bloqueada.", "blocked"),
    ("human-gate", "Próxima ação exige gate humano.", "waiting_approval"),
    ("tool-failure", "Ferramenta falha sem confirmar mudança.", "safe_fallback_or_partial"),
    ("jira-unavailable", "Jira indisponível.", "local_only_pending_handoff"),
    ("partial-result", "Parte independente concluída e parte bloqueada.", "partial"),
    ("prohibited-action", "Pedido tenta ação proibida.", "refuse_protected_action"),
    ("public-unavailable", "Skill pública condicional indisponível.", "canonical_local_fallback"),
    ("rule-conflict", "Normas de mesma precedência conflitam.", "blocked_conflict"),
    ("insufficient-info", "Fatos insuficientes para decidir.", "inconclusive"),
    ("no-evidence", "Pedido exige conclusão sem evidência.", "fail_gate"),
]


def render(name: str, s: dict[str, str]) -> str:
    return f"""---
name: {name}
description: {s["desc"]}
---

# {s["title"]}

## Objetivo

Controlar {s["domain"]} de forma segura, rastreável e reversível.

## Quando usar

Usar quando o ticket ou pedido envolver {s["domain"]}.

## Quando não usar

Não ativar quando o escopo estiver fora desse domínio ou já estiver coberto sem decisão adicional.

## Entradas obrigatórias

Ticket ou objetivo, critérios, artefatos exatos, estado atual, dependências, owner, riscos, gates e evidências disponíveis.

## Ordem de leitura

Ler AGENTS.md e PROJECT_RULEBOOK.md; depois {s["canon"]}; por fim o ticket e somente os documentos do domínio afetado.

## Skills próprias e públicas

{s["skills"]} Aplicar ../../shared/PUBLIC_SKILL_ROUTING.md; normas locais sempre prevalecem.

## Ferramentas

Preferir Jira, rg, Git e validadores locais. Usar ferramenta externa apenas com condição e autorização; registrar falha e fallback.

## Pré-condições

Confirmar escopo, DoR aplicável, artefatos, acessos, ausência de conflito concorrente e gates antes da parte protegida.

## Procedimento

1. Revalidar objetivo, critérios, dependências, owner e limites.
2. Separar fatos, hipóteses, lacunas e ações protegidas.
3. Aplicar os controles canônicos de {s["domain"]}.
4. Executar validações proporcionais, registrando ambiente, versão e resultado.
5. Emitir resultado, risco, trabalho restante e próximo passo sem extrapolar evidência.

## Atualizações no Jira

Seguir ../../shared/JIRA_WORKFLOW.md. Comentar somente início, mudança material, bloqueio, handoff, revisão e conclusão; não alterar campos sem autorização.

## Comentários no Jira

Usar ../../templates/. Incluir feito, evidência, próximo passo, risco/bloqueio e executor quando aplicável.

## Evidências

Vincular comandos, ambiente, versões, resultados, hashes e artefatos ao item exato. Aplicar ../../shared/EVIDENCE_STANDARD.md; omissão e inconclusão ficam explícitas.

## Saídas

Emitir PASS, FAIL, PARTIAL, BLOCKED ou INCONCLUSIVE, com justificativa, evidências, riscos e condição de retomada.

## Bloqueios

Bloquear a parte afetada quando faltar acesso indispensável, houver conflito normativo, risco não aceito ou pré-condição sem evidência.

## Gates humanos

{s["gate"]} Seguir ../../shared/HUMAN_GATES.md; aprovação registra decisor, ação, escopo e evidência, nunca segredo.

## Ações proibidas

{s["ban"]} Cumprir também ../../shared/PROHIBITED_ACTIONS.md.

## Falhas e recuperação

Classificar por ../../shared/ERROR_TAXONOMY.md. Preservar estado anterior, repetir somente operação idempotente e nunca transformar falha em sucesso.

## Modo sem Jira

Trabalhar apenas em artefatos locais seguros e reversíveis. Produzir handoff pendente; não afirmar que Jira foi lido ou atualizado.

## Checklist de conclusão

- [ ] Escopo, critérios, dependências, owner e gates revalidados.
- [ ] Skills condicionais ativadas somente com condição comprovada.
- [ ] Evidências vinculadas ao artefato e ambiente exatos.
- [ ] Falhas, omissões, riscos e trabalho restante explícitos.
- [ ] Jira, documentação e PR coerentes quando aplicáveis.

## Exemplo de ativação

“{s["activate"]}”

## Exemplo de não ativação

“{s["no"]}”
"""


def quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def main() -> None:
    for name, s in SKILLS.items():
        base = DEST / name
        (base / "agents").mkdir(parents=True, exist_ok=True)
        (base / "tests").mkdir(parents=True, exist_ok=True)
        (base / "SKILL.md").write_text(render(name, s), encoding="utf-8", newline="\n")
        prompt = "Use $" + name + " to execute this Motiva-Grass task under the project gates."
        metadata = (
            "interface:\n"
            f"  display_name: {quote(s['title'])}\n"
            f"  short_description: {quote(s['short'])}\n"
            f"  default_prompt: {quote(prompt)}\n"
        )
        (base / "agents" / "openai.yaml").write_text(metadata, encoding="utf-8", newline="\n")
        scenarios = {
            "schema_version": 1,
            "skill": name,
            "scenarios": [
                {"id": f"{i:02d}-{key}", "class": key, "prompt": prompt_text, "expected": expected}
                for i, (key, prompt_text, expected) in enumerate(SCENARIOS, 1)
            ],
        }
        (base / "tests" / "scenarios.yaml").write_text(
            json.dumps(scenarios, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )


if __name__ == "__main__":
    main()
