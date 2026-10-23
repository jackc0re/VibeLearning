# 🧠 References vs Values Quiz

---

## Question 1
What is the difference between a shallow and a deep copy?

- A) Shallow copies are always faster and always safe
- B) Shallow copy duplicates inner objects; deep copy does not
- C) Shallow copy copies only the outer container; deep copy copies nested objects too
- D) There is no difference in Python

<details>
<summary>Show Answer</summary>

**C)** Shallow copies keep references to the same inner objects.

</details>

---

## Question 2
If two variables reference the same list, what happens when you `append()` through one variable?

- A) Only that variable changes
- B) Both “see” the change because it is the same object
- C) Python raises an error
- D) The list is automatically copied

<details>
<summary>Show Answer</summary>

**B)** Mutation affects the single shared list object.

</details>

---

## Question 3
What does `a is b` check?

- A) That `a` and `b` have equal values
- B) That `a` and `b` are the same object
- C) That `a` and `b` have the same type
- D) That `a` and `b` take the same amount of memory

<details>
<summary>Show Answer</summary>

**B)** `is` compares identity. Two equal but separate lists are `==` but not `is`.

</details>

---

## Question 4
After this code, what is `nested`?

```python
nested = [[1], [2]]
shallow = copy.copy(nested)
shallow[0].append(99)
```

- A) `[[1], [2]]` — the copy is fully independent
- B) `[[1, 99], [2]]` — the inner list is shared with the shallow copy
- C) `[[99], [2]]`
- D) `TypeError`

<details>
<summary>Show Answer</summary>

**B)** A shallow copy shares inner objects, so appending through the copy is
visible through the original. A deep copy would have prevented this.

</details>

---

## Question 5
When is copying (shallow or deep) usually the **wrong** choice?

- A) When you plan to modify the object and don't want callers to see the changes
- B) When the object is large and you only need to read it
- C) When you need an independent version to edit
- D) When the object might be mutated through an alias

<details>
<summary>Show Answer</summary>

**B)** Copying a large object just to read it wastes memory and time.
The other options are the classic *good* reasons to copy.

</details>

---

[Back to References vs Values README](README.md)
