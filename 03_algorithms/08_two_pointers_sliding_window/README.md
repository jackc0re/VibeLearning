# 👉 Two Pointers & Sliding Window

> Replace nested loops with one smart pass - two indices that know where to go

---

## 📋 Table of Contents

1. [The Core Idea](#the-core-idea)
2. [Family 1: Opposite-Direction Pointers](#family-1-opposite-direction-pointers)
3. [Family 2: Same-Direction Fast/Slow Pointers](#family-2-same-direction-fastslow-pointers)
4. [Family 3: Fixed-Size Sliding Window](#family-3-fixed-size-sliding-window)
5. [Family 4: Dynamic Sliding Window](#family-4-dynamic-sliding-window)
6. [When Does Two Pointers Apply?](#when-does-two-pointers-apply)
7. [Common Mistakes](#common-mistakes)
8. [Quick Reference](#quick-reference)

---

## The Core Idea

Imagine a very long hallway of numbered lockers. You need two lockers whose
contents add up to exactly 18. The brute-force approach checks **every pair** -
like walking every possible route between two lockers. For `n` lockers, that is
roughly `n * n / 2` comparisons.

The two pointers approach is smarter: stand one friend at the **left end** of
the hallway and one at the **right end**, then slide them toward each other.
After every look, the *comparison itself* tells you which friend must move.
Each friend walks the hallway at most once, so the whole search is **O(n)**.

```python
# Brute force: O(n^2) - every pair
def pair_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

# Two pointers: O(n) - one pass, two indices
def pair_sum_two_pointers(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return (left, right)
        if current < target:
            left += 1    # sum too small -> need a bigger left value
        else:
            right -= 1   # sum too big -> need a smaller right value
    return None
```

This topic is a **pattern catalog**, not a single algorithm. Every pattern below
is a member of one of four families. Learn to recognize the family, and the code
almost writes itself.

---

## Family 1: Opposite-Direction Pointers

**Signature:** one pointer starts at each end, both move toward the middle.
**Usually requires SORTED input** - the sorted order is what lets a comparison
decide which pointer to move.

> Analogy: two friends searching a bookshelf for two books that cost exactly
> $18. The books are sorted by price. If the cheapest + most expensive is too
> cheap, no book can replace the cheapest to help - so move the cheap side in.

### ✅ Pair With Target Sum (sorted input)

```python
def pair_with_target_sum(nums, target):
    """
    Return indices of two numbers that add to target.
    nums must be SORTED ascending.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return (left, right)
        if current < target:
            left += 1
        else:
            right -= 1
    return None

print(pair_with_target_sum([2, 5, 9, 13, 15], 18))  # (1, 3) -> 5 + 13
```

**Why it works:** if the sum is too small, `nums[left]` can never be part of a
solution with anything at or before `right` - every partner is even smaller.
So `left` is safe to discard. Symmetric logic for "too big".

### ✅ Valid Palindrome

```python
def is_palindrome(text):
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("honor"))    # False (h != r)
```

### ✅ Reverse a String In Place

```python
def reverse_in_place(chars):
    """Reverse a list of characters without a second list."""
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return chars

print(reverse_in_place(list("hello")))  # ['o', 'l', 'l', 'e', 'h']
```

### ✅ Remove Duplicates From a Sorted Array

Keep one copy of each value, in place, and return the new length.

```python
def remove_duplicates_sorted(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write

nums = [1, 1, 2, 3, 3]
length = remove_duplicates_sorted(nums)
print(length, nums[:length])  # 3 [1, 2, 3]
```

> ⚠️ **Heads-up - this one is a hybrid.** Both pointers travel left to right:
> the `read` pointer races ahead while the `write` pointer trails behind. The
> sorted order still does the heavy lifting (duplicates sit next to each
> other), which is why it lives in the sorted-input family - and it is the
> perfect bridge into Family 2.

### ✅ Container With Most Water (works on UNSORTED input!)

Find two lines that, together with the x-axis, hold the most water:

```python
def container_with_most_water(heights):
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        best = max(best, width * height)
        # Move the SHORTER side inward - the taller side is the bottleneck's partner
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best

print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
```

**Why it works:** moving the *taller* side inward can only shrink the area
(width shrinks, height is capped by the shorter side anyway). Moving the
*shorter* side is the only move that can find a bigger area. Notice this does
**not** need sorted input - the "which pointer moves" decision comes from the
values themselves, not from sort order.

### Family 1 Template

```python
def opposite_pointers(items):
    left, right = 0, len(items) - 1
    while left < right:
        # 1. Look at the pair (items[left], items[right])
        # 2. If it solves/updates the answer, record it
        # 3. Compare and move exactly ONE pointer:
        #    - pair too small -> left += 1
        #    - pair too big   -> right -= 1
        ...
    return ...
```

---

## Family 2: Same-Direction Fast/Slow Pointers

**Signature:** both pointers start at the left and move left to right. The
**read** (fast) pointer visits every element; the **write** (slow) pointer only
moves when it sees something worth keeping.

> Analogy: sorting mail on a conveyor belt. Your eyes (read pointer) look at
> every letter; your hand (write pointer) only moves when you place a letter
> into the keep pile. Everything before your hand is final.

### ✅ Move Zeros to the End

```python
def move_zeros(nums):
    """Move all zeros to the end, in place, keeping the order of the rest."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return nums

print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
```

### ✅ Squash Duplicates (sorted input)

Keep the first copy of each run of equal values:

```python
def squash_duplicates(nums):
    """Remove duplicates in place from a sorted list. Return new length."""
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```

This is Family 1's remove-duplicates seen through the fast/slow lens - same
walk, different name. The fast/slow framing is what unlocks the *unsorted*
cases below.

### ✅ Partition-Style Removal (remove all occurrences of a value)

```python
def remove_all_occurrences(nums, value):
    """Remove every `value` in place. Return the new length."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != value:
            nums[write] = nums[read]
            write += 1
    return write

nums = [3, 2, 2, 3]
length = remove_all_occurrences(nums, 3)
print(length, nums[:length])  # 2 [2, 2]
```

### Family 2 Template

```python
def fast_slow_rewrite(items):
    write = 0
    for read in range(len(items)):
        if should_keep(items[read]):     # <-- the only part that changes
            items[write] = items[read]   # (or swap, to preserve order)
            write += 1
    return write  # everything from write on is disposable
```

---

## Family 3: Fixed-Size Sliding Window

**Signature:** "for every `k` consecutive elements..." - the window has a
constant size, and it slides one step at a time: **add on the right, remove on
the left**.

> Analogy: a train of exactly `k` carriages passing a tunnel. When one
> carriage enters on the right, one leaves on the left. To know the total
> passengers, you don't recount the whole train - you just add who entered and
> subtract who left.

```python
def max_window_sum(nums, k):
    """Maximum sum of any k consecutive elements. O(n)."""
    if k <= 0 or k > len(nums):
        return None
    window = sum(nums[:k])          # first window, counted once
    best = window
    for right in range(k, len(nums)):
        window += nums[right]       # new element enters on the right...
        window -= nums[right - k]   # ...old element leaves on the left
        best = max(best, window)
    return best

print(max_window_sum([2, 1, 5, 1, 3, 2], 3))  # 9 -> window [1, 3, 2]
```

Watch the running sum slide (k = 3):

```
[2, 1, 5] 1 3 2   sum = 8        (counted fresh)
 2 [1, 5, 1] 3 2  sum = 8 + 1 - 2 = 7
 2  1 [5, 1, 3] 2 sum = 7 + 3 - 1 = 9   <- new best
 2  1  5 [1, 3, 2] sum = 9 + 2 - 5 = 6
```

Recounting each window would be O(n * k); sliding keeps it **O(n)** no matter
how big `k` is. The same skeleton computes averages:

```python
def window_averages(nums, k):
    """Average of every k consecutive elements, as a list."""
    if k <= 0 or k > len(nums):
        return []
    averages = []
    window = sum(nums[:k])
    averages.append(window / k)
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        averages.append(window / k)
    return averages

print(window_averages([2, 1, 5, 1, 3, 2], 3))  # [2.67, 2.33, 3.0, 2.0]
```

### Family 3 Template

```python
def fixed_window(items, k):
    window = compute(items[:k])          # build the first window once
    answer = window
    for right in range(k, len(items)):
        window = update(window,          # enter: items[right]
                        items[right - k])  # leave: items[right - k]
        answer = best(answer, window)
    return answer
```

---

## Family 4: Dynamic Sliding Window

**Signature:** "longest / shortest substring or subarray such that *some
condition* holds." The window **grows on the right** to explore, and **shrinks
from the left** only when the condition breaks - like a stretchy rubber band.

The universal rhythm:

1. **Expand**: pull in `items[right]`, update the window's state.
2. **Repair**: while the state violates the condition, push out `items[left]`.
3. **Record**: the window `[left..right]` is now valid - update the answer.

### ✅ Longest Substring Without Repeating Characters

You may have already solved this in the sets topic of module 02
([that exercise](../../02_data_structures/04_sets/exercises.py)) - possibly
without giving the technique its name. Here it is again, wearing its real hat:

```python
def longest_unique_substring(s):
    """Return (length, substring) of the longest run with no repeated char."""
    seen = set()
    left = 0
    best_len, best_start = 0, 0
    for right, char in enumerate(s):
        while char in seen:          # condition broken -> repair
            seen.remove(s[left])
            left += 1
        seen.add(char)               # expand
        if right - left + 1 > best_len:
            best_len, best_start = right - left + 1, left
    return best_len, s[best_start:best_start + best_len]

print(longest_unique_substring("abcabcbb"))  # (3, 'abc')
print(longest_unique_substring("pwwkew"))    # (3, 'kew')
```

### ✅ Longest Substring With At Most K Distinct Characters

Same rhythm, but the window state is a count map instead of a set:

```python
def longest_substring_k_distinct(s, k):
    if k == 0:
        return 0
    counts = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1      # expand
        while len(counts) > k:                      # too many distinct -> repair
            left_char = s[left]
            counts[left_char] -= 1
            if counts[left_char] == 0:
                del counts[left_char]
            left += 1
        best = max(best, right - left + 1)
    return best

print(longest_substring_k_distinct("eceba", 2))   # 3 -> "ece"
print(longest_substring_k_distinct("araaci", 2))  # 4 -> "araa"
```

### ✅ Smallest Window Containing a Target Substring (the classic hard one)

Find the **shortest** substring of `s` that contains every character of `t`
(with multiplicity). For `s = "ADOBECODEBANC"`, `t = "ABC"` the answer is
`"BANC"`.

The trick that makes it O(n): track `missing` (how many required characters we
still lack) and a `need` map of counts. Expanding with a needed character
decrements `missing`; when `missing == 0` the window is complete, and we shrink
as far as it survives - recording the best along the way.

```python
def min_window_substring(s, t):
    if not t or not s or len(t) > len(s):
        return ""
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)
    left = 0
    best_start, best_len = 0, len(s) + 1

    for right, ch in enumerate(s):
        # EXPAND
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1
        # REPAIR (shrink while the window is still complete)
        while missing == 0:
            if right - left + 1 < best_len:
                best_start, best_len = left, right - left + 1
            left_ch = s[left]
            need[left_ch] += 1
            if need[left_ch] > 0:   # we just pushed out a REQUIRED char
                missing += 1
            left += 1

    return "" if best_len > len(s) else s[best_start:best_start + best_len]

print(min_window_substring("ADOBECODEBANC", "ABC"))  # "BANC"
```

**Careful worked trace** - `s = "ADOBECODEBANC"`, `t = "ABC"`.
Start: `need = {A:1, B:1, C:1}`, `missing = 3`, `left = 0`.

| Step | right | char | What happens | missing | Best window so far |
|------|-------|------|--------------|---------|--------------------|
| 1 | 0 | A | needed - counts toward A | 3 -> 2 | - |
| 2 | 1 | D | surplus (goes negative in `need`) | 2 | - |
| 3 | 2 | O | surplus | 2 | - |
| 4 | 3 | B | needed | 2 -> 1 | - |
| 5 | 4 | E | surplus | 1 | - |
| 6 | 5 | C | needed - window complete! | 1 -> 0 | **ADOBEC (6)** |
| 7 | - | - | shrink: pop `A` -> A becomes required again | 0 -> 1 | ADOBEC |
| 8 | 6-8 | O, D, E | surplus - nothing completes | 1 | ADOBEC |
| 9 | 9 | B | surplus (B already inside window) | 1 | ADOBEC |
| 10 | 10 | A | needed - complete again | 1 -> 0 | ADOBEC (6) |
| 11 | - | - | shrink: pop D, O, B, E (all surplus), then pop `C` -> broken | 0 -> 1 | ADOBEC |
| 12 | 11 | N | surplus | 1 | ADOBEC |
| 13 | 12 | C | needed - complete | 1 -> 0 | ADOBEC (6) |
| 14 | - | - | shrink: pop `O` -> ODEBANC (6); pop `D` -> EBANC (5, new best); pop `E` -> **BANC (4, new best)**; pop `B` -> broken | 0 -> 1 | **BANC (4)** |

Right pointer reached the end. Answer: `s[9:13]` = **"BANC"**, length 4.

Notice every character entered the window once and left at most once - that is
why the nested `while` loop is still **O(n)** overall.

### Family 4 Template

```python
def dynamic_window(items):
    state = initial_state()          # set, count map, running total...
    left = 0
    best = nothing_yet
    for right, item in enumerate(items):
        add_to_state(state, item)              # 1. EXPAND
        while state_violates(state):           # 2. REPAIR
            remove_from_state(state, items[left])
            left += 1
        best = better_of(best, measure(right - left + 1))  # 3. RECORD
    return best
```

---

## When Does Two Pointers Apply?

Reach for this pattern when you see these signals:

1. **A sorted array plus a pair/target condition** - "find two numbers that
   sum to X", "does this array have a pair with difference D". Family 1.
2. **In-place array rewriting** - "move zeros", "remove duplicates",
   "remove all occurrences of a value" with O(1) extra space. Family 2.
3. **Contiguous subarray / substring questions** - the word *contiguous* is
   the giveaway. "Longest substring with...", "max sum of k consecutive...",
   "smallest window containing...". Families 3 and 4.

And when **not** to: if the answer needs non-contiguous combinations, or the
condition cannot be repaired by shrinking from the left (e.g. "subsequence"),
two pointers will give wrong answers confidently. That is a job for dynamic
programming (see [04_dynamic_programming](../04_dynamic_programming/README.md)).

---

## Common Mistakes

### ❌ Moving the wrong pointer first

In pair-with-target-sum, moving the pointer on the *larger* value when the sum
is too small walks you away from the answer. The comparison must always evict
the side that **cannot** be part of any solution:

```python
if current < target:
    left += 1    # too small -> discard the SMALL side, never the big one
else:
    right -= 1
```

For container-with-most-water, the rule is "move the shorter side" - moving the
taller one can never help, because the shorter side caps the area either way.

### ❌ Forgetting to shrink before (or after) expanding

In a dynamic window, if you expand without repairing when the condition breaks,
your state (`seen`, `counts`) silently lies about the window. The repair
`while` loop is not optional decoration - it is what restores the invariant
before you measure the window.

### ❌ Infinite loops when both pointers stall

```python
while left < right:
    if nums[left] + nums[right] == target:
        return (left, right)
    # BUG: neither pointer moved when nothing matched
```

Every loop iteration must move at least one pointer. If your logic can hit a
case where neither branch fires, the loop spins forever. When in doubt, make
the final line of the loop body an unconditional `left += 1` or `right -= 1`
for the fall-through case.

### ❌ Assuming the array must be sorted when it must NOT be

Two pointers on sorted input *uses* order to decide which pointer moves - that
is family 1's pair-sum. But container-with-most-water works on **unsorted**
input, and families 2-4 never sort anything. Sorting first is not free
(O(n log n)) and can destroy information you needed, like original indices in
an "unsorted pair sum" problem. Ask: *does my pointer-moving rule actually
depend on sorted order?*

---

## Quick Reference

| Family | Signal in the problem | Template | Time |
|--------|----------------------|----------|------|
| Opposite-direction pointers | Sorted array + pair/target condition; palindrome check | Move `left`/`right` toward each other, one comparison decides which | O(n) (O(n log n) if sorting first) |
| Same-direction fast/slow | Rewrite an array in place: move, squash, partition | `read` visits everything, `write` keeps survivors | O(n) |
| Fixed-size window | "every k consecutive elements" | `window += items[right] - items[right - k]` | O(n) |
| Dynamic window | "longest/shortest substring with a condition" | Expand right, repair from left while violated, record | O(n) amortized |

---

## 🔑 Key Takeaways

1. **Two pointers trades nested loops for one pass** - O(n^2) becomes O(n)
2. **Family 1** moves pointers toward each other; sorted order usually decides who moves
3. **Family 2** is in-place rewriting: read fast, write slow
4. **Family 3** slides a fixed window: add right, remove left - never recount
5. **Family 4** stretches a window: expand, repair, record
6. Every iteration must move a pointer, or you have built an infinite loop

---

## 🔗 Next Steps

- Practice with [`exercises.py`](exercises.py)
- Test your knowledge with [`quiz.md`](quiz.md)
- Return to [Module Overview](../README.md)
