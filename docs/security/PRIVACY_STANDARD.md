# Padrão de Privacidade

Status: **Proposed**. Princípios: finalidade, minimização, transparência, controle, segurança e retenção mínima.

## Ciclo da imagem

Antes do envio, informar finalidade, dados/metadados, processamento, retenção, terceiros e contato. Consentimento é afirmativo, específico, registrável e revogável quando base aplicável; não pré-marcar nem condicionar funcionalidade desnecessariamente.

Imagem fica em memória/temporário pelo menor tempo. Default proposto: exclusão ao terminar/falhar/cancelar a requisição; qualquer retenção para melhoria/dataset exige finalidade separada, consentimento/autoridade, storage, prazo, acesso e ticket. EXIF/GPS/nome original são removidos antes de uso persistente. Preview local/object URL é revogado.

## Classificação

- Público: licença validada.
- Interno: metadado técnico não pessoal.
- Confidencial: imagem/dado de coleta autorizado.
- Restrito: PII, GPS, credencial, dataset privado, evidência de segurança.

Restrito não entra em Jira, Git, logs, screenshots, analytics ou CI comum. Terceiro recebe somente mínimo necessário após avaliação de contrato/localização/retenção e gate humano.

## Logs e telemetria

Permitir IDs opacos, versão, duração, código de erro e métricas agregadas. Proibir imagem/URL, EXIF/GPS, nome original, IP completo sem necessidade/base, user-agent bruto persistente, predição ligada a pessoa/local e payload. Retenção e acesso são definidos/testados; ambiente local não é exceção.

## Direitos e operação

Documentar exclusão, acesso/correção quando aplicável, incidente, export e prova de cleanup. Backups respeitam expiração e restauração não reativa dado vencido silenciosamente. Mudança de finalidade/retenção/terceiro ativa KAN-31/gate humano.

## Checklist

- [ ] Finalidade/base/consentimento/transparência.
- [ ] Minimização, classificação e acesso.
- [ ] EXIF/GPS/nome removidos; cleanup/backup testados.
- [ ] Logs/analytics/terceiros permitidos e retidos corretamente.
- [ ] Evidência sanitizada e gate para mudança material.

## Riscos e pendências

Requisitos legais e prazos dependem de jurisdição/owner humano. KAN-31 e KAN-147 fecham a política real; textos não podem prometer antes da implementação.

## Referência

- [NIST Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework)

