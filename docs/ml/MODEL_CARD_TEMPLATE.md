# Template de Model Card

```markdown
# Model Card — <nome> <versão/checksum>

- Status: <candidate|validated|staging|production|rejected|retired>
- Owner/data/tickets: <papel>/<ISO>/<KAN-N>
- Run, code, dataset, config, taxonomy, preprocessing e contract: <IDs/versões>

## Finalidade e fora do escopo
<usuários, decisões suportadas e proibidas>

## Arquitetura e artefato
<família, heads, package format, size, checksum, licença e dependencies>

## Dados e protocolo
<Data Card, splits/frozen test, unidades e amostras>

## Métricas e calibração
<todas as métricas/slices/n/intervalos/runs; não só melhor>

## Unknown, OOD, incerteza e inconclusivo
<métodos, thresholds de validation, coverage e ações>

## Limitações, falhas e riscos
<galeria referenciada, vieses, condições e segurança/privacidade>

## Runtime e compatibilidade
<CPU/GPU, memória/latência, API/taxonomia/preprocessing/capabilities/fallbacks>

## Monitoramento e rollback
<métricas, thresholds, owner, artifact anterior e triggers>

## Aprovação e changelog
<GO/NO-GO, revisores, datas e diferenças>
```

## Regras

Card descreve o artefato exato/checksum; `não medido` substitui invenção. Atualização de status não altera métricas históricas.

## Checklist

- [ ] Identidade/proveniência/licença.
- [ ] Dados/protocolo/métricas completas.
- [ ] OOD/incerteza/limitações/riscos.
- [ ] Runtime/compatibilidade/monitoramento/rollback/aprovação.

## Riscos e pendências

Preenchimento real depende de KAN-61/65/68/69/82/139.

