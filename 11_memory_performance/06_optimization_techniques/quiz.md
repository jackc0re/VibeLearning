# 🧠 Optimization Techniques Quiz

---

## Question 1
What is usually the best first step before optimizing code?

- A) Rewrite everything in a different language
- B) Add caching everywhere
- C) Measure and identify the bottleneck
- D) Remove all comments

<details>
<summary>Show Answer</summary>

**C)** Profiling/measurement tells you what is actually slow.

</details>

---

## Question 2
Why is `"".join(parts)` typically faster than repeated string concatenation in a loop?

- A) It uses less CPU because it skips checks
- B) It is implemented in optimized C and avoids many intermediate strings
- C) It automatically compresses the output
- D) It changes Big-O from `O(n)` to `O(1)`

<details>
<summary>Show Answer</summary>

**B)** Joining avoids creating many temporary strings.

</details>

---

## Question 3
Which tool is the best fit for finding **which functions** a bigger program
spends its time in?

- A) `timeit`
- B) `cProfile`
- C) `tracemalloc`
- D) `id()`

<details>
<summary>Show Answer</summary>

**B)** `cProfile` reports per-function call counts and time. `timeit` is for
micro-benchmarks of single statements, and `tracemalloc` tracks memory.

</details>

---

## Question 4
What is `tracemalloc` used for?

- A) Timing how long a function takes
- B) Tracing where memory is being allocated
- C) Detecting deadlocks
- D) Caching function results

<details>
<summary>Show Answer</summary>

**B)** `tracemalloc` records allocations so you can see what uses memory.

</details>

---

## Question 5
Why does a micro-benchmark use `timeit` with several repeats instead of one
`perf_counter` measurement?

- A) `timeit` disables the GIL for faster runs
- B) A single measurement is mostly noise; repeating and taking the best/minimum shows the real cost
- C) `timeit` compiles the code to C
- D) Repeats make the code more readable

<details>
<summary>Show Answer</summary>

**B)** One-off timings are dominated by noise (OS, cache, other programs).
`timeit` runs the statement many times and supports `repeat=`, so small,
reliable comparisons are possible.

</details>

---

## Question 6
What does `functools.lru_cache` do?

- A) Limits how much memory a list may use
- B) Stores results of previous calls so repeated calls with the same arguments return instantly
- C) Runs the function in a separate thread
- D) Deletes old objects from memory

<details>
<summary>Show Answer</summary>

**B)** It is a memoization cache: same arguments in, saved result out —
great when inputs repeat, wasteful when they never do.

</details>

---

[Back to Optimization Techniques README](README.md)
