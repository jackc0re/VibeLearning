# ⚙️ Optimization Techniques

Optimization is a skill — and a trap.

The best workflow is:

1. Make it correct.
2. Measure.
3. Improve the bottleneck.
4. Measure again.

---

## ✅ Practical Techniques

### 1) Use the right data structure

- list membership: `O(n)`
- set/dict membership: `O(1)` average

### 2) Avoid repeated work

Cache results when inputs repeat.

### 3) Prefer built-ins

Built-ins like `sum`, `sorted`, `"".join` are implemented in optimized C.

### 4) Profile before guessing

- `timeit` for micro-benchmarks
- `cProfile` for bigger programs
- `tracemalloc` for memory investigations

---

## 🔍 Key Takeaways

- Measure first.
- Optimize the bottleneck, not the code you “feel” is slow.
- Prefer readability until performance is proven to be a problem.

---

[Back: Module 11 README](../README.md)

