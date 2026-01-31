# 📝 Boolean Logic Quiz

Test your understanding of logic gates, truth tables, and boolean algebra.

---

## Question 1

What is the output of an AND gate when both inputs are 1?

- A) 0
- B) 1
- C) Depends on the other gate
- D) Undefined

---

## Question 2

According to De Morgan's Law, what is `NOT (A AND B)` equal to?

- A) `(NOT A) AND (NOT B)`
- B) `(NOT A) OR (NOT B)`
- C) `A OR B`
- D) `A AND B`

---

## Question 3

What is the output of an XOR gate when both inputs are the same?

- A) 1
- B) 0
- C) Depends on the value
- D) Error

---

## Question 4

Which boolean law states that `A AND (B OR C) = (A AND B) OR (A AND C)`?

- A) Commutative Law
- B) Associative Law
- C) Distributive Law
- D) Identity Law

---

## Question 5

In Python, what is the result of `True or expensive_function()`?

- A) It calls `expensive_function()` and returns its result
- B) It returns `True` without calling `expensive_function()`
- C) It raises an error
- D) It depends on what `expensive_function()` returns

---

## Question 6

What makes the NAND gate "universal"?

- A) It can only be used in NAND flash memory
- B) It can be used to build any other logic gate
- C) It always outputs True
- D) It requires no power

---

## Question 7

What is `A OR (A AND B)` simplified to?

- A) A AND B
- B) A OR B
- C) A
- D) B

---

## Question 8

In Python, which value is considered "falsy"?

- A) `"0"` (string with zero)
- B) `[0]` (list containing zero)
- C) `0` (integer zero)
- D) `True`

---

## Question 9

What is the output of a NOR gate when both inputs are 0?

- A) 0
- B) 1
- C) Undefined
- D) Depends on previous state

---

## Question 10

If `A = True` and `B = False`, what is `(A AND B) OR (NOT B)`?

- A) True
- B) False
- C) Error
- D) None

---

# Answers

<details>
<summary>Click to reveal answers</summary>

## Answer 1
**B) 1**

AND outputs 1 only when BOTH inputs are 1. This is its defining characteristic.

---

## Answer 2
**B) `(NOT A) OR (NOT B)`**

De Morgan's First Law states that the negation of a conjunction is the disjunction of the negations. In plain English: "Not (A and B)" equals "Not A or Not B".

---

## Answer 3
**B) 0**

XOR (Exclusive OR) outputs 1 only when the inputs are DIFFERENT. When both inputs are the same (both 0 or both 1), XOR outputs 0.

---

## Answer 4
**C) Distributive Law**

The distributive law shows how AND distributes over OR (and vice versa). It's analogous to regular algebra where `a × (b + c) = (a × b) + (a × c)`.

---

## Answer 5
**B) It returns `True` without calling `expensive_function()`**

Python uses short-circuit evaluation for boolean operations. Since `True OR anything` is always `True`, Python doesn't need to evaluate the right side.

---

## Answer 6
**B) It can be used to build any other logic gate**

The NAND gate is called universal because any boolean function can be implemented using only NAND gates. This is useful in circuit design and manufacturing.

---

## Answer 7
**C) A**

This is the Absorption Law. If A is true, the whole expression is true regardless of B. If A is false, `(A AND B)` is also false, so the result is false (which equals A).

---

## Answer 8
**C) `0` (integer zero)**

In Python, the integer `0` is falsy. However, `"0"` is a non-empty string (truthy), and `[0]` is a non-empty list (truthy). Only empty collections and zero values are falsy.

---

## Answer 9
**B) 1**

NOR (NOT OR) outputs 1 only when BOTH inputs are 0. It's the opposite of OR, which outputs 0 only when both inputs are 0.

---

## Answer 10
**A) True**

Step by step:
1. `A AND B` = `True AND False` = `False`
2. `NOT B` = `NOT False` = `True`
3. `False OR True` = `True`

</details>

---

## Scoring

- **9-10 correct:** 🏆 Logic Master!
- **7-8 correct:** 👍 Solid understanding
- **5-6 correct:** 📚 Review the material
- **Below 5:** 🔄 Start with the README and examples

---

## Next Steps

Ready for more? Move on to [Memory Architecture](../04_memory_architecture/README.md) to learn how computers store and manage data!
