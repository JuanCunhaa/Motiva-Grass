# Padrão de Acessibilidade

Status: **Proposed**. Meta: WCAG 2.2 nível AA; requisitos legais adicionais dependem de revisão aplicável.

## Regras obrigatórias

- Operação completa por teclado, ordem lógica, skip link e sem keyboard trap.
- `:focus-visible` persistente, não oculto por sticky/overlay; contraste e área conforme WCAG.
- Texto normal ≥4,5:1; grande e componentes essenciais ≥3:1; cor nunca única informação.
- Landmarks (`header/nav/main/footer`), H1 único e headings sem saltos arbitrários.
- Todo campo tem label; erro associado, resumo focável quando submissão falha e instrução antes da entrada.
- Alvo WCAG mínimo 24×24 CSS px ou espaçamento equivalente; recomendado 44×44 para ações/câmera/mobile.
- Semântica nativa primeiro. ARIA complementa, não corrige HTML errado.
- Leitor de tela recebe nomes, estados, unidades, warnings e progresso; anúncios por marcos, sem spam.
- Zoom 200% e reflow a 320 CSS px sem perda/scroll bidimensional salvo conteúdo essencial.
- `prefers-reduced-motion`; sem flash; autoplay proibido.
- Gráfico tem resumo, dados alternativos/tabela e séries distinguíveis sem cor.
- Ícone informativo vem com texto/nome; decorativo é oculto.
- Câmera oferece instruções textuais/sonoras opcionais, alternativa por arquivo e funciona em ambas orientações.
- Linguagem simples, `lang="pt-BR"`, mudanças de idioma marcadas; preparar catálogo `en`.

## Testes

PR: lint/axe equivalente, teclado e componentes alterados. Manual antes de análise: NVDA+Firefox/Chrome no Windows e VoiceOver+Safari quando suportado, zoom/reflow, contraste, touch e reduced motion. KAN-133/KAN-148 fazem auditoria independente.

Problema crítico: impede tarefa principal, expõe dado/decisão incorreta ou bloqueia tecnologia assistiva sem alternativa — bloqueia PR/release. Alto: fluxo importante degradado — corrigir antes da release salvo aceite formal.

## Uso correto e anti-patterns

- Correto: warning com ícone, heading, texto e ação; gráfico com tabela.
- Incorreto: div clicável, foco removido, placeholder como label, toast como único erro, gesto/cor como único canal.

## Checklist

- [ ] Teclado/foco/landmarks/headings/labels.
- [ ] Contraste, alvos, zoom/reflow e reduced motion.
- [ ] SR, anúncios, gráficos e ícones.
- [ ] Mobile/câmera/linguagem simples.
- [ ] Automação + teste manual/evidência.

## Riscos e pendências

Ferramenta automática detecta apenas parte dos problemas. Matriz final de navegadores/dispositivos será definida em KAN-146.

## Referências

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Contraste mínimo](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
- [Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum)

