# 🧳 Space Complexity

Space complexity describes how much **extra memory** an algorithm uses as input grows.

Important idea: distinguish between:

- **input space** (the data you already have)
- **auxiliary space** (extra memory the algorithm allocates)

> **📖 About the `O()` notation on this page:** `O(n)` is a compact way to describe
> how an algorithm's memory use grows as input grows (`n` = input size). We use it here
> informally — the full explanation is in [Big-O Notation](../05_big_o_notation/README.md).

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

## ⚠️ Common Mistakes

- Copying a huge list when a **view** or generator would do
- Forgetting that recursion depth costs **stack** memory (deep recursion can crash)
- Assuming generators are faster — they save *memory*, not necessarily *time*

---

## 📝 Quick Reference

```python
[x * x for x in range(n)]  # list:      O(n) extra memory
(x * x for x in range(n))  # generator: O(1) extra memory

nums.sort()                # in-place:  O(1) extra
sorted(nums)               # new list:  O(n) extra
```

---

[Back: Module 11 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
