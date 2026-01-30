"""\
Unit Testing - Examples

Shows:
  - unittest style
  - pytest-style plain asserts (without requiring pytest)

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


def pytest_style_demo():
    # This looks like pytest, but plain Python `assert` works too.
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0


if __name__ == "__main__":
    print("Running unittest example")
    unittest.main(exit=False)
    print("\nRunning pytest-style assertions")
    pytest_style_demo()
    print("OK - Examples complete")

