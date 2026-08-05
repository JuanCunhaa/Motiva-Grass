# Padrão de Rastreamento de Experimentos

Status: **Proposed**. Todo run, inclusive falho/abortado, recebe ID imutável.

## Metadados obrigatórios

`run_id`, ticket/objetivo/hipótese, timestamp/owner, git commit/dirty flag, environment/container/dependencies, hardware/CPU/GPU, dataset manifest/checksum e splits, schema/taxonomy/preprocessing versions, config completa, seeds/determinism flags, parent/baseline, métricas por época/finais, duração/recursos/custo, artifacts/checksums, status/failure/cancellation e notes/limitations.

## Regras

- Config é declarativa e armazenada antes do run; override é registrado.
- Métrica não é editada; correção cria run/report derivado.
- Comparação exige mesmo protocolo/dataset/split/métrica ou destaca incompatibilidade.
- Run falho não é apagado; segredo, dado/imagem e URL assinada não entram no tracker.
- Artefato promovível liga run → dataset → code → config → metrics → Model Card.
- Pesquisa exploratória/notebook exporta config/resultados para tracker; notebook não é fonte única.

## Checklist

- [ ] Identidade/hipótese/code/env/hardware.
- [ ] Dados/config/seed/protocolo.
- [ ] Métricas/recursos/status/falhas.
- [ ] Artefatos/checksums/parent/Card.

## Riscos e pendências

Ferramenta/local de tracking depende de KAN-95 e gate para serviço pago. Retenção/acesso seguem KAN-31/106.

