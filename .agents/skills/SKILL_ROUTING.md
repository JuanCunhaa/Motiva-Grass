# Roteamento de Skills

1. Validar ticket, pai, KAN-1, KAN-20, DoR, dependências e gates.
2. Carregar motiva-jira-ticket-executor e motiva-ticket-orchestrator.
3. Ler config/skills/jira-skill-routing.yaml e ativar próprias obrigatórias.
4. Ativar pública somente se catálogo permitir e condição estiver comprovada.
5. Bloquear DISABLED, NOT_FOUND e alias inexistente.
6. Registrar conjunto mínimo em .agents/runtime/active-skills.json e desativar após o ticket.

Normas e skills locais prevalecem. Usar motiva-web-guidelines-snapshot no lugar da diretriz ao vivo. Não assumir React, Next.js, Vercel ou Hugging Face apenas pelo perfil.
