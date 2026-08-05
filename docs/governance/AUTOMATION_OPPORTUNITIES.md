# Oportunidades de automação normativa

**Status:** propostas; nenhuma automação foi implementada por este documento.

Automação aplica regras verificáveis, mas não aprova risco, licença, uso de dado, gasto, produção ou release. Para detalhes exclusivos de Jira, prevalece `JIRA_AUTOMATION_RECOMMENDATIONS.md`.

| Prioridade | Automação | Regra verificada | Resultado seguro | Tickets relacionados |
|---|---|---|---|---|
| P0 | Secret e privacy scan | nenhum segredo/dado pessoal em Git, log ou fixture | bloquear PR e orientar canal privado | KAN-31, KAN-73, KAN-86, KAN-136–138 |
| P0 | Proteção de branch e quality gates | checks obrigatórios e revisão antes de merge | bloquear merge | KAN-19, KAN-74, KAN-85–88 |
| P0 | Validador Jira/branch/PR/commit | `KAN-N` consistente e ticket único | falhar check com correção sugerida | KAN-20–23, KAN-80–82 |
| P0 | Validação de upload | formato real, tamanho, limites e conteúdo perigoso | rejeitar com erro seguro | KAN-125–126, KAN-133, KAN-147 |
| P1 | Lint documental | links, headings, arquivo no índice e duplicação simples | bloquear documento órfão/quebrado | KAN-19, KAN-79, KAN-88, KAN-144 |
| P1 | Acessibilidade e regressão visual | axe, contraste, teclado e snapshots aprovados | bloquear regressão; revisão visual humana | KAN-75, KAN-132, KAN-146, KAN-148 |
| P1 | Política de dependências | lockfile, licença, SCA e versão suportada | bloquear vulnerabilidade/licença não aceita | KAN-73, KAN-86, KAN-127 |
| P1 | Contratos e schemas | exemplos, compatibilidade e versionamento | bloquear quebra incompatível não declarada | KAN-79, KAN-125, KAN-144 |
| P1 | Manifesto de dataset | schema, checksum, proveniência e separação de splits | bloquear dataset incompleto ou leak detectável | KAN-31, KAN-120–122, KAN-139 |
| P1 | Validador de experimento/modelo | run metadata, métricas completas, Cards e checksum | impedir promoção, nunca escolher modelo sozinho | KAN-66, KAN-69, KAN-120–122, KAN-139–140, KAN-156 |
| P1 | Bundle de evidências | agrega checks, ambiente, artefatos e links | publicar síntese no PR/Jira | KAN-20, KAN-88, KAN-143, KAN-151 |
| P2 | Hygiene do backlog | pai, labels, dependências, bloqueios e itens sem owner | sinalizar; não reordenar silenciosamente | KAN-20–23, KAN-80–84 |
| P2 | Monitoramento de flakiness | taxa por teste e quarentena com expiração | abrir/atualizar item rastreável | KAN-87, KAN-134–135, KAN-145 |
| P2 | Verificação de drift/rollback | distribuição, latência, falha e prontidão do fallback | alertar ou acionar fallback previamente aprovado | KAN-140–142, KAN-151–152 |

## Ordem recomendada

1. scanners e proteções P0;
2. checks determinísticos já executáveis em CPU;
3. evidência e higiene de documentação;
4. GPU, regressão visual e monitoramento com orçamento/aprovação;
5. automações de produção somente após threat model, runbook, rollback e gate humano.

## Critérios para automatizar

Cada regra deve ter owner, entrada, saída, falso-positivo conhecido, modo de falha, observabilidade, teste e rollback. Se o sistema externo estiver indisponível, a automação não fabrica sucesso: bloqueia apenas quando o risco justificar fail-closed ou registra inconclusivo conforme a norma especializada.
