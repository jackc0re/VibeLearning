# 📝 Operators - Quiz

Test your understanding of operators!

---

## Question 1
What is the result of `17 // 5`?

A) 3.4  
B) 3  
C) 4  
D) 2

<details>
<summary>Click for answer</summary>

**B) 3**

`//` is floor division. It divides and rounds down to the nearest integer.

</details>

---

## Question 2
What is `17 % 5`?

A) 3.4  
B) 3  
C) 2  
D) 0

<details>
<summary>Click for answer</summary>

**C) 2**

`%` (modulo) gives the remainder. 17 = 5 × 3 + **2**

</details>

---

## Question 3
What does `True and False or True` evaluate to?

A) True  
B) False  
C) Error  
D) None

<details>
<summary>Click for answer</summary>

**A) True**

`and` has higher precedence than `or`:
- `True and False` → `False`
- `False or True` → `True`

</details>

---

## Question 4
What is the result of `2 ** 3 ** 2`?

A) 64  
B) 512  
C) 256  
D) Error

<details>
<summary>Click for answer</summary>

**B) 512**

Exponentiation is right-associative:
- First: `3 ** 2` = 9
- Then: `2 ** 9` = 512

</details>

---

## Question 5
Which expression checks if `x` is between 1 and 10 (inclusive)?

A) `x > 1 and x < 10`  
B) `1 < x < 10`  
C) `1 <= x <= 10`  
D) `x >= 1 or x <= 10`

<details>
<summary>Click for answer</summary>

**C) `1 <= x <= 10`**

This is a chained comparison that includes the endpoints (1 and 10).

</details>

---

## Question 6
What does `"3" in "12345"` return?

A) True  
B) False  
C) 3  
D) Error

<details>
<summary>Click for answer</summary>

**A) True**

The `in` operator checks if the substring "3" exists in "12345". It does!

</details>

---

## Question 7
Given `a = [1, 2, 3]` and `b = [1, 2, 3]`, what is `a is b`?

A) True  
B) False  
C) [1, 2, 3]  
D) Error

<details>
<summary>Click for answer</summary>

**B) False**

`is` checks if they're the same object in memory. They have equal values (`a == b` is True), but they're different objects.

</details>

---

## Question 8
What is `10 / 5`?

A) 2  
B) 2.0  
C) 2.5  
D) Error

<details>
<summary>Click for answer</summary>

**B) 2.0**

Regular division `/` always returns a float, even when the result is a whole number.

</details>

---

## Question 9
What does `x += 3` mean?

A) x = 3  
B) x = x + 3  
C) x + 3  
D) x == x + 3

<details>
<summary>Click for answer</summary>

**B) x = x + 3**

`+=` is a compound assignment operator. It adds and assigns in one step.

</details>

---

## Question 10
What is `not (True or False)`?

A) True  
B) False  
C) None  
D) Error

<details>
<summary>Click for answer</summary>

**B) False**

- First: `True or False` → `True`
- Then: `not True` → `False`

</details>

---

## Bonus Question
What does this return: `"a" < "A"`?

A) True  
B) False  
C) Error  
D) Cannot be compared

<details>
<summary>Click for answer</summary>

**B) False**

In ASCII, uppercase letters (A=65) come before lowercase letters (a=97). So "a" > "A".

</details>

---

## How did you do?

- **9-11 correct:** Operator master! 🏆
- **7-8 correct:** Great job! Review the tricky ones.
- **5-6 correct:** Keep practicing with examples.
- **0-4 correct:** Re-read the README and run examples again.
