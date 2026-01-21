"""
Dynamic Programming - Examples

This file demonstrates dynamic programming techniques with
classic problems and detailed explanations.

Run this file to see the examples in action:
    python examples.py
"""

from functools import lru_cache


# =============================================================================
# FIBONACCI - THE CLASSIC DP EXAMPLE
# =============================================================================

def fib_naive(n):
    """
    Naive recursive Fibonacci - O(2^n) time!
    
    This is SLOW because it recalculates the same values many times.
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memoization(n, memo=None):
    """
    Top-down DP with memoization - O(n) time, O(n) space.
    
    Cache results to avoid redundant calculations.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]


def fib_tabulation(n):
    """
    Bottom-up DP with tabulation - O(n) time, O(n) space.
    
    Build solution iteratively from smallest subproblems.
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fib_optimized(n):
    """
    Space-optimized DP - O(n) time, O(1) space.
    
    Only keep track of the last two values.
    """
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    
    return prev1


# =============================================================================
# CLIMBING STAIRS
# =============================================================================

def climb_stairs(n):
    """
    How many distinct ways to climb n stairs (1 or 2 steps at a time)?
    
    dp[i] = number of ways to reach step i
    dp[i] = dp[i-1] + dp[i-2]  (from 1 step below OR 2 steps below)
    
    Time: O(n), Space: O(n)
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1  # 1 way to reach step 1: (1)
    dp[2] = 2  # 2 ways to reach step 2: (1,1) or (2)
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def climb_stairs_k_steps(n, k):
    """
    Climb n stairs with 1 to k steps at a time.
    
    dp[i] = sum of dp[i-1] + dp[i-2] + ... + dp[i-k]
    """
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to stay at ground level
    
    for i in range(1, n + 1):
        for j in range(1, min(k, i) + 1):
            dp[i] += dp[i - j]
    
    return dp[n]


# =============================================================================
# COIN CHANGE PROBLEMS
# =============================================================================

def coin_change_min_coins(coins, amount):
    """
    Minimum number of coins needed to make amount.
    
    dp[i] = minimum coins needed for amount i
    dp[i] = min(dp[i], dp[i - coin] + 1) for each coin
    
    Time: O(amount * len(coins)), Space: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_count_ways(coins, amount):
    """
    Count number of ways to make amount using coins.
    
    dp[i] = number of ways to make amount i
    
    Time: O(amount * len(coins)), Space: O(amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1  # 1 way to make amount 0: use no coins
    
    # Process each coin
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]


# =============================================================================
# LONGEST COMMON SUBSEQUENCE (LCS)
# =============================================================================

def lcs_length(text1, text2):
    """
    Find length of longest common subsequence.
    
    dp[i][j] = LCS length of text1[0:i] and text2[0:j]
    
    If text1[i-1] == text2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1  (extend LCS)
    Else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (skip one char)
    
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def lcs_string(text1, text2):
    """
    Find the actual longest common subsequence string.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))


# =============================================================================
# KNAPSACK PROBLEM
# =============================================================================

def knapsack_01(weights, values, capacity):
    """
    0/1 Knapsack: Maximize value with weight capacity.
    Each item can be used at most once.
    
    dp[i][w] = max value using first i items with capacity w
    
    Time: O(n * capacity), Space: O(n * capacity)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i - 1][w]
            
            # Take item i (if it fits)
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
    
    return dp[n][capacity]


def knapsack_01_optimized(weights, values, capacity):
    """
    Space-optimized 0/1 Knapsack using 1D array.
    
    Time: O(n * capacity), Space: O(capacity)
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Traverse backwards to avoid using same item twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]


def knapsack_unbounded(weights, values, capacity):
    """
    Unbounded Knapsack: Each item can be used multiple times.
    
    Time: O(n * capacity), Space: O(capacity)
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]


# =============================================================================
# LONGEST INCREASING SUBSEQUENCE (LIS)
# =============================================================================

def lis_dp(nums):
    """
    Find length of longest strictly increasing subsequence.
    
    dp[i] = length of LIS ending at index i
    dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
    
    Time: O(n²), Space: O(n)
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # Every element is a subsequence of length 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def lis_binary_search(nums):
    """
    Optimized LIS using binary search.
    
    Time: O(n log n), Space: O(n)
    """
    if not nums:
        return 0
    
    # tails[i] = smallest ending element for LIS of length i+1
    tails = []
    
    for num in nums:
        # Binary search for position
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)


# =============================================================================
# EDIT DISTANCE (LEVENSHTEIN DISTANCE)
# =============================================================================

def edit_distance(word1, word2):
    """
    Minimum operations (insert, delete, replace) to convert word1 to word2.
    
    dp[i][j] = min edits to convert word1[0:i] to word2[0:j]
    
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete from word1
                    dp[i][j - 1],      # Insert into word1
                    dp[i - 1][j - 1]   # Replace in word1
                )
    
    return dp[m][n]


# =============================================================================
# MAXIMUM SUBARRAY (KADANE'S ALGORITHM)
# =============================================================================

def max_subarray(nums):
    """
    Find contiguous subarray with maximum sum.
    
    dp[i] = max sum ending at index i
    dp[i] = max(nums[i], dp[i-1] + nums[i])
    
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Either start fresh or extend previous subarray
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# =============================================================================
# HOUSE ROBBER
# =============================================================================

def house_robber(nums):
    """
    Maximum money from non-adjacent houses.
    
    dp[i] = max money from houses 0 to i
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr
    
    return prev1


# =============================================================================
# UNIQUE PATHS IN GRID
# =============================================================================

def unique_paths(m, n):
    """
    Count unique paths from top-left to bottom-right in m×n grid.
    Can only move right or down.
    
    dp[i][j] = number of paths to cell (i, j)
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    Time: O(m*n), Space: O(n)
    """
    dp = [1] * n  # First row is all 1s
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]
    
    return dp[n - 1]


def unique_paths_with_obstacles(grid):
    """
    Count unique paths avoiding obstacles (1 = obstacle, 0 = clear).
    """
    if not grid or grid[0][0] == 1:
        return 0
    
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] = dp[j] + dp[j - 1]
    
    return dp[n - 1]


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_fibonacci():
    """Compare Fibonacci implementations."""
    print("=" * 60)
    print("FIBONACCI COMPARISON")
    print("=" * 60)
    
    import time
    
    # First 10 Fibonacci numbers
    print("\nFirst 10 Fibonacci numbers:")
    fibs = [fib_optimized(i) for i in range(10)]
    print(f"  {fibs}")
    
    # Performance comparison
    print("\nPerformance for F(30):")
    
    # Memoization
    start = time.perf_counter()
    result = fib_memoization(30)
    memo_time = time.perf_counter() - start
    print(f"  Memoization: F(30) = {result}, Time: {memo_time:.6f}s")
    
    # Tabulation
    start = time.perf_counter()
    result = fib_tabulation(30)
    tab_time = time.perf_counter() - start
    print(f"  Tabulation:  F(30) = {result}, Time: {tab_time:.6f}s")
    
    # Optimized
    start = time.perf_counter()
    result = fib_optimized(30)
    opt_time = time.perf_counter() - start
    print(f"  Optimized:   F(30) = {result}, Time: {opt_time:.6f}s")
    
    print("\n  Note: Naive recursive would take ~0.3 seconds for F(30)!")


def demo_climbing_stairs():
    """Demonstrate climbing stairs problem."""
    print("\n" + "=" * 60)
    print("CLIMBING STAIRS")
    print("=" * 60)
    
    print("\nWays to climb n stairs (1 or 2 steps at a time):")
    for n in range(1, 8):
        ways = climb_stairs(n)
        print(f"  n={n}: {ways} ways")
    
    print("\nWith up to 3 steps at a time (n=5):")
    print(f"  {climb_stairs_k_steps(5, 3)} ways")


def demo_coin_change():
    """Demonstrate coin change problems."""
    print("\n" + "=" * 60)
    print("COIN CHANGE")
    print("=" * 60)
    
    coins = [1, 5, 10, 25]
    amount = 67
    
    print(f"\nCoins: {coins}")
    print(f"Amount: {amount}")
    
    min_coins = coin_change_min_coins(coins, amount)
    print(f"\n1. Minimum coins needed: {min_coins}")
    
    ways = coin_change_count_ways(coins, amount)
    print(f"2. Number of ways: {ways}")
    
    # Smaller example for visualization
    print("\nSmaller example - amount=11 with coins [1, 5, 6]:")
    print(f"  Minimum coins: {coin_change_min_coins([1, 5, 6], 11)}")
    print("  Optimal: 6 + 5 = 11 (2 coins)")


def demo_lcs():
    """Demonstrate Longest Common Subsequence."""
    print("\n" + "=" * 60)
    print("LONGEST COMMON SUBSEQUENCE")
    print("=" * 60)
    
    pairs = [
        ("ABCDGH", "AEDFHR"),
        ("AGGTAB", "GXTXAYB"),
        ("ABC", "AC"),
    ]
    
    for text1, text2 in pairs:
        length = lcs_length(text1, text2)
        lcs = lcs_string(text1, text2)
        print(f"\n  '{text1}' and '{text2}'")
        print(f"  LCS: '{lcs}' (length {length})")


def demo_knapsack():
    """Demonstrate Knapsack problem."""
    print("\n" + "=" * 60)
    print("KNAPSACK PROBLEM")
    print("=" * 60)
    
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    
    print(f"\nItems:")
    for i, (w, v) in enumerate(zip(weights, values)):
        print(f"  Item {i+1}: weight={w}, value={v}")
    print(f"Capacity: {capacity}")
    
    max_value = knapsack_01(weights, values, capacity)
    print(f"\n0/1 Knapsack maximum value: {max_value}")
    
    max_value_unbounded = knapsack_unbounded(weights, values, capacity)
    print(f"Unbounded Knapsack maximum value: {max_value_unbounded}")


def demo_lis():
    """Demonstrate Longest Increasing Subsequence."""
    print("\n" + "=" * 60)
    print("LONGEST INCREASING SUBSEQUENCE")
    print("=" * 60)
    
    arrays = [
        [10, 22, 9, 33, 21, 50, 41, 60],
        [3, 10, 2, 1, 20],
        [50, 3, 10, 7, 40, 80],
    ]
    
    for arr in arrays:
        length = lis_dp(arr)
        print(f"\n  Array: {arr}")
        print(f"  LIS length: {length}")


def demo_edit_distance():
    """Demonstrate Edit Distance."""
    print("\n" + "=" * 60)
    print("EDIT DISTANCE")
    print("=" * 60)
    
    pairs = [
        ("kitten", "sitting"),
        ("horse", "ros"),
        ("intention", "execution"),
    ]
    
    for word1, word2 in pairs:
        dist = edit_distance(word1, word2)
        print(f"\n  '{word1}' → '{word2}'")
        print(f"  Edit distance: {dist}")


def demo_max_subarray():
    """Demonstrate Maximum Subarray."""
    print("\n" + "=" * 60)
    print("MAXIMUM SUBARRAY (KADANE'S ALGORITHM)")
    print("=" * 60)
    
    arrays = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
    ]
    
    for arr in arrays:
        max_sum = max_subarray(arr)
        print(f"\n  Array: {arr}")
        print(f"  Maximum subarray sum: {max_sum}")


def demo_house_robber():
    """Demonstrate House Robber."""
    print("\n" + "=" * 60)
    print("HOUSE ROBBER")
    print("=" * 60)
    
    cases = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2, 1, 1, 2],
    ]
    
    for houses in cases:
        max_money = house_robber(houses)
        print(f"\n  Houses: {houses}")
        print(f"  Maximum money: {max_money}")


def demo_unique_paths():
    """Demonstrate Unique Paths."""
    print("\n" + "=" * 60)
    print("UNIQUE PATHS IN GRID")
    print("=" * 60)
    
    grids = [(3, 7), (3, 3), (7, 3)]
    
    print("\nUnique paths without obstacles:")
    for m, n in grids:
        paths = unique_paths(m, n)
        print(f"  {m}×{n} grid: {paths} paths")
    
    print("\nWith obstacles:")
    obstacle_grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(f"  Grid:")
    for row in obstacle_grid:
        print(f"    {row}")
    paths = unique_paths_with_obstacles(obstacle_grid)
    print(f"  Unique paths: {paths}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    demo_fibonacci()
    demo_climbing_stairs()
    demo_coin_change()
    demo_lcs()
    demo_knapsack()
    demo_lis()
    demo_edit_distance()
    demo_max_subarray()
    demo_house_robber()
    demo_unique_paths()
    
    print("\n" + "=" * 60)
    print("✓ All dynamic programming examples completed!")
    print("=" * 60)
