# Relatório de conflitos e consolidação normativa

**Data da auditoria:** 2026-08-05  
**Escopo:** documentação dos Prompts 1, 2 e 3 e tickets KAN-18 a KAN-156  
**Natureza:** registro de resolução; não substitui as normas especializadas

## Resultado executivo

As áreas solicitadas possuem cobertura em tickets existentes. Não foi identificado tema que justifique novo ticket: a ação correta é atualizar os tickets mapeados com links, critérios e decisões. A consolidação criou uma fonte canônica por assunto e reclassificou `docs/DOCUMENTATION_STRUCTURE.md` como referência arquitetural.

Não houve alteração de ticket Jira nesta etapa. O Confluence não pôde ser consultado porque a integração disponível retornou `403`; KAN-89 já rastreia esse bloqueio. A auditoria, portanto, prova ausência de duplicidade dentro do backlog Jira KAN-18–156 e do repositório, não dentro de conteúdo inacessível do Confluence.

## Conflitos e resoluções

| Tema | Formulações concorrentes ou ambíguas | Resolução canônica | Estado |
|---|---|---|---|
| Jira versus Git/Confluence | processo e documentação poderiam existir em mais de um sistema | Jira governa trabalho; Git governa normas; Confluence só referencia | resolvido |
| Workflow de quatro ou seis estados | materiais antigos mencionam estados não disponíveis | somente os quatro estados reais de `JIRA_WORKFLOW_POLICY.md` | resolvido |
| Prioridade | prioridade nativa poderia divergir de `priority-p*` | ordem operacional usa labels `priority-p0/p1/p2`; divergência deve ser corrigida, não interpretada | resolvido |
| Links `Blocks` | uso histórico pode inverter causa e efeito | validar semântica pelo texto e registrar correção; não transicionar automaticamente com link ambíguo | mitigado; limpeza Jira pendente |
| Evidência no Jira ou PR | cópias extensas poderiam divergir | artefato imutável em CI/PR; Jira contém síntese e link | resolvido |
| Documento global ou especializado | rulebook, AGENTS e normas repetiam detalhes | rulebook define precedência; AGENTS resume; especializado é canônico no domínio | resolvido |
| Estrutura documental | `DOCUMENTATION_STRUCTURE.md` competia com nova política/índice | arquivo antigo é referência; `DOCUMENTATION_POLICY.md` e `DOCUMENTATION_INDEX.md` prevalecem | resolvido |
| Automação Jira ou geral | recomendações poderiam ser duplicadas | este relatório global cataloga; `JIRA_AUTOMATION_RECOMMENDATIONS.md` detalha Jira | resolvido |
| Alvo de toque 24 ou 44 px | conformidade mínima e boa usabilidade pareciam conflitar | 24×24 CSS px é mínimo WCAG; 44×44 é alvo recomendado do produto | resolvido |
| Cobertura de testes | percentuais não constam como decisão de negócio no backlog | valores de `QUALITY_GATES.md` permanecem propostos até ratificação | decisão pendente |
| SLA de vulnerabilidade | prazos operacionais não têm owner/aceite confirmado | valores de `VULNERABILITY_MANAGEMENT.md` permanecem propostos | decisão pendente |
| Runtime e ferramentas | versões Python/Node e stack podem ser apenas hipóteses | ADR e lockfiles futuros serão fonte; não presumir stack | decisão pendente |
| Métricas de ML | tickets pedem qualidade, mas não fecham todos os limiares | `MODEL_EVALUATION_STANDARD.md` define método; threshold exige decisão registrada | decisão pendente |

## Cobertura comprovada no Jira

| Tema | Tickets existentes a atualizar ou referenciar |
|---|---|
| Design, UX e acessibilidade | KAN-75, KAN-76, KAN-78, KAN-128–133, KAN-146, KAN-148 |
| Testes e qualidade | KAN-74, KAN-85–88, KAN-127, KAN-132, KAN-134–135, KAN-143, KAN-145–150 |
| Segurança e privacidade | KAN-31, KAN-73, KAN-81, KAN-86, KAN-125–126, KAN-133, KAN-136–138, KAN-147 |
| Dados e ML/MLOps | KAN-31, KAN-66, KAN-69, KAN-120–122, KAN-139–140, KAN-156 |
| Documentação, rastreabilidade e release | KAN-19, KAN-20, KAN-79, KAN-88, KAN-107, KAN-144, KAN-148, KAN-151–152 |

### Tickets novos realmente necessários

Nenhum. Criar tickets agora duplicaria escopos comprovadamente existentes. Caso a atualização revele critério executável que não caiba nos tickets listados, uma nova busca de duplicidade é obrigatória antes da criação.

## Gates humanos consolidados

| Gate | Tickets de referência | Evidência mínima |
|---|---|---|
| Privacidade, licença e dado real | KAN-31, KAN-86, KAN-136–139 | decisão, finalidade, base/licença, retenção e escopo |
| Mudança de teste/aceite e limitações | KAN-66, KAN-69 | aceite explícito dos critérios e limitações |
| Custo, credencial e administração | KAN-81, KAN-83–84, KAN-135 | aprovador, teto/escopo e confirmação sem segredo |
| Produção e aceite de risco | KAN-86, KAN-140–142 | risco residual, rollback, janela e owner |
| Dispositivo ou medição física | KAN-146 | executor, protocolo, ambiente e evidência |
| Release | KAN-151–152 | checklist GO/NO-GO, aprovadores e artefato exato |

## Decisões ainda pendentes

- owners nominais de design, segurança, dados, ML, qualidade e documentação;
- stack, frameworks, versões de runtime e serviços de armazenamento/observabilidade;
- limites de upload, formatos finais, retenção e jurisdição de privacidade;
- fonte tipográfica, necessidade de tema claro e dispositivos oficialmente suportados;
- thresholds de cobertura, flakiness, performance, acessibilidade e vulnerabilidade;
- taxonomias, unidades, datasets licenciados, splits oficiais e métricas/limiares de ML;
- infraestrutura GPU, orçamento, promoção de modelo e rollback em produção;
- canal e SLA de resposta a vulnerabilidade/incidente.

## Inventário desta consolidação

### Arquivos adicionados

```text
PROJECT_RULEBOOK.md
CONTRIBUTING.md
docs/README.md
docs/DOCUMENTATION_POLICY.md
docs/DOCUMENTATION_INDEX.md
docs/DOCUMENT_TEMPLATES.md
docs/design/DESIGN_SYSTEM.md
docs/design/DESIGN_TOKENS.md
docs/design/COMPONENT_GUIDELINES.md
docs/design/UX_ANALYSIS_FLOW.md
docs/design/ACCESSIBILITY_STANDARD.md
docs/design/CONTENT_AND_TONE_GUIDE.md
docs/testing/TEST_STRATEGY.md
docs/testing/QUALITY_GATES.md
docs/testing/TEST_DATA_POLICY.md
docs/testing/TEST_EVIDENCE_STANDARD.md
docs/testing/TEST_MATRIX.md
docs/security/SECURITY_STANDARD.md
docs/security/PRIVACY_STANDARD.md
docs/security/SECURITY_TESTING.md
docs/security/VULNERABILITY_MANAGEMENT.md
docs/security/THREAT_MODEL.md
docs/security/RISK_ACCEPTANCE_TEMPLATE.md
docs/data/DATA_GOVERNANCE.md
docs/data/DATASET_VERSIONING.md
docs/data/DATA_CARD_TEMPLATE.md
docs/ml/ML_DEVELOPMENT_STANDARD.md
docs/ml/EXPERIMENT_TRACKING_STANDARD.md
docs/ml/MODEL_EVALUATION_STANDARD.md
docs/ml/MODEL_CARD_TEMPLATE.md
docs/ml/MODEL_RELEASE_AND_ROLLBACK.md
docs/ml/MODEL_MONITORING.md
docs/governance/RULE_CONFLICT_REPORT.md
docs/governance/AUTOMATION_OPPORTUNITIES.md
```

### Arquivos alterados

- `AGENTS.md`: guia operacional consolidado;
- `docs/DOCUMENTATION_STRUCTURE.md`: classificado como referência, sem autoridade concorrente;
- `docs/governance/README.md`: ligado ao índice global e aos novos registros de consolidação.

### Diretórios reservados pela arquitetura

`docs/design/`, `docs/testing/`, `docs/security/`, `docs/data/`, `docs/ml/`, `docs/product/`, `docs/api/`, `docs/computer-vision/`, `docs/operations/` e `docs/release/`. Diretório vazio não representa norma existente; só deve entrar no índice após receber documento oficial.

## Procedimento futuro

Ao achar conflito: capture as duas fontes e impacto, identifique nível de precedência, interrompa ação irreversível, proponha resolução no ticket responsável, obtenha gate quando necessário, atualize a fonte canônica e transforme a antiga em link ou histórico. Nunca mantenha duas regras “temporariamente oficiais”.
