---
name: motiva-design-system-guardian
description: Review Motiva-Grass UI changes for design-system consistency, accessibility, content, interaction, responsiveness, and privacy. Use for any user-facing web interface or component change.
---

# Motiva Design System Guardian

## Objetivo

Controlar design system, tokens, semântica, teclado, foco, contraste, conteúdo, estados e responsividade de forma segura, rastreável e reversível.

## Quando usar

Usar quando o ticket ou pedido envolver design system, tokens, semântica, teclado, foco, contraste, conteúdo, estados e responsividade.

## Quando não usar

Não ativar quando o escopo estiver fora desse domínio ou já estiver coberto sem decisão adicional.

## Entradas obrigatórias

Ticket ou objetivo, critérios, artefatos exatos, estado atual, dependências, owner, riscos, gates e evidências disponíveis.

## Ordem de leitura

Ler AGENTS.md e PROJECT_RULEBOOK.md; depois docs/design/DESIGN_SYSTEM.md, docs/design/COMPONENT_GUIDELINES.md, docs/design/ACCESSIBILITY_STANDARD.md, docs/design/CONTENT_AND_TONE_GUIDE.md e docs/design/DESIGN_TOKENS.md; por fim o ticket e somente os documentos do domínio afetado.

## Skills próprias e públicas

Usar $motiva-web-guidelines-snapshot; vercel-react-best-practices só com React/Vercel comprovado; Playwright só em alvo autorizado. Aplicar ../../shared/PUBLIC_SKILL_ROUTING.md; normas locais sempre prevalecem.

## Ferramentas

Preferir Jira, rg, Git e validadores locais. Usar ferramenta externa apenas com condição e autorização; registrar falha e fallback.

## Pré-condições

Confirmar escopo, DoR aplicável, artefatos, acessos, ausência de conflito concorrente e gates antes da parte protegida.

## Procedimento

1. Revalidar objetivo, critérios, dependências, owner e limites.
2. Separar fatos, hipóteses, lacunas e ações protegidas.
3. Aplicar os controles canônicos de design system, tokens, semântica, teclado, foco, contraste, conteúdo, estados e responsividade.
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

Captura privada, produção e teste com usuários exigem aprovação. Seguir ../../shared/HUMAN_GATES.md; aprovação registra decisor, ação, escopo e evidência, nunca segredo.

## Ações proibidas

Não buscar guideline flutuante, inventar teste assistivo, assumir stack ou expor dados em captura. Cumprir também ../../shared/PROHIBITED_ACTIONS.md.

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

“Revise a nova tela e o formulário responsivo.”

## Exemplo de não ativação

“Atualize uma política interna sem UI.”
