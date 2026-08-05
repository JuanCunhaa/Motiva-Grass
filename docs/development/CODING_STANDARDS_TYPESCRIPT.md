# Padrões de Código TypeScript

## Decisão

Propor Node.js 24 LTS, TypeScript 6.x e pnpm com versões exatas fixadas em KAN-34. Usar TypeScript estrito, ESM, validação runtime nas fronteiras e arquitetura por features. Framework web permanece pendente.

## Justificativa

Node 24 está em LTS em 05/08/2026 e TypeScript 6 oferece defaults mais estritos; o roadmap exige build reproduzível, zero `any`, acessibilidade e contratos validados. A versão Python/ML não determina o frontend.

## Alternativas

- npm/yarn: válidos, mas pnpm é proposto por workspaces, instalação determinística e eficiência.
- Node 26 Current: não adotado antes de LTS.
- Framework React/Vue/Svelte/Next: decisão pendente de KAN-34/KAN-75; este padrão é agnóstico.

## Regras obrigatórias

- `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `useUnknownInCatchVariables`, `noImplicitOverride` e `noFallthroughCasesInSwitch` habilitados explicitamente.
- `any` proibido, inclusive casts e gerados não isolados. Entrada externa é `unknown` e validada por schema antes do uso.
- Tipos públicos são derivados dos contratos canônicos; não duplicar DTO manualmente.
- `null` representa ausência explícita do contrato; `undefined` representa argumento/campo TS opcional. Converter na fronteira e nunca usar truthiness para valores `0`, `false` ou string vazia válidos.
- Funções/componentes fazem uma tarefa; extrair quando misturam domínio, I/O e apresentação. Componente visual não contém regra de negócio nem chamada direta de API.
- Nomes: `camelCase` valores/funções, `PascalCase` tipos/componentes, `UPPER_SNAKE_CASE` constantes estáveis; booleanos `is/has/can/should`.
- Imports ordenados: plataforma, externos, aliases internos, relativos. Alias apenas para raízes públicas (`@web/*`, `@contracts/*`, `@ui/*`); não atravessar internals.
- Barrel files somente em API pública de pacote; proibidos internamente quando criam ciclos, side effects ou escondem dependências.
- Toda Promise é aguardada, retornada ou explicitamente tratada. Proibir floating promises e `new Promise` desnecessário.
- Operações canceláveis recebem `AbortSignal`; componentes cancelam fetch/timers no descarte. Timeout não é cancelamento.
- Erros tipados por código/categoria e `cause`; não lançar string nem exibir detalhes internos ao usuário.
- Configuração passa por módulo validado. Variável pública usa prefixo definido pelo bundler e nunca contém secret; secrets não entram no bundle.
- UI suporta `pt-BR` e `en` por chaves, sem texto de regra de negócio hardcoded. Datas/números via `Intl`.
- HTML semântico, teclado, foco, labels, contraste, live regions e preferência de movimento são requisitos; testes automatizados não substituem revisão manual.
- Testes: unitários para lógica pura, componentes para comportamento/acessibilidade, integração para cliente/contrato e E2E para jornadas. Evitar snapshot amplo.
- Comentário explica “por quê”, risco ou contrato; não repete código. API pública exportada recebe TSDoc quando uso/erro não for óbvio.

## Regras recomendadas

- Unions discriminadas para estados `idle/loading/success/inconclusive/error`.
- Imutabilidade por padrão; `readonly` em contratos.
- Limite indicativo: função 40 linhas, componente 150; exceder exige coesão clara.
- ESLint type-aware e formatter único, definidos em KAN-34.

## Exemplos

```ts
const parsed = AnalyzeResponseSchema.safeParse(value);
if (!parsed.success) throw new ContractError("CONTRACT_RESPONSE_INVALID", { cause: parsed.error });
return parsed.data;
```

Um componente `ResultCard` recebe `AnalyzeResult`; não conhece endpoint, nome de modelo ou retry.

## Anti-patterns

- `as any`, `as unknown as T`, non-null assertion para silenciar problema ou `catch {}`.
- Estado booleano impossível (`isLoading` e `hasError` simultâneos) em vez de union.
- Importar `src/internal` de outro pacote ou criar barrel global.
- Secret em `PUBLIC_*`, logar imagem/EXIF ou regra de domínio em JSX/template.

## Checklist

- [ ] Strict completo e zero `any`.
- [ ] Entradas `unknown` validadas e tipos derivados do contrato.
- [ ] Fronteiras/imports respeitados; sem ciclo/barrel perigoso.
- [ ] Promises, cancelamento e erros tipados.
- [ ] Config/secrets, i18n e acessibilidade corretos.
- [ ] Testes e TSDoc aplicáveis.

## Riscos

TypeScript 6 é recente; fixar versão e validar tooling. Schemas gerados podem perder expressividade; golden/contract tests devem detectar. Abstração de componentes prematura aumenta indirection.

## Pontos pendentes

- KAN-34 decide framework, bundler, test runner, ESLint/formatter e versão exata do pnpm.
- KAN-75/KAN-128 definem arquitetura visual e design system.
- Validar suporte do ecossistema escolhido a Node 24/TypeScript 6 antes de aceitar esta proposta.

## Referências externas

- [Calendário oficial de releases do Node.js](https://nodejs.org/en/about/previous-releases)
- [Release notes do TypeScript 6.0](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)
- [Documentação oficial do pnpm](https://pnpm.io/)
