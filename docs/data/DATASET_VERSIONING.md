# Versionamento de Dataset

Status: **Proposed**. Dados permanecem externos; Git versiona metadados verificáveis.

## Identidade e estados

ID recomendado: `grass-dataset-vMAJOR.MINOR.PATCH` + manifest checksum. Major muda taxonomia/unidade/protocolo/split de forma incompatível; minor adiciona amostras/labels compatíveis; patch corrige metadado sem mover conteúdo semanticamente. Estados: `draft → validated → frozen → deprecated`.

## Manifest obrigatório

Versão/schema, created_at, owner, finalidade, storage URI opaca, algoritmo/checksums, amostras e `group_id`, split, labels/taxonomy version, measurement units/protocol, provenance/license/consent class, transformations, exclusions/quarantine e parents. Manifest não contém PII, secret ou URL assinada.

## Regras

- Raw é imutável; transformação cria versão/derivação com código/config/seed.
- Checksums são recalculados/verificados na ingestão, treino, avaliação e release.
- Split nunca é refeito silenciosamente. Mudança após frozen cria nova versão e análise de impacto; test set requer gate KAN-66.
- Duplicata/near-duplicate e leakage reports acompanham manifest.
- Rollback seleciona manifest/artefato anterior sem sobrescrever versão.

## Checklist

- [ ] ID/estado/parent/schema/taxonomia/unidade.
- [ ] Proveniência, transformações, groups/splits e checksums.
- [ ] Relatórios de qualidade/leakage e storage seguro.
- [ ] Data Card/changelog/deprecation/rollback.

## Riscos e pendências

Ferramenta de versionamento e algoritmo de checksum dependem de KAN-44/106. Sem storage real, URIs permanecem proposta.

