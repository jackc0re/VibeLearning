"""\
Integration Testing - Exercises

Test a simple "load -> validate -> transform" pipeline that touches the filesystem.

Run with:
    python exercises.py
"""


from __future__ import annotations

import csv
import tempfile
from pathlib import Path


def load_scores_csv(path: Path) -> list[dict]:
    """Load a CSV with columns: name, score.

Return a list of dicts like: {"name": str, "score": int}
Raise ValueError if a score is not an integer.
"""
    rows: list[dict] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                score = int(r["score"])
            except Exception as exc:
                raise ValueError(f"Invalid score: {r.get('score')!r}") from exc
            rows.append({"name": r["name"], "score": score})
    return rows


def average_score(rows: list[dict]) -> float:
    if not rows:
        raise ValueError("rows must be non-empty")
    return sum(r["score"] for r in rows) / len(rows)


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Integration Testing Exercises Tests")
    print("=" * 50)
    all_passed = True

    print("\nExercise: load_scores_csv + average_score")
    try:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scores.csv"
            path.write_text(
                "name,score\nAda,10\nBob,20\n",
                encoding="utf-8",
            )
            rows = load_scores_csv(path)
            ok = rows == [{"name": "Ada", "score": 10}, {"name": "Bob", "score": 20}]
            print("  ", "PASS" if ok else "FAIL", "loads rows")
            all_passed = all_passed and ok

            avg = average_score(rows)
            ok = abs(avg - 15.0) < 1e-9
            print("  ", "PASS" if ok else "FAIL", "average is", avg)
            all_passed = all_passed and ok

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.csv"
            path.write_text(
                "name,score\nAda,not-a-number\n",
                encoding="utf-8",
            )
            try:
                load_scores_csv(path)
                all_passed = False
                print("  FAIL did not raise for invalid score")
            except ValueError:
                print("  PASS raises for invalid score")

    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

