# 🐜 Common Bugs

Some bugs appear so frequently that every developer should recognize them instantly. Learning these patterns helps you avoid them and fix them quickly when they occur.

---

## ✅ Off-By-One Errors

```python
# Bug: Missing last element
for i in range(len(items) - 1):  # Should be len(items)
    process(items[i])

# Bug: Index out of range
items = [1, 2, 3]
last = items[len(items)]  # Should be len(items) - 1

# Bug: Wrong loop bounds
for i in range(1, 10):  # Processes 1-9, not 1-10
    print(i)
```

**Fix:** Always verify loop bounds include/exclude correct values.

---

## ✅ Mutable Default Arguments

```python
# Bug: Shared mutable default
def append_item(item, items=[]):  # BAD!
    items.append(item)
    return items

append_item(1)  # Returns [1]
append_item(2)  # Returns [1, 2] - same list!

# Fix: Use None as default
def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

**Rule:** Never use mutable objects (lists, dicts) as default arguments.

---

## ✅ Modifying While Iterating

```python
# Bug: Modifying list during iteration
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # Skips elements!

# Fix: Iterate over a copy or use list comprehension
items = [1, 2, 3, 4, 5]
items = [x for x in items if x % 2 != 0]

# Or iterate backwards
for i in range(len(items) - 1, -1, -1):
    if items[i] % 2 == 0:
        del items[i]
```

---

## ✅ Variable Scope Issues

```python
# Bug: UnboundLocalError
counter = 0

def increment():
    counter += 1  # Error! Looks for local 'counter'
    return counter

# Fix: Use global (or better, avoid global state)
def increment():
    global counter
    counter += 1
    return counter

# Better fix: Pass and return values
def increment(counter):
    return counter + 1
```

---

## ✅ String/Integer Confusion

```python
# Bug: Comparing string to int
user_input = input("Enter number: ")  # Returns string!
if user_input == 5:  # Always False
    print("Got 5")

# Fix: Convert types
if int(user_input) == 5:
    print("Got 5")
```

---

## ✅ None Comparisons

```python
# Bug: Using == for None
if value == None:  # Works but not idiomatic
    pass

# Fix: Use 'is' for None
if value is None:
    pass

# Bug: Not handling None
def process(data):
    return data.upper()  # Crashes if data is None

# Fix: Check for None
def process(data):
    if data is None:
        return ""
    return data.upper()
```

---

## ✅ Shallow vs Deep Copy

```python
# Bug: Shallow copy shares nested objects
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] - also changed!

# Fix: Use deep copy for nested structures
import copy
deep = copy.deepcopy(original)
```

---

## ✅ Boolean Traps

```python
# Bug: Empty collections are falsy
items = []
if not items:
    print("No items")  # This runs

# Bug: Zero is falsy
count = 0
if count:  # False!
    print("Has count")

# Be explicit when checking for None vs empty vs zero
if items is None:
    print("Not initialized")
elif len(items) == 0:
    print("Empty list")
```

---

## ✅ Late Binding in Closures

```python
# Bug: All functions use final value of i
funcs = []
for i in range(3):
    funcs.append(lambda: i)

[f() for f in funcs]  # [2, 2, 2] - all use i=2!

# Fix: Capture current value
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)  # Default argument captures

[f() for f in funcs]  # [0, 1, 2]
```

---

## 🔍 Key Takeaways

- Check loop bounds for off-by-one errors.
- Never use mutable default arguments.
- Don't modify collections while iterating them.
- Be aware of variable scope in functions.
- Use `is` for None comparisons.
- Remember shallow copy vs deep copy.
- Capture loop variables in closures explicitly.

---

[Back: Reading Tracebacks](../03_reading_tracebacks/) | [Back to Module 14](../README.md)
