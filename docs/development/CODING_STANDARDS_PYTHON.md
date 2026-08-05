# Padrões de Código Python

## Decisão

Propor CPython 3.12.x, `uv`/`uv.lock`, Ruff, mypy estrito e pytest. Python 3.12 é conservador para o ecossistema ML/CUDA; a pinagem final depende de KAN-25/KAN-27/KAN-33. Framework HTTP e framework de ML não são decididos aqui.

## Justificativa

O roadmap exige tipagem, ambientes CPU/GPU reproduzíveis e import sem rede. Embora Python 3.14 seja estável em 2026, 3.12 mantém compatibilidade mais ampla declarada por stacks ML; permanece suportado por segurança até 2028.

## Alternativas

- Python 3.13/3.14: reavaliar quando todas as dependências ML/CV publicarem wheels compatíveis.
- Poetry/pip-tools: válidos; uv é proposto por lock universal e workspaces.
- Pyright: alternativa a mypy; escolher um único verificador oficial.

## Regras obrigatórias

- Type hints em toda API pública e função de produção; `Any` só em adapter isolado, com justificativa e validação imediata.
- Ruff é linter/formatter único; mypy usa modo estrito. Exceção `noqa`/`type: ignore[code]` exige código específico e comentário quando não óbvio.
- Pydantic v2 em modo estrito é proposta para fronteiras/configuração; domínio usa dataclasses/enums/value objects sem depender do framework HTTP.
- Módulos pequenos e coesos; I/O, domínio e computação separados. API não importa `training`, notebooks ou CLI de experimento.
- Configuração declarativa versionada; parâmetros, taxonomia, preprocessing, thresholds e versão de modelo não ficam espalhados em constantes.
- Seed registra Python, NumPy, framework ML e sampler. Declarar operações não determinísticas; nunca prometer determinismo absoluto em GPU sem prova.
- Treino, avaliação e inferência têm entry points e dependências separadas. Test set congelado não é importado por treino.
- Logging estruturado pelo padrão oficial; `print` somente em CLI para saída destinada ao usuário.
- Erros de domínio tipados com código estável; preservar `cause`, não engolir exceções.
- Dependências exatas no lock; perfis CPU/GPU explícitos. Importar pacote nunca baixa peso, dataset, abre rede ou seleciona GPU silenciosamente.
- Serialização: JSON/MessagePack seguro conforme contrato; `pickle`/`torch.load` de origem não confiável proibidos. Artefato exige origem, checksum, formato e compatibilidade.
- Carregamento de modelo é explícito, lazy quando apropriado, com verificação de manifesto/checksum e falha atômica. Sem fallback silencioso para outro peso/modelo.
- CPU é caminho funcional mínimo quando tecnicamente viável; GPU é capability configurada. Divergência/tolerância é testada.
- Memória: limites de imagem/batch, context managers, inferência sem gradiente, liberação de temporários e benchmark. Timeout/cancelamento são propagados entre camadas.
- Testes: unitários puros, propriedades para geometria quando útil, integração de artefato/adapter, contrato, regressão e smoke CPU; GPU marcado e nunca falso-verde.
- CLI via entry point, argumentos tipados, `--help`, códigos de saída, `--dry-run` para ação cara e sem prompt interativo em CI.
- Notebook apenas em `notebooks/`/área de exploração ignorada ou claramente não normativa; sem secrets/dados privados/output pesado. Código final migra para módulo testado.

## Regras recomendadas

- Funções puras e arrays/tensores com shapes/unidades documentados.
- Protocols para ports/adapters; composition root escolhe implementação.
- Docstrings em APIs públicas, matemática, unidades, shapes, exceções e efeitos.
- Hypothesis para invariantes de schemas/geometria.

## Exemplos

```python
def estimate_height(image: ImageArray, *, config: HeightConfig) -> HeightEstimate:
    """Return centimetres and uncertainty; raise ImageRejected for invalid input."""
```

O runtime recebe `ModelArtifactRef`; valida checksum antes de carregar e retorna erro explícito se CUDA solicitada não existir.

## Anti-patterns

- `except Exception: pass`, `# type: ignore` genérico, mutable default ou import com download.
- Notebook como pipeline, seed fixa sem registro, caminho absoluto local ou `pickle` externo.
- API importando loop de treino; fallback de GPU para CPU sem log/capability.

## Checklist

- [ ] Python/uv/lock e grupos CPU/GPU fixados.
- [ ] Ruff, mypy estrito e zero `Any` injustificado.
- [ ] Treino/avaliação/inferência separados.
- [ ] Config, seeds, determinismo e artefatos rastreáveis.
- [ ] Erros/logs, memória, timeout e CPU/GPU tratados.
- [ ] Testes/CLI/docstrings; notebook não normativo.

## Riscos

Python 3.12 entrou em fase de correções de segurança; dependências continuam suportadas, mas a migração deve ser planejada. CUDA pode exigir locks/índices por plataforma.

## Pontos pendentes

- KAN-33 valida versão final, mypy versus Pyright, Pydantic e matriz CUDA.
- KAN-25/KAN-27 auditam stack ML, pesos e licenças.
- Definir formato seguro do modelo em KAN-82.

## Referências externas

- [Status oficial das versões Python](https://devguide.python.org/versions/)
- [Instalação oficial do PyTorch](https://docs.pytorch.org/get-started/locally/)
- [Projetos e lockfile do uv](https://docs.astral.sh/uv/concepts/projects/layout/)
