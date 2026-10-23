"""\
Unit Testing - Examples

Shows:
  - unittest style
  - plain `assert` statements (no test framework needed)

Run with:
    python examples.py
"""


import unittest


def clamp(value: int, low: int, high: int) -> int:
    """Return value clamped to [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    if value < low:
        return low
    if value > high:
        return high
    return value


class TestClamp(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_below_range(self):
        self.assertEqual(clamp(-1, 0, 10), 0)

    def test_above_range(self):
        self.assertEqual(clamp(99, 0, 10), 10)

    def test_invalid_bounds(self):
        with self.assertRaises(ValueError):
            clamp(1, 10, 0)


def plain_assert_demo():
    # Plain Python `assert` checks behaviour without any test framework.
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0


if __name__ == "__main__":
    # flush=True so this line appears before unittest writes its report to stderr.
    print("Running unittest example", flush=True)
    unittest.main(exit=False)
    print("\nRunning plain assert statements")
    plain_assert_demo()
    print("OK - Examples complete")

