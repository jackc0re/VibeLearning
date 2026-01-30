"""
Boolean Logic - Exercises
=========================
Practice working with logic gates and boolean algebra.
"""

print("=" * 60)
print("BOOLEAN LOGIC - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Logic Gate Functions
# =============================================================================
print("\n--- Exercise 1: Logic Gate Functions ---")
print("""
Implement these logic gates without using Python's and/or/not:
- my_and(a, b): Return True only if both are True
- my_or(a, b): Return True if either is True
- my_not(a): Return the opposite
- my_xor(a, b): Return True if inputs are different

Hint: You can use comparisons and arithmetic.
""")

def my_and(a, b):
    """Implement AND without using 'and' keyword."""
    # Your code here:
    pass

def my_or(a, b):
    """Implement OR without using 'or' keyword."""
    # Your code here:
    pass

def my_not(a):
    """Implement NOT without using 'not' keyword."""
    # Your code here:
    pass

def my_xor(a, b):
    """Implement XOR without using '!=' or 'xor'."""
    # Your code here:
    pass

# Test your functions
# print("Testing my_and:", my_and(True, True), my_and(True, False), my_and(False, False))
# print("Testing my_or:", my_or(True, False), my_or(False, False))
# print("Testing my_not:", my_not(True), my_not(False))
# print("Testing my_xor:", my_xor(True, True), my_xor(True, False))

# =============================================================================
# EXERCISE 2: Simplify Boolean Expressions
# =============================================================================
print("\n--- Exercise 2: Simplify Boolean Expressions ---")
print("""
Simplify these expressions using boolean algebra laws:

a) A AND (A OR B)
b) A OR (A AND B)
c) (A AND B) OR (A AND NOT B)
d) NOT (NOT A AND NOT B)
e) (A OR B) AND (A OR NOT B)

Hint: Use the distributive, identity, and complement laws.
""")

# Your answers:
# a) Simplifies to: ...
# b) Simplifies to: ...
# c) Simplifies to: ...
# d) Simplifies to: ...
# e) Simplifies to: ...

# =============================================================================
# EXERCISE 3: Truth Table Generator
# =============================================================================
print("\n--- Exercise 3: Truth Table Generator ---")
print("""
Write a function that generates a truth table for any given
boolean function with 2 inputs.
""")

def print_truth_table(function, name):
    """
    Print a truth table for a 2-input boolean function.

    Args:
        function: A callable that takes 2 boolean arguments
        name: String name of the function
    """
    # Your code here:
    pass

# Test with various functions
# def implication(a, b):
#     return (not a) or b
# print_truth_table(implication, "IMPLIES")

# =============================================================================
# EXERCISE 4: NAND is Universal
# =============================================================================
print("\n--- Exercise 4: NAND is Universal ---")
print("""
The NAND gate is called "universal" because you can build any
other logic gate using only NANDs.

Implement AND, OR, and NOT using only NAND operations.

Hint: First define nand(a, b), then use it to build others.
""")

def nand(a, b):
    """NAND gate - the universal gate."""
    return not (a and b)

def not_from_nand(a):
    """Implement NOT using only NAND."""
    # Your code here:
    pass

def and_from_nand(a, b):
    """Implement AND using only NAND."""
    # Your code here:
    pass

def or_from_nand(a, b):
    """Implement OR using only NAND."""
    # Hint: Use De Morgan's Law
    # Your code here:
    pass

# Test your implementations
# print("NOT from NAND:", not_from_nand(True), not_from_nand(False))
# print("AND from NAND:", and_from_nand(True, True), and_from_nand(True, False))
# print("OR from NAND:", or_from_nand(True, False), or_from_nand(False, False))

# =============================================================================
# EXERCISE 5: Complex Condition
# =============================================================================
print("\n--- Exercise 5: Complex Condition ---")
print("""
You need to write a function that determines if someone can rent a car.
Rules:
- Must be at least 21 years old
- Must have a valid driver's license
- If under 25, must have clean driving record (no accidents)
- OR if they pay extra insurance fee, age requirement drops to 18

Implement: can_rent_car(age, has_license, has_accidents, pays_extra)
""")

def can_rent_car(age, has_license, has_accidents, pays_extra):
    """
    Determine if person can rent a car.

    Args:
        age: Integer age
        has_license: Boolean
        has_accidents: Boolean
        pays_extra: Boolean

    Returns:
        Boolean indicating if they can rent
    """
    # Your code here:
    pass

# Test cases
# print(can_rent_car(25, True, False, False))   # Expected: True
# print(can_rent_car(20, True, False, False))   # Expected: False
# print(can_rent_car(20, True, False, True))    # Expected: True
# print(can_rent_car(24, True, True, False))    # Expected: False
# print(can_rent_car(24, True, True, True))     # Expected: True
# print(can_rent_car(30, False, False, False))  # Expected: False

# =============================================================================
# EXERCISE 6: Boolean Expression Evaluator
# =============================================================================
print("\n--- Exercise 6: Boolean Expression Evaluator ---")
print("""
Write a function that evaluates a boolean expression given as a string.
For simplicity, handle only variables A, B, C and operators AND, OR, NOT.

Example: "A AND (B OR NOT C)" with A=True, B=False, C=True
""")

def evaluate_expression(expression, values):
    """
    Evaluate a simple boolean expression.

    Args:
        expression: String like "A AND B"
        values: Dict like {"A": True, "B": False}

    Returns:
        Boolean result
    """
    # Your code here (simplified version):
    pass

# Test
# result = evaluate_expression("A AND B", {"A": True, "B": False})
# print(f"True AND False = {result}")  # Expected: False

# =============================================================================
# EXERCISE 7: Majority Vote
# =============================================================================
print("\n--- Exercise 7: Majority Vote ---")
print("""
Implement a majority vote function that returns True if at least
2 out of 3 inputs are True.

Do this in two ways:
1. Using boolean algebra
2. By counting Trues
""")

def majority_vote_algebra(a, b, c):
    """Implement majority using boolean algebra (no counting)."""
    # Your code here:
    pass

def majority_vote_count(a, b, c):
    """Implement majority by counting."""
    # Your code here:
    pass

# Test both implementations
# inputs = [(False, False, False), (False, False, True), (False, True, True), (True, True, True)]
# for a, b, c in inputs:
#     alg = majority_vote_algebra(a, b, c)
#     cnt = majority_vote_count(a, b, c)
#     print(f"{a}, {b}, {c} → Algebra: {alg}, Count: {cnt}")

# =============================================================================
# EXERCISE 8: DNF and CNF
# =============================================================================
print("\n--- Exercise 8: DNF and CNF ---")
print("""
Given this truth table for function F(A, B, C):

  A B C | F
  ------|---
  0 0 0 | 0
  0 0 1 | 1
  0 1 0 | 0
  0 1 1 | 0
  1 0 0 | 1
  1 0 1 | 1
  1 1 0 | 0
  1 1 1 | 1

a) Write the Disjunctive Normal Form (DNF/SOP)
   - OR together the rows where F=1

b) Write the Conjunctive Normal Form (CNF/POS)
   - AND together the rows where F=0 (inverted)
""")

# Your answers:
# DNF: F = ...
# CNF: F = ...

def f_from_dnf(a, b, c):
    """Implement F using your DNF expression."""
    # Your code here:
    pass

def f_from_cnf(a, b, c):
    """Implement F using your CNF expression."""
    # Your code here:
    pass

# Verify both match the truth table

print("\n" + "=" * 60)
print("Exercises complete! Check your answers below.")
print("=" * 60)

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("\n--- Exercise 1: Logic Gate Functions (Solution) ---")
solution_1 = '''
def my_and(a, b):
    # If both are 1 (True), product is 1
    return bool(a * b)

def my_or(a, b):
    # Sum is > 0 if either is 1
    return bool(a + b)

def my_not(a):
    # 1 - 1 = 0, 1 - 0 = 1
    # Alternative: return a == False
    return 1 - bool(a)

def my_xor(a, b):
    # XOR is true when sum is exactly 1
    return bool(a + b) and not (a and b)
    # Alternative: return bool((a + b) % 2)
'''
print(solution_1)

print("\n--- Exercise 2: Simplify Boolean Expressions (Solution) ---")
print("""
a) A AND (A OR B) = A  (Absorption Law)
b) A OR (A AND B) = A  (Absorption Law)
c) (A AND B) OR (A AND NOT B) = A AND (B OR NOT B) = A AND 1 = A
d) NOT (NOT A AND NOT B) = A OR B  (De Morgan's Law)
e) (A OR B) AND (A OR NOT B) = A OR (B AND NOT B) = A OR 0 = A
""")

print("\n--- Exercise 3: Truth Table Generator (Solution) ---")
solution_3 = '''
def print_truth_table(function, name):
    print(f"\\n{name} Truth Table:")
    print("  A | B | Output")
    print("  --|---|-------")
    for a in [False, True]:
        for b in [False, True]:
            result = function(a, b)
            print(f"  {int(a)} | {int(b)} |   {int(result)}")
'''
print(solution_3)

print("\n--- Exercise 4: NAND is Universal (Solution) ---")
solution_4 = '''
def nand(a, b):
    return not (a and b)

def not_from_nand(a):
    # A NAND A = NOT (A AND A) = NOT A
    return nand(a, a)

def and_from_nand(a, b):
    # NOT (A NAND B) = NOT (NOT (A AND B)) = A AND B
    return not_from_nand(nand(a, b))

def or_from_nand(a, b):
    # Using De Morgan's: A OR B = NOT (NOT A AND NOT B)
    #                   = NOT A NAND NOT B
    return nand(not_from_nand(a), not_from_nand(b))
'''
print(solution_4)

print("\n--- Exercise 5: Complex Condition (Solution) ---")
solution_5 = '''
def can_rent_car(age, has_license, has_accidents, pays_extra):
    # Basic requirements
    old_enough = (age >= 21) or (pays_extra and age >= 18)
    clean_record = not has_accidents or age >= 25

    return has_license and old_enough and clean_record

# Alternative one-liner:
def can_rent_car_v2(age, has_license, has_accidents, pays_extra):
    return (has_license and
            ((age >= 21) or (pays_extra and age >= 18)) and
            (not has_accidents or age >= 25))
'''
print(solution_5)

print("\n--- Exercise 6: Boolean Expression Evaluator (Solution) ---")
solution_6 = '''
def evaluate_expression(expression, values):
    # Simple approach: replace and evaluate
    expr = expression.upper()

    # Replace variables with their values
    for var, val in values.items():
        expr = expr.replace(var, str(val))

    # Replace operators with Python equivalents
    expr = expr.replace("AND", "and")
    expr = expr.replace("OR", "or")
    expr = expr.replace("NOT", "not")

    # Evaluate safely
    return eval(expr, {"__builtins__": {}}, {})
'''
print(solution_6)

print("\n--- Exercise 7: Majority Vote (Solution) ---")
solution_7 = '''
def majority_vote_algebra(a, b, c):
    # True if at least 2 are True
    # Pairs: (a,b), (a,c), (b,c)
    return (a and b) or (a and c) or (b and c)

def majority_vote_count(a, b, c):
    return sum([a, b, c]) >= 2
'''
print(solution_7)

print("\n--- Exercise 8: DNF and CNF (Solution) ---")
print("""
DNF (rows where F=1):
  Row 001: NOT A AND NOT B AND C
  Row 100: A AND NOT B AND NOT C
  Row 101: A AND NOT B AND C
  Row 111: A AND B AND C

F = (NOT A AND NOT B AND C) OR
    (A AND NOT B AND NOT C) OR
    (A AND NOT B AND C) OR
    (A AND B AND C)

CNF (rows where F=0, inverted):
  Row 000: A OR B OR C
  Row 010: A OR NOT B OR C
  Row 011: A OR NOT B OR NOT C
  Row 110: NOT A OR NOT B OR C

F = (A OR B OR C) AND
    (A OR NOT B OR C) AND
    (A OR NOT B OR NOT C) AND
    (NOT A OR NOT B OR C)
""")

print("\n" + "=" * 60)
print("All solutions provided. Keep practicing!")
print("=" * 60)
