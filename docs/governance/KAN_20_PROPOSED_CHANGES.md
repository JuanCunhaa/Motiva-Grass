# Alterações Sugeridas para KAN-20

## Objetivo

Fornecer uma proposta pronta para revisão humana antes de atualizar KAN-20. Este documento não altera o Jira.

## Escopo

Consolida diferenças entre o texto atual de KAN-20, as novas políticas versionadas e os conflitos encontrados no backlog em 05/08/2026.

## Mudanças obrigatórias sugeridas

### 1. Substituir a regra documental

Texto atual atribui ao Confluence a futura fonte oficial. Substituir por:

> O Jira é a fonte oficial de gestão e aceite. O repositório Git é a fonte oficial da documentação técnica versionada. O Pull Request é a fonte oficial da mudança e de sua revisão. O Confluence, quando autorizado, publica, organiza e facilita a descoberta dessas informações, sem criar uma segunda versão normativa. Nenhuma informação importante pode existir somente em conversa com IA.

Motivo: alinha KAN-20 à divisão de responsabilidades solicitada e evita divergência entre Git e Confluence.

### 2. Acrescentar algoritmo de seleção

Inserir após `Política de dependências`:

> O executor mantém um ticket principal. Deve filtrar itens concluídos, bloqueados, duplicados e já assumidos; respeitar a primeira frente executável da ordem de KAN-1; verificar pai, labels, dependências textuais e estruturadas, gates, dados, acessos, custo e produção; e, dentro da mesma frente, ordenar P0, P1, P2 e posição no roadmap. Número menor não define prioridade.

### 3. Tornar transições objetivas

Adicionar critérios completos de `Tarefas pendentes`, `Em andamento`, `Em análise` e `Concluído` conforme `JIRA_WORKFLOW_POLICY.md`, incluindo retorno de análise, reabertura e regra contra ticket sem atividade real.

### 4. Completar DoR

Adicionar explicitamente: resultado verificável, fora do escopo quando relevante, entregáveis, testes/evidências, responsável, riscos, dados/fixtures, execução concorrente, credenciais/custo/produção e momento do gate. A seção atual resume esses pontos, mas não os torna todos verificáveis.

### 5. Completar DoD

Adicionar explicitamente: evidência real, documentação versionada, aprovação do PR, checks, segurança, acessibilidade, impactos de dados/ML, rollback, merge commit, Bugs relacionados, riscos residuais e Jira atualizado.

### 6. Incorporar templates normativos

Referenciar `JIRA_COMMENT_TEMPLATES.md` para início, progresso, bloqueio, desbloqueio, análise, conclusão, parcial e decisão. Progresso é orientado por evento, não por frequência fixa.

### 7. Detalhar Bug, parcial e NO-GO

Referenciar `BUG_MANAGEMENT_POLICY.md` e proibir explicitamente: fixture como dado real, integração não testada, teste declarado sem execução, aceite flexibilizado sem decisão e parcial apresentado como completo.

### 8. Corrigir rastreabilidade

Adicionar formatos:

- branch: `tipo/KAN-N-descricao-curta`;
- PR: `[KAN-N] Descrição objetiva`;
- commit: Conventional Commits com `[KAN-N]`;
- cadeia: `Jira → branch → commits → PR → documentação → release`.

### 9. Definir conflitos entre fontes

Adicionar procedimento: parar parte afetada, registrar evidências no Jira, obter decisão do owner do domínio, atualizar fontes afetadas/ADR e retomar somente após interpretação única.

### 10. Corrigir a dependência estruturada com KAN-89

KAN-20 declara depender de KAN-89, mas o link estruturado atual indica a direção oposta. Após revisão humana, inverter o vínculo para que KAN-89 bloqueie KAN-20, ou alterar formalmente a dependência textual se essa não for a intenção.

## Regras recomendadas

- Manter KAN-20 como norma curta que aponta para os documentos versionados, evitando duplicação integral.
- Registrar versão e data efetiva da política.
- Definir owner de governança e revisão semestral ou após mudança de workflow.
- Relacionar o PR de criação destas políticas a KAN-20 após aprovação.

## Exemplos corretos

- KAN-20 resume o contrato e aponta para arquivos versionados aprovados.
- Mudança de workflow atualiza KAN-20 e a política na mesma decisão/PR.

## Exemplos incorretos

- Colar políticas divergentes em Jira e Confluence sem versão/owner.
- Atualizar KAN-20 antes de corrigir ou decidir a direção de `Blocks`.

## Exceções

Enquanto não houver repositório Git oficial, Jira pode ser fonte técnica temporária, com prazo e plano de migração. Esta exceção termina quando o repositório versionado for aprovado.

## Checklist de revisão humana

- [ ] Divisão Jira/Git/PR/Confluence aprovada.
- [ ] Workflow de quatro estados confirmado.
- [ ] Direção KAN-89 → bloqueia → KAN-20 confirmada e corrigida.
- [ ] DoR, DoD, gates, Bugs, comentários e rastreabilidade referenciados.
- [ ] Owner, versão e data efetiva definidos.
- [ ] Jira só será alterado após aprovação destes documentos.

