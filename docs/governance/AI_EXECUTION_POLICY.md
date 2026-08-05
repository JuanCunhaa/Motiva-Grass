# Política de Execução por IA e Desenvolvedores

## Objetivo

Estabelecer o processo oficial para selecionar, iniciar, executar, revisar, concluir ou interromper trabalho no Motiva-Grass. Esta política é normativa para agentes de IA e pessoas e deriva de KAN-1, KAN-2 a KAN-17, KAN-20, KAN-89 e dos tickets KAN-18 a KAN-156.

## Escopo

Aplica-se a História, Tarefa, Bug e Subtask do projeto Jira `KAN`, incluindo pesquisa, documentação, código, dados, ML, infraestrutura, QA e release. Épicos e KAN-1 organizam o trabalho, mas não geram branch própria. Esta política não autoriza gasto, produção, uso de credenciais, alteração administrativa ou aceite de risco.

## Fontes oficiais e conflitos

| Fonte | Responsabilidade oficial |
|---|---|
| Jira | objetivo, escopo, fora do escopo, dependências, prioridade, responsável, status, bloqueios, gates humanos, critérios de aceite, progresso, branch/PR, Bugs e decisão de conclusão |
| Repositório Git | arquitetura, regras de desenvolvimento, código, ADRs, API, schemas, dados, segurança, testes, runbooks, Data Cards, Model Cards e documentação de release |
| Pull Request | alterações e arquivos, evidências, testes, screenshots, impactos, riscos, revisão, aprovação e rollback |

Não existe uma precedência universal entre as três fontes: cada uma prevalece no domínio acima. O PR não pode mudar o escopo do Jira; o Jira não substitui um schema versionado; uma conversa não substitui nenhuma fonte oficial.

Ao encontrar conflito, o executor deve:

1. parar apenas a parte afetada;
2. registrar no Jira os trechos conflitantes, links e impacto;
3. manter o ticket em `Tarefas pendentes`, ou retirar de `Em andamento` se não restar trabalho legítimo;
4. pedir decisão do responsável pelo domínio: Product Owner para objetivo/escopo, owner técnico para arquitetura, data/ML owner para dados e modelos, security owner para aceite de risco;
5. atualizar todas as fontes afetadas pela decisão, preferencialmente por ADR quando a decisão técnica for duradoura;
6. retomar somente quando houver uma interpretação única e rastreável.

Nenhuma decisão, credencial, evidência, limitação ou mudança de escopo importante pode existir somente em conversa com uma IA.

## Regras obrigatórias

### Um ticket principal por vez

Cada executor mantém no máximo um ticket principal em execução. Subtasks podem dividir o mesmo objetivo; correções indispensáveis dentro do mesmo escopo não contam como outro ticket. Trabalho independente exige outro ticket e não pode ser iniciado pelo mesmo executor até encerrar, devolver ou bloquear formalmente o atual.

### Seleção da próxima tarefa executável

O executor deve gerar uma lista de candidatos e aplicar, nesta ordem:

1. excluir KAN-1, Épicos, itens concluídos, duplicados e itens já assumidos por outro executor;
2. localizar a posição do candidato na ordem oficial de KAN-1 e respeitar o primeiro conjunto de trabalho que possa avançar em paralelo;
3. validar o Épico pai e ler suas regras de encerramento;
4. verificar dependências na seção `Dependências` e links Jira, sem assumir que um link `Blocks` está correto quando contradiz o texto;
5. excluir qualquer item com dependência bloqueadora não concluída ou não formalmente dispensada;
6. verificar Definition of Ready, dados, fixtures, acessos, credenciais, licenças, custo, produção e gates;
7. verificar duplicidade por objetivo, componente, erro e entregável, não apenas por título;
8. confirmar que não há responsável, comentário de início, branch ou PR indicando execução concorrente;
9. dentro da mesma frente executável, ordenar por `priority-p0`, depois `priority-p1`, depois `priority-p2`, e então pela posição em KAN-1;
10. selecionar o primeiro ticket cujo resultado seja específico e verificável.

O menor número de ticket é apenas um identificador. Não é critério de seleção.

### Validação antes do início

Antes de alterar o status, o executor deve ler KAN-1, o Épico pai, o ticket, KAN-20, dependências e documentação relacionada; executar a checklist da DoR; confirmar responsável e ausência de execução concorrente; e registrar qualquer lacuna no Jira sem inventar conteúdo.

Se houver alteração versionada, deve criar branch exclusiva no formato `tipo/KAN-N-descricao-curta`. Em seguida, registra o comentário de início e move imediatamente para `Em andamento`. Se não houver alteração versionada, deve registrar no comentário `Branch: não aplicável` e justificar.

### Execução e progresso

O executor trabalha somente no escopo, preserva mudanças alheias, testa proporcionalmente ao risco e mantém documentação junto da entrega. Decisão técnica duradoura, transversal, difícil de reverter ou com alternativas relevantes exige ADR. Decisão local e reversível pode ficar no PR e no comentário de progresso.

Adicionar comentário de progresso quando ocorrer ao menos um destes eventos:

- mudança material de plano, risco, escopo proposto ou premissa;
- bloqueio novo ou removido;
- marco relevante em tarefa com duração superior a um dia útil;
- troca de executor/modelo;
- resultado intermediário necessário para auditoria;
- solicitação explícita do revisor.

Tarefas pequenas não exigem diário de atividades: início e envio para análise bastam quando não há evento material.

### Bloqueios e trabalho parcial

Um bloqueio deve ser registrado com evidência, dono do desbloqueio, ação requerida, impacto e condição de revisão. Aplicar `Flagged = Impediment` e uma label específica como `blocked-access`, `blocked-data`, `blocked-license`, `blocked-admin` ou `blocked-external`.

Se nada útil puder avançar, comentar e manter ou devolver o item a `Tarefas pendentes`. Permanecer em `Em andamento` é permitido somente quando existe trabalho parcial legítimo, delimitado e ativo; o comentário deve separar explicitamente `pode avançar` de `não pode avançar`.

Resultado parcial nunca satisfaz a conclusão. Deve ser entregue como evidência intermediária, com itens feitos, ausentes, impacto e ticket de continuação quando aplicável.

### Bugs durante a execução

Corrigir no ticket atual apenas defeito introduzido pelas mudanças atuais, pequeno, diretamente necessário aos critérios de aceite e sem ampliar materialmente o risco. Abrir Bug separado para defeito preexistente, fora do escopo, reproduzível em outra área, que exija investigação própria, altere prazo/risco, ou precise de priorização e regressão independentes.

Um Bug crítico que invalide critérios de aceite bloqueia o ticket original. Bug não crítico pode permitir o envio para análise se a limitação estiver explícita, o escopo entregue continuar válido e o responsável aceitar a separação. A hipótese inicial nunca é causa confirmada sem evidência.

### Envio, conclusão e interrupção

Mover para `Em análise` somente depois de implementação/documentação concluídas, testes aplicáveis executados, evidências reais disponíveis, critérios verificados, riscos registrados e PR aberto quando aplicável.

Mover para `Concluído` somente após aprovação do PR, checks obrigatórios, DoD completa, rastreabilidade registrada e ausência de Bug crítico bloqueador. O comentário final deve declarar `concluído`, `concluído com limitações` ou `NO-GO`. `Concluído com limitações` exige que todos os critérios de aceite ainda estejam satisfeitos; limitação que viola aceite impede conclusão.

O executor deve interromper e exigir ação humana quando houver gate ativo, credencial ou acesso indisponível, custo/contratação, produção, aceite de risco, mudança significativa de escopo, conflito normativo não resolvido, dado real ausente, licença ambígua, promoção de modelo, publicação de release ou ação física. A interrupção não autoriza declarar sucesso parcial como conclusão.

## Resultados parciais e NO-GO

Todo resultado não integral deve informar: estado (`parcial`, `bloqueado` ou `NO-GO`), trabalho concluído, trabalho não concluído, motivo, evidência, impacto nos critérios, artefatos aproveitáveis, ação necessária e ticket seguinte.

Casos mínimos:

| Situação | Registro obrigatório |
|---|---|
| Teste não executado | nome do teste, motivo, risco e condição para execução |
| Ferramenta/serviço indisponível | erro real, horário, alternativa tentada e reavaliação |
| Acesso/credencial ausente | acesso necessário e owner; nunca registrar o segredo |
| Licença não confirmada | componente, fonte consultada e uso suspenso |
| Pesquisa inconclusiva | perguntas respondidas, lacunas e fontes |
| Modelo abaixo do critério | métricas reais, dataset/split/versão e decisão NO-GO |
| Dataset insuficiente | cobertura real, lacunas e impacto estatístico |
| Dependência externa | serviço, evidência e fallback permitido |
| Decisão de não prosseguir | critérios acionados, alternativas e decisão autorizada |

É proibido inventar métricas, dados, testes, medições ou evidências; usar fixture como dado real; declarar integração sem teste; concluir ticket bloqueado; esconder limitações; relaxar aceite sem decisão formal; ou apresentar parcial como completo.

## Regras recomendadas

- Usar comentários curtos com links para detalhes versionados.
- Registrar decisões duradouras em ADR e relacioná-las ao Jira/PR.
- Preferir fixtures sintéticas identificadas e reproduzíveis para testes locais.
- Revalidar dependências e execução concorrente imediatamente antes do início.
- Dividir ticket somente quando cada parte mantiver resultado verificável e rastreabilidade própria.

## Exemplos corretos

- `KAN-76` está pronto, suas dependências foram concluídas e não há executor ativo; cria-se `feat/KAN-76-image-preview`, comenta-se o início e então move-se para `Em andamento`.
- Uma API externa retorna 403; o executor registra a resposta, mantém o teste como não executado e solicita acesso, sem declarar a integração funcional.
- Um defeito preexistente de upload é reproduzido durante outra tarefa; abre-se Bug separado e só bloqueia o original se invalidar seu aceite.

## Exemplos incorretos

- Escolher KAN-21 apenas porque tem número baixo, ignorando a ordem e as dependências de KAN-1.
- Mover para `Em andamento` para “reservar” trabalho sem branch, comentário ou atividade real.
- Copiar uma conclusão da conversa para o código sem registrar Jira, PR ou ADR.
- Marcar `Concluído` com teste não executado ou resultado parcial.

## Exceções

Hotfix de incidente pode usar fluxo abreviado somente conforme runbook versionado, com ticket e rastreabilidade retroativa no prazo definido pelo runbook. Pesquisa sem mudança de arquivos pode dispensar branch/PR quando Jira e documento oficial contiverem entrega e evidência; a exceção deve ser registrada. Alteração conjunta de tickets em um PR exige justificativa prévia, escopo inseparável e aprovação humana; a regra padrão continua sendo um ticket por branch e PR.

## Checklist

- [ ] Um único ticket principal foi selecionado pela ordem de KAN-1 e prioridade da frente executável.
- [ ] Épico, labels, dependências textuais, `Blocks`, gates, duplicidade e execução concorrente foram verificados.
- [ ] A DoR está completa e dados/acessos necessários existem.
- [ ] Branch e comentário de início precederam `Em andamento`, ou a exceção foi documentada.
- [ ] Progresso, decisões, riscos, bloqueios e parciais foram registrados quando materiais.
- [ ] Testes e evidências são reais e distinguem fixtures de dados reais.
- [ ] PR, documentação e critérios estão completos antes de `Em análise`.
- [ ] Aprovação, checks, DoD e rastreabilidade estão completos antes de `Concluído`.

