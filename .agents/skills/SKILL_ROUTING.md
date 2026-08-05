# Roteamento de Skills

A fonte estruturada é `config/skills/jira-skill-routing.yaml`. Ative somente o perfil ou ticket atual; não carregue as 41 skills simultaneamente.

## Fluxo

1. Validar Jira, DoR, dependências e gates.
2. Ler o roteamento do ticket.
3. Bloquear `DISABLED`, `REJECTED` e `NOT_FOUND`.
4. Copiar apenas skills obrigatórias auditadas para `.agents/skills/public/`.
5. Incluir condicionais somente quando a condição estiver comprovada.
6. Registrar `.agents/runtime/active-skills.json` e desativar após o ticket.

Skills próprias do Motiva-Grass prevalecem sobre públicas. As 16 skills próprias ausentes permanecem `planned`; o agente deve aplicar as normas canônicas diretamente, sem simular que a skill existe.

