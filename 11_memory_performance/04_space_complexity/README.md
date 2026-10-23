# 🧳 Space Complexity

Space complexity describes how much **extra memory** an algorithm uses as input grows.

Important idea: distinguish between:

- **input space** (the data you already have)
- **auxiliary space** (extra memory the algorithm allocates)

---

## ✅ Common Space Patterns

- Building a new list of size `n` → `O(n)` extra space
- Using a few variables → `O(1)` extra space
- Recursion adds call stack frames → often `O(depth)`

---

## ✅ Generators vs Lists

```python
squares_list = [x * x for x in range(1_000_000)]  # stores everything
squares_gen = (x * x for x in range(1_000_000))   # computes one at a time
```

Generators often reduce memory usage because they don’t store all results at once.

---

## 🔍 Key Takeaways

- Favor in-place operations when safe.
- Prefer generators for streaming data.
- Remember recursion uses stack memory.

---

[Back: Module 11 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
