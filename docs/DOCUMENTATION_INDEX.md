# Índice oficial de documentação

Este é o catálogo canônico. `PROJECT_RULEBOOK.md` define precedência; `docs/DOCUMENTATION_POLICY.md` define manutenção.

## Comece aqui

- [Rulebook do projeto](../PROJECT_RULEBOOK.md)
- [Guia operacional para agentes](../AGENTS.md)
- [Como contribuir](../CONTRIBUTING.md)
- [Política de documentação](DOCUMENTATION_POLICY.md)
- [Templates](DOCUMENT_TEMPLATES.md)

## Governança e execução

- [Governança](governance/README.md)
- [Política de execução por IA](governance/AI_EXECUTION_POLICY.md)
- [Workflow Jira](governance/JIRA_WORKFLOW_POLICY.md)
- [Campos e labels Jira](governance/JIRA_FIELDS_AND_LABELS.md)
- [Comentários e evidências Jira](governance/JIRA_COMMENT_TEMPLATES.md)
- [Gates humanos](governance/HUMAN_GATES_POLICY.md)
- [Interrupção e escalação](governance/AI_EXECUTION_POLICY.md)
- [Definition of Ready](governance/DEFINITION_OF_READY.md)
- [Definition of Done](governance/DEFINITION_OF_DONE.md)
- [Gestão de bugs](governance/BUG_MANAGEMENT_POLICY.md)
- [Rastreabilidade](governance/TRACEABILITY_POLICY.md)
- [Resolução de conflitos](governance/RULE_CONFLICT_REPORT.md)
- [Oportunidades de automação](governance/AUTOMATION_OPPORTUNITIES.md)
- [Recomendações específicas de automação Jira](governance/JIRA_AUTOMATION_RECOMMENDATIONS.md)
- [Inconsistências do backlog](governance/BACKLOG_INCONSISTENCY_REPORT.md)
- [Mudanças propostas para KAN-20](governance/KAN_20_PROPOSED_CHANGES.md)
- [Auditoria de skills públicas](governance/PUBLIC_SKILLS_AUDIT.md)
- [Versionamento de skills públicas](governance/PUBLIC_SKILLS_VERSIONING.md)
- [Decisão de arquitetura de skills](governance/SKILL_ARCHITECTURE_DECISION.md)
- [Matriz Jira × skills](governance/JIRA_SKILL_ROUTING_MATRIX.md)
- [Matriz de avaliação das skills](governance/SKILL_EVALUATION_MATRIX.md)
- [Relatório final de implementação das skills](governance/SKILL_IMPLEMENTATION_REPORT.md)
- [Relatório histórico de mapeamento público](governance/SKILL_MAPPING_REPORT.md)

## Desenvolvimento e arquitetura

- [Método de desenvolvimento](development/DEVELOPMENT_METHOD.md)
- [Workflow Git](development/GIT_WORKFLOW.md)
- [Padrão de pull request](development/PULL_REQUEST_STANDARD.md)
- [TypeScript](development/CODING_STANDARDS_TYPESCRIPT.md)
- [Python](development/CODING_STANDARDS_PYTHON.md)
- [Contratos e schemas](development/CONTRACTS_AND_SCHEMAS.md)
- [Erros e logs](development/ERROR_AND_LOGGING_STANDARD.md)
- [Dependências](development/DEPENDENCY_MANAGEMENT.md)
- [Arquitetura do repositório](architecture/REPOSITORY_ARCHITECTURE.md)
- [Estrutura de pastas](architecture/FOLDER_STRUCTURE.md)
- [ADR 0001](architecture/adr/0001-repository-architecture.md)

## Design e experiência

- [Design system](design/DESIGN_SYSTEM.md)
- [Tokens](design/DESIGN_TOKENS.md)
- [Componentes](design/COMPONENT_GUIDELINES.md)
- [Fluxo de análise](design/UX_ANALYSIS_FLOW.md)
- [Acessibilidade](design/ACCESSIBILITY_STANDARD.md)
- [Conteúdo e tom](design/CONTENT_AND_TONE_GUIDE.md)

## Testes e qualidade

- [Estratégia](testing/TEST_STRATEGY.md)
- [Quality gates](testing/QUALITY_GATES.md)
- [Matriz de testes](testing/TEST_MATRIX.md)
- [Dados de teste](testing/TEST_DATA_POLICY.md)
- [Evidências](testing/TEST_EVIDENCE_STANDARD.md)

## Segurança e privacidade

- [Padrão de segurança](security/SECURITY_STANDARD.md)
- [Privacidade](security/PRIVACY_STANDARD.md)
- [Testes de segurança](security/SECURITY_TESTING.md)
- [Gestão de vulnerabilidades](security/VULNERABILITY_MANAGEMENT.md)
- [Threat model](security/THREAT_MODEL.md)
- [Aceitação de risco](security/RISK_ACCEPTANCE_TEMPLATE.md)

## Dados e machine learning

- [Governança de dados](data/DATA_GOVERNANCE.md)
- [Versionamento de datasets](data/DATASET_VERSIONING.md)
- [Template de Data Card](data/DATA_CARD_TEMPLATE.md)
- [Desenvolvimento de ML](ml/ML_DEVELOPMENT_STANDARD.md)
- [Experimentos](ml/EXPERIMENT_TRACKING_STANDARD.md)
- [Avaliação](ml/MODEL_EVALUATION_STANDARD.md)
- [Template de Model Card](ml/MODEL_CARD_TEMPLATE.md)
- [Release e rollback de modelo](ml/MODEL_RELEASE_AND_ROLLBACK.md)
- [Monitoramento](ml/MODEL_MONITORING.md)

## Templates e registros

Use [templates documentais](DOCUMENT_TEMPLATES.md). Data Cards e Model Cards usam exclusivamente os templates canônicos listados acima. Novas áreas (`product/`, `api/`, `computer-vision/`, `operations/` e `release/`) devem ser catalogadas aqui quando receberem documentos oficiais.

### Prompts operacionais

- [Executar ticket](prompt/execute.md)
- [Revisar e finalizar ticket](prompt/revisao.md)
- [Corrigir findings](prompt/correcao.md)
- [Retomar ticket bloqueado](prompt/bloqueado.md)

## Documentos históricos ou de apoio

- [Estrutura documental proposta no Prompt 2](DOCUMENTATION_STRUCTURE.md) — referência arquitetural; esta página e a política atual prevalecem em matéria normativa.
