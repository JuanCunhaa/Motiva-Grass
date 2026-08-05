# Padrão de Evidências de Teste

Status: **Proposed**. Evidência prova o que executou; não é declaração genérica.

## No Pull Request

Registrar comando/caso, commit, ambiente/runtime, dados/fixture e versão, seed quando aplicável, resultado, duração/amostra, link ao log/artefato estável e testes não executados. Screenshots ocultam imagem/PII e mostram viewport/browser. ML inclui dataset/split/model checksum, configuração e métricas completas; performance inclui hardware, concorrência, warmup e distribuição.

## No Jira

Resumo por critério de aceite, PR/checks, resultado final, falhas/Bugs, limitações, riscos e links — sem duplicar logs extensos. Evidência privada fica no storage autorizado com acesso/retenção, nunca anexada ao Jira.

## Padrão mínimo

```markdown
| Validação | Versão/ambiente | Dados | Resultado | Evidência |
|---|---|---|---|---|
| `<comando/caso>` | `<commit/runtime>` | `<fixture/dataset+checksum>` | `<pass/fail/not run>` | `<link>` |
```

`pass`, `fail`, `not run`, `blocked` e `not applicable` são distintos. `Not run` informa motivo, risco e condição de execução. Log/screenshot é sanitizado; nunca inventar, editar para esconder falha ou selecionar apenas a melhor execução.

## Retenção e integridade

Checks de release, segurança, ML e performance seguem retenção da release; PR comum segue política do CI. Artefatos incluem timestamp, commit e checksum quando crítico. Link efêmero/pessoal não é evidência final.

## Checklist

- [ ] Comando/caso, commit, ambiente, dado/seed e resultado.
- [ ] Evidência acessível, íntegra e sanitizada.
- [ ] Falhas/not-run/limitações visíveis.
- [ ] Jira resume por aceite; PR contém detalhe.

## Riscos e pendências

Retenção/sink dependem de KAN-31/135/151. Excesso de evidência pode vazar dados; aplicar minimização.

