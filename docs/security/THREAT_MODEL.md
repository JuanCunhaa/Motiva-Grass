# Threat Model do Motiva-Grass

Status: **Draft/Proposed** para KAN-31. Deve ser atualizado com arquitetura/deploy reais.

## Escopo, ativos e fronteiras

Ativos: imagem/EXIF, consentimento, contratos, datasets/splits, pesos, registry, secrets, serviço/API, resultados, logs e release. Atores: usuário, operador, desenvolvedor, revisor, terceiro e atacante. Fronteiras: browser→API, API→temp/runtime, runtime→registry/storage, CI→registries/cloud, coleta→storage, promoção→produção.

## Ameaças e controles

| ID | Ameaça | Impacto | Controles/validação | Residual/owner |
|---|---|---|---|---|
| T01 | upload falso/malformado/bomb | RCE/DoS | allowlist, magic+decode, pixel/resource limits, sandbox, tests | Backend/Security |
| T02 | EXIF/GPS/nome vazado | privacidade | strip, minimização, redaction, audit KAN-147 | Privacy |
| T03 | temporário/backup retido | disclosure | isolated temp, cleanup finally, TTL/restore tests | Backend/Platform |
| T04 | abuso/rate/concurrency | indisponibilidade/custo | rate, queue, budgets, timeout, monitor | SRE |
| T05 | secret/supply-chain comprometido | takeover | scanners, pin/digest, least privilege, SBOM | DevSecOps |
| T06 | peso/dataset adulterado | resultado falso | checksum, provenance, signed candidate, access | MLOps/Data |
| T07 | taxonomia/API incompatível | resultado enganoso | manifest compatibility, startup/readiness fail | ML/Backend |
| T08 | leakage/test tuning | métrica falsa | group splits, frozen test ACL/audit | ML Validation |
| T09 | log/predição sensível | disclosure | schema allowlist/redaction/retention | Security/Privacy |
| T10 | fallback silencioso/OOD | confiança artificial | explicit capability/warning/inconclusive | Product/ML |
| T11 | promoção diferente do avaliado | release inválida | immutable artifact/checksum/gate/rollback | MLOps/Release |
| T12 | IaC/CORS/header/permissão errada | exposição | policy tests, staging review, least privilege | Platform/Security |

## Método e risco

Usar STRIDE por fronteira e privacy harms para dados; classificar probabilidade × impacto, ajustando exposição/controles. Critical sem mitigação → NO-GO. Revisar em mudança de fluxo, dado, terceiro, modelo, infra, incidente ou release.

## Checklist

- [ ] Diagrama/ativos/atores/fronteiras atuais.
- [ ] Ameaças, controles, testes, owner e residual.
- [ ] Tickets e gates relacionados.
- [ ] Revisão de security/privacy/data/ML.

## Riscos e pendências

Autenticação, cloud, storage, registry e retenção ainda não decididos; não aceitar este draft como validação final.

