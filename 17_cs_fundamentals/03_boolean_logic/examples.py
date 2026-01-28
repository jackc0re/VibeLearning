"""
Boolean Logic - Examples
========================
Exploring logic gates, truth tables, and boolean algebra.
"""

print("=" * 60)
print("BOOLEAN LOGIC - Examples")
print("=" * 60)

# =============================================================================
# BASIC LOGIC GATES AS FUNCTIONS
# =============================================================================
print("\n--- Logic Gates as Python Functions ---\n")

def AND(a, b):
    """Logical AND gate."""
    return a and b

def OR(a, b):
    """Logical OR gate."""
    return a or b

def NOT(a):
    """Logical NOT gate."""
    return not a

def NAND(a, b):
    """Logical NAND gate (NOT AND)."""
    return not (a and b)

def NOR(a, b):
    """Logical NOR gate (NOT OR)."""
    return not (a or b)

def XOR(a, b):
    """Logical XOR gate (exclusive OR)."""
    return a != b

def XNOR(a, b):
    """Logical XNOR gate (exclusive NOR)."""
    return a == b

# =============================================================================
# TRUTH TABLES
# =============================================================================
print("=" * 60)
print("TRUTH TABLES")
print("=" * 60)

def print_truth_table(gate_name, gate_func, inputs):
    """Print a truth table for a logic gate."""
    print(f"\n{gate_name} Gate:")
    print("  A | B | Output")
    print("  --|---|-------")
    for a, b in inputs:
        result = gate_func(a, b)
        # Convert to 0/1 for display
        a_disp = int(a)
        b_disp = int(b)
        r_disp = int(result)
        print(f"  {a_disp} | {b_disp} |   {r_disp}")

# All possible inputs for 2-input gates
inputs = [(False, False), (False, True), (True, False), (True, True)]

print_truth_table("AND", AND, inputs)
print_truth_table("OR", OR, inputs)
print_truth_table("XOR", XOR, inputs)
print_truth_table("NAND", NAND, inputs)
print_truth_table("NOR", NOR, inputs)
print_truth_table("XNOR", XNOR, inputs)

# Single-input gate (NOT)
print("\nNOT Gate:")
print("  A | Output")
print("  --|-------")
for a in [False, True]:
    result = NOT(a)
    print(f"  {int(a)} |   {int(result)}")

# =============================================================================
# BOOLEAN LAWS
# =============================================================================
print("\n" + "=" * 60)
print("BOOLEAN ALGEBRA LAWS")
print("=" * 60)

print("\n--- Identity Laws ---")
A = True
print(f"A AND True = A:    {A and True} = {A}")
A = False
print(f"A OR False = A:    {A or False} = {A}")

print("\n--- Null Laws ---")
A = True
print(f"A AND False = 0:   {A and False}")
print(f"A OR True = 1:     {A or True}")

print("\n--- Idempotent Laws ---")
A = True
print(f"A AND A = A:       {A and A} = {A}")
print(f"A OR A = A:        {A or A} = {A}")

print("\n--- Complement Laws ---")
A = True
print(f"A AND NOT A = 0:   {A and (not A)}")
print(f"A OR NOT A = 1:    {A or (not A)}")

print("\n--- Double Negation ---")
A = True
print(f"NOT (NOT A) = A:   {not (not A)} = {A}")

print("\n--- Commutative Laws ---")
A, B = True, False
print(f"A AND B = B AND A: {A and B} = {B and A}")
print(f"A OR B = B OR A:   {A or B} = {B or A}")

print("\n--- Distributive Laws ---")
A, B, C = True, False, True
left = A and (B or C)
right = (A and B) or (A and C)
print(f"A AND (B OR C) = (A AND B) OR (A AND C)")
print(f"  {left} = {right} ✓")

left = A or (B and C)
right = (A or B) and (A or C)
print(f"A OR (B AND C) = (A OR B) AND (A OR C)")
print(f"  {left} = {right} ✓")

# =============================================================================
# DE MORGAN'S LAWS
# =============================================================================
print("\n" + "=" * 60)
print("DE MORGAN'S LAWS")
print("=" * 60)

print("\nLaw 1: NOT (A AND B) = (NOT A) OR (NOT B)")
print("\nVerification:")
print("  A | B | NOT(A&B) | !A OR !B | Match")
print("  --|---|----------|----------|------")
for A in [False, True]:
    for B in [False, True]:
        left = not (A and B)
        right = (not A) or (not B)
        match = "✓" if left == right else "✗"
        print(f"  {int(A)} | {int(B)} |     {int(left)}    |    {int(right)}     |  {match}")

print("\nLaw 2: NOT (A OR B) = (NOT A) AND (NOT B)")
print("\nVerification:")
print("  A | B | NOT(A|B) | !A AND !B | Match")
print("  --|---|----------|-----------|------")
for A in [False, True]:
    for B in [False, True]:
        left = not (A or B)
        right = (not A) and (not B)
        match = "✓" if left == right else "✗"
        print(f"  {int(A)} | {int(B)} |     {int(left)}    |     {int(right)}     |  {match}")

# Real-world examples
print("\n--- De Morgan's in Plain English ---")
print("NOT (sunny AND warm) = NOT sunny OR NOT warm")
print("  Meaning: 'It's not sunny and warm' = 'It's not sunny OR it's not warm'")

print("\nNOT (rainy OR cold) = NOT rainy AND NOT cold")
print("  Meaning: 'It's not rainy or cold' = 'It's not rainy AND not cold'")

# =============================================================================
# PRACTICAL: PERMISSION SYSTEM
# =============================================================================
print("\n" + "=" * 60)
print("PRACTICAL: SIMPLE SECURITY SYSTEM")
print("=" * 60)

def can_enter(has_keycard, knows_pin, is_admin):
    """
    Determine if someone can enter the building.
    Rules:
    - Admin can always enter
    - OR (keycard AND pin)
    """
    regular_access = has_keycard and knows_pin
    return regular_access or is_admin

print("\nSecurity System Rules:")
print("- Regular employees: need keycard AND pin")
print("- Admins: always allowed")

print("\nTest Cases:")
test_cases = [
    (True, True, False, "Regular employee with both"),
    (True, False, False, "Has keycard, forgot PIN"),
    (False, True, False, "Knows PIN, no keycard"),
    (False, False, True, "Admin without credentials"),
    (False, False, False, "Unauthorized person"),
]

for has_key, knows_pin, admin, description in test_cases:
    allowed = can_enter(has_key, knows_pin, admin)
    status = "✓ ALLOWED" if allowed else "✗ DENIED"
    print(f"  {description:35s} → {status}")

# =============================================================================
# PRACTICAL: VOTING SYSTEM
# =============================================================================
print("\n" + "=" * 60)
print("PRACTICAL: VOTING SYSTEM")
print("=" * 60)

def motion_passes(votes_for, votes_against, total_voters):
    """
    Determine if a motion passes.
    Rules:
    - Simple majority required (> 50%)
    - At least 3 votes total
    """
    total_votes = votes_for + votes_against
    has_quorum = total_votes >= 3
    majority = votes_for > votes_against
    return has_quorum and majority

print("\nVoting Rules:")
print("- Simple majority (> 50%)")
print("- Minimum 3 votes required")

print("\nTest Cases:")
vote_cases = [
    (5, 2, "Clear majority"),
    (2, 1, "Bare majority, minimum votes"),
    (2, 0, "Not enough total votes"),
    (3, 3, "Tie - no majority"),
    (1, 4, "Defeated motion"),
]

for for_votes, against_votes, description in vote_cases:
    passes = motion_passes(for_votes, against_votes, for_votes + against_votes)
    status = "✓ PASSES" if passes else "✗ FAILS"
    print(f"  {for_votes}-{against_votes}: {description:30s} → {status}")

# =============================================================================
# PRACTICAL: DISCOUNT ELIGIBILITY
# =============================================================================
print("\n" + "=" * 60)
print("PRACTICAL: DISCOUNT ELIGIBILITY")
print("=" * 60)

def qualifies_for_discount(is_student, is_senior, is_member, purchase_amount):
    """
    Check if customer qualifies for discount.
    Rules:
    - Students get 10% off
    - Seniors (65+) get 15% off
    - Members get 5% off
    - Discounts don't stack - best one applies
    - Minimum purchase: $20
    """
    meets_minimum = purchase_amount >= 20
    has_discount_status = is_student or is_senior or is_member
    return meets_minimum and has_discount_status

def calculate_discount(is_student, is_senior, is_member):
    """Calculate the discount percentage."""
    if is_senior:
        return 0.15
    elif is_student:
        return 0.10
    elif is_member:
        return 0.05
    return 0.0

print("\nDiscount Rules:")
print("- Minimum purchase: $20")
print("- Senior (65+): 15%")
print("- Student: 10%")
print("- Member: 5%")

print("\nTest Cases:")
discount_cases = [
    (True, False, False, 25.00, "Student, $25 purchase"),
    (False, True, False, 50.00, "Senior, $50 purchase"),
    (False, False, True, 15.00, "Member, $15 purchase (below min)"),
    (True, True, False, 100.00, "Student AND Senior (gets senior)"),
    (False, False, False, 100.00, "No discount status"),
]

for student, senior, member, amount, description in discount_cases:
    qualifies = qualifies_for_discount(student, senior, member, amount)
    if qualifies:
        discount = calculate_discount(student, senior, member)
        final = amount * (1 - discount)
        print(f"  {description:40s} → {discount*100:.0f}% off, ${final:.2f}")
    else:
        print(f"  {description:40s} → No discount")

# =============================================================================
# TRUTHINESS IN PYTHON
# =============================================================================
print("\n" + "=" * 60)
print("TRUTHINESS IN PYTHON")
print("=" * 60)

print("\nValues considered False (falsy):")
falsy_values = [False, 0, 0.0, "", [], {}, None]
for val in falsy_values:
    print(f"  {repr(val):15s} → bool({val}) = {bool(val)}")

print("\nValues considered True (truthy):")
truthy_values = [True, 1, 3.14, "hello", [1, 2], {"a": 1}, [0]]
for val in truthy_values:
    print(f"  {repr(val):15s} → bool({val}) = {bool(val)}")

print("\n--- Practical Truthiness ---")

def greet_user(name):
    """Greet a user if they provided a name."""
    if name:
        return f"Hello, {name}!"
    return "Hello, mysterious stranger!"

print(greet_user("Alice"))
print(greet_user(""))

def process_items(items):
    """Process a list if it has items."""
    if items:
        return f"Processing {len(items)} items"
    return "No items to process"

print(process_items([1, 2, 3]))
print(process_items([]))

# =============================================================================
# SHORT-CIRCUIT EVALUATION
# =============================================================================
print("\n" + "=" * 60)
print("SHORT-CIRCUIT EVALUATION")
print("=" * 60)

def expensive_operation():
    """Simulates an expensive function."""
    print("    (expensive_operation was called!)")
    return True

print("\nAND Short-Circuit:")
print("  False AND expensive_operation():")
result = False and expensive_operation()
print(f"    Result: {result}")
print("  (expensive_operation was NOT called!)")

print("\n  True AND expensive_operation():")
result = True and expensive_operation()
print(f"    Result: {result}")

print("\nOR Short-Circuit:")
print("  True OR expensive_operation():")
result = True or expensive_operation()
print(f"    Result: {result}")
print("  (expensive_operation was NOT called!)")

print("\n  False OR expensive_operation():")
result = False or expensive_operation()
print(f"    Result: {result}")

# =============================================================================
# HALF ADDER
# =============================================================================
print("\n" + "=" * 60)
print("BUILDING A HALF ADDER")
print("=" * 60)

def half_adder(a, b):
    """
    A half adder adds two single bits.
    Returns (sum, carry)
    """
    sum_bit = XOR(a, b)      # a XOR b
    carry_bit = AND(a, b)    # a AND b
    return sum_bit, carry_bit

print("\nHalf Adder (adds two bits):")
print("  A | B | Sum | Carry")
print("  --|---|-----|------")
for a in [0, 1]:
    for b in [0, 1]:
        sum_bit, carry = half_adder(bool(a), bool(b))
        print(f"  {a} | {b} |  {int(sum_bit)}  |   {int(carry)}")

print("\n--- Adding Binary Numbers ---")
print("  0 + 0 = 00 (0)")
print("  0 + 1 = 01 (1)")
print("  1 + 0 = 01 (1)")
print("  1 + 1 = 10 (2)")

print("\n" + "=" * 60)
print("Examples complete! Try the exercises next.")
print("=" * 60)
