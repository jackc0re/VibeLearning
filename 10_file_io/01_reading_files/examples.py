"""Reading Files - Examples

Demonstrates several ways to read text files safely.
Run with:
    python examples.py
"""

from __future__ import annotations

import tempfile


def make_sample_file() -> str:
    """Create a temporary text file and return its path."""
    content = "First line\nSecond line\nThird line\n"
    tmp = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False)
    try:
        tmp.write(content)
        return tmp.name
    finally:
        tmp.close()


def demo_read_all(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    print("Read with f.read():")
    print(text)


def demo_read_lines(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print("Read with f.readlines():")
    print(lines)


def demo_iterate_lines(path: str) -> None:
    print("Iterating line-by-line:")
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}: {line.rstrip()}")


if __name__ == "__main__":
    p = make_sample_file()
    demo_read_all(p)
    demo_read_lines(p)
    # NOTE: line iteration is the most memory-friendly for large files.
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            pass
    print("\n✓ Examples complete!")

