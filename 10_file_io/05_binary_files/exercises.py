"""Binary Files - Exercises

Practice working with bytes, binary file IO, and hashing.
Run with:
    python exercises.py
"""

from __future__ import annotations

import hashlib
import os
import tempfile


# =============================================================================
# EXERCISE 1: XOR Bytes
# =============================================================================


def exercise_1_xor_bytes(data: bytes, key: int) -> bytes:
    """XOR each byte in data with key (0-255) and return the result."""
    if not (0 <= key <= 255):
        raise ValueError("key must be in range 0..255")
    return bytes(b ^ key for b in data)


# =============================================================================
# EXERCISE 2: Write Bytes
# =============================================================================


def exercise_2_write_bytes(path: str, data: bytes) -> int:
    """Write data to path in binary mode. Return number of bytes written."""
    with open(path, "wb") as f:
        return f.write(data)


# =============================================================================
# EXERCISE 3: Read Bytes
# =============================================================================


def exercise_3_read_bytes(path: str) -> bytes:
    """Read all bytes from path."""
    with open(path, "rb") as f:
        return f.read()


# =============================================================================
# EXERCISE 4: Compute SHA-256
# =============================================================================


def exercise_4_compute_sha256(path: str) -> str:
    """Compute the SHA-256 hex digest of a file using chunked reads."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Binary Files Exercises Tests")
    print("=" * 50)
    all_passed = True

    payload = b"abc\x00def"

    # Exercise 1
    print("\nExercise 1: XOR Bytes")
    try:
        got = exercise_1_xor_bytes(b"\x00\x01", 255)
        expected = b"\xff\xfe"
        status = "PASS" if got == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> {got}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 2 & 3
    print("\nExercise 2/3: Write and Read Bytes")
    try:
        tmp_dir = tempfile.mkdtemp(prefix="bin_ex_")
        path = os.path.join(tmp_dir, "blob.bin")
        n = exercise_2_write_bytes(path, payload)
        back = exercise_3_read_bytes(path)
        status = "PASS" if (n == len(payload) and back == payload) else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> wrote={n} bytes")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 4
    print("\nExercise 4: Compute SHA-256")
    try:
        tmp_dir = tempfile.mkdtemp(prefix="bin_hash_")
        path = os.path.join(tmp_dir, "blob.bin")
        with open(path, "wb") as f:
            f.write(payload)
        got = exercise_4_compute_sha256(path)
        expected = hashlib.sha256(payload).hexdigest()
        status = "PASS" if got == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> {got}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    print("\n" + "=" * 50)
    if all_passed:
        print("All tests passed! Great job!")
    else:
        print("Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

