# Guia de Conteúdo e Tom

Status: **Proposed**. Idioma inicial `pt-BR`; toda string de UI usa chave preparada para `en`.

## Voz da marca

Clara, calma, responsável, técnica sem ser hermética e honesta sobre limites. Falar com o usuário, não sobre o sistema. Frases curtas, voz ativa e ação concreta.

## Regras obrigatórias

- Usar “espécie provável”, “altura estimada”, “intervalo” e “não foi possível concluir”.
- Explicar termos na primeira ocorrência: confiança, intervalo de incerteza, qualidade da imagem, marcador, OOD/fora do domínio.
- Erro: o que ocorreu, o que fazer e referência; não culpar usuário nem expor interno.
- Loading: ação real (“Validando a imagem…”, “Analisando características…”); não prometer duração/percentual sem medição.
- Privacidade: finalidade, dados processados, retenção/exclusão e controle do usuário antes do envio.
- Warning: fato + impacto + ação. Inconclusivo é resultado seguro, não “falha” genérica.
- Números usam locale; unidades junto do valor; precisão não excede evidência.

## Biblioteca inicial pt-BR

| Situação | Texto recomendado |
|---|---|
| consentimento | “Usaremos esta imagem somente para realizar a análise descrita abaixo. Consulte como ela é processada e excluída.” |
| loading | “Analisando a imagem. Isso pode levar alguns instantes.” |
| qualidade | “A imagem está escura e pode reduzir a precisão. Tente novamente em um local mais iluminado.” |
| inconclusivo | “Não foi possível produzir uma estimativa confiável com esta imagem.” |
| erro temporário | “O serviço não está disponível agora. Tente novamente. Referência: {requestId}.” |
| resultado | “Espécie provável” / “Altura estimada” / “Faixa estimada” |

Textos proibidos: “100% preciso”, “certeza”, “garantido”, “a IA sabe”, “erro do usuário”, “imagem ruim”, “sem risco”, “anônimo” sem prova, “não armazenamos” se a implementação não comprovar.

## Preparação para en

Chaves sem concatenar frases; plural/gênero via biblioteca i18n; não traduzir IDs/códigos; glossário controla espécie/unidades. Tradução exige revisão humana de produto e a11y, não tradução literal automática publicada.

## Uso correto e incorreto

- Correto: “Confiança estimada: 78%. Fotos semelhantes podem produzir resultados diferentes.”
- Incorreto: “A IA identificou definitivamente sua grama.”

## Checklist

- [ ] Simples, acionável, sem certeza artificial.
- [ ] Privacidade corresponde à implementação.
- [ ] Erro/loading/warning/inconclusivo específicos.
- [ ] Números/unidades/termos explicados.
- [ ] String externalizada e pronta para `en`.

## Riscos e pendências

Nomes de espécies e metas dependem de KAN-23/36/69. Textos legais/consentimento dependem de KAN-31 e revisão humana quando a finalidade for aprovada.
