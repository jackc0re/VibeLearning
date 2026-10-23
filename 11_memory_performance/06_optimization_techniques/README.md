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

- `timeit` for micro-benchmarks - repeat the run and compare the shape of the
  growth, not tiny differences: a single slow run is usually noise
- `cProfile` for bigger programs
- `tracemalloc` for memory investigations

---

## 🔍 Key Takeaways

- Measure first.
- Optimize the bottleneck, not the code you “feel” is slow.
- Prefer readability until performance is proven to be a problem.

---

## ⚠️ Common Mistakes

- Optimizing **before** measuring — the bottleneck is rarely where it feels like it is
- Trusting a single timing run — noise dominates; repeat benchmarks and compare trends
- Micro-optimizing cold code instead of the hot spot the profiler found

---

## 📝 Quick Reference

```python
import time
start = time.perf_counter()      # wall-clock timing
# ... work ...
elapsed = time.perf_counter() - start

import timeit
timeit.repeat("x in d", setup=..., number=100, repeat=3)  # micro-benchmarks

import cProfile
cProfile.run("my_function()")    # where the time goes

import tracemalloc               # where the memory goes
tracemalloc.start()
```

`examples.py` for this topic runs all three measuring tools — read it next.

---

[Back: Module 11 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
