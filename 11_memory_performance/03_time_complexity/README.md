# ⏱️ Time Complexity

Time complexity describes how runtime grows as input size grows.

You usually care about the *shape* of the growth, not the exact milliseconds.

> **📖 About the `O()` notation on this page:** `O(n)` is a compact way to describe
> how an algorithm's runtime grows as input grows (`n` = input size). We use it here
> informally — the full explanation is in [Big-O Notation](../05_big_o_notation/README.md).

---

## ✅ Common Patterns

| Pattern | Example | Typical Big-O |
|--------|---------|---------------|
| Constant | Access `arr[0]` | `O(1)` |
| Linear | Loop over list | `O(n)` |
| Quadratic | Nested loops over list | `O(n^2)` |
| Logarithmic | Binary search | `O(log n)` |

---

## ✅ Data Structures Matter

Checking membership:

```python
target in some_list  # O(n)
target in some_set   # O(1) average
```

Same problem, different runtime.

---

## 🔍 Key Takeaways

- Focus on growth trends (`n`, `n^2`, `log n`).
- Use sets/dicts for fast membership when appropriate.
- Avoid unnecessary nested loops.

---

## ⚠️ Common Mistakes

- Guessing what is slow instead of **measuring** (see [Optimization Techniques](../06_optimization_techniques/README.md))
- Using a list for repeated membership checks when a set/dict would be `O(1)`
- Nesting loops "just for now" — `O(n^2)` hides until the data grows

---

## 📝 Quick Reference

| Operation | `list` | `set`/`dict` (average) |
|-----------|--------|------------------------|
| membership `x in c` | `O(n)` | `O(1)` |
| access by index/key | `O(1)` | `O(1)` |
| append / add | `O(1)` amortized | `O(1)` |
| remove by value | `O(n)` | `O(1)` |

---

[Back: Module 11 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
