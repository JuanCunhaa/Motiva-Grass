# Relatório de Inconsistências do Backlog

## Objetivo

Registrar divergências encontradas na leitura de KAN-1 a KAN-156 para revisão humana, sem alterar tickets.

## Escopo e método

Snapshot somente leitura do Jira em 05/08/2026. Foram inspecionados chave, tipo, pai, descrição, status, prioridade, labels, responsável, links e, para KAN-20/KAN-89, comentários. A direção de `Blocks` foi interpretada conforme os campos estruturados `outwardIssue` (`bloqueia`) e `inwardIssue` (`é bloqueado por`) da API.

## Resumo validado

- 156 itens, sem lacunas de KAN-1 a KAN-156.
- 16 Épicos (KAN-2 a KAN-17).
- 139 tickets executáveis (KAN-18 a KAN-156).
- 139/139 executáveis com pai, descrição, label de área, fase, modelo, prioridade e documentação.
- 125 tickets com `priority-p0`, 14 com `priority-p1`, nenhum com `priority-p2`.
- 29 tickets com `gate-human`.
- 64 tickets recomendam Thinking e 75 recomendam Sol Alto.
- Todos os 156 itens estão em `Tarefas pendentes` no snapshot.
- KAN-89 é o único item com `Flagged = Impediment`.

## Inconsistências de alta prioridade

### INC-01 — 23 dependências `Blocks` provavelmente invertidas

Em cada par abaixo, o primeiro ticket lista o segundo em `Dependências`, mas o link estruturado indica que o primeiro **bloqueia** o segundo. A intenção textual exige o inverso:

```text
KAN-20  depende de KAN-89
KAN-40  depende de KAN-44, KAN-106
KAN-50  depende de KAN-66
KAN-51  depende de KAN-66
KAN-52  depende de KAN-66
KAN-53  depende de KAN-66
KAN-66  depende de KAN-155
KAN-71  depende de KAN-69
KAN-75  depende de KAN-70
KAN-77  depende de KAN-70
KAN-84  depende de KAN-89, KAN-35
KAN-85  depende de KAN-143
KAN-101 depende de KAN-40
KAN-102 depende de KAN-101
KAN-139 depende de KAN-69
KAN-142 depende de KAN-140
KAN-151 depende de KAN-88
KAN-152 depende de KAN-151
KAN-153 depende de KAN-102
KAN-154 depende de KAN-153
KAN-155 depende de KAN-154
```

Impacto: seleção automática e visualização de caminho crítico podem liberar o ticket errado. Ação: revisar par a par na UI, preservar a dependência textual aprovada e inverter o link onde confirmada.

### INC-02 — Duas fontes de prioridade divergem

Todos os itens possuem prioridade nativa Jira `Medium`, enquanto 125 executáveis têm label P0 e 14 têm P1. KAN-1 manda priorizar as labels. Impacto: ordenação nativa, dashboards e automações podem contradizer o roadmap. Ação: escolher uma fonte oficial e migrar; recomenda-se campo estruturado P0/P1/P2 ou mapear para prioridade nativa.

### INC-03 — Todos os tickets executáveis estão sem responsável

139/139 executáveis têm `Assignee = vazio`. Isso é aceitável no backlog, mas impede identificar execução concorrente e viola a DoR no momento do início. Ação: validator deve exigir responsável antes de `Em andamento`, sem atribuir antecipadamente todo o backlog.

### INC-04 — Conflito sobre fonte documental

- KAN-20 diz que Confluence será a fonte oficial quando provisionado.
- KAN-89 exige uma página de execução por ticket no Confluence.
- A política solicitada define o repositório Git como fonte oficial técnica.

Impacto: duas versões normativas de ADRs, schemas, Data/Model Cards e runbooks. Recomendação: Jira para gestão, Git para documentação técnica normativa, PR para mudança/evidência e Confluence como catálogo/publicação com links, sem cópia normativa divergente.

### INC-05 — Conflito sobre workflow desejado

- KAN-1 afirma que KAN-89 concentra recomendação de adicionar `Pronto` e `Aguardando ação humana/Bloqueado`.
- A descrição atual de KAN-89 recomenda manter quatro estados e usar Flagged/labels.
- O comentário 10024 de KAN-89 recomenda seis estados, incluindo `Pronto` e `Bloqueado`.

Impacto: automações e políticas podem mirar estados inexistentes ou redundantes. Recomendação: manter os quatro estados atuais até decisão administrativa formal; então atualizar KAN-1, KAN-20, KAN-89 e estes documentos na mesma mudança.

## Inconsistências médias

### INC-06 — Deriva do template de descrição em 15 tickets

Comparando com os títulos de seção padronizados usados no restante do backlog:

- KAN-18, KAN-19 e KAN-21 a KAN-27 não têm seções `Testes` e `Documentação` com esses nomes.
- KAN-20 não tem seções explícitas `Escopo`, `Entregáveis`, `Testes` e `Modelo recomendado`, embora parte do conteúdo exista em outras seções.
- KAN-76, KAN-78, KAN-129 e KAN-131 não têm seção `Objetivo` explícita.
- KAN-89 não tem seção `Escopo` explícita.

Impacto: parsers/validators por heading falham e a DoR fica menos objetiva. Ação: normalizar headings preservando conteúdo e histórico.

### INC-07 — Gates condicionais e label não estão totalmente alinhados

Casos para decisão:

- KAN-24 e KAN-25 descrevem gate obrigatório se licença ficar ambígua, mas não têm `gate-human`.
- KAN-85 admite possível apoio humano em dispositivos físicos, sem label.
- KAN-100 tem `gate-human`, mas a seção diz apenas que validação de campo é recomendada.
- KAN-23 e KAN-66 mencionam aprovação recomendada, corretamente não necessariamente ativa.

Recomendação: label somente quando a necessidade humana fizer parte real do ticket; usar estado do gate `Futuro/Ativo` e Flagged apenas quando bloquear o próximo passo.

### INC-08 — Muitas dependências textuais críticas sem link estruturado

Há 14 tickets com cinco ou mais dependências textuais e nenhum `Blocks`: KAN-39, KAN-41, KAN-43, KAN-47, KAN-54, KAN-60, KAN-61, KAN-62, KAN-65, KAN-74, KAN-86, KAN-123, KAN-147 e KAN-148.

Nem toda referência deve virar link. Porém, KAN-20 exige `Blocks` para caminho crítico. Ação: classificar quais dependências são bloqueadoras e criar somente esses links, na direção correta.

## Regras obrigatórias para correção

- Corrigir somente após revisão humana; este relatório não autoriza edição em massa.
- Exportar os links/campos antes da migração.
- Não derivar direção de dependência apenas do número do ticket.
- Atualizar texto e link na mesma operação lógica.
- Testar JQLs, automações e ordem do roadmap depois das correções.

## Regras recomendadas

- Tratar INC-01, INC-02, INC-04 e INC-05 antes de automatizar seleção/transições.
- Fazer correções em lotes pequenos com amostra validada.
- Reexecutar auditoria e anexar contagens ao KAN-20/KAN-89.

## Exemplos corretos

- Confirmar que KAN-66 bloqueia KAN-50 e então inverter o link, mantendo KAN-50 dependente de KAN-66.
- Migrar prioridade após comparar 125 P0/14 P1 com a ordem de KAN-1 e atualizar filtros.

## Exemplos incorretos

- Inverter todos os links sem inspeção visual e backup.
- Criar `Pronto`/`Bloqueado` apenas porque aparecem em comentário antigo.
- Remover labels de prioridade antes de popular o campo substituto.

## Exceções

Dependência textual pode permanecer sem `Blocks` quando for somente referência auxiliar. Ticket pode permanecer sem responsável enquanto pendente. Gate condicional pode ficar sem label até tornar-se uma necessidade real, desde que a descrição indique o ponto de decisão.

## Checklist de revisão

- [ ] 23 pares `Blocks` revisados e direção confirmada.
- [ ] Fonte única de prioridade decidida e migração planejada.
- [ ] Validator de responsável antes de estado ativo definido.
- [ ] Papel de Git versus Confluence decidido.
- [ ] Workflow de quatro versus seis estados decidido.
- [ ] 15 descrições normalizadas sem perda de conteúdo.
- [ ] Gates condicionais revisados.
- [ ] Dependências críticas textuais classificadas.
- [ ] Auditoria repetida após mudanças.

