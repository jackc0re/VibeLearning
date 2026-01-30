"""Working with CSV - Exercises

Practice reading and writing CSV files safely.
Run with:
    python exercises.py
"""

from __future__ import annotations

import csv
import os
import tempfile


# =============================================================================
# EXERCISE 1: Read CSV Rows
# =============================================================================


def exercise_1_read_csv_rows(path: str) -> list[list[str]]:
    """Read a CSV file and return all rows as lists of strings (including header)."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        return [row for row in reader]


# =============================================================================
# EXERCISE 2: Read CSV as Dicts
# =============================================================================


def exercise_2_read_csv_as_dicts(path: str) -> list[dict[str, str]]:
    """Read a CSV file with headers and return rows as dicts."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


# =============================================================================
# EXERCISE 3: Write Dicts to CSV
# =============================================================================


def exercise_3_write_dicts_to_csv(
    path: str,
    fieldnames: list[str],
    rows: list[dict[str, str]],
) -> None:
    """Write rows (dicts) to a CSV file with a header."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# =============================================================================
# EXERCISE 4: Sum Numeric Column
# =============================================================================


def exercise_4_sum_csv_column(path: str, column_name: str) -> float:
    """Sum a numeric column from a header-based CSV. Raises ValueError if missing."""
    total = 0.0
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or column_name not in reader.fieldnames:
            raise ValueError(f"Missing column: {column_name}")

        for row in reader:
            raw = (row.get(column_name) or "").strip()
            if raw == "":
                continue
            total += float(raw)
    return total


# =============================================================================
# TESTS
# =============================================================================


def _write_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def run_tests() -> None:
    print("Running CSV Exercises Tests")
    print("=" * 50)
    all_passed = True

    tmp_dir = tempfile.mkdtemp(prefix="csv_ex_")
    path = os.path.join(tmp_dir, "data.csv")
    _write_text(path, "name,amount\nAda,10\nBob,2.5\nEve,\n")

    # Exercise 1
    print("\nExercise 1: Read CSV Rows")
    try:
        got = exercise_1_read_csv_rows(path)
        expected = [
            ["name", "amount"],
            ["Ada", "10"],
            ["Bob", "2.5"],
            ["Eve", ""],
        ]
        status = "PASS" if got == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> rows={len(got)}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 2
    print("\nExercise 2: Read CSV as Dicts")
    try:
        got = exercise_2_read_csv_as_dicts(path)
        expected_first = {"name": "Ada", "amount": "10"}
        status = "PASS" if (len(got) == 3 and got[0] == expected_first) else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> first={got[0]}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 3
    print("\nExercise 3: Write Dicts to CSV")
    try:
        out = os.path.join(tmp_dir, "out.csv")
        exercise_3_write_dicts_to_csv(
            out,
            fieldnames=["name", "amount"],
            rows=[{"name": "X", "amount": "1"}],
        )
        rows = exercise_1_read_csv_rows(out)
        status = "PASS" if rows == [["name", "amount"], ["X", "1"]] else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> {rows}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 4
    print("\nExercise 4: Sum Numeric Column")
    try:
        got = exercise_4_sum_csv_column(path, "amount")
        expected = 12.5
        status = "PASS" if abs(got - expected) < 1e-9 else "FAIL"
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

