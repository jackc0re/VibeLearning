"""
Coupling and Cohesion - Examples

Demonstrates reducing coupling and increasing cohesion.
Run with:
    python examples.py
"""

# =============================================================================
# TIGHT COUPLING (FOR CONTRAST)
# =============================================================================


def send_welcome_email_tightly_coupled(user_email):
    """
    Overly coupled: hard-coded dependencies and side effects.
    (Here we just print, but imagine a real email service.)
    """
    print(f"Sending welcome email to {user_email}")


# =============================================================================
# LOOSER COUPLING VIA DEPENDENCY INJECTION
# =============================================================================


def send_welcome_email(email_sender, user_email):
    """Looser coupling: caller supplies the dependency."""
    email_sender(user_email)


def console_email_sender(address):
    print(f"[email] Welcome -> {address}")


# =============================================================================
# COHESION EXAMPLE
# =============================================================================


class OrderTotals:
    """High cohesion: one focused responsibility (price calculations)."""

    def __init__(self, items):
        self._items = items

    def subtotal(self):
        return sum(price for _, price in self._items)

    def with_tax(self, tax_rate):
        return self.subtotal() * (1 + tax_rate)


# =============================================================================
# DEMONSTRATIONS
# =============================================================================


def demo_coupling_and_cohesion():
    print("=" * 60)
    print("Coupling and Cohesion")
    print("=" * 60)

    # Coupling
    print("\nLooser coupling example:")
    send_welcome_email(console_email_sender, "user@example.com")

    # Cohesion
    print("\nHigh cohesion example:")
    items = [("book", 10.0), ("pen", 2.0)]
    totals = OrderTotals(items)
    print(f"Subtotal: {totals.subtotal():.2f}")
    print(f"With tax (10%): {totals.with_tax(0.10):.2f}")


if __name__ == "__main__":
    demo_coupling_and_cohesion()
    print("\n✓ Examples complete!")
