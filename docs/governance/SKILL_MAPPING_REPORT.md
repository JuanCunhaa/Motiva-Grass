# Relatório final de mapeamento de Agent Skills

Data da análise: 2026-08-05. Escopo: KAN-1 a KAN-156, 41 skills públicas solicitadas, 16 skills próprias previstas e um wrapper local explícito. A auditoria foi estática: nenhum script público foi executado.

## 1. Resumo executivo

- 41/41 entradas públicas têm resultado registrado.
- 40/41 skills foram localizadas e baixadas para auditoria; `static-analysis` não existe como skill raiz no seletor solicitado.
- 37/41 foram vendoradas: 15 `APPROVED` e 22 `APPROVED_WITH_RESTRICTIONS`.
- 3 foram classificadas como `DISABLED`, 1 como `NOT_FOUND` e 0 como `REJECTED`.
- 0/16 skills próprias existiam no workspace; as 16 permanecem `planned` e não foram simuladas.
- Foi criado o wrapper local `motiva-web-guidelines-snapshot`, com snapshot, licença e proveniência próprios.
- KAN-1 a KAN-156 foram atualizados e relidos; 156/156 têm uma única seção de skills, 139/139 executáveis têm mapeamento detalhado e nenhuma descrição original foi perdida.
- Todos os itens permanecem em `Tarefas pendentes`. Títulos, prioridades, responsáveis, labels, links, flags e workflow não foram alterados.
- O repositório Git foi confirmado, a branch `chore/KAN-1-agent-skills-catalog` foi publicada e o PR [#89](https://github.com/JuanCunhaa/Motiva-Grass/pull/89) foi aberto contra `main` com commits semânticos.

## 2. Fontes utilizadas

| Fonte | Repositório | Conteúdo solicitado | Licença observada |
|---|---|---|---|
| `github-awesome-copilot` | `github/awesome-copilot` | 13 skills | MIT |
| `vercel-next-skills` | `vercel-labs/next-skills` | 2 skills históricas | Não identificada no commit histórico |
| `vercel-agent-skills` | `vercel-labs/agent-skills` | 3 skills | MIT |
| `trailofbits` | `trailofbits/skills` | 17 seletores | CC-BY-SA-4.0 |
| `huggingface` | `huggingface/skills` | 6 skills | Apache-2.0 |
| Wrapper local | `vercel-labs/web-interface-guidelines` | snapshot do comando público | licença preservada no wrapper |

As cópias aprovadas estão sob `vendor/agent-skills/`; proveniência, paths e hashes por arquivo estão em `config/skills/skills-lock.yaml`.

## 3. Commits fixados

| Fonte | Commit fixado | Observação |
|---|---|---|
| `github-awesome-copilot` | `940cf68164ea8a44d2e4d7cd9ce24c76eee56ed0` | HEAD selecionado e fixado |
| `vercel-next-skills` | `dc1de9caf7612d73f56a8dec3cb1bd6c9ec096b9` | último commit histórico contendo as duas skills; HEAD consultado `b76d687cf3e026eac3b1032f610f06b47a56377c` já não as contém |
| `vercel-agent-skills` | `7c180d9044c9ae2b442b567aad4e42a28dd5ed62` | HEAD selecionado e fixado |
| `trailofbits` | `9ea55c598763f7cb87ab56933d773d7dc34344a0` | HEAD selecionado e fixado |
| `huggingface` | `32f8bb0928e95fc9d47ca9fbf69cbfbaf2bc2bda` | HEAD selecionado e fixado |
| snapshot do wrapper | `4e799d45c17aec1498c269287a83b9dba22b966b` | `command.md` SHA-256 `fb9b73dd69cead884f29e8a6fb0adf53d525e65d4bf82c51f78f2c781638f2f1` |

## 4. 41 skills esperadas

| Skill | Fonte | Encontrada | Vendorada | Status |
|---|---|---:|---:|---|
| `agent-skill-stack` | GitHub | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `acquire-codebase-knowledge` | GitHub | sim | sim | `APPROVED` |
| `make-repo-contribution` | GitHub | sim | sim | `APPROVED` |
| `create-specification` | GitHub | sim | sim | `APPROVED` |
| `create-technical-spike` | GitHub | sim | sim | `APPROVED` |
| `agentic-eval` | GitHub | sim | sim | `APPROVED` |
| `security-review` | GitHub | sim | sim | `APPROVED` |
| `secret-scanning` | GitHub | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `dependabot` | GitHub | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `playwright-explore-website` | GitHub | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `playwright-generate-test` | GitHub | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `quality-playbook` | GitHub | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `screen-recording` | GitHub | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `next-best-practices` | Vercel Next | sim, histórica | não | `DISABLED` |
| `next-cache-components` | Vercel Next | sim, histórica | não | `DISABLED` |
| `vercel-react-best-practices` | Vercel Agent | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `web-design-guidelines` | Vercel Agent | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `vercel-optimize` | Vercel Agent | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `audit-context-building` | Trail of Bits | sim | sim | `APPROVED` |
| `differential-review` | Trail of Bits | sim | sim | `APPROVED` |
| `property-based-testing` | Trail of Bits | sim | sim | `APPROVED` |
| `dimensional-analysis` | Trail of Bits | sim | sim | `APPROVED` |
| `sharp-edges` | Trail of Bits | sim | sim | `APPROVED` |
| `insecure-defaults` | Trail of Bits | sim | sim | `APPROVED` |
| `supply-chain-risk-auditor` | Trail of Bits | sim | sim | `APPROVED` |
| `fp-check` | Trail of Bits | sim | sim | `APPROVED` |
| `variant-analysis` | Trail of Bits | sim | sim | `APPROVED` |
| `modern-python` | Trail of Bits | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `mutation-testing` | Trail of Bits | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `agentic-actions-auditor` | Trail of Bits | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `semgrep-rule-creator` | Trail of Bits | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `semgrep-rule-variant-creator` | Trail of Bits | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `second-opinion` | Trail of Bits | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `static-analysis` | Trail of Bits | não como skill raiz | não | `NOT_FOUND` |
| `skill-improver` | Trail of Bits | sim | não | `DISABLED` |
| `hf-cli` | Hugging Face | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `huggingface-datasets` | Hugging Face | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `huggingface-trackio` | Hugging Face | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `huggingface-vision-trainer` | Hugging Face | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `hf-mem` | Hugging Face | sim | sim | `APPROVED_WITH_RESTRICTIONS` |
| `huggingface-best` | Hugging Face | sim | sim | `APPROVED_WITH_RESTRICTIONS` |

## 5. Skills encontradas

Foram encontradas 40 skills reais nos commits fixados. As 37 classificadas como aprovadas ou aprovadas com restrições foram copiadas sem modificação para `vendor/agent-skills/`. As três encontradas mas não vendoradas são `next-best-practices`, `next-cache-components` e `skill-improver`.

## 6. Skills ausentes

`static-analysis` não existe como uma skill com `SKILL.md` raiz e frontmatter homônimo. O path solicitado é um plugin agregador com skills filhas (`codeql`, `sarif-parsing` e `semgrep`). Nenhuma filha foi substituída automaticamente.

Também não existiam no workspace as 16 skills próprias esperadas: `motiva-work-selector`, `motiva-jira-ticket-executor`, `motiva-ticket-orchestrator`, `motiva-repository-context`, `motiva-architecture-guard`, `motiva-dataset-governance`, `motiva-physical-data-gate`, `motiva-inference-contract`, `motiva-ml-experiment`, `motiva-ml-evaluation-gate`, `motiva-model-release-gate`, `motiva-design-system-guardian`, `motiva-security-privacy-gate`, `motiva-quality-gate`, `motiva-documentation-maintainer` e `motiva-release-manager`. Todas foram registradas como `planned`.

## 7. Auditoria

A auditoria estática inventariou frontmatter, paths, licenças, scripts, padrões destrutivos, rede, secrets e escrita potencial fora do projeto. O resultado detalhado está em `docs/governance/PUBLIC_SKILLS_AUDIT.md` e `reports/skills/audit-results.json`. O verificador conferiu 37 árvores vendoradas contra hashes por arquivo e detecta extras, ausências e alterações.

Resultados: 15 `APPROVED`, 22 `APPROVED_WITH_RESTRICTIONS`, 3 `DISABLED`, 1 `NOT_FOUND`, 0 `REJECTED`.

## 8. Restrições

- Skills com rede, instalação, automação de repositório, browser, gravação, publicação, GPU, recursos pagos ou acesso a produção são condicionais e preservam os gates do ticket.
- Material Trail of Bits mantém atribuição CC-BY-SA-4.0 e cópias vendoradas imutáveis.
- Skills Hugging Face não autorizam upload, publicação, alteração de Hub/Space, Job pago ou GPU paga.
- `modern-python` não autoriza instalar pacotes ou acessar a rede sem passo explícito.
- `quality-playbook` não autoriza limpeza destrutiva nem recuperação de Git.
- Nenhuma skill pública é ativada por padrão; a ativação materializa somente o subconjunto roteado e permitido.

## 9. Riscos

- A licença das duas skills históricas de `vercel-next-skills` não foi identificada.
- O seletor `static-analysis` é ambíguo e pode levar a uma substituição indevida por uma skill filha.
- `skill-improver` depende de `plugin-dev/skill-reviewer` ausente e prevê hooks automatizados de edição/revisão.
- Skills externas podem mudar comportamento upstream; por isso o update gera diff e exige nova auditoria, sem substituir automaticamente o vendor atual.
- As 16 skills próprias ainda são contratos planejados; até serem implementadas, as normas canônicas precisam ser aplicadas diretamente.
- O PR #89 ainda depende dos checks e da revisão aplicáveis antes de qualquer merge; este trabalho não antecipa aprovação nem conclusão de KAN-1.

## 10. Matriz por Épico

As linhas abaixo agregam os tickets filhos; o mapeamento ticket a ticket, justificativas, ordem, evidências e gates estão em `config/skills/jira-skill-routing.yaml`.

### Skills por Épico

| Épico | Skills próprias | Skills públicas | Tickets |
|---|---|---|---:|
| KAN-2 Governança | orquestração, Jira, documentação, contrato, qualidade, seleção | especificação, contribuição, property testing; condicionais de avaliação/segurança | 4 |
| KAN-3 Produto | orquestração, Jira, documentação, qualidade, release, contrato | especificação, contribuição, quality playbook, segurança, property testing | 4 |
| KAN-4 Pesquisa | orquestração, Jira, experimento ML, qualidade, documentação | spike, Python; condicionais Hugging Face e second opinion | 8 |
| KAN-5 Arquitetura | orquestração, Jira, arquitetura, dados, segurança, release de modelo | segurança, supply chain, contexto, especificação, Python, defaults | 8 |
| KAN-6 Fundação | orquestração, Jira, documentação, qualidade, design system, contrato | especificação, contribuição, Python, segurança; condicionais web | 4 |
| KAN-7 Coleta | orquestração, Jira, qualidade, dados físicos, contrato, segurança | análise dimensional, especificação, Python, segurança, property testing | 11 |
| KAN-8 Dataset | orquestração, Jira, qualidade, documentação, governança de dados, arquitetura | Python, segurança, supply chain; condicionais de dados | 11 |
| KAN-9 Geometria | orquestração, Jira, contrato, qualidade, documentação | Python, análise dimensional; condicionais de revisão | 5 |
| KAN-10 Baselines | orquestração, Jira, qualidade, experimento e avaliação ML | Python, property testing; condicionais Hugging Face | 9 |
| KAN-11 Multitarefa | orquestração, Jira, qualidade, experimento e avaliação ML | Python, property testing, agentic eval; condicionais Hugging Face | 11 |
| KAN-12 MoGe-2 | orquestração, Jira, qualidade, experimento e avaliação ML | Python, property testing; condicionais Hugging Face | 7 |
| KAN-13 Seleção ML | orquestração, Jira, qualidade, avaliação e release | Python, property testing, avaliação, quality playbook, segurança | 7 |
| KAN-14 API | orquestração, Jira, qualidade, contrato, segurança | segurança, Python, defaults, especificação, property testing, avaliação | 10 |
| KAN-15 Web | orquestração, Jira, design system, qualidade, documentação | contribuição, especificação; condicionais React, Playwright, gravação e wrapper | 11 |
| KAN-16 Operação | orquestração, Jira, documentação, qualidade, segurança, release de modelo, arquitetura | supply chain, secrets, segurança, especificação, contribuição, defaults | 17 |
| KAN-17 QA/release | qualidade, orquestração, Jira, documentação, release, segurança, dados, design e arquitetura | segurança, quality playbook, avaliação, defaults, Python, supply chain, contribuição, especificação | 12 |

## 11. Tickets atualizados

- Roadmap: KAN-1.
- Épicos: KAN-2 a KAN-17 (16/16).
- Executáveis: KAN-18 a KAN-156 (139/139).
- Total: 156/156, processados em lotes de no máximo 10 e relidos após cada lote.
- Marcadores: uma única seção normalizada entre `MOTIVA-SKILLS:INÍCIO` e `MOTIVA-SKILLS:FIM` por item.
- Comentários adicionados somente em KAN-1, KAN-20 e KAN-89.

## 12. Tickets não atualizados

Nenhum. O checkpoint final registra 156 sucessos, 0 falhas e 0 pendências. Não foi necessário criar `reports/skills/JIRA_UPDATE_PENDING.md` porque o Jira estava acessível.

## 13. Conflitos encontrados

- O HEAD de `vercel-labs/next-skills` já não contém as duas skills solicitadas; foi fixado o último commit histórico que as continha, sem ativá-las.
- `static-analysis` é nome de plugin agregador, não de skill raiz.
- `skill-improver` pressupõe uma dependência ausente e hooks incompatíveis com execução ordinária segura.
- Os marcadores retornam do conector Jira com colchetes escapados em Markdown; a validação normaliza essa representação sem alterar o conteúdo semântico.

## 14. Duplicidades

- Seções Jira duplicadas: 0/156.
- Skills públicas duplicadas no vendor: 0.
- O wrapper `motiva-web-guidelines-snapshot` possui namespace local e não substitui `web-design-guidelines`.
- Nenhuma skill pública bloqueada foi roteada como obrigatória ou condicional.

## 15. Lacunas

- As 16 skills próprias são planejadas e precisam de tickets separados de implementação e validação.
- `motiva-repository-context` é a única skill própria planejada sem associação atual; contexto foi coberto pontualmente por skills públicas e leitura direta das normas.
- Falta uma decisão humana de licença para as duas skills Next históricas.
- Falta decidir se `static-analysis` deve ser renomeada para uma filha específica ou removida do catálogo esperado.
- Falta disponibilizar/revisar a dependência de `skill-improver`, caso essa automação continue desejada.
- O PR #89 está aberto; checks, revisão e merge permanecem como gates normais do repositório.

## 16. Skills mais utilizadas

Contagem por ticket associado, unificando uso obrigatório e condicional: `motiva-ticket-orchestrator`, `motiva-jira-ticket-executor` e `motiva-documentation-maintainer` aparecem em 156 itens; `motiva-quality-gate` em 130; `modern-python` em 65; `agentic-eval` em 55; `property-based-testing` em 50; `create-specification` e `dimensional-analysis` em 45; `security-review` em 44; `make-repo-contribution` em 36.

### Cobertura das skills

| Skill | Tickets associados | Épicos | Status |
|---|---:|---:|---|
| `motiva-ticket-orchestrator` | 156 | 16 | `PLANNED` |
| `motiva-jira-ticket-executor` | 156 | 16 | `PLANNED` |
| `motiva-documentation-maintainer` | 156 | 16 | `PLANNED` |
| `motiva-quality-gate` | 130 | 16 | `PLANNED` |
| `modern-python` | 65 | 12 | `APPROVED_WITH_RESTRICTIONS` |
| `agentic-eval` | 55 | 16 | `APPROVED` |
| `property-based-testing` | 50 | 13 | `APPROVED` |
| `create-specification` | 45 | 16 | `APPROVED` |
| `dimensional-analysis` | 45 | 12 | `APPROVED` |
| `security-review` | 44 | 11 | `APPROVED` |
| `make-repo-contribution` | 36 | 16 | `APPROVED` |
| `huggingface-datasets` | 34 | 7 | `APPROVED_WITH_RESTRICTIONS` |
| `huggingface-trackio` | 32 | 5 | `APPROVED_WITH_RESTRICTIONS` |
| `motiva-ml-experiment` | 27 | 4 | `PLANNED` |
| `hf-mem` | 24 | 7 | `APPROVED_WITH_RESTRICTIONS` |
| `screen-recording` | 21 | 5 | `APPROVED_WITH_RESTRICTIONS` |
| `fp-check` | 20 | 6 | `APPROVED` |
| `huggingface-vision-trainer` | 20 | 4 | `APPROVED_WITH_RESTRICTIONS` |
| `insecure-defaults` | 20 | 7 | `APPROVED` |
| `motiva-work-selector` | 18 | 16 | `PLANNED` |
| `supply-chain-risk-auditor` | 18 | 4 | `APPROVED` |
| `motiva-inference-contract` | 17 | 6 | `PLANNED` |
| `motiva-design-system-guardian` | 15 | 3 | `PLANNED` |
| `motiva-security-privacy-gate` | 15 | 5 | `PLANNED` |
| `variant-analysis` | 15 | 5 | `APPROVED` |
| `vercel-react-best-practices` | 15 | 3 | `APPROVED_WITH_RESTRICTIONS` |
| `agentic-actions-auditor` | 14 | 4 | `APPROVED_WITH_RESTRICTIONS` |
| `differential-review` | 14 | 6 | `APPROVED` |
| `motiva-dataset-governance` | 14 | 3 | `PLANNED` |
| `motiva-ml-evaluation-gate` | 12 | 4 | `PLANNED` |
| `huggingface-best` | 11 | 3 | `APPROVED_WITH_RESTRICTIONS` |
| `playwright-generate-test` | 11 | 3 | `APPROVED_WITH_RESTRICTIONS` |
| `quality-playbook` | 10 | 5 | `APPROVED_WITH_RESTRICTIONS` |
| `audit-context-building` | 9 | 3 | `APPROVED` |
| `create-technical-spike` | 9 | 2 | `APPROVED` |
| `motiva-architecture-guard` | 9 | 4 | `PLANNED` |
| `sharp-edges` | 9 | 3 | `APPROVED` |
| `semgrep-rule-creator` | 8 | 5 | `APPROVED_WITH_RESTRICTIONS` |
| `semgrep-rule-variant-creator` | 8 | 5 | `APPROVED_WITH_RESTRICTIONS` |
| `dependabot` | 7 | 1 | `APPROVED_WITH_RESTRICTIONS` |
| `motiva-physical-data-gate` | 7 | 1 | `PLANNED` |
| `second-opinion` | 7 | 1 | `APPROVED_WITH_RESTRICTIONS` |
| `secret-scanning` | 7 | 1 | `APPROVED_WITH_RESTRICTIONS` |
| `playwright-explore-website` | 6 | 3 | `APPROVED_WITH_RESTRICTIONS` |
| `motiva-release-manager` | 5 | 3 | `PLANNED` |
| `motiva-web-guidelines-snapshot` | 5 | 3 | `LOCAL_WRAPPER` |
| `hf-cli` | 4 | 2 | `APPROVED_WITH_RESTRICTIONS` |
| `motiva-model-release-gate` | 4 | 2 | `PLANNED` |
| `vercel-optimize` | 4 | 4 | `APPROVED_WITH_RESTRICTIONS` |
| `acquire-codebase-knowledge` | 2 | 1 | `APPROVED` |

## 17. Skills sem utilização atual

Públicas sem associação: `agent-skill-stack`, `mutation-testing`, `web-design-guidelines`, `next-best-practices`, `next-cache-components`, `static-analysis` e `skill-improver`. As quatro últimas não são roteáveis ou exigem resolução prévia; as três primeiras permanecem disponíveis no catálogo para seleção futura baseada em ticket. Própria planejada sem associação: `motiva-repository-context`.

## 18. Recomendações

1. Implementar primeiro as skills próprias transversais: orquestração, executor Jira, manutenção documental e quality gate.
2. Tratar cada atualização pública em PR separado, com novo commit fixado, diff, auditoria e hashes.
3. Manter `vendor` imutável e usar wrappers/adapters locais para regras Motiva.
4. Ativar somente por perfil ou ticket; nunca copiar todas as skills para o runtime.
5. Resolver as quatro exceções sem substituições implícitas: licença Next, seletor `static-analysis` e dependência/hooks de `skill-improver`.
6. Revisar o PR #89, executar os checks aplicáveis e somente fazer merge após aprovação.

## 19. Gates humanos

- Licença: aprovar ou rejeitar formalmente o uso das duas skills históricas Next.
- Escopo: decidir qual skill filha, se alguma, representa `static-analysis`.
- Automação: aprovar dependência e comportamento de edição/revisão antes de habilitar `skill-improver`.
- Rede/custo/produção: aplicar gates já presentes nos tickets antes de uploads, publicação, GPU/Job pagos, recursos Vercel, configurações de repositório ou acesso a produção.
- Dados e ML: preservar gates de licença, dados reais restritos, medição física, promoção de modelo e release definidos nos tickets.
- Git remoto: revisão, checks e merge do PR #89 continuam sujeitos aos gates do repositório.

## 20. Próximos passos

1. Revisar o PR #89 (`[KAN-1] versionar e mapear Agent Skills`) e acompanhar seus checks.
2. Revisar e decidir as quatro entradas não roteáveis.
3. Criar tickets separados para as 16 skills próprias, começando pelas quatro transversais.
4. Executar `verify-public-skills.py` em CI e antes de qualquer ativação.
5. Usar `activate-public-skills.py --ticket KAN-N` ou um perfil explícito somente durante a execução real do ticket.
6. Manter KAN-1 aberto; esta entrega mapeia skills, mas não conclui o roadmap.

### Falhas

| Ticket | Falha | Impacto | Ação necessária |
|---|---|---|---|
| KAN-15 e tickets web relacionados | `next-best-practices` e `next-cache-components` sem licença identificada no commit histórico | Skills desativadas e não roteadas | Decisão humana de licença ou substituição auditada |
| Tickets de segurança/DevSecOps | `static-analysis` não existe como skill raiz | Nenhuma análise estática genérica foi roteada | Escolher e auditar explicitamente `codeql`, `sarif-parsing` ou `semgrep`, se aplicável |
| Governança de skills | `skill-improver` depende de componente ausente e hooks automatizados | Skill desativada | Revisar dependência, escopo e autorização de automação |
| Todos os tickets | 16 skills próprias não existiam | Contratos locais permanecem `planned` | Implementar e validar em tickets separados; aplicar normas diretamente até lá |

### Versionamento Git

| Commit | Mensagem |
|---|---|
| `0fc23f0a7a332f2e041e9a3f03e0323dfb47afaf` | `chore(skills): vendor audited public catalog [KAN-1]` |
| `a43b141e6777e2208d1bdb412857b185cfe31803` | `feat(skills): add governance automation [KAN-1]` |
| `2954bd990b941aea867294b3db8e0b37ee3615fa` | `docs(skills): map Jira skill routing [KAN-1]` |

Branch publicada: `chore/KAN-1-agent-skills-catalog`. Pull Request: [#89](https://github.com/JuanCunhaa/Motiva-Grass/pull/89).
