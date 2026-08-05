# Workflow Git

## Decisão

Usar trunk-based development com `main` protegida, branches curtas por ticket, PR obrigatório e squash merge por padrão.

## Justificativa

Reduz divergência, preserva uma história principal legível e implementa a rastreabilidade exigida por KAN-20 e pela política Jira–GitHub.

## Alternativas

- GitFlow: rejeitado para o MVP por branches longas e releases paralelas desnecessárias.
- Commit direto em `main`: proibido.
- Merge commits por padrão: possível em exceção, mas gera histórico mais ruidoso.

## Regras obrigatórias

### Branches

Formato: `tipo/KAN-N-descricao-curta`.

Tipos: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `security`, `data`, `ml`, `infra`.

- Caracteres: ASCII minúsculo `a-z`, dígitos e hífen; `/` somente após o tipo.
- Comprimento: até 63 caracteres; descrição de 2 a 6 palavras em inglês técnico simples.
- Base: `main` atualizada e verde.
- Duração: ideal até 5 dias úteis; alerta após 7; considerar abandonada após 14 dias sem atividade, após confirmar owner/PR.
- Atualizar com `main` antes de análise/merge. Rebase é preferido em branch de um único owner; branch compartilhada não recebe force push sem coordenação. Usar `--force-with-lease`, nunca `--force`.
- Excluir branch remota após merge. Branch abandonada é fechada com comentário no Jira/PR; preservar tag/commit apenas se houver artefato útil referenciado.
- Proibidos: `feature/test`, `juan-work`, `misc`, `changes`, `final`, `tmp` e nomes sem KAN.

### Commits

Formato: `<type>(<scope>): <imperative summary> [KAN-N]`.

Tipos Conventional Commits: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `build`, `ci`, `revert`.

Escopos oficiais: `web`, `api`, `contracts`, `domain`, `image`, `geometry`, `inference`, `training`, `evaluation`, `data`, `registry`, `observability`, `infra`, `ci`, `security`, `deps`, `docs`, `release`, `repo`.

- Um commit representa uma intenção reversível e mantém build/testes relevantes coerentes.
- Resumo em inglês, imperativo, até 72 caracteres antes da chave quando possível.
- Mensagens proibidas: `wip`, `fix`, `updates`, `misc`, `try again`, `final`, `checkpoint` no histórico revisável.
- Commits temporários são tolerados na branch/draft; devem ser corrigidos ou absorvidos pelo squash antes do merge.
- Squash merge padrão: título do PR vira commit final Conventional Commit com `[KAN-N]`.
- Assistência material de IA usa trailer `Assisted-by: Codex (<modelo>)`. Não inventar identidade/e-mail. `Co-authored-by` só para identidade real e autorizada.
- Trailers opcionais: `Jira: KAN-N`, `ADR: ADR-0001`, `Breaking-Change: ...`; breaking change exige `!` e corpo explicativo.

Exemplos:

```text
feat(web): add camera preview [KAN-76]
fix(api): reject oversized image [KAN-125]
test(ml): validate frozen test-set checksum [KAN-66]
docs(adr): record model registry decision [KAN-95]
```

## Regras recomendadas

- Preferir commits pequenos que expliquem o raciocínio do diff.
- Assinar commits/tags de release quando a infraestrutura permitir.
- Usar merge queue após proteção da `main` em KAN-84.
- Resolver conflitos entendendo ambas as mudanças; nunca escolher “ours/theirs” em massa.

## Exemplos

- `security(api): redact EXIF metadata from logs [KAN-126]` é válido.
- Branch `ml/KAN-60-training-cli` parte de `main` verde e é removida após squash.

## Anti-patterns

- Reescrever branch de outra pessoa, misturar tickets ou commitar secrets/pesos/datasets.
- Criar tag/release diretamente de branch não aprovada.
- Usar commit vazio para fazer CI passar sem corrigir causa.

## Checklist

- [ ] Branch válida, curta, baseada em `main`.
- [ ] Commits atômicos, Conventional Commits e chave Jira.
- [ ] Autoria/assistência de IA transparente.
- [ ] Branch atualizada e CI verde antes do merge.
- [ ] Squash/estratégia correta e branch removida.

## Riscos

Squash perde granularidade de commits; preservar no PR decisões/evidências importantes. Rebase incorreto pode sobrescrever trabalho, mitigado por owner único e `--force-with-lease`.

## Pontos pendentes

- KAN-84 deve configurar proteção, merge queue, assinatura e política de force push.
- Definir identidade oficial do bot/IA, se existir, sem retroagir autoria.

