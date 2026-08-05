# EXECUTAR TICKET KAN-XX

Execute integralmente o ticket Jira `KAN-XX` do projeto Motiva-Grass.

Trabalhe exclusivamente nesse ticket. Não avance automaticamente para outro ticket ao finalizar.

Você possui acesso ao repositório e deve utilizar o Jira como fonte de gestão e o repositório como fonte técnica.

## 1. Carregamento inicial obrigatório

Antes de alterar código ou Jira:

1. Leia KAN-1.
2. Leia KAN-20.
3. Leia o Épico pai de KAN-XX.
4. Leia completamente KAN-XX.
5. Leia todas as dependências indicadas.
6. Verifique links `Blocks`.
7. Verifique status das dependências.
8. Verifique `Flagged = Impediment`.
9. Verifique a presença de `gate-human`.
10. Leia o bloco `MOTIVA-SKILLS`.
11. Leia `AGENTS.md`.
12. Leia `PROJECT_RULEBOOK.md`.
13. Leia `CONTRIBUTING.md`.
14. Leia a documentação relevante em `docs/`.
15. Leia `config/skills/jira-skill-routing.yaml`.
16. Leia o `SKILL.md` das skills obrigatórias.

Não peça para que eu copie a descrição do ticket. Consulte o Jira diretamente.

## 2. Conferir o estado atual do repositório

Antes de iniciar uma nova implementação:

1. Analise a branch principal.
2. Pesquise arquivos, módulos, testes e documentos relacionados a KAN-XX.
3. Pesquise commits e Pull Requests que mencionem KAN-XX.
4. Verifique se o ticket já foi total ou parcialmente implementado.
5. Compare o que existe com cada critério de aceite.
6. Não recrie arquivos ou funcionalidades existentes.
7. Preserve decisões válidas já aplicadas.

Classifique inicialmente o ticket como:

* `NOT_STARTED`;
* `PARTIAL`;
* `IMPLEMENTED_UNTRACKED`;
* `READY_FOR_REVIEW`;
* `BLOCKED`;
* `DONE`.

A existência de um arquivo não comprova a conclusão. Cruze código, testes, documentação, commits, PRs e critérios de aceite.

## 3. Validar o roteamento de skills

Use as skills do bloco `MOTIVA-SKILLS` e da matriz central.

Não utilize skills incompatíveis apenas porque aparecem no ticket.

Exemplos:

* DevSecOps e CI/CD não devem utilizar skill de frontend/design sem alteração visual real.
* Ticket de treino deve utilizar skills de experimento de ML.
* Ticket de avaliação deve utilizar gate de avaliação.
* Ticket de dataset deve utilizar governança de dados.
* Ticket de coleta física deve utilizar o gate físico.
* Ticket de API deve utilizar contrato de inferência e segurança quando aplicável.
* Ticket visual deve utilizar design system e acessibilidade.

Se houver divergência clara:

1. registre a inconsistência;
2. siga o roteamento tecnicamente correto;
3. atualize o bloco `MOTIVA-SKILLS` e a matriz central quando estiver autorizado;
4. não simule skill inexistente;
5. não carregue skill irrelevante.

## 4. Validar Definition of Ready

Confirme:

* objetivo claro;
* escopo;
* fora do escopo;
* entregáveis;
* critérios de aceite;
* testes esperados;
* documentação esperada;
* dependências concluídas;
* gate humano disponível;
* acessos disponíveis;
* ausência de ciclo;
* ausência de impedimento ativo;
* ausência de ticket duplicado.

Se alguma dependência realmente bloquear o ticket:

1. não mova para `Em andamento`;
2. adicione comentário de bloqueio;
3. aplique `Flagged = Impediment`;
4. informe exatamente o desbloqueio necessário;
5. execute somente preparação independente do bloqueio;
6. finalize com `BLOCKED`.

Não invente acessos, aprovações, imagens, medições, dados, licenças, métricas ou resultados.

## 5. Início no Jira

Se o ticket estiver pronto:

1. adicione o comentário oficial de início;
2. informe o executor e o modelo;
3. informe as skills ativadas;
4. informe o plano resumido;
5. informe riscos conhecidos;
6. mova KAN-XX para `Em andamento`;
7. crie uma branch exclusiva.

Formato da branch:

```text
tipo/KAN-XX-descricao-curta
```

Não use a mesma branch para outro ticket principal.

## 6. Plano de execução

Antes da implementação, apresente um plano curto contendo:

* estado atual encontrado;
* lacunas;
* arquivos ou módulos afetados;
* abordagem;
* testes;
* documentação;
* riscos;
* critérios de aceite que serão validados.

Depois do plano, prossiga automaticamente. Não solicite confirmação para decisões técnicas reversíveis já cobertas pelas regras.

## 7. Implementação

Durante a implementação:

* execute somente o escopo de KAN-XX;
* siga a arquitetura existente;
* preserve as fronteiras dos módulos;
* utilize as skills corretas;
* evite refatorações externas ao ticket;
* mantenha tipagem estrita;
* não introduza `any`;
* não exponha secrets;
* não armazene imagens reais, datasets ou pesos no Git;
* não utilize dados de teste como dados reais;
* não utilize test set para tuning;
* não altere produção;
* não crie recursos pagos;
* não faça push direto para `main`;
* não faça merge automático;
* não esconda falhas com `continue-on-error`;
* não desative testes para obter resultado verde;
* não altere critérios de aceite silenciosamente.

Quando encontrar defeito fora do escopo, abra um Bug conforme a política oficial e relacione-o ao ticket.

## 8. Atualização durante o trabalho

Adicione comentário de progresso apenas quando houver:

* decisão relevante;
* mudança de abordagem;
* resultado parcial importante;
* risco novo;
* bloqueio;
* descoberta que afete o ticket;
* execução longa com avanço significativo.

Não crie comentários vazios ou repetitivos.

## 9. Validação obrigatória

Antes de considerar a implementação pronta:

1. execute lint aplicável;
2. execute formatação;
3. execute typecheck;
4. execute testes unitários;
5. execute testes de integração;
6. execute testes de contrato;
7. execute E2E quando aplicável;
8. execute testes de segurança quando aplicável;
9. execute build;
10. execute smoke test;
11. valide os critérios de aceite um por um;
12. revise todo o diff;
13. confirme ausência de mudança fora do escopo;
14. atualize a documentação;
15. valide os links;
16. registre limitações reais.

Não declare nenhum teste como executado sem possuir resultado real.

Caso um teste não possa ser executado, informe explicitamente:

* qual teste;
* motivo;
* impacto;
* ação necessária;
* status do ticket.

## 10. Commits e Pull Request

Quando a implementação estiver pronta:

1. crie commits pequenos e rastreáveis;
2. utilize Conventional Commits;
3. mencione `KAN-XX` em todos os commits relevantes;
4. faça push da branch;
5. abra Pull Request contra a branch principal;
6. use o título:

```text
[KAN-XX] Descrição objetiva
```

O Pull Request deve conter:

* objetivo;
* ticket;
* alterações;
* fora do escopo;
* testes e resultados;
* evidências;
* screenshots quando aplicável;
* impacto arquitetural;
* impacto de segurança;
* impacto de privacidade;
* impacto em dados ou ML;
* documentação;
* riscos;
* limitações;
* rollback;
* checklist.

## 11. Atualização final do Jira

Depois de abrir o Pull Request:

1. adicione comentário de envio para análise;
2. informe branch;
3. informe PR;
4. informe commits;
5. informe arquivos principais;
6. informe testes e resultados;
7. valide cada critério de aceite;
8. informe documentação atualizada;
9. informe Bugs relacionados;
10. informe riscos residuais;
11. informe as skills realmente utilizadas;
12. mova KAN-XX para `Em análise`.

Não mova para `Concluído`.

A conclusão ocorrerá somente após revisão independente.

## 12. Caso a implementação já esteja pronta

Se a auditoria inicial comprovar que o trabalho já existe no repositório:

* não reimplemente;
* execute os testes;
* valide critérios de aceite;
* corrija apenas lacunas;
* encontre ou crie a rastreabilidade necessária;
* atualize documentação;
* abra ou relacione PR;
* mova para `Em análise`.

Não feche diretamente sem revisão independente.

## 13. Resposta final obrigatória

Apresente:

* ticket;
* classificação inicial;
* status final no Jira;
* branch;
* commits;
* Pull Request;
* arquivos alterados;
* testes executados;
* resultados;
* critérios de aceite;
* documentação atualizada;
* Bugs;
* riscos;
* limitações;
* skills utilizadas;
* decisão final:

  * `READY_FOR_REVIEW`;
  * `PARTIAL`;
  * `BLOCKED`.

Não execute o próximo ticket.
