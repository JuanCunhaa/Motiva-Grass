# Definition of Done (DoD)

## Objetivo

Definir as condições cumulativas para declarar um ticket completo com evidência verificável.

## Escopo

Aplica-se a todos os tickets executáveis e complementa critérios específicos do Jira. Merge, deploy ou comentário isolado não equivalem à conclusão.

## Regras obrigatórias

### Entrega e aceite

- escopo do Jira implementado, sem entregas ocultas;
- fora do escopo respeitado;
- critérios de aceite verificados um a um;
- resultado parcial não apresentado como completo;
- resultado `NO-GO` usado como conclusão somente quando previsto pelo objetivo.

### Qualidade e evidência

- testes aplicáveis executados na versão entregue;
- resultados, comandos/ambiente e evidências reais registrados;
- teste não aplicável justificado;
- falhas conhecidas relacionadas a Bugs;
- nenhuma métrica, dado, medição ou evidência inventada;
- fixture explicitamente diferenciada de dado real.

### Código, revisão e integração

- branch/commits/PR seguem a política de rastreabilidade;
- PR aprovado por revisores aplicáveis;
- checks obrigatórios aprovados;
- conflitos resolvidos sem apagar mudanças alheias;
- rollback definido proporcionalmente ao risco;
- merge commit registrado.

### Documentação

- documentação normativa no repositório atualizada;
- Jira atualizado com estado, links, critérios e decisão;
- ADR criado/atualizado para decisão duradoura;
- API/schema/runbook/release notes atualizados quando aplicável;
- Data Card e impactos de dados registrados quando aplicável;
- Model Card, versão, métricas, limitações e promoção registrados quando aplicável.

### Revisões especializadas

- segurança e privacidade revisadas quando aplicável;
- acessibilidade revisada para experiência do usuário;
- migração, retenção, proveniência e leakage revisados para dados;
- calibração, OOD, incerteza e splits revisados para ML;
- custo, capacidade, observabilidade e rollback revisados para operação.

### Riscos, Bugs e gates

- Bugs necessários abertos e relacionados;
- nenhum Bug crítico bloqueador;
- riscos residuais e limitações registrados;
- gates humanos satisfeitos com evidência;
- comentário de conclusão declara `concluído`, `concluído com limitações` ou `NO-GO`;
- `Flagged` removida apenas se não houver impedimento real restante.

`Concluído com limitações` é permitido apenas quando as limitações não violam critérios de aceite, segurança ou obrigação normativa. Caso contrário, o ticket permanece aberto/bloqueado ou resulta em NO-GO quando essa decisão faz parte do objetivo.

## Procedimento de verificação

1. executor preenche a checklist e comenta envio para análise;
2. revisor confere evidências e critérios, não apenas diff;
3. checks e revisões especializadas terminam;
4. merge/deploy aplicável ocorre sobre o artefato aprovado;
5. executor registra merge, documentos, Bugs, riscos e decisão;
6. somente então o Jira muda para `Concluído`.

## Regras recomendadas

- Automatizar checks objetivos, mantendo julgamento humano para risco/escopo.
- Anexar evidência mínima suficiente e armazenar detalhes no sistema apropriado.
- Validar rollback em ambiente seguro para mudanças de alto risco.
- Fazer revisão independente de métricas de ML e de segurança antes da release.

## Exemplos corretos

- Pesquisa de licença conclui `NO-GO` com fontes, alternativas e critérios previstos; isso pode satisfazer a DoD do ticket de decisão.
- Implementação passa testes, atualiza OpenAPI, tem PR aprovado e Bug não bloqueador relacionado com limitação explícita.
- Modelo abaixo da meta não é promovido; métricas reais e Model Card documentam a decisão.

## Exemplos incorretos

- Marcar completo porque o código compila, ignorando aceite e documentação.
- Declarar integração aprovada usando mock sem teste real exigido.
- Aceitar check vermelho porque “não parece relacionado” sem investigação/dispensa formal.
- Usar `concluído com limitações` para esconder critério de aceite não satisfeito.

## Exceções

Ticket administrativo sem PR pode concluir com evidência no Jira e revisão identificada. Hotfix pode mesclar com aprovação acelerada conforme runbook, mas completa evidência e documentação retroativamente no prazo definido. Trabalho descartado não usa DoD de entrega: exige decisão formal de cancelamento/NO-GO conforme objetivo e workflow disponível.

## Checklist

- [ ] Escopo implementado e fora do escopo respeitado.
- [ ] Critérios de aceite verificados com evidência real.
- [ ] Testes aplicáveis executados; N/A e não executados tratados corretamente.
- [ ] PR aprovado e checks aprovados.
- [ ] Segurança, privacidade e acessibilidade revisadas quando aplicável.
- [ ] Impactos e documentos de dados/ML atualizados quando aplicável.
- [ ] Jira, documentação, ADRs e release notes atualizados.
- [ ] Bugs relacionados e nenhum bloqueador crítico aberto.
- [ ] Riscos residuais, limitações e rollback registrados.
- [ ] Comentário final, merge e rastreabilidade completos.
