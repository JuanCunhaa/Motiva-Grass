# Quality Gates

Status: **Proposed**. Gates são cumulativos; “não aplicável” exige justificativa.

## Gates por estágio

| Estágio | Bloqueadores mínimos |
|---|---|
| local/pre-commit | format/lint básico, secret/arquivo proibido, testes focados |
| Pull Request | build, types, unit/component, contract, arquitetura, docs/links, SAST/secrets/deps aplicáveis, diff coverage, smoke CPU |
| Em análise | PR completo, evidências, a11y/visual/segurança/dados/ML por risco, documentação e aceite |
| merge/main | revisão/CODEOWNERS, checks obrigatórios e branch atualizada |
| release candidate | E2E, segurança, privacidade, a11y, performance/capacidade, SBOM, Data/Model Cards, smoke/rollback |
| produção | gate humano, candidata imutável, checksums, config/secrets, rollback e monitoramento |

## Regras por alteração

- Contrato: schema/golden/generation + web/API/model consumers.
- Upload/security: casos maliciosos, recursos, redaction e threat model.
- UI: component/E2E, visual e WCAG.
- Dados: schema/checksum/dedup/split/leakage/Data Card.
- ML: unit/dry-run/metrics/calibration/OOD/equivalence/Model Card; sem test tuning.
- Infra: validate/plan/policy/smoke/rollback sem secret.
- Docs: Markdown/link/anchor/exemplo.

Se check obrigatório não puder executar, o gate falha ou fica explicitamente pendente; nunca verde. Critical security/privacy, perda/corrupção, leakage, modelo incompatível, test set violado, regressão de aceite ou a11y crítica bloqueiam release.

## Exceções

Aceite formal registra risco, escopo, evidência, mitigação, owner, expiração e aprovador. Não se aceita risco crítico sem controle e autoridade. Check instável não é desativado silenciosamente; quarantine exige Bug e substituto temporário.

## Checklist

- [ ] Gates aplicáveis selecionados por path/risco.
- [ ] Sem skips, retries ou N/A silenciosos.
- [ ] Evidência e exceção rastreáveis.
- [ ] Artefato avaliado é o candidato/release.

## Riscos e pendências

Paths incorretos geram verde falso; KAN-80/134 devem testar a matriz. Metas finais vêm de KAN-23/87.

