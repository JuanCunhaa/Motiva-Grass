# Testes de Segurança

Status: **Proposed**. Testes seguros, reproduzíveis e ligados ao threat model.

## Matriz mínima

| Área | PR | Scheduled/release |
|---|---|---|
| upload | extensão dupla, MIME falso, signature inválida, truncado, pixels/ratio/size | corpus malformado, decompression/decoder, soak/memória |
| API | validação, erro/redaction, timeout/cancel, CORS/headers | rate/concurrency/DoS controlado, DAST autorizado |
| web | CSP/config pública, XSS encoding, storage de imagem | browser matrix, privacy audit |
| secrets/supply chain | secret scan, SAST, dependency review, action pin | full scan, license, SBOM e container/IaC |
| ML/artifact | checksum/manifest, safe loader, incompatibilidade | adversarial/OOD autorizado, registry/promotion/rollback |
| infra | IaC validate/policy/least privilege | staging review, network/secrets/rollback |

Payloads são sintéticos/inertes; malware/exploit real somente em laboratório isolado e autorizado, nunca Git/Jira. Fuzzers têm budgets e não atacam terceiros/produção. Finding preserva request ID, versão e passo minimizado sanitizado.

## Gates

Critical/high reproduzível sem mitigação bloqueia PR/release. Scanner indisponível é `not run`, não pass. Falso positivo exige triagem, justificativa e expiração. Correção inclui regressão; reteste independente em critical.

## Checklist

- [ ] Threat/model/risco mapeados a testes.
- [ ] Payload/evidência seguros e sanitizados.
- [ ] PR/scheduled/manual definidos; sem verde falso.
- [ ] Finding, owner, regressão e reteste.

## Riscos e pendências

Ferramentas SAST/DAST/fuzz dependem de KAN-137/86; ambientes autorizados de KAN-83/97.

