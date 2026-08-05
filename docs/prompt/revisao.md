# REVISAR E FINALIZAR TICKET KAN-XX

Atue como revisor independente do ticket Jira `KAN-XX` do projeto Motiva-Grass.

Esta é uma revisão sem confiança no executor anterior. Não presuma que código, comentários, testes ou status estão corretos.

Sua função é auditar a entrega, executar novamente as validações críticas e somente concluir o ticket quando todas as evidências forem reais.

## 1. Leitura obrigatória

Leia:

1. KAN-1.
2. KAN-20.
3. O Épico pai.
4. A descrição completa de KAN-XX.
5. As dependências.
6. Os links `Blocks`.
7. O bloco `MOTIVA-SKILLS`.
8. Os comentários do ticket.
9. `AGENTS.md`.
10. `PROJECT_RULEBOOK.md`.
11. `CONTRIBUTING.md`.
12. A documentação relevante.
13. A matriz `config/skills/jira-skill-routing.yaml`.
14. O Pull Request relacionado.
15. Todos os commits.
16. O diff completo.
17. Os resultados da CI.
18. Os Bugs relacionados.

Não peça que eu forneça manualmente esses conteúdos. Consulte Jira e repositório.

## 2. Confirmar rastreabilidade

Valide:

```text
Jira → branch → commits → Pull Request → testes → documentação → resultado
```

Confirme:

* branch exclusiva;
* commits mencionando KAN-XX;
* PR relacionado;
* escopo correspondente ao ticket;
* nenhuma entrega escondida;
* nenhuma alteração relevante fora do escopo;
* documentação atualizada;
* evidências sanitizadas.

Quando faltar rastreabilidade, não conclua o ticket.

## 3. Revisão técnica independente

Revise:

* critérios de aceite um por um;
* arquitetura;
* estrutura de pastas;
* qualidade do código;
* tipagem;
* tratamento de erros;
* logs;
* segurança;
* privacidade;
* acessibilidade;
* performance;
* testes;
* dependências;
* compatibilidade;
* dados;
* unidades;
* geometria;
* ML;
* documentação;
* rollback.

Considere somente as áreas aplicáveis ao ticket.

Use as skills de revisão, segurança, qualidade e domínio indicadas no bloco `MOTIVA-SKILLS`.

Não use skills irrelevantes.

## 4. Executar validações novamente

Não confie apenas no relatório do executor.

Execute novamente, quando aplicável:

* lint;
* formatação;
* typecheck;
* testes unitários;
* testes de integração;
* testes de contrato;
* E2E;
* testes de segurança;
* build;
* smoke test;
* verificação de links;
* validação de schemas;
* validação de manifests;
* avaliação de ML com protocolo correto.

Compare os resultados com os que foram registrados no Jira e no PR.

## 5. Procurar verde falso

Verifique especificamente:

* `continue-on-error`;
* testes ignorados;
* asserts removidos;
* mocks substituindo integração real;
* comandos terminando com `|| true`;
* exceções silenciosamente capturadas;
* cobertura artificial;
* fixtures apresentadas como dados reais;
* métricas sem artefato;
* valores hardcoded;
* checks não obrigatórios;
* resultados manuais sem evidência;
* documentação declarando funcionalidade inexistente.

Qualquer verde falso deve ser classificado como `BLOCKER`.

## 6. Classificação dos findings

Classifique cada finding como:

* `BLOCKER`;
* `HIGH`;
* `MEDIUM`;
* `LOW`;
* `SUGGESTION`.

Para cada finding, informe:

* arquivo e linha;
* problema;
* impacto;
* evidência;
* correção esperada;
* critério de aceite afetado.

## 7. Quando houver BLOCKER ou HIGH

Se existir `BLOCKER` ou `HIGH` não resolvido:

1. não aprove o PR;
2. não faça merge;
3. registre findings no PR;
4. adicione comentário no Jira;
5. mova KAN-XX para `Em andamento`, quando possível;
6. mantenha em `Em análise` com comentário bloqueador quando a transição inversa não estiver disponível;
7. aplique `Flagged = Impediment` somente se houver bloqueio real;
8. retorne `CHANGES_REQUIRED`.

Não conclua o ticket.

## 8. Correções pequenas

Findings `LOW`, ajustes de documentação, pequenos problemas de lint ou correções mecânicas podem ser corrigidos diretamente na branch do ticket quando:

* não alterarem a arquitetura;
* não ampliarem o escopo;
* não modificarem critérios de aceite;
* não exigirem decisão humana.

Depois da correção:

* execute novamente os testes;
* registre o commit;
* atualize o PR;
* registre no Jira.

Problemas maiores devem voltar ao fluxo de implementação.

## 9. Aprovação

Só aprove quando:

* todos os critérios estiverem comprovados;
* todos os checks obrigatórios estiverem verdes;
* não houver `BLOCKER` ou `HIGH`;
* documentação estiver atualizada;
* riscos estiverem registrados;
* não houver gate humano pendente;
* o PR representar exatamente o ticket.

Quando aprovado e ainda não mergeado:

1. aprove o PR;
2. registre a aprovação no Jira;
3. mantenha o ticket em `Em análise`;
4. retorne `READY_TO_MERGE`.

Não faça merge automático quando as regras do repositório exigirem merge humano.

## 10. Conclusão após merge

Se o PR estiver aprovado e mergeado:

1. confirme o commit de merge na branch principal;
2. confirme que o código auditado é o código mergeado;
3. execute ou valide smoke test pós-merge;
4. confirme documentação;
5. confirme ausência de gate pendente;
6. confirme ausência de Bug crítico;
7. remova `Flagged = Impediment` quando não houver bloqueio;
8. adicione comentário final no Jira;
9. mova KAN-XX para `Concluído`.

O comentário final deve conter:

* PR;
* commit de merge;
* testes;
* evidências;
* critérios de aceite;
* documentação;
* Bugs;
* riscos residuais;
* skills utilizadas;
* resultado final.

## 11. Ticket já implementado sem Jira atualizado

Quando o código estiver comprovadamente implementado e mergeado, mas o Jira estiver desatualizado:

1. valide todos os critérios;
2. encontre commits e PRs reais;
3. execute testes;
4. registre as evidências;
5. classifique como `IMPLEMENTED_UNTRACKED`;
6. reconcilie o Jira;
7. conclua somente após a auditoria completa.

Não conclua apenas porque arquivos semelhantes existem.

## 12. Resposta final obrigatória

Apresente:

* ticket revisado;
* PR;
* commits;
* findings;
* testes reexecutados;
* resultados;
* critérios de aceite;
* documentação;
* status do PR;
* status do Jira;
* riscos residuais;
* decisão:

  * `CHANGES_REQUIRED`;
  * `READY_TO_MERGE`;
  * `COMPLETED`;
  * `BLOCKED`.

Não selecione nem execute o próximo ticket.
