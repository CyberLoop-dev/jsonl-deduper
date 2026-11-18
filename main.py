#!/usr/bin/env python3
"""Deduplicate JSONL records by canonical JSON or selected dotted keys."""
import argparse
import json
from pathlib import Path
from typing import Any


def nested_value(record: Any, path: str) -> Any:
    value = record
    for part in path.split("."):
        if isinstance(value, dict):
            value = value.get(part)
        else:
            return None
    return value


def signature(record: Any, keys: list[str]) -> str:
    comparable = {key: nested_value(record, key) for key in keys} if keys else record
    return json.dumps(comparable, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def deduplicate(source: Path, destination: Path, keys: list[str], skip_invalid: bool = False) -> tuple[int, int, int]:
    if source.resolve() == destination.resolve():
        raise ValueError("input and output paths must be different")
    seen: set[str] = set()
    kept = duplicates = invalid = 0
    with source.open("r", encoding="utf-8-sig") as input_file, destination.open("w", encoding="utf-8", newline="\n") as output_file:
        for line_number, raw in enumerate(input_file, 1):
            if not raw.strip():
                continue
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                invalid += 1
                if not skip_invalid:
                    raise ValueError(f"line {line_number}: {exc.msg}") from exc
                continue
            key = signature(record, keys)
            if key in seen:
                duplicates += 1
                continue
            seen.add(key)
            output_file.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
            kept += 1
    return kept, duplicates, invalid


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--key", action="append", default=[], help="dotted field path; may be repeated")
    parser.add_argument("--skip-invalid", action="store_true", help="skip malformed lines instead of stopping")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"input file not found: {args.input}")
    try:
        kept, duplicates, invalid = deduplicate(args.input, args.output, args.key, args.skip_invalid)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Kept {kept}; removed {duplicates} duplicates; skipped {invalid} invalid lines.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
