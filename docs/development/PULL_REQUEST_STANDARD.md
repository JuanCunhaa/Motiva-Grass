# Padrão de Pull Request

## Decisão

Todo trabalho versionado usa PR exclusivo, título `[KAN-N] Descrição objetiva`, revisão obrigatória e o template abaixo.

## Justificativa

O PR é a fonte oficial da mudança, evidências, revisão, riscos e rollback. Um template único reduz omissões entre web, API, dados e ML.

## Alternativas

- Templates separados por área: adiar até existir divergência comprovada.
- Corpo livre: rejeitado por baixa auditabilidade.
- Merge automático ao CI verde: rejeitado; CI não valida escopo/risco sozinho.

## Regras obrigatórias

```markdown
## Ticket Jira
- [KAN-N](https://gp16-motiva.atlassian.net/browse/KAN-N)

## Objetivo
<resultado verificável>

## Contexto
<por que e premissas>

## Alterações
- <mudança>

## Fora do escopo
- <limite ou N/A>

## Arquitetura impactada
- Módulos/fronteiras: <lista>
- ADR: <link ou N/A>

## Testes e resultados
| Teste/comando | Ambiente | Resultado | Evidência |
|---|---|---|---|
| | | | |

## Evidências e screenshots
<links; sem dados sensíveis; N/A justificado>

## Impactos
- Segurança: <impacto/revisão ou N/A>
- Privacidade: <impacto/revisão ou N/A>
- Dados: <schema, proveniência, migração ou N/A>
- ML: <dataset/modelo/métricas/fallback ou N/A>
- Acessibilidade/i18n: <impacto ou N/A>
- Operação/custo: <impacto ou N/A>

## Documentação
- <arquivos/links atualizados>

## Riscos e limitações
- <risco, controle e residual>

## Rollback
<passos, compatibilidade e dados>

## Checklist
- [ ] Escopo e critérios Jira verificados.
- [ ] Branch/commits seguem o padrão.
- [ ] Testes aplicáveis executados; N/A justificado.
- [ ] Contratos e consumidores validados.
- [ ] Sem secrets, pesos, datasets reais ou imagens privadas.
- [ ] Documentação/ADR atualizados.
- [ ] Segurança, privacidade, dados, ML e acessibilidade avaliados.
- [ ] Bugs/dívida/feature flags relacionados.
- [ ] Rollback é executável e proporcional ao risco.
```

PR fica em draft enquanto incompleto. Antes de review deve estar dentro dos limites de tamanho, sem conversas não resolvidas críticas, com CI aplicável verde e descrição atualizada ao diff real. Revisor não aprova área fora de sua competência quando CODEOWNERS exigir especialista.

## Regras recomendadas

- Guiar o revisor por commits/ordem lógica e destacar arquivos críticos.
- Screenshot antes/depois para UI; golden diff para contrato; métricas comparáveis para ML.
- Responder feedback com mudança ou justificativa, sem marcar thread prematuramente.

## Exemplos

- PR de schema inclui golden files, compatibilidade web/API e plano de versão.
- PR de UI usa fixture sanitizada e screenshots sem foto real privada.

## Anti-patterns

- `N/A` em todas as seções sem justificativa.
- Evidência em link pessoal/efêmero, screenshot com localização ou métrica sem versão de dataset.
- Alterar objetivo Jira dentro do PR.
- Aprovar o próprio risco material sem gate.

## Checklist

- [ ] Template completo corresponde ao diff atual.
- [ ] Título, Jira, ADRs e documentação ligados.
- [ ] Testes/evidências reproduzíveis e sanitizados.
- [ ] Revisores/owners corretos solicitados.
- [ ] Riscos, limitações e rollback explícitos.
- [ ] Aprovação e checks antes do merge.

## Riscos

Template pode virar burocracia; campos N/A justificados e tamanho proporcional mitigam. Evidência extensa deve morar no sistema oficial, com resumo no PR.

## Pontos pendentes

- KAN-19/KAN-84 devem publicar o template real e CODEOWNERS.
- Definir checks obrigatórios por path em KAN-80/KAN-134.

