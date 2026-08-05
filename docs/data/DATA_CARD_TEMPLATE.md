# Template de Data Card

```markdown
# Data Card — <nome> <versão>

- Status/owner/data: <draft|validated|frozen|deprecated> / <papel> / <ISO>
- Manifest/checksum/storage class: <links/valor/classificação>
- Tickets: <KAN-N>

## Finalidade e usos proibidos
<objetivo, população/domínio, decisões que não suporta>

## Origem, licença e consentimento
<fontes, coleta, direitos, privacidade e retenção>

## Schema, taxonomia e unidades
<versões, unknown, missing, protocolo de altura>

## Composição e cobertura
<contagens por classe/grupo/dispositivo/condição/altura; sem inventar>

## Qualidade
<integridade, rejeição, duplicatas, near-duplicates, rótulos e auditoria>

## Splits e prevenção de leakage
<group key, proporções, seed, frozen test e checksums>

## Processamento e proveniência
<código/config/transformações e versões parent>

## Limitações, vieses e riscos
<lacunas, impacto, mitigação e OOD>

## Acesso, segurança e governança
<papéis, storage, expiração, incidentes e owner>

## Changelog e aprovação
<diferenças, revisores, decisão GO/NO-GO>
```

## Regras

Campos sem evidência usam `não medido`/`desconhecido`, nunca estimativa inventada. Tabelas agregadas não podem reidentificar. Card é atualizado com a versão e não descreve outro manifest.

## Checklist

- [ ] Identidade/checksum/owner/tickets.
- [ ] Finalidade, origem/direitos, schema/taxonomia/unidades.
- [ ] Cobertura/qualidade/splits/leakage/proveniência.
- [ ] Limitações, acesso, changelog e aprovação.

## Riscos e pendências

Métricas reais só após KAN-45/107/155; este template não autoriza preenchimento fictício.

