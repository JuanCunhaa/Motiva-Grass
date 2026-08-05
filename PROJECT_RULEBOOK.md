# Project Rulebook — Motiva Grass

**Status:** norma raiz  
**Escopo:** pessoas, agentes de IA e automações que atuem no projeto

Este arquivo define precedência e aponta para a única norma oficial de cada tema. Detalhes vivem nos documentos especializados do [índice oficial](docs/DOCUMENTATION_INDEX.md).

## Precedência

1. lei, obrigação regulatória e política organizacional aplicável;
2. decisão humana explícita, registrada e válida para o escopo;
3. este rulebook;
4. documento normativo especializado listado no índice;
5. ADR aceito dentro de sua decisão;
6. ticket Jira dentro de seu escopo de entrega;
7. PR, comentário e material de referência.

Uma regra mais específica prevalece sobre uma geral apenas se não contrariar nível superior. Data mais recente não corrige conflito por si só. Conflitos devem ser registrados no [relatório de conflitos](docs/governance/RULE_CONFLICT_REPORT.md); até a decisão, use a opção segura e reversível e pare a ação irreversível.

## Regras invariantes

- Execute um ticket principal por vez e mantenha Jira, branch, PR e evidência ligados por `KAN-N`.
- Não invente requisito, estado, medição, dado, resultado, teste ou aprovação.
- Não exponha segredo, dado pessoal, mídia privada, dataset restrito, peso de modelo ou saída identificável.
- Trabalho incompleto, inconclusivo ou não executado nunca é apresentado como aprovado.
- Alteração de comportamento exige teste proporcional ao risco e documentação no mesmo PR.
- Decisão transversal e duradoura exige ADR; exceção exige responsável, justificativa e validade.
- Produção, custo, credencial, licença, risco aceito, dado real, medição física e promoção de modelo respeitam gate humano.
- Artefatos de dados e ML são reproduzíveis, versionados e promovidos por identidade verificável; o conjunto de teste não orienta ajuste.

## Fontes oficiais

| Assunto | Fonte de verdade |
|---|---|
| Objetivo, responsável, prioridade, dependências e estado | Jira |
| Código, contrato, configuração e norma técnica | Git |
| Decisão arquitetural | ADR aceito |
| Revisão de mudança | PR e checks |
| Evidência de teste | execução imutável em CI/artefato, ligada ao PR e Jira |
| Aprovação humana | registro no sistema aplicável, sem segredo |

## Fluxo obrigatório

1. Leia `AGENTS.md`, KAN-1, épico, ticket, KAN-20, dependências e normas do domínio.
2. Confirme Definition of Ready, ausência de duplicidade e gates.
3. Registre início, mova o Jira apenas com atividade real e crie a branch padrão.
4. Implemente estritamente o escopo, com commits rastreáveis.
5. Execute a matriz de testes, guarde evidências e atualize documentação.
6. Abra PR, obtenha revisões/gates e só conclua com Definition of Done integral.

## Auditoria normativa e rastreabilidade Jira

| Área | Documento oficial | Regra principal | Validação automática | Ticket Jira |
|---|---|---|---|---|
| Governança de execução | `docs/governance/AI_EXECUTION_POLICY.md` | executar com escopo, evidência e interrupção segura | lint de referência Jira e checklist | KAN-20, KAN-21–23, KAN-80–84 |
| Jira | `docs/governance/JIRA_WORKFLOW_POLICY.md` | estado reflete realidade; bloqueio não é progresso | regras de transição e campos | KAN-20–23, KAN-80–84 |
| Desenvolvimento | `docs/development/DEVELOPMENT_METHOD.md` | incremento pequeno, revisável e rastreável | checks de branch/commit/PR | KAN-19, KAN-74, KAN-85–88 |
| Arquitetura | `docs/architecture/REPOSITORY_ARCHITECTURE.md` | fronteiras explícitas e dependências direcionadas | lint de imports e arquitetura | KAN-19, KAN-79, KAN-88 |
| Design | `docs/design/DESIGN_SYSTEM.md` | tokens e estados canônicos; nada ad hoc | visual regression, axe e lint | KAN-75, KAN-76, KAN-128–133 |
| Acessibilidade | `docs/design/ACCESSIBILITY_STANDARD.md` | WCAG 2.2 AA e operação por teclado | axe, contraste e testes E2E | KAN-75, KAN-132, KAN-146 |
| Testes | `docs/testing/TEST_STRATEGY.md` | pirâmide por risco; GPU indisponível não é aprovação | CI por camada e matriz | KAN-74, KAN-85–88, KAN-134–135, KAN-145–150 |
| Qualidade | `docs/testing/QUALITY_GATES.md` | gate falho ou ausente bloqueia promoção | status checks protegidos | KAN-85–88, KAN-127, KAN-143 |
| Segurança | `docs/security/SECURITY_STANDARD.md` | defesa em profundidade e menor privilégio | SAST, SCA, secrets e testes negativos | KAN-31, KAN-73, KAN-81, KAN-125–138, KAN-147 |
| Privacidade | `docs/security/PRIVACY_STANDARD.md` | minimizar, limitar finalidade e retenção | scan de fixtures/logs e checklist | KAN-31, KAN-86, KAN-136–138 |
| Dados | `docs/data/DATA_GOVERNANCE.md` | proveniência, licença, schema e versão obrigatórios | schema, checksum e política de repositório | KAN-31, KAN-66, KAN-120–122, KAN-139 |
| ML | `docs/ml/ML_DEVELOPMENT_STANDARD.md` | experimentos reproduzíveis, avaliação íntegra e promoção exata | validação de metadata, métricas e checksum | KAN-66, KAN-69, KAN-120–122, KAN-139–140, KAN-156 |
| Documentação | `docs/DOCUMENTATION_POLICY.md` | uma fonte canônica por regra e atualização no mesmo PR | links, headings e secret scan | KAN-19, KAN-20, KAN-79, KAN-88, KAN-144, KAN-151–152 |

Valores ainda sem decisão explícita estão marcados como propostos nos documentos especializados e não devem ser tratados como aprovação de negócio.
