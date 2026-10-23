"""Time Complexity - Examples
============================

Small demonstrations of common time-complexity pitfalls.

Run:
    python examples.py
"""

from __future__ import annotations


# =============================================================================
# DEMO: QUADRATIC VS SET-BASED DUPLICATES CHECK
# =============================================================================

def has_duplicates_quadratic(items: list[int]) -> bool:
    """O(n^2): check all pairs."""
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False


def has_duplicates_set(items: list[int]) -> bool:
    """O(n) average: track seen values."""
    seen: set[int] = set()
    for x in items:
        if x in seen:
            return True
        seen.add(x)
    return False


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("TIME COMPLEXITY - Examples")
    print("=" * 50)

    print("\n--- Duplicates: quadratic vs set-based ---\n")
    data = list(range(1000)) + [999]
    print("Quadratic duplicates check:", has_duplicates_quadratic(data))
    print("Set-based duplicates check:", has_duplicates_set(data))

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
