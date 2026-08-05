# Gerenciamento de Dependências

## Decisão

Propor pnpm para JavaScript/TypeScript e uv para Python, com versões do gerenciador fixadas, `pnpm-lock.yaml` e `uv.lock` commitados, atualizações automatizadas em PRs pequenos, auditoria de licença/vulnerabilidade e SBOM por release.

## Justificativa

O monorepo precisa de resolução reproduzível em Windows/Linux, grupos CPU/GPU e visibilidade de supply chain. Lockfiles são artefatos de produção, não ruído.

## Alternativas

- npm/yarn e Poetry/pip-tools: possíveis se KAN-33/34 encontrar incompatibilidade comprovada.
- Dependências flutuantes sem lock: proibidas.
- Vendor de biblioteca: somente exceção de segurança/licença documentada.

## Regras obrigatórias

- Pin exato do gerenciador e runtimes; CI falha se lock estiver desatualizado (`--frozen-lockfile`/`uv --locked`).
- Dependência direta só com uso explícito, owner, licença, manutenção, origem e alternativa avaliados. Não adicionar dependência para função trivial sem justificar.
- Dependências transitivas são controladas pelo lock; override/resolution exige comentário, ticket, teste e expiração.
- Aplicações usam constraints compatíveis no manifest e resolução exata no lock. Ferramentas, geradores e stack ML/CUDA são fixados exatamente quando reprodução exigir.
- Separar produção, desenvolvimento, CPU, GPU e extras opcionais; pacote base não instala GPU nem baixa artefato.
- Atualização em PR próprio ou escopo claro, com changelog, testes, diff de lock, licença e vulnerabilidades. Major exige ticket/ADR quando impacto arquitetural.
- Git dependency usa tag/commit imutável e licença auditada; branch/URL arbitrária proibida. Registry privado exige configuração segura, nunca secret no arquivo.
- Vulnerabilidade crítica/alta conforme política bloqueia merge/release salvo exceção formal com owner, mitigação e validade. Não alegar que transitiva é irrelevante sem reachability/análise.
- Licenças permitidas/bloqueadas são definidas em KAN-27/KAN-81. Código, pesos e dados têm auditorias separadas.
- Biblioteca abandonada: congelar upgrade, avaliar risco, fork controlado ou substituição com ticket; não substituir silenciosamente.
- Gerar SBOM CycloneDX/SPDX de JS, Python e artefato/release; assinar/armazenar com checksums quando possível.
- Ferramentas dev também são fixadas e auditadas porque executam no CI.

## Regras recomendadas

- Automação semanal agrupada apenas por ecossistema compatível; atualizações críticas imediatas.
- `minimumReleaseAge`/janela de maturação quando suportado, com exceção para correção urgente revisada.
- Revisão trimestral de dependências centrais e EOL dos runtimes.
- Exportar SBOM do uv/pnpm com ferramenta aprovada e validar conteúdo.

## Exemplos

- Upgrade de validador em PR `chore(deps)` com golden/contract tests.
- Wheel CUDA usa índice e versão explícitos em grupo GPU, sem afetar instalação CPU.

## Anti-patterns

- Editar lock manualmente, rodar update global junto de feature ou ignorar CVE sem prazo.
- Pacote sem licença, abandonado ou copiado de notebook sem proveniência.
- Dois lockfiles concorrentes para a mesma resolução sem motivo.

## Checklist

- [ ] Manager/runtime e lock exatos.
- [ ] Dependência necessária, mantida, licenciada e com owner.
- [ ] Grupos CPU/GPU/dev/prod corretos.
- [ ] PR de update com testes, lock diff, licença e CVE.
- [ ] Exceções têm mitigação e expiração.
- [ ] SBOM/release inclui JS, Python e artefatos aplicáveis.

## Riscos

Lock universal pode não capturar incompatibilidade CUDA/OS; matriz de CI e manifests por capability mitigam. Automação excessiva gera ruído; limitar tamanho/frequência.

## Pontos pendentes

- KAN-27 define allow/deny de licenças; KAN-33/34 aprovam managers e versões.
- KAN-81/KAN-138 definem scanners e formato final do SBOM.

## Referências externas

- [Lock e sincronização no uv](https://docs.astral.sh/uv/concepts/projects/sync/)
- [Exportação de SBOM pelo uv](https://docs.astral.sh/uv/concepts/projects/export/)
- [Workspaces e gerenciador pnpm](https://pnpm.io/)
