# Registro do bootstrap do repositório

- **Status:** evidência histórica
- **Ticket:** KAN-18
- **Registrado em:** 2026-08-05
- **Responsável pelo registro:** executor do KAN-18

## Objetivo e escopo

Este documento registra os fatos verificáveis do bootstrap inicial e delimita a
exceção única de commit direto em `main`. Ele não cria uma regra concorrente: o
fluxo vigente continua definido no [Workflow Git](../development/GIT_WORKFLOW.md)
e na [política de rastreabilidade](TRACEABILITY_POLICY.md).

## Estado encontrado na retomada

- O repositório já não estava vazio quando a execução rastreável do KAN-18 foi
  retomada.
- O commit raiz `20655ae39b8bd202d0d0ba689928703c3df6e3dc`, criado em
  `2026-08-05T01:39:44-03:00`, adicionou diretamente à `main` 60 arquivos e
  4.312 linhas.
- Esse conteúdo excedeu o bootstrap mínimo descrito no ticket e não possuía
  branch, Pull Request ou chave KAN-18 no commit.
- A história publicada foi preservada. Reescrevê-la eliminaria rastreabilidade e
  poderia sobrescrever trabalho posterior já revisado.
- Na retomada, `docs/` e `.gitignore` já existiam; README raiz,
  `.editorconfig` e este registro ainda estavam ausentes.

## Exceção única

O commit raiz acima é o único evento reconhecido como exceção histórica de
bootstrap direto em `main`. A exceção está encerrada e não pode ser reutilizada
para mudanças futuras. Toda complementação do KAN-18 ocorre na branch
`docs/KAN-18-bootstrap-documentation` e deve entrar por Pull Request.

Este registro documenta a não conformidade histórica; ele não atribui
retroativamente ao KAN-18 arquivos, testes ou decisões que não possuíam essa
rastreabilidade.

## Complementação rastreável

| Entregável | Estado na retomada | Tratamento no KAN-18 |
|---|---|---|
| README raiz honesto | ausente | criado sem declarar produto funcional |
| `.gitignore` | parcial | ampliado para secrets, temporários, dados e modelos |
| `.editorconfig` | ausente | criado com defaults portáveis |
| `docs/` | existente | preservado; este registro foi indexado |
| Licença | não definida | permanece fora do escopo |

## Validação exigida

A entrega deve registrar, no Pull Request e no Jira, os resultados reais de:

- validação de Markdown e links internos;
- inspeção da árvore final;
- `git diff --check`;
- verificação de arquivos binários/proibidos e indícios de secrets;
- revisão de que nenhuma licença ou código funcional foi adicionado.

## Riscos e limitações

- O critério histórico de “somente README mínimo direto na `main`” não pode ser
  reconstruído retroativamente sem reescrever a história publicada.
- A entrega corrige as lacunas atuais e encerra a exceção, mas mantém explícita
  a não conformidade original para revisão.
- A ausência de arquivo de licença é intencional até a auditoria e aprovação de
  compliance aplicáveis.

## Referências

- [KAN-18](https://gp16-motiva.atlassian.net/browse/KAN-18)
- [Project Rulebook](../../PROJECT_RULEBOOK.md)
- [Workflow Git](../development/GIT_WORKFLOW.md)
- [Política de rastreabilidade](TRACEABILITY_POLICY.md)
- [Política de documentação](../DOCUMENTATION_POLICY.md)
