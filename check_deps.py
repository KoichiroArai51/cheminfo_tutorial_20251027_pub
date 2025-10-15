#!/usr/bin/env python3
"""
check_deps.py

Usage:
  python3 check_deps.py path/to/file.py

This script parses top-level import statements from the given Python file and
attempts to import each referenced top-level module. It prints which modules
are present and which are missing, and returns exit code 0 when all imports
are available, or 1 when some are missing.

It intentionally keeps suggestions simple (``pip install <module>``). For some
packages (for example `rdkit`) users may need to prefer conda installs.
"""
from __future__ import annotations

import argparse
import ast
import importlib
import os
import sys
from typing import Set, List


def extract_top_level_modules_from_file(path: str) -> List[str]:
    """Parse a Python file and return a sorted list of top-level module names.

    Examples:
      - from rdkit import Chem  -> rdkit
      - import numpy as np    -> numpy
      - import a.b.c          -> a
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    with open(path, "r", encoding="utf-8") as f:
        contents = f.read()

    try:
        tree = ast.parse(contents, filename=path)
    except SyntaxError:
        raise

    mods: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split(".")[0]
                mods.add(top)
        elif isinstance(node, ast.ImportFrom):
            # skip relative imports
            if node.module:
                top = node.module.split(".")[0]
                mods.add(top)

    # Remove built-ins and local package names if desired? Keep all for reporting.
    return sorted(mods)


def check_modules(modules: List[str]) -> int:
    """Try to import each module and print status lines. Returns number of missing."""
    missing_count = 0
    for mod in modules:
        # skip standard library heuristics? We'll just try importing.
        try:
            importlib.import_module(mod)
            print(f"OK     {mod}")
        except Exception:
            missing_count += 1
            hint = f"pip install {mod}"
            if mod.lower() == "rdkit":
                hint = "conda install -c conda-forge rdkit  # or pip install rdkit-pypi"
            print(f"MISSING {mod}  -> {hint}")

    return missing_count


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check whether imports in a Python file are installed")
    parser.add_argument("path", help="Python file to scan for imports")
    parser.add_argument("--json", action="store_true", help="(reserved) output JSON")
    args = parser.parse_args(argv)

    try:
        modules = extract_top_level_modules_from_file(args.path)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.path}", file=sys.stderr)
        return 2
    except SyntaxError as e:
        print(f"ERROR: could not parse {args.path}: {e}", file=sys.stderr)
        return 2

    if not modules:
        print("No imports found in file.")
        return 0

    print(f"Checking {len(modules)} top-level module(s): {', '.join(modules)}\n")
    missing = check_modules(modules)

    if missing:
        print(f"\n{missing} module(s) missing")
        return 1
    print("\nAll modules appear to be importable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
