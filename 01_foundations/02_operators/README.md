# ➕ Operators

Operators are symbols that perform operations on values. Think of them as verbs in the language of programming.

---

## Categories of Operators

| Category | Purpose | Examples |
|----------|---------|----------|
| **Arithmetic** | Math operations | `+`, `-`, `*`, `/` |
| **Comparison** | Compare values | `==`, `!=`, `<`, `>` |
| **Logical** | Combine booleans | `and`, `or`, `not` |
| **Assignment** | Assign values | `=`, `+=`, `-=` |
| **Membership** | Check containment | `in`, `not in` |
| **Identity** | Check if same object | `is`, `is not` |

---

## Arithmetic Operators

Perform mathematical calculations.

```python
a = 10
b = 3

# Basic operations
print(a + b)   # 13  (Addition)
print(a - b)   # 7   (Subtraction)
print(a * b)   # 30  (Multiplication)
print(a / b)   # 3.333... (Division - always float)
print(a // b)  # 3   (Floor/Integer division)
print(a % b)   # 1   (Modulo - remainder)
print(a ** b)  # 1000 (Exponentiation - power)
```

### Division Types

```python
# Regular division (/) - always returns float
10 / 3   # 3.333...
10 / 2   # 5.0 (still a float!)

# Floor division (//) - rounds down to integer
10 // 3  # 3
-10 // 3 # -4 (rounds toward negative infinity)

# Modulo (%) - remainder after division
10 % 3   # 1 (10 = 3*3 + 1)
15 % 5   # 0 (15 = 5*3 + 0, evenly divisible)
```

### Order of Operations (PEMDAS)

```python
# Python follows mathematical order of operations
result = 2 + 3 * 4      # 14 (not 20!)
result = (2 + 3) * 4    # 20 (parentheses first)
result = 2 ** 3 ** 2    # 512 (exponents: right to left)
result = 10 - 5 - 2     # 3 (same precedence: left to right)
```

---

## Comparison Operators

Compare values and return `True` or `False`.

```python
x = 5
y = 10

# Equality
x == y   # False (equal to)
x != y   # True  (not equal to)

# Ordering
x < y    # True  (less than)
x > y    # False (greater than)
x <= y   # True  (less than or equal)
x >= y   # False (greater than or equal)
```

### String Comparison

Strings are compared lexicographically (dictionary order):

```python
"apple" < "banana"   # True (a comes before b)
"Apple" < "apple"    # True (uppercase before lowercase)
"10" < "9"           # True (string comparison, not numeric!)
```

### Chained Comparisons

Python allows elegant chained comparisons:

```python
x = 5
1 < x < 10     # True  (x is between 1 and 10)
1 < x < 3      # False (x is not between 1 and 3)
1 <= x <= 10   # True  (inclusive range)
```

---

## Logical Operators

Combine boolean expressions.

```python
a = True
b = False

a and b    # False (both must be True)
a or b     # True  (at least one must be True)
not a      # False (inverts the value)
```

### Truth Tables

```
AND: Returns True only if BOTH are True
True  and True   → True
True  and False  → False
False and True   → False
False and False  → False

OR: Returns True if AT LEAST ONE is True
True  or True    → True
True  or False   → True
False or True    → True
False or False   → False

NOT: Inverts the value
not True  → False
not False → True
```

### Short-Circuit Evaluation

Python stops evaluating as soon as the result is determined:

```python
# With 'and': stops at first False
False and expensive_function()  # expensive_function() never runs

# With 'or': stops at first True
True or expensive_function()    # expensive_function() never runs
```

### Practical Examples

```python
age = 25
has_license = True
has_car = False

# Can drive alone?
can_drive = age >= 16 and has_license  # True

# Has transportation?
has_transport = has_car or has_bicycle  # Depends on has_bicycle

# Is teenager?
is_teen = age >= 13 and age <= 19  # False (25 is not 13-19)
is_teen = 13 <= age <= 19          # Same thing, cleaner syntax
```

---

## Assignment Operators

Regular and compound assignment.

```python
# Simple assignment
x = 10

# Compound assignment (shorthand for x = x + 5)
x += 5   # x = x + 5  → x is now 15
x -= 3   # x = x - 3  → x is now 12
x *= 2   # x = x * 2  → x is now 24
x /= 4   # x = x / 4  → x is now 6.0
x //= 2  # x = x // 2 → x is now 3.0
x **= 2  # x = x ** 2 → x is now 9.0
x %= 5   # x = x % 5  → x is now 4.0
```

---

## Membership Operators

Check if a value exists in a sequence.

```python
# With strings
"a" in "cat"       # True
"x" in "cat"       # False

# With lists
fruits = ["apple", "banana", "cherry"]
"apple" in fruits       # True
"grape" in fruits       # False
"grape" not in fruits   # True

# With ranges
5 in range(1, 10)   # True
15 in range(1, 10)  # False
```

---

## Identity Operators

Check if two variables refer to the same object in memory.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Equality (==) checks if values are the same
a == b  # True (same values)
a == c  # True (same values)

# Identity (is) checks if it's the same object
a is b  # False (different objects, same values)
a is c  # True (same object!)

# None should be checked with 'is'
x = None
x is None      # ✅ Correct
x == None      # ⚠️ Works but not recommended
```

---

## Operator Precedence (Highest to Lowest)

| Priority | Operators | Description |
|----------|-----------|-------------|
| 1 | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `not` | Unary plus, minus, NOT |
| 4 | `*`, `/`, `//`, `%` | Multiplication, division |
| 5 | `+`, `-` | Addition, subtraction |
| 6 | `<`, `<=`, `>`, `>=`, `==`, `!=` | Comparisons |
| 7 | `is`, `is not` | Identity |
| 8 | `in`, `not in` | Membership |
| 9 | `and` | Logical AND |
| 10 | `or` | Logical OR |

**Tip:** When in doubt, use parentheses to make your intent clear!

```python
# Confusing
result = True or False and False  # True

# Clear
result = True or (False and False)  # True (and evaluates first anyway)
```

---

## Quick Reference

```python
# Arithmetic
+ - * /  // % **

# Comparison
== != < > <= >=

# Logical
and or not

# Assignment
= += -= *= /= //= **= %=

# Membership
in, not in

# Identity
is, is not
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
