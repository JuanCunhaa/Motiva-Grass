# Padrão de Erros e Logs

## Decisão

Usar erros tipados por categoria/código, mapeamento explícito para mensagens localizadas e logs JSON estruturados com `request_id` e `correlation_id`. Falhas e fallbacks nunca são ocultados.

## Justificativa

Imagens, EXIF, localização e predições podem ser sensíveis; o pipeline possui dependências opcionais e precisa distinguir inválido, inconclusivo, indisponível e erro interno.

## Alternativas

- Exceções/texto livre: rejeitado por instabilidade e vazamento.
- Logar payload para depuração: proibido por privacidade.
- Retornar sempre 500: rejeitado por impedir comportamento determinístico.

## Regras obrigatórias

### Taxonomia

- `ValidationError`: entrada/config/schema inválido; código público `VALIDATION_*`.
- `DomainError`: regra/qualidade/OOD/inconclusivo; `DOMAIN_*`.
- `ExternalDependencyError`: storage/registry/serviço; `DEPENDENCY_*`.
- `InfrastructureError`: memória, disco, runtime, timeout; `INFRA_*`.
- `UnexpectedError`: falha não classificada; público `INTERNAL_ERROR`, detalhes só internos.

Cada erro contém código estável, mensagem interna, retryability, HTTP mapping futuro, contexto sanitizado e `cause`. Usuário recebe código, mensagem `pt-BR`/`en`, ação segura e request ID; nunca stack trace, caminho, fornecedor interno ou secret.

`request_id` é único por requisição; `correlation_id` liga operações relacionadas. Validar ID recebido ou gerar UUID/ULID; propagar em headers, logs e chamadas externas. Não usar dado do usuário como ID.

### Logs

JSON com timestamp UTC, level, service, environment, event, code, request/correlation ID, version, duração e contexto permitido. Níveis: `DEBUG` diagnóstico local controlado; `INFO` lifecycle sem payload; `WARN` modo degradado/recuperável; `ERROR` falha da operação; `CRITICAL` risco/indisponibilidade ampla.

Redaction ocorre antes do sink e é testada. Proibido registrar: bytes/URL de imagem, EXIF, GPS/localização, credencial/token/cookie/header sensível, dado pessoal, caminho absoluto do usuário, dataset real, prompt cru, logits/vetores, resposta detalhada do modelo ou stack trace em produção. Permitidos, quando necessários: identificador opaco, tamanho/MIME validado, versão/checksum do artefato, código do resultado, métricas agregadas sem reidentificação.

Local pode ter stack trace e DEBUG por opt-in, ainda sem secrets/dados reais. Produção usa INFO por padrão, stack trace apenas no sink restrito e retenção definida. Fallback registra capability ausente, motivo, alternativa usada e efeito na confiança/resposta.

## Regras recomendadas

- Eventos nomeados (`analysis.started`, `model.load.failed`) em vez de frases variáveis.
- Sampling somente em eventos de alto volume; erros críticos nunca amostrados.
- Métricas separadas de logs; auditoria de promoção separada de telemetria.
- Testes automáticos de redaction e estabilidade de códigos.

## Exemplos

```json
{"level":"WARN","event":"inference.fallback","code":"DEPENDENCY_MOGE_UNAVAILABLE","request_id":"...","fallback":"rgb_only"}
```

Ao usuário: `Não foi possível concluir a análise. Código: DOMAIN_IMAGE_INCONCLUSIVE. Referência: <request_id>`.

## Anti-patterns

- `logger.info(image_base64)`, `print(exception)` ou `except: return None`.
- Mensagem pública com `/home/user/model.pt`, bucket, classe interna ou token.
- Logar sucesso após fallback sem indicar limitação.

## Checklist

- [ ] Categoria/código/retry/mapeamento definidos.
- [ ] Request/correlation IDs propagados.
- [ ] Mensagem pública localizada e sanitizada.
- [ ] Logs JSON, níveis corretos e redaction testada.
- [ ] Nenhum dado proibido; local/produção diferenciados.
- [ ] Fallback/timeout/cancelamento visíveis.

## Riscos

Redaction tardia ainda pode vazar; deve ocorrer na origem. Contexto insuficiente dificulta diagnóstico; usar IDs e metadados técnicos permitidos, não payload.

## Pontos pendentes

- KAN-31 define retenção/telemetria; KAN-96 fecha matriz de falhas; KAN-126 fecha códigos HTTP/headers.
- Stack/sink de observabilidade depende de KAN-97/KAN-143.

