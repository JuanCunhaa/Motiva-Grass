#!/usr/bin/env python3
"""Perform static-only auditing of vendored public skills."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from skills_common import load_yaml_json, write_yaml_json

SCRIPT_SUFFIXES = {".py", ".sh", ".ps1", ".js", ".mjs", ".cjs", ".ts"}
PATTERNS = {
    "network": re.compile(r"https?://|\bcurl\b|\bwget\b|Invoke-WebRequest|fetch\(|requests\.|urllib|git\s+clone", re.I),
    "secrets": re.compile(r"\b(secret|token|api[_ -]?key|credentials?|\.env|environment variable)\b", re.I),
    "git_mutation": re.compile(r"\bgit\s+(push|merge|commit|checkout|switch|reset|clean)\b", re.I),
    "destructive": re.compile(r"rm\s+-rf|Remove-Item[^\n]*-Recurse|git\s+reset\s+--hard|git\s+clean\s+-[a-z]*f|shutil\.rmtree", re.I),
    "external_action": re.compile(r"\b(upload|publish|deploy|create[_ -]?repo|paid|billing|production)\b", re.I),
}


def scan_text_files(root: Path) -> tuple[Counter[str], list[str]]:
    signals: Counter[str] = Counter()
    executables: list[str] = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        relative = path.relative_to(root).as_posix()
        if path.suffix.lower() in SCRIPT_SUFFIXES:
            executables.append(relative)
        if path.stat().st_size > 3_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for name, pattern in PATTERNS.items():
            signals[name] += len(pattern.findall(text))
    return signals, executables


def build_markdown(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Auditoria de Skills Públicas",
        "",
        "Auditoria estática; nenhum script público foi executado.",
        "",
        "| Skill | Fonte | Commit | Licença | Rede | Scripts | Risco | Status | Restrições |",
        "|---|---|---|---|---:|---:|---|---|---|",
    ]
    for row in rows:
        restrictions = "; ".join(str(item) for item in row["restrictions"]) or "Nenhuma adicional"
        lines.append(
            f"| `{row['id']}` | `{row['source']}` | `{str(row['commit'])[:12]}` | {row['license']} | "
            f"{row['signals'].get('network', 0)} | {len(row['executables'])} | {row['risk']} | "
            f"`{row['audit_status']}` | {restrictions} |"
        )
    lines.extend(["", "Contagens de padrões são indicadores para revisão; exemplos em documentação de segurança podem gerar correspondências sem representar execução.", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--lock", type=Path, default=Path("config/skills/skills-lock.yaml"))
    args = parser.parse_args()
    repo = args.repo.resolve()
    lock_path = args.lock if args.lock.is_absolute() else repo / args.lock
    lock = load_yaml_json(lock_path)
    rows: list[dict[str, object]] = []
    for skill in lock.get("skills", []):
        signals: Counter[str] = Counter()
        executables: list[str] = []
        if skill.get("vendored"):
            signals, executables = scan_text_files(repo / str(skill["vendor_path"]))
        score = signals["destructive"] * 4 + signals["external_action"] * 2 + signals["git_mutation"] + len(executables)
        risk = "HIGH" if score >= 20 else "MEDIUM" if score else "LOW"
        source = lock["sources"][skill["source"]]
        rows.append(
            {
                "id": skill["id"],
                "source": skill["source"],
                "commit": source["commit"],
                "license": source["license"],
                "signals": dict(signals),
                "executables": executables,
                "risk": risk,
                "audit_status": skill["audit_status"],
                "restrictions": skill.get("restrictions", []),
            }
        )
    result = {
        "schema_version": 1,
        "audited_at": datetime.now(timezone.utc).isoformat(),
        "method": "static-only",
        "public_scripts_executed": False,
        "counts": dict(Counter(str(row["audit_status"]) for row in rows)),
        "skills": rows,
    }
    write_yaml_json(repo / "reports/skills/audit-results.json", result)
    markdown = build_markdown(rows)
    output = repo / "docs/governance/PUBLIC_SKILLS_AUDIT.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown, encoding="utf-8")
    print(json.dumps(result["counts"], ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
