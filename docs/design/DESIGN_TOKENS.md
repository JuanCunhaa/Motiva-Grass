# Design Tokens

Status: **Proposed** — aprovação em KAN-75/KAN-128. Escopo: tema escuro do MVP.

## Cores

| Token | Valor | Uso |
|---|---:|---|
| `color.bg.canvas` | `#0B0A12` | fundo global |
| `color.bg.surface` | `#15131F` | cards e formulários |
| `color.bg.elevated` | `#201C2D` | modal, menu, tooltip |
| `color.border.default` | `#443D57` | divisores/controles |
| `color.text.primary` | `#F3F0F8` | texto principal; evitar branco puro |
| `color.text.secondary` | `#CEC8DA` | texto auxiliar |
| `color.text.muted` | `#A69DB5` | metadado; nunca instrução crítica |
| `color.brand.default` | `#A78BFA` | ação/identidade roxa |
| `color.brand.strong` | `#8B5CF6` | borda/ênfase, não texto pequeno isolado |
| `color.accent.blue` | `#60A5FA` | informação/gráficos |
| `color.accent.cyan` | `#67E8F9` | visão computacional |
| `color.accent.green` | `#4ADE80` | natureza/sucesso |
| `color.status.success` | `#4ADE80` | sucesso + ícone/texto |
| `color.status.warning` | `#FBBF24` | warning + ícone/texto |
| `color.status.danger` | `#FB7185` | erro/perigo + ícone/texto |
| `color.status.info` | `#60A5FA` | informação |
| `color.focus` | `#C4B5FD` | outline de foco |
| `color.disabled.bg` | `#2B2736` | controle desabilitado |
| `color.disabled.text` | `#81798E` | somente estado inativo |
| `color.overlay` | `#050409CC` | overlay 80% |

Texto normal deve atingir 4,5:1; texto grande e limites/ícones essenciais, 3:1. Botão brand usa texto `#171122`, não branco. Validar cada combinação real, inclusive hover/gradiente, em CI e auditoria manual.

Gráficos: sequência `#A78BFA`, `#60A5FA`, `#67E8F9`, `#4ADE80`, `#FBBF24`, `#FB7185`; nunca diferenciar séries apenas por cor: usar marcador, padrão, rótulo ou traço. Eixos usam `text.secondary`; grid `border.default` a 60%.

## Estados

| Estado | Regra |
|---|---|
| hover | elevar luminância/contraste sem deslocar layout; não é único feedback |
| focus-visible | outline `2px color.focus` + offset `2px`; área/contraste WCAG |
| active | reduzir brilho/sombra e feedback de pressão |
| selected | brand tint + borda + ícone/check/`aria-selected` |
| disabled | sem interação/foco; motivo disponível quando necessário |
| loading | preserva largura, `aria-busy`, rótulo e cancelamento quando longo |
| error | danger + texto associado; não só cor |
| success | success + ícone/texto; não usar toast como única confirmação |

## Forma, espaço e elevação

- Spacing base 4 px: `0, 4, 8, 12, 16, 24, 32, 48, 64`.
- Radius: `4` técnico, `8` controles, `12` cards, `16` modal, `999` pill.
- Sombras: `sm 0 1px 2px #0006`; `md 0 8px 24px #0008`; `lg 0 16px 48px #000A`. Borda continua necessária no dark.
- Z-index: base `0`, sticky `100`, dropdown `300`, overlay `500`, modal `600`, toast `700`, tooltip `800`. Não inventar valores locais.

## Tipografia e motion

- UI: `Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif`; preferir self-host após licença/performance aprovadas.
- Código/números tabulares: `"JetBrains Mono", "SFMono-Regular", Consolas, monospace`.
- Escala rem: `12/.75`, `14/.875`, `16/1`, `18/1.125`, `20/1.25`, `24/1.5`, `32/2`, `40/2.5`, `48/3`.
- Pesos: 400 corpo, 500 labels, 600 títulos/ação, 700 display; evitar 300.
- Line-height: 1.5 corpo, 1.35 labels, 1.2 títulos, 1.1 métricas.
- Motion: fast `120ms`, normal `180ms`, slow `260ms`; easing `cubic-bezier(.2,.8,.2,1)`. Com `prefers-reduced-motion`, remover deslocamento/parallax e usar transição ≤1 ms.

## Tema claro futuro

Componentes consomem tokens sem hex local. Um futuro `data-theme="light"` redefine semântica, não nomes. Antes de lançar, revalidar contraste, gráficos, imagens, sombras e screenshots; não inverter cores mecanicamente.

## Regras obrigatórias

- Tokens centralizados e nomes semânticos; zero cor/spacing arbitrário em componentes.
- Estados e contraste testados no contexto real.
- Cor nunca é o único canal.

## Checklist

- [ ] Tema escuro completo e contraste AA.
- [ ] Focus/disabled/loading/error/success definidos.
- [ ] Gráficos redundantes, spacing/radius/shadow/z consistentes.
- [ ] Reduced motion e tema claro futuro preservados.

## Riscos e pendências

Fontes externas podem afetar privacidade/performance; decidir self-host em KAN-128. Tokens são proposta e exigem medição automática de contraste antes da aceitação.

