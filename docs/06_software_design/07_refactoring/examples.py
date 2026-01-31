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

    name = user.get("name", "<unknown>").strip().title()
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
# DEMONSTRATIONS
# =============================================================================


def demo_refactoring():
    print("=" * 60)
    print("Refactoring: Improve structure, keep behavior")
    print("=" * 60)

    users = [
        {"name": "  alice ", "age": 30, "is_active": True},
        {"name": None, "age": None, "is_active": False},
        None,
    ]

    for user in users:
        before = format_user_summary_before(user)
        after = format_user_summary_after(user)
        print(f"before: {before}")
        print(f"after : {after}")
        print(f"same? : {before == after}\n")


if __name__ == "__main__":
    demo_refactoring()
    print("✓ Examples complete!")
