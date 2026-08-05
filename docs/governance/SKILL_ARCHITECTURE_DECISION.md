# Decisão de Arquitetura de Skills

- Status: Proposed
- Data: 2026-08-05
- Escopo: Agent Skills públicas e próprias do Motiva-Grass

## Decisão

Separar aquisição, auditoria, vendor, ativação e roteamento:

```text
fonte fixada → snapshot temporário → auditoria estática → vendor imutável
             → lock/hashes → roteamento por ticket → cópia ativa mínima
```

O runtime lê `config/skills/jira-skill-routing.yaml`, aceita somente status roteável e copia para `.agents/skills/public/` apenas o conjunto obrigatório do ticket. Condicionais exigem prova da condição e opção explícita.

## Consequências

- Disponibilidade não implica ativação.
- Skills próprias e documentos canônicos prevalecem sobre instruções públicas.
- As 16 skills próprias previstas estão `planned`; não se inventou conteúdo para elas.
- `motiva-web-guidelines-snapshot` é o único wrapper criado, pois o prompt exigiu substituir a busca flutuante por snapshot fixado.
- `vendor/` é imutável; adaptações vivem fora dele.
- Atualizações normais de tickets não consultam a internet nem atualizam skills.

## Riscos e controles

- Supply chain: commits/hashes, licença, auditoria e revisão.
- Comandos destrutivos: ativação não executa scripts; restrições bloqueiam ações automáticas.
- Rede/terceiros: condicionais e gates explícitos.
- Contexto excessivo: limite de 3–7 skills principais, até 4 condicionais e 12 totais.
- Drift Jira/repositório: matriz central e seção idempotente delimitada por marcadores.

## Reversibilidade

Desativar as skills remove somente cópias registradas em `.agents/runtime/active-skills.json`. Reverter a mudança restaura vendor, lock e roteamento anteriores sem tocar em código do produto.
