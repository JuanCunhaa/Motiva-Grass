# Governança de Dados

Status: **Proposed**. Fonte canônica de ownership, proveniência, qualidade, acesso e uso.

## Princípios e papéis

Data Owner aprova finalidade/acesso; Steward mantém schema/taxonomia/Data Card; Engineering implementa pipeline; Privacy/Security revisam dados sensíveis; ML Validation protege splits/test set. A mesma pessoa pode acumular papéis, mas decisões ficam registradas.

## Regras obrigatórias

- Toda amostra tem `sample_id` opaco, origem, data/faixa, consentimento/licença, classe de sensibilidade, dispositivo/condição permitidos, transformações e checksum.
- Schema, taxonomia, unidades e regras de missing/rejection são versionados. Altura usa unidade canônica explícita (cm no contrato, se aprovada) e método de medição.
- Qualidade registra integridade, MIME real, dimensões, EXIF removido, marcador/medição, rótulo, duplicata/near-duplicate, inconsistência e quarentena.
- Dedup ocorre antes do split; near-duplicates e mesma coleta/local/sujeito/câmera relacionada ficam no mesmo grupo.
- Split é por `group_id`, determinístico e manifestado. Leakage entre train/validation/test é bloqueador.
- Test set é congelado por KAN-66, checksum/ACL auditados e proibido ao desenvolvimento/tuning. Acesso excepcional gera gate e nova versão/protocolo.
- Dados reais, imagens privadas e datasets não entram no Git/Jira/PR/CI comum. Git guarda schemas, manifests sem PII, fixtures sintéticas e checksums.
- Toda versão aprovada possui Data Card, owner, finalidade, cobertura, limitações e retenção.

## Proibições

Usar dado sem proveniência/licença; rotular unknown como classe conhecida por conveniência; excluir falhas para melhorar cobertura; alterar unidade silenciosamente; compartilhar URL/credencial; tratar fixture como evidência real.

## Checklist

- [ ] Proveniência/licença/consentimento/classificação.
- [ ] Schema/taxonomia/unidade/qualidade versionados.
- [ ] Dedup/grupos/splits/leakage/test set protegidos.
- [ ] Storage/acesso/retenção e Data Card.

## Riscos e pendências

Taxonomia depende de KAN-36; coleta/medição de gates físicos; storage KAN-106; Dataset V1 KAN-155.

