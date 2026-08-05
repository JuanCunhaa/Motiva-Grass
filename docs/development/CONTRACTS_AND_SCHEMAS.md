# Contratos e Schemas

## Decisão

Usar `packages/contracts` como fonte oficial language-neutral: JSON Schema 2020-12, OpenAPI 3.x, exemplos/golden files e versões explícitas. Tipos TypeScript e modelos Python são gerados ou adaptados e nunca substituem o schema canônico.

## Justificativa

Web não pode depender de Python e API não pode expor detalhes de modelo. Contrato canônico permite validação runtime e testes entre consumidores, conforme KAN-90/KAN-70.

## Alternativas

- Pydantic como fonte e OpenAPI gerado: acopla contrato ao backend/framework.
- TypeScript como fonte: dificulta consumidores Python.
- Duplicar DTOs: rejeitado por drift.
- Protobuf: adiar; JSON/HTTP é suficiente para o MVP.

## Regras obrigatórias

- Estrutura `packages/contracts/{schema,openapi,examples,golden,generated}` com diretórios `v1`, `v2` quando breaking.
- IDs, enums, unidades, nullability, limites e semântica são explícitos. Campo ausente nunca significa zero.
- Entrada externa é validada em runtime na web e API; resposta do runtime de ML é validada antes de serializar.
- Artefatos gerados contêm aviso, versão do gerador e não são editados manualmente.
- Compatibilidade é aditiva dentro da major: adicionar campo opcional com default semântico seguro; não remover/renomear, estreitar domínio, mudar unidade ou semântica.
- Breaking change exige nova major/rota (`/v2` quando pública), ADR, plano de migração, período de coexistência e validação dos consumidores.
- Erro de contrato usa código público estável e detalhe interno sanitizado; não tentar coerção silenciosa arriscada.
- Golden files cobrem sucesso, parcial, inconclusivo, inválido e erro; dados são sintéticos e identificados.
- Contract tests validam schema, exemplos, OpenAPI e consumidores TypeScript/Python. Mudança em contratos dispara web e API na CI.
- Compatibilidade do modelo inclui `contract_version`, `taxonomy_version`, `preprocessing_version`, capabilities e modelo/artefato; capability não aprovada não é prometida.

## Regras recomendadas

- Usar discriminadores para estados de resultado e erros.
- Publicar changelog por versão e matriz produtor/consumidor.
- Validar exemplos como parte da documentação.
- Gerar cliente TS a partir de OpenAPI somente na fronteira HTTP; domínio UI usa tipos próprios derivados/mapeados.

## Exemplos

- `status: "inconclusive"` exige `warnings` e proíbe altura fabricada.
- Adicionar `request_id` opcional em v1 pode ser compatível; trocar centímetros por milímetros no mesmo campo é breaking.

## Anti-patterns

- `Record<string, any>`, enum livre, unidade só em comentário ou schema diferente no frontend.
- Alterar golden para fazer teste passar sem revisar semântica.
- Expor logits, nome interno de checkpoint ou stack trace no contrato público.

## Checklist

- [ ] Schema canônico, ID/versão e exemplos válidos.
- [ ] Runtime validation nos produtores/consumidores.
- [ ] Tipos gerados reproduzíveis e sem edição manual.
- [ ] Compatibilidade/breaking avaliados e ADR quando necessário.
- [ ] Golden e contract tests cobrem todos os estados.
- [ ] Versões de taxonomia/preprocessing/modelo rastreáveis.

## Riscos

Geradores podem divergir em recursos de JSON Schema; limitar subset suportado e testar. Versionamento excessivo gera manutenção; breaking precisa de evidência.

## Pontos pendentes

- KAN-90/KAN-70 fecham campos, biblioteca de geração e versão OpenAPI exata.
- Definir política de depreciação/tempo de coexistência antes de v2.

