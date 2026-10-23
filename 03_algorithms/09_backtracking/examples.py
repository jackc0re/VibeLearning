"""
Backtracking - Examples
=======================

This file demonstrates the backtracking template (choose -> explore ->
unchoose) on classic problems: subsets, generate parentheses,
combination sum, N-Queens, Sudoku, and word search.

Run this file to see the examples in action:
    python examples.py
"""

print("=" * 60)
print("BACKTRACKING - Examples")
print("=" * 60)


# =============================================================================
# THE UNIVERSAL TEMPLATE
# =============================================================================

def subsets_with_trace(items, depth=0, path=None):
    """
    Every subset of items, choosing INCLUDE or SKIP per element.

    This is the template with the three verbs printed out:
        CHOOSE  - commit to one option
        EXPLORE - recurse deeper
        UNCHOOSE- undo it so the next option starts clean
    """
    if path is None:
        path = []

    indent = "  " * depth

    if depth == len(items):
        # Base case: every element got a decision -> path is a subset
        print(f"{indent}base case -> record subset {path}")
        return [path[:]]

    results = []

    # Choice 1: INCLUDE items[depth]
    print(f"{indent}CHOOSE  include {items[depth]} (path={path})")
    path.append(items[depth])
    results.extend(subsets_with_trace(items, depth + 1, path))
    path.pop()
    print(f"{indent}UNCHOOSE include {items[depth]} (path back to {path})")

    # Choice 2: SKIP items[depth]
    print(f"{indent}CHOOSE  skip {items[depth]} (path={path})")
    results.extend(subsets_with_trace(items, depth + 1, path))

    return results


# =============================================================================
# GENERATE PARENTHESES
# =============================================================================

def generate_parentheses(n):
    """
    Return every balanced string of n pairs of parentheses.

    State: the chars built so far + how many ( and ) are used.
    Prune: add ( only while open < n;
           add ) only while close < open (never close more than opened).

    Time: O(4^n / sqrt(n)) answers (the n-th Catalan number)
    Space: O(n) recursion depth (plus the output)
    """
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            # Base case: used all n pairs; valid by construction
            result.append("".join(current))
            return
        if open_count < n:
            current.append("(")
            backtrack(current, open_count + 1, close_count)
            current.pop()
        if close_count < open_count:
            current.append(")")
            backtrack(current, open_count, close_count + 1)
            current.pop()

    backtrack([], 0, 0)
    return result


# =============================================================================
# COMBINATION SUM (REUSABLE AND NO-REUSE VARIANTS)
# =============================================================================

def combination_sum(candidates, target):
    """
    All combinations summing to target; each candidate may be reused.

    Prune: sort first, then break as soon as a candidate exceeds the
    remaining target (everything after it is bigger still).

    Time: exponential in general, but pruning skips all overshoots
    Space: O(target / min(candidates)) recursion depth
    """
    result = []
    candidates = sorted(candidates)

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])  # copy: we keep mutating path
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # sorted -> the rest are too big as well
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)  # i: allows reuse
            path.pop()

    backtrack(0, target, [])
    return result


def combination_sum_no_reuse(candidates, target):
    """
    All combinations summing to target; each candidate used at most once.

    The sorted + skip-duplicates trick:
        i > start and candidates[i] == candidates[i - 1]
    skips the second (and later) copy of an equal value at the same tree
    level, where it could only produce answers the first copy produced.
    """
    result = []
    candidates = sorted(candidates)

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue  # skip duplicate value at this tree level
            if candidates[i] > remaining:
                break  # sorted -> the rest are too big as well
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], path)  # i + 1: no reuse
            path.pop()

    backtrack(0, target, [])
    return result


# =============================================================================
# N-QUEENS
# =============================================================================

def solve_n_queens(n):
    """
    Return every n-queens solution as board[row] = column of that row's queen.

    O(1) safety checks with three sets:
        cols  - occupied columns
        diag1 - occupied "/" diagonals... keyed by (row - col)
        diag2 - occupied "\" diagonals... keyed by (row + col)
    Moving down-right keeps row - col constant; moving down-left keeps
    row + col constant. Two integers per queen replace a full board scan.

    Time: exponential worst case; pruning makes n=8 instant
    """
    solutions = []
    cols = set()
    diag1 = set()  # keyed by row - col
    diag2 = set()  # keyed by row + col
    board = []     # board[row] = col; doubles as the chosen path

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if (col in cols or (row - col) in diag1
                    or (row + col) in diag2):
                continue  # prune BEFORE recursing
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board.append(col)
            backtrack(row + 1)
            board.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return solutions


def format_n_queens_board(queens):
    """Render one solution (board[row] = col) as rows of Q and . strings."""
    n = len(queens)
    return [" ".join("Q" if col == queens[row] else "." for col in range(n))
            for row in range(n)]


# =============================================================================
# SUDOKU SOLVER
# =============================================================================

def find_empty(grid):
    """Return (row, col) of the first empty cell, or None if the grid is full."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None


def is_valid(grid, row, col, value):
    """Can value be placed at (row, col) without breaking Sudoku rules?"""
    # Row and column check
    for i in range(9):
        if grid[row][i] == value or grid[i][col] == value:
            return False
    # 3x3 box check; the box's top-left corner is (3 * (row // 3), 3 * (col // 3))
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == value:
                return False
    return True


def solve_sudoku(grid):
    """
    Solve the 9x9 grid in place (blanks are 0). Returns True when solved.

    The early exit: a well-posed puzzle has exactly one solution, so the
    moment a branch reports success we return True all the way up the call
    stack instead of unchoosing and searching for more.
    """
    find = find_empty(grid)
    if find is None:
        return True  # base case: no empty cells left -> solved
    row, col = find

    for value in range(1, 10):
        if is_valid(grid, row, col, value):  # prune BEFORE recursing
            grid[row][col] = value           # choose
            if solve_sudoku(grid):           # explore
                return True                  # early exit: keep the solution
            grid[row][col] = 0               # unchoose
    return False  # no digit fits this cell -> backtrack


# =============================================================================
# WORD SEARCH
# =============================================================================

def word_search(board, word):
    """
    True if word can be traced through horizontally/vertically adjacent
    cells, using each cell at most once per path.

    Visited-set discipline: add the cell BEFORE recursing, remove it AFTER.
    The set then always holds exactly the cells on the current path.
    """
    rows, cols = len(board), len(board[0])
    visited = set()

    def backtrack(row, col, index):
        if index == len(word):
            return True  # base case: matched every letter
        if (row < 0 or row >= rows or col < 0 or col >= cols
                or (row, col) in visited
                or board[row][col] != word[index]):
            return False  # prune: off-grid / reused cell / wrong letter

        visited.add((row, col))  # choose (BEFORE recursing)
        found = (backtrack(row + 1, col, index + 1) or
                 backtrack(row - 1, col, index + 1) or
                 backtrack(row, col + 1, index + 1) or
                 backtrack(row, col - 1, index + 1))
        visited.remove((row, col))  # unchoose (AFTER recursing)
        return found

    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, 0):
                return True
    return False


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_template():
    """Demonstrate choose / explore / unchoose on tiny subset generation."""
    print("\n" + "=" * 60)
    print("THE UNIVERSAL TEMPLATE (all subsets of [1, 2])")
    print("=" * 60)

    print("\nTrace of choices (CHOOSE / UNCHOOSE pairs):")
    result = subsets_with_trace([1, 2])
    print(f"\nAll subsets of [1, 2]: {result}")
    print("After every EXPLORE the state is exactly what it was before.")


def demo_generate_parentheses():
    """Demonstrate generate_parentheses for small n."""
    print("\n" + "=" * 60)
    print("GENERATE PARENTHESES")
    print("=" * 60)

    for n in [1, 2, 3]:
        result = generate_parentheses(n)
        label = "string" if len(result) == 1 else "strings"
        print(f"\nn = {n} -> {len(result)} balanced {label}:")
        for s in result:
            print(f"    {s}")

    print("\nPruning guarantees validity: we never add ')' unless one")
    print("parenthesis is still open, so no completed string needs a check.")


def demo_combination_sum():
    """Demonstrate both combination sum variants."""
    print("\n" + "=" * 60)
    print("COMBINATION SUM")
    print("=" * 60)

    print("\nReusable variant: candidates [2, 3, 6, 7], target 7")
    print(f"  -> {sorted(combination_sum([2, 3, 6, 7], 7))}")
    print("  (2 may be used repeatedly: [2, 2, 3])")

    print("\nReusable variant: candidates [2, 3, 5], target 8")
    print(f"  -> {sorted(combination_sum([2, 3, 5], 8))}")

    print("\nNo-reuse variant: candidates [10, 1, 2, 7, 6, 1, 5], target 8")
    print(f"  -> {sorted(combination_sum_no_reuse([10, 1, 2, 7, 6, 1, 5], 8))}")
    print("  (the input has two 1s, but each answer appears exactly once)")
    print("  (sorted + 'skip duplicates at the same tree level' did that)")


def demo_n_queens():
    """Demonstrate N-Queens: one board printed, counts for n = 4..8."""
    print("\n" + "=" * 60)
    print("N-QUEENS")
    print("=" * 60)

    solutions4 = solve_n_queens(4)
    print(f"\nn = 4 has {len(solutions4)} solutions. The first one:")
    for row in format_n_queens_board(solutions4[0]):
        print(f"    {row}")

    print("\nSolution counts (match the known sequence):")
    known = {4: 2, 5: 10, 6: 4, 7: 40, 8: 92}
    for n in [4, 5, 6, 7, 8]:
        count = len(solve_n_queens(n))
        status = "PASS" if count == known[n] else "FAIL"
        print(f"  n = {n}: {count:3d} solutions (expected {known[n]:3d}) {status}")

    print("\nThe sets (cols, row-col, row+col) make each safety check O(1),")
    print("but the real win is pruning whole columns at the top of the tree.")


def demo_sudoku():
    """Demonstrate the Sudoku solver: before/after grid."""
    print("\n" + "=" * 60)
    print("SUDOKU SOLVER")
    print("=" * 60)

    # 0 marks an empty cell.
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    def print_grid(grid, title):
        print(f"\n{title}")
        for row in grid:
            print("    " + " ".join(str(v) if v != 0 else "." for v in row))

    print_grid(puzzle, "Before:")

    import time
    start = time.perf_counter()
    solved = solve_sudoku(puzzle)
    elapsed = time.perf_counter() - start

    print(f"\nSolved: {solved} (took {elapsed * 1000:.1f} ms)")
    print_grid(puzzle, "After:")

    print("\nThe 'return True' early exit stops the search the moment the")
    print("solution is found instead of enumerating alternative fills.")


def demo_word_search():
    """Demonstrate word search with visited-set discipline."""
    print("\n" + "=" * 60)
    print("WORD SEARCH")
    print("=" * 60)

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    print("\nGrid:")
    for row in board:
        print("    " + " ".join(row))

    for word in ["ABCCED", "SEE", "ABCB"]:
        found = word_search(board, word)
        print(f"\n  '{word}' -> {found}")
        if word == "ABCCED":
            print("         path: A(0,0) B(0,1) C(0,2) C(1,2) E(2,2) D(2,1)")
        if word == "ABCB":
            print("         the B at (0,1) is on the path already; reusing it")
            print("         would need the visited set to lie - so: not found")


def demo_complexity_honesty():
    """Show why these problems are exponential - and why pruning matters."""
    print("\n" + "=" * 60)
    print("COMPLEXITY HONESTY")
    print("=" * 60)

    print("\nThe number of subsets alone grows as 2^n:")
    for n in [5, 10, 15, 20, 25]:
        print(f"  n = {n:2d}: {2 ** n:>10,} subsets")

    print("\nN-Queens solution counts keep growing too (no closed formula):")
    for n in [4, 5, 6, 7, 8]:
        print(f"  n = {n}: {len(solve_n_queens(n)):3d} solutions")

    print("\nPruning does not make these problems polynomial. It shrinks the")
    print("EXPLORED part of the tree enough that small n finishes in ms.")
    print("Backtracking enumerates answers; DP (next topic) counts or")
    print("optimizes when subproblems overlap.")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    demo_template()
    demo_generate_parentheses()
    demo_combination_sum()
    demo_n_queens()
    demo_sudoku()
    demo_word_search()
    demo_complexity_honesty()

    print("\n" + "=" * 60)
    print("PASS All backtracking examples completed!")
    print("Examples complete! Try exercises.py next.")
    print("=" * 60)
