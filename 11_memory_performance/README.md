# 🧠 Module 11: Memory & Performance

Writing correct programs is step one. Writing programs that are **fast enough** and **use memory efficiently** is step two.

This module teaches the practical side of performance:

- how Python stores objects in memory,
- what “references” actually mean,
- how to reason about **time/space complexity**,
- and how to apply safe, measurable optimizations.

> **Estimated Time:** 8-10 hours  \
> **Prerequisites:** Module 02 (Data Structures), Module 03 (Algorithms)  \
> **Level:** ⭐⭐⭐ Intermediate

---

## 📚 Topics Covered

| # | Topic | Description | Key Concepts |
|---|-------|-------------|--------------|
| 01 | [Memory Basics](01_memory_basics/README.md) | How Python represents objects | `id()`, mutability, GC, `memoryview` |
| 02 | [References vs Values](02_references_vs_values/README.md) | Aliasing and copying | shallow vs deep copy, `copy` module |
| 03 | [Time Complexity](03_time_complexity/README.md) | Reason about runtime growth | linear vs quadratic, sets vs lists |
| 04 | [Space Complexity](04_space_complexity/README.md) | Reason about memory usage | in-place, recursion stack, generators |
| 05 | [Big-O Notation](05_big_o_notation/README.md) | Analyze algorithms consistently | common Big-O classes, tradeoffs |
| 06 | [Optimization Techniques](06_optimization_techniques/README.md) | Make code faster safely | profiling, caching, built-ins |

---

## 🎯 Learning Goals

By the end of this module, you should be able to:

- Explain how Python uses **object references** and why “assignment doesn’t copy”.
- Predict how runtime changes when input size grows (Big-O).
- Choose data structures with appropriate performance characteristics.
- Identify “slow” patterns (nested loops, repeated work, unnecessary copies).
- Apply optimizations **only after measuring**.

---

## 📂 Module Structure

```
11_memory_performance/
├── README.md
├── 01_memory_basics/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 02_references_vs_values/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 03_time_complexity/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 04_space_complexity/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 05_big_o_notation/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
└── 06_optimization_techniques/
    ├── README.md
    ├── examples.py
    ├── exercises.py
    └── quiz.md
```

---

**Start here:** [01_memory_basics](01_memory_basics/README.md)

