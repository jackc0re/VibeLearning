"""
DRY Principle - Examples

Demonstrates removing duplication by extracting shared logic.
Run with:
    python examples.py
"""

# =============================================================================
# BEFORE: DUPLICATION
# =============================================================================

def total_price_before(items, tax_rate, shipping_fee):
    """Duplicated calculation pattern."""
    subtotal = sum(price for _, price in items)
    taxed = subtotal + (subtotal * tax_rate)
    return taxed + shipping_fee


def refund_amount_before(items, tax_rate, restocking_fee):
    """Duplicated calculation pattern (same idea, different place)."""
    subtotal = sum(price for _, price in items)
    taxed = subtotal + (subtotal * tax_rate)
    return taxed - restocking_fee


# =============================================================================
# AFTER: SINGLE SOURCE OF TRUTH
# =============================================================================

def calculate_subtotal(items):
    return sum(price for _, price in items)


def apply_tax(amount, tax_rate):
    return amount * (1 + tax_rate)


def total_price_after(items, tax_rate, shipping_fee):
    subtotal = calculate_subtotal(items)
    return apply_tax(subtotal, tax_rate) + shipping_fee


def refund_amount_after(items, tax_rate, restocking_fee):
    subtotal = calculate_subtotal(items)
    return apply_tax(subtotal, tax_rate) - restocking_fee


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_before_and_after():
    items = [("book", 12.00), ("pen", 3.50), ("notebook", 5.25)]
    tax_rate = 0.10

    print("=" * 60)
    print("DRY: BEFORE vs AFTER")
    print("=" * 60)

    before_total = total_price_before(items, tax_rate, shipping_fee=4.99)
    after_total = total_price_after(items, tax_rate, shipping_fee=4.99)

    before_refund = refund_amount_before(items, tax_rate, restocking_fee=2.00)
    after_refund = refund_amount_after(items, tax_rate, restocking_fee=2.00)

    print(f"Total (before): {before_total:.2f}")
    print(f"Total (after) : {after_total:.2f}")
    print(f"Refund (before): {before_refund:.2f}")
    print(f"Refund (after) : {after_refund:.2f}")

    print("\nNotice how the AFTER version centralizes shared logic")
    print("in calculate_subtotal() and apply_tax().")


if __name__ == "__main__":
    demo_before_and_after()
    print("\n✓ Examples complete!")
