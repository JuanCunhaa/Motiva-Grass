# Guidelines de Componentes

Status: **Proposed**. Todos os componentes usam tokens, HTML nativo quando possível e WCAG 2.2 AA.

## Matriz normativa

| Componente | Variantes/estados | Acessibilidade e mobile | Uso correto / incorreto | Testes |
|---|---|---|---|---|
| Botão | primary, secondary, ghost, danger; hover/focus/active/loading/disabled | `<button>`, nome acessível, alvo recomendado 44px; full-width só quando útil | uma primary por região / ícone sem nome | teclado, foco, loading, contraste |
| Input | text, search, number; valid/error/disabled | label persistente, hint e erro por `aria-describedby`; teclado adequado | unidade fora do placeholder / placeholder como label | label, erro, zoom, autofill |
| Select | nativo primeiro, combobox quando necessário | setas/Esc/typeahead; modal bottom-sheet em mobile se custom | lista curta e clara / custom sem teclado | ARIA pattern, touch, SR |
| Checkbox | checked/mixed/error | label clicável, 44px, `indeterminate` real | escolhas independentes / consentimento pré-marcado | teclado/SR/estado |
| Radio | grupo/erro | `fieldset/legend`, setas, uma escolha | mutuamente exclusivo / usar para multiselect | navegação/erro |
| Switch | on/off/loading | label descreve efeito imediato; não para submit | preferência instantânea / pergunta complexa | teclado/announcements |
| Upload | idle/drag/validating/error/ready | input file acessível, botão alternativo, tipos/limites antes; drag não exclusivo | uma imagem e feedback / dropzone única | arquivo inválido, teclado, mobile |
| Câmera | permission/preview/capture/error | instrução textual, câmera traseira proposta, alternativa arquivo, orientação não só overlay | consentimento antes / captura automática | permissão negada, rotação, device |
| Preview | ready/invalid/processing | alt funcional, remover/substituir alcançáveis; contain no mobile | mostrar foto inteira / crop silencioso | proporção, memória, remoção |
| Card | default/interactive/status | heading correto; card inteiro link apenas se sem controles internos | agrupar um conceito / painel decorativo excessivo | semântica/foco/reflow |
| Modal | confirm/info/destructive | dialog, foco inicial/retorno, Esc salvo ação crítica; tela cheia compact | decisão bloqueante / conteúdo longo de navegação | focus trap, SR, scroll |
| Drawer | nav/detail | dialog/nav adequado, foco/retorno; bottom/full em mobile | contexto auxiliar / esconder fluxo principal | foco, swipe não exclusivo |
| Tooltip | help curto | hover+focus, dismissível, não conteúdo essencial; tap abre popover | termo breve / instrução ou erro | teclado, hover, zoom |
| Alert | info/success/warning/error | role status/alert conforme urgência, heading/ação | persistente para risco / sumir sozinho | announcement, contraste |
| Toast | success/info/error não crítico | `status`, pausa e histórico; não única evidência | confirmação redundante / erro de formulário | timing, SR, reduced motion |
| Progress | determinate/indeterminate/steps | `<progress>`/ARIA, anúncio por marcos; cancelar quando possível | progresso real / porcentagem inventada | announcements/cancel |
| Skeleton | text/card/image | `aria-hidden`, região `aria-busy`; reduzir motion | preservar layout / substituir mensagem necessária | reduced motion/layout |
| Tabela | data/compact/responsive | caption, headers/scope; scroll com contexto ou cards mobile | comparação tabular / layout de página | SR, reflow, sort |
| Gráfico | line/bar/distribution | resumo, tabela/download, padrões/rótulos; scroll/zoom acessível | complementar números / cor única | contraste, SR fallback |
| Badge | neutral/status/version | texto explícito; não único indicador | “Inconclusivo” / ponto colorido | contraste/zoom |
| Tabs | small peer views | ARIA tabs, setas, foco; tabs viram scroll, não dropdown oculto | conteúdo relacionado / etapas obrigatórias | teclado/SR/deep link |
| Navegação | primary/contextual | landmarks, current page, skip link; menu acessível | poucos destinos / sidebar dashboard sem necessidade | teclado/mobile |
| Breadcrumbs | hierarchy | `nav` label, lista, `aria-current` | páginas profundas / jornada linear curta | SR/reflow |
| Paginação | pages/load more | links/botões nomeados; manter foco; mobile compact | resultados extensos / esconder total essencial | teclado/URL |
| Estado vazio | first-use/no-results | heading, causa, ação; ilustração decorativa | orientar / culpar usuário | conteúdo/reflow |
| Erro | inline/page/recoverable/fatal | foco/resumo, campo associado, ação/referência | explicar correção / stack trace | erro por tipo/SR |
| Resultado | normal/warning/inconclusive | headings, unidades, texto+padrão; ordem lógica mobile | provável+intervalo / certeza absoluta | contrato, a11y, visual |
| Warning | quality/privacy/limitation | ícone+texto, impacto e ação | acionável / banner genérico amarelo | contraste/announcement |
| Inconclusivo | quality/OOD/capability/error seguro | não usar danger por padrão; motivo e próxima ação | resultado honesto / preencher com zero | todos motivos/golden/E2E |

## Regras obrigatórias

Estados devem vir de unions/contrato, nunca booleanos impossíveis. Loading preserva contexto; erro não apaga entrada sem necessidade. Componente interativo tem foco visível, nome, alvo mínimo e teste de teclado/leitor de tela.

## Checklist

- [ ] Variante e estado previstos; sem estado impossível.
- [ ] Acessibilidade, mobile e reduced motion verificados.
- [ ] Uso correto/incorreto considerado.
- [ ] Testes unitário/componente/visual/E2E proporcionais.

## Riscos e pendências

ARIA custom aumenta risco: preferir nativo. Framework e biblioteca headless serão decididos em KAN-34/KAN-128.

