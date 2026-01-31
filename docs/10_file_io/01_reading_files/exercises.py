"""Reading Files - Exercises

Practice reading text files with correct newline/whitespace handling.
Run with:
    python exercises.py
"""

from __future__ import annotations

import tempfile


# =============================================================================
# EXERCISE 1: Read Entire File
# =============================================================================


def exercise_1_read_text_file(path: str) -> str:
    """Return the entire file contents as a string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# =============================================================================
# EXERCISE 2: Read Lines (Stripped)
# =============================================================================


def exercise_2_read_lines_stripped(path: str) -> list[str]:
    """Return a list of lines with trailing newlines removed."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


# =============================================================================
# EXERCISE 3: Count Words
# =============================================================================


def exercise_3_count_words_in_file(path: str) -> int:
    """Count words in the file (split on whitespace)."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    # split() handles multiple spaces/newlines/tabs.
    return len(text.split())


# =============================================================================
# EXERCISE 4: Read First N Lines
# =============================================================================


def exercise_4_read_first_n_lines(path: str, n: int) -> list[str]:
    """Return the first n lines (without trailing newlines)."""
    if n <= 0:
        return []

    result: list[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for _ in range(n):
            line = f.readline()
            if line == "":
                break
            result.append(line.rstrip("\n"))
    return result


# =============================================================================
# TESTS
# =============================================================================


def _make_temp_file(contents: str) -> str:
    tmp = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False)
    try:
        tmp.write(contents)
        return tmp.name
    finally:
        tmp.close()


def run_tests() -> None:
    print("Running Reading Files Exercises Tests")
    print("=" * 50)
    all_passed = True

    path = _make_temp_file("Hello world\nThis is a test\n")

    # Exercise 1
    print("\nExercise 1: Read Entire File")
    try:
        got = exercise_1_read_text_file(path)
        expected = "Hello world\nThis is a test\n"
        status = "PASS" if got == expected else "FAIL"
        if got != expected:
            all_passed = False
        print(f"  {status} content matches")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 2
    print("\nExercise 2: Read Lines (Stripped)")
    try:
        got = exercise_2_read_lines_stripped(path)
        expected = ["Hello world", "This is a test"]
        status = "PASS" if got == expected else "FAIL"
        if got != expected:
            all_passed = False
        print(f"  {status} -> {got}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 3
    print("\nExercise 3: Count Words")
    try:
        got = exercise_3_count_words_in_file(path)
        expected = 6
        status = "PASS" if got == expected else "FAIL"
        if got != expected:
            all_passed = False
        print(f"  {status} -> {got}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 4
    print("\nExercise 4: Read First N Lines")
    try:
        got = exercise_4_read_first_n_lines(path, 1)
        expected = ["Hello world"]
        status = "PASS" if got == expected else "FAIL"
        if got != expected:
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

