# 🧠 Memory Basics Quiz

---

## Question 1
In Python, what does assigning `b = a` (for a list) do?

- A) Creates a deep copy of the list
- B) Creates a shallow copy of the list
- C) Makes `b` refer to the same list object
- D) Converts the list to a tuple

<details>
<summary>Show Answer</summary>

**C)** `b` becomes another reference to the same object.

</details>

---

## Question 2
Why might you use `memoryview` with bytes?

- A) To automatically compress data
- B) To avoid copying when slicing/processing binary data
- C) To convert bytes into a string
- D) To increase recursion depth

<details>
<summary>Show Answer</summary>

**B)** `memoryview` can create a view into the same buffer without copying.

</details>

---

## Question 3
What does `id(obj)` tell you?

- A) The object's value
- B) The object's type
- C) The object's identity (which specific object it is)
- D) How many references point to the object

<details>
<summary>Show Answer</summary>

**C)** `id()` returns an identity that is unique among all living objects.
Two variables have the same `id` exactly when they refer to the same object.

</details>

---

## Question 4
Which of these types is **immutable**?

- A) `list`
- B) `dict`
- C) `set`
- D) `tuple`

<details>
<summary>Show Answer</summary>

**D)** Tuples cannot be changed after creation; lists, dicts, and sets can
change in place.

</details>

---

## Question 5
`data` is a bytes object. What is the difference between `data[1:4]` and
`memoryview(data)[1:4]`?

- A) No difference, both copy the bytes
- B) The plain slice creates a **copy**; the memoryview slice is a **view** into the same buffer
- C) The plain slice is a view; the memoryview slice copies
- D) Both raise `TypeError`

<details>
<summary>Show Answer</summary>

**B)** Slicing bytes copies; slicing a `memoryview` gives another view, so no
copy happens until you ask for one (e.g. `.tobytes()`).

</details>

---

[Back to Memory Basics README](README.md)
