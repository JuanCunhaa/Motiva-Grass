"""Shared, standard-library-only helpers for Motiva-Grass skill governance."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

START_MARKER = "**[MOTIVA-SKILLS:INÍCIO]**"
END_MARKER = "**[MOTIVA-SKILLS:FIM]**"
ROUTABLE_STATUSES = {"APPROVED", "APPROVED_WITH_RESTRICTIONS"}


def load_yaml_json(path: Path) -> dict[str, Any]:
    """Load JSON syntax stored in a YAML 1.2-compatible file."""
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected an object in {path}")
    return value


def write_yaml_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_manifest(root: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for path in sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.as_posix()):
        entries.append(
            {
                "path": path.relative_to(root).as_posix(),
                "size": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return entries


def tree_sha256(entries: Iterable[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for entry in sorted(entries, key=lambda item: str(item["path"])):
        digest.update(f"{entry['path']}\0{entry['size']}\0{entry['sha256']}\n".encode("utf-8"))
    return digest.hexdigest()


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Invalid or missing YAML frontmatter: {path}")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, raw_value = line.partition(":")
        if separator and key.strip() in {"name", "description"}:
            result[key.strip()] = raw_value.strip().strip("'\"")
    if not result.get("name") or not result.get("description"):
        raise ValueError(f"Frontmatter must contain name and description: {path}")
    return result


def replace_jira_section(description: str, section: str) -> str:
    if section.count(START_MARKER) != 1 or section.count(END_MARKER) != 1:
        raise ValueError("Generated section must contain exactly one marker pair")
    start_count = description.count(START_MARKER)
    end_count = description.count(END_MARKER)
    if start_count != end_count or start_count > 1:
        raise ValueError("Existing Jira description has missing or duplicate markers")
    if start_count == 0:
        return f"{description.rstrip()}\n\n{section.strip()}\n"
    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    return pattern.sub(section.strip(), description, count=1)


def ensure_within(root: Path, candidate: Path) -> Path:
    resolved_root = root.resolve()
    resolved_candidate = candidate.resolve()
    if resolved_candidate != resolved_root and resolved_root not in resolved_candidate.parents:
        raise ValueError(f"Path escapes managed root: {candidate}")
    return resolved_candidate

