---
name: motiva-work-selector
description: Select the next executable Motiva-Grass Jira ticket from KAN-1 using readiness, dependency, priority, ownership, gate, and concurrent-work rules. Use before starting backlog work or when the current ticket becomes fully blocked.
---

# Motiva Work Selector

## Objetivo

Controlar seleção de um único ticket executável na primeira frente aberta de KAN-1 de forma segura, rastreável e reversível.

## Quando usar

Usar quando o ticket ou pedido envolver seleção de um único ticket executável na primeira frente aberta de KAN-1.

## Quando não usar

Não ativar quando o escopo estiver fora desse domínio ou já estiver coberto sem decisão adicional.

## Entradas obrigatórias

Ticket ou objetivo, critérios, artefatos exatos, estado atual, dependências, owner, riscos, gates e evidências disponíveis.

## Ordem de leitura

Ler AGENTS.md e PROJECT_RULEBOOK.md; depois docs/governance/DEFINITION_OF_READY.md, docs/governance/JIRA_WORKFLOW_POLICY.md e ../../shared/LABELS_AND_PRIORITIES.md; por fim o ticket e somente os documentos do domínio afetado.

## Skills próprias e públicas

Entregar a decisão a $motiva-jira-ticket-executor e $motiva-ticket-orchestrator; usar create-specification apenas para lacunas formalizáveis. Aplicar ../../shared/PUBLIC_SKILL_ROUTING.md; normas locais sempre prevalecem.

## Ferramentas

Preferir Jira, rg, Git e validadores locais. Usar ferramenta externa apenas com condição e autorização; registrar falha e fallback.

## Pré-condições

Confirmar escopo, DoR aplicável, artefatos, acessos, ausência de conflito concorrente e gates antes da parte protegida.

## Procedimento

1. Revalidar objetivo, critérios, dependências, owner e limites.
2. Separar fatos, hipóteses, lacunas e ações protegidas.
3. Aplicar os controles canônicos de seleção de um único ticket executável na primeira frente aberta de KAN-1.
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

A seleção não vale como aprovação de qualquer gate do ticket. Seguir ../../shared/HUMAN_GATES.md; aprovação registra decisor, ação, escopo e evidência, nunca segredo.

## Ações proibidas

Não reordenar roadmap, alterar prioridade, assumir lacunas ou selecionar múltiplos tickets. Cumprir também ../../shared/PROHIBITED_ACTIONS.md.

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

“Qual é o próximo ticket executável do roadmap?”

## Exemplo de não ativação

“Execute KAN-42, quando a seleção já foi dada e permanece válida.”
