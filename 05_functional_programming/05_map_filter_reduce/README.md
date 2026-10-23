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

## ⚠️ Common Mistakes

1. **Printing the `map`/`filter` object directly** - `print(map(...))` shows
   `<map object ...>` because these return *lazy iterators*. Wrap them in
   `list(...)` to see the values.
2. **Using the iterator twice** - a `map`/`filter` object is exhausted after one
   pass; a second loop over it silently yields nothing. Convert to a list first
   if you need it twice.
3. **Swapping the argument order** - the function comes first:
   `map(fn, nums)`, not `map(nums, fn)`.
4. **Using `reduce` without importing it** - unlike `map` and `filter`, `reduce`
   is not built in: `from functools import reduce`.
5. **Reducing an empty sequence without an initializer** - `reduce(fn, [])` raises
   `TypeError`. Pass a starting value: `reduce(fn, nums, 0)`.

---

## 📝 Quick Reference

| Function | Signature | Returns | Needs |
|---|---|---|---|
| `map` | `map(fn, iterable)` | lazy iterator | built in |
| `filter` | `filter(predicate, iterable)` | lazy iterator (truthy kept) | built in |
| `reduce` | `reduce(fn, iterable, initializer)` | a single value | `from functools import reduce` |

```python
from functools import reduce

nums = [1, 2, 3, 4]
evens = list(filter(lambda n: n % 2 == 0, nums))   # [2, 4]
total = reduce(lambda acc, n: acc + n, nums, 0)    # 10
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
