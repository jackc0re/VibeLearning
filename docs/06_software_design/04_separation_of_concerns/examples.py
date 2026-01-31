"""
Separation of Concerns - Examples

Shows how separating I/O from business logic improves reuse and testability.
Run with:
    python examples.py
"""

# =============================================================================
# PURE / CORE LOGIC
# =============================================================================

def parse_numbers(text):
    """Parse comma-separated integers: '1,2,3' -> [1,2,3]."""
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def average(nums):
    """Business logic: compute average. Return None for empty."""
    if not nums:
        return None
    return sum(nums) / len(nums)


def format_average(avg):
    """Presentation concern."""
    if avg is None:
        return "No numbers provided"
    return f"Average: {avg:.2f}"


# =============================================================================
# I/O / EDGE CODE
# =============================================================================

def run_program():
    text = "1, 2, 3, 4"  # pretend this came from input() or a file
    nums = parse_numbers(text)
    avg = average(nums)
    output = format_average(avg)
    print(output)


if __name__ == "__main__":
    print("=" * 60)
    print("Separation of Concerns")
    print("=" * 60)
    run_program()
    print("\n✓ Examples complete!")
