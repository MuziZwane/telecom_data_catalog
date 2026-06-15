"""Dataset scanner utilities."""

from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _infer_type(values: list[str]) -> str:
    """Infer a simple data type from non-empty string values."""
    non_empty = [value for value in values if value != ""]
    if not non_empty:
        return "string"

    if all(_is_int(value) for value in non_empty):
        return "integer"
    if all(_is_float(value) for value in non_empty):
        return "number"
    if all(_is_date(value) for value in non_empty):
        return "date"
    return "string"


def _is_int(value: str) -> bool:
    try:
        int(value)
    except ValueError:
        return False
    return True


def _is_float(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    return True


def _is_date(value: str) -> bool:
    try:
        datetime.fromisoformat(value)
    except ValueError:
        return False
    return True


def scan_csv(path: str | Path, dataset_name: str | None = None) -> dict[str, Any]:
    """Scan a CSV file and return baseline catalog metadata."""
    csv_path = Path(path)
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    columns = []
    for field in fieldnames:
        values = [row.get(field, "") for row in rows]
        columns.append({"name": field, "type": _infer_type(values)})

    modified_at = datetime.fromtimestamp(csv_path.stat().st_mtime, tz=timezone.utc)
    return {
        "name": dataset_name or csv_path.stem,
        "source": str(csv_path),
        "format": "csv",
        "row_count": len(rows),
        "freshness": modified_at.isoformat(),
        "columns": columns,
    }
