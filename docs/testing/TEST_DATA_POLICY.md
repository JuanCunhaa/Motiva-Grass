# Política de Dados de Teste

Status: **Proposed**. Fonte canônica para fixtures, golden files e dados usados em CI.

## Classes permitidas

1. Sintético gerado e reproduzível — preferido.
2. Público com licença/termos aprovados e proveniência.
3. Amostra real sanitizada/minimizada — somente storage controlado e pipeline autorizado; nunca Git/CI público.
4. Privado/restrito — proibido no Git, PR, Jira, screenshots e CI comum.

Cada item registra ID, finalidade, classe, gerador/origem, licença/consentimento, schema, checksum, owner, retenção e versão. Fixtures não são dados reais e nunca sustentam métrica de produto.

## Regras obrigatórias

- Remover EXIF/GPS/nome original e identificadores; validar que sanitização não destrói o caso testado.
- Geradores usam seed/config versionadas; arquivos pequenos e limites de tamanho.
- Casos maliciosos são inertes/seguros, nomeados e não contêm secret/malware real sem laboratório aprovado.
- Golden recebe revisão semântica; mudança explica por que o esperado mudou.
- Dados ML mantêm grupos/splits; test set congelado inacessível ao treino/CI de feature.
- Limpeza/expiração de dados temporários é testada.

## Uso proibido

Foto pessoal do desenvolvedor no repo, cópia de produção, dado sem licença, secret em fixture, hash reversível como anonimização, download de rede não fixado e uso de fixture sintética como evidência real.

## Checklist

- [ ] Classificação, origem, licença, checksum e owner.
- [ ] Sanitização/EXIF/GPS e retenção.
- [ ] Seed/schema/versão reproduzíveis.
- [ ] Split/test set protegidos.
- [ ] CI não contém dado privado real.

## Riscos e pendências

Reidentificação e licença exigem revisão de KAN-31/KAN-27. Storage de teste controlado depende de KAN-106.

