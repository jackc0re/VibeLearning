"""Working with JSON - Examples

Demonstrates serializing/deserializing JSON strings and files.
Run with:
    python examples.py
"""

from __future__ import annotations

import json
import os
import tempfile


def demo_json_string() -> None:
    data = {"name": "Ada", "age": 30, "skills": ["python", "math"]}
    text = json.dumps(data, indent=2, sort_keys=True)
    print("JSON string:\n", text)

    back = json.loads(text)
    print("Back to Python:", back)


def demo_json_file() -> None:
    tmp_dir = tempfile.mkdtemp(prefix="json_demo_")
    path = os.path.join(tmp_dir, "data.json")
    data = {"ok": True, "items": [1, 2, 3]}

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    with open(path, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("Loaded from file:", loaded)


if __name__ == "__main__":
    demo_json_string()
    demo_json_file()
    print("✓ Examples complete!")

