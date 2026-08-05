# Matriz de Testes por Componente

Status: **Proposed**. `P` PR, `S` scheduled, `M` manual/release, `G` GPU aprovado.

| Componente | Unit/Component | Integração/Contrato | E2E/Manual | Não funcionais |
|---|---|---|---|---|
| contracts | schema/generator P | golden + web/API/model P | compatibilidade M | breaking diff P |
| web UI | state/component/a11y P | client mock/contract P | jornada/browser P/S; device M | visual P/S, bundle/perf S |
| câmera/upload local | validators P | browser APIs fake P | câmera/device/permission M | memória/privacidade M |
| API upload | validators/mappers P | multipart/lifecycle P | inválidos E2E P | abuse/decompression/mem S |
| domain/orchestrator | unit/property P | adapters fake P | modos degradados P | timeout/cancel P |
| image quality | unit/golden P | pipeline P | amostra aprovada M | benchmark S |
| geometry | unit/property/golden P | pipeline P | marcador físico M | precisão/robustez S/M |
| inference runtime | unit/smoke CPU P | artefato/equivalência P/S | candidate M | CPU mem/latency S; GPU G |
| training | unit/dry-run P | resume/artifact S | experimento M | GPU G, determinismo S |
| evaluation | metric/golden P | frozen split S | revisão estatística M | calibration/OOD S |
| datasets | schema/transform P | adapter/storage S | auditoria M | dedup/leakage/split S |
| registry/promotion | manifest/checksum P | registry sandbox S | promoção/rollback M | permissão/auditoria M |
| infra/deploy | validate/plan P | preview S | smoke/rollback M | carga/capacidade S/M |
| observability | event/redaction P | sink sandbox S | alerta/runbook M | volume/retention S |
| docs | lint/link P | exemplos/schema P | revisão owner M | accessibility de docs M |

## Regras

Mudança executa a linha afetada e consumidores. `S/M/G` pendente impede release quando obrigatório; indisponibilidade não vira pass. Dados privados reais são proibidos em CI comum.

## Checklist

- [ ] Linhas/consumidores afetados selecionados.
- [ ] Frequência e ambiente corretos.
- [ ] Evidência conforme padrão e gate aplicado.

## Riscos e pendências

Ferramentas e budgets serão preenchidos em KAN-33/34/87/127/135/146.
