# Política de Rastreabilidade Jira–GitHub

## Objetivo

Garantir uma cadeia auditável entre necessidade, implementação, evidência, documentação e release.

## Escopo

Aplica-se a mudanças de código, configuração, schema, documentação, dados versionados, modelos, infraestrutura e release.

## Regras obrigatórias

A cadeia padrão é:

`Jira → branch → commits → Pull Request → documentação → release`

Cada elo deve apontar para o anterior e o seguinte quando existir. Ausência aplicável exige justificativa no Jira e PR.

### Jira

O ticket identifica objetivo, escopo, aceite e dependências; recebe link da branch, PR, Bugs, documento oficial e release. Não colar segredo, dataset privado ou evidência efêmera sem retenção definida.

### Branch

Formato obrigatório: `tipo/KAN-N-descricao-curta`.

Tipos recomendados: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `research`, `data`, `mlops`, `infra`, `hotfix`.

Exemplos:

- `feat/KAN-76-image-preview`
- `fix/KAN-145-invalid-upload`
- `docs/KAN-20-agent-policy`

Usar minúsculas, hífens, uma única chave e descrição curta. Um ticket com alteração versionada possui branch exclusiva.

### Commits

Usar Conventional Commits e chave Jira:

`<tipo>(<escopo>): <descrição imperativa> [KAN-N]`

Exemplo: `feat(web): add image preview [KAN-76]`.

Cada commit deve ser revisável, não conter secrets/dados proibidos e corresponder ao ticket da branch. Commit de merge é registrado no comentário final.

### Pull Request

Título: `[KAN-N] Descrição objetiva`.

O corpo deve conter resumo, ticket, escopo/fora do escopo, arquivos/componentes, testes e resultados, evidências/screenshots, critérios de aceite, documentação, impactos, riscos, segurança/acessibilidade/dados/ML quando aplicável, Bugs, rollback e checklist. PR não substitui atualização do Jira.

Todo ticket com código requer PR exclusivo, salvo exceção documentada antes da implementação. PR em draft pode apoiar colaboração, mas não satisfaz `Em análise` até estar revisável.

### Documentação

Documentação normativa vive no repositório. O PR liga o ticket aos caminhos alterados; o Jira recebe links para documentos renderizados ou caminhos estáveis. ADR inclui chave Jira e PR. Data Card/Model Card identifica dataset/modelo, versão, checksum, métricas e limitações reais.

### Release

Release identifica PRs/tickets, tag imutável, commit, checksums de artefatos, Model/Data Cards aplicáveis, notas, migração, riscos e rollback. Publicar exatamente a release candidate aprovada. KAN-151/KAN-152 exigem gate humano.

### Exceções e múltiplos tickets

Um PR com múltiplos tickets só é permitido quando as mudanças são tecnicamente inseparáveis, todos os tickets estão prontos, a exceção está registrada antes, cada critério é verificável e um ticket é declarado principal. Não usar para conveniência ou acumulação.

PR de documentação/pesquisa pode ser dispensado apenas quando não houver repositório/artefato versionado e o Jira/documento oficial tiverem revisão e evidência. Assim que o repositório existir, documentação normativa deve ser versionada.

## Regras recomendadas

- Configurar autolink de `KAN-\d+` para o Jira.
- Usar squash somente se preservar mensagem com chave e autoria útil.
- Gerar changelog/release notes a partir de PRs, com revisão humana.
- Manter screenshots e evidências em local com retenção estável.
- Assinar tags/releases e registrar checksums para modelos e artefatos críticos.

## Exemplos corretos

- Ticket KAN-76 → branch `feat/KAN-76-image-preview` → commits com `[KAN-76]` → PR `[KAN-76] Add image preview` → documentação UX → release note.
- ADR `ADR-0003` referencia KAN-97 e o PR que o adicionou; o Jira aponta de volta ao ADR.
- Model Card registra hash do artefato promovido e release aponta para o card.

## Exemplos incorretos

- Branch `feature/new-stuff` sem chave Jira.
- Commit `fix things` ou PR que mistura KAN-76 e refatoração independente.
- PR declara teste aprovado sem link/resultado.
- Release recompila artefato diferente da candidate aprovada.

## Exceções

Hotfix segue `hotfix/KAN-N-descricao`, runbook e PR acelerado, sem eliminar revisão posterior. Commit automatizado pode usar conta de bot, mas deve incluir chave e origem. Artefatos grandes/privados permanecem fora do Git e são rastreados por URI controlada, versão e checksum.

## Checklist

- [ ] Ticket possui objetivo, aceite e links atuais.
- [ ] Branch segue `tipo/KAN-N-descricao-curta`.
- [ ] Commits seguem Conventional Commits e contêm `[KAN-N]`.
- [ ] PR segue `[KAN-N] Descrição objetiva` e contém evidências, riscos e rollback.
- [ ] Documentos/ADRs/Data Cards/Model Cards foram relacionados.
- [ ] Merge commit e Bugs foram registrados no Jira.
- [ ] Release aponta para artefato exato, tickets, documentação e rollback.

