# 🔢 Number Systems

> Understanding how computers count differently than humans

---

## What You'll Learn

- Why computers use binary (base-2)
- How to convert between number systems
- Decimal, binary, octal, and hexadecimal
- Python's built-in conversion functions

---

## The Story of Counting

Humans have ten fingers, so we naturally count in **base-10** (decimal). Computers have electrical circuits that are either ON or OFF, so they count in **base-2** (binary).

Think of it like different languages:
- Decimal: English (what humans speak)
- Binary: Computer's native language
- Hexadecimal: A compact way to write binary (like shorthand)

---

## Decimal (Base-10) 🧮

The number system you're most familiar with. Uses digits 0-9.

```
Decimal: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11...
```

**How it works:**
```
253 = 2×100 + 5×10 + 3×1
    = 2×10² + 5×10¹ + 3×10⁰
```

Each position represents a power of 10.

---

## Binary (Base-2) 💻

Computers only understand 0s and 1s (OFF and ON).

```
Binary: 0, 1, 10, 11, 100, 101, 110, 111, 1000...
```

**How it works:**
```
1011 (binary) = 1×8 + 0×4 + 1×2 + 1×1
              = 1×2³ + 0×2² + 1×2¹ + 1×2⁰
              = 11 (decimal)
```

Each position represents a power of 2.

### Why Binary?

- Electrical circuits have two states: ON (1) or OFF (0)
- Magnetic storage: North/South polarity
- CDs/DVDs: Pits and lands
- Simple and reliable!

---

## Octal (Base-8) 🐙

Uses digits 0-7. Each octal digit represents 3 binary digits.

```
Octal: 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12...
```

**Conversion:**
```
Decimal 10 = Octal 12 = Binary 1010

Binary:  101 110
Octal:     5   6  → 56 (octal)
```

Less common today but still used in:
- Unix file permissions (e.g., `chmod 755`)
- Legacy systems

---

## Hexadecimal (Base-16) 🔮

Uses digits 0-9 and letters A-F. Each hex digit represents 4 binary digits.

```
Hex: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10...

A = 10    B = 11    C = 12    D = 13    E = 14    F = 15
```

**Conversion:**
```
Decimal 255 = Hex FF = Binary 11111111

Binary:  1101 1011
Hex:        D    B  → DB (hex)
```

### Why Hexadecimal?

- More compact than binary
- Easy conversion (4 bits = 1 hex digit)
- Used everywhere in computing:
  - Color codes: `#FF5733`
  - Memory addresses: `0x7FFF5E`
  - MAC addresses
  - Hash values

---

## Python Conversion Functions

Python makes conversions easy with built-in functions:

```python
# To binary
bin(10)      # Returns '0b1010'

# To octal
oct(10)      # Returns '0o12'

# To hexadecimal
hex(10)      # Returns '0xa'

# To decimal (from any base)
int('1010', 2)   # Returns 10
int('12', 8)     # Returns 10
int('a', 16)     # Returns 10
```

**The prefixes:**
- `0b` = binary
- `0o` = octal
- `0x` = hexadecimal

---

## Conversion Methods

### Binary to Decimal

Multiply each bit by its place value and sum:

```
Binary: 1 0 1 0 1
Place: 16 8 4 2 1

Value: 16 + 0 + 4 + 0 + 1 = 21
```

### Decimal to Binary

Repeatedly divide by 2, collect remainders (read bottom-up):

```
13 ÷ 2 = 6 remainder 1
 6 ÷ 2 = 3 remainder 0
 3 ÷ 2 = 1 remainder 1
 1 ÷ 2 = 0 remainder 1

Result: 1101 (read remainders bottom-up)
```

---

## Quick Reference Table

| Decimal | Binary | Octal | Hexadecimal |
|---------|--------|-------|-------------|
| 0       | 0      | 0     | 0           |
| 1       | 1      | 1     | 1           |
| 2       | 10     | 2     | 2           |
| 3       | 11     | 3     | 3           |
| 4       | 100    | 4     | 4           |
| 5       | 101    | 5     | 5           |
| 6       | 110    | 6     | 6           |
| 7       | 111    | 7     | 7           |
| 8       | 1000   | 10    | 8           |
| 9       | 1001   | 11    | 9           |
| 10      | 1010   | 12    | A           |
| 11      | 1011   | 13    | B           |
| 12      | 1100   | 14    | C           |
| 13      | 1101   | 15    | D           |
| 14      | 1110   | 16    | E           |
| 15      | 1111   | 17    | F           |
| 16      | 10000  | 20    | 10          |

---

## Common Mistakes ⚠️

### 1. Forgetting the prefix
```python
# Wrong
int('1010')      # This is decimal 1010, not binary!

# Right
int('1010', 2)   # Specify base=2 for binary
```

### 2. Reading binary remainders in wrong order
```
Decimal 5 to binary:
5 ÷ 2 = 2 R 1
2 ÷ 2 = 1 R 0
1 ÷ 2 = 0 R 1

Result: 101 (NOT 011!)
Read from bottom to top!
```

### 3. Confusing letter values in hex
```
A = 10, not 11
B = 11, not 12
# Remember: A comes after 9, so A = 10
```

### 4. Off-by-one in binary place values
```
Binary: 1 0 0 0
Place:  8 4 2 1  (powers of 2: 2³, 2², 2¹, 2⁰)
        ↑
        Leftmost is 8 (2³), not 4!
```

---

## Try It Out! 🚀

Run `examples.py` to see number systems in action:
```bash
python examples.py
```

Then try `exercises.py` to practice:
```bash
python exercises.py
```

---

## Key Takeaways

1. **Binary** (base-2) is the language of computers (0s and 1s)
2. **Hexadecimal** (base-16) is a compact way to write binary
3. **Octal** (base-8) is still used for file permissions
4. Python provides `bin()`, `oct()`, `hex()`, and `int()` for conversions
5. Understanding number systems helps you debug and work with low-level code

---

**Next:** [Bitwise Operations →](../02_bitwise_operations/README.md)
