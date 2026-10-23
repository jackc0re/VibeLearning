# 📈 Big-O Notation

Big-O is a way to describe how runtime (or memory) grows with input size `n`.

It ignores constant factors and focuses on long-term growth.

---

## ✅ Common Big-O Classes

| Big-O | Name | Example |
|------|------|---------|
| `O(1)` | constant | dict/set membership (average) |
| `O(log n)` | logarithmic | binary search |
| `O(n)` | linear | scanning a list |
| `O(n log n)` | linearithmic | merge sort |
| `O(n^2)` | quadratic | nested loops over list |

---

## ✅ How to Analyze

- Loops add up: `for` over `n` → `O(n)`
- Nested loops multiply: `n` inside `n` → `O(n^2)`
- Sequential steps: keep the dominant term: `O(n) + O(n^2)` → `O(n^2)`

---

## 🔍 Key Takeaways

- Big-O is about growth, not exact time.
- Use it to compare approaches.
- Don’t guess: reason about loops, recursion, and data structure operations.

---

[Back: Module 11 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
