"""
KISS Principle - Examples

Shows how simpler code is usually clearer and safer.
Run with:
    python examples.py
"""

# =============================================================================
# EXAMPLE 1: OVER-COMPLICATED VS SIMPLE
# =============================================================================


def is_even_overcomplicated(n):
    """A silly example of unnecessary complexity."""
    return (n % 2) == 0 and True or False


def is_even_simple(n):
    """Clear, direct expression."""
    return n % 2 == 0


# =============================================================================
# EXAMPLE 2: EARLY RETURNS REDUCE NESTING
# =============================================================================


def can_edit_user_profile(user):
    """Prefer early returns for clarity."""
    if user is None:
        return False
    if not user.get("is_active"):
        return False
    if "edit" not in user.get("permissions", []):
        return False
    return True


# =============================================================================
# DEMONSTRATIONS
# =============================================================================


def demo_kiss():
    print("=" * 60)
    print("KISS: Keep It Simple")
    print("=" * 60)

    for n in [0, 1, 2, 3, 4]:
        print(f"{n}: even_overcomplicated={is_even_overcomplicated(n)}, even_simple={is_even_simple(n)}")

    user_ok = {"is_active": True, "permissions": ["edit"]}
    user_no = {"is_active": False, "permissions": ["edit"]}

    print("\nEarly returns reduce nesting:")
    print(f"can_edit_user_profile(None) -> {can_edit_user_profile(None)}")
    print(f"can_edit_user_profile(user_no) -> {can_edit_user_profile(user_no)}")
    print(f"can_edit_user_profile(user_ok) -> {can_edit_user_profile(user_ok)}")


if __name__ == "__main__":
    demo_kiss()
    print("\n✓ Examples complete!")
