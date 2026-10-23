# 🧩 Algorithm Problems: A Self-Contained Practice Set

> Every problem statement is right here on the page - no external site needed.
> Read the problem, name the pattern, then code it in a plain `.py` file.

---

## How This Page Works

Interview algorithm questions are less about knowing 500 problems and more about
recognizing **patterns**. When you hear "sorted array", "top k", or "all possible
combinations", the pattern is already whispering its name.

Each section below covers one pattern:

- 📖 A link to the topic on this site that **teaches** the pattern first
- 2–4 **self-contained problems** - the full statement is on this page
- A **pattern signal** - what in the problem statement tells you it belongs here
- A **hint** hidden in a collapsible block (try without it first!)
- The **target complexity** a correct solution should hit

Before you start, brush up on:

- [Algorithms cheatsheet](../cheatsheets/algorithms.md) - Big O and sorting syntax at a glance
- [Big O Notation](../../11_memory_performance/05_big_o_notation/README.md) - how to *count* the work your solution does

Pair this page with [system_design_basics.md](system_design_basics.md) when you are
ready for the "how would this run at scale?" style of interview.

---

## 👉 Two Pointers & Sliding Window

📖 **Learn the pattern first:** [Two Pointers & Sliding Window](../../03_algorithms/08_two_pointers_sliding_window/README.md)

### Problem 1: Pair With Target Sum

**Statement.** Given a **sorted** list of integers `nums` and a `target`, return the
indices `(i, j)` with `i < j` such that `nums[i] + nums[j] == target`. If no such
pair exists, return `None`.

Example: `nums = [1, 3, 5, 8, 13]`, `target = 13` → `(2, 3)` because `5 + 8 == 13`.

**Pattern signal.** The input is *sorted* and you are hunting for a *pair*. Sorted
order means a comparison can tell you which end to move - the signature of
opposite-direction two pointers.

<details>
<summary>Click for hint</summary>

Start one pointer at index `0` and one at the last index. If the sum is too small,
only moving the left pointer up can help; if it is too big, move the right pointer
down. Each pointer only ever moves inward, so the loop ends after at most `n` steps.

</details>

**Target complexity:** O(n) time, O(1) extra space.

### Problem 2: Valid Palindrome

**Statement.** Given a string `text`, return `True` if it reads the same forwards
and backwards, using **two indices** and no slicing (`text[::-1]` is cheating today).
For an extra star, ignore characters that are not letters or digits.

Example: `"racecar"` → `True`, `"race a car"` → `False` (with the extra rule).

**Pattern signal.** You are comparing the *first* character with the *last*, then
walking inward. Two ends moving toward each other is two pointers even without a
sum in sight.

<details>
<summary>Click for hint</summary>

Keep `left` and `right` indices. While `left < right`, if the characters differ,
return `False` immediately; otherwise `left += 1` and `right -= 1`. If the loop
finishes, the string is a palindrome.

</details>

**Target complexity:** O(n) time, O(1) extra space.

### Problem 3: Longest Substring Without Repeating Characters

**Statement.** Given a string, return the length of the longest run of consecutive
characters that contains **no repeated character**.

Example: `"abcabcbb"` → `3` (`"abc"`), `"bbbbb"` → `1`, `"pwwkew"` → `3` (`"wke"`).

**Pattern signal.** "Longest ... substring" (a *contiguous* chunk) with a rule that
the chunk must keep satisfying - that is a sliding window: grow the right edge,
shrink the left edge when the rule breaks.

<details>
<summary>Click for hint</summary>

Keep a `set` of the characters currently inside the window. Move `right` forward,
adding each character. If the new character is already in the set, remove characters
from the `left` side until the duplicate is gone. Track the best
(`right - left + 1`) you ever saw.

</details>

**Target complexity:** O(n) time - each character enters and leaves the window at
most once - and O(min(n, alphabet)) space.

---

## #️⃣ Hashing

📖 **Learn the pattern first:** [Hash Tables](../../02_data_structures/10_hash_tables/README.md)

### Problem 1: Two Sum (Unsorted)

**Statement.** Given an **unsorted** list of integers `nums` and a `target`, return
the indices of the two numbers that add up to `target`. Exactly one answer exists.

Example: `nums = [2, 7, 11, 15]`, `target = 9` → `(0, 1)`.

**Pattern signal.** You keep asking "have I already seen the number that completes
me?" - a question dictionaries answer in O(1). Any "have I seen X before?" problem
is a hash table problem.

<details>
<summary>Click for hint</summary>

Walk the list once. For each number, compute `complement = target - num` and check
whether the complement is already a key in your dictionary. If not, store
`num -> index` and keep going.

</details>

**Target complexity:** O(n) time, O(n) space.

### Problem 2: First Non-Repeating Character

**Statement.** Given a string, return the first character that appears exactly
once, or `None` if every character repeats.

Example: `"swiss"` → `"w"`, `"aabb"` → `None`.

**Pattern signal.** Counts + "first one in order" = two passes with a dictionary:
one pass to count, one pass to scan in order.

<details>
<summary>Click for hint</summary>

Pass 1: build `counts = {}` mapping each character to how many times it appears.
Pass 2: walk the string from the start and return the first character whose count
is `1`. Because dictionaries remember insertion order in Python 3.7+, you could
even scan the dictionary keys - but scanning the string is clearer.

</details>

**Target complexity:** O(n) time, O(k) space where k is the number of distinct
characters.

### Problem 3: Group Anagrams

**Statement.** Given a list of words, group the words that are anagrams of each
other (same letters, different order). Return a list of groups.

Example: `["eat", "tea", "tan", "ate", "nat", "bat"]` →
`[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]` (groups in any order).

**Pattern signal.** "Group things that share a hidden identity" asks for a
dictionary whose **key is a canonical form** of each item - something equal for all
members of a group and unique across groups.

<details>
<summary>Click for hint</summary>

Two words are anagrams exactly when their **sorted letters** are equal:
`"".join(sorted(word))` maps `"eat"`, `"tea"`, `"ate"` all to `"aet"`. Use that
string as the dictionary key and append words to the list stored under it. You can
also use a 26-slot letter count tuple as the key to avoid sorting.

</details>

**Target complexity:** O(n · k log k) time for n words of length k, O(n · k) space.

---

## ⛰️ Heaps & Priority Queues

📖 **Learn the pattern first:** [Heaps & Priority Queues](../../02_data_structures/11_heaps_priority_queues/README.md)

### Problem 1: K Largest Elements

**Statement.** Given a list of numbers and an integer `k`, return the `k` largest
values in descending order.

Example: `nums = [3, 1, 7, 5, 9, 2]`, `k = 3` → `[9, 7, 5]`.

**Pattern signal.** Anytime you see "**top k**", "**k largest/smallest**", or
"most frequent k" - and the list is too big to comfortably sort - reach for a heap
of size k instead of a full sort.

<details>
<summary>Click for hint</summary>

Keep a **min-heap** containing at most k numbers. Push each number; when the heap
grows past k, pop the smallest - it can no longer be among the k largest. At the
end the heap holds exactly the k winners. (`heapq.nlargest(k, nums)` does this
for you, but write it by hand once.)

</details>

**Target complexity:** O(n log k) time, O(k) space.

### Problem 2: Merge K Sorted Lists

**Statement.** You are given `k` lists, each already sorted ascending. Merge them
into one sorted list containing all their elements.

Example: `[[1, 4, 7], [2, 5], [0, 9]]` → `[0, 1, 2, 4, 5, 7, 9]`.

**Pattern signal.** You must repeatedly ask "which list has the next smallest
element?" across k candidates - a priority queue is precisely the machine for
"smallest so far" questions.

<details>
<summary>Click for hint</summary>

Put the first element of every list into a min-heap as a tuple
`(value, list_index, element_index)` - the extra indices break ties and tell you
where the *next* element of that list lives. Pop the smallest, append it to the
result, and push that list's next element. (`heapq` needs the tuples to be
comparable, which is why the index is included.)

</details>

**Target complexity:** O(N log k) time for N total elements and k lists,
O(k) space for the heap.

### Problem 3: Top K Frequent Elements

**Statement.** Given a list and an integer `k`, return the `k` values that occur
most often, in any order.

Example: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2` → `[1, 2]`.

**Pattern signal.** "K most ..." is the two-pattern combo: count first (hashing),
then select the top k (heap).

<details>
<summary>Click for hint</summary>

Build `counts` with a dictionary, then push `(frequency, value)` pairs into a
min-heap of size k exactly like Problem 1 - popping the *least* frequent whenever
the heap overflows.

</details>

**Target complexity:** O(n log k) time for the heap phase (plus O(n) counting),
O(n) space for the counts.

---

## 🌲 Tries

📖 **Learn the pattern first:** [Tries](../../02_data_structures/12_tries/README.md)

### Problem 1: Implement a Prefix Tree

**Statement.** Build a trie supporting three operations:

- `insert(word)` - store a word (lowercase letters only)
- `search(word)` - `True` only if the *complete* word was inserted
- `starts_with(prefix)` - `True` if any inserted word starts with `prefix`

Example: after `insert("cat")` and `insert("car")`: `search("cat")` → `True`,
`search("ca")` → `False`, `starts_with("ca")` → `True`.

**Pattern signal.** Lots of words + questions about **shared prefixes** - a trie
stores the prefix once and answers prefix questions by walking letters.

<details>
<summary>Click for hint</summary>

Each node is an object with `children = {}` (letter → child node) and an
`is_word` flag. To insert, walk letter by letter creating missing children with
`dict.setdefault`; at the end set `is_word = True`. `search` and `starts_with`
walk the same way - `search` additionally requires the final node to be a word.

</details>

**Target complexity:** O(L) time per operation, where L is the word or prefix
length.

### Problem 2: Autocomplete

**Statement.** Given a list of dictionary words, support a query
`suggestions(prefix)` that returns **all** stored words beginning with `prefix`.

Example: words `["car", "cat", "dog"]`, prefix `"ca"` → `["car", "cat"]`.

**Pattern signal.** It is Problem 1 plus one walk: find the prefix's node, then
collect every word underneath it. If your data were a flat list you would scan all
n words per query; the trie touches only the matching branch.

<details>
<summary>Click for hint</summary>

Walk to the node where the prefix ends (return `[]` if you fall off the tree).
Then explore every branch from that node, building up the word as you go; whenever
you reach a node with `is_word == True`, record the word. Any tree traversal
order works.

</details>

**Target complexity:** O(P + M) per query, where P is the prefix length and M is
the total length of the matched words.

---

## 🔙 Backtracking

📖 **Learn the pattern first:** [Backtracking](../../03_algorithms/09_backtracking/README.md)

### Problem 1: All Subsets (Power Set)

**Statement.** Given a list of **distinct** numbers, return every possible subset
(including the empty one). Order of subsets does not matter.

Example: `[1, 2, 3]` → `[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]`
(any order of the 8 subsets is fine).

**Pattern signal.** "**All** possible ..." with no shortcut - each element is a
yes/no *choice*, and choices build on earlier choices. That is backtracking: choose,
explore, un-choose.

<details>
<summary>Click for hint</summary>

Keep a `path` list of the choices made so far. At each call, record a **copy** of
`path` (it is a valid subset already!), then for each remaining index: append the
element, recurse with the next index, then `path.pop()` to undo. The recursion
index `start` stops you from reusing elements or making `[2, 1]` after `[1, 2]`.

</details>

**Target complexity:** O(n · 2ⁿ) time - there are 2ⁿ subsets and copying one costs
up to O(n). Exponential is *correct* here: the answer itself is that big.

### Problem 2: Permutations

**Statement.** Given a list of distinct numbers, return every ordering of them.

Example: `[1, 2, 3]` → `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2],
[3, 2, 1]]` (any order of the 6 permutations is fine).

**Pattern signal.** "**All** arrangements" - at every step you choose which unused
element comes next, then undo the choice. Same choose/explore/un-choose loop, but
every element is a candidate at every position.

<details>
<summary>Click for hint</summary>

Track the unused elements (a `set`, or an `index` into the list that you swap
around). For each unused element: append it to `path`, recurse, pop it back off.
Record a copy of `path` when its length equals the input length.

</details>

**Target complexity:** O(n · n!) time - n! permutations, each copied in O(n).

### Problem 3: Combination Sum

**Statement.** Given a list of **distinct** positive integers `candidates` (each
usable an unlimited number of times) and a `target`, return all combinations that
sum to `target`. Combinations that differ only in order count once.

Example: `candidates = [2, 3, 6, 7]`, `target = 7` → `[[2, 2, 3], [7]]`.

**Pattern signal.** "**All** combinations reaching a goal" - choices, but with a
built-in reason to give up early: once the running sum passes the target, that
whole branch is dead. Pruning dead branches is backtracking's superpower.

<details>
<summary>Click for hint</summary>

Recurse with `(start, remaining)`. For each `candidates[i]` from `start` onward:
if it exceeds `remaining`, skip; otherwise append it and recurse with
`(i, remaining - candidates[i])` - reusing `i` (not `i + 1`) is what allows
repeats like `[2, 2, 3]`. When `remaining == 0`, record a copy of the path. Always
pop on the way back up.

</details>

**Target complexity:** exponential in the worst case - roughly
O(k^(target/min(candidates))) for k candidates - because the output can itself be
exponentially large. Say that out loud in an interview; it shows you know the cost
belongs to the answer, not the algorithm.

---

## 📈 Dynamic Programming

📖 **Learn the pattern first:** [Dynamic Programming](../../03_algorithms/04_dynamic_programming/README.md)

### Problem 1: Climbing Stairs

**Statement.** You are climbing a staircase with `n` steps and can take either
1 or 2 steps at a time. How many **distinct ways** are there to reach the top?

Example: `n = 3` → `3` (1+1+1, 1+2, 2+1).

**Pattern signal.** A counting question whose answer for `n` is built from answers
for smaller inputs (the last move was a 1-step or a 2-step). Overlapping
subproblems + optimal substructure = DP.

<details>
<summary>Click for hint</summary>

`ways(n) = ways(n - 1) + ways(n - 2)` - it is Fibonacci in disguise. Base cases:
`ways(1) = 1`, `ways(2) = 2`. Fill upward with two variables and you never need
an array.

</details>

**Target complexity:** O(n) time, O(1) space.

### Problem 2: House Robber

**Statement.** Given a list of non-negative integers representing money in a row
of houses, return the maximum you can rob if you **cannot rob two adjacent houses**.

Example: `[2, 7, 9, 3, 1]` → `12` (rob houses with 2, 9, and 1).

**Pattern signal.** "Maximum ... subject to a constraint between **neighbors**" -
the best answer up to house `i` depends only on the best answers up to `i - 1`
and `i - 2`. That sliding dependence is a DP table of width 2.

<details>
<summary>Click for hint</summary>

For each house: `best = max(prev_best, prev_prev_best + money)`. You either skip
this house (keep `prev_best`) or rob it (add its money to `prev_prev_best`).
Carry just two variables through the loop.

</details>

**Target complexity:** O(n) time, O(1) space.

### Problem 3: Coin Change (Fewest Coins)

**Statement.** Given coin denominations (unlimited supply of each) and an amount,
return the **minimum number of coins** that makes the amount exactly, or `-1` if
it is impossible.

Example: `coins = [1, 2, 5]`, `amount = 11` → `3` (5 + 5 + 1);
`coins = [2]`, `amount = 3` → `-1`.

**Pattern signal.** "Minimum count to reach a total" with reusable pieces - greedy
(pick the biggest coin) *fails* here (try `coins = [1, 3, 4]`, `amount = 6`), which
is your clue that DP is required.

<details>
<summary>Click for hint</summary>

Build an array `best[0..amount]` where `best[a]` = fewest coins for amount `a`.
Start with `best[0] = 0` and "infinity" elsewhere. For each amount `a` from 1 to
`amount`, try every coin `c` that fits: `best[a] = min(best[a], best[a - c] + 1)`.

</details>

**Target complexity:** O(amount · len(coins)) time, O(amount) space.

---

## 🕸️ Graphs

📖 **Learn the pattern first:** [Graph Algorithms](../../03_algorithms/07_graph_algorithms/README.md)

### Problem 1: Number of Islands

**Statement.** You are given a 2D grid of `1`s (land) and `0`s (water). An island
is a group of `1`s connected **horizontally or vertically** (not diagonally).
Return the number of islands.

Example:

```
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
→ `3` islands.

**Pattern signal.** A grid where you must visit connected cells and count/label
groups - the grid *is* a graph (each cell is a node, neighbors are edges), and
"count the groups" is connected components.

<details>
<summary>Click for hint</summary>

Scan every cell. When you find a `'1'`, increment the island count and flood-fill
its whole island with DFS or BFS, marking visited cells (e.g. set them to `'0'`)
so you never count them again. Four recursive/nbhd directions: up, down, left,
right - watch the grid borders.

</details>

**Target complexity:** O(rows × cols) time - each cell is visited a constant number
of times - and O(rows × cols) space worst case for the recursion/queue.

### Problem 2: Course Schedule

**Statement.** You must take `num_courses` courses labeled `0` to
`num_courses - 1`. You are given a list of `[a, b]` pairs meaning you must take
`b` before `a`. Return `True` if **all** courses can be finished, else `False`.

Example: `num_courses = 2`, `prerequisites = [[1, 0]]` → `True`;
`prerequisites = [[1, 0], [0, 1]]` → `False` (a deadlock).

**Pattern signal.** Prerequisites form a **directed** graph; "can I finish
everything?" is "does this graph contain a **cycle**?" - detectable with DFS colors
or Kahn's algorithm.

<details>
<summary>Click for hint</summary>

Build an adjacency list from the pairs and track three states per node:
unvisited, in-progress (on the current DFS path), done. If DFS ever reaches an
in-progress node, there is a cycle → `False`. Alternatively, repeatedly remove
nodes with no remaining prerequisites (topological sort); if some nodes never get
removed, they are in a cycle.

</details>

**Target complexity:** O(V + E) time and space for V courses and E prerequisite
pairs.

### Problem 3: Shortest Path in a Grid

**Statement.** Given a grid of `0`s (open) and `1`s (walls), return the **fewest
number of moves** from the top-left cell to the bottom-right cell, moving up,
down, left, or right. Return `-1` if there is no path. (You start and end on open
cells.)

Example:

```
0 0 1
1 0 1
1 0 0
```
→ `4` (right, down, down, right).

**Pattern signal.** "**Fewest moves**" on an unweighted graph - breadth-first
search explores distance layer by layer, so the *first* time BFS reaches the goal
is guaranteed to be via a shortest path.

<details>
<summary>Click for hint</summary>

Use a `collections.deque` holding `(row, col, distance)` starting with
`(0, 0, 0)`. Pop from the left, and for each of the 4 neighbors that is in bounds,
open (`0`), and **not yet visited**, mark it visited and enqueue it with
`distance + 1`. Mark visited *when enqueueing*, not when popping, or one cell may
enter the queue many times.

</details>

**Target complexity:** O(rows × cols) time and space.

---

## 🔍 Searching & Sorting

📖 **Learn the pattern first:** [Searching](../../03_algorithms/01_searching/README.md)
and [Sorting](../../03_algorithms/02_sorting/README.md)

### Problem 1: Classic Binary Search

**Statement.** Given a **sorted** list and a `target`, return the index of
`target`, or `-1` if absent. Write it from memory - no `list.index()`, no `bisect`.

Example: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9` → `4`; `target = 2` → `-1`.

**Pattern signal.** "**Sorted**" + "find one thing" = throw away half the data per
step. If a problem *sorts first* and then answers many queries, every query can be
a binary search too.

<details>
<summary>Click for hint</summary>

Keep `lo = 0`, `hi = len(nums) - 1`. While `lo <= hi`, compute
`mid = (lo + hi) // 2`. If `nums[mid] == target`, done; if too small,
`lo = mid + 1`; if too big, `hi = mid - 1`. The classic bugs are `lo < hi` instead
of `lo <= hi`, and forgetting the `+ 1` / `- 1` (infinite loop).

</details>

**Target complexity:** O(log n) time, O(1) space.

### Problem 2: Search in a Rotated Sorted Array

**Statement.** A sorted list was rotated at some pivot - e.g.
`[0, 1, 2, 4, 5, 6, 7]` became `[4, 5, 6, 7, 0, 1, 2]`. Given the rotated list
(all values distinct) and a `target`, return its index or `-1` - in
**O(log n)**.

Example: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0` → `4`.

**Pattern signal.** You still have "sorted-ness" - just sliced into two sorted
pieces. The trick is finding which half is *fully* sorted and testing whether the
target lives in it.

<details>
<summary>Click for hint</summary>

Binary search as usual, but at each `mid`, one of `[lo..mid]` and `[mid..hi]` is
properly sorted (check which end value is smaller). If the target falls inside the
sorted half's value range, search there; otherwise search the other half.

</details>

**Target complexity:** O(log n) time, O(1) space.

### Problem 3: Merge Intervals

**Statement.** Given a list of intervals `[start, end]`, merge all overlapping
intervals and return the result sorted by start.

Example: `[[1, 3], [2, 6], [8, 10], [15, 18]]` → `[[1, 6], [8, 10], [15, 18]]`
(because `[1, 3]` and `[2, 6]` overlap).

**Pattern signal.** Intervals + overlap questions become easy once the intervals
are **sorted by start**: then each interval only needs to be compared with the
most recent merged one. Sort first, sweep second - a tiny subset of
"sweep line" thinking.

<details>
<summary>Click for hint</summary>

Sort by start. Keep a result list; for each interval, if it overlaps the last one
in the result (`start <= last_end`), merge by extending that last interval's end
to the max of the two ends. Otherwise append it as a new interval.

</details>

**Target complexity:** O(n log n) time for the sort, O(n) space for the result.

---

## 🏋️ How to Practice

A problem you only *read* is a problem you will fumble in an interview. Work every
problem above in three passes:

### Pass 1: Solve it in your head (5–10 minutes)

- Say the pattern signal out loud: *"sorted pair → two pointers"*, *"top k → heap"*.
- Trace a tiny example by hand - real pen and paper beats staring at the ceiling.
- State your time and space complexity **before** coding. Interviewers grade the
  conversation, not just the final code.

### Pass 2: Code it as plain functions with asserts

Save each solution as a small standalone `.py` file - no classes, no frameworks,
just functions and tests. The whole file should run with `python my_solution.py`:

```python
def climbing_stairs(n):
    """Return the number of distinct ways to climb n stairs,
    taking 1 or 2 steps at a time."""
    # your solution here
    ...


assert climbing_stairs(1) == 1
assert climbing_stairs(2) == 2
assert climbing_stairs(3) == 3      # 1+1+1, 1+2, 2+1
assert climbing_stairs(5) == 8      # Fibonacci shows up fast
print("All tests passed!")
```

Rules of thumb for this pass:

- **Start from the asserts, not the function.** Write the examples from the
  problem statement as `assert` lines first - then the function has a target.
- Include one **edge case** per problem: empty list, single element, duplicate
  values, or the impossible input (like `coin_change([2], 3)`).
- When an assert fails, do not change the assert to match your code - figure out
  which one is wrong. (Sometimes it really is the assert; prove it.)
- Once your solution passes, try to **break it** with a nastier input before
  moving on. That habit is half of what interviews probe.

### Pass 3: Compare with the site's exercises

- [Intermediate algorithms exercises](../../Exercises/intermediate/03_algorithms.py)
  and [advanced algorithms exercises](../../Exercises/advanced/06_algorithms.py)
  cover several of the same patterns with ready-made problems and solutions at the
  bottom - struggle first, then peek.
- The [Exercises overview](../../Exercises/README.md) shows how the tracks fit
  together if you want a broader warm-up before these.

Keep a small notebook (a plain `.md` file works) with one line per problem:
*pattern signal → the one idea that unlocked it → where you got stuck*. After
20 problems you will notice the same three signals repeating - that is the moment
interview questions stop feeling like trivia.

## 🧭 Keep Going

- **Next up:** [system_design_basics.md](system_design_basics.md) - the other
  half of interview prep: what to say when asked "how would this scale?"
- Back to the [Interview Prep guide](README.md) or the
  [Resources index](../README.md).
