"""
Input and Output - Exercises
============================
Practice communicating with users!
"""

print("=" * 50)
print("INPUT AND OUTPUT - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: Formatted Greeting
# =============================================================================
print("\n--- Exercise 1: Formatted Greeting ---\n")
"""
Given a name and age, create a nicely formatted greeting.
Include:
- A personalized welcome message
- Their age next year
- A fun fact: days they've been alive (age * 365)

Use f-strings for formatting.
"""

name = "Alex"
age = 25

# Your code here:


# =============================================================================
# EXERCISE 2: Receipt Formatter
# =============================================================================
print("\n--- Exercise 2: Receipt Formatter ---\n")
"""
Create a receipt display for a shopping cart.
Items: [("Apple", 3, 1.50), ("Banana", 5, 0.75), ("Orange", 2, 2.00)]
Each item is (name, quantity, price_each)

Display:
- Each item with subtotal
- Total with tax (8%)
- Format prices with 2 decimal places
"""

items = [
    ("Apple", 3, 1.50),
    ("Banana", 5, 0.75),
    ("Orange", 2, 2.00),
]
tax_rate = 0.08

# Your code here:


# =============================================================================
# EXERCISE 3: Progress Bar
# =============================================================================
print("\n--- Exercise 3: Progress Bar ---\n")
"""
Create a function that displays a text progress bar.
For 50% progress: [=====     ] 50%

The bar should be 10 characters wide.
"""

def show_progress(percent):
    """Display a progress bar for the given percentage (0-100)."""
    # Your code here:
    pass

# Test it:
# show_progress(0)
# show_progress(30)
# show_progress(50)
# show_progress(75)
# show_progress(100)


# =============================================================================
# EXERCISE 4: Multiplication Table
# =============================================================================
print("\n--- Exercise 4: Multiplication Table ---\n")
"""
Print a nicely formatted multiplication table (1-5).
Each number should be right-aligned with width 4.
Include a header row and column.
"""

# Your code here:


# =============================================================================
# EXERCISE 5: Student Report Card
# =============================================================================
print("\n--- Exercise 5: Report Card ---\n")
"""
Create a formatted report card given:
- Student name
- Dictionary of subjects and scores

Display each subject, score, and grade (A/B/C/D/F).
Include average at the bottom.
"""

student = "Emily Chen"
scores = {
    "Math": 92,
    "Science": 88,
    "English": 95,
    "History": 79,
    "Art": 85
}

# Your code here:


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")
name = "Alex"
age = 25

print(f"╔{'═' * 40}╗")
print(f"║{'Welcome, ' + name + '!':^40}║")
print(f"╠{'═' * 40}╣")
print(f"║ You are currently {age} years old.{' ' * 9}║")
print(f"║ Next year, you'll be {age + 1}!{' ' * 13}║")
print(f"║ You've been alive ~{age * 365:,} days!{' ' * 6}║")
print(f"╚{'═' * 40}╝")

# SOLUTION 2
print("\n--- Solution 2 ---")
items = [
    ("Apple", 3, 1.50),
    ("Banana", 5, 0.75),
    ("Orange", 2, 2.00),
]
tax_rate = 0.08

print("=" * 35)
print(f"{'STORE RECEIPT':^35}")
print("=" * 35)
print(f"{'Item':<12} {'Qty':>4} {'Price':>7} {'Total':>8}")
print("-" * 35)

subtotal = 0
for name, qty, price in items:
    item_total = qty * price
    subtotal += item_total
    print(f"{name:<12} {qty:>4} ${price:>5.2f} ${item_total:>6.2f}")

tax = subtotal * tax_rate
total = subtotal + tax

print("-" * 35)
print(f"{'Subtotal:':<20} ${subtotal:>10.2f}")
print(f"{'Tax (8%):':<20} ${tax:>10.2f}")
print("=" * 35)
print(f"{'TOTAL:':<20} ${total:>10.2f}")
print("=" * 35)

# SOLUTION 3
print("\n--- Solution 3 ---")

def show_progress(percent):
    """Display a progress bar for the given percentage (0-100)."""
    filled = int(percent / 10)
    empty = 10 - filled
    bar = "=" * filled + " " * empty
    print(f"[{bar}] {percent:3}%")

show_progress(0)
show_progress(30)
show_progress(50)
show_progress(75)
show_progress(100)

# SOLUTION 4
print("\n--- Solution 4 ---")

# Header
print("    ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print()
print("    " + "----" * 5)

# Body
for i in range(1, 6):
    print(f"{i:3} |", end="")
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# SOLUTION 5
print("\n--- Solution 5 ---")

def get_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

student = "Emily Chen"
scores = {
    "Math": 92,
    "Science": 88,
    "English": 95,
    "History": 79,
    "Art": 85
}

print("╔" + "═" * 36 + "╗")
print(f"║{'REPORT CARD':^36}║")
print(f"║{'Student: ' + student:^36}║")
print("╠" + "═" * 36 + "╣")
print(f"║ {'Subject':<12} {'Score':>8} {'Grade':>8}  ║")
print("║" + "-" * 34 + "  ║")

for subject, score in scores.items():
    grade = get_grade(score)
    print(f"║ {subject:<12} {score:>8} {grade:>8}  ║")

avg = sum(scores.values()) / len(scores)
print("║" + "-" * 34 + "  ║")
print(f"║ {'Average':<12} {avg:>8.1f} {get_grade(avg):>8}  ║")
print("╚" + "═" * 36 + "╝")

print("\n" + "=" * 50)
print("🎉 Congratulations! Module 01 Complete!")
print("Move on to 02_data_structures to continue.")
print("=" * 50)
