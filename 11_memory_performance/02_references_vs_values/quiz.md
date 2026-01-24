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

[Back to References vs Values README](README.md)

