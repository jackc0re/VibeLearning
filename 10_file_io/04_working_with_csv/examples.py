"""Working with CSV - Examples

Demonstrates reading/writing CSV with both list-based and dict-based APIs.
Run with:
    python examples.py
"""

from __future__ import annotations

import csv
import os
import tempfile


def demo_write_and_read_dicts() -> None:
    tmp_dir = tempfile.mkdtemp(prefix="csv_demo_")
    path = os.path.join(tmp_dir, "people.csv")

    rows = [
        {"name": "Ada", "age": "30"},
        {"name": "Linus", "age": "55"},
    ]

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(rows)

    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        loaded = list(reader)

    print("CSV rows:", loaded)


if __name__ == "__main__":
    demo_write_and_read_dicts()
    print("✓ Examples complete!")

