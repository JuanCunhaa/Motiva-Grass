# Definition of Ready (DoR)

## Objetivo

Determinar objetivamente se um ticket pode entrar em desenvolvimento sem depender de suposições do executor.

## Escopo

Aplica-se a História, Tarefa, Bug e Subtask antes de `Em andamento`. A DoR é verificada novamente após bloqueio, mudança material de escopo ou troca de executor.

## Regras obrigatórias

Um ticket está pronto somente quando todos os itens aplicáveis estão satisfeitos:

### Identidade e responsabilidade

- objetivo único, claro e verificável;
- resultado esperado observável;
- tipo correto;
- Épico pai (ou ticket pai para Subtask);
- responsável/executor definido antes do início;
- prioridade operacional `priority-p0`, `priority-p1` ou `priority-p2`;
- labels de área, fase e modelo recomendado.

### Escopo e entrega

- escopo incluído explícito;
- fora do escopo quando houver fronteira relevante;
- entregáveis identificados;
- critérios de aceite objetivos e testáveis;
- testes esperados e evidências necessárias;
- documentação oficial a criar/atualizar.

### Dependências e viabilidade

- dependências conhecidas na descrição;
- links `Blocks` corretos para caminho crítico;
- dependências bloqueadoras concluídas ou dispensa formal registrada;
- ausência de duplicidade e execução concorrente;
- dados reais, fixtures e schemas disponíveis e identificados;
- acessos e ambientes disponíveis, sem expor credenciais;
- ferramenta e capacidade mínimas disponíveis;
- custo, produção, licença e credencial avaliados;
- riscos conhecidos registrados.

### Gates

- gate humano real identificado com papel, momento e evidência;
- gate necessário ao início já aprovado;
- gate futuro não é tratado como impedimento ativo;
- `Flagged = Impediment` aplicado quando houver bloqueio atual.

### Bugs

Além dos itens aplicáveis, Bug precisa de observado, esperado, reprodução, ambiente, versão/commit, dados/fixture, evidência, impacto, severidade, prioridade, hipótese claramente rotulada, origem e regressão esperada.

## Procedimento quando não estiver pronto

1. não criar branch nem mover para `Em andamento`;
2. listar no Jira cada requisito ausente sem inventar resposta;
3. identificar owner/ação para preencher a lacuna;
4. aplicar impedimento somente se a lacuna bloquear trabalho agora;
5. propor ajuste ou ticket preparatório quando a lacuna for grande;
6. manter em `Tarefas pendentes`;
7. reavaliar após evidência do preenchimento.

Se escopo e aceite forem contraditórios, registrar conflito e pedir decisão do Product Owner. Se a documentação técnica contradizer o ticket, aplicar a política de conflitos. O executor não pode flexibilizar a DoR por conta própria.

## Regras recomendadas

- Escrever critérios no formato situação–ação–resultado quando útil.
- Limitar ticket a resultado revisável em um PR coerente.
- Incluir exemplos/fixtures sanitizados para contratos complexos.
- Marcar item da DoR como N/A com justificativa, não omiti-lo silenciosamente.
- Revisar links estruturados após alteração de dependência textual.

## Exemplos corretos

- `Implementar validação MIME` contém formatos, limites, erros esperados, fixtures maliciosas, testes e dependências concluídas.
- Pesquisa define perguntas, fontes mínimas, entregável, critérios de suficiência e possibilidade de resultado inconclusivo.
- Gate de produção está documentado, mas não impede implementação local anterior.

## Exemplos incorretos

- `Melhorar upload` sem comportamento esperado ou aceite.
- Iniciar com dependência crítica aberta porque “provavelmente ficará pronta”.
- Inventar credencial, dataset ou meta ausente para marcar a checklist.
- Considerar label de prioridade suficiente enquanto o objetivo é ambíguo.

## Exceções

Incidente pode iniciar com DoR mínima definida no runbook (impacto, owner, contenção, evidência e autoridade), devendo completar o registro depois. Spike exploratório pode ter solução desconhecida, mas precisa de pergunta, limite de tempo, fontes, entregável e critério de encerramento. Subtask herda contexto do pai, porém deve manter objetivo e aceite próprios.

## Checklist

- [ ] Objetivo e resultado verificável.
- [ ] Pai, tipo, responsável, prioridade e labels de área/fase/modelo.
- [ ] Escopo, fora do escopo aplicável e entregáveis.
- [ ] Testes, evidências e critérios de aceite objetivos.
- [ ] Riscos e documentação esperada.
- [ ] Dependências textuais e `Blocks` corretos e liberados.
- [ ] Sem duplicidade nem execução concorrente.
- [ ] Dados, fixtures, acesso, ambiente e capacidade disponíveis.
- [ ] Custo, produção, licença, credenciais e gate avaliados.
- [ ] Nenhuma informação ausente foi inventada.

