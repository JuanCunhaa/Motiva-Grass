# Templates de Comentários do Jira

## Objetivo

Padronizar registros auditáveis e concisos de início, progresso, bloqueio, análise e conclusão.

## Escopo

Aplica-se a todos os tickets executáveis KAN. Os templates devem ser adaptados ao trabalho; campos não aplicáveis recebem `N/A — motivo`, nunca conteúdo inventado.

## Regras obrigatórias

- Usar data/hora ISO 8601 com fuso, por exemplo `2026-08-05T14:30:00-03:00`.
- Identificar pessoa/agente e modelo realmente usado.
- Usar links estáveis para branch, PR, documentos e evidências.
- Distinguir `não executado`, `não aplicável`, `falhou` e `aprovado`.
- Não registrar secrets, dados pessoais desnecessários ou logs sensíveis.
- Editar somente para correção pequena; mudança de estado material recebe novo comentário.

### Comentário de início

```markdown
## Início da execução

- Responsável/agente: <nome ou identificador>
- Modelo de IA: <modelo e modo; ou N/A>
- Início: <ISO 8601 com fuso>
- Objetivo resumido: <resultado verificável>
- Dependências verificadas: <chaves + estado/evidência>
- Gates verificados: <inativos/aprovados/N/A + evidência>
- Branch: <URL ou N/A — motivo>
- Documentos lidos: <KAN-1, Épico, KAN-20, ticket, ADRs/docs>
- Plano curto:
  1. <passo>
  2. <passo>
  3. <passo>
- Testes planejados: <lista objetiva>
- Riscos conhecidos: <riscos ou nenhum identificado>
```

### Comentário de progresso

```markdown
## Progresso

- Data/hora: <ISO 8601 com fuso>
- Concluído desde a última atualização: <atividades/artefatos>
- Atividade atual: <uma frase>
- Testes executados: <comando/caso + resultado + evidência>
- Decisões tomadas: <decisão + link para ADR/PR quando aplicável>
- Problemas encontrados: <fatos, sem causa não comprovada>
- Alterações de plano: <mudança + motivo; ou nenhuma>
- Riscos/limitações: <estado atual>
- Próximo passo: <ação verificável>
```

Publicar progresso apenas em mudança material, marco de tarefa longa, novo/removido bloqueio, troca de executor/modelo ou alteração relevante de plano/risco. Para tarefa pequena, não repetir o que já está no PR.

### Comentário de bloqueio

```markdown
## Bloqueio ativo

- Detectado em: <ISO 8601 com fuso>
- Motivo objetivo: <condição que impede o próximo passo>
- Evidência: <erro, link, screenshot ou teste>
- Dependência/pessoa que pode desbloquear: <chave, papel ou owner>
- Ação necessária: <ação única e verificável>
- Impacto: <escopo, prazo, aceite e testes afetados>
- Partes que ainda podem avançar: <lista ou nenhuma>
- Próxima revisão: <data ou condição>
- Flag/label: `Flagged = Impediment`, `<blocked-* ou gate-human>`
```

### Comentário de desbloqueio/retomada

```markdown
## Desbloqueio e retomada

- Data/hora: <ISO 8601 com fuso>
- Evidência do desbloqueio: <link/resultado>
- Flag removida: <sim/não + motivo>
- DoR revalidada: <sim + alterações>
- Próximo passo: <ação>
```

### Comentário de envio para análise

```markdown
## Envio para análise

- Resumo da entrega: <resultado>
- Branch: <URL ou N/A — motivo>
- Pull Request: <URL ou N/A — motivo>
- Arquivos/componentes: <lista curta>
- Testes executados: <comandos/casos>
- Resultados: <aprovados/falhas conhecidas + evidências>
- Critérios de aceite:
  - [x] <critério 1> — <evidência>
  - [x] <critério 2> — <evidência>
- Documentação criada/atualizada: <links>
- Bugs relacionados: <chaves ou nenhum>
- Riscos: <lista>
- Limitações: <lista; declarar testes não executados>
- Instruções ao revisor: <áreas críticas e como validar>
```

### Comentário de conclusão

```markdown
## Conclusão

- Resultado final: <resultado verificável>
- Pull Request: <URL ou N/A — motivo>
- Commit de merge: <SHA/URL ou N/A>
- Testes finais: <checks, comandos e resultados>
- Evidências: <links>
- Documentos alterados: <links/caminhos>
- Bugs relacionados: <chaves + estado>
- Riscos residuais: <lista ou nenhum conhecido>
- Decisão final: <concluído | concluído com limitações | NO-GO>
- Justificativa da decisão: <relação com critérios de aceite e DoD>
```

### Registro de resultado parcial

```markdown
## Resultado parcial — não é conclusão

- Estado: <parcial | bloqueado | NO-GO>
- Entregue: <itens e evidências>
- Não entregue: <itens>
- Motivo: <fato verificável>
- Critérios afetados: <lista>
- Artefatos aproveitáveis: <links>
- Ação/ticket de continuação: <chave ou ação humana>
```

### Registro de decisão

```markdown
## Decisão

- Contexto: <problema>
- Opções consideradas: <lista>
- Decisão: <escolha>
- Evidências e critérios: <links>
- Impactos/riscos: <lista>
- Reversibilidade: <como desfazer>
- ADR: <link ou N/A — decisão local e reversível>
- Aprovador humano: <quando exigido>
```

## Regras recomendadas

- Preferir resumo no comentário e detalhe no repositório/PR.
- Usar checklists somente para critérios realmente verificados.
- Referenciar comandos de teste e versões sem colar logs extensos.
- Comentar remoção do bloqueio para fechar o ciclo de auditoria.

## Exemplos corretos

- `Testes executados: pytest tests/api - 42 passed; log no check do PR`.
- `Teste de integração: não executado — credencial do sandbox ausente; risco: contrato externo não validado`.
- `Causa: hipótese de timeout no proxy; ainda não confirmada`.

## Exemplos incorretos

- `Tudo pronto` sem evidência, branch ou critérios.
- `Provavelmente funciona` apresentado como resultado de teste.
- Colar token de acesso em comentário.
- Publicar progresso a cada arquivo salvo sem mudança material.

## Exceções

Incidente ativo pode usar comentário abreviado conforme runbook, mas deve ser consolidado depois. Automação pode gerar o esqueleto do comentário, porém o executor continua responsável pela veracidade. Campo sem aplicação deve ser justificado, não removido quando sua ausência prejudicar auditoria.

## Checklist

- [ ] O comentário apropriado ao evento foi usado.
- [ ] Responsável, data/hora e modelo estão corretos.
- [ ] Links e evidências são acessíveis e não contêm segredos.
- [ ] Testes não executados estão claramente separados de aprovados.
- [ ] Limitações, riscos e hipóteses estão explícitos.
- [ ] O nível de detalhe é proporcional à tarefa.
