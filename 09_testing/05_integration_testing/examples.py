"""\
Integration Testing - Examples

Example: write JSON to disk and read it back.
This is an integration test because it crosses the filesystem boundary.

Run with:
    python examples.py
"""


import json
import tempfile
from pathlib import Path


def save_settings(path: Path, settings: dict) -> None:
    path.write_text(json.dumps(settings, indent=2), encoding="utf-8")


def load_settings(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def demo_integration_test():
    with tempfile.TemporaryDirectory() as tmp:
        file_path = Path(tmp) / "settings.json"

        expected = {"theme": "dark", "page_size": 25}
        save_settings(file_path, expected)
        actual = load_settings(file_path)

        assert actual == expected
        print("OK - Integration demo passed")


if __name__ == "__main__":
    demo_integration_test()

