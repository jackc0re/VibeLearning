# ⚡ Lambda Expressions

**Lambda expressions** are small, anonymous functions written in a single line. They are commonly used for short transformations and callbacks.

---

## ✅ Syntax

```python
lambda args: expression
```

Examples:

```python
square = lambda x: x * x
square(4)  # 16

add = lambda a, b: a + b
add(2, 3)  # 5
```

---

## ✅ When to Use

- Short, simple logic
- Passed to higher-order functions (e.g., `map`, `filter`, `sorted`)
- Inline callbacks

---

## ✅ Common Examples

### Sorting with a key
```python
names = ["Alice", "bob", "charlie"]
sorted(names, key=lambda n: n.lower())
```

### Filtering with a lambda
```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
```

---

## ⚠️ Keep It Readable

If the logic gets complex, use a named function instead. Readability matters more than brevity.

---

## 🔍 Key Takeaways

- Lambda functions are anonymous and single-expression.
- Best for short, simple operations.
- Often used with higher-order functions.

---

[Next: Map, Filter, Reduce](../05_map_filter_reduce/README.md)
