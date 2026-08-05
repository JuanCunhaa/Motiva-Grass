# Como contribuir

## Antes da mudança

Leia [AGENTS.md](AGENTS.md), o ticket Jira e os documentos canônicos no [índice](docs/DOCUMENTATION_INDEX.md). Confirme Definition of Ready, dependências, ausência de trabalho concorrente e gates humanos. Uma contribuição deve ter um ticket principal `KAN-N`.

## Branch e commits

- Branch: `tipo/KAN-N-descricao-curta`.
- Commit: Conventional Commits com `[KAN-N]`, por exemplo `fix(api): reject invalid media [KAN-125]`.
- Mantenha commits pequenos, coerentes e sem segredos, binários privados, datasets ou pesos proibidos.
- Um ticket por branch e PR, salvo exceção registrada e aprovada.

Não reescreva histórico compartilhado nem altere trabalho alheio sem coordenação.

## Implementação

Respeite fronteiras arquiteturais, padrões da linguagem e contratos versionados. Mudança transversal ou difícil de reverter exige ADR. Atualize documentação junto com o comportamento. Dados, experimentos e modelos seguem seus Cards e registros canônicos.

## Testes e evidências

Execute a matriz proporcional ao risco em [TEST_STRATEGY](docs/testing/TEST_STRATEGY.md) e satisfaça [QUALITY_GATES](docs/testing/QUALITY_GATES.md). Registre comando/workflow, versão, ambiente, resultado, falhas e links conforme [TEST_EVIDENCE_STANDARD](docs/testing/TEST_EVIDENCE_STANDARD.md). Teste não executado deve ser declarado; indisponibilidade não equivale a sucesso.

## Pull request

Título: `[KAN-N] descrição objetiva`.

O corpo deve conter:

- problema, resultado e limites do escopo;
- arquivos/contratos/documentos afetados;
- critérios de aceite mapeados para evidências;
- testes executados, resultados e omissões;
- impacto em segurança, privacidade, dados, ML e acessibilidade;
- riscos, gates, compatibilidade, migração e rollback;
- links para Jira, ADR e artefatos.

O autor resolve checks e comentários sem ocultar divergências. Aprovação exige revisores competentes nos domínios afetados.

## Conclusão

Só mova para `Em análise` com entrega e evidência completas. Só conclua o Jira após merge/revisão aplicável, checks obrigatórios, documentação, rastreabilidade e comentário final. Resultado parcial permanece explicitamente parcial e gera continuação rastreável quando necessária.

Vulnerabilidades seguem [VULNERABILITY_MANAGEMENT](docs/security/VULNERABILITY_MANAGEMENT.md); não divulgue detalhes exploráveis em canal público.
