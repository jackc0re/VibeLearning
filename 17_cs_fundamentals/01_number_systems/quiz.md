# 📝 Number Systems Quiz

Test your understanding of decimal, binary, octal, and hexadecimal number systems.

---

## Question 1

What is the decimal value of the binary number `1010`?

- A) 8
- B) 10
- C) 12
- D) 20

---

## Question 2

Which Python function converts a decimal number to hexadecimal?

- A) `to_hex()`
- B) `hexadecimal()`
- C) `hex()`
- D) `to_base16()`

---

## Question 3

What does `int('1010', 2)` return?

- A) `'1010'`
- B) `10`
- C) `1010`
- D) Error

---

## Question 4

Convert the hexadecimal number `FF` to decimal.

- A) 15
- B) 150
- C) 255
- D) 256

---

## Question 5

In binary, what is `1 + 1`?

- A) 2
- B) 10
- C) 11
- D) 0

---

## Question 6

How many bits are in one hexadecimal digit?

- A) 1
- B) 2
- C) 4
- D) 8

---

## Question 7

What is the octal representation of decimal 8?

- A) 8
- B) 10
- C) 16
- D) 0o8

---

## Question 8

Which number system uses digits 0-7 only?

- A) Binary
- B) Decimal
- C) Octal
- D) Hexadecimal

---

## Question 9

What is the binary representation of decimal 5?

- A) 100
- B) 101
- C) 110
- D) 111

---

## Question 10

In the hexadecimal system, what decimal value does the letter `A` represent?

- A) 0
- B) 9
- C) 10
- D) 11

---

# Answers

<details>
<summary>Click to reveal answers</summary>

## Answer 1
**B) 10**

`1010` in binary = 1×8 + 0×4 + 1×2 + 0×1 = 10

---

## Answer 2
**C) `hex()`**

Python's built-in `hex()` function converts decimal to hexadecimal. Example: `hex(255)` returns `'0xff'`.

---

## Answer 3
**B) `10`**

`int('1010', 2)` converts the binary string `'1010'` to its decimal equivalent, which is 10.

---

## Answer 4
**C) 255**

`FF` in hex = F×16 + F = 15×16 + 15 = 240 + 15 = 255

---

## Answer 5
**B) 10**

In binary, `1 + 1 = 10` (read as "one-zero", meaning one 2 and zero 1s). This is equivalent to decimal 2.

---

## Answer 6
**C) 4**

Each hexadecimal digit represents exactly 4 binary digits (bits). This makes conversion between hex and binary very convenient.

---

## Answer 7
**B) 10**

Octal is base-8, so: 8 = 1×8 + 0×1 = `10` in octal (written as `0o10` in Python).

---

## Answer 8
**C) Octal**

Octal is base-8 and uses digits 0 through 7. Binary uses 0-1, decimal uses 0-9, and hexadecimal uses 0-9 and A-F.

---

## Answer 9
**B) 101**

5 in binary: 
- 5 ÷ 2 = 2 remainder 1
- 2 ÷ 2 = 1 remainder 0  
- 1 ÷ 2 = 0 remainder 1

Reading remainders bottom-up: `101`

---

## Answer 10
**C) 10**

In hexadecimal:
- A = 10
- B = 11
- C = 12
- D = 13
- E = 14
- F = 15

</details>

---

## Scoring

- **9-10 correct:** 🏆 Number Systems Master!
- **7-8 correct:** 👍 Solid understanding
- **5-6 correct:** 📚 Review the material
- **Below 5:** 🔄 Start with the README and examples

---

## Next Steps

Ready for more? Move on to [Bitwise Operations](../02_bitwise_operations/README.md) to learn how to manipulate individual bits!
