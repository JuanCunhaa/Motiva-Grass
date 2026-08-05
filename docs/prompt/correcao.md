# CORRIGIR FINDINGS DO TICKET KAN-XX

Corrija os findings encontrados na revisão independente do ticket Jira `KAN-XX`.

Trabalhe exclusivamente nos problemas registrados no Pull Request e no Jira.

Não reimplemente o ticket inteiro e não amplie o escopo.

## 1. Leitura obrigatória

Antes de alterar qualquer arquivo:

1. Leia KAN-XX.
2. Leia os comentários mais recentes do Jira.
3. Leia o Pull Request relacionado.
4. Leia todos os findings da revisão.
5. Leia os comentários de revisão nos arquivos.
6. Leia os resultados da CI.
7. Leia `AGENTS.md`.
8. Leia `PROJECT_RULEBOOK.md`.
9. Leia `CONTRIBUTING.md`.
10. Leia as skills relacionadas aos findings.
11. Confira o estado atual da branch.

## 2. Classificar os findings

Organize os findings em:

* `BLOCKER`;
* `HIGH`;
* `MEDIUM`;
* `LOW`;
* `SUGGESTION`.

Para cada finding, registre:

* origem;
* arquivo;
* linha;
* impacto;
* critério de aceite afetado;
* correção planejada;
* teste necessário.

Findings `SUGGESTION` não são obrigatórios, salvo quando foram explicitamente incorporados ao escopo.

## 3. Validar o escopo

Corrija somente:

* findings da revisão;
* regressões causadas pela correção;
* documentação diretamente afetada;
* testes necessários para comprovar a correção.

Não:

* adicione funcionalidades;
* faça refatoração ampla;
* altere arquitetura sem necessidade;
* mude critérios de aceite;
* altere dependências;
* inicie outro ticket;
* reutilize a branch para outra tarefa.

Quando um finding exigir trabalho fora do escopo:

1. abra um ticket separado;
2. relacione-o ao ticket atual;
3. informe se ele bloqueia ou não a conclusão.

## 4. Atualização do Jira

Confirme que KAN-XX está em `Em andamento`.

Caso esteja em `Em análise`, mova para `Em andamento` quando a transição estiver disponível.

Adicione um comentário curto contendo:

* findings que serão corrigidos;
* abordagem;
* testes que serão reexecutados;
* possíveis riscos.

Não aplique `Flagged = Impediment` apenas porque houve reprovação na revisão.

Flagged deve ser usado somente quando existir bloqueio real externo.

## 5. Implementação das correções

Para cada finding:

1. reproduza o problema quando aplicável;
2. implemente a menor correção segura;
3. adicione ou atualize teste de regressão;
4. execute o teste específico;
5. confirme que o finding foi realmente resolvido;
6. preserve compatibilidade;
7. atualize documentação quando necessário.

Não masque o problema por meio de:

* `continue-on-error`;
* `|| true`;
* remoção de assertions;
* exclusão de testes;
* aumento arbitrário de timeout;
* captura silenciosa de exceções;
* valores hardcoded;
* desativação de regras de lint;
* alteração artificial de métricas.

## 6. Validação completa

Depois das correções, execute novamente:

* lint;
* formatação;
* typecheck;
* testes diretamente relacionados;
* suíte de regressão aplicável;
* testes de integração;
* testes de contrato;
* E2E quando aplicável;
* testes de segurança quando aplicável;
* build;
* smoke test.

Compare os resultados com os findings originais.

Crie uma tabela:

| Finding | Correção | Teste | Resultado |
| ------- | -------- | ----- | --------- |

## 7. Commit e Pull Request

Faça commits na mesma branch do ticket.

Utilize Conventional Commits e mencione `KAN-XX`.

Exemplo:

```text
fix(api): validate real MIME before decoding [KAN-XX]
```

Faça push e atualize o Pull Request existente.

Não abra outro Pull Request para o mesmo ciclo de correção, salvo quando a branch original estiver indisponível ou tecnicamente inválida.

## 8. Responder aos findings

Para cada comentário de revisão:

* informe a correção aplicada;
* indique o commit;
* informe o teste executado;
* não marque como resolvido antes de a correção estar disponível na branch.

## 9. Atualização final do Jira

Adicione um comentário contendo:

* findings corrigidos;
* commits;
* testes reexecutados;
* resultados;
* documentação atualizada;
* findings ainda pendentes;
* riscos residuais.

Mova KAN-XX novamente para `Em análise`.

Não mova para `Concluído`.

## 10. Resposta final

Apresente:

* ticket;
* Pull Request;
* findings recebidos;
* findings corrigidos;
* findings pendentes;
* commits;
* arquivos alterados;
* testes executados;
* resultados;
* status do Jira;
* decisão:

  * `READY_FOR_RE_REVIEW`;
  * `PARTIAL`;
  * `BLOCKED`.

Não execute outro ticket.
