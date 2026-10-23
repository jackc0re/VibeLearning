# 📊 Module 03: Algorithms

> **Estimated Time:** 19-24 hours  
> **Prerequisites:** Modules 01 (Foundations), 02 (Data Structures)  
> **Level:** ⭐⭐⭐ Intermediate

---

## 🎯 What You'll Learn

Algorithms are step-by-step procedures for solving problems. In this module, you'll master:

- **Searching** — Finding elements efficiently
- **Sorting** — Organizing data in order
- **Recursion** — Solving problems by breaking them into smaller pieces
- **Dynamic Programming** — Optimizing by storing subproblem solutions
- **Greedy Algorithms** — Making locally optimal choices
- **Divide and Conquer** — Breaking problems into independent subproblems
- **Graph Algorithms** — Traversing and analyzing connected data
- **Two Pointers & Sliding Window** — Turning nested loops into one pass
- **Backtracking** — Enumerating solutions with choose/explore/unchoose

---

## 📚 Topics

| # | Topic | Description | Key Concepts |
|---|-------|-------------|--------------|
| 01 | [Searching](01_searching/README.md) | Finding elements in collections | Linear search, binary search |
| 02 | [Sorting](02_sorting/README.md) | Ordering elements | Bubble, selection, insertion, merge, quick sort |
| 03 | [Recursion](03_recursion/README.md) | Self-referential problem solving | Base case, recursive case, call stack |
| 04 | [Dynamic Programming](04_dynamic_programming/README.md) | Optimization through memoization | Overlapping subproblems, optimal substructure |
| 05 | [Greedy Algorithms](05_greedy_algorithms/README.md) | Local optimization strategies | Greedy choice property, activity selection |
| 06 | [Divide and Conquer](06_divide_and_conquer/README.md) | Breaking down problems | Merge sort, quick sort, binary search |
| 07 | [Graph Algorithms](07_graph_algorithms/README.md) | Traversing connected structures | BFS, DFS, shortest paths |
| 08 | [Two Pointers & Sliding Window](08_two_pointers_sliding_window/README.md) | Interview-pattern techniques | opposite/fast-slow pointers, fixed & dynamic windows |
| 09 | [Backtracking](09_backtracking/README.md) | Building solutions, then undoing | choose/explore/unchoose, pruning, N-Queens, Sudoku |

---

## 🧠 Why Algorithms Matter

```
"An algorithm must be seen to be believed." — Donald Knuth
```

Understanding algorithms helps you:

1. **Write efficient code** — Choose the right approach for each problem
2. **Pass technical interviews** — Algorithms are a core interview topic
3. **Think systematically** — Break complex problems into manageable steps
4. **Optimize performance** — Know when O(n) vs O(n²) matters

---

## 📖 How to Study This Module

### Step 1: Understand the Concept
Read each topic's README to understand:
- What problem the algorithm solves
- How it works (step by step)
- When to use it
- Time and space complexity

### Step 2: Study the Examples
Run and modify `examples.py` to see algorithms in action:
```bash
cd 03_algorithms/01_searching
python examples.py
```

### Step 3: Practice
Complete the exercises in `exercises.py`:
- Start with the easier problems
- Write code before looking at hints
- Test with different inputs

### Step 4: Test Your Knowledge
Take the quiz in `quiz.md` to verify understanding.

---

## 🔑 Key Complexity Classes

Understanding Big-O notation is crucial for this module:

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access by index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Naive recursive fibonacci |

---

## 🗺️ Learning Path

```
01_searching ──────┐
                   ├──► 03_recursion ──► 04_dynamic_programming
02_sorting ────────┤                          │
                   │                          ▼
                   ├──► 06_divide_and_conquer
                   │
                   └──► 07_graph_algorithms
```

> 08_two_pointers_sliding_window and 09_backtracking slot in after sorting and
> recursion respectively — they are pattern drills, not new dependencies.

**Recommended order:**
1. Start with **Searching** — simplest algorithms
2. Move to **Sorting** — builds on comparisons
3. Learn **Recursion** — fundamental technique
4. Study **Divide and Conquer** — applies recursion
5. Tackle **Dynamic Programming** — optimizes recursion
6. Explore **Greedy Algorithms** — alternative approach
7. Finish with **Graph Algorithms** — combines everything
8. Drill **Two Pointers & Sliding Window** — the interview-pattern workhorses
9. Explore **Backtracking** — decision trees you walk and then undo

---

## 💡 Tips for Success

1. **Trace through by hand** — Draw arrays and step through algorithms on paper
2. **Visualize** — Use sites like [visualgo.net](https://visualgo.net/) to see algorithms animate
3. **Implement from scratch** — Don't just read, write the code yourself
4. **Analyze complexity** — Always think about time and space
5. **Practice variations** — Same algorithm, different problems

---

## 📂 Module Structure

```
03_algorithms/
├── README.md (this file)
├── 01_searching/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 02_sorting/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 03_recursion/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 04_dynamic_programming/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 05_greedy_algorithms/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 06_divide_and_conquer/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 07_graph_algorithms/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 08_two_pointers_sliding_window/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
└── 09_backtracking/
    ├── README.md
    ├── examples.py
    ├── exercises.py
    └── quiz.md
```

---

## ✅ Completion Checklist

- [ ] Complete all 9 topic READMEs
- [ ] Run and understand all examples
- [ ] Solve at least 3 exercises per topic
- [ ] Pass all quizzes with 80%+ score
- [ ] Implement one algorithm from memory

---

**Ready to start? Begin with [01_searching](01_searching/README.md)!**
