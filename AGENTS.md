# Motiva Grass — guia operacional para agentes

Este resumo é obrigatório. O [PROJECT_RULEBOOK](PROJECT_RULEBOOK.md) define precedência e o [índice](docs/DOCUMENTATION_INDEX.md) aponta para as normas completas.

## Ordem de leitura

1. `AGENTS.md` e `PROJECT_RULEBOOK.md`.
2. KAN-1, épico pai, ticket principal, KAN-20 e dependências.
3. documentos canônicos dos domínios afetados.
4. ADRs, contratos, código e evidências existentes.

## Seleção do ticket

- Execute um único ticket principal.
- Respeite a primeira frente executável de KAN-1; dentro dela: `priority-p0`, `priority-p1`, `priority-p2`.
- Verifique Definition of Ready, pai, labels, links, `Blocks`, duplicidade, owner, trabalho concorrente, dados, acessos e gates.
- Não invente lacuna: registre-a e mantenha o item em `Tarefas pendentes` se impedir execução.

## Jira e comentários

- Jira é a fonte de objetivo, escopo, responsável, prioridade, dependências e estado.
- Comente início antes de mover para `Em andamento`.
- Comente mudança material, marco longo, bloqueio, handoff e conclusão; evite comentário sem informação nova.
- Todo comentário relevante inclui feito, evidência, próximo passo, risco/bloqueio e executor quando aplicável.
- Bloqueio: marque `Flagged = Impediment`, label `blocked-*`, explique impacto e ação necessária; volte a `Tarefas pendentes` quando nada útil puder avançar.

## Estados

- `Tarefas pendentes`: não iniciado, DoR incompleta ou bloqueio total.
- `Em andamento`: DoR completa, início registrado e atividade real.
- `Em análise`: entrega, testes, evidências, documentação, critérios e PR completos.
- `Concluído`: merge/revisão/checks aplicáveis, DoD e comentário final completos, sem bloqueador crítico.

## Branch, commits e PR

- Branch: `tipo/KAN-N-descricao-curta`.
- Commit: Conventional Commits + `[KAN-N]`.
- PR: `[KAN-N] descrição objetiva`.
- Um ticket por branch e PR, salvo exceção prévia registrada e aprovada.
- Preserve mudanças alheias; não reescreva histórico compartilhado.
- PR inclui escopo, critérios, arquivos, testes/resultados, evidências, documentos, impactos, riscos, gates e rollback.

## Testes e evidências

- Aplique `docs/testing/TEST_STRATEGY.md`, a matriz e os quality gates proporcionais ao risco.
- Registre versão, ambiente, comando/workflow, dados, resultado e artefatos.
- Falha, omissão e teste não executado são explícitos. GPU indisponível não significa aprovação.
- Nunca invente execução, métrica, medição ou evidência; fixture não é dado real.

## Documentação

- Atualize norma, contrato, ADR, Card ou runbook no mesmo PR que muda o comportamento.
- Não duplique regra: linke o arquivo canônico de `docs/DOCUMENTATION_INDEX.md`.
- Decisão transversal/duradoura exige ADR; decisão local reversível pode ficar no PR.

## Segurança, dados e ML

- Menor privilégio e defesa em profundidade; nunca exponha segredo, dado pessoal, mídia privada, dataset restrito, peso ou saída identificável.
- Dado exige proveniência, licença, schema, versão, checksum, retenção e separação de splits.
- Experimento registra inclusive falhas; conjunto de teste não orienta tuning.
- Modelo só é promovido com artefato exato, avaliação, Model Card, aprovação aplicável, rollback e monitoramento.
- Resultado inconclusivo ou estimativa monocular não vira afirmação métrica.

## Gates humanos

Pare a parte afetada diante de licença, negócio, mudança relevante de escopo, ação/medição física, credencial, administração, contratação/custo, produção, risco aceito, dado real restrito, promoção de modelo ou release. Registre decisor, ação, escopo e evidência da aprovação — nunca o segredo.

Sem `gate-human`, decisões técnicas reversíveis dentro do ticket podem avançar. Continue apenas trabalho independente, seguro e reversível.

## Bugs, interrupção e encerramento

- Corrija no ticket atual apenas defeito pequeno criado pela mudança e indispensável ao aceite; caso contrário, registre Bug separado conforme a política.
- Hipótese não é causa confirmada. Resultado parcial lista feito, ausente, motivo, impacto e continuação.
- Interrompa em conflito normativo, acesso indispensável ausente, risco não aceito ou ação irreversível sem autoridade.
- `NO-GO` só conclui quando produzir essa decisão é o objetivo aceito.
- Done exige critérios, testes, documentação, evidências, revisão, rastreabilidade e estado Jira coerente.
