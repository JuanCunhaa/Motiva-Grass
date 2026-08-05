# ADR-0001 — Arquitetura do Repositório

## Decisão

Adotar, se aprovado, monorepo polyglot modular conforme `REPOSITORY_ARCHITECTURE.md` e `FOLDER_STRUCTURE.md`, com contratos language-neutral e pesos/datasets fora do Git.

## Justificativa

Permite mudanças atômicas entre contrato, web, API e ML, CI por paths e uma fonte documental, preservando fronteiras por regras de import e ownership.

## Alternativas

1. Multi-repo: isolamento maior; rejeitado inicialmente por coordenação/versionamento.
2. Monólito único: simples; rejeitado por misturar UI, HTTP e treino.
3. Microserviços: rejeitados por custo operacional sem demanda comprovada.

## Regras obrigatórias

- **Status:** Proposed.
- **Data:** 2026-08-05.
- **Responsáveis/decisores:** owner de arquitetura e responsáveis de Web, Backend, ML, Data e Security — pendentes de nomeação.
- **Tickets:** KAN-1, KAN-5, KAN-6, KAN-28, KAN-29, KAN-30, KAN-31, KAN-32.
- API não importa treino/notebooks; web não importa Python; domínio não depende de framework.
- Contratos são versionados; integrações usam adapters; testes rodam offline com fakes.
- Dataset real, imagem privada, pesos e secrets não entram no Git.
- Mudança desta decisão exige novo ADR que a substitua.

### Consequências

Positivas: refactors atômicos, rastreabilidade, ferramentas unificadas e feedback rápido. Negativas: CI/build polyglot, risco de acoplamento e ownership compartilhado.

### Segurança, custos e reversibilidade

Fronteiras reduzem acesso indevido; monorepo exige CODEOWNERS e path protections. Custo inicial de tooling é maior, menor que sincronização multi-repo no MVP. Reversível: módulos com APIs públicas podem ser extraídos para repos/serviços mantendo contratos.

## Regras recomendadas

- Medir duração da CI e acoplamento antes de extrair serviços.
- Revisar ADR após primeira release ou mudança de deploy independente.

### Template oficial de ADR

```markdown
# ADR-NNNN — <Título>

- Status: <Proposed | Accepted | Deprecated | Superseded>
- Data: <YYYY-MM-DD>
- Responsáveis/decisores: <papéis ou nomes>
- Tickets relacionados: <KAN-N>
- Substitui/substituído por: <ADR ou N/A>

## Contexto
<problema, restrições, fatos e hipóteses>

## Decisão
<escolha e limites>

## Alternativas
<opções avaliadas e por que não escolhidas>

## Consequências
<positivas, negativas e trabalho decorrente>

## Riscos
<riscos, controles e residual>

## Segurança e privacidade
<impactos ou N/A justificado>

## Custos
<implantação, operação e oportunidade>

## Reversibilidade
<rollback, migração e gatilho de revisão>
```

## Exemplos

- Mudança de schema altera contrato, generated types, API e web no mesmo PR.
- Extração futura do runtime mantém OpenAPI/artefato e recebe ADR próprio.

## Anti-patterns

- Declarar `Accepted` antes de KAN-28/KAN-31.
- Usar monorepo para imports arbitrários ou armazenar artefatos grandes.

## Checklist

- [ ] KAN-27/28/31 e owners revisaram.
- [ ] Fronteiras, estrutura e CI são viáveis.
- [ ] Segurança/licenças/custos avaliados.
- [ ] Decisão e status atualizados no Jira/PR.

## Riscos

Acoplamento, CI lenta, permissões amplas e incompatibilidade de toolchains.

## Pontos pendentes

- Aprovação de KAN-28 e threat model KAN-31.
- Stack e versões finais KAN-33/KAN-34; deploy KAN-97.
