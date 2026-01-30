"""Working with JSON - Exercises

Practice JSON serialization and file-based JSON IO.
Run with:
    python exercises.py
"""

from __future__ import annotations

import json
import os
import tempfile


# =============================================================================
# EXERCISE 1: To JSON String
# =============================================================================


def exercise_1_to_json_string(obj, pretty: bool = False) -> str:
    """Serialize obj to a JSON string. If pretty=True, indent with 2 spaces."""
    if pretty:
        return json.dumps(obj, indent=2, sort_keys=True)
    return json.dumps(obj, separators=(",", ":"), sort_keys=True)


# =============================================================================
# EXERCISE 2: From JSON String
# =============================================================================


def exercise_2_from_json_string(text: str):
    """Parse a JSON string into Python objects."""
    return json.loads(text)


# =============================================================================
# EXERCISE 3: Save JSON
# =============================================================================


def exercise_3_save_json(path: str, obj) -> None:
    """Save obj to a JSON file using UTF-8 and indent=2."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)


# =============================================================================
# EXERCISE 4: Load JSON
# =============================================================================


def exercise_4_load_json(path: str):
    """Load and return a JSON object from a UTF-8 JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running JSON Exercises Tests")
    print("=" * 50)
    all_passed = True

    data = {"b": 2, "a": 1, "items": [3, 2, 1]}

    # Exercise 1
    print("\nExercise 1: To JSON String")
    try:
        s = exercise_1_to_json_string(data)
        # Ensure it's valid JSON and stable ordering due to sort_keys.
        back = json.loads(s)
        status = "PASS" if back == data else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> {s}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 2
    print("\nExercise 2: From JSON String")
    try:
        got = exercise_2_from_json_string('{"x":1,"y":[2,3]}')
        expected = {"x": 1, "y": [2, 3]}
        status = "PASS" if got == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> {got}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 3 & 4
    print("\nExercise 3/4: Save and Load JSON")
    try:
        tmp_dir = tempfile.mkdtemp(prefix="json_ex_")
        path = os.path.join(tmp_dir, "data.json")
        exercise_3_save_json(path, data)
        got = exercise_4_load_json(path)
        status = "PASS" if got == data else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {status} -> loaded matches")
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

