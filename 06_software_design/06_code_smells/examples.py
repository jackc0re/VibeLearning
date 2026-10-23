"""
Code Smells - Examples

Shows common smells (long function, magic numbers, duplicated code,
feature envy) and simple refactoring directions.
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
# SMELL 2: MAGIC NUMBERS
# =============================================================================


def shipping_cost_smelly(weight):
    # 0.5 and 5? The reader has to guess.
    return weight * 0.5 + 5


RATE_PER_KG = 0.5
BASE_FEE = 5


def shipping_cost_clean(weight):
    return weight * RATE_PER_KG + BASE_FEE


# =============================================================================
# SMELL 3: DUPLICATED CODE
# =============================================================================


def email_total(items):
    total = 0
    for _, price in items:
        total += price * 1.1  # tax logic, copy #1
    return round(total, 2)


def report_total(items):
    total = 0
    for _, price in items:
        total += price * 1.1  # same tax logic, copy #2
    return round(total, 2)


def taxed_total(items, tax_rate):
    """One shared implementation both callers should use."""
    return round(sum(price for _, price in items) * (1 + tax_rate), 2)


# =============================================================================
# SMELL 4: FEATURE ENVY
# =============================================================================


class User:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display_name(self):
        # The logic lives next to the data it uses.
        return f"{self.name.upper()} from {self.city}"


class ReportEnvious:
    def __init__(self, user):
        self.user = user

    def summary(self):
        # Reaches into user's data again and again.
        return f"{self.user.name.upper()} from {self.user.city}"


class ReportClean:
    def __init__(self, user):
        self.user = user

    def summary(self):
        return self.user.display_name()


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


def demo_more_smells():
    print("\nMore smells, before and after")

    # Magic numbers
    weight = 4
    smelly = shipping_cost_smelly(weight)
    clean = shipping_cost_clean(weight)
    print(f"  shipping {smelly} (smelly) vs {clean} (named constants) -> "
          f"{'MATCH' if smelly == clean else 'MISMATCH'}")

    # Duplicated code
    items = [("book", 10.0), ("pen", 2.0)]
    duplicated = email_total(items)
    shared = taxed_total(items, 0.10)
    print(f"  totals: {duplicated} (copy-pasted tax) vs {shared} (shared fn) -> "
          f"{'MATCH' if duplicated == shared else 'MISMATCH'}")

    # Feature envy
    user = User("alice", "Paris")
    envy = ReportEnvious(user).summary()
    tidy = ReportClean(user).summary()
    print(f"  summary: {envy} (envy) vs {tidy} (moved to User) -> "
          f"{'MATCH' if envy == tidy else 'MISMATCH'}")


if __name__ == "__main__":
    demo_code_smells()
    demo_more_smells()
    print("\nPASS Examples complete!")
