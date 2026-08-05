# Templates documentais

Copie apenas o bloco aplicável. Não remova seções obrigatórias; marque `Não aplicável` com justificativa. Para dados e modelos, use [Data Card](data/DATA_CARD_TEMPLATE.md) e [Model Card](ml/MODEL_CARD_TEMPLATE.md), sem duplicá-los aqui.

## Ticket Jira

```markdown
## Contexto
## Resultado esperado
## Escopo / fora de escopo
## Critérios de aceite verificáveis
## Riscos e gates humanos
## Evidências exigidas
## Dependências e links
```

## ADR

```markdown
# ADR-NNNN — Título
Status: proposta | aceita | substituída
Data: AAAA-MM-DD
Decisores:

## Contexto
## Opções consideradas
## Decisão
## Consequências e riscos
## Validação
## Referências
```

## Pesquisa técnica

```markdown
# Pergunta
## Hipótese e critérios
## Fontes e data da consulta
## Método
## Resultados, inclusive negativos
## Limitações
## Recomendação e decisão humana pendente
```

## Experimento

Use o esquema de `docs/ml/EXPERIMENT_TRACKING_STANDARD.md`: objetivo, código, ambiente, dataset, configuração, seed, métricas completas, artefatos, falhas e conclusão.

## Runbook

```markdown
# Operação
Owner:                 Última validação:
## Pré-condições e permissões
## Diagnóstico
## Procedimento seguro
## Validação
## Rollback
## Escalação
## Evidência e auditoria
```

## Postmortem

```markdown
# Incidente — data e impacto
## Resumo
## Linha do tempo factual
## Detecção e resposta
## Causas e fatores contribuintes
## O que funcionou / não funcionou
## Ações, responsáveis e prazos
## Evidências e aprendizado
```

## Relatório de QA

```markdown
# Escopo e versão avaliada
## Ambiente e dados
## Matriz executada
## Resultados e evidências
## Defeitos e riscos residuais
## Testes não executados e motivo
## Recomendação: aprovar | bloquear | aprovar com risco aceito
```

## GO/NO-GO

```markdown
# Release / artefato / checksum
## Gates e evidências
## Riscos e exceções vigentes
## Rollback validado
## Monitoramento e responsáveis
## Decisão: GO | NO-GO
Aprovadores:             Data:
```

## Release notes

```markdown
# Versão e data
## Valor entregue
## Mudanças de comportamento e contrato
## Migração ou ação necessária
## Limitações conhecidas
## Segurança e privacidade
## Rollback e suporte
## Tickets e artefatos
```
