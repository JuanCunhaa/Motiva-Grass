# Release e Rollback de Modelo

Status: **Proposed**. Fonte canônica de registry/promoção KAN-139/140.

## Estados e gates

`candidate → validated → staging → production → retired`; `rejected` é terminal salvo novo artefato. Cada transição registra actor, data, origem/destino, checksum, evidência e aprovação.

| Gate | Requisitos |
|---|---|
| candidate→validated | protocolo final, métricas/Model Card, KAN-69 GO/limitations |
| validated→staging | package equivalence, checksum, API/taxonomy/preprocessing compatibility, smoke/security |
| staging→production | smoke/perf/monitoring/rollback, release candidate exata e gate humano |

## Regras obrigatórias

- Promover por referência imutável; nunca recompilar/retreinar/copiar peso diferente após avaliação.
- Manifest inclui model/data/code/config/preprocessing/taxonomy/contract/capabilities/checksums.
- Runtime falha readiness se incompatível; não escolhe “latest” nem fallback de artefato silencioso.
- Rollback aponta ao pacote anterior aprovado, sem recompilar, e valida health/smoke/compatibilidade. Mudança de schema/dado tem plano separado.
- Canary/feature flag somente com métricas, limite, owner e stop condition. Promoção/produção é gate humano.

## Checklist

- [ ] Artefato avaliado=registrado=promovido por checksum.
- [ ] Manifest/Card/equivalência/compatibilidade.
- [ ] Aprovação, smoke/perf/security/monitoring.
- [ ] Rollback testado e artefato anterior disponível.

## Riscos e pendências

Registry/deploy/custos dependem de KAN-95/97/98/139–143. Rollback pode não desfazer contrato incompatível; breaking exige migração.

