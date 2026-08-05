# RETOMAR TICKET BLOQUEADO KAN-XX

Retome a execução do ticket Jira `KAN-XX`, anteriormente classificado como `BLOCKED`.

Não presuma que o bloqueio foi realmente resolvido. Verifique as evidências antes de continuar.

## 1. Leitura obrigatória

Leia:

1. KAN-XX.
2. O Épico pai.
3. KAN-20.
4. Dependências.
5. Links `Blocks`.
6. Comentário de bloqueio.
7. Comentários adicionados após o bloqueio.
8. Evidências do desbloqueio.
9. `AGENTS.md`.
10. Documentação relevante.
11. Branch e Pull Request existentes.
12. Estado atual do repositório.
13. Skills do bloco `MOTIVA-SKILLS`.

## 2. Confirmar o motivo original

Registre:

* motivo do bloqueio;
* data do bloqueio;
* ação esperada;
* pessoa, sistema ou ticket responsável;
* trabalho preparatório realizado;
* estado atual.

## 3. Validar o desbloqueio

Confirme por evidência real:

* dependência concluída;
* acesso concedido;
* licença aprovada;
* credencial fornecida de forma segura;
* coleta realizada;
* medição registrada;
* recurso autorizado;
* ambiente disponível;
* decisão humana documentada.

Não aceite como evidência apenas:

* mensagem dizendo “já foi”;
* arquivo vazio;
* dado sem origem;
* screenshot sem contexto;
* credencial colocada no Jira;
* resultado não verificável;
* ticket dependente ainda aberto sem dispensa formal.

## 4. Bloqueio não resolvido

Caso o bloqueio continue:

1. mantenha o ticket fora de `Em andamento`;
2. mantenha `Flagged = Impediment`;
3. atualize o comentário com o estado atual;
4. informe o que ainda falta;
5. não repita trabalho preparatório já concluído;
6. finalize com `STILL_BLOCKED`.

## 5. Bloqueio resolvido

Quando houver comprovação:

1. remova `Flagged = Impediment`;
2. registre um comentário de desbloqueio;
3. informe a evidência recebida;
4. informe os riscos restantes;
5. mova o ticket para `Em andamento`;
6. reutilize a branch original quando ela continuar válida;
7. atualize a branch com a principal;
8. resolva conflitos cuidadosamente;
9. retome a partir do último ponto comprovado.

Não recomece a implementação do zero.

## 6. Reavaliar o ticket

Como o tempo ou as dependências podem ter mudado, confirme novamente:

* Definition of Ready;
* critérios de aceite;
* arquitetura;
* contratos;
* skills;
* documentação;
* riscos;
* testes;
* implementação parcial existente.

Quando o desbloqueio alterar materialmente o escopo, registre a mudança antes de continuar.

## 7. Continuação da implementação

Siga todas as regras do prompt oficial de execução de ticket.

Preserve:

* escopo;
* branch;
* rastreabilidade;
* testes;
* documentação;
* segurança;
* gates.

Quando o ticket ficar pronto, abra ou atualize o Pull Request e mova para `Em análise`.

Não mova diretamente para `Concluído`.

## 8. Resposta final

Apresente:

* ticket;
* bloqueio original;
* evidência de desbloqueio;
* Flagged removido ou mantido;
* status final no Jira;
* branch;
* Pull Request;
* trabalho retomado;
* testes;
* pendências;
* decisão:

  * `READY_FOR_REVIEW`;
  * `PARTIAL`;
  * `STILL_BLOCKED`.

Não avance para outro ticket.
