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

[Back to Optimization Techniques README](README.md)

