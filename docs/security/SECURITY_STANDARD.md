# Padrão de Segurança

Status: **Proposed**. Defesa em profundidade para web, API, ML, supply chain e infraestrutura.

## Upload e processamento

- Allowlist inicial somente de formatos de imagem exigidos pelo produto; extensão é dica, nunca prova.
- Decodificar nome, limitar comprimento/caracteres, ignorar nome original no storage e gerar ID aleatório.
- Validar Content-Type declarado, magic/signature, decoder seguro e consistência; nenhuma técnica isolada basta.
- Limites configurados e testados: bytes, pixels, largura/altura, frames, ratio e custo de decodificação; rejeitar decompression bombs/malformados antes do modelo.
- Processar fora do webroot, sem execução, com least privilege, temporário isolado e exclusão garantida em sucesso/erro/timeout/cancelamento.
- Remover EXIF/GPS antes de persistência/telemetria; nunca retornar arquivo ativo. Malware/CDR somente se formato/risco justificar e privacidade aprovar.

## API e infraestrutura

- CORS allowlist por ambiente; credenciais somente quando necessárias. Headers: CSP para web, `nosniff`, frame policy, referrer e transport security em produção conforme arquitetura.
- Rate limit, concorrência, queue/bulkhead, timeout, cancelamento e budgets de CPU/GPU/memória por identidade/IP com tratamento de NAT e abuso.
- Respostas usam códigos estáveis, request ID e nenhum detalhe interno.
- Secrets em secret manager/CI protegido, rotacionáveis, mínimo privilégio e nunca bundle/log/Jira/Git.
- Permissões por serviço/ambiente; produção separada, IaC revisada, sem console drift não registrado.
- Dependências/containers/actions fixados por versão/digest; SAST, secret scanning, dependency review e SBOM bloqueantes conforme risco.

## Secure development

Threat model em nova fronteira, dado, integração, auth, upload, modelo ou deploy. Findings têm owner/ticket/severidade. Critical/high sem controle bloqueia merge/release; aceite segue template. Mudança de segurança exige teste negativo/regressão.

## Dados proibidos

Jira/PR/Git: secret/token/cookie, imagem privada, EXIF/GPS, dataset/peso, exploit ativo, log bruto com PII, caminho/endpoint interno sensível. Git também proíbe `.env`, chaves, dumps e artefatos grandes. Evidências usam redaction, dados sintéticos, ID opaco e storage restrito.

## Incidente

Detectar → conter → preservar evidência sanitizada → erradicar → recuperar/validar → comunicar por canal autorizado → post-mortem sem culpa. Revogar credenciais e bloquear release quando integridade do artefato/dado for incerta. Runbook KAN-144 define contatos e tempos.

## Checklist

- [ ] Upload defense-in-depth e cleanup.
- [ ] CORS/headers/rate/concurrency/timeout/memory.
- [ ] Secrets/permissions/IaC/supply chain.
- [ ] Erros/logs/redaction e dados proibidos.
- [ ] Threat model/testes/findings/gates.

## Riscos e pendências

Limites numéricos dependem de KAN-22/98/125/127; retenção de KAN-31; infraestrutura de KAN-97/83. Antimalware externo pode vazar imagem e exige aprovação.

## Referências

- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [OWASP Vulnerability Management Guide](https://owasp.org/www-project-vulnerability-management-guide/)

