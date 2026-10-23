# 🧠 Backtracking Quiz

Test your understanding of backtracking!

---

## Question 1

**What are the three verbs of the universal backtracking template, in order?**

- A) Divide, Conquer, Combine
- B) Choose, Explore, Unchoose
- C) Plan, Execute, Verify
- D) Sort, Search, Return

<details>
<summary>Show Answer</summary>

**B) Choose, Explore, Unchoose**

For each candidate choice: make it, recurse to explore everything downstream of it,
then undo it so the next choice in the loop starts from exactly the same state. The
undo step is what lets the walk move sideways across the decision tree.

</details>

---

## Question 2

**Why should you check a constraint BEFORE recursing rather than after returning?**

- A) The result is different
- B) Python forbids recursion after a failed check
- C) A bad choice recursed first costs the whole subtree walk; caught first it costs one `if`
- D) It makes the code shorter

<details>
<summary>Show Answer</summary>

**C) A bad choice recursed first costs the whole subtree walk; caught first it costs one `if`**

A constraint violation at depth 2 dooms a subtree with roughly `b^(n-2)` nodes.
Checking before recursing skips entering that subtree at all. On exponential trees
this is the difference between milliseconds and never finishing — pruning makes
backtracking practical, though it does not make it polynomial.

</details>

---

## Question 3

**In generate_parentheses(n), what are the two pruning conditions on adding characters?**

- A) Add `(` while `open <= n`; add `)` any time
- B) Add `(` only while `open < n`; add `)` only while `close < open`
- C) Add `(` and `)` alternately, always
- D) Add `)` only while `close < n`; add `(` only while `open < close`

<details>
<summary>Show Answer</summary>

**B) Add `(` only while `open < n`; add `)` only while `close < open`**

With these two rules, every string that reaches length `2n` is balanced by
construction — no final validity check is needed. The `close < open` rule is the
one that prevents prefixes like `())` that can never recover.

</details>

---

## Question 4

**In N-Queens, why do the two diagonal sets use `row - col` and `row + col` as keys?**

- A) They are random hash keys that avoid collisions
- B) Moving down-right keeps `row - col` constant; moving down-left keeps `row + col` constant
- C) They store the queen's row and column directly
- D) They count how many diagonals cross each square

<details>
<summary>Show Answer</summary>

**B) Moving down-right keeps `row - col` constant; moving down-left keeps `row + col` constant**

Every square on the same "\" diagonal shares the same `row - col` value (0+0 = 1+1
= 2+2), and every square on the same "/" diagonal shares the same `row + col` value
(0+2 = 1+1 = 2+0). Two integer sets therefore replace scanning the whole board —
each safety check is O(1).

</details>

---

## Question 5

**In word search, what goes wrong if you add cells to the `visited` set but forget to remove them after the recursive calls?**

- A) Nothing, the answer stays correct
- B) Cells explored during one failed path stay "poisoned" for later paths, so valid words stop being found
- C) The recursion never terminates
- D) The word is found twice

<details>
<summary>Show Answer</summary>

**B) Cells explored during one failed path stay "poisoned" for later paths, so valid words stop being found**

The visited set must contain exactly the cells on the *current* path. Without the
remove step it contains every cell ever touched, so the search wrongly treats cells
from unrelated branches as used. This "forgot to undo" bug is the most common
backtracking mistake in general.

</details>

---

## Question 6

**Your input for a no-reuse combination-sum style problem contains duplicates (e.g. [1, 1, 2, 5]). What is the standard trick for avoiding duplicate answers?**

- A) Sort, then skip a candidate when `i > start and nums[i] == nums[i-1]`
- B) Keep a set of answers and remove duplicates at the end
- C) Reverse the input before searching
- D) Use a dictionary instead of a list for candidates

<details>
<summary>Show Answer</summary>

**A) Sort, then skip a candidate when `i > start and nums[i] == nums[i-1]`**

At any tree node, a branch beginning with the second copy of an equal value can only
produce combinations the branch beginning with the first copy already produced. The
guard skips exactly those branches, deleting duplicate answers without losing any
distinct one. Deduplicating finished answers at the end works too, but it pays for
the duplicate subtrees instead of never exploring them.

</details>

---

## Question 7

**Which problem calls for backtracking rather than dynamic programming?**

- A) "How many ways can we make change for amount X?" (same coins reused many ways)
- B) "What is the minimum edit distance between two strings?"
- C) "List every way to place 8 non-attacking queens on a board"
- D) "What is the maximum sum of a contiguous subarray?"

<details>
<summary>Show Answer</summary>

**C) List every way to place 8 non-attacking queens on a board**

Backtracking *enumerates* solutions; DP *counts or optimizes* when subproblems
overlap. A, B, and D ask how many / how good — classic DP. The queen problem asks
for every distinct arrangement, states almost never repeat, so there is nothing to
memoize and backtracking with pruning is the right tool.

</details>

---

## Question 8

**A teammate claims their backtracking solution "runs in O(n)" because each tree node does O(n) work. What is the honest assessment?**

- A) Correct — work per node determines total complexity
- B) The node count itself is exponential; pruning reduces explored nodes but does not make the problem polynomial
- C) They forgot to count the recursion stack, which is O(n!)
- D) Backtracking is always O(2^n), no exceptions

<details>
<summary>Show Answer</summary>

**B) The node count itself is exponential; pruning reduces explored nodes but does not make the problem polynomial**

Total cost is (work per node) x (number of nodes). Backtracking trees are
exponential in the worst case — subsets 2^n, permutations n!, Sudoku up to 9^blanks.
Pruning shrinks the *explored* tree dramatically (that is why 8-queens finishes in
milliseconds), but the worst case remains exponential. Say "exponential, made
practical by pruning" — not O(n).

</details>

---

## 🏆 Score Guide

| Score | Rating |
|-------|--------|
| 8 | ⭐⭐⭐⭐⭐ Backtracking master! |
| 6-7 | ⭐⭐⭐⭐ Great understanding! |
| 4-5 | ⭐⭐⭐ Good progress! |
| 2-3 | ⭐⭐ Review the concepts |
| 0-1 | ⭐ Start with the template |

---

## 📚 Review Topics

If you struggled with certain questions, review these topics:

- **Questions 1-2**: The universal template and pruning before recursing
- **Questions 3-4**: Constraint tracking in parentheses and N-Queens
- **Questions 5-6**: Undo discipline and the sorted + skip-duplicates trick
- **Questions 7-8**: Backtracking vs DP, and complexity honesty

---

[Back to Backtracking README](README.md) | [Next: Dynamic Programming →](../04_dynamic_programming/README.md)
