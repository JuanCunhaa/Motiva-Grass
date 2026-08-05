# Template de Aceite de Risco

Aceite não remove risco nem substitui correção. Exige autoridade humana, prazo e rastreabilidade.

```markdown
# RA-<ID> — <Título>

- Ticket/findings: <KAN-N/CVE/ID>
- Owner do risco: <papel/pessoa>
- Aprovador autorizado: <papel/pessoa>
- Data/expiração: <ISO>/<ISO>
- Ambiente/ativos/versões: <escopo exato>

## Risco
<cenário, ameaça, vulnerabilidade e impacto>

## Evidências
<testes, exposição, CVSS/contexto e links restritos>

## Alternativas avaliadas
<corrigir, remover, isolar, adiar, NO-GO>

## Controles compensatórios
<controle, owner e teste>

## Residual e decisão
<probabilidade/impacto residual e justificativa>

## Plano de correção
<ticket, prazo e condição de reavaliação/revogação>

## Comunicação e monitoramento
<alerta, indicador, incidente e público autorizado>
```

## Regras obrigatórias

- Critical exige controle efetivo e autoridade executiva/security; não pode aceitar risco de release/artifact incerto sem contenção.
- Expiração automática; mudança de exposição/versão/incidente revoga e exige nova avaliação.
- Secret, exploit ativo, imagem/PII e evidência bruta ficam fora do Jira/Git.

## Checklist

- [ ] Escopo/owner/aprovador/expiração.
- [ ] Evidência, alternativas e controles testados.
- [ ] Residual, plano, monitoramento e revogação.

## Riscos e pendências

Matriz de autoridade e níveis aprováveis depende de KAN-31/KAN-86/KAN-152.
