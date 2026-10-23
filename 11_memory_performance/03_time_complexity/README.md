# ⏱️ Time Complexity

Time complexity describes how runtime grows as input size grows.

You usually care about the *shape* of the growth, not the exact milliseconds.

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

[Back: Module 11 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
