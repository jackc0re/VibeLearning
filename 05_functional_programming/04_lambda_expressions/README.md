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

## ⚠️ Common Mistakes

1. **Trying to put statements in a lambda** - a lambda body is a single *expression*:
   `lambda x: return x` is a `SyntaxError`, and `lambda x: x = x + 1` cannot work.
   If you need statements or multiple lines, write a `def`.
2. **Naming complex lambdas** - `process = lambda row: (row[0].strip(), int(row[1]))`
   hides a real function behind an anonymous-looking name (and PEP 8 advises against
   it). Use a `def` with a docstring once the logic needs a name.
3. **Forgetting that `i` moves on** - `lambda: i` inside a loop reads `i` when the
   lambda is *called*, so every copy sees the final value. Snapshot it:
   `lambda i=i: i`. See the [Closures gotcha](../06_closures/README.md).
4. **Using the `map`/`filter` result twice** - they return lazy iterators; after one
   pass they are empty. Wrap in `list(...)` if you need the results more than once.

---

## 📝 Quick Reference

| Situation | Reach for |
|---|---|
| Tiny one-expression transform, used inline | `lambda` |
| Logic with a name, docstring, or multiple steps | `def` |
| Custom sort order | `sorted(xs, key=lambda item: ...)` |
| Keep matching items | `filter(lambda x: ..., xs)` or a comprehension |
| Transform every item | `map(lambda x: ..., xs)` or a comprehension |

```python
pairs = [("b", 2), ("a", 1)]
pairs.sort(key=lambda pair: pair[1])   # sort by the number -> [("a", 1), ("b", 2)]
```

---

## 🔍 Key Takeaways

- Lambda functions are anonymous and single-expression.
- Best for short, simple operations.
- Often used with higher-order functions.

---

[Next: Map, Filter, Reduce](../05_map_filter_reduce/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
