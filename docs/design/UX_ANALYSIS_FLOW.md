# Fluxo UX da Análise

Status: **Proposed** — canônico para KAN-75, KAN-76, KAN-78 e KAN-129–132.

## Máquina de estados

`intro → consent → selecting/camera → local-validating → preview → ready → uploading → processing → result|warning|inconclusive|error → retry|new-analysis`.

Cancelamento é possível em upload/processamento quando tecnicamente suportado; resposta tardia cancelada não altera a tela.

## Jornada

1. **Entrada:** H1, benefício limitado e CTA “Selecionar uma foto”. Explicar que é estimativa experimental.
2. **Explicação:** três passos, requisitos da foto/marcador e link metodologia.
3. **Consentimento:** finalidade, processamento, retenção/exclusão e ação afirmativa não pré-marcada.
4. **Seleção:** arquivo ou câmera equivalentes; tipos/limites visíveis.
5. **Câmera:** pedir permissão após ação; instruir luz, distância, marcador, estabilidade; alternativa arquivo.
6. **Validação local:** formato/tamanho/dimensões básicas; não alegar validação final.
7. **Preview:** imagem inteira, nome sanitizado opcional, remover/substituir.
8. **Qualidade:** checklist acionável; warning não bloqueia salvo requisito mínimo.
9. **Envio:** resumo de consentimento e CTA “Analisar imagem”.
10. **Processamento:** etapas verdadeiras ou indeterminado; request ID; cancelar; não inventar porcentagem.
11. **Erro:** código estável, linguagem simples, entrada preservada quando seguro, retentar sem duplicar.
12. **Resultado:** espécie provável + confiança; altura estimada + unidade/intervalo; qualidade; versão/data; limitações.
13. **Warning:** resultado permanece, mas impacto e recomendação ficam junto do campo afetado.
14. **Inconclusivo:** nenhum valor fabricado; motivo específico e ação (nova foto, marcador, condição suportada).
15. **Nova análise:** limpa imagem/estado/request e solicita consentimento novamente se finalidade/política exigir.

## Conteúdo de resultado

| Campo | Apresentação |
|---|---|
| espécie provável | nome + “provável”; unknown quando apropriado |
| confiança | percentual calibrado com explicação, não “certeza” |
| altura | “estimada”, cm e precisão coerente |
| intervalo | faixa e nível/método quando definido |
| qualidade | dimensões relevantes e impacto |
| limitações/warnings | próximos ao resultado afetado |
| inconclusão | código/motivo e ação recomendada |

## Regras obrigatórias

- Não persistir preview além do necessário; revogar object URLs.
- Campos ausentes permanecem ausentes; nunca zero/“N/A” ambíguo.
- Retentativa idempotente/explicada; nova análise reinicia estado.
- Foco segue mudança de etapa; progresso/erro/resultado são anunciados.

## Testes e checklist

- [ ] Caminhos arquivo/câmera, permissão negada, inválido, substituir e cancelar.
- [ ] Normal, warning, inconclusivo, timeout, offline e retry sem duplicação.
- [ ] Teclado, SR, 200% zoom, mobile portrait/landscape, reduced motion.
- [ ] Textos correspondem ao contrato e à política real de privacidade.

## Riscos e pendências

Progresso real depende da API; usar indeterminado até existir contrato. Consentimento/retenção dependem de KAN-31. Métricas/metas finais dependem de KAN-23/69/121.

