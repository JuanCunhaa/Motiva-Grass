# Estrutura da Documentação

> **Status:** referência arquitetural originada no Prompt 2. Para regras vigentes e catálogo canônico, prevalecem `docs/DOCUMENTATION_POLICY.md` e `docs/DOCUMENTATION_INDEX.md`.

## Decisão

Documentação técnica normativa vive em Git, organizada por domínio, com índice, owner, status e revisão no mesmo PR da mudança. Confluence pode publicar links/resumos, sem segunda cópia normativa.

```text
docs/
├── README.md
├── governance/
├── development/
├── architecture/adr/
├── product/
├── design/
├── api/
├── data/
├── ml/
├── security/
├── testing/
├── operations/
└── release/
```

## Justificativa

Evita conhecimento apenas em IA/Jira/Confluence e permite review, links, histórico e validação automática junto do código.

## Alternativas

- Confluence normativo: rejeitado por drift com Git.
- Docs somente no Jira: útil temporariamente, inadequado para API/ADR/schema.
- Wiki gerada de docs Git: recomendada como publicação, não fonte.

## Regras obrigatórias

- Título H1 único, nome descritivo em `UPPER_SNAKE_CASE.md` para normas e `NNNN-kebab-case.md` para ADRs.
- Cada área possui `README.md` com índice, owner lógico, status e links. Documento registra `Proposed/Accepted/Deprecated/Superseded` quando decisório.
- Links relativos dentro do repo; links externos apontam à fonte primária. Não usar caminhos locais.
- Atualização acompanha o PR que altera comportamento. Reviewer técnico e owner documental aplicável aprovam.
- Documento obsoleto recebe banner com substituto/data; não apagar histórico. Arquivar somente material não normativo em `docs/archive/` com índice.
- CI valida Markdown, links internos, anchors, diagramas e exemplos/schemas quando executáveis.
- Alteração de API atualiza OpenAPI/exemplos; arquitetura, ADR/diagramas; dados, schemas/Data Card; ML, Model Card/métricas; segurança, threat model; operação, runbook; release, notas/checksums/rollback; UI, design/a11y/i18n.
- Jira aponta para documento; documento/ADR aponta para ticket/PR. Conversa não é documentação.

## Regras recomendadas

- Frases curtas, exemplos reproduzíveis, datas ISO e glossário comum.
- Gerar site estático a partir do Git quando necessário.
- Revisão semestral de normas e pós-incidente de runbooks.

## Exemplos

- ADR superseded mantém arquivo e link para novo ADR.
- Model Card referencia artefato/checksum e não copia peso.

## Anti-patterns

- `final_v2.md`, documento sem owner, link `C:\...`, screenshot como única especificação ou cópia divergente no Confluence.
- Atualizar comportamento sem docs porque “o código é autoexplicativo”.

## Checklist

- [ ] Local/título/status/owner corretos.
- [ ] Conteúdo e exemplos correspondem à entrega.
- [ ] Links relativos e Jira/PR/ADR rastreáveis.
- [ ] Documento substituído/deprecated tratado.
- [ ] Lint/link/schema checks aprovados.

## Riscos

Documentação pode ficar pesada ou desatualizada; matriz por tipo e checks reduzem. Informações sensíveis não devem entrar no Git.

## Pontos pendentes

- Escolher gerador/site e checker de links em KAN-35/KAN-134.
- Nomear owners/CODEOWNERS em KAN-84.

## Matriz final de regras

| Regra | Documento oficial | Ticket Jira | Validação automática | Gate humano |
|---|---|---|---|---|
| Um ticket por branch | `DEVELOPMENT_METHOD.md` | KAN-20 | nome branch/PR check | Não |
| Branch `tipo/KAN-N-*` | `GIT_WORKFLOW.md` | KAN-20, KAN-84 | regex CI | Não |
| Conventional Commit + Jira | `GIT_WORKFLOW.md` | KAN-20, KAN-84 | commitlint | Não |
| PR obrigatório/template | `PULL_REQUEST_STANDARD.md` | KAN-19, KAN-84 | PR lint/validator | Revisão humana |
| Limites de ticket/PR | `DEVELOPMENT_METHOD.md` | KAN-20 | alerta de LOC/arquivos | Exceção acima do limite |
| Monorepo modular | `REPOSITORY_ARCHITECTURE.md`, ADR-0001 | KAN-28, KAN-32 | architecture tests | Aprovação do ADR |
| Web não conhece modelo | `REPOSITORY_ARCHITECTURE.md` | KAN-28, KAN-75 | import/dependency rules | Não |
| API não importa treino | `REPOSITORY_ARCHITECTURE.md` | KAN-28, KAN-30 | import test | Não |
| Domínio sem framework | `REPOSITORY_ARCHITECTURE.md` | KAN-28, KAN-123 | import test | Não |
| Pesos/dados reais fora do Git | `FOLDER_STRUCTURE.md` | KAN-29, KAN-35 | tamanho/extensão/secret checks | Acesso a storage |
| TypeScript estrito/zero any | `CODING_STANDARDS_TYPESCRIPT.md` | KAN-34 | tsc/lint | Não |
| Python tipado/Ruff/mypy | `CODING_STANDARDS_PYTHON.md` | KAN-33 | lint/typecheck | Não |
| Contrato canônico/versionado | `CONTRACTS_AND_SCHEMAS.md` | KAN-90, KAN-70 | schema/golden/consumer tests | Breaking change |
| Runtime validation | `CONTRACTS_AND_SCHEMAS.md` | KAN-70, KAN-124 | contract tests | Não |
| Config startup/default seguro | `REPOSITORY_ARCHITECTURE.md` | KAN-83 | config/startup tests | Secret/produção/custo |
| Erros tipados/fallback visível | `ERROR_AND_LOGGING_STANDARD.md` | KAN-96, KAN-126 | unit/contract tests | Aceite de risco |
| Logs estruturados/redaction | `ERROR_AND_LOGGING_STANDARD.md` | KAN-31, KAN-126 | log schema/redaction tests | Retenção/privacidade |
| Lockfiles imutáveis em CI | `DEPENDENCY_MANAGEMENT.md` | KAN-33, KAN-34 | frozen/locked install | Não |
| Licença/CVE/SBOM | `DEPENDENCY_MANAGEMENT.md` | KAN-27, KAN-81, KAN-138 | scanners/SBOM check | Exceção/aceite de risco |
| ADR para decisão arquitetural | ADR template/`architecture/adr` | KAN-28, KAN-95, KAN-97 | metadata/link check | Aprovação decisores |
| Docs junto da entrega | `DOCUMENTATION_STRUCTURE.md` | KAN-20, KAN-35 | Markdown/link check | Não |
| Feature flag com remoção | `DEVELOPMENT_METHOD.md` | ticket da feature | flag inventory/expiry alert | Produção quando aplicável |
| Release exata/rollback | governance + release docs | KAN-151, KAN-152 | checksum/tag/checks | Obrigatório |
