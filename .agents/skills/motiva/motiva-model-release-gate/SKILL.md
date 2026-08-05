---
name: motiva-model-release-gate
description: Control promotion of an exact Motiva-Grass model with evaluation, Model Card, approvals, rollback, monitoring, and artifact integrity. Use before staging or production model release.
---

# Motiva Model Release Gate

## Objetivo

Controlar promoção de modelo/hash exato com avaliação, Model Card, licença, dependências, rollback e monitoramento de forma segura, rastreável e reversível.

## Quando usar

Usar quando o ticket ou pedido envolver promoção de modelo/hash exato com avaliação, Model Card, licença, dependências, rollback e monitoramento.

## Quando não usar

Não ativar quando o escopo estiver fora desse domínio ou já estiver coberto sem decisão adicional.

## Entradas obrigatórias

Ticket ou objetivo, critérios, artefatos exatos, estado atual, dependências, owner, riscos, gates e evidências disponíveis.

## Ordem de leitura

Ler AGENTS.md e PROJECT_RULEBOOK.md; depois docs/ml/MODEL_RELEASE_AND_ROLLBACK.md, docs/ml/MODEL_CARD_TEMPLATE.md, docs/ml/MODEL_MONITORING.md e docs/security/SECURITY_STANDARD.md; por fim o ticket e somente os documentos do domínio afetado.

## Skills próprias e públicas

Usar supply-chain-risk-auditor e security-review; hf-cli somente para destino Hub autorizado. Aplicar ../../shared/PUBLIC_SKILL_ROUTING.md; normas locais sempre prevalecem.

## Ferramentas

Preferir Jira, rg, Git e validadores locais. Usar ferramenta externa apenas com condição e autorização; registrar falha e fallback.

## Pré-condições

Confirmar escopo, DoR aplicável, artefatos, acessos, ausência de conflito concorrente e gates antes da parte protegida.

## Procedimento

1. Revalidar objetivo, critérios, dependências, owner e limites.
2. Separar fatos, hipóteses, lacunas e ações protegidas.
3. Aplicar os controles canônicos de promoção de modelo/hash exato com avaliação, Model Card, licença, dependências, rollback e monitoramento.
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

Promoção, publicação externa e produção são gates humanos obrigatórios. Seguir ../../shared/HUMAN_GATES.md; aprovação registra decisor, ação, escopo e evidência, nunca segredo.

## Ações proibidas

Não publicar, promover, alterar produção, aceitar risco ou trocar hash sem autoridade. Cumprir também ../../shared/PROHIBITED_ACTIONS.md.

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

“Prepare a promoção do modelo candidato e pare no gate.”

## Exemplo de não ativação

“Registre resultados de um experimento local.”
