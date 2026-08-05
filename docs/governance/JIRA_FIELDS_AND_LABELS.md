# Campos e Labels Recomendados

## Objetivo

Definir taxonomia controlada para seleção, bloqueio, execução, revisão e auditoria no Jira.

## Escopo

Aplica-se ao projeto KAN. A configuração administrativa depende de KAN-89. O objetivo é reduzir o uso de labels como substituto de campos estruturados.

## Regras obrigatórias

- Cada conceito possui uma única fonte operacional; não manter prioridade simultaneamente em label e campo após migração.
- Valores devem ser controlados, documentados e estáveis.
- Labels livres não podem alterar escopo ou aprovação.
- Campos de link não armazenam credenciais ou URLs temporárias.

## Campos recomendados

| Campo | Tipo | Obrigatoriedade/momento |
|---|---|---|
| Prioridade operacional | select P0/P1/P2 ou campo nativo normalizado | obrigatório na DoR; substituir labels `priority-*` após migração |
| Área | component ou multi-select controlado | obrigatório na DoR |
| Fase/Roadmap | single select | obrigatório; alinhado a KAN-1 |
| Modelo de IA recomendado | single select | obrigatório: Thinking, Sol Alto, Híbrido, N/A |
| Modelo de IA usado | texto/select + versão | comentário de início/conclusão |
| Estado da DoR | select Não avaliada/Reprovada/Aprovada | antes de `Em andamento` |
| Estado da DoD | select Não avaliada/Reprovada/Aprovada | antes de `Concluído` |
| Gate humano | checkbox/select | quando houver gate real |
| Estado do gate | Futuro/Ativo/Aprovado/Rejeitado/Expirado | para tickets com gate |
| Papel decisor do gate | user/group/text controlado | antes da ativação |
| Evidência do gate | URL | antes da retomada |
| Motivo do bloqueio | select Access/Data/License/Admin/External/Cost/Production/Risk/Physical | com Flagged |
| Ação de desbloqueio | texto curto | com Flagged |
| Próxima revisão | data/condição | com Flagged |
| Branch URL | URL | antes de `Em andamento` quando aplicável |
| Pull Request URL | URL | antes de `Em análise` quando aplicável |
| Documentação URL | URL/múltiplo | antes de `Em análise` |
| Evidências URL | URL/múltiplo | antes de `Em análise` |
| Commit de merge | texto/URL | antes de `Concluído` |
| Release/versão corrigida | fixVersion/s | quando aplicável |
| Severidade | select S0–S3 | obrigatório em Bug |
| Ambiente afetado | multi-select | obrigatório em Bug |
| Versão de dataset/modelo | texto/asset reference | dados/ML |
| Classificação do dado | select Sintético/Público/Interno/Restrito | quando houver dado |

Usar campos nativos `Assignee`, `Priority`, `Parent`, `Issue links`, `Flagged`, `Fix version` e `Affected version` sempre que servirem ao conceito.

## Labels controladas durante a transição

| Namespace | Exemplos |
|---|---|
| área | `area-frontend`, `area-backend`, `area-ml`, `area-security`, `area-data-quality` |
| fase | `phase-00-governance`, `phase-12-api`, `phase-15-release` |
| modelo | `model-gpt-5-6-thinking`, `model-gpt-5-6-sol-alto`, `model-hybrid` |
| prioridade (transitória) | `priority-p0`, `priority-p1`, `priority-p2` |
| bloqueio | `blocked-access`, `blocked-data`, `blocked-license`, `blocked-admin`, `blocked-external`, `blocked-cost`, `blocked-production`, `blocked-risk`, `blocked-physical` |
| gate | `gate-human` |
| componente | `component-upload`, `component-model-registry`, `component-marker` |
| controle/teste | `control-sast`, `control-sbom`, `test-e2e`, `test-resilience` |

Uma label de cada namespace singular (fase, modelo, prioridade) é permitida. Área/componente podem ser múltiplos. `gate-human` indica existência do gate; Flagged indica bloqueio ativo.

## Migração recomendada

1. inventariar valores atuais;
2. escolher campo oficial por conceito;
3. popular campos a partir das labels com relatório de exceções;
4. validar amostra e contagens;
5. atualizar filtros/automações;
6. congelar criação de labels equivalentes;
7. remover labels redundantes somente após aprovação e export de rollback.

## Exemplos corretos

- `gate-human` + estado `Futuro`, sem Flagged enquanto implementação local avança.
- Prioridade operacional P0 no campo oficial e Jira nativo coerente após migração.
- Bug S1 com prioridade P0 e justificativas distintas.

## Exemplos incorretos

- `priority-p0` e prioridade nativa Medium sem regra de precedência.
- `blocked` genérica sem causa/ação.
- Labels novas como `urgent-now`, `very-important` e `pzero` para o mesmo conceito.
- Colocar URL de PR em comentário apenas, sem campo/link rastreável.

## Exceções

Labels temporárias de experimento podem existir com prefixo e validade documentados. Projetos team-managed com limitação de campo podem manter labels controladas, mas devem declarar a precedência e validar cardinalidade. Migração nunca remove valores sem export recuperável.

## Checklist

- [ ] Cada conceito tem fonte única definida.
- [ ] Campos obrigatórios estão ligados às transições apropriadas.
- [ ] Namespaces e cardinalidade das labels estão documentados.
- [ ] Gate e impedimento são conceitos separados.
- [ ] Bugs possuem severidade, ambiente e versões.
- [ ] Migração tem validação, rollback e atualização de filtros/automações.

