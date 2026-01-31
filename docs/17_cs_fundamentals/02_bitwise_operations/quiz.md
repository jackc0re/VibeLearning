# 📝 Bitwise Operations Quiz

Test your understanding of bitwise operators and their applications.

---

## Question 1

What is the result of `12 & 10` in binary?

- A) `1110`
- B) `1000`
- C) `1100`
- D) `1010`

---

## Question 2

Which operation sets a bit to 1 regardless of its current value?

- A) AND (`&`)
- B) OR (`|`)
- C) XOR (`^`)
- D) NOT (`~`)

---

## Question 3

What is `5 << 2` equal to?

- A) 7
- B) 10
- C) 20
- D) 25

---

## Question 4

In Python, what is `~5`?

- A) 10
- B) -6
- C) -5
- D) 4

---

## Question 5

Which bitwise operation is commonly used to toggle (flip) a bit?

- A) AND
- B) OR
- C) XOR
- D) NOT

---

## Question 6

What does `value & ~(1 << 3)` do?

- A) Sets bit 3 to 1
- B) Clears bit 3 to 0
- C) Toggles bit 3
- D) Checks if bit 3 is set

---

## Question 7

If `n = 16`, what is `n >> 3`?

- A) 128
- B) 48
- C) 4
- D) 2

---

## Question 8

What property makes XOR useful for finding a unique number in an array?

- A) `a & a = 0`
- B) `a ^ a = 0`
- C) `a | a = 0`
- D) `~a = 0`

---

## Question 9

Which expression extracts the lower 4 bits of a number?

- A) `value & 0xF0`
- B) `value | 0x0F`
- C) `value & 0x0F`
- D) `value >> 4`

---

## Question 10

How do you check if a number is a power of 2 using bitwise operations?

- A) `n & 1 == 0`
- B) `n & (n - 1) == 0`
- C) `n ^ (n - 1) == 0`
- D) `n | (n - 1) == 0`

---

# Answers

<details>
<summary>Click to reveal answers</summary>

## Answer 1
**B) `1000`**

```
12 = 1100
10 = 1010
     ----
     1000 (8 in decimal)
```

Only positions where both bits are 1 remain 1.

---

## Answer 2
**B) OR (`|`)

OR sets a bit to 1 if either operand has that bit set:
```
value | (1 << n)  # Always sets bit n to 1
```

---

## Answer 3
**C) 20**

Left shift by 2 is equivalent to multiplying by 4:
`5 × 4 = 20`

In binary: `101 << 2 = 10100` (5 → 20)

---

## Answer 4
**B) -6**

In Python, integers are represented with unlimited precision in two's complement.
`~n = -n - 1`, so `~5 = -6`.

---

## Answer 5
**C) XOR**

XOR toggles a bit:
- `0 ^ 1 = 1` (0 becomes 1)
- `1 ^ 1 = 0` (1 becomes 0)

Usage: `value ^= (1 << n)` toggles bit n.

---

## Answer 6
**B) Clears bit 3 to 0**

`~(1 << 3)` creates a mask with all bits set except bit 3.
ANDing with this mask clears bit 3:
```python
value &= ~(1 << 3)  # Clear bit 3
```

---

## Answer 7
**D) 2**

Right shift by 3 divides by 8 (2³):
`16 ÷ 8 = 2`

In binary: `10000 >> 3 = 00010` (16 → 2)

---

## Answer 8
**B) `a ^ a = 0`**

XOR of a number with itself is 0. This property, combined with XOR being commutative and associative, means all pairs cancel out, leaving only the unique number.

---

## Answer 9
**C) `value & 0x0F`**

`0x0F` in binary is `00001111`. ANDing with this mask keeps only the lower 4 bits.

---

## Answer 10
**B) `n & (n - 1) == 0`**

Powers of 2 have exactly one bit set. Subtracting 1 flips all bits up to and including that set bit. ANDing them gives 0 for powers of 2.

Example:
- 8 (1000) - 1 = 7 (0111)
- 8 & 7 = 0 ✓

</details>

---

## Scoring

- **9-10 correct:** 🏆 Bit Manipulation Master!
- **7-8 correct:** 👍 You understand the bits
- **5-6 correct:** 📚 Review the examples
- **Below 5:** 🔄 Start with the README

---

## Next Steps

Ready for more? Move on to [Boolean Logic](../03_boolean_logic/README.md) to learn about logic gates and boolean algebra!
