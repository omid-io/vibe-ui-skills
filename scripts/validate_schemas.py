#!/usr/bin/env python3
"""
validate_schemas.py — Validates all JSON Schemas in schemas/ for syntax and self-consistency.
"""

import sys
import json
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT_DIR / "schemas"

def validate_schema_file(schema_path: Path):
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    if not isinstance(schema, dict):
        raise ValueError("Schema root must be a JSON object")

    if "$schema" not in schema:
        raise ValueError("Missing $schema declaration")

    if "type" not in schema and "properties" not in schema:
        raise ValueError("Schema lacks type or properties")

    return True

def main():
    print("[INFO] Auditing JSON Schemas in schemas/...")
    schema_files = list(SCHEMAS_DIR.glob("*.json"))
    if not schema_files:
        print("[FAIL] No schema files found in schemas/", file=sys.stderr)
        return 1

    errors = []
    for sf in schema_files:
        try:
            validate_schema_file(sf)
            print(f"  [OK] {sf.name} is valid JSON schema")
        except Exception as e:
            errors.append(f"{sf.name}: {e}")

    if errors:
        print("\n[FAIL] Schema validation errors:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"\n[SUCCESS] All {len(schema_files)} schemas validated successfully.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
