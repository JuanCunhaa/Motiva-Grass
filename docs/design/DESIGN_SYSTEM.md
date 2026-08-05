# Design System Motiva-Grass

Status: **Proposed**. Fonte canônica de princípios e composição; tokens vivem em `DESIGN_TOKENS.md`, comportamento em `COMPONENT_GUIDELINES.md`.

## Direção

Dark-first, moderna, tecnológica e confiável, com roxo como marca e referências discretas a natureza/CV por grades, recortes e overlays — nunca neon excessivo, dashboard genérico ou estética que comprometa leitura. Clareza para usuário não técnico prevalece sobre efeito visual.

## Princípios obrigatórios

1. **Incerteza visível:** “provável”, intervalo, qualidade, warnings e motivo de inconclusão; estimativa não é verdade absoluta.
2. **Uma ação principal:** cada etapa destaca a próxima ação, sem competir com métricas.
3. **Privacidade na interface:** explicar processamento/retenção antes do envio e permitir remover/recomeçar.
4. **Progressive disclosure:** resumo simples; metodologia técnica em expansão/página própria.
5. **Acessível por padrão:** WCAG 2.2 AA, teclado, foco, leitor de tela, zoom/reflow e reduced motion.
6. **Responsivo por conteúdo:** mobile-first; sem esconder informação crítica.

## Layout

- Conteúdo principal máx. 1200 px; texto 65–75 caracteres; grid 4/8/12 colunas conforme viewport.
- Breakpoints são orientativos: compact `<640`, medium `640–1023`, wide `≥1024`; componente responde ao container.
- Jornada usa stepper textual discreto, não shell de dashboard. Resultado combina narrativa, faixas e evidência, não apenas KPIs.
- Imagem/preview preserva proporção, nunca corta silenciosamente região usada na análise.

## Tipografia

- Display 40–48/700; H1 32–40/700; H2 24–32/600; H3 20–24/600.
- Corpo 16/1.5; corpo pequeno 14/1.5; caption 12/1.5 somente não crítico; labels 14/500.
- Métricas 24–40/600 com algarismos tabulares e unidade no mesmo contexto. Código 13–14 mono.
- Em compact, reduzir display/títulos um passo, nunca corpo abaixo de 16 para conteúdo principal.

## Composição e ownership

Tokens → primitives acessíveis → componentes base → patterns (upload, análise, resultado) → páginas. Componente base não chama API; feature controla estado; domínio fornece resultado tipado. Design/Frontend são owners, com Accessibility e Product como revisores.

## Uso correto

- Resultado: “Espécie provável: Esmeralda — confiança estimada 78%” e “Altura estimada: 4,2 cm; intervalo 3,4–5,1 cm”.
- Inconclusivo mostra motivo e ação: “Não foi possível estimar a altura: marcador não detectado. Refaça a foto com o marcador inteiro visível.”

## Uso incorreto

- “Sua grama é Esmeralda, 4,2 cm” sem incerteza.
- Cards de métricas sem hierarquia, glow roxo/ciano, texto cinza de baixo contraste ou warning apenas amarelo.

## Qualidade e evolução

Mudança de token/componente exige ticket, exemplos, a11y, visual regression e migração. Breaking de API visual exige depreciação. Componente novo só quando padrão se repete ou tem semântica própria; não criar wrapper cosmético sem valor.

## Checklist

- [ ] Princípios, tokens e guideline do componente aplicados.
- [ ] Estados conclusivo/warning/inconclusivo completos.
- [ ] Mobile, teclado, zoom, contraste e leitor de tela validados.
- [ ] Sem certeza artificial, retenção implícita ou estética de dashboard genérico.

## Riscos e pendências

Tokens ainda não foram testados em UI real. KAN-75 valida fluxo/conteúdo; KAN-128 implementa; KAN-133/KAN-148 auditam.

