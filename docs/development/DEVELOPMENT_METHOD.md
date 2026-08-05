# Método de Desenvolvimento

## Decisão

Adotar desenvolvimento orientado a tickets, incremental e revisado: um ticket principal por branch, testes e documentação na mesma entrega, ADR para decisões arquiteturais, Bugs e dívida técnica rastreados separadamente. Não há desenvolvimento especulativo fora de KAN-1.

## Justificativa

O MVP combina web, API, visão computacional, dados e ML; lotes pequenos reduzem integração tardia e tornam evidências auditáveis. A política complementa KAN-20 e `docs/governance/AI_EXECUTION_POLICY.md`.

## Alternativas

- Lotes grandes por Épico: rejeitados por aumentar risco e tempo de revisão.
- Desenvolvimento sem ticket para “ganhar velocidade”: rejeitado por perder escopo e rastreabilidade.
- Arquitetura completa antecipada: rejeitada; usar arquitetura evolutiva com fronteiras mínimas firmes.

## Regras obrigatórias

### Fluxo

1. Selecionar ticket pronto conforme KAN-1 e DoR.
2. Definir plano curto, branch e testes.
3. Implementar a menor mudança que satisfaz o aceite.
4. Testar durante a implementação, não ao final do Épico.
5. Atualizar documentação e ADR aplicável.
6. Abrir PR, revisar, corrigir e concluir pela DoD.

### Tamanho

- Ticket recomendado: 0,5 a 3 dias úteis de trabalho focado; limite recomendado de 5 dias.
- PR recomendado: até 400 linhas manuscritas alteradas e 20 arquivos; limite recomendado de 800 linhas ou 40 arquivos. Gerados, lockfiles e snapshots são contados separadamente, mas continuam revisáveis.
- Ultrapassar um limite exige divisão ou justificativa no Jira/PR e revisor adicional quando o risco for alto.

Dividir ticket quando houver mais de um resultado independente, mais de um deploy/revisor especializado, partes entregáveis em ordens diferentes, aceite não verificável em um PR ou estimativa acima de cinco dias.

Criar Subtask somente para parte do mesmo objetivo, já iniciado, que compartilha aceite e não precisa de prioridade independente. Abrir novo ticket para novo objetivo, componente independente, descoberta fora do escopo, Bug preexistente, dívida ou refatoração com risco/valor próprios.

Refatoração permanece no ticket quando pequena, local, necessária à mudança e coberta pelos mesmos testes. Exige ticket separado quando transversal, altera API/arquitetura, domina o diff, muda comportamento, requer migração ou pode ser entregue/priorizada isoladamente.

Trabalho descoberto deve ser classificado: indispensável e dentro do escopo → executar e registrar; defeito introduzido → corrigir; fora do escopo → abrir ticket/Bug/dívida e não implementar; bloqueador → registrar e aplicar política de bloqueio. Nunca “aproveitar o PR” para mudanças oportunistas.

Feature flag é permitida para rollout, experimento ou risco operacional quando houver owner, default seguro, ambientes, telemetria, plano e data/ticket de remoção. Não pode esconder código incompleto nem contornar aceite.

## Regras recomendadas

- Fatias verticais pequenas quando contrato e dependências permitirem.
- Draft PR cedo para colaboração, sem movê-lo a análise antes de estar completo.
- Teste falhando primeiro em Bug/regressão quando praticável.
- Orçamento explícito de complexidade; extrair abstração após repetição comprovada.

## Exemplos

- KAN-76 entrega seleção e preview com testes e docs; arrastar-e-soltar descoberto vira melhoria separada.
- Ajustar uma função interna para testar upload permanece no ticket; redesenhar todo o pipeline de arquivos vira novo ticket/ADR.
- Pesquisa conclui NO-GO com evidências: entrega válida se prevista no aceite.

## Anti-patterns

- Branch por Épico, PR “mega”, refatoração invisível ou TODO sem ticket.
- Criar interface genérica para fornecedor ainda não selecionado.
- Adiar todos os testes/documentos para uma fase futura.
- Feature flag permanente sem owner ou remoção.

## Checklist

- [ ] Um objetivo, um ticket principal e uma branch.
- [ ] Ticket/PR dentro dos limites ou exceção justificada.
- [ ] Descobertas classificadas sem expansão silenciosa.
- [ ] Testes e documentação acompanham a mudança.
- [ ] ADR, Bug, dívida e feature flag tratados quando aplicável.
- [ ] PR revisado e DoD completa.

## Riscos

Fragmentação excessiva pode criar dependências artificiais; limites de tamanho não substituem julgamento. Fatias muito pequenas podem não gerar valor verificável.

## Pontos pendentes

- Definir WIP e SLA de revisão após conhecer a equipe.
- Validar limites de PR após os primeiros 20 PRs.
- Definir ferramenta de feature flags em ticket próprio apenas se necessária.

