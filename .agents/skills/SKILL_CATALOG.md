# Catálogo de Agent Skills

## Resumo

- Públicas esperadas: 41
- `APPROVED`: 15
- `APPROVED_WITH_RESTRICTIONS`: 22
- `DISABLED`: 3
- `NOT_FOUND`: 1
- Próprias previstas no prompt: 16, todas `planned` porque não existiam no workspace.
- Wrapper próprio disponível: `motiva-web-guidelines-snapshot`.

## Fontes fixadas

| Fonte | Repositório | Commit | Licença |
|---|---|---|---|
| `github-awesome-copilot` | `github/awesome-copilot` | `940cf68164ea8a44d2e4d7cd9ce24c76eee56ed0` | MIT |
| `vercel-next-skills` | `vercel-labs/next-skills` | `dc1de9caf7612d73f56a8dec3cb1bd6c9ec096b9` | UNIDENTIFIED |
| `vercel-agent-skills` | `vercel-labs/agent-skills` | `7c180d9044c9ae2b442b567aad4e42a28dd5ed62` | MIT |
| `trailofbits` | `trailofbits/skills` | `9ea55c598763f7cb87ab56933d773d7dc34344a0` | CC-BY-SA-4.0 |
| `huggingface` | `huggingface/skills` | `32f8bb0928e95fc9d47ca9fbf69cbfbaf2bc2bda` | Apache-2.0 |

## Inventário público

| Skill | Fonte | Frontmatter | Status | Restrições |
|---|---|---|---|---|
| `agent-skill-stack` | `github-awesome-copilot` | `agent-skill-stack` | `APPROVED_WITH_RESTRICTIONS` | Do not execute installation/staging scripts without explicit approval.; Restrict deletion to a validated staging directory. |
| `acquire-codebase-knowledge` | `github-awesome-copilot` | `acquire-codebase-knowledge` | `APPROVED` |  |
| `make-repo-contribution` | `github-awesome-copilot` | `make-repo-contribution` | `APPROVED` |  |
| `create-specification` | `github-awesome-copilot` | `create-specification` | `APPROVED` |  |
| `create-technical-spike` | `github-awesome-copilot` | `create-technical-spike` | `APPROVED` |  |
| `agentic-eval` | `github-awesome-copilot` | `agentic-eval` | `APPROVED` |  |
| `security-review` | `github-awesome-copilot` | `security-review` | `APPROVED` |  |
| `secret-scanning` | `github-awesome-copilot` | `secret-scanning` | `APPROVED_WITH_RESTRICTIONS` | Do not change repository settings or push protection without the current ticket and authorization. |
| `dependabot` | `github-awesome-copilot` | `dependabot` | `APPROVED_WITH_RESTRICTIONS` | Network and repository configuration changes require the current dependency-governance ticket. |
| `playwright-explore-website` | `github-awesome-copilot` | `playwright-explore-website` | `APPROVED_WITH_RESTRICTIONS` | Use only against an authorized local, preview, or test target.; Do not enter secrets or mutate production data. |
| `playwright-generate-test` | `github-awesome-copilot` | `playwright-generate-test` | `APPROVED_WITH_RESTRICTIONS` | Use only against an authorized local, preview, or test target.; Do not enter secrets or mutate production data. |
| `quality-playbook` | `github-awesome-copilot` | `quality-playbook` | `APPROVED_WITH_RESTRICTIONS` | Run only for a scoped large audit after preserving user changes.; Do not use git clean or destructive recovery commands automatically. |
| `screen-recording` | `github-awesome-copilot` | `screen-recording` | `APPROVED_WITH_RESTRICTIONS` | Capture only authorized windows and sanitized test data.; Review recordings for private or sensitive content before storage. |
| `next-best-practices` | `vercel-next-skills` | `next-best-practices` | `DISABLED` | No license file or license declaration was found in the pinned historical commit.; Do not route until a human records a valid license decision.; Upstream removed or split these skills; validate an alternative separately. |
| `next-cache-components` | `vercel-next-skills` | `next-cache-components` | `DISABLED` | No license file or license declaration was found in the pinned historical commit.; Do not route until a human records a valid license decision.; Upstream removed or split these skills; validate an alternative separately. |
| `vercel-react-best-practices` | `vercel-agent-skills` | `vercel-react-best-practices` | `APPROVED_WITH_RESTRICTIONS` | Activate only when the ticket confirms the relevant Vercel/React context.; Do not create paid resources, change billing, or access production without a human gate. |
| `web-design-guidelines` | `vercel-agent-skills` | `web-design-guidelines` | `APPROVED_WITH_RESTRICTIONS` | Activate only when the ticket confirms the relevant Vercel/React context.; Do not create paid resources, change billing, or access production without a human gate. |
| `vercel-optimize` | `vercel-agent-skills` | `vercel-optimize` | `APPROVED_WITH_RESTRICTIONS` | Activate only when the ticket confirms the relevant Vercel/React context.; Do not create paid resources, change billing, or access production without a human gate. |
| `audit-context-building` | `trailofbits` | `audit-context-building` | `APPROVED` | Preserve CC-BY-SA-4.0 attribution and keep vendor copies unmodified. |
| `differential-review` | `trailofbits` | `differential-review` | `APPROVED` | Preserve CC-BY-SA-4.0 attribution and keep vendor copies unmodified. |
| `property-based-testing` | `trailofbits` | `property-based-testing` | `APPROVED` | Preserve CC-BY-SA-4.0 attribution and keep vendor copies unmodified. |
| `dimensional-analysis` | `trailofbits` | `dimensional-analysis` | `APPROVED` | Preserve CC-BY-SA-4.0 attribution and keep vendor copies unmodified. |
| `sharp-edges` | `trailofbits` | `sharp-edges` | `APPROVED` | Preserve CC-BY-SA-4.0 attribution and keep vendor copies unmodified. |
| `insecure-defaults` | `trailofbits` | `insecure-defaults` | `APPROVED` | Preserve CC-BY-SA-4.0 attribution and keep vendor copies unmodified. |
| `supply-chain-risk-auditor` | `trailofbits` | `supply-chain-risk-auditor` | `APPROVED` | Preserve CC-BY-SA-4.0 attribution and keep vendor copies unmodified. |
| `fp-check` | `trailofbits` | `fp-check` | `APPROVED` | Preserve CC-BY-SA-4.0 attribution and keep vendor copies unmodified. |
| `variant-analysis` | `trailofbits` | `variant-analysis` | `APPROVED` | Preserve CC-BY-SA-4.0 attribution and keep vendor copies unmodified. |
| `modern-python` | `trailofbits` | `modern-python` | `APPROVED_WITH_RESTRICTIONS` | Package installation and network access require an explicit ticket step.; Preserve CC-BY-SA-4.0 attribution. |
| `mutation-testing` | `trailofbits` | `mutation-testing` | `APPROVED_WITH_RESTRICTIONS` | Run only after the base suite is stable and compute budget is appropriate.; Preserve CC-BY-SA-4.0 attribution. |
| `agentic-actions-auditor` | `trailofbits` | `agentic-actions-auditor` | `APPROVED_WITH_RESTRICTIONS` | Use only for authorized GitHub Actions workflows; never expose secrets.; Preserve CC-BY-SA-4.0 attribution. |
| `semgrep-rule-creator` | `trailofbits` | `semgrep-rule-creator` | `APPROVED_WITH_RESTRICTIONS` | Activate only for the rule-authoring purpose named by the skill.; Preserve CC-BY-SA-4.0 attribution. |
| `semgrep-rule-variant-creator` | `trailofbits` | `semgrep-rule-variant-creator` | `APPROVED_WITH_RESTRICTIONS` | Activate only for the rule-authoring purpose named by the skill.; Preserve CC-BY-SA-4.0 attribution. |
| `second-opinion` | `trailofbits` | `second-opinion` | `APPROVED_WITH_RESTRICTIONS` | External model or CLI use requires explicit authorization and a non-sensitive code scope.; Preserve CC-BY-SA-4.0 attribution. |
| `static-analysis` | `trailofbits` | `—` | `NOT_FOUND` | The selector is a plugin containing codeql, sarif-parsing, and semgrep; no root SKILL.md or frontmatter name static-analysis exists.; Do not substitute a child skill without human validation. |
| `skill-improver` | `trailofbits` | `skill-improver` | `DISABLED` | Requires the unavailable plugin-dev/skill-reviewer dependency.; Automated edit/review hooks are not permitted in ordinary ticket execution. |
| `hf-cli` | `huggingface` | `hf-cli` | `APPROVED_WITH_RESTRICTIONS` | Activate only for a technically related Hugging Face ticket.; No upload, publication, Hub repository mutation, Space, paid Job, or paid GPU without an explicit human gate. |
| `huggingface-datasets` | `huggingface` | `huggingface-datasets` | `APPROVED_WITH_RESTRICTIONS` | Activate only for a technically related Hugging Face ticket.; No upload, publication, Hub repository mutation, Space, paid Job, or paid GPU without an explicit human gate. |
| `huggingface-trackio` | `huggingface` | `huggingface-trackio` | `APPROVED_WITH_RESTRICTIONS` | Activate only for a technically related Hugging Face ticket.; No upload, publication, Hub repository mutation, Space, paid Job, or paid GPU without an explicit human gate. |
| `huggingface-vision-trainer` | `huggingface` | `huggingface-vision-trainer` | `APPROVED_WITH_RESTRICTIONS` | Activate only for a technically related Hugging Face ticket.; No upload, publication, Hub repository mutation, Space, paid Job, or paid GPU without an explicit human gate. |
| `hf-mem` | `huggingface` | `hf-mem` | `APPROVED_WITH_RESTRICTIONS` | Activate only for a technically related Hugging Face ticket.; No upload, publication, Hub repository mutation, Space, paid Job, or paid GPU without an explicit human gate. |
| `huggingface-best` | `huggingface` | `huggingface-best` | `APPROVED_WITH_RESTRICTIONS` | Activate only for a technically related Hugging Face ticket.; No upload, publication, Hub repository mutation, Space, paid Job, or paid GPU without an explicit human gate. |

