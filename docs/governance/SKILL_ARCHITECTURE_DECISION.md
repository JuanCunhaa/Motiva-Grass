# Decisão de Arquitetura de Skills

- Status: Accepted
- Data: 2026-08-05
- Ticket: KAN-1
- Escopo: 16 skills próprias, um wrapper local e catálogo público fixado

## Decisão

Separar aquisição, auditoria, vendor, implementação local, ativação e roteamento:

    fonte fixada → auditoria → vendor imutável → catálogo/lock
    ticket → perfil → skills próprias → públicas comprovadas → evidências/gates

As 16 skills próprias vivem em .agents/skills/motiva/, compartilham referências em .agents/skills/shared/ e templates em .agents/skills/templates/. Cada skill possui SKILL.md, agents/openai.yaml e 14 cenários. Versões semânticas e status VALIDATED ficam no manifesto.

## Roteamento

motiva-jira-ticket-executor e motiva-ticket-orchestrator formam o núcleo. Skills de domínio entram conforme objetivo técnico. motiva-repository-context é obrigatória apenas em perfis com descoberta estrutural relevante. Públicas são ativadas somente quando APPROVED ou APPROVED_WITH_RESTRICTIONS e sua condição está comprovada.

## Precedência e conflitos resolvidos

- AGENTS.md, PROJECT_RULEBOOK.md e documentos canônicos prevalecem.
- Vendor nunca é modificado.
- motiva-web-guidelines-snapshot substitui a busca ao vivo da pública web-design-guidelines.
- React, Next.js, Vercel e Hugging Face não são inferidos sem manifesto ou ticket.
- O nome válido é vercel-react-best-practices; react-best-practices é apenas seletor upstream.
- next-best-practices, next-cache-components e skill-improver permanecem desabilitadas.
- static-analysis permanece NOT_FOUND; nenhuma child skill foi substituída silenciosamente.
- Confluence não é usado; Git é a fonte normativa e Jira governa o trabalho.

## Consequências

- 16 skills próprias e o wrapper estão VALIDATED na versão 1.0.0.
- 224 cenários cobrem ativação, não ativação, entradas, bloqueios, gates, falhas e evidência.
- config/skills/jira-skill-routing.yaml mantém 156 roteamentos idempotentes.
- O runtime ativa apenas o conjunto mínimo e registra .agents/runtime/active-skills.json.
- Atualizações comuns não consultam a internet nem alteram snapshots.

## Segurança e reversibilidade

Vendor, lock e backup Jira permitem reproduzir ou reverter a decisão. A atualização Jira é limitada ao bloco MOTIVA-SKILLS; campos protegidos e texto externo são auditados. Gates humanos continuam obrigatórios para licença, custo, produção, dados restritos, ações físicas, modelos e release.
