# 🧠 Map, Filter, Reduce Quiz

Test your understanding of map, filter, and reduce.

---

## Question 1
What does `map` do?

- A) Filters elements by condition
- B) Transforms each element using a function
- C) Combines elements into one
- D) Sorts a list

<details>
<summary>Show Answer</summary>

**B)** `map` applies a function to each element.

</details>

---

## Question 2
What does this produce?

```python
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
```

- A) [1, 3]
- B) [2, 4]
- C) [1, 2, 3, 4]
- D) []

<details>
<summary>Show Answer</summary>

**B)** It keeps the even numbers.

</details>

---

## Question 3
Where is `reduce` imported from?

- A) math
- B) itertools
- C) functools
- D) collections

<details>
<summary>Show Answer</summary>

**C)** `reduce` is in `functools`.

</details>

---

## Question 4
What does this return?

```python
from functools import reduce
reduce(lambda acc, x: acc + x, [1, 2, 3], 0)
```

- A) 3
- B) 6
- C) 0
- D) Error

<details>
<summary>Show Answer</summary>

**B)** It sums to 6.

</details>

---

## Question 5
Which Python alternative is often more readable than map/filter?

- A) List comprehensions
- B) while loops only
- C) try/except
- D) slicing

<details>
<summary>Show Answer</summary>

**A)** List comprehensions are often clearer in Python.

</details>

---

[Back to Map/Filter/Reduce README](README.md) | [Next: Closures →](../06_closures/README.md)
