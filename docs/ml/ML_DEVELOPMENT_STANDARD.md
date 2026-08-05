# Padrão de Desenvolvimento de ML

Status: **Proposed**. Abrange CV, treinamento, avaliação e integração.

## Regras obrigatórias

- Pergunta/hipótese, baseline, dataset/manifest, split/protocolo, métricas e critério de decisão definidos antes do treino.
- Run registra código, config, seed, ambiente/hardware, dependências, dados, artefatos e todos os resultados/falhas.
- Treino usa train; seleção de arquitetura/features/hyperparameters/thresholds usa validation; test apenas avaliação final congelada.
- Proibido observar test para selecionar feature, threshold ou modelo; comparar protocolos/splits diferentes como equivalentes; publicar só melhor run; excluir falhas/outliers sem regra prévia.
- Seeds e determinismo possível são registrados; variabilidade usa múltiplas runs/intervalos quando material.
- Métricas por classe/faixa/dispositivo/condição e amostra; nenhuma precisão sem `n`, versão e intervalo adequado.
- Unknown/OOD, calibração, incerteza e inconclusivo fazem parte do produto, não pós-processo cosmético.
- Profundidade monocular é sinal relativo/feature experimental; nunca verdade métrica direta sem escala/validação física.
- Treino, avaliação e inferência separados; preprocessing/taxonomia/contrato compartilhados por versão e teste de equivalência.
- Pesos/datasets fora do Git; artefatos por registry, checksum e Model Card.
- Capability opcional tem disponibilidade parcial, timeout, fallback explícito e impacto na resposta.

## Ciclo

Baseline → experimento → validação/calibração → análise OOD/falhas → candidata imutável → avaliação final → decisão KAN-69 → package/equivalence → registry/promoção KAN-139/140.

## Checklist

- [ ] Hipótese/baseline/protocolo/critério pré-definidos.
- [ ] Dados/splits/test protegidos e run reproduzível.
- [ ] Métricas completas, calibração/OOD/incerteza/falhas.
- [ ] Artefato/checksum/Card e compatibilidade runtime.
- [ ] Sem proibições violadas.

## Riscos e pendências

Framework/modelos/licenças dependem de KAN-24–27/91–94. Metas dependem de KAN-23; nenhum número é aprovado aqui.

