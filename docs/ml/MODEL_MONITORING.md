# Monitoramento de Modelo

Status: **Proposed** para KAN-156. Monitoramento não registra imagem/PII e não substitui ground truth.

## Sinais

- Sistema: volume, sucesso/erro, latência P50/P95, memória, timeout, readiness e versão.
- Entrada: MIME/dimensões/qualidade agregados, marcador detectado, dispositivo/condição permitidos — sem imagem/EXIF/GPS.
- Saída: distribuição agregada de classes/unknown, altura/faixas, confiança/calibração proxy, warnings, fallback/capability e taxa de inconclusivo por motivo.
- Drift: distribuição/feature summary aprovada, mudança de mix/qualidade e performance quando labels tardios existirem.
- Governança: artefato/taxonomia/API/config ativos, rollback/promotion events e incompatibilidades.

## Regras

- Baseline vem de validação/staging e possui janela/versão. Alertas têm threshold, janela, severidade, owner, runbook e anti-noise.
- Drift é sinal de investigação, não causa nem gatilho automático de retreino/promoção.
- Métrica por slice só se privacidade/amostra permitirem; grupos pequenos são suprimidos.
- Aumento de inconclusivo pode ser comportamento seguro; investigar contexto antes de reduzir threshold.
- Resposta: observar → confirmar dados/sistema/modelo → conter/rollback se risco → abrir ticket → coletar labels autorizados → nova versão/avaliação completa.
- Retreino nunca usa produção/test sem governança; produção não redefine test set.

## Checklist

- [ ] Sinais de sistema/entrada/saída/drift/governança.
- [ ] Baseline/janela/threshold/owner/runbook.
- [ ] Privacidade/supressão/retention.
- [ ] Investigação e rollback, sem automação de promoção.

## Riscos e pendências

Ground truth pode ser tardio/ausente; declarar proxies. Stack e thresholds dependem de KAN-143/156 e métricas reais.

## Referência

- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
