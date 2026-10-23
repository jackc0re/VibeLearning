# 🧭 Backtracking

> Walk every path depth-first, and undo your choices on the way back

---

## 📋 Table of Contents

1. [You Already Know Half of This](#you-already-know-half-of-this)
2. [The Universal Template](#the-universal-template)
3. [Pruning: Check Before You Recurse](#pruning-check-before-you-recurse)
4. [Worked Problem 1: Generate Parentheses](#worked-problem-1-generate-parentheses)
5. [Worked Problem 2: Combination Sum](#worked-problem-2-combination-sum)
6. [Worked Problem 3: N-Queens](#worked-problem-3-n-queens)
7. [Worked Problem 4: Sudoku Solver](#worked-problem-4-sudoku-solver)
8. [Worked Problem 5: Word Search](#worked-problem-5-word-search)
9. [Complexity Honesty](#complexity-honesty)
10. [Backtracking vs Dynamic Programming](#backtracking-vs-dynamic-programming)
11. [Common Mistakes](#common-mistakes)
12. [Quick Reference](#quick-reference)

---

## You Already Know Half of This

If you have worked through [03_recursion](../03_recursion/README.md), you have already
met backtracking: its `generate_permutations` and `generate_subsets` examples build an
answer choice by choice, recurse on the smaller remaining problem, and return. That is
the template. One paragraph of review: every backtracking function carries a **state**
(the partial answer built so far), and at each call it either recognizes a **base case**
("this state is a complete answer") or loops over the **choices** available at that
point — for each choice it *makes* the choice, *recurses* to explore everything that
follows from it, and then *undoes* the choice so the next choice starts from a clean
state. This topic takes that same loop and applies it to real puzzles: matching
parentheses, N-Queens, Sudoku, and word searches — where the real skill is **pruning**,
the art of abandoning a bad path *before* walking down it.

### The Analogy: A Maze and a Piece of Chalk

Imagine exploring a maze with a piece of chalk.

- At every fork you **draw an arrow** on the floor marking the turn you took (choose).
- You walk deeper. If you reach the exit, you write down the path (a solution).
- If you hit a dead end, you walk back to the last fork and **erase your arrow**
  (unchoose), then try a different corridor.

Two things make you fast at mazes: you never re-walk a corridor (the chalk remembers),
and you learn to spot obviously pointless corridors from the entrance — "this hallway
is flooded, skip it" — instead of walking in first and discovering it later. The first
trick is the template; the second trick is **pruning**, and it is what makes the
difference between a program that finishes in milliseconds and one that outlives you.

---

## The Universal Template

Nearly every backtracking solution is this shape:

```python
def backtrack(state):
    if is_a_solution(state):        # BASE CASE: complete, valid answer
        record(state)
        return

    for choice in get_choices(state):
        if violates_a_constraint(choice, state):
            continue                # PRUNE: never recurse into a bad branch
        make(choice, state)         # CHOOSE
        backtrack(updated_state)    # EXPLORE
        undo(choice, state)         # UNCHOOSE: restore the state exactly
```

Three verbs, always in this order:

1. **Choose** — commit to one option (place a queen, add a parenthesis, mark a cell).
2. **Explore** — recurse; go as deep as possible down that option.
3. **Unchoose** — undo exactly what you did, so the loop's next option starts clean.

> The call stack is your trail of arrows. Returning from a call *is* walking back to
> the last fork — but the marks you left behind do not erase themselves. That is why
> the undo step is your job.

### The Picture: A Decision Tree

Every backtracking problem is a tree. The root is the empty state; each level adds one
decision; solutions are leaves. Backtracking walks this tree depth-first:

```
root
├── choice A
│   ├── A then B   <- leaf: a complete answer
│   └── A then C   <- leaf: dead end, walked back
└── choice B
    └── B then A   <- leaf: a complete answer
```

The undo step is what lets the walk move sideways: after finishing the subtree under
"A then B", we un-choose B, return to the "A" node, and try C from exactly the state
we had at "A".

---

## Pruning: Check Before You Recurse

The single most important performance idea in this topic:

> **Test each choice for validity BEFORE recursing, not after.**

```python
# SLOW: recurse first, discover the mistake deeper down
for choice in get_choices(state):
    make(choice)
    backtrack(state)        # walks into a branch that is already doomed
    undo(choice)

# FAST: refuse to enter doomed branches
for choice in get_choices(state):
    if violates_constraint(choice):
        continue            # the whole subtree under this choice is skipped
    make(choice)
    backtrack(state)
    undo(choice)
```

A constraint violation discovered *after* recursing still costs you the entire walk
down that branch. Discovered *before*, it costs one `if`. On exponential trees, that
one `if` is the difference between n=8 finishing instantly and never finishing.

You will see this in every worked problem below, and you can watch the numbers move in
[examples.py](examples.py) (the N-Queens demo counts solutions for n = 4 to 8).

---

## Worked Problem 1: Generate Parentheses

**Problem:** given `n` pairs of parentheses, produce every string of `2n` characters
that is *balanced*. For `n = 2`: `(())` and `()()`.

**State:** the string built so far, plus how many `(` and `)` we have used.
**Choices:** add `(` or add `)`.
**Prune rules (checked before recursing):**

- add `(` only while `open < n`
- add `)` only while `close < open` (never close more than you have opened)
- when the length reaches `2n`, the string is a solution — no pruning needed, it is
  valid by construction

### Decision Tree (n = 2)

```
                         ""                  open=0, close=0
                          |
           add "(" -------+------- add ")"
           open=1         |         (pruned! close == open,
           close=0        |          cannot close before opening)
                          |
        add "(" ----------+---------- add ")"
        open=2, close=0                open=1, close=1
        "("                            "()"
          |                              |
       only "(" was possible,         only "(" fits
       now only ")" fits              (close == open)
       (open == n)
          |                              |
        "(()"                          "()("
          |                              |
       only ")" fits                   only ")" fits
          |                              |
       "(())"  length 4 -> SOLUTION   "()()"  length 4 -> SOLUTION
```

### Code

```python
def generate_parentheses(n):
    """Return all balanced strings of n pairs of parentheses."""
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:          # base case: used all n pairs
            result.append("".join(current))
            return
        if open_count < n:                 # prune: too many "(" otherwise
            current.append("(")
            backtrack(current, open_count + 1, close_count)
            current.pop()                  # unchoose
        if close_count < open_count:       # prune: ")" only if one is open
            current.append(")")
            backtrack(current, open_count, close_count + 1)
            current.pop()                  # unchoose

    backtrack([], 0, 0)
    return result
```

Notice there is *no* validity check at the end — pruning guarantees every completed
string is balanced. The number of answers is the n-th Catalan number (1, 2, 5, 14, 42,
... for n = 1..6), which grows like `4^n / n^1.5` — exponential, but far smaller than
the `2^(2n)` strings brute force would try.

---

## Worked Problem 2: Combination Sum

**Problem:** given candidates and a target, find all combinations that sum to the
target. Two variants:

- **Reusable** (a candidate may be used any number of times)
- **No-reuse** (each candidate may be used at most once; the input may contain
  duplicates)

**State:** the remaining target and the combination built so far.
**Prune rule:** sort the candidates first; stop the loop (`break`) as soon as the
current candidate exceeds the remaining target — everything after it is bigger still.

### Decision Tree (candidates [2, 3, 5], target 5, reusable)

```
need=5, start at 2 (reuse allowed)
[]
├── take 2 -> need=3
│   ├── take 2 -> need=1
│   │   ├── take 2 -> need=-1   pruned (overshot)
│   │   ├── take 3 -> need=-2   pruned
│   │   └── take 5 -> need=-4   pruned
│   ├── take 3 -> need=0        SOLUTION [2, 3]
│   └── take 5 -> need=-2       pruned
├── take 3 -> need=2
│   ├── take 3 -> need=-1       pruned
│   └── take 5 -> need=-3       pruned
└── take 5 -> need=0            SOLUTION [5]
```

### Reusable Variant

```python
def combination_sum(candidates, target):
    """All combinations summing to target; candidates may be reused."""
    result = []
    candidates = sorted(candidates)            # enables the break-prune

    def backtrack(start, remaining, path):
        if remaining == 0:                     # base case: exact sum
            result.append(path[:])             # COPY: we keep building on path
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:      # prune: sorted -> rest too big
                break
            path.append(candidates[i])         # choose
            backtrack(i, remaining - candidates[i], path)  # i, not i+1: reuse
            path.pop()                         # unchoose

    backtrack(0, target, [])
    return result
```

The two subtle details:

- Recursing with `i` (not `i + 1`) allows reuse of the same candidate.
- Starting the loop at `start` (not `0`) keeps combinations sorted internally, so
  `[2, 3]` is produced once — never again as `[3, 2]`.

### No-Reuse Variant: the Sorted + Skip-Duplicates Trick

When the *input* has duplicates (say `[1, 1, 2, 5]`) and each element may be used
once, sorting plus one guard removes the duplicate answers:

```python
def combination_sum_no_reuse(candidates, target):
    """All combinations summing to target; each candidate used at most once."""
    result = []
    candidates = sorted(candidates)

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            # Skip duplicates AT THE SAME tree level: the first copy of a value
            # already explored every branch that begins with that value.
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:      # prune: sorted -> rest too big
                break
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], path)  # i + 1: no reuse
            path.pop()

    backtrack(0, target, [])
    return result
```

Why `i > start and candidates[i] == candidates[i - 1]` works: at any tree node, if
two equal candidates sit side by side, the branch beginning with the *second* copy
can only produce combinations the branch beginning with the *first* copy already
produced. Skipping it deletes duplicates without deleting any distinct answer.

---

## Worked Problem 3: N-Queens

**Problem:** place `n` queens on an `n x n` chessboard so that no two attack each
other (no shared row, column, or diagonal).

**State:** which column each row's queen occupies, plus three sets recording the
occupied columns and diagonals.
**Choices:** for the current row, one of the `n` columns.
**Prune rules:** a column is safe only if

- `col` is not in `cols` (column check),
- `row - col` is not in `diag1` (each "\" diagonal has a constant `row - col`),
- `row + col` is not in `diag2` (each "/" diagonal has a constant `row + col`).

The diagonal math is worth pausing on. Moving down-right keeps `row - col` the same
(0+0 = 1+1 = 2+2 = 0); moving down-left keeps `row + col` the same (0+2 = 1+1 = 2+0
= 2). So two integer sets track *all* diagonals on the board.

### Decision Tree (n = 4)

```
                     row 0: try columns 0, 1, 2, 3
        col 0            col 1            col 2            col 3
          |                |                |                |
        row 1:           row 1:           row 1:           row 1:
    only col 2, 3    only col 3       only col 0       only col 0, 1
    pass the checks  passes           passes           pass the checks
          |                |                |                |
        rows 2-3:        row 2:           row 2:          rows 2-3:
    every path dies  col 0 (forced)   col 3 (forced)   every path dies
          X                |                |                X
                       row 3:           row 3:
                       col 2 (forced)   col 1 (forced)
                           |                |
                    SOLUTION           SOLUTION
                    [1, 3, 0, 2]       [2, 0, 3, 1]
```

For example, under the col 1 branch the queen at (0, 1) immediately attacks three of
row 1's four squares: col 0 shares `row + col = 1`, col 1 is the same column, and
col 2 shares `row - col = -1`. Only col 3 survives, and the rest of that branch is
forced all the way to the solution.

The first solution, drawn with `Q` and `.` (queens at columns 1, 3, 0, 2 by row):

```
. Q . .
. . . Q
Q . . .
. . Q .
```

### Code

```python
def solve_n_queens(n):
    """Return every solution as a list: board[row] = column of that row's queen."""
    solutions = []
    cols = set()    # occupied columns
    diag1 = set()   # occupied "\" diagonals (row - col)
    diag2 = set()   # occupied "/" diagonals (row + col)
    board = []      # board[row] = col (doubles as the chosen path)

    def backtrack(row):
        if row == n:                       # base case: every row has a queen
            solutions.append(board[:])
            return
        for col in range(n):
            if (col in cols or (row - col) in diag1
                    or (row + col) in diag2):
                continue                   # prune BEFORE recursing
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            board.append(col)              # choose
            backtrack(row + 1)             # explore next row
            board.pop()                    # unchoose
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

    backtrack(0)
    return solutions


def format_n_queens_board(queens):
    """Render a solution as rows of 'Q' and '.'."""
    n = len(queens)
    return [" ".join("Q" if col == queens[row] else "." for col in range(n))
            for row in range(n)]
```

Actual counts you can verify with [examples.py](examples.py):

| n | solutions |
|---|-----------|
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 7 | 40 |
| 8 | 92 |

Without the diagonal sets you would re-scan the whole board for every candidate
square; with them each check is O(1). But the *shape* of the win is the pruning:
whole columns are refused at row 0, entire subtrees die one level down.

---

## Worked Problem 4: Sudoku Solver

**Problem:** fill a 9x9 grid (blanks stored as `0`) so every row, column, and 3x3 box
contains the digits 1-9 exactly once.

**State:** the grid itself (mutated in place — there is one grid, not a copy per call).
**Choices:** for the first empty cell, digits 1 through 9.
**Prune rule:** `is_valid` rejects any digit that already appears in the cell's row,
column, or box — before recursing.

```python
def find_empty(grid):
    """Return (row, col) of the first empty cell, or None if the grid is full."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None


def is_valid(grid, row, col, value):
    """Can 'value' be placed at (row, col) without breaking Sudoku rules?"""
    # Row and column check
    for i in range(9):
        if grid[row][i] == value or grid[i][col] == value:
            return False
    # 3x3 box check: (row, col) lives in the box whose top-left corner is
    # (3 * (row // 3), 3 * (col // 3))
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == value:
                return False
    return True


def solve_sudoku(grid):
    """Solve the grid in place. Returns True when solved."""
    find = find_empty(grid)
    if find is None:
        return True                     # base case: no empty cells -> solved
    row, col = find

    for value in range(1, 10):
        if is_valid(grid, row, col, value):     # prune BEFORE recursing
            grid[row][col] = value              # choose
            if solve_sudoku(grid):              # explore
                return True                     # single-solution early exit
            grid[row][col] = 0                  # unchoose
    return False                            # no digit fits: backtrack
```

Two differences from the earlier problems are worth noticing:

- **The early exit.** Most backtracking problems want *every* solution, so after
  recording one they unchoose and keep searching. Sudoku (with a well-posed puzzle)
  has exactly one, so the moment a branch reports success, `return True` ripples all
  the way up the call stack and every remaining branch is abandoned unexplored.
- **The state is mutated in place** and restored by assignment (`grid[row][col] = 0`)
  rather than by `append`/`pop` — the choose/unchoose pattern is the same either way.

---

## Worked Problem 5: Word Search

**Problem:** given a grid of letters and a word, can the word be traced by moving
between horizontally/vertically adjacent cells, using each cell at most once per path?

**State:** the current cell, the index into the word, and a `visited` set of cells on
the current path.
**Choices:** the four neighbors of the current cell.
**Prune rules:** reject a neighbor that is out of bounds, already visited, or holds
the wrong letter — all *before* recursing.

The heart of this problem is **visited-set discipline**: add the cell to `visited`
*before* the recursive calls, remove it *after*. The set then always contains exactly
the cells on the current path — no more, no less.

```python
def word_search(board, word):
    """True if 'word' can be traced through adjacent cells of the grid."""
    rows, cols = len(board), len(board[0])
    visited = set()

    def backtrack(row, col, index):
        if index == len(word):                 # base case: matched everything
            return True
        if (row < 0 or row >= rows or col < 0 or col >= cols
                or (row, col) in visited       # prune: cell already on path
                or board[row][col] != word[index]):   # prune: wrong letter
            return False

        visited.add((row, col))                # choose (BEFORE recursing)
        found = (backtrack(row + 1, col, index + 1) or
                 backtrack(row - 1, col, index + 1) or
                 backtrack(row, col + 1, index + 1) or
                 backtrack(row, col - 1, index + 1))
        visited.remove((row, col))             # unchoose (AFTER recursing)
        return found

    for row in range(rows):                    # try every starting cell
        for col in range(cols):
            if backtrack(row, col, 0):
                return True
    return False
```

Trace for `"ABCCED"` on a small grid:

```
grid:            path:
A B C E          (0,0)'A' -> right (0,1)'B' -> right (0,2)'C'
S F C S                    -> down  (1,2)'C' -> down (2,2)'E'
A D E E                              -> left (2,1)'D'   FOUND
```

Forget the `visited.remove` and the set keeps growing across *unrelated* branches:
a cell explored during one failed path stays poisoned for every later path, and
correct answers silently disappear. This is the most common backtracking bug in
the wild — see [Common Mistakes](#common-mistakes).

---

## Complexity Honesty

No comforting lies: backtracking problems are **exponential**.

| Problem | Number of solutions / worst case | Growth |
|---------|----------------------------------|--------|
| Subsets of n items | `2^n` | n=20 -> ~1M, n=30 -> ~1B |
| Permutations of n items | `n!` | n=10 -> ~3.6M, n=13 -> ~6.2B |
| Generate parentheses (n pairs) | Catalan(n) ~ `4^n / n^1.5` | n=10 -> 16,796 |
| N-Queens (n rows) | no formula; counts: 2, 10, 4, 40, 92, ... for n=4..8 | explodes |
| Sudoku (m empty cells) | up to `9^m` leaves without pruning | brutal |

If you need *all* solutions, there is no way around output-sensitive exponential
time — the answer itself is exponentially large. What pruning buys you is not a
polynomial algorithm; it is a **constant-factor-to-catastrophe** reduction in the
number of *explored* nodes, which is what makes n = 8 queens (92 answers) or a
newspaper Sudoku finish in milliseconds. When someone tells you their backtracking
solution "is O(n)", they mean the work per node — the node count is still exponential.

Practical consequences:

1. **Prune as early as possible.** A check at depth 2 kills a subtree of size
   `b^(n-2)`; the same check at depth n-2 kills one leaf.
2. **Order choices cleverly** when you only need *one* solution (try most-constrained
   cells first in Sudoku).
3. **Know when to stop.** If n can be 10^5, backtracking is the wrong tool — see DP
   below.

---

## Backtracking vs Dynamic Programming

Both explore decision trees recursively — the difference is the question they ask.

| Aspect | Backtracking | Dynamic Programming |
|--------|--------------|---------------------|
| Question asked | "List/produce every valid arrangement" | "How many are there? What is the best one?" |
| Output | The solutions themselves | A count or an optimal value |
| Subproblems | Distinct states — little overlap | Heavy overlap (same state reached many ways) |
| State after a call | Restored (choose/unchoose) | Cached (memo table) |
| Cost | Exponential in general | Polynomial when the state space is |
| Typical problems | N-Queens, Sudoku, word search, parentheses | Fibonacci, knapsack, edit distance |

Rule of thumb: if two different decision paths can arrive at the *same* partial
state (overlapping subproblems), memoizing turns enumeration into DP. In pure
combinatorial puzzles — queens, Sudoku — states almost never repeat, there is
nothing to cache, and backtracking with good pruning is the right (and often only)
tool. For a deeper look at the DP side, see
[04_dynamic_programming](../04_dynamic_programming/README.md).

---

## Common Mistakes

### 1. Forgetting to undo the choice

```python
path.append(choice)
backtrack(state)
# BUG: missing path.pop()
```

Every branch's choices leak into its siblings: results get duplicated, lengths go
wrong, and "impossible" states appear. The fix is mechanical — whatever you add,
remove; whatever you set, unset; and do it in the same function, right after the
recursive call.

### 2. Pruning too late

```python
backtrack(state)                    # recurse first...
if not is_valid(state):             # ...check afterwards
    return
```

A check placed after the recursive call still pays for the entire subtree below the
bad choice. Validate the choice at the top of the loop and `continue` before any
recursion happens. In word search the "too late" version is even worse: without the
bounds/visited checks placed first, the recursion never terminates at all.

### 3. Copying state when you could undo (and vice versa)

Two opposite errors:

- Copying the whole state (`path[:]`) at every tree node "to be safe". The template
  needs ONE shared list that choose/unchoose keeps correct — copying at every node
  multiplies your cost by the state size.
- NOT copying when *recording* a solution. `result.append(path)` stores a reference
  to the list you keep mutating; by the end every recorded "solution" is the same
  (empty or final) list. Record with `path[:]`.

Rule: mutate + undo while exploring; copy only at the moment you save an answer.

### 4. Recursion without bounds

Missing the base case (or making it unreachable) means `RecursionError` once the
tree gets deep — and in problems like word search, missing *bounds* checks means
the walk wanders off the grid or cycles through the same cells forever. Every
backtracking function needs a provably reachable base case, and every state
transition must make bounded progress (an index that increases, a remaining target
that shrinks, a row that advances).

---

## Quick Reference

| Problem | State | Choose / Undo | Prune when |
|---------|-------|---------------|------------|
| Generate parentheses | current chars + open/close counts | append char / pop | `open == n` blocks "(", `close == open` blocks ")" |
| Combination sum (reuse) | remaining target + start index | append candidate / pop | candidate > remaining (sorted) |
| Combination sum (no reuse) | remaining target + start index | append candidate / pop | duplicate at same level, or candidate > remaining |
| N-Queens | row + cols/diag sets | place queen / remove queen | column or either diagonal occupied |
| Sudoku | grid + first empty cell | write digit / reset to 0 | digit clashes with row/col/box |
| Word search | (row, col) + word index + visited set | add to visited / remove | out of bounds, visited, wrong letter |

The template underneath all six rows:

```python
for choice in choices(state):
    if bad(choice):        # prune BEFORE recursing
        continue
    make(choice)           # choose
    backtrack(state)       # explore
    undo(choice)           # unchoose
```

---

## 🔑 Key Takeaways

1. **Choose -> Explore -> Unchoose** — the three verbs of every backtracking function.
2. **The state must be restored** after each branch, or siblings inherit garbage.
3. **Prune before recursing** — one early `if` kills entire subtrees.
4. **Sort + skip duplicates** (`i > start and nums[i] == nums[i-1]`) de-duplicates
   no-reuse combination problems.
5. **N-Queens in O(1) per check**: `cols`, `row - col`, `row + col` sets.
6. **Visited-set discipline**: add before recursing, remove after.
7. **These problems are exponential** — pruning makes them practical, not polynomial.
8. **Backtracking enumerates; DP counts or optimizes** when subproblems overlap.

---

## 🔗 Next Steps

- Practice with [`exercises.py`](exercises.py)
- Test your knowledge with [`quiz.md`](quiz.md)
- Revisit [03_recursion](../03_recursion/README.md) and re-read its permutation and
  subset examples — you will now recognize every choose/unchoose pair
- See the counting side of decision trees in
  [04_dynamic_programming](../04_dynamic_programming/README.md)
