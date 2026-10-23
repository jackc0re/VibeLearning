"""
Backtracking - Exercises
========================

Practice implementing backtracking algorithms with the universal
template: choose -> explore -> unchoose, pruning before you recurse.

Each exercise includes test cases to verify your solution.

Run this file to test your implementations:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Generate Parentheses
# =============================================================================

def generate_parentheses(n):
    """
    Return every balanced string of n pairs of parentheses.

    Template hints:
    - State: the characters chosen so far + open/close counters
    - Choose: append "(" while open < n; append ")" while close < open
    - Unchoose: pop the character after the recursive call
    - Base case: the string reaches length 2 * n

    Args:
        n: Number of parenthesis pairs

    Returns:
        List of balanced strings (any order)

    Example:
        >>> sorted(generate_parentheses(2))
        ['(())', '()()']
        >>> len(generate_parentheses(3))
        5
    """
    # TODO: YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Combination Sum (Reusable)
# =============================================================================

def combination_sum(candidates, target):
    """
    Return all combinations of candidates that sum to target.
    The same candidate may be chosen any number of times.

    Template hints:
    - Sort the candidates so you can break when one exceeds the remaining
      target (everything after it is bigger still)
    - Recurse with index i (not i + 1) to allow reuse
    - Recurse with a start index so combinations come out in one order
      only (never both [2, 3] and [3, 2])

    Args:
        candidates: List of distinct positive integers
        target: Target sum (positive integer)

    Returns:
        List of combinations (each a list), any order

    Example:
        >>> sorted(combination_sum([2, 3, 6, 7], 7))
        [[2, 2, 3], [7]]
    """
    # TODO: YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Combination Sum (No Reuse, Duplicates in Input)
# =============================================================================

def combination_sum_no_reuse(candidates, target):
    """
    Return all combinations that sum to target, where each candidate may
    be used AT MOST once. The input may contain duplicate values, but the
    output must not contain duplicate combinations.

    Template hints:
    - Sort the candidates first
    - Skip duplicates at the same tree level:
          if i > start and candidates[i] == candidates[i - 1]: continue
    - Recurse with i + 1 (no reuse)

    Args:
        candidates: List of positive integers (may contain duplicates)
        target: Target sum (positive integer)

    Returns:
        List of distinct combinations (each a list), any order

    Example:
        >>> sorted(combination_sum_no_reuse([10, 1, 2, 7, 6, 1, 5], 8))
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    """
    # TODO: YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Subsets With Duplicates
# =============================================================================

def subsets_with_dupes(nums):
    """
    Return every subset of nums (the power set). The input may contain
    duplicates, but the output must not contain duplicate subsets.

    Template hints:
    - Same sorted + skip-duplicates trick as Exercise 3
    - Record the current path at EVERY node of the tree (the empty path
      is a subset too), not just at leaves

    Args:
        nums: List of integers (may contain duplicates)

    Returns:
        List of subsets (each a list), any order

    Example:
        >>> sorted(map(tuple, subsets_with_dupes([1, 2, 2])))
        [(), (1,), (1, 2), (1, 2, 2), (2,), (2, 2)]
    """
    # TODO: YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: N-Queens Solution Count
# =============================================================================

def count_n_queens(n):
    """
    Count the number of ways to place n non-attacking queens on an
    n x n chessboard.

    Template hints:
    - Place one queen per row (rows never conflict by construction)
    - Track occupied columns and diagonals in sets for O(1) checks:
          cols, diag1 (row - col), diag2 (row + col)
    - Prune BEFORE recursing; add to the sets when placing, remove after

    Args:
        n: Board size (and number of queens)

    Returns:
        Number of distinct solutions

    Example:
        >>> count_n_queens(4)
        2
        >>> count_n_queens(1)
        1
    """
    # TODO: YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 6: Validate a Sudoku Board
# =============================================================================

def is_valid_sudoku(board):
    """
    Check whether a 9x9 board breaks no Sudoku rule so far.

    Rules: each digit 1-9 may appear at most once in every row, every
    column, and every 3x3 box. Empty cells are fine.

    Args:
        board: 9x9 grid. Cells are either ints (0 means empty) or
               strings ('.' means empty, other cells '1'..'9')

    Returns:
        True if no rule is broken, False otherwise

    Example:
        >>> is_valid_sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0]] + [[0] * 9 for _ in range(8)])
        True
    """
    # TODO: YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 7: Word Search
# =============================================================================

def word_search(board, word):
    """
    Decide whether word can be traced through the letter grid by moving
    between horizontally/vertically adjacent cells. A cell may be used
    at most once per path.

    Template hints:
    - State: current (row, col) + index into word + visited set
    - Prune: out of bounds, already visited, or wrong letter
    - Visited-set discipline: add BEFORE recursing, remove AFTER
    - Try every cell as a starting point

    Args:
        board: 2D grid of single-character strings
        word: The word to find

    Returns:
        True if the word can be traced, False otherwise

    Example:
        >>> grid = [['A', 'B', 'C', 'E'],
        ...         ['S', 'F', 'C', 'S'],
        ...         ['A', 'D', 'E', 'E']]
        >>> word_search(grid, 'ABCCED')
        True
        >>> word_search(grid, 'ABCB')
        False
    """
    # TODO: YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 8: Permutations
# =============================================================================

def permute(nums):
    """
    Return every permutation of nums (all n! orderings).

    Template hints:
    - Choose one remaining element, recurse on what is left, unchoose
    - A clean way to track "remaining" is a second list you build by
      slicing: remaining[:i] + remaining[i + 1:]

    Args:
        nums: List of distinct elements

    Returns:
        List of permutations (each a list), any order

    Example:
        >>> sorted(map(tuple, permute([1, 2, 3])))
        [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    """
    # TODO: YOUR CODE HERE
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def test_generate_parentheses():
    """Test generate_parentheses."""
    print("Testing generate_parentheses...")

    tests = [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ]

    for n, expected in tests:
        result = sorted(generate_parentheses(n))
        assert result == expected, (
            f"generate_parentheses({n}) = {result}, expected {expected}")

    print("PASS All generate_parentheses tests passed!")


def test_combination_sum():
    """Test the reusable combination sum."""
    print("\nTesting combination_sum...")

    tests = [
        ([2, 3, 6, 7], 7, [(2, 2, 3), (7,)]),
        ([2, 3, 5], 8, [(2, 2, 2, 2), (2, 3, 3), (3, 5)]),
        ([2], 1, []),
        ([7, 3], 6, [(3, 3)]),
    ]

    for candidates, target, expected in tests:
        result = combination_sum(candidates, target)
        result_tuples = sorted(map(tuple, result))
        assert result_tuples == sorted(expected), (
            f"combination_sum({candidates}, {target}) = {result}, "
            f"expected {sorted(expected)}")

    print("PASS All combination_sum tests passed!")


def test_combination_sum_no_reuse():
    """Test the no-reuse combination sum with duplicate inputs."""
    print("\nTesting combination_sum_no_reuse...")

    tests = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [(1, 1, 6), (1, 2, 5), (1, 7), (2, 6)]),
        ([1, 1, 1], 2, [(1, 1)]),           # duplicates must not duplicate answers
        ([2, 5, 2, 1, 2], 5, [(1, 2, 2), (5,)]),
        ([1, 2], 4, []),                    # impossible target
    ]

    for candidates, target, expected in tests:
        result = combination_sum_no_reuse(candidates, target)
        result_tuples = sorted(map(tuple, result))
        assert result_tuples == sorted(expected), (
            f"combination_sum_no_reuse({candidates}, {target}) = {result}, "
            f"expected {sorted(expected)}")

    print("PASS All combination_sum_no_reuse tests passed!")


def test_subsets_with_dupes():
    """Test subsets with duplicates."""
    print("\nTesting subsets_with_dupes...")

    tests = [
        ([1, 2, 2], [(), (1,), (1, 2), (1, 2, 2), (2,), (2, 2)]),
        ([0], [(), (0,)]),
        ([5, 5, 5], [(), (5,), (5, 5), (5, 5, 5)]),
    ]

    for nums, expected in tests:
        result = subsets_with_dupes(nums)
        result_tuples = sorted(map(tuple, result))
        assert result_tuples == sorted(expected), (
            f"subsets_with_dupes({nums}) = {result}, expected {sorted(expected)}")

    print("PASS All subsets_with_dupes tests passed!")


def test_count_n_queens():
    """Test the N-Queens solution counter."""
    print("\nTesting count_n_queens...")

    tests = [
        (1, 1),
        (2, 0),
        (3, 0),
        (4, 2),
        (5, 10),
        (6, 4),
    ]

    for n, expected in tests:
        result = count_n_queens(n)
        assert result == expected, (
            f"count_n_queens({n}) = {result}, expected {expected}")

    print("PASS All count_n_queens tests passed!")


def test_is_valid_sudoku():
    """Test the Sudoku board validator."""
    print("\nTesting is_valid_sudoku...")

    solved = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]

    # A partially filled (valid) puzzle, with '.' for blanks
    puzzle_str = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]

    # Row duplicate: row 0 gets a second 5
    row_dup = [row[:] for row in solved]
    row_dup[0][8] = 5

    # Column duplicate: column 0 gets a second 5 (row 2, col 0 -> 5)
    col_dup = [row[:] for row in solved]
    col_dup[2][0] = 5

    # Box duplicate: top-left 3x3 box gets a second 5 (row 2, col 2 -> 5)
    box_dup = [row[:] for row in solved]
    box_dup[2][2] = 5

    assert is_valid_sudoku(solved) is True, "solved board should be valid"
    assert is_valid_sudoku(puzzle_str) is True, "puzzle with blanks should be valid"
    assert is_valid_sudoku(row_dup) is False, "duplicate in a row should fail"
    assert is_valid_sudoku(col_dup) is False, "duplicate in a column should fail"
    assert is_valid_sudoku(box_dup) is False, "duplicate in a 3x3 box should fail"

    print("PASS All is_valid_sudoku tests passed!")


def test_word_search():
    """Test word search."""
    print("\nTesting word_search...")

    grid = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
    ]

    assert word_search(grid, "ABCCED") is True, "ABCCED should be traceable"
    assert word_search(grid, "SEE") is True, "SEE should be traceable"
    assert word_search(grid, "ABCB") is False, "ABCB reuses the B at (0,1)"
    assert word_search(grid, "A") is True, "single letters exist"
    assert word_search(grid, "ZZZZ") is False, "Z is not on the board"

    print("PASS All word_search tests passed!")


def test_permute():
    """Test permutations."""
    print("\nTesting permute...")

    result = permute([1, 2, 3])
    expected = [(1, 2, 3), (1, 3, 2), (2, 1, 3),
                (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    assert sorted(map(tuple, result)) == expected, (
        f"permute([1, 2, 3]) = {result}, expected {expected}")

    result = permute([0, 1])
    assert sorted(map(tuple, result)) == [(0, 1), (1, 0)], (
        f"permute([0, 1]) = {result}")

    result = permute([7])
    assert result == [[7]], f"permute([7]) = {result}"

    print("PASS All permute tests passed!")


# =============================================================================
# SOLUTIONS (Hidden - Try to solve without looking!)
# =============================================================================

def _show_solutions():
    """Display solutions for all exercises."""
    solutions = '''
# =============================================================================
# SOLUTIONS
# =============================================================================

# Exercise 1: Generate Parentheses
def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
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


# Exercise 2: Combination Sum (Reusable)
def combination_sum(candidates, target):
    result = []
    candidates = sorted(candidates)

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result


# Exercise 3: Combination Sum (No Reuse, Duplicates in Input)
def combination_sum_no_reuse(candidates, target):
    result = []
    candidates = sorted(candidates)

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result


# Exercise 4: Subsets With Duplicates
def subsets_with_dupes(nums):
    result = []
    nums = sorted(nums)

    def backtrack(start, path):
        result.append(path[:])  # record at EVERY node, including the empty path
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


# Exercise 5: N-Queens Solution Count
def count_n_queens(n):
    cols = set()
    diag1 = set()  # keyed by row - col
    diag2 = set()  # keyed by row + col
    board = []
    count = 0

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if (col in cols or (row - col) in diag1
                    or (row + col) in diag2):
                continue
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
    return count


# Exercise 6: Validate a Sudoku Board
def is_valid_sudoku(board):
    def cell_value(value):
        # Accept both int boards (0 = empty) and string boards ('.' = empty)
        if value == 0 or value == '.':
            return None
        return value

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            value = cell_value(board[r][c])
            if value is None:
                continue
            b = (r // 3) * 3 + c // 3
            if value in rows[r] or value in cols[c] or value in boxes[b]:
                return False
            rows[r].add(value)
            cols[c].add(value)
            boxes[b].add(value)
    return True


# Exercise 7: Word Search
def word_search(board, word):
    rows, cols = len(board), len(board[0])
    visited = set()

    def backtrack(row, col, index):
        if index == len(word):
            return True
        if (row < 0 or row >= rows or col < 0 or col >= cols
                or (row, col) in visited
                or board[row][col] != word[index]):
            return False
        visited.add((row, col))
        found = (backtrack(row + 1, col, index + 1) or
                 backtrack(row - 1, col, index + 1) or
                 backtrack(row, col + 1, index + 1) or
                 backtrack(row, col - 1, index + 1))
        visited.remove((row, col))
        return found

    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, 0):
                return True
    return False


# Exercise 8: Permutations
def permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i + 1:])
            path.pop()

    backtrack([], list(nums))
    return result
'''
    print(solutions)


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--solutions":
        _show_solutions()
    else:
        print("=" * 60)
        print("BACKTRACKING - EXERCISES")
        print("=" * 60)
        print("\nImplement each function and run this file to test.")
        print("Use 'python exercises.py --solutions' to see solutions.\n")

        try:
            test_generate_parentheses()
        except (AssertionError, TypeError) as e:
            print(f"FAIL generate_parentheses: {e}")

        try:
            test_combination_sum()
        except (AssertionError, TypeError) as e:
            print(f"FAIL combination_sum: {e}")

        try:
            test_combination_sum_no_reuse()
        except (AssertionError, TypeError) as e:
            print(f"FAIL combination_sum_no_reuse: {e}")

        try:
            test_subsets_with_dupes()
        except (AssertionError, TypeError) as e:
            print(f"FAIL subsets_with_dupes: {e}")

        try:
            test_count_n_queens()
        except (AssertionError, TypeError) as e:
            print(f"FAIL count_n_queens: {e}")

        try:
            test_is_valid_sudoku()
        except (AssertionError, TypeError) as e:
            print(f"FAIL is_valid_sudoku: {e}")

        try:
            test_word_search()
        except (AssertionError, TypeError) as e:
            print(f"FAIL word_search: {e}")

        try:
            test_permute()
        except (AssertionError, TypeError) as e:
            print(f"FAIL permute: {e}")

        print("\n" + "=" * 60)
        print("Testing complete!")
        print("=" * 60)
