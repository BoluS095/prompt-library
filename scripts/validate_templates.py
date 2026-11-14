#!/usr/bin/env python3
"""Validate prompt-library YAML structure and placeholder documentation."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates"
PLACEHOLDER_RE = re.compile(r"(?<!\\)\{([A-Za-z_][A-Za-z0-9_]*)\}")


def validate_template(path: Path, root: Path = TEMPLATE_ROOT) -> list[str]:
    errors: list[str] = []
    try:
        data: Any = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [f"{path}: cannot parse YAML: {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: template must be a YAML mapping"]

    for key in ("name", "model", "category", "prompt", "settings"):
        if key not in data or data[key] in (None, "", {}):
            errors.append(f"{path}: missing required field '{key}'")

    if not isinstance(data.get("settings"), dict):
        errors.append(f"{path}: 'settings' must be a mapping")

    relative = path.relative_to(root)
    expected_category = relative.parts[0] if len(relative.parts) > 1 else None
    if expected_category and data.get("category") != expected_category:
        errors.append(
            f"{path}: category '{data.get('category')}' does not match "
            f"directory '{expected_category}'"
        )

    variables = data.get("variables", {})
    if variables is None:
        variables = {}
    if not isinstance(variables, dict):
        errors.append(f"{path}: 'variables' must be a mapping")
        variables = {}

    prompt = data.get("prompt", "")
    if isinstance(prompt, str):
        placeholders = set(PLACEHOLDER_RE.findall(prompt))
        documented = set(variables)
        for missing in sorted(placeholders - documented):
            errors.append(f"{path}: prompt placeholder '{missing}' is not documented")
        for unused in sorted(documented - placeholders):
            errors.append(f"{path}: variable '{unused}' is not used in prompt")
    else:
        errors.append(f"{path}: 'prompt' must be a string")

    if not data.get("tips") and not data.get("notes"):
        errors.append(f"{path}: add practical 'tips' or 'notes'")

    return errors


def discover_templates(root: Path = TEMPLATE_ROOT) -> list[Path]:
    return sorted(root.rglob("*.yaml"))


def main() -> int:
    templates = discover_templates()
    if not templates:
        print("No YAML templates found.", file=sys.stderr)
        return 1

    errors = [error for path in templates for error in validate_template(path)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"Validation failed: {len(errors)} issue(s) across {len(templates)} template(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(templates)} YAML prompt template(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
