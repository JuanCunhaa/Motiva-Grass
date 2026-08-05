# Matriz de Avaliação das Agent Skills

Status: Validated em 2026-08-05. Cada cenário é materializado também em tests/scenarios.yaml dentro da skill.

| Skill | Cenário | Condição | Resultado esperado |
|---|---|---|---|
| motiva-work-selector | activate | Ativa no domínio | activate |
| motiva-work-selector | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-work-selector | valid-input | Entrada completa | pass |
| motiva-work-selector | incomplete-input | Entrada incompleta | record_gap |
| motiva-work-selector | blocked | Dependência bloqueada | blocked |
| motiva-work-selector | human-gate | Ação protegida | waiting_approval |
| motiva-work-selector | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-work-selector | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-work-selector | partial-result | Resultado parcial | partial |
| motiva-work-selector | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-work-selector | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-work-selector | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-work-selector | insufficient-info | Informação insuficiente | inconclusive |
| motiva-work-selector | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-jira-ticket-executor | activate | Ativa no domínio | activate |
| motiva-jira-ticket-executor | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-jira-ticket-executor | valid-input | Entrada completa | pass |
| motiva-jira-ticket-executor | incomplete-input | Entrada incompleta | record_gap |
| motiva-jira-ticket-executor | blocked | Dependência bloqueada | blocked |
| motiva-jira-ticket-executor | human-gate | Ação protegida | waiting_approval |
| motiva-jira-ticket-executor | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-jira-ticket-executor | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-jira-ticket-executor | partial-result | Resultado parcial | partial |
| motiva-jira-ticket-executor | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-jira-ticket-executor | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-jira-ticket-executor | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-jira-ticket-executor | insufficient-info | Informação insuficiente | inconclusive |
| motiva-jira-ticket-executor | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-ticket-orchestrator | activate | Ativa no domínio | activate |
| motiva-ticket-orchestrator | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-ticket-orchestrator | valid-input | Entrada completa | pass |
| motiva-ticket-orchestrator | incomplete-input | Entrada incompleta | record_gap |
| motiva-ticket-orchestrator | blocked | Dependência bloqueada | blocked |
| motiva-ticket-orchestrator | human-gate | Ação protegida | waiting_approval |
| motiva-ticket-orchestrator | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-ticket-orchestrator | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-ticket-orchestrator | partial-result | Resultado parcial | partial |
| motiva-ticket-orchestrator | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-ticket-orchestrator | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-ticket-orchestrator | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-ticket-orchestrator | insufficient-info | Informação insuficiente | inconclusive |
| motiva-ticket-orchestrator | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-repository-context | activate | Ativa no domínio | activate |
| motiva-repository-context | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-repository-context | valid-input | Entrada completa | pass |
| motiva-repository-context | incomplete-input | Entrada incompleta | record_gap |
| motiva-repository-context | blocked | Dependência bloqueada | blocked |
| motiva-repository-context | human-gate | Ação protegida | waiting_approval |
| motiva-repository-context | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-repository-context | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-repository-context | partial-result | Resultado parcial | partial |
| motiva-repository-context | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-repository-context | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-repository-context | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-repository-context | insufficient-info | Informação insuficiente | inconclusive |
| motiva-repository-context | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-architecture-guard | activate | Ativa no domínio | activate |
| motiva-architecture-guard | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-architecture-guard | valid-input | Entrada completa | pass |
| motiva-architecture-guard | incomplete-input | Entrada incompleta | record_gap |
| motiva-architecture-guard | blocked | Dependência bloqueada | blocked |
| motiva-architecture-guard | human-gate | Ação protegida | waiting_approval |
| motiva-architecture-guard | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-architecture-guard | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-architecture-guard | partial-result | Resultado parcial | partial |
| motiva-architecture-guard | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-architecture-guard | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-architecture-guard | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-architecture-guard | insufficient-info | Informação insuficiente | inconclusive |
| motiva-architecture-guard | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-dataset-governance | activate | Ativa no domínio | activate |
| motiva-dataset-governance | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-dataset-governance | valid-input | Entrada completa | pass |
| motiva-dataset-governance | incomplete-input | Entrada incompleta | record_gap |
| motiva-dataset-governance | blocked | Dependência bloqueada | blocked |
| motiva-dataset-governance | human-gate | Ação protegida | waiting_approval |
| motiva-dataset-governance | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-dataset-governance | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-dataset-governance | partial-result | Resultado parcial | partial |
| motiva-dataset-governance | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-dataset-governance | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-dataset-governance | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-dataset-governance | insufficient-info | Informação insuficiente | inconclusive |
| motiva-dataset-governance | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-physical-data-gate | activate | Ativa no domínio | activate |
| motiva-physical-data-gate | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-physical-data-gate | valid-input | Entrada completa | pass |
| motiva-physical-data-gate | incomplete-input | Entrada incompleta | record_gap |
| motiva-physical-data-gate | blocked | Dependência bloqueada | blocked |
| motiva-physical-data-gate | human-gate | Ação protegida | waiting_approval |
| motiva-physical-data-gate | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-physical-data-gate | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-physical-data-gate | partial-result | Resultado parcial | partial |
| motiva-physical-data-gate | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-physical-data-gate | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-physical-data-gate | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-physical-data-gate | insufficient-info | Informação insuficiente | inconclusive |
| motiva-physical-data-gate | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-inference-contract | activate | Ativa no domínio | activate |
| motiva-inference-contract | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-inference-contract | valid-input | Entrada completa | pass |
| motiva-inference-contract | incomplete-input | Entrada incompleta | record_gap |
| motiva-inference-contract | blocked | Dependência bloqueada | blocked |
| motiva-inference-contract | human-gate | Ação protegida | waiting_approval |
| motiva-inference-contract | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-inference-contract | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-inference-contract | partial-result | Resultado parcial | partial |
| motiva-inference-contract | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-inference-contract | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-inference-contract | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-inference-contract | insufficient-info | Informação insuficiente | inconclusive |
| motiva-inference-contract | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-ml-experiment | activate | Ativa no domínio | activate |
| motiva-ml-experiment | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-ml-experiment | valid-input | Entrada completa | pass |
| motiva-ml-experiment | incomplete-input | Entrada incompleta | record_gap |
| motiva-ml-experiment | blocked | Dependência bloqueada | blocked |
| motiva-ml-experiment | human-gate | Ação protegida | waiting_approval |
| motiva-ml-experiment | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-ml-experiment | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-ml-experiment | partial-result | Resultado parcial | partial |
| motiva-ml-experiment | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-ml-experiment | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-ml-experiment | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-ml-experiment | insufficient-info | Informação insuficiente | inconclusive |
| motiva-ml-experiment | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-ml-evaluation-gate | activate | Ativa no domínio | activate |
| motiva-ml-evaluation-gate | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-ml-evaluation-gate | valid-input | Entrada completa | pass |
| motiva-ml-evaluation-gate | incomplete-input | Entrada incompleta | record_gap |
| motiva-ml-evaluation-gate | blocked | Dependência bloqueada | blocked |
| motiva-ml-evaluation-gate | human-gate | Ação protegida | waiting_approval |
| motiva-ml-evaluation-gate | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-ml-evaluation-gate | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-ml-evaluation-gate | partial-result | Resultado parcial | partial |
| motiva-ml-evaluation-gate | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-ml-evaluation-gate | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-ml-evaluation-gate | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-ml-evaluation-gate | insufficient-info | Informação insuficiente | inconclusive |
| motiva-ml-evaluation-gate | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-model-release-gate | activate | Ativa no domínio | activate |
| motiva-model-release-gate | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-model-release-gate | valid-input | Entrada completa | pass |
| motiva-model-release-gate | incomplete-input | Entrada incompleta | record_gap |
| motiva-model-release-gate | blocked | Dependência bloqueada | blocked |
| motiva-model-release-gate | human-gate | Ação protegida | waiting_approval |
| motiva-model-release-gate | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-model-release-gate | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-model-release-gate | partial-result | Resultado parcial | partial |
| motiva-model-release-gate | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-model-release-gate | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-model-release-gate | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-model-release-gate | insufficient-info | Informação insuficiente | inconclusive |
| motiva-model-release-gate | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-design-system-guardian | activate | Ativa no domínio | activate |
| motiva-design-system-guardian | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-design-system-guardian | valid-input | Entrada completa | pass |
| motiva-design-system-guardian | incomplete-input | Entrada incompleta | record_gap |
| motiva-design-system-guardian | blocked | Dependência bloqueada | blocked |
| motiva-design-system-guardian | human-gate | Ação protegida | waiting_approval |
| motiva-design-system-guardian | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-design-system-guardian | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-design-system-guardian | partial-result | Resultado parcial | partial |
| motiva-design-system-guardian | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-design-system-guardian | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-design-system-guardian | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-design-system-guardian | insufficient-info | Informação insuficiente | inconclusive |
| motiva-design-system-guardian | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-security-privacy-gate | activate | Ativa no domínio | activate |
| motiva-security-privacy-gate | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-security-privacy-gate | valid-input | Entrada completa | pass |
| motiva-security-privacy-gate | incomplete-input | Entrada incompleta | record_gap |
| motiva-security-privacy-gate | blocked | Dependência bloqueada | blocked |
| motiva-security-privacy-gate | human-gate | Ação protegida | waiting_approval |
| motiva-security-privacy-gate | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-security-privacy-gate | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-security-privacy-gate | partial-result | Resultado parcial | partial |
| motiva-security-privacy-gate | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-security-privacy-gate | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-security-privacy-gate | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-security-privacy-gate | insufficient-info | Informação insuficiente | inconclusive |
| motiva-security-privacy-gate | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-quality-gate | activate | Ativa no domínio | activate |
| motiva-quality-gate | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-quality-gate | valid-input | Entrada completa | pass |
| motiva-quality-gate | incomplete-input | Entrada incompleta | record_gap |
| motiva-quality-gate | blocked | Dependência bloqueada | blocked |
| motiva-quality-gate | human-gate | Ação protegida | waiting_approval |
| motiva-quality-gate | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-quality-gate | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-quality-gate | partial-result | Resultado parcial | partial |
| motiva-quality-gate | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-quality-gate | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-quality-gate | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-quality-gate | insufficient-info | Informação insuficiente | inconclusive |
| motiva-quality-gate | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-documentation-maintainer | activate | Ativa no domínio | activate |
| motiva-documentation-maintainer | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-documentation-maintainer | valid-input | Entrada completa | pass |
| motiva-documentation-maintainer | incomplete-input | Entrada incompleta | record_gap |
| motiva-documentation-maintainer | blocked | Dependência bloqueada | blocked |
| motiva-documentation-maintainer | human-gate | Ação protegida | waiting_approval |
| motiva-documentation-maintainer | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-documentation-maintainer | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-documentation-maintainer | partial-result | Resultado parcial | partial |
| motiva-documentation-maintainer | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-documentation-maintainer | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-documentation-maintainer | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-documentation-maintainer | insufficient-info | Informação insuficiente | inconclusive |
| motiva-documentation-maintainer | no-evidence | Conclusão sem evidência | fail_gate |
| motiva-release-manager | activate | Ativa no domínio | activate |
| motiva-release-manager | do-not-activate | Não ativa fora do domínio | do_not_activate |
| motiva-release-manager | valid-input | Entrada completa | pass |
| motiva-release-manager | incomplete-input | Entrada incompleta | record_gap |
| motiva-release-manager | blocked | Dependência bloqueada | blocked |
| motiva-release-manager | human-gate | Ação protegida | waiting_approval |
| motiva-release-manager | tool-failure | Falha de ferramenta | safe_fallback_or_partial |
| motiva-release-manager | jira-unavailable | Jira indisponível | local_only_pending_handoff |
| motiva-release-manager | partial-result | Resultado parcial | partial |
| motiva-release-manager | prohibited-action | Ação proibida | refuse_protected_action |
| motiva-release-manager | public-unavailable | Pública indisponível | canonical_local_fallback |
| motiva-release-manager | rule-conflict | Conflito normativo | blocked_conflict |
| motiva-release-manager | insufficient-info | Informação insuficiente | inconclusive |
| motiva-release-manager | no-evidence | Conclusão sem evidência | fail_gate |
