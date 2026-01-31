"""
Code Smells - Examples

Shows a few common smells and simple refactoring directions.
Run with:
    python examples.py
"""

# =============================================================================
# SMELL 1: LONG FUNCTION (FOR DEMO)
# =============================================================================


def checkout_long_function(items, tax_rate, coupon=None):
    # Parses items, validates, computes totals, applies coupon, formats output...
    # This is intentionally doing too much.
    if not items:
        return "No items"

    subtotal = 0.0
    for name, price in items:
        if price < 0:
            return "Invalid price"
        subtotal += price

    total = subtotal * (1 + tax_rate)

    if coupon == "SAVE10":
        total *= 0.9

    return f"Total: ${total:.2f}"


# =============================================================================
# A CLEANER DIRECTION: EXTRACT RESPONSIBILITIES
# =============================================================================


def validate_items(items):
    if not items:
        return False
    return all(price >= 0 for _, price in items)


def subtotal(items):
    return sum(price for _, price in items)


def apply_coupon(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.9
    return amount


def checkout_refactored(items, tax_rate, coupon=None):
    if not validate_items(items):
        return "Invalid items"

    total = subtotal(items) * (1 + tax_rate)
    total = apply_coupon(total, coupon)
    return f"Total: ${total:.2f}"


# =============================================================================
# DEMONSTRATIONS
# =============================================================================


def demo_code_smells():
    print("=" * 60)
    print("Code Smells")
    print("=" * 60)

    items = [("book", 10.0), ("pen", 2.0)]
    print("Long function output:")
    print(" ", checkout_long_function(items, 0.10, coupon="SAVE10"))

    print("\nRefactored output:")
    print(" ", checkout_refactored(items, 0.10, coupon="SAVE10"))

    print("\nSmell takeaway: long functions often hide mixed concerns.")


if __name__ == "__main__":
    demo_code_smells()
    print("\n✓ Examples complete!")
