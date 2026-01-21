# 📝 Dynamic Programming

> Optimizing recursive solutions by storing and reusing computed results

---

## 📋 Table of Contents

1. [What is Dynamic Programming?](#what-is-dynamic-programming)
2. [Key Properties](#key-properties)
3. [Two Approaches](#two-approaches)
4. [Classic Problems](#classic-problems)
5. [How to Identify DP Problems](#how-to-identify-dp-problems)
6. [Problem-Solving Framework](#problem-solving-framework)
7. [Common Patterns](#common-patterns)

---

## What is Dynamic Programming?

Dynamic Programming (DP) is an optimization technique that solves complex problems by:

1. Breaking them into **smaller subproblems**
2. Solving each subproblem **only once**
3. **Storing** the results to avoid redundant calculations

> "Those who cannot remember the past are condemned to repeat it." — George Santayana

### The Core Idea

Instead of recalculating the same thing multiple times, **remember** what you've already computed.

### Example: Fibonacci Numbers

**Naive Recursion (Slow):**
```python
def fib(n):  # O(2^n) time!
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

**With Dynamic Programming (Fast):**
```python
def fib_dp(n):  # O(n) time!
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

The DP version is **exponentially faster** because it calculates each Fibonacci number exactly once.

---

## Key Properties

A problem can be solved with DP if it has these two properties:

### 1. Overlapping Subproblems

The same smaller problems are solved multiple times.

```
fib(5)
├── fib(4)
│   ├── fib(3)     ← Calculated once here
│   └── fib(2)     ← Calculated once here
└── fib(3)         ← Same as above! Redundant!
    ├── fib(2)     ← Same as above! Redundant!
    └── fib(1)
```

### 2. Optimal Substructure

The optimal solution to the problem can be constructed from optimal solutions of its subproblems.

```
fib(n) = fib(n-1) + fib(n-2)
```

The solution to `fib(n)` depends directly on solutions to `fib(n-1)` and `fib(n-2)`.

---

## Two Approaches

### 1. Top-Down (Memoization)

Start with the original problem and recursively break it down, caching results.

```python
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]  # Return cached result
    
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

**Pros:**
- Natural translation from recursion
- Only computes what's needed

**Cons:**
- Recursion overhead
- Stack limit for deep recursion

### 2. Bottom-Up (Tabulation)

Start with the smallest subproblems and build up to the original.

```python
def fib_tab(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

**Pros:**
- No recursion overhead
- Often cache-friendly

**Cons:**
- May compute unnecessary values
- Requires understanding the order of subproblems

### Space Optimization

Often we only need a few previous values:

```python
def fib_optimized(n):
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    
    return prev1
```

This reduces space from O(n) to O(1)!

---

## Classic Problems

### 1. Climbing Stairs

You can climb 1 or 2 steps at a time. How many ways to reach step n?

```python
def climb_stairs(n):
    """
    dp[i] = number of ways to reach step i
    dp[i] = dp[i-1] + dp[i-2]  (come from 1 or 2 steps below)
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

### 2. Coin Change

Minimum coins needed to make amount, given coin denominations.

```python
def coin_change(coins, amount):
    """
    dp[i] = minimum coins needed for amount i
    dp[i] = min(dp[i], dp[i - coin] + 1) for each coin
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

### 3. Longest Common Subsequence (LCS)

Find the longest subsequence common to two strings.

```python
def lcs(text1, text2):
    """
    dp[i][j] = LCS length of text1[0:i] and text2[0:j]
    
    If text1[i-1] == text2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
    Else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

### 4. 0/1 Knapsack

Maximize value with limited weight capacity.

```python
def knapsack(weights, values, capacity):
    """
    dp[i][w] = max value using first i items with weight limit w
    
    If we can include item i (weight[i] <= w):
        dp[i][w] = max(
            dp[i-1][w],                    # Don't take item
            dp[i-1][w-weight[i]] + value[i] # Take item
        )
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            
            # Take item i (if it fits)
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i-1][w - weights[i-1]] + values[i-1]
                )
    
    return dp[n][capacity]
```

### 5. Longest Increasing Subsequence (LIS)

Find the length of the longest strictly increasing subsequence.

```python
def lis(nums):
    """
    dp[i] = length of LIS ending at index i
    dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
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
```

---

## How to Identify DP Problems

### Look for These Clues

1. **"Count the number of ways..."**
2. **"Find the minimum/maximum..."**
3. **"Is it possible to..."**
4. **"Find the longest/shortest..."**
5. **Optimal choice depends on previous choices**
6. **Problem can be broken into similar subproblems**

### Common DP Categories

| Category | Examples |
|----------|----------|
| Sequence | Fibonacci, Climbing Stairs, House Robber |
| Two Sequences | LCS, Edit Distance |
| Grid | Unique Paths, Minimum Path Sum |
| Knapsack | 0/1 Knapsack, Coin Change, Subset Sum |
| String | Palindrome, Word Break |
| Tree | Tree DP, Binary Tree Maximum Path Sum |
| Interval | Matrix Chain Multiplication |

---

## Problem-Solving Framework

### Step 1: Define the State

What information do you need to answer the subproblem?

> "What does `dp[i]` represent?"

Examples:
- `dp[i]` = min cost to reach position i
- `dp[i][j]` = LCS length of first i and j characters
- `dp[i][w]` = max value with first i items and capacity w

### Step 2: Find the Recurrence Relation

How does the current state relate to previous states?

> "How do I build `dp[i]` from smaller subproblems?"

### Step 3: Identify Base Cases

What are the simplest subproblems with known answers?

> "What is `dp[0]`? `dp[1]`?"

### Step 4: Determine Computation Order

Which subproblems must be solved first?

> "Do I iterate forward or backward? 1D or 2D?"

### Step 5: Optimize Space (if needed)

Can you reduce the space complexity?

> "Do I need the entire table or just the last row?"

---

## Common Patterns

### Pattern 1: Linear DP

```python
# dp[i] depends on dp[i-1], dp[i-2], etc.
dp = [0] * n
dp[0] = base_case

for i in range(1, n):
    dp[i] = f(dp[i-1], dp[i-2], ...)
```

### Pattern 2: 2D Grid DP

```python
# dp[i][j] depends on dp[i-1][j], dp[i][j-1], etc.
dp = [[0] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        dp[i][j] = f(dp[i-1][j], dp[i][j-1], ...)
```

### Pattern 3: Knapsack Pattern

```python
# Choose or don't choose each item
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacity + 1):
        # Don't take item i
        dp[i][w] = dp[i-1][w]
        # Take item i (if possible)
        if items[i-1].weight <= w:
            dp[i][w] = max(dp[i][w], dp[i-1][w - items[i-1].weight] + items[i-1].value)
```

### Pattern 4: Interval DP

```python
# Solve for all intervals of increasing length
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = f(all splits between i and j)
```

---

## 🔑 Key Takeaways

1. **DP = Recursion + Memoization** — avoid redundant work
2. **Two approaches**: Top-down (memoization) vs Bottom-up (tabulation)
3. **Identify the state**: What information defines a subproblem?
4. **Find the recurrence**: How to build solutions from subproblems
5. **Start with brute force**, then optimize with DP
6. **Practice patterns** — most DP problems follow common templates

---

## 🔗 Next Steps

- Practice with [`exercises.py`](exercises.py)
- Test your knowledge with [`quiz.md`](quiz.md)
- Move on to [05_greedy_algorithms](../05_greedy_algorithms/)
