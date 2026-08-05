# Política de Gates Humanos

## Objetivo

Limitar intervenção humana a decisões, ações e riscos que realmente não podem ser assumidos autonomamente, sem transformar aprovação futura em bloqueio prematuro.

## Escopo

Aplica-se a tickets com licença, negócio, escopo, ação física, credencial, administração, contratação, custo, produção, aceite de risco, promoção de modelo ou release.

## Regras obrigatórias

### Quando usar `gate-human`

A label deve existir quando o ticket contém uma necessidade humana real e identificável de:

- aprovação de licença ou escolha da licença do produto;
- decisão de negócio ou alteração significativa de escopo;
- coleta, impressão ou medição física;
- fornecimento de credencial ou acesso administrativo;
- contratação, assinatura, quota ou recurso pago;
- alteração em produção ou domínio público;
- aceitação de risco material de segurança, privacidade, dados ou compliance;
- promoção de modelo;
- criação/publicação de tag ou release final.

A descrição deve identificar o gate, o papel decisor, evidência esperada e momento em que será necessário. `gate-human` não significa que todo o ticket esteja bloqueado desde a criação.

### Ausência da label

Sem `gate-human`, a IA ou o desenvolvedor pode tomar decisões técnicas reversíveis dentro do escopo e das regras versionadas. Não deve pedir confirmação para criar arquivos internos, corrigir lint/tipagem, executar testes locais, criar fixtures identificadas, escolher nomes coerentes, fazer pequena refatoração diretamente relacionada ou criar documentação técnica.

### Quando o gate vira impedimento ativo

O gate torna-se ativo quando sua decisão/ação é pré-condição do próximo passo útil, necessária para validar evidência atual ou exigida antes de uma ação irreversível/externa. Nesse instante:

1. não executar a ação protegida;
2. aplicar `Flagged = Impediment` e label de causa;
3. comentar motivo, evidência, decisor, ação, impacto e partes que podem avançar;
4. deixar ou devolver a `Tarefas pendentes` se não houver trabalho legítimo;
5. solicitar somente a decisão mínima necessária;
6. retomar após evidência explícita, remover Flagged e revalidar DoR.

Gate futuro não ativo não bloqueia planejamento, código local reversível ou preparação de documentos, desde que esses trabalhos não pressuponham a aprovação.

### Formato da solicitação humana

```markdown
## Gate humano ativo
- Decisão/ação requerida: <uma ação>
- Papel decisor: <owner, não necessariamente pessoa nominal>
- Evidência necessária: <aprovação, medição, acesso, registro>
- Prazo/condição: <quando necessário>
- Opções e impactos: <alternativas reais>
- Recomendação técnica: <se houver>
- Ação protegida que não será executada: <produção, gasto etc.>
- Trabalho que ainda pode avançar: <lista ou nenhum>
```

### Decisão e evidência

`Aprovado` em conversa privada não basta. Registrar no Jira a decisão, decisor, data, escopo exato, limitações e evidência; atualizar ADR/documento quando duradoura. Nunca registrar a própria credencial: apenas confirmar disponibilização no mecanismo seguro.

Aceite de risco deve conter risco, impacto, probabilidade, controles, validade, owner e condição de revisão. Aprovação de custo deve conter teto, moeda, período e recurso autorizado. Aprovação de produção/release deve identificar artefato exato, checksum/tag e rollback.

## Regras recomendadas

- Separar gate de preparação e gate de execução quando ocorrem em momentos diferentes.
- Pedir decisão com opções e recomendação, evitando pergunta vaga.
- Definir expiração para aceites de risco e credenciais temporárias.
- Evitar colocar `gate-human` no Épico se somente tickets específicos exigem ação humana.

## Exemplos corretos

- KAN-99 pode preparar protocolo; torna-se impedida quando precisa de impressão e medição reais.
- KAN-97 compara opções sem gasto; o gate ativa antes de criar recurso pago ou publicar produção.
- KAN-140 implementa promoção localmente; a promoção de produção exige aprovação do artefato exato.

## Exemplos incorretos

- Pedir permissão para rodar lint local em ticket sem gate.
- Marcar Flagged no início porque uma release futura exigirá aprovação.
- Interpretar silêncio como aceite de risco.
- Colar secret no comentário como evidência de acesso.

## Exceções

Resposta a incidente pode executar ação previamente autorizada em runbook e limite de competência, registrando-a de imediato. Ação emergencial fora do runbook ainda exige autoridade humana. Se o decisor e o executor forem a mesma pessoa, a decisão continua sendo registrada separadamente da execução.

## Checklist

- [ ] O gate corresponde a necessidade humana real da lista autorizada.
- [ ] Papel, momento, evidência e ação protegida estão definidos.
- [ ] Flagged só foi aplicada quando o gate ficou ativo.
- [ ] Trabalho reversível permitido não foi bloqueado desnecessariamente.
- [ ] Decisão foi registrada no Jira e documento oficial aplicável.
- [ ] Credencial/segredo não foi exposto.
- [ ] Retomada removeu o impedimento e revalidou a DoR.

