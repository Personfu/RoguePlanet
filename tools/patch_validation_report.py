#!/usr/bin/env python3
"""Render patch-validation notes for an owned lab or authorized assessment."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def render(data: dict[str, Any]) -> str:
    lines = [
        '# Patch Validation Report',
        '',
        f"System: {data.get('system', 'TBD')}",
        f"Patch window: {data.get('patch_window', 'TBD')}",
        f"Validator: {data.get('validator', 'TBD')}",
        '',
        '## Validation Checks',
        '',
        '| Check | Result | Evidence |',
        '|---|---|---|',
    ]
    for check in data.get('checks', []):
        lines.append(f"| {check.get('name','TBD')} | {check.get('result','TBD')} | {check.get('evidence','TBD')} |")
    lines.extend(['', '## Residual Risk', '', data.get('residual_risk', 'TBD'), ''])
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='Render patch validation report markdown.')
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    args.output.write_text(render(json.loads(args.input.read_text(encoding='utf-8'))), encoding='utf-8')
    print(f'wrote {args.output}')


if __name__ == '__main__':
    main()
