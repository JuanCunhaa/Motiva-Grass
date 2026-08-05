# Padrão de Avaliação de Modelos

Status: **Proposed**. Avaliação final segue KAN-66/67/68/120–122 e critérios KAN-23.

## Protocolo

Pré-registrar candidata/checksum, dataset/split checksum, métricas, slices, amostra, bootstrap/intervalos, thresholds e regra GO/NO-GO. Rodar uma vez no test congelado após seleção/calibração; acesso é auditado. Correção que observa test exige declarar contaminação e nova governança, não repetir silenciosamente.

## Métricas mínimas

- Classificação: per-class/macro, matriz, unknown/OOD, calibration/reliability e coverage.
- Segmentação: métricas definidas + distribuição/slices e falhas.
- Altura: MAE/erro por faixa, bias, interval coverage/width e amostra.
- Sistema: taxa conclusivo/inconclusivo, warnings/fallbacks, latência/memória e estabilidade.
- Geometria: detecção/erro/uncertainty por condição; monocular não é ground truth métrico.

Relatar `n`, distribuição, intervalo e todas as runs pré-definidas. Não excluir falha para melhorar número; análise de erro separa dado, geometria, modelo, contrato e produto. Modelos só são comparáveis sob protocolo idêntico; caso contrário, relatório qualitativo/novo experimento.

## Decisão

GO, GO WITH LIMITATIONS ou NO-GO por critérios previamente aprovados. Limitação material e mudança de threshold ativam gate. A candidata permanece imutável; Model Card recebe métricas/limitações completas.

## Checklist

- [ ] Protocolo/candidata/test checksum pré-registrados.
- [ ] Métricas/slices/calibração/OOD/incerteza/sistema.
- [ ] Falhas e `n` completos; sem cherry-pick.
- [ ] Decisão e Card rastreáveis.

## Riscos e pendências

Metas/intervalos dependem de KAN-23/121. Test set insuficiente produz inconclusão/NO-GO, não precisão inventada.

