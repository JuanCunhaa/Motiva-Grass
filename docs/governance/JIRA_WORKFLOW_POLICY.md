# Política de Workflow do Jira

## Objetivo

Definir critérios objetivos para estados, transições, comentários e bloqueios no workflow atual do projeto KAN.

## Escopo

Aplica-se ao fluxo `Tarefas pendentes → Em andamento → Em análise → Concluído`. Enquanto KAN-89 não alterar administrativamente o workflow, bloqueios são representados por `Flagged = Impediment`, labels e comentários, e não por um status fictício.

## Regras obrigatórias

### Tarefas pendentes

É o estado obrigatório quando o trabalho ainda não começou, a DoR falha, há dependência bloqueadora, gate ativo, falta acesso/dado, há conflito de escopo ou o item aguarda responsável. Um artefato parcial já criado não justifica `Em andamento` se não existir atividade útil atual.

Ao detectar falta de prontidão, o executor deve comentar as lacunas concretas, aplicar impedimento se o bloqueio estiver ativo e indicar quem ou o que desbloqueia. Não deve preencher informações por suposição.

### Transição para Em andamento

Todos os critérios devem ser verdadeiros:

- DoR aprovada pela checklist do executor;
- dependências críticas concluídas ou formalmente dispensadas;
- ticket não duplicado nem executado por outra pessoa/agente;
- executor e modelo identificados;
- gate humano não ativo;
- dados, acessos e fixtures disponíveis;
- branch criada para alteração versionada;
- comentário de início registrado;
- atividade real iniciada imediatamente.

Ordem operacional: validar → criar branch → comentar início → transicionar → executar. O intervalo entre transição e atividade deve ser mínimo. Reserva preventiva de ticket é proibida.

### Permanência em Em andamento

O status exige atividade real. O executor registra progresso apenas em eventos materiais. Se um bloqueio eliminar todo o trabalho útil, registra bloqueio e devolve a `Tarefas pendentes`. Se uma parte independente ainda puder avançar, pode permanecer, desde que o comentário delimite a parte ativa e a bloqueada.

Troca de executor exige handoff no Jira com estado do trabalho, branch, último commit, testes, riscos e próximo passo.

### Transição para Em análise

Todos os critérios devem ser verdadeiros:

- escopo implementado ou decisão/documento final produzido;
- testes aplicáveis executados e resultados registrados;
- teste não aplicável explicitamente justificado;
- evidências acessíveis e reais;
- PR exclusivo aberto quando houver mudança versionada;
- documentação oficial atualizada;
- critérios de aceite verificados um a um pelo executor;
- riscos, limitações e Bugs relacionados registrados;
- comentário de envio para análise publicado.

Falha de check, PR ausente, documentação pendente ou teste obrigatório não executado impede a transição.

### Retorno de Em análise para Em andamento

Usar quando a revisão exigir mudança de código, documentação, evidência ou teste. O revisor registra cada motivo de retorno. O executor comenta a retomada, implementa as correções e publica novo resumo de análise. Dúvida do revisor que não exige alteração não muda o status.

### Transição para Concluído

Todos os critérios devem ser verdadeiros:

- PR revisado e aprovado, quando aplicável;
- checks obrigatórios aprovados;
- entrega corresponde ao escopo do Jira;
- todos os critérios de aceite têm evidência;
- documentação oficial atualizada;
- segurança, acessibilidade, dados e ML revisados quando aplicável;
- nenhum Bug crítico bloqueador aberto;
- branch, PR, merge commit, documentos e release relacionados no Jira;
- comentário de conclusão publicado;
- DoD integralmente satisfeita.

Resultado parcial, bloqueio ativo ou aceite flexibilizado sem decisão formal impede `Concluído`. `NO-GO` pode ser uma conclusão válida somente quando o objetivo do ticket era produzir uma decisão e os critérios exigiam essa possibilidade.

### Reabertura

Reabrir para `Em andamento` quando a conclusão estiver materialmente incorreta e a correção pertencer ao mesmo escopo/entrega ainda não aceita. Abrir Bug quando houver defeito pós-conclusão que mereça triagem, regressão e prioridade próprias. Registrar o motivo e preservar a evidência histórica.

## Política de bloqueio

Um gate vira impedimento ativo somente quando sua ação é necessária para o próximo passo ou para validar o resultado atual. Gate futuro não deve bloquear trabalho técnico anterior.

Enquanto ativo:

- aplicar `Flagged = Impediment`;
- aplicar label de causa;
- registrar comentário de bloqueio;
- deixar fora de `Em andamento`, exceto com trabalho parcial legítimo;
- remover `Flagged` apenas após evidência do desbloqueio;
- comentar a retomada e revalidar a DoR.

## Regras recomendadas

- Configurar WIP de acordo com a capacidade real e alertar tickets sem atividade.
- Medir lead time sem transformar comentários em apontamento excessivo.
- Usar automações como validação e lembrete, não como prova de aceite.
- Exibir no card tipo, pai, prioridade operacional, responsável, labels e Flagged.

## Exemplos corretos

- KAN-99 permanece pendente e impedida até existirem impressão e medição reais; o protocolo preparatório pode avançar em ticket próprio.
- Um PR completo é enviado a `Em análise`; após pedido de correção, o ticket volta a `Em andamento` e recebe comentário objetivo.
- Um ticket de decisão pode concluir com `NO-GO` quando compara alternativas com evidência e esse resultado está previsto no aceite.

## Exemplos incorretos

- Manter ticket `Em andamento` por vários dias apenas porque alguém pretende começá-lo.
- Mover para `Em análise` com PR em rascunho sem testes obrigatórios.
- Usar `Flagged` somente porque o ticket possui label `gate-human`, embora o gate seja futuro.
- Concluir automaticamente porque o PR foi mesclado, sem validar documentação e Jira.

## Exceções

Tickets puramente administrativos sem artefato versionado podem ir a `Em análise` sem PR, desde que contenham evidência verificável e revisão identificada no Jira. Hotfix segue runbook próprio. Se o Jira ganhar estados `Pronto` ou `Bloqueado`, esta política deve ser revisada antes de usá-los; até lá, os quatro estados são os únicos normativos.

## Checklist

- [ ] O estado representa a realidade atual, não uma intenção futura.
- [ ] Toda entrada em `Em andamento` tem DoR, executor, branch aplicável e comentário.
- [ ] Todo bloqueio ativo tem Flagged, label, evidência e ação de desbloqueio.
- [ ] Toda entrada em `Em análise` tem entrega, testes, evidências, documentação e PR aplicável.
- [ ] Todo retorno da análise tem motivo explícito.
- [ ] Toda conclusão tem aprovação, checks, DoD, rastreabilidade e comentário final.

