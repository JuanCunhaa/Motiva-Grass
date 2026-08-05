# Motiva Grass

Motiva Grass é um MVP em estágio inicial que pretende analisar uma fotografia
de gramado, validar a captura, identificar uma classe suportada e estimar a
altura com confiança explícita, avisos e resultado inconclusivo quando
necessário.

O repositório contém atualmente documentação de governança, arquitetura e
engenharia, além de ferramentas de governança de agentes. Ele **ainda não**
contém aplicação web funcional, API, modelo treinado ou implantação em produção.

## Comece aqui

1. Leia o [rulebook do projeto](PROJECT_RULEBOOK.md) para conhecer a precedência
   e as regras invariantes.
2. Leia [AGENTS.md](AGENTS.md) antes de trabalho assistido por agentes.
3. Use o [índice da documentação](docs/DOCUMENTATION_INDEX.md) para encontrar os
   documentos técnicos e operacionais canônicos.
4. Siga [CONTRIBUTING.md](CONTRIBUTING.md) para branches, commits, testes e Pull
   Requests.

## Conteúdo do repositório

| Caminho | Finalidade |
|---|---|
| `docs/` | Documentação, decisões e evidências canônicas do projeto |
| `.agents/` | Skills Motiva, controles compartilhados e templates |
| `config/skills/` | Catálogo versionado de skills e roteamento Jira |
| `scripts/` | Geradores e validadores de governança |
| `tests/` | Testes da automação de governança existente |
| `vendor/` | Snapshots auditados de skills públicas |

Diretórios de aplicação, API, dados e ML serão criados somente pelos respectivos
tickets Jira após a aprovação da arquitetura proposta. Datasets reais, imagens
privadas, pesos de modelos e secrets devem permanecer fora do Git.

## Fluxo de trabalho

O Jira é a fonte de verdade para escopo, prioridade, dependências e estado. Toda
mudança versionada usa branch e Pull Request exclusivos do ticket; commits
diretos na `main` não fazem parte do fluxo normal. O registro factual do
bootstrap inicial e de sua exceção única está no
[registro de bootstrap](docs/governance/REPOSITORY_BOOTSTRAP_RECORD.md).

## Estado da licença

Nenhuma licença do projeto foi selecionada ou publicada. A visibilidade do
repositório não deve ser interpretada como concessão de licença. A análise e a
aprovação de licença pertencem ao ticket de compliance aplicável.
