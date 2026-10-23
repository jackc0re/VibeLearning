# 🧮 Map, Filter, Reduce

These three functions are classic tools in functional programming:

- **map**: transform each element
- **filter**: keep elements that match a condition
- **reduce**: combine all elements into one value

---

## ✅ map

Apply a function to every element.

```python
nums = [1, 2, 3]
squares = list(map(lambda x: x * x, nums))
# [1, 4, 9]
```

---

## ✅ filter

Keep items that satisfy a predicate.

```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4]
```

---

## ✅ reduce

Reduce combines values into a single result. In Python, it lives in `functools`.

```python
from functools import reduce
nums = [1, 2, 3, 4]
total = reduce(lambda acc, x: acc + x, nums, 0)
# 10
```

---

## ✅ Alternatives

Python also offers comprehensions, which are often clearer:

```python
sq = [x * x for x in nums]
ev = [x for x in nums if x % 2 == 0]
```

---

## 🔍 Key Takeaways

- `map` transforms, `filter` selects, `reduce` aggregates.
- Use lambdas for short logic, named functions for clarity.
- Comprehensions are often more readable in Python.

---

[Next: Closures](../06_closures/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
