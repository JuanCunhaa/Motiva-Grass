# Estratégia de Testes

Status: **Proposed**. Objetivo: evidência proporcional ao risco em cada camada, sem tratar cobertura como qualidade.

## Pirâmide e responsabilidades

- Unitários: domínio, validação, geometria, mapeadores, estados e funções puras; rápidos/offline.
- Componentes: comportamento, acessibilidade e estados visuais.
- Integração: adapters, storage/registry fake/real controlado, carregamento de artefato, API.
- Contrato: schemas, golden files e compatibilidade web/API/modelo.
- E2E: jornadas normal, warning, inconclusivo, inválido, cancelamento e retry.
- Visual: componentes/páginas estáveis nos viewports suportados; revisão de diff.
- Segurança: upload malicioso, auth futura, secrets, SAST, dependency/SBOM e abuso.
- Performance: latência P50/P95, throughput, concorrência, memória/startup e soak.
- Dados/CV/ML: schema, checksums, leakage, geometria, métricas, calibração, OOD e equivalência.
- Deploy: smoke, readiness, configuração, rollback e artefato exato.

## Execução

PR rápido: lint/types/unit/component/contract, security leve, data schemas, smoke CPU e testes afetados por paths. Scheduled: suite completa, E2E multi-browser, visual ampla, SAST/deps, performance tendência e ML pesado/GPU. Manual: câmera/dispositivos, leitor de tela, UX, threat model, resultados estatísticos e rollback de alto risco.

GPU roda em PR somente quando mudança de kernel/runtime exige e recurso aprovado; caso contrário scheduled/on-demand em KAN-135. Indisponibilidade não vira sucesso: estado `not run/infrastructure unavailable`, evidência e reexecução. CPU smoke é obrigatório e não prova equivalência GPU; tolerância CPU/GPU é versionada.

## Cobertura e flakiness

- Proposta inicial: domínio/contratos/segurança ≥90% branches; demais lógica de produção ≥80%; diff coverage ≥85%. Código gerado, glue declarativo e I/O impraticável exigem justificativa, não exclusão silenciosa.
- Mutation/property tests para invariantes críticos quando úteis. Cobertura não substitui assertividade, casos negativos ou revisão.
- Retry automático máximo 1 apenas para diagnóstico e preserva a primeira falha. Teste com 2 falhas inesperadas em 20 execuções ou taxa >1% é flaky: abre Bug, owner e prazo; não pode bloquear indefinidamente sem caminho de correção nem ser simplesmente ignorado.

## Fixtures/golden

Somente sintéticos, públicos aprovados ou minimizados/sanitizados. Dados privados reais não entram em Git/CI. Fixture identifica origem/licença/classificação e objetivo. Golden é pequeno, revisado semanticamente e atualizado pelo comando oficial — nunca para “fazer verde”.

## Regras obrigatórias

- Teste junto da implementação e regressão para Bug.
- Ambiente, versão, seed, dados, comando e resultado registrados.
- Teste pulado exige condição explícita; skip inesperado falha.
- Test set congelado nunca participa de PR/tuning.
- Falha crítica bloqueia PR/release; exceção segue aceite de risco.

## Checklist

- [ ] Camadas e casos negativos proporcionais ao risco.
- [ ] PR/scheduled/manual/GPU/CPU corretamente classificados.
- [ ] Fixtures/golden permitidos e rastreáveis.
- [ ] Cobertura e flakiness dentro da política.
- [ ] Evidência no PR/Jira e nenhum verde falso.

## Riscos e pendências

Limiares serão calibrados após baseline KAN-35/134. Ferramentas/frameworks dependem de KAN-33/34. Matriz de browsers/devices depende de KAN-146.

