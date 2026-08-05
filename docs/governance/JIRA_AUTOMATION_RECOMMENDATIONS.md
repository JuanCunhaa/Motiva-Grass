# Automações Recomendadas no Jira

## Objetivo

Reduzir erros operacionais e melhorar rastreabilidade sem automatizar julgamento de aceite ou fabricar evidências.

## Escopo

Recomendações para o projeto team-managed KAN e o workflow atual de quatro estados. Implementação depende de KAN-89 e aprovação administrativa.

## Princípios obrigatórios

- Automação pode validar, comentar, sinalizar, notificar e impedir transição quando a plataforma permitir.
- Automação não confirma teste, aceite, revisão de risco ou conclusão por inferência.
- Toda regra deve ter owner, log de auditoria, ambiente de teste, rollback/desativação e proteção contra loops.
- Não criar status `Pronto` ou `Bloqueado` sem decisão formal de workflow.

## Catálogo recomendado

| ID | Gatilho | Condições | Ações | Nível |
|---|---|---|---|---|
| AUT-01 | Transição para `Em andamento` | falta responsável, pai, prioridade operacional, área/fase/modelo, comentário de início ou branch aplicável | impedir via validator; se indisponível, retornar e comentar lacunas | Obrigatória |
| AUT-02 | Ticket permanece `Em andamento` sem atualização material | limiar configurado por equipe | notificar responsável; não transicionar automaticamente | Recomendada |
| AUT-03 | `Flagged = Impediment` adicionado | comentário de bloqueio/label `blocked-*` ausente | solicitar campos e notificar owner do desbloqueio | Obrigatória |
| AUT-04 | Impedimento removido | havia bloqueio ativo | solicitar comentário de retomada e revalidação DoR | Recomendada |
| AUT-05 | Transição para `Em análise` | PR/evidência/documentação/aceite ausentes | impedir ou retornar com checklist de lacunas | Obrigatória |
| AUT-06 | PR aberto com `[KAN-N]` | chave válida no projeto | vincular PR/branch ao ticket e comentar uma vez | Recomendada |
| AUT-07 | PR aprovado e checks verdes | ticket em `Em análise` | notificar responsável para validar DoD; não concluir | Obrigatória |
| AUT-08 | Transição para `Concluído` | DoD, comentário final, PR/merge aplicável ou Bugs críticos ausentes | impedir quando faltar dado objetivo | Obrigatória |
| AUT-09 | Bug criado | campos do template ausentes | impedir criação quando possível ou comentar checklist e marcar triagem | Obrigatória |
| AUT-10 | Dependência crítica concluída | links `Blocks` válidos | notificar tickets realmente desbloqueados; não iniciar automaticamente | Recomendada |
| AUT-11 | `gate-human` + Flagged | gate ativo | notificar papel decisor e registrar SLA/condição, sem repetir comentários | Recomendada |
| AUT-12 | Branch/PR sem chave KAN | repositório Motiva-Grass | falhar check ou solicitar correção | Obrigatória |
| AUT-13 | Label de prioridade diverge do campo oficial | ambos preenchidos | sinalizar conflito e impedir seleção automática | Transitória |
| AUT-14 | Ticket sem responsável entra em estado ativo | qualquer tipo executável | impedir transição | Obrigatória |
| AUT-15 | Release/tag criada | ausência de KAN-151/KAN-152 aprovados ou checksum | bloquear pipeline de publicação | Obrigatória |

## JQLs sugeridos

```jql
project = KAN AND status = "Em andamento" AND updated <= -2d
project = KAN AND Flagged = Impediment AND labels not in (blocked-access, blocked-data, blocked-license, blocked-admin, blocked-external)
project = KAN AND labels = gate-human AND statusCategory != Done
project = KAN AND assignee is EMPTY AND status in ("Em andamento", "Em análise")
project = KAN AND issuetype = Bug AND statusCategory != Done ORDER BY priority DESC, created ASC
project = KAN AND labels = priority-p0 AND statusCategory != Done ORDER BY Rank ASC
```

O limiar `-2d` é exemplo; deve refletir dias úteis e capacidade real.

## Regras recomendadas

- Preferir workflow validators a automações reativas para pré-condições críticas.
- Usar uma propriedade/campo de idempotência para evitar comentário duplicado.
- Criar dashboard de falhas das automações.
- Testar em ticket sandbox antes de ativar no projeto inteiro.
- Revisar regras após qualquer mudança de status, campo ou app.

## Exemplos corretos

- Checks verdes geram lembrete de DoD, mas uma pessoa/executor ainda confirma documentação e aceite.
- Falta de branch em tarefa puramente administrativa é aceita porque o campo contém justificativa N/A.

## Exemplos incorretos

- Concluir o Jira automaticamente no merge do PR.
- Marcar teste como aprovado porque existe um arquivo de teste.
- Criar comentários repetidos a cada atualização do ticket.
- Remover Flagged automaticamente por passagem de tempo.

## Exceções

Hotfix pode usar regras específicas do runbook. Projeto sem validators pode usar automação de retorno, mas deve registrar que houve transição inválida. Integrações indisponíveis devem falhar de forma visível e nunca assumir sucesso.

## Checklist de implantação

- [ ] Owner e objetivo de cada regra definidos.
- [ ] Campos e estados existem com IDs verificados.
- [ ] Condições N/A e tickets administrativos tratados.
- [ ] Idempotência, auditoria e anti-loop testados.
- [ ] Falha da integração não produz falso positivo.
- [ ] Rollback/desativação documentado.
- [ ] Regra testada em sandbox e aprovada em KAN-89.

