# Política de documentação

**Status:** normativa  
**Responsável:** mantenedores do repositório  
**Revisão:** quando mudar processo, arquitetura, risco ou obrigação regulatória

## Objetivo

Manter documentação útil, rastreável, sem regras concorrentes e próxima do artefato que descreve. O índice oficial é `docs/DOCUMENTATION_INDEX.md`; a precedência geral está em `PROJECT_RULEBOOK.md`.

## Fonte oficial por tipo de informação

| Informação | Fonte oficial |
|---|---|
| Trabalho, responsável, prioridade e estado | Jira |
| Código, contratos, testes e configuração versionada | Git |
| Regra técnica ou operacional do projeto | Documento normativo no Git |
| Decisão arquitetural aceita | ADR no Git |
| Evidência de execução | PR/CI e link no Jira |
| Conhecimento colaborativo não normativo | Confluence, quando disponível |

Confluence não substitui regras versionadas. Se uma cópia for necessária, ela deve apontar para o arquivo canônico e declarar que pode estar desatualizada.

## Classes de documento

- **Normativo:** usa “deve”, possui responsável, critério verificável e fonte de rastreabilidade.
- **Decisão:** ADR imutável após aceitação; mudanças exigem novo ADR que substitua o anterior.
- **Evidência:** registra uma execução, resultado, ambiente e artefatos; não cria regra geral.
- **Referência:** explica contexto, exemplos ou operação sem competir com uma norma.
- **Template:** estrutura mínima para um novo registro.

## Requisitos mínimos

Todo documento normativo deve declarar título, status, escopo, regras, exceções, validação e referências. Toda afirmação temporal deve trazer data. Toda decisão excepcional deve apontar para ticket, responsável e prazo.

Documentos devem:

1. usar Markdown e links relativos para arquivos do repositório;
2. usar português claro, preservando nomes técnicos e identificadores;
3. evitar copiar regras já canônicas; usar links;
4. incluir diagramas apenas quando melhorarem a compreensão;
5. não conter segredo, credencial, dado pessoal, amostra privada, peso de modelo ou saída identificável;
6. ser atualizados no mesmo PR que altera o comportamento correspondente.

## Documentação exigida por mudança

| Mudança | Documentação mínima |
|---|---|
| Arquitetura, fronteira ou dependência estrutural | ADR e atualização do índice arquitetural |
| Contrato, schema ou API | contrato versionado, exemplos válidos e incompatíveis |
| Fluxo ou componente de UI | guideline, estados, acessibilidade e evidência visual |
| Dataset ou transformação | versão do dataset e Data Card |
| Treino ou avaliação | registro do experimento e métricas completas |
| Modelo promovido | Model Card, evidência de avaliação, rollback e monitoramento |
| Operação recorrente | runbook |
| Incidente | postmortem sem culpa e ações rastreáveis |
| Release | GO/NO-GO e release notes |

## Revisão e expiração

O autor do PR verifica links, duplicação e aderência ao template. O revisor técnico valida conteúdo; segurança, privacidade, dados ou ML participam quando o assunto os afetar. Documentos temporários devem informar data de expiração. Exceções vencidas são inválidas.

## Conflitos

Em conflito, não se escolhe silenciosamente uma regra. Aplicam-se a precedência e o procedimento de `PROJECT_RULEBOOK.md`, registrando a resolução em `docs/governance/RULE_CONFLICT_REPORT.md`. Até a decisão, vale a alternativa mais restritiva que seja segura e reversível; mudanças irreversíveis aguardam decisão humana.

## Validação

A CI deve verificar links internos, arquivos exigidos, headings mínimos, ausência de segredos e referências Jira em documentos de evidência. Revisões periódicas devem localizar documentos órfãos e links para normas substituídas.
