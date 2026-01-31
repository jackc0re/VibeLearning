"""Binary Files - Examples

Demonstrates writing bytes and computing a simple hash.
Run with:
    python examples.py
"""

from __future__ import annotations

import hashlib
import os
import tempfile


def demo_binary_and_hash() -> None:
    tmp_dir = tempfile.mkdtemp(prefix="bin_demo_")
    path = os.path.join(tmp_dir, "blob.bin")
    payload = b"hello\x00world"

    with open(path, "wb") as f:
        f.write(payload)

    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)

    print("sha256:", h.hexdigest())


if __name__ == "__main__":
    demo_binary_and_hash()
    print("✓ Examples complete!")

