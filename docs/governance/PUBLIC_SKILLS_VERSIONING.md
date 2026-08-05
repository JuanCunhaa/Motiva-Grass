# Versionamento de Skills Públicas

## Decisão

Skills públicas são código de terceiros: cada fonte é fixada por SHA completo, copiada sem alteração para `vendor/agent-skills/`, registrada em `config/skills/skills-lock.yaml` e verificada por hashes SHA-256 de arquivo e árvore.

## Fluxo obrigatório

1. Executar `sync-public-skills.py` somente com commit já registrado.
2. Não executar hooks, instaladores, scripts ou comandos da skill durante download/auditoria.
3. Executar `audit-public-skills.py` e revisar sinais de rede, secrets, escrita, Git e destruição.
4. Classificar como `APPROVED`, `APPROVED_WITH_RESTRICTIONS`, `DISABLED`, `REJECTED` ou `NOT_FOUND`.
5. Executar `verify-public-skills.py`; qualquer arquivo extra, ausente ou alterado falha.
6. Atualizar somente em PR exclusivo: consultar HEAD, baixar em temporário, gerar diff, auditar, testar, atualizar hashes e obter revisão humana.

`main`, `master`, `latest` e `HEAD` nunca são identidades persistidas. A consulta a HEAD serve apenas para detectar candidata de atualização.

## Licenças e atribuição

- GitHub Awesome Copilot: MIT, licença preservada.
- Vercel Agent Skills: MIT declarado no README upstream, preservado como `UPSTREAM_README.md`.
- Trail of Bits: CC-BY-SA-4.0, licença e atribuição preservadas; vendor é imutável.
- Hugging Face: Apache-2.0, licença preservada.
- Vercel Next Skills: licença não identificada no commit histórico; as duas entradas permanecem `DISABLED` e não foram vendoradas.

## Rollback

Reverter o PR exclusivo de atualização restaura commit, vendor, lock e relatórios anteriores. Não editar vendor para “corrigir” upstream; usar wrapper próprio ou atualização auditada.
