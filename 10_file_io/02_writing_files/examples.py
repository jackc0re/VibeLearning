"""Writing Files - Examples

Demonstrates writing and appending to text files.
Run with:
    python examples.py
"""

from __future__ import annotations

import os
import tempfile


def demo_write_and_read_back() -> None:
    tmp_dir = tempfile.mkdtemp(prefix="file_io_demo_")
    path = os.path.join(tmp_dir, "demo.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")

    with open(path, "a", encoding="utf-8") as f:
        f.write("Line 3 (appended)\n")

    with open(path, "r", encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    demo_write_and_read_back()
    print("✓ Examples complete!")

