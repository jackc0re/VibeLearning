# 📝 Tuples - Quiz

Test your understanding!

---

## Question 1
How do you create a single-element tuple?

A) `(42)`  
B) `(42,)`  
C) `[42]`  
D) `tuple(42)`

<details>
<summary>Click for answer</summary>

**B) `(42,)`**

Without the comma, `(42)` is just an integer in parentheses.

</details>

---

## Question 2
What is the result of `(1, 2, 3)[1]`?

A) 1  
B) 2  
C) (1, 2)  
D) (2,)

<details>
<summary>Click for answer</summary>

**B) 2**

Tuple indexing is 0-based, just like lists.

</details>

---

## Question 3
What happens with `t = (1, 2, 3); t[0] = 99`?

A) t becomes (99, 2, 3)  
B) TypeError  
C) t becomes (1, 2, 3, 99)  
D) No change

<details>
<summary>Click for answer</summary>

**B) TypeError**

Tuples are immutable — you cannot change their elements.

</details>

---

## Question 4
What is tuple unpacking?

A) Converting tuple to list  
B) Assigning tuple elements to variables  
C) Removing elements from tuple  
D) Joining tuples

<details>
<summary>Click for answer</summary>

**B) Assigning tuple elements to variables**

Example: `x, y = (10, 20)` assigns 10 to x and 20 to y.

</details>

---

## Question 5
Which can be a dictionary key?

A) [1, 2]  
B) {1, 2}  
C) (1, 2)  
D) [[1], [2]]

<details>
<summary>Click for answer</summary>

**C) (1, 2)**

Tuples are hashable (immutable), so they can be dict keys. Lists and sets cannot.

</details>

---

## Question 6
What does `first, *rest = (1, 2, 3, 4)` give?

A) first=1, rest=(2, 3, 4)  
B) first=1, rest=[2, 3, 4]  
C) first=(1,), rest=(2, 3, 4)  
D) Error

<details>
<summary>Click for answer</summary>

**B) first=1, rest=[2, 3, 4]**

The `*` operator collects remaining elements into a **list**, not a tuple.

</details>

---

## Question 7
How many methods do tuples have?

A) 0  
B) 2  
C) Many like lists  
D) 5

<details>
<summary>Click for answer</summary>

**B) 2**

Only `count()` and `index()`. Tuples are immutable so no add/remove methods.

</details>

---

## Question 8
What is `(1, 2) + (3, 4)`?

A) (1, 2, 3, 4)  
B) ((1, 2), (3, 4))  
C) [1, 2, 3, 4]  
D) Error

<details>
<summary>Click for answer</summary>

**A) (1, 2, 3, 4)**

Tuples support concatenation with `+`.

</details>

---

## How did you do?

- **7-8 correct:** Excellent! Tuples mastered.
- **5-6 correct:** Good! Review missed ones.
- **0-4 correct:** Re-read README and examples.
