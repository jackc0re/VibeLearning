"""\
Mocking - Exercises

Use mocking to test code that depends on time.

Run with:
    python exercises.py
"""


from __future__ import annotations

from datetime import datetime, timezone
from unittest.mock import patch


def is_weekend(dt: datetime) -> bool:
    """Return True if dt is Saturday (5) or Sunday (6)."""
    return dt.weekday() >= 5


def should_send_newsletter() -> bool:
    """Business rule: send newsletter on weekdays only, using current UTC time."""
    now = datetime.now(timezone.utc)
    return not is_weekend(now)


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Mocking Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Patch datetime used in this module
    module_path = __name__ + ".datetime"

    print("\nExercise: should_send_newsletter")
    try:
        # 2026-01-24 is Saturday
        saturday = datetime(2026, 1, 24, 9, 0, 0, tzinfo=timezone.utc)
        with patch(module_path) as mock_datetime:
            mock_datetime.now.return_value = saturday
            mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)

            ok = should_send_newsletter() is False
            print("  ", "PASS" if ok else "FAIL", "does not send on weekend")
            all_passed = all_passed and ok

        # 2026-01-26 is Monday
        monday = datetime(2026, 1, 26, 9, 0, 0, tzinfo=timezone.utc)
        with patch(module_path) as mock_datetime:
            mock_datetime.now.return_value = monday
            mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)

            ok = should_send_newsletter() is True
            print("  ", "PASS" if ok else "FAIL", "sends on weekday")
            all_passed = all_passed and ok

    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

