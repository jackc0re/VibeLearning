"""Writing Files - Exercises

Practice writing/overwriting/appending and copying text files.
Run with:
    python exercises.py
"""

from __future__ import annotations

import os
import tempfile


# =============================================================================
# EXERCISE 1: Write Text File
# =============================================================================


def exercise_1_write_text_file(path: str, content: str) -> int:
    """Write content to path (overwrite). Return the number of characters written."""
    with open(path, "w", encoding="utf-8") as f:
        written = f.write(content)
    return written


# =============================================================================
# EXERCISE 2: Append Line
# =============================================================================


def exercise_2_append_line(path: str, line: str) -> None:
    """Append a line (ensure exactly one trailing newline is written)."""
    line_to_write = line.rstrip("\n") + "\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(line_to_write)


# =============================================================================
# EXERCISE 3: Write Lines
# =============================================================================


def exercise_3_write_lines(path: str, lines: list[str]) -> None:
    """Overwrite a file with lines, each ending with a newline."""
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.rstrip("\n") + "\n")


# =============================================================================
# EXERCISE 4: Copy File
# =============================================================================


def exercise_4_copy_text_file(src_path: str, dst_path: str) -> None:
    """Copy text from src_path to dst_path."""
    with open(src_path, "r", encoding="utf-8") as src:
        data = src.read()
    with open(dst_path, "w", encoding="utf-8") as dst:
        dst.write(data)


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Writing Files Exercises Tests")
    print("=" * 50)
    all_passed = True

    tmp_dir = tempfile.mkdtemp(prefix="file_io_write_")
    p1 = os.path.join(tmp_dir, "out.txt")
    p2 = os.path.join(tmp_dir, "copy.txt")

    # Exercise 1
    print("\nExercise 1: Write Text File")
    try:
        n = exercise_1_write_text_file(p1, "abc\n")
        with open(p1, "r", encoding="utf-8") as f:
            got = f.read()
        status = "PASS" if (n == 4 and got == "abc\n") else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> wrote={n}, got={got!r}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 2
    print("\nExercise 2: Append Line")
    try:
        exercise_2_append_line(p1, "line")
        exercise_2_append_line(p1, "line2\n")
        with open(p1, "r", encoding="utf-8") as f:
            got = f.read()
        expected_end = "abc\nline\nline2\n"
        status = "PASS" if got == expected_end else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> {got!r}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 3
    print("\nExercise 3: Write Lines")
    try:
        exercise_3_write_lines(p1, ["a", "b\n", "c"])
        with open(p1, "r", encoding="utf-8") as f:
            got = f.read()
        status = "PASS" if got == "a\nb\nc\n" else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> {got!r}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 4
    print("\nExercise 4: Copy File")
    try:
        exercise_4_copy_text_file(p1, p2)
        with open(p2, "r", encoding="utf-8") as f:
            got = f.read()
        status = "PASS" if got == "a\nb\nc\n" else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> copied content matches")
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

