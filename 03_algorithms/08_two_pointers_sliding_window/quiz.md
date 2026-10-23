# 🧠 Two Pointers & Sliding Window Quiz

Test your understanding of the two pointers technique and the sliding window pattern!

---

## Question 1: The Core Idea

What does the two pointers technique trade for a single smart pass?

- A) Extra memory to cache every pair
- B) Nested loops (O(n^2)) become one pass with two moving indices (O(n))
- C) Sorting is always required
- D) Recursion depth

<details>
<summary>Show Answer</summary>

**B) Nested loops (O(n^2)) become one pass with two moving indices (O(n))**

The whole point: instead of checking every pair with two nested loops, each
pointer walks the data at most once, and a comparison decides where each
pointer goes next.

</details>

---

## Question 2: Why Sorted Input?

Pair-with-target-sum uses pointers at both ends. Why does it usually need a
SORTED array?

- A) Sorting makes the code shorter
- B) The comparison "sum too small / too big" can only safely discard a pointer if the values are ordered
- C) Sorted arrays use less memory
- D) It doesn't - the algorithm works the same on unsorted input

<details>
<summary>Show Answer</summary>

**B) The comparison "sum too small / too big" can only safely discard a pointer if the values are ordered**

If the sum is too small, you discard `left` only because *every other partner
for it* is even smaller (they sit before `right` in a sorted array). Without
order, discarding could throw away the only valid pair. Note: some
opposite-pointer problems like container-with-most-water have a different
decision rule and genuinely do not need sorting.

</details>

---

## Question 3: Code Analysis

```python
def mystery(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return nums
```

What does `mystery([0, 1, 0, 3, 12])` return?

- A) [0, 0, 1, 3, 12]
- B) [1, 3, 12, 0, 0]
- C) [1, 3, 12]
- D) [12, 3, 1, 0, 0]

<details>
<summary>Show Answer</summary>

**B) [1, 3, 12, 0, 0]**

This is the fast/slow "move zeros" pattern: `read` visits every slot, and every
non-zero value is swapped into the `write` slot. Non-zeros keep their order;
zeros bubble to the end.

</details>

---

## Question 4: Fixed-Size Window

The window has size k = 3 and currently sums `[4, 1, 6]`. It slides one step
right and the new element 2 enters. What must happen to keep the sum correct?

- A) Recount the whole window from scratch
- B) Subtract the element leaving on the left (4) and add the entering element (2)
- C) Subtract the entering element and add the leaving element
- D) Multiply the sum by k

<details>
<summary>Show Answer</summary>

**B) Subtract the element leaving on the left (4) and add the entering element (2)**

The slide updates: `window += nums[right] - nums[right - k]`. Here the sum goes
from 11 to 9. This O(1) update per step is what keeps the whole scan O(n)
instead of O(n * k).

</details>

---

## Question 5: The Dynamic Window Rhythm

In a dynamic sliding window (e.g. longest substring without repeating
characters), what are the three steps performed for each new `right`?

- A) Sort, search, return
- B) Count, double, merge
- C) Expand right, repair from the left while the condition is broken, record the answer
- D) Shrink left, then expand right, then reset the state

<details>
<summary>Show Answer</summary>

**C) Expand right, repair from the left while the condition is broken, record the answer**

The invariant: after the repair `while` loop finishes, the window `[left..right]`
satisfies the condition - and only then is it safe to measure it. Skipping the
repair step means the window state lies about what the window contains.

</details>

---

## Question 6: Container With Most Water

Which pointer should move after comparing the two lines?

- A) Always the left pointer
- B) Always the right pointer
- C) The pointer at the SHORTER line
- D) Both pointers at once

<details>
<summary>Show Answer</summary>

**C) The pointer at the SHORTER line**

Moving the taller side inward can never increase the area: the width shrinks
and the height is still capped by the shorter line. Moving the shorter side is
the only move that can find something better. Bonus fact: this problem works
on UNSORTED input - the decision comes from the values, not from sort order.

</details>

---

## Question 7: Common Bug

Which version of an opposite-pointers loop risks running forever?

- A) One where exactly one pointer moves every iteration
- B) One where a code path exists in which NEITHER pointer moves
- C) One where both pointers move toward each other
- D) One where the loop condition is `left < right`

<details>
<summary>Show Answer</summary>

**B) One where a code path exists in which NEITHER pointer moves**

Every iteration must move at least one pointer, or the loop spins forever.
Classic cause: an `if` with no fall-through `else` that advances a pointer,
so some comparison matches no branch. Always make sure the loop body ends
with an unconditional pointer move in the default case.

</details>

---

## Question 8: Complexity

The smallest-window algorithm has a `while` loop nested inside a `for` loop.
Why is it still O(n)?

- A) Python optimizes nested loops automatically
- B) The while loop only runs for the first character
- C) Each character enters the window once and leaves at most once, so total pointer movement is bounded by 2n
- D) It isn't - the true complexity is O(n^2)

<details>
<summary>Show Answer</summary>

**C) Each character enters the window once and leaves at most once, so total pointer movement is bounded by 2n**

This is amortized analysis: the `right` pointer advances n times, and across
the whole run the `left` pointer also advances at most n times. The nested
loop's total work is capped by total pointer movement, not by n times n.

</details>

---

## Scoring

| Score | Level |
|-------|-------|
| 8 | ⭐⭐⭐ Expert |
| 6-7 | ⭐⭐ Proficient |
| 4-5 | ⭐ Intermediate |
| 0-3 | Keep studying! |

---

## Key Takeaways

1. **Two pointers replaces nested loops** - O(n^2) becomes O(n)
2. **Opposite-direction pointers usually need sorted input** - order justifies discarding a side
3. **Fast/slow pointers rewrite arrays in place** - read scans, write keeps
4. **Fixed windows slide** - add the entering element, subtract the leaving one
5. **Dynamic windows stretch** - expand, repair, record
6. **Every loop iteration must move a pointer** - or you built an infinite loop

---

[Back to Two Pointers README](README.md) | [Return to Module Overview](../README.md)
