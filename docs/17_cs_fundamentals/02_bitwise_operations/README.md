# ⚡ Bitwise Operations

> Manipulating data at the bit level

---

## What You'll Learn

- How to work with individual bits
- Bitwise operators: AND, OR, XOR, NOT
- Bit shifting: left and right
- Practical uses: permissions, flags, optimization

---

## Why Bitwise Operations?

Computers store everything as bits. Sometimes you need to:
- Check if specific flags are set
- Pack multiple values into a single integer
- Optimize memory usage
- Work with hardware or network protocols

Think of bits like light switches: each one can be ON (1) or OFF (0).

---

## The Bitwise Operators

### AND (`&`) - Both must be ON

```
  1010  (10 in decimal)
& 1100  (12 in decimal)
  ----
  1000  (8 in decimal)
```

**Rule:** Output is 1 only if BOTH inputs are 1.

**Truth Table:**
| A | B | A & B |
|---|---|-------|
| 0 | 0 | 0     |
| 0 | 1 | 0     |
| 1 | 0 | 0     |
| 1 | 1 | 1     |

**Real-world:** Security system with two keys - both must be turned to unlock.

---

### OR (`|`) - At least one is ON

```
  1010  (10 in decimal)
| 1100  (12 in decimal)
  ----
  1110  (14 in decimal)
```

**Rule:** Output is 1 if EITHER input is 1.

**Truth Table:**
| A | B | A \| B |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |

**Real-world:** Light switch with two locations - either can turn on the light.

---

### XOR (`^`) - Exclusive OR (different)

```
  1010  (10 in decimal)
^ 1100  (12 in decimal)
  ----
  0110  (6 in decimal)
```

**Rule:** Output is 1 if inputs are DIFFERENT.

**Truth Table:**
| A | B | A ^ B |
|---|---|-------|
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

**Real-world:** Toggling a light - flipping any switch changes the state.

---

### NOT (`~`) - Invert all bits

```
~ 1010  (10 in decimal)
  ----
  0101  (infinite leading 1s in two's complement)
```

**Rule:** Flip all bits (0 becomes 1, 1 becomes 0).

**Note:** In Python, integers have unlimited precision, so `~n` equals `-n-1`.

| A | ~A |
|---|----|
| 0 | 1  |
| 1 | 0  |

---

## Bit Shifting

### Left Shift (`<<`) - Multiply by 2

```
  00101  (5 in decimal)
<<    2  (shift left by 2)
  -----
  10100  (20 in decimal)
```

Every left shift doubles the number.

---

### Right Shift (`>>`) - Divide by 2

```
  10100  (20 in decimal)
>>    2  (shift right by 2)
  -----
  00101  (5 in decimal)
```

Every right shift halves the number (integer division).

---

## Practical Applications

### 1. Permission System (like Unix file permissions)

```python
READ = 0b001    # 1
WRITE = 0b010   # 2
EXECUTE = 0b100 # 4

# Grant read and write permissions
user_perm = READ | WRITE  # 0b011 = 3

# Check if user has write permission
if user_perm & WRITE:
    print("Can write!")

# Add execute permission
user_perm |= EXECUTE  # Now 0b111 = 7

# Remove write permission
user_perm &= ~WRITE   # Now 0b101 = 5
```

### 2. Feature Flags

```python
FEATURE_A = 1 << 0  # 1 (binary: 0001)
FEATURE_B = 1 << 1  # 2 (binary: 0010)
FEATURE_C = 1 << 2  # 4 (binary: 0100)
FEATURE_D = 1 << 3  # 8 (binary: 1000)

# Enable features A and C
enabled = FEATURE_A | FEATURE_C  # 5

# Check if feature B is enabled
if enabled & FEATURE_B:  # False
    pass
```

### 3. Setting, Clearing, and Toggling Bits

```python
# Set bit 3 (make it 1)
value |= (1 << 3)

# Clear bit 3 (make it 0)
value &= ~(1 << 3)

# Toggle bit 3 (flip it)
value ^= (1 << 3)

# Check bit 3
is_set = value & (1 << 3)
```

---

## Bit Masking

A **mask** is a pattern of bits used to extract or modify specific bits.

### Extracting Lower 4 Bits

```python
value = 0b10101111
mask = 0b00001111   # Keep only last 4 bits

result = value & mask  # 0b00001111 = 15
```

### Extracting a Specific Range

```python
# Extract bits 4-7 from an 8-bit number
value = 0b10110101
mask = 0b11110000   # Bits 4-7

result = (value & mask) >> 4  # 0b1011 = 11
```

---

## Python Bitwise Operators Reference

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `&` | AND | `5 & 3` | `1` |
| `\|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT | `~5` | `-6` |
| `<<` | Left Shift | `5 << 1` | `10` |
| `>>` | Right Shift | `5 >> 1` | `2` |

---

## Common Mistakes ⚠️

### 1. Confusing `&` with `and`
```python
# Wrong - logical operator
if a and b:  # Checks truthiness

# Right - bitwise operator
if a & b:    # Compares each bit
```

### 2. Forgetting parentheses with shifts
```python
# Wrong operator precedence
result = 1 << 2 + 3   # Shifts by 5, not 2!

# Right
result = (1 << 2) + 3  # Shift then add
```

### 3. Not understanding two's complement
```python
# In Python, ~n = -n-1
~5   # Returns -6, not just bit inversion
# Use masking if you want fixed-width behavior
```

### 4. Shifting too far
```python
# In some languages, shifting by width or more is undefined
# Python handles it gracefully, but be careful
1 << 100  # Works in Python (huge number!)
```

---

## Try It Out! 🚀

Run `examples.py` to see bitwise operations in action:
```bash
python examples.py
```

Then try `exercises.py` to practice:
```bash
python exercises.py
```

---

## Key Takeaways

1. **AND (`&`)** keeps bits that are 1 in both operands
2. **OR (`|`)** sets bits that are 1 in either operand
3. **XOR (`^`)** sets bits that are different
4. **NOT (`~`)** inverts all bits (in Python: `~n = -n-1`)
5. **Left shift (`<<`)** multiplies by 2
6. **Right shift (`>>`)** divides by 2
7. Bitwise operations are fast and memory-efficient

---

**Previous:** [Number Systems ←](../01_number_systems/README.md)  
**Next:** [Boolean Logic →](../03_boolean_logic/README.md)
