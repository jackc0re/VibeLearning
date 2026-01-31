# 🔲 Boolean Logic

> The foundation of digital circuits and programming conditions

---

## What You'll Learn

- Logic gates: AND, OR, NOT, and more
- Truth tables
- Boolean algebra and De Morgan's Laws
- How boolean logic powers programming

---

## What is Boolean Logic?

Boolean logic is a branch of algebra that deals with **true** and **false** values (1 and 0). It was invented by George Boole in the 1800s and is the foundation of:
- Computer circuits
- Programming conditions (if statements)
- Database queries
- Search engines

Think of boolean logic as the "decision-making" system of computers.

---

## The Three Basic Gates

### AND Gate

**Output is TRUE only if ALL inputs are TRUE.**

```
A ──┐
    ├─── Output
B ──┘
```

| A | B | A AND B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 1       |

**Real-world:** A car that needs both a key AND the brake pressed to start.

---

### OR Gate

**Output is TRUE if ANY input is TRUE.**

```
A ──┐
    ├─── Output
B ──┘
```

| A | B | A OR B |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |

**Real-world:** A light switch that can be turned on from upstairs OR downstairs.

---

### NOT Gate (Inverter)

**Output is the OPPOSITE of the input.**

```
A ──[NOT]─── Output
```

| A | NOT A |
|---|-------|
| 0 | 1     |
| 1 | 0     |

**Real-world:** A light that turns on when it gets DARK (NOT light).

---

## More Logic Gates

### NAND (NOT AND)

Output is FALSE only when ALL inputs are TRUE.

| A | B | A NAND B |
|---|---|----------|
| 0 | 0 | 1        |
| 0 | 1 | 1        |
| 1 | 0 | 1        |
| 1 | 1 | 0        |

**Fun fact:** NAND gates are "universal" - you can build ANY other gate using only NANDs!

---

### NOR (NOT OR)

Output is TRUE only when ALL inputs are FALSE.

| A | B | A NOR B |
|---|---|---------|
| 0 | 0 | 1       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 0       |

---

### XOR (Exclusive OR)

Output is TRUE when inputs are DIFFERENT.

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

**Real-world:** A light that toggles when either switch is flipped.

---

### XNOR (Exclusive NOR)

Output is TRUE when inputs are the SAME.

| A | B | A XNOR B |
|---|---|----------|
| 0 | 0 | 1        |
| 0 | 1 | 0        |
| 1 | 0 | 0        |
| 1 | 1 | 1        |

---

## Logic Gate Reference

| Gate  | Symbol | Python | Description                    |
|-------|--------|--------|--------------------------------|
| AND   | ∧      | `and`  | True if both are true          |
| OR    | ∨      | `or`   | True if either is true         |
| NOT   | ¬      | `not`  | Inverts the value              |
| NAND  | ↑      | `not (a and b)` | Not AND           |
| NOR   | ↓      | `not (a or b)`  | Not OR            |
| XOR   | ⊕      | `a != b` | True if different           |
| XNOR  | ⊙      | `a == b` | True if same                |

---

## Boolean Algebra

Boolean algebra defines rules for working with boolean values.

### Basic Laws

**Identity Laws:**
```
A AND 1 = A
A OR 0 = A
```

**Null Laws:**
```
A AND 0 = 0
A OR 1 = 1
```

**Idempotent Laws:**
```
A AND A = A
A OR A = A
```

**Complement Laws:**
```
A AND (NOT A) = 0
A OR (NOT A) = 1
```

**Double Negation:**
```
NOT (NOT A) = A
```

### Commutative, Associative, Distributive

**Commutative:**
```
A AND B = B AND A
A OR B = B OR A
```

**Associative:**
```
(A AND B) AND C = A AND (B AND C)
(A OR B) OR C = A OR (B OR C)
```

**Distributive:**
```
A AND (B OR C) = (A AND B) OR (A AND C)
A OR (B AND C) = (A OR B) AND (A OR C)
```

---

## De Morgan's Laws

De Morgan's Laws are powerful tools for simplifying boolean expressions.

### Law 1
```
NOT (A AND B) = (NOT A) OR (NOT B)
```

**In words:** "Not (A and B)" means "Not A or Not B"

Example:
- "Not (sunny and warm)" = "Not sunny OR Not warm"

### Law 2
```
NOT (A OR B) = (NOT A) AND (NOT B)
```

**In words:** "Not (A or B)" means "Not A and Not B"

Example:
- "Not (rainy or cold)" = "Not rainy AND Not cold"

---

## Boolean Logic in Programming

### If Statements

```python
# AND
if has_ticket and is_adult:
    enter_concert()

# OR
if is_weekend or is_holiday:
    sleep_in()

# NOT
if not is_raining:
    go_for_walk()

# Combined
if (has_key and has_permission) or is_admin:
    open_door()
```

### Truthiness in Python

Python treats certain values as "falsy":
- `False`
- `0` (integer)
- `0.0` (float)
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dict)
- `None`

Everything else is "truthy".

```python
name = input("Enter your name: ")
if name:  # True if name is not empty
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")
```

### Short-Circuit Evaluation

Python only evaluates what it needs to:

```python
# AND: Stops at first False
False and expensive_function()  # expensive_function never runs!

# OR: Stops at first True
True or expensive_function()    # expensive_function never runs!
```

---

## Building Complex Gates

You can combine basic gates to create complex logic:

### Half Adder
Adds two single bits, outputs sum and carry.

```
A ──┬──[XOR]─── Sum
    │
B ──┴──[AND]─── Carry
```

### Full Adder
Adds three bits (including carry from previous addition).

### Multiplexer (MUX)
Selects one of many inputs based on a selector.

---

## Common Mistakes ⚠️

### 1. Confusing `and`/`or` precedence
```python
# Wrong
if age > 18 and has_id or is_vip:
    # Parsed as: (age > 18 and has_id) or is_vip
    pass

# Better with parentheses
if (age > 18 and has_id) or is_vip:
    pass
```

### 2. Using `==` instead of `=` in conditions
```python
# Wrong - assignment, not comparison
if x = 5:  # SyntaxError!
    pass

# Right
if x == 5:
    pass
```

### 3. Double negatives
```python
# Confusing
if not (not is_valid):
    pass

# Simpler
if is_valid:
    pass
```

### 4. Overcomplicating conditions
```python
# Overcomplicated
if (x > 0 and x < 10) or (x > 0 and x == 5):
    pass

# Simplified
if x > 0 and x < 10:
    pass
```

---

## Try It Out! 🚀

Run `examples.py` to see boolean logic in action:
```bash
python examples.py
```

Then try `exercises.py` to practice:
```bash
python exercises.py
```

---

## Key Takeaways

1. **AND** is true only when all inputs are true
2. **OR** is true when any input is true
3. **NOT** inverts the value
4. **XOR** is true when inputs are different
5. **De Morgan's Laws** help simplify complex conditions
6. Boolean logic is the foundation of all programming decisions

---

**Previous:** [Bitwise Operations ←](../02_bitwise_operations/README.md)  
**Next:** [Memory Architecture →](../04_memory_architecture/README.md)
