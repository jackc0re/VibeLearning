"""
Refactoring - Examples

Demonstrates behavior-preserving refactoring by extracting functions.
Run with:
    python examples.py
"""

# =============================================================================
# BEFORE: A FUNCTION THAT DOES TOO MUCH
# =============================================================================


def format_user_summary_before(user):
    if user is None:
        return "<missing user>"

    # `or` (not a dict default) so an explicit {"name": None} is handled too
    name = (user.get("name") or "<unknown>").strip().title()
    age = user.get("age")
    if age is None:
        age_part = "age: ?"
    else:
        age_part = f"age: {age}"

    status = "active" if user.get("is_active") else "inactive"
    return f"{name} ({age_part}, {status})"


# =============================================================================
# AFTER: EXTRACT SMALL, NAMED STEPS
# =============================================================================


def normalize_name(raw):
    return (raw or "<unknown>").strip().title()


def format_age(age):
    return "age: ?" if age is None else f"age: {age}"


def format_status(is_active):
    return "active" if is_active else "inactive"


def format_user_summary_after(user):
    if user is None:
        return "<missing user>"

    name = normalize_name(user.get("name"))
    age_part = format_age(user.get("age"))
    status = format_status(user.get("is_active"))
    return f"{name} ({age_part}, {status})"


# =============================================================================
# THE REFACTORING RITUAL: PIN BEHAVIOR, CHANGE, PROVE
# =============================================================================

REFACTORING_CHECKLIST = [
    "1. Run the tests (or examples) BEFORE touching anything",
    "2. Capture the current output as your golden behavior",
    "3. Make ONE small move (extract, rename, guard clause)",
    "4. Re-run and compare. Same behavior? Repeat with the next move.",
]

CASES = [
    {"name": "  alice ", "age": 30, "is_active": True},
    {"name": None, "age": None, "is_active": False},
    None,
]


def prove_behavior_unchanged():
    """After-version must match before-version for every case."""
    for user in CASES:
        expected = format_user_summary_before(user)
        actual = format_user_summary_after(user)
        assert actual == expected, (
            f"behavior changed for {user!r}: {actual!r} != {expected!r}"
        )


# =============================================================================
# DEMONSTRATIONS
# =============================================================================


def demo_refactoring():
    print("=" * 60)
    print("Refactoring: Improve structure, keep behavior")
    print("=" * 60)

    for user in CASES:
        before = format_user_summary_before(user)
        after = format_user_summary_after(user)
        print(f"before: {before}")
        print(f"after : {after}")
        print(f"same? : {before == after}\n")

    prove_behavior_unchanged()
    print("Behavior check: PASS (after == before for every case)")

    print("\nRefactoring checklist:")
    for step in REFACTORING_CHECKLIST:
        print(" ", step)


if __name__ == "__main__":
    demo_refactoring()
    print("PASS Examples complete!")
