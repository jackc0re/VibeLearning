# 📝 Sets - Quiz

Test your understanding! Try to answer without looking back.

---

## Question 1
How do you create an empty set?

A) `{}`  
B) `set()`  
C) `[]`  
D) `set{}`

<details>
<summary>Click for answer</summary>

**B) `set()`**

`{}` creates an empty **dictionary**, not a set. This is a common gotcha in Python!

</details>

---

## Question 2
What is the result?
```python
s = {1, 2, 2, 3, 3, 3}
print(len(s))
```

A) 6  
B) 3  
C) 1  
D) Error

<details>
<summary>Click for answer</summary>

**B) 3**

Sets automatically remove duplicates. The set contains only `{1, 2, 3}`.

</details>

---

## Question 3
What does `{1, 2, 3} & {2, 3, 4}` return?

A) {1, 2, 3, 4}  
B) {2, 3}  
C) {1, 4}  
D) {}

<details>
<summary>Click for answer</summary>

**B) {2, 3}**

`&` is the intersection operator — it returns elements common to both sets.

</details>

---

## Question 4
What is `{1, 2, 3} - {2, 3, 4}`?

A) {1}  
B) {4}  
C) {1, 4}  
D) {2, 3}

<details>
<summary>Click for answer</summary>

**A) {1}**

`-` is the difference operator — elements in the first set but not in the second.

</details>

---

## Question 5
Which can be added to a set?

A) [1, 2, 3]  
B) {"a": 1}  
C) (1, 2, 3)  
D) {1, 2, 3}

<details>
<summary>Click for answer</summary>

**C) (1, 2, 3)**

Set elements must be hashable (immutable). Lists, dicts, and sets are mutable. Tuples are immutable.

</details>

---

## Question 6
What is `{1, 2}.issubset({1, 2, 3})`?

A) True  
B) False  
C) {1, 2}  
D) Error

<details>
<summary>Click for answer</summary>

**A) True**

`{1, 2}` is a subset of `{1, 2, 3}` because all elements of `{1, 2}` are in `{1, 2, 3}`.

</details>

---

## Question 7
What's the difference between `remove()` and `discard()`?

A) No difference  
B) `remove()` raises error if missing, `discard()` doesn't  
C) `discard()` raises error if missing, `remove()` doesn't  
D) `remove()` returns the value, `discard()` doesn't

<details>
<summary>Click for answer</summary>

**B) `remove()` raises error if missing, `discard()` doesn't**

Use `discard()` when you're not sure if the element exists and don't want an error.

</details>

---

## Question 8
What is the time complexity of `x in my_set`?

A) O(n)  
B) O(log n)  
C) O(1)  
D) O(n²)

<details>
<summary>Click for answer</summary>

**C) O(1)**

Sets use hash tables, making membership testing constant time on average. This is much faster than lists (O(n)).

</details>

---

## Question 9
What is `{1, 2, 3} ^ {2, 3, 4}`?

A) {1, 4}  
B) {2, 3}  
C) {1, 2, 3, 4}  
D) {}

<details>
<summary>Click for answer</summary>

**A) {1, 4}**

`^` is the symmetric difference — elements in either set but not in both.

</details>

---

## Question 10
What's wrong with this code?
```python
s = {[1, 2], [3, 4]}
```

A) Syntax error  
B) TypeError: lists are unhashable  
C) Empty set  
D) Nothing, it works

<details>
<summary>Click for answer</summary>

**B) TypeError: lists are unhashable**

Lists can't be set elements because they're mutable. Use tuples instead: `s = {(1, 2), (3, 4)}`.

</details>

---

## How did you do?

- **9-10 correct:** Excellent! You've mastered sets.
- **7-8 correct:** Good job! Review the ones you missed.
- **5-6 correct:** Keep practicing with the examples.
- **0-4 correct:** Re-read the README and run the examples again.
