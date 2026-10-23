# 🧱 Module 01: Foundations

The building blocks of every program. Master these, and you'll have a solid base for everything else.

---

## What's in This Module

| Topic | Description |
|-------|-------------|
| [01_variables_and_types](01_variables_and_types/README.md) | Storing and naming data |
| [02_operators](02_operators/README.md) | Math, comparison, and logic |
| [03_control_flow](03_control_flow/README.md) | Making decisions with if/else |
| [04_loops](04_loops/README.md) | Repeating actions |
| [05_functions_basics](05_functions_basics/README.md) | Creating reusable code blocks |
| [06_input_output](06_input_output/README.md) | Getting and displaying data |

---

## Learning Objectives

By the end of this module, you will:

- ✅ Store data in variables with appropriate types
- ✅ Perform calculations and comparisons
- ✅ Make your program take different paths based on conditions
- ✅ Repeat code efficiently with loops
- ✅ Organize code into reusable functions
- ✅ Interact with users through input and output

---

## Time Estimate

⏱️ **8-10 hours** total for this module

| Topic | Time |
|-------|------|
| Variables and Types | 1-2 hours |
| Operators | 1 hour |
| Control Flow | 1-2 hours |
| Loops | 1-2 hours |
| Functions | 2-3 hours |
| Input/Output | 1 hour |

---

## Prerequisites

- Python installed ([00_getting_started](../00_getting_started/README.md))
- A code editor ready to use

---

## Key Concepts Preview

> **60-second list & dict primer** — the examples below (and later topics) sometimes
> group values together before Module 02 explains how. This is all you need for now:
>
> **A list** is an ordered group of items.
> `colors = ["red", "green"]` → `colors.append("blue")` adds one → `colors[0]` is `"red"`.
>
> **A dict** (dictionary) is a group of labeled items.
> `ages = {"Alice": 25}` → `ages["Alice"]` is `25` → `ages["Bob"] = 30` adds one.
>
> Full treatment in **[Module 02: Data Structures](../02_data_structures/README.md)**.

### Variables
```python
name = "Alice"      # A string (text)
age = 25            # An integer (whole number)
height = 1.75       # A float (decimal number)
is_student = True   # A boolean (True/False)
```

### Operators
```python
total = 10 + 5      # Math: 15
is_adult = age >= 18  # Comparison: True
can_vote = is_adult and is_citizen  # Logic
```

### Control Flow
```python
if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote.")
```

### Loops
```python
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

while count < 10:
    count += 1
```

### Functions
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("World")  # "Hello, World!"
```

### Input/Output
```python
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")
```

---

## Start Learning!

Begin with **[01_variables_and_types](01_variables_and_types/README.md)** — the most fundamental concept.
