"""
Dynamic Programming - Exercises

Practice implementing dynamic programming solutions.
Complete each exercise by filling in the function body.

Run tests with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Fibonacci (Memoization)
# =============================================================================

def exercise_1_fib_memo(n, memo=None):
    """
    Calculate nth Fibonacci number using memoization (top-down DP).
    
    Args:
        n: Non-negative integer
        memo: Dictionary for caching results
        
    Returns:
        int: The nth Fibonacci number
        
    Example:
        >>> exercise_1_fib_memo(10)
        55
    """
    if memo is None:
        memo = {}
    
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Fibonacci (Tabulation)
# =============================================================================

def exercise_2_fib_tab(n):
    """
    Calculate nth Fibonacci number using tabulation (bottom-up DP).
    
    Args:
        n: Non-negative integer
        
    Returns:
        int: The nth Fibonacci number
        
    Example:
        >>> exercise_2_fib_tab(10)
        55
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Climbing Stairs
# =============================================================================

def exercise_3_climb_stairs(n):
    """
    Count distinct ways to climb n stairs (1 or 2 steps at a time).
    
    Args:
        n: Number of stairs
        
    Returns:
        int: Number of distinct ways
        
    Example:
        >>> exercise_3_climb_stairs(5)
        8
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Coin Change (Minimum Coins)
# =============================================================================

def exercise_4_coin_change(coins, amount):
    """
    Find minimum number of coins needed to make amount.
    Return -1 if amount cannot be made.
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        
    Returns:
        int: Minimum coins needed, or -1 if impossible
        
    Example:
        >>> exercise_4_coin_change([1, 5, 10, 25], 67)
        7
        >>> exercise_4_coin_change([2], 3)
        -1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Maximum Subarray Sum (Kadane's Algorithm)
# =============================================================================

def exercise_5_max_subarray(nums):
    """
    Find the contiguous subarray with the maximum sum.
    
    Args:
        nums: List of integers (can be negative)
        
    Returns:
        int: Maximum subarray sum
        
    Example:
        >>> exercise_5_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6  # [4, -1, 2, 1]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 6: House Robber
# =============================================================================

def exercise_6_house_robber(nums):
    """
    Maximum money from non-adjacent houses.
    You cannot rob two adjacent houses.
    
    Args:
        nums: List of money in each house
        
    Returns:
        int: Maximum money you can rob
        
    Example:
        >>> exercise_6_house_robber([2, 7, 9, 3, 1])
        12  # Rob houses 0, 2, 4: 2 + 9 + 1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 7: Unique Paths
# =============================================================================

def exercise_7_unique_paths(m, n):
    """
    Count unique paths from top-left to bottom-right in m×n grid.
    Can only move right or down.
    
    Args:
        m: Number of rows
        n: Number of columns
        
    Returns:
        int: Number of unique paths
        
    Example:
        >>> exercise_7_unique_paths(3, 7)
        28
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 8: Longest Common Subsequence
# =============================================================================

def exercise_8_lcs(text1, text2):
    """
    Find length of longest common subsequence of two strings.
    
    Args:
        text1: First string
        text2: Second string
        
    Returns:
        int: Length of LCS
        
    Example:
        >>> exercise_8_lcs("abcde", "ace")
        3  # "ace"
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 9: 0/1 Knapsack
# =============================================================================

def exercise_9_knapsack(weights, values, capacity):
    """
    Maximize value while staying within weight capacity.
    Each item can be used at most once.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
        
    Returns:
        int: Maximum value achievable
        
    Example:
        >>> exercise_9_knapsack([2, 3, 4, 5], [3, 4, 5, 6], 8)
        10
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 10: Longest Increasing Subsequence
# =============================================================================

def exercise_10_lis(nums):
    """
    Find length of longest strictly increasing subsequence.
    
    Args:
        nums: List of integers
        
    Returns:
        int: Length of LIS
        
    Example:
        >>> exercise_10_lis([10, 9, 2, 5, 3, 7, 101, 18])
        4  # [2, 3, 7, 101] or [2, 5, 7, 101]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 11: Edit Distance
# =============================================================================

def exercise_11_edit_distance(word1, word2):
    """
    Minimum operations (insert, delete, replace) to convert word1 to word2.
    
    Args:
        word1: Source string
        word2: Target string
        
    Returns:
        int: Minimum edit operations
        
    Example:
        >>> exercise_11_edit_distance("horse", "ros")
        3
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 12: Coin Change (Count Ways)
# =============================================================================

def exercise_12_coin_ways(coins, amount):
    """
    Count number of ways to make amount using given coins.
    Each coin can be used unlimited times.
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        
    Returns:
        int: Number of ways
        
    Example:
        >>> exercise_12_coin_ways([1, 2, 5], 5)
        4  # (5), (2+2+1), (2+1+1+1), (1+1+1+1+1)
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# BONUS: Palindrome Partitioning (Minimum Cuts)
# =============================================================================

def bonus_min_cuts(s):
    """
    BONUS: Minimum cuts needed to partition string into palindromes.
    
    Args:
        s: Input string
        
    Returns:
        int: Minimum cuts
        
    Example:
        >>> bonus_min_cuts("aab")
        1  # ["aa", "b"]
        >>> bonus_min_cuts("a")
        0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests():
    """Run all test cases."""
    print("Running Dynamic Programming Exercises Tests")
    print("=" * 50)
    
    all_passed = True
    
    # Test Exercise 1: Fibonacci (Memoization)
    print("\nExercise 1: Fibonacci (Memoization)")
    tests_1 = [
        (0, 0),
        (1, 1),
        (10, 55),
        (20, 6765),
    ]
    for n, expected in tests_1:
        result = exercise_1_fib_memo(n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} fib_memo({n}) = {result} (expected {expected})")
    
    # Test Exercise 2: Fibonacci (Tabulation)
    print("\nExercise 2: Fibonacci (Tabulation)")
    tests_2 = [
        (0, 0),
        (1, 1),
        (10, 55),
        (30, 832040),
    ]
    for n, expected in tests_2:
        result = exercise_2_fib_tab(n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} fib_tab({n}) = {result} (expected {expected})")
    
    # Test Exercise 3: Climbing Stairs
    print("\nExercise 3: Climbing Stairs")
    tests_3 = [
        (1, 1),
        (2, 2),
        (5, 8),
        (10, 89),
    ]
    for n, expected in tests_3:
        result = exercise_3_climb_stairs(n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} climb_stairs({n}) = {result} (expected {expected})")
    
    # Test Exercise 4: Coin Change
    print("\nExercise 4: Coin Change (Minimum)")
    tests_4 = [
        ([1, 5, 10, 25], 67, 7),
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]
    for coins, amount, expected in tests_4:
        result = exercise_4_coin_change(coins, amount)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} coin_change({coins}, {amount}) = {result} (expected {expected})")
    
    # Test Exercise 5: Maximum Subarray
    print("\nExercise 5: Maximum Subarray")
    tests_5 = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1, -2, -3], -1),
    ]
    for nums, expected in tests_5:
        result = exercise_5_max_subarray(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} max_subarray({nums}) = {result} (expected {expected})")
    
    # Test Exercise 6: House Robber
    print("\nExercise 6: House Robber")
    tests_6 = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([], 0),
    ]
    for nums, expected in tests_6:
        result = exercise_6_house_robber(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} house_robber({nums}) = {result} (expected {expected})")
    
    # Test Exercise 7: Unique Paths
    print("\nExercise 7: Unique Paths")
    tests_7 = [
        (3, 7, 28),
        (3, 2, 3),
        (1, 1, 1),
        (3, 3, 6),
    ]
    for m, n, expected in tests_7:
        result = exercise_7_unique_paths(m, n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} unique_paths({m}, {n}) = {result} (expected {expected})")
    
    # Test Exercise 8: LCS
    print("\nExercise 8: Longest Common Subsequence")
    tests_8 = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "abc", 0),
    ]
    for t1, t2, expected in tests_8:
        result = exercise_8_lcs(t1, t2)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} lcs('{t1}', '{t2}') = {result} (expected {expected})")
    
    # Test Exercise 9: Knapsack
    print("\nExercise 9: 0/1 Knapsack")
    tests_9 = [
        ([2, 3, 4, 5], [3, 4, 5, 6], 8, 10),
        ([1, 2, 3], [10, 15, 40], 6, 65),
        ([10], [100], 5, 0),
    ]
    for weights, values, cap, expected in tests_9:
        result = exercise_9_knapsack(weights, values, cap)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} knapsack(..., {cap}) = {result} (expected {expected})")
    
    # Test Exercise 10: LIS
    print("\nExercise 10: Longest Increasing Subsequence")
    tests_10 = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
    ]
    for nums, expected in tests_10:
        result = exercise_10_lis(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} lis({nums}) = {result} (expected {expected})")
    
    # Test Exercise 11: Edit Distance
    print("\nExercise 11: Edit Distance")
    tests_11 = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "abc", 3),
        ("abc", "abc", 0),
    ]
    for w1, w2, expected in tests_11:
        result = exercise_11_edit_distance(w1, w2)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} edit_distance('{w1}', '{w2}') = {result} (expected {expected})")
    
    # Test Exercise 12: Coin Ways
    print("\nExercise 12: Coin Change (Count Ways)")
    tests_12 = [
        ([1, 2, 5], 5, 4),
        ([2], 3, 0),
        ([1], 0, 1),
        ([1, 2], 3, 2),
    ]
    for coins, amount, expected in tests_12:
        result = exercise_12_coin_ways(coins, amount)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} coin_ways({coins}, {amount}) = {result} (expected {expected})")
    
    # Test Bonus: Palindrome Partitioning
    print("\nBonus: Palindrome Partitioning")
    tests_bonus = [
        ("aab", 1),
        ("a", 0),
        ("ab", 1),
        ("aaa", 0),
    ]
    for s, expected in tests_bonus:
        result = bonus_min_cuts(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} min_cuts('{s}') = {result} (expected {expected})")
    
    # Summary
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


# =============================================================================
# SOLUTIONS (Hidden - Try to solve on your own first!)
# =============================================================================

"""
SOLUTIONS - Scroll down only after attempting the exercises!

.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

# Exercise 1: Fibonacci (Memoization)
def exercise_1_fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = exercise_1_fib_memo(n - 1, memo) + exercise_1_fib_memo(n - 2, memo)
    return memo[n]

# Exercise 2: Fibonacci (Tabulation)
def exercise_2_fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Exercise 3: Climbing Stairs
def exercise_3_climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1

# Exercise 4: Coin Change
def exercise_4_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Exercise 5: Maximum Subarray
def exercise_5_max_subarray(nums):
    if not nums:
        return 0
    max_sum = current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

# Exercise 6: House Robber
def exercise_6_house_robber(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums) if nums else 0
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr
    return prev1

# Exercise 7: Unique Paths
def exercise_7_unique_paths(m, n):
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]
    return dp[n - 1]

# Exercise 8: LCS
def exercise_8_lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# Exercise 9: Knapsack
def exercise_9_knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

# Exercise 10: LIS
def exercise_10_lis(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Exercise 11: Edit Distance
def exercise_11_edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

# Exercise 12: Coin Ways
def exercise_12_coin_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

# Bonus: Palindrome Partitioning
def bonus_min_cuts(s):
    n = len(s)
    if n <= 1:
        return 0
    
    # is_palindrome[i][j] = True if s[i:j+1] is palindrome
    is_palindrome = [[False] * n for _ in range(n)]
    for i in range(n):
        is_palindrome[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                is_palindrome[i][j] = (s[i] == s[j])
            else:
                is_palindrome[i][j] = (s[i] == s[j] and is_palindrome[i + 1][j - 1])
    
    # dp[i] = min cuts for s[0:i+1]
    dp = [0] * n
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            dp[i] = i  # Worst case: cut after each character
            for j in range(1, i + 1):
                if is_palindrome[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
    
    return dp[n - 1]
"""


if __name__ == "__main__":
    run_tests()
