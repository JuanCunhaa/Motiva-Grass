# Estrutura de Pastas

## Decisão

Adotar, após aprovação de KAN-28/KAN-32, a estrutura proposta abaixo. Nesta tarefa apenas a documentação é criada; pastas de aplicação não são scaffoldadas.

```text
/
├── apps/{web,api}/
├── packages/{contracts,config,ui,observability,test-utils}/
├── ml/{domain,validation,image,geometry,orchestration,inference,training,evaluation,datasets,registry}/
├── data/{schemas,manifests,fixtures,validation}/
├── infra/
├── scripts/
├── tests/{contract,integration,e2e,performance}/
├── docs/
├── tools/
└── .github/
```

## Justificativa

Mantém deployables, bibliotecas, pipeline ML, metadados de dados, operação e documentação visíveis, sem multiplicar repositórios ou pacotes Python prematuramente.

## Alternativas

- `src/` único: simples, mas obscurece fronteiras polyglot.
- Um pacote por módulo ML: adiar até versionamento/deploy independente.
- `services/` em vez de `apps/`: sem necessidade de microserviços no MVP.

## Regras obrigatórias

### Matriz de pastas

| Pasta | Responsabilidade / permitido | Proibido | Dependências e API exposta | Testes / owner / versão |
|---|---|---|---|---|
| `apps/web` | UI, rotas, features, i18n, cliente HTTP | regra ML, secret, acesso interno API | usa `contracts`, `config`, `ui`, `observability`; expõe bundle web | component/E2E; Frontend; versão da aplicação |
| `apps/api` | HTTP, upload, auth futura, composition root | treino, dataset, domínio duplicado | usa contracts e API pública de orchestration; expõe OpenAPI/health | integração/contrato; Backend; versão API |
| `packages/contracts` | schemas vN, OpenAPI, golden, gerados | regra, I/O, tipo manual divergente | não depende de app; expõe schemas/tipos gerados | contract/generation; Architecture; SemVer de contrato |
| `packages/config` | schemas/config TS e defaults seguros | secret/valor de ambiente real | depende só de contracts quando necessário; expõe config validada | unit/startup; Platform; versão junto ao repo |
| `packages/ui` | tokens/componentes visuais acessíveis | chamada API e regra de negócio | usa tipos UI estáveis; expõe componentes públicos | component/a11y; Frontend/Design; changeset quando publicado |
| `packages/observability` | eventos/ports TS e redaction | sink/credencial/payload sensível | sem app internals; expõe logger/telemetry interfaces | unit/redaction; Platform/Security; versão junto ao repo |
| `packages/test-utils` | builders/fixtures sintéticas | código de produção/dado real | somente dependência de teste; sem export runtime | self-tests; QA; versão junto ao repo |
| `ml/domain` | value objects, unidades, erros, ports | framework HTTP/ML/storage | stdlib/core controlado; API Python pública | unit/property; ML Architecture; SemVer interno |
| `ml/validation` | schemas/validação runtime | HTTP e coerção silenciosa | domain/contracts; expõe validators | unit/golden; Backend/ML |
| `ml/image` | MIME, EXIF, qualidade, preprocessing | rede/storage concreto | domain/validation; funções determinísticas | unit/property/fixtures; CV |
| `ml/geometry` | marcador, pose, escala, plano | API/treino/orquestração | domain/image; API matemática tipada | unit/property/benchmark; CV |
| `ml/orchestration` | use cases, ordem, fallbacks | framework HTTP/adapters concretos | domain/image/geometry/inference ports; expõe `AnalyzeUseCase` | unit com fakes/integration; Backend+ML |
| `ml/inference` | carregamento, inferência, calibração | treino/download implícito | domain/registry ports; expõe runtime | smoke CPU/GPU/equivalência; ML Runtime |
| `ml/training` | loop, losses, checkpoint, CLI | import por API/runtime, test set | domain/datasets + libs aprovadas; expõe CLI | dry-run/regressão; ML Training |
| `ml/evaluation` | métricas, slices, calibração | treino/promoção automática | domain/datasets e artefatos imutáveis; expõe CLI/report | golden/statistical; ML Validation |
| `ml/datasets` | adapters, transforms, splits/manifests | bytes reais no Git, leakage | data schemas + storage ports; expõe dataset API | unit/integration externo opcional; Data |
| `ml/registry` | interfaces/adapters de artefato e checksum | peso no Git, promoção implícita | domain/config; expõe refs/loaders | fake/integration; MLOps |
| `data` | schemas, manifests pequenos, fixtures sintéticas, validators | dataset real, imagem privada, secret | não importa apps; APIs são schemas/CLI | schema/checksum; Data Governance; versão de schema/dataset |
| `infra` | IaC, deploy, policies, env templates | segredo, lógica de domínio | pode referir artefatos/apps; app nunca importa infra | validate/plan/policy; Platform/Security; módulos versionados |
| `scripts` | wrappers curtos e portáveis | lógica única sem testes | chamam CLIs públicas; não internals | smoke; Platform; junto ao repo |
| `tests` | cenários cruzados | lógica reutilizada pela produção | consome APIs públicas | QA; fixtures sanitizadas; junto ao release |
| `docs` | normas, ADRs, API, dados, ML, operação | secret/cópia normativa divergente | links estáveis; expõe conhecimento versionado | link/lint; owners por área; revisão/versionamento Git |
| `tools` | geradores, architecture checks, release tooling | feature do produto | usa APIs públicas e manifests | unit/snapshot; Developer Experience; pinado |
| `.github` | workflows, templates, CODEOWNERS | lógica não reproduzível localmente | chama scripts/tools; não contém secret | actionlint/dry-run; DevSecOps; revisão protegida |

Imports públicos passam por entry points declarados, não por caminhos `internal`. Ciclos são proibidos. Conteúdo gerado fica em subpasta `generated` com comando e hash; não misturar com fonte manual.

## Regras recomendadas

- README/owner em cada pasta raiz.
- Arquivos próximos aos testes unitários; testes cruzados em `/tests`.
- Dividir módulo somente após coesão/ownership/deploy exigir.

## Exemplos

- `apps/api` instancia adapter de registry e injeta no `AnalyzeUseCase`.
- Fixture JPEG sintética pequena vive em `data/fixtures`; coleta real vive fora do Git.

## Anti-patterns

- `common/` genérico, `utils.py` ilimitado, imports relativos atravessando módulos ou código de produto em `scripts`.
- Gerado editado manualmente; docs sem owner; infra importada pela aplicação.

## Checklist

- [ ] Conteúdo está na pasta responsável e permitido.
- [ ] Dependências/API pública respeitadas; sem ciclo/internal import.
- [ ] Teste no nível correto e owner identificado.
- [ ] Dados/pesos/secrets/gerados tratados corretamente.
- [ ] Regra de versionamento aplicada.

## Riscos

Muitos diretórios vazios geram arquitetura teatral; criar somente no ticket que entrega conteúdo. `ml` pode crescer; separar packages depois, via ADR.

## Pontos pendentes

- KAN-32 deve validar estrutura física e tooling de import rules.
- Definir nomes finais de pacotes Python/TS após escolha de frameworks/build.

