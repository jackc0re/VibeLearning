# 🔀 Control Flow

Control flow determines which code runs based on conditions. It's how your program makes decisions.

---

## What is Control Flow?

Without control flow, code runs line by line, top to bottom:

```python
print("Line 1")
print("Line 2")
print("Line 3")
# Always prints all three lines
```

With control flow, you can make decisions:

```python
if weather == "sunny":
    print("Go outside!")
else:
    print("Stay inside.")
# Only one message prints, depending on the condition
```

---

## The `if` Statement

The most basic form of control flow.

```python
age = 20

if age >= 18:
    print("You are an adult")
```

### Key Points:
- The condition must evaluate to `True` or `False`
- The colon (`:`) is required after the condition
- The code block must be **indented** (usually 4 spaces)

---

## `if-else` Statement

Do one thing or another.

```python
temperature = 35

if temperature > 30:
    print("It's hot!")
else:
    print("It's not too hot.")
```

### The Flow:
```
       ┌─────────────────┐
       │  temperature>30 │
       └───────┬─────────┘
              / \
         True/   \False
            /     \
   ┌───────▼─┐   ┌─▼───────┐
   │ "It's   │   │ "It's   │
   │  hot!"  │   │ not..." │
   └─────────┘   └─────────┘
```

---

## `if-elif-else` Statement

Multiple conditions, check one after another.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")  # B
```

### Key Points:
- `elif` is short for "else if"
- Only the **first** matching condition runs
- `else` catches everything that didn't match
- `else` is optional

### Common Mistake:

```python
score = 95

# ❌ Wrong: All conditions checked independently
if score >= 60:
    print("D")  # This runs!
if score >= 70:
    print("C")  # This also runs!
if score >= 80:
    print("B")  # This also runs!
if score >= 90:
    print("A")  # This also runs!

# ✅ Correct: Use elif for mutually exclusive conditions
if score >= 90:
    print("A")  # Only this runs
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
```

---

## Nested Conditions

Conditions inside conditions.

```python
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Welcome to the movie!")
    else:
        print("You need a guardian for this movie.")
else:
    print("Please buy a ticket first.")
```

### When to Nest:
- When one condition depends on another
- Keep nesting shallow (2-3 levels max)
- Consider using `and` / `or` to flatten

### Flattened Version:
```python
if not has_ticket:
    print("Please buy a ticket first.")
elif age < 18:
    print("You need a guardian for this movie.")
else:
    print("Welcome to the movie!")
```

---

## Conditional Expressions (Ternary Operator)

A one-liner for simple if-else.

```python
# Traditional if-else
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Conditional expression (same result)
status = "adult" if age >= 18 else "minor"
```

### Syntax:
```python
value_if_true if condition else value_if_false
```

### Best Used For:
```python
# Simple assignments
max_value = a if a > b else b

# Default values
name = username if username else "Anonymous"

# Quick formatting
print(f"You have {count} item{'s' if count != 1 else ''}")
```

### When NOT to Use:
```python
# ❌ Too complex, hard to read
result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"

# ✅ Better as regular if-elif-else
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
# ...
```

---

## Truthy and Falsy Values

In conditions, some values act as `True` or `False`:

### Falsy Values (evaluate to False):
```python
bool(False)    # False
bool(None)     # False
bool(0)        # False
bool(0.0)      # False
bool("")       # False (empty string)
bool([])       # False (empty list)
bool({})       # False (empty dict)
```

### Truthy Values (evaluate to True):
```python
bool(True)     # True
bool(1)        # True (any non-zero number)
bool(-1)       # True
bool("hello")  # True (non-empty string)
bool([1, 2])   # True (non-empty list)
bool({"a": 1}) # True (non-empty dict)
```

### Practical Use:
```python
# Check if a list has items
items = []
if items:
    print(f"You have {len(items)} items")
else:
    print("Your list is empty")

# Check if a string has content
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Hello, stranger")
```

---

## Common Patterns

### Guard Clauses
Check for invalid cases first, return early:

```python
def process_order(order):
    if order is None:
        return "No order provided"
    
    if len(order.items) == 0:
        return "Order is empty"
    
    if not order.is_paid:
        return "Order not paid"
    
    # Main logic here (only reached if all checks pass)
    return "Processing order..."
```

### Default Values with `or`
```python
# If username is empty/None, use "Guest"
display_name = username or "Guest"
```

### Safe Access with `and`
```python
# Only access .name if user exists
name = user and user.name
```

---

## Quick Reference

```python
# Basic if
if condition:
    # code

# If-else
if condition:
    # code if true
else:
    # code if false

# If-elif-else
if condition1:
    # code
elif condition2:
    # code
else:
    # code

# Conditional expression
value = true_val if condition else false_val

# Truthy/Falsy shorthand
if my_list:  # same as: if len(my_list) > 0
    pass

if name:  # same as: if name != ""
    pass
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
