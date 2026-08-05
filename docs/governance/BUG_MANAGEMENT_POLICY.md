# Política de Gestão de Bugs

## Objetivo

Definir como identificar, registrar, priorizar, relacionar, corrigir e encerrar defeitos sem confundi-los com melhoria ou dívida técnica.

## Escopo

Aplica-se a defeitos observados em implementação, revisão, QA, dados, ML, segurança, infraestrutura e produção. Um Bug descreve comportamento real contrário a um resultado esperado verificável.

## Regras obrigatórias

### Classificação

- **Bug:** comportamento observado viola contrato, requisito, critério de aceite, documentação normativa ou comportamento anteriormente comprovado.
- **Melhoria:** comportamento atual está correto, mas deseja-se nova capacidade, desempenho ou experiência.
- **Dívida técnica:** estrutura interna aumenta custo/risco sem necessariamente causar falha observável.
- **Incidente:** impacto operacional ativo; deve seguir runbook e pode gerar um ou mais Bugs posteriores.
- **Lacuna de requisito:** resultado esperado não está definido; corrigir o ticket/requisito antes de declarar Bug.

A hipótese de causa deve ser rotulada como hipótese até haver reprodução, isolamento ou outra evidência técnica suficiente.

### Quando corrigir no ticket atual

Corrigir no ticket atual somente quando todas as condições forem verdadeiras:

- o defeito foi introduzido pelas mudanças do ticket;
- é diretamente necessário para seu aceite;
- a correção é pequena e não amplia materialmente escopo, risco ou revisão;
- o mesmo PR pode provar a regressão;
- não há valor de priorização ou histórico independente.

Mesmo nesse caso, registrar o defeito e o teste no PR. Se qualquer condição falhar, abrir Bug separado.

### Quando abrir Bug separado

Abrir Bug quando o defeito for preexistente, fora do objetivo, compartilhado por vários componentes, descoberto após conclusão, exigir investigação própria, alterar prazo/risco, precisar de owner/prioridade independentes, envolver segurança/privacidade/dados, ou não puder ser corrigido com segurança no PR atual.

### Relação com o ticket original

- Vincular `found in`/`relates to` conforme tipos disponíveis e citar ticket/PR onde foi encontrado.
- Usar `Blocks` somente se o Bug realmente impedir um critério, teste obrigatório ou entrega segura.
- Manter o ticket original fora de `Concluído` para Bug crítico bloqueador.
- Permitir que o original continue para Bug não bloqueador somente se o escopo restante continuar válido, a limitação estiver explícita e nenhum aceite for falsamente marcado.
- Não encerrar Bug apenas porque o ticket original foi concluído.

### Severidade e prioridade

Severidade mede impacto técnico; prioridade mede ordem de correção.

| Severidade | Critério |
|---|---|
| S0 Crítica | risco imediato a segurança/privacidade, perda/corrupção grave, produção indisponível ou resultado perigoso sem contenção |
| S1 Alta | fluxo principal bloqueado, resultado materialmente incorreto, sem workaround aceitável |
| S2 Média | função degradada com workaround, impacto limitado ou não crítico |
| S3 Baixa | impacto cosmético/local, sem perda funcional relevante |

Mapeamento recomendado: S0→P0; S1→P0/P1; S2→P1/P2; S3→P2. Exceção exige justificativa.

### Template obrigatório de Bug

```markdown
## Resultado observado
<fato reproduzido; não incluir hipótese como fato>

## Resultado esperado
<contrato, requisito ou comportamento verificável>

## Passos de reprodução
1. <estado inicial>
2. <ação>
3. <resultado>

## Contexto técnico
- Ambiente: <local/CI/preview/staging/produção>
- Versão/release: <versão>
- Branch/commit: <URL/SHA>
- Navegador/dispositivo: <versão/modelo ou N/A>
- Dados/fixture: <identificador e classificação sintético/real>

## Evidências
- Logs sanitizados: <link ou trecho mínimo>
- Screenshots/vídeo: <link ou N/A>
- Teste falhando: <link/comando>

## Impacto e triagem
- Impacto: <usuários, dados, ML, operação>
- Severidade: <S0|S1|S2|S3 + justificativa>
- Prioridade: <P0|P1|P2 + justificativa>
- Workaround/contensão: <ação ou nenhum>

## Investigação
- Hipótese inicial: <hipótese, não causa confirmada>
- Ticket onde foi encontrado: <KAN-N>
- PR relacionado: <URL ou N/A>
- Teste de regressão esperado: <caso que deve falhar antes e passar depois>
```

### Encerramento do Bug

Exige reprodução inicial ou justificativa de não reprodutibilidade, correção/decisão registrada, teste de regressão aprovado, revisão, riscos residuais, versão de entrega e atualização do ticket que estava bloqueado. `Cannot reproduce`, `Won't fix` e duplicidade são decisões, não provas de correção, e exigem justificativa e aprovador quando houver risco material.

## Regras recomendadas

- Minimizar reprodução com fixture sanitizada.
- Registrar primeira versão afetada e versão corrigida quando conhecidas.
- Preservar evidência do comportamento anterior sem manter dados sensíveis.
- Agrupar sintomas somente quando a causa e a correção forem comprovadamente comuns.

## Exemplos corretos

- Upload PNG válido retorna 415 contra o contrato; há passos, commit, fixture, log e regressão esperada: Bug.
- A interface funciona conforme contrato, mas deseja-se arrastar e soltar: melhoria.
- Duplicação interna não causa falha observável, porém aumenta risco de manutenção: dívida técnica.

## Exemplos incorretos

- Título `Upload quebrado` sem ambiente ou reprodução.
- Marcar S0 para elevar prioridade de problema cosmético.
- Declarar `causa no proxy` apenas porque houve timeout.
- Corrigir defeito preexistente silenciosamente em PR de outro objetivo.

## Exceções

Vulnerabilidade sensível pode usar canal restrito e ticket com detalhes mínimos, conforme política de segurança. Incidente crítico permite ticket inicial abreviado, complementado após contenção. Defeito não reproduzível pode permanecer aberto para coleta de telemetria, sem alegar causa.

## Checklist

- [ ] Observado e esperado são distintos e verificáveis.
- [ ] Reprodução, ambiente, versão, commit, dispositivo e dados estão registrados.
- [ ] Logs e screenshots estão sanitizados.
- [ ] Severidade e prioridade têm justificativa.
- [ ] Hipótese não foi apresentada como causa.
- [ ] Ticket de origem e teste de regressão estão definidos.
- [ ] Relação de bloqueio reflete impacto real.

