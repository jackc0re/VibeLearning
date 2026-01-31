# 🧠 Dynamic Programming Quiz

Test your understanding of dynamic programming!

---

## Question 1: Core Concept

What is the main advantage of dynamic programming over naive recursion?

- A) DP uses less code
- B) DP avoids recalculating the same subproblems
- C) DP is always faster
- D) DP doesn't use recursion

<details>
<summary>Show Answer</summary>

**B) DP avoids recalculating the same subproblems**

Dynamic programming stores (memoizes) the results of subproblems so each subproblem is solved only once, avoiding exponential redundant calculations.

</details>

---

## Question 2: Key Properties

Which TWO properties must a problem have to be solvable with DP?

- A) Overlapping subproblems and optimal substructure
- B) Sorted input and binary search capability
- C) Linear structure and constant time operations
- D) Fixed size and deterministic output

<details>
<summary>Show Answer</summary>

**A) Overlapping subproblems and optimal substructure**

- **Overlapping subproblems**: Same subproblems are solved multiple times
- **Optimal substructure**: Optimal solution to the problem can be constructed from optimal solutions of its subproblems

</details>

---

## Question 3: Approaches

What is the difference between memoization and tabulation?

- A) Memoization is bottom-up, tabulation is top-down
- B) Memoization is top-down with caching, tabulation is bottom-up with iteration
- C) They are the same thing
- D) Memoization uses arrays, tabulation uses hash maps

<details>
<summary>Show Answer</summary>

**B) Memoization is top-down with caching, tabulation is bottom-up with iteration**

- **Memoization (top-down)**: Start with the original problem, recursively break down, cache results
- **Tabulation (bottom-up)**: Start with smallest subproblems, iteratively build up to the solution

</details>

---

## Question 4: Fibonacci Analysis

What is the time complexity of the naive recursive Fibonacci vs DP Fibonacci?

- A) Both are O(n)
- B) Naive: O(n), DP: O(n log n)
- C) Naive: O(2^n), DP: O(n)
- D) Naive: O(n²), DP: O(n)

<details>
<summary>Show Answer</summary>

**C) Naive: O(2^n), DP: O(n)**

- **Naive recursion**: Each call branches into two calls, creating an exponential tree
- **DP**: Each Fibonacci number is computed exactly once

For F(40):
- Naive: ~1 billion operations
- DP: 40 operations

</details>

---

## Question 5: DP Array Meaning

In the climbing stairs problem, what does `dp[i]` represent?

```python
dp[i] = dp[i-1] + dp[i-2]
```

- A) The number of steps remaining
- B) The number of ways to reach step i
- C) The minimum steps to reach step i
- D) The maximum height at step i

<details>
<summary>Show Answer</summary>

**B) The number of ways to reach step i**

You can reach step i either from step i-1 (taking 1 step) or from step i-2 (taking 2 steps). So the total ways = ways to reach (i-1) + ways to reach (i-2).

</details>

---

## Question 6: Coin Change

For coin change with coins [1, 3, 4] and amount 6, what is the minimum number of coins?

- A) 2 (3+3)
- B) 3 (4+1+1)
- C) 6 (1+1+1+1+1+1)
- D) 2 (4+1+1)

<details>
<summary>Show Answer</summary>

**A) 2 (3+3)**

The optimal solution uses two 3-cent coins: 3 + 3 = 6.

Dynamic programming builds up:
- dp[0] = 0
- dp[1] = 1 (1)
- dp[2] = 2 (1+1)
- dp[3] = 1 (3)
- dp[4] = 1 (4)
- dp[5] = 2 (4+1)
- dp[6] = 2 (3+3)

</details>

---

## Question 7: State Definition

In the 0/1 Knapsack problem, what does `dp[i][w]` typically represent?

- A) Weight of first i items
- B) Maximum value using first i items with capacity w
- C) Number of items with weight w
- D) Minimum weight needed for value w

<details>
<summary>Show Answer</summary>

**B) Maximum value using first i items with capacity w**

The recurrence relation:
- If we don't take item i: `dp[i][w] = dp[i-1][w]`
- If we take item i: `dp[i][w] = dp[i-1][w-weight[i]] + value[i]`

We take the maximum of these two choices.

</details>

---

## Question 8: LCS Recurrence

In Longest Common Subsequence, if `text1[i-1] == text2[j-1]`, what is `dp[i][j]`?

- A) `dp[i-1][j-1]`
- B) `dp[i-1][j-1] + 1`
- C) `max(dp[i-1][j], dp[i][j-1])`
- D) `dp[i-1][j] + dp[i][j-1]`

<details>
<summary>Show Answer</summary>

**B) `dp[i-1][j-1] + 1`**

When characters match, we extend the LCS by 1 from the previous state (both indices reduced by 1).

When characters don't match, we take the max of skipping either character:
`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

</details>

---

## Question 9: Space Optimization

How can we reduce space complexity in the Fibonacci DP solution from O(n) to O(1)?

- A) Use binary search
- B) Only keep the last two values
- C) Use recursion instead
- D) It's not possible

<details>
<summary>Show Answer</summary>

**B) Only keep the last two values**

Since `F(n) = F(n-1) + F(n-2)`, we only need the previous two values:

```python
def fib(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```

</details>

---

## Question 10: Problem Identification

Which of these problems is NOT typically solved with DP?

- A) Finding shortest path in a weighted graph
- B) Finding if an element exists in a sorted array
- C) Computing minimum edit distance
- D) Counting ways to make change

<details>
<summary>Show Answer</summary>

**B) Finding if an element exists in a sorted array**

Binary search is the optimal approach for searching in sorted arrays - it doesn't involve overlapping subproblems or need to remember previous calculations.

The other problems all exhibit optimal substructure and overlapping subproblems.

</details>

---

## Question 11: Kadane's Algorithm

What does Kadane's algorithm solve?

- A) Longest increasing subsequence
- B) Maximum subarray sum
- C) Minimum path sum
- D) Longest palindromic substring

<details>
<summary>Show Answer</summary>

**B) Maximum subarray sum**

Kadane's algorithm finds the contiguous subarray with the maximum sum in O(n) time:

```python
def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
```

</details>

---

## Question 12: Order of Computation

In bottom-up DP for the knapsack problem, why do we iterate weights in reverse when using a 1D array?

```python
for w in range(capacity, weight[i] - 1, -1):  # Why reverse?
```

- A) It's more efficient
- B) To prevent using the same item multiple times
- C) Required by Python syntax
- D) No particular reason

<details>
<summary>Show Answer</summary>

**B) To prevent using the same item multiple times**

In 0/1 knapsack, each item can be used at most once. If we iterate forward, we might use the updated value `dp[w-weight[i]]` which already includes item i, effectively using it twice.

Iterating backwards ensures we use values from the previous item's iteration.

</details>

---

## Question 13: Code Output

```python
def mystery(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, 3) + 1):
            dp[i] += dp[i - j]
    return dp[n]

print(mystery(4))
```

What is the output?

- A) 4
- B) 7
- C) 8
- D) 15

<details>
<summary>Show Answer</summary>

**B) 7**

This is "climbing stairs with up to 3 steps at a time":
- dp[0] = 1
- dp[1] = dp[0] = 1
- dp[2] = dp[1] + dp[0] = 2
- dp[3] = dp[2] + dp[1] + dp[0] = 4
- dp[4] = dp[3] + dp[2] + dp[1] = 7

</details>

---

## Question 14: 2D DP

For a 3x3 grid (unique paths problem), what is `dp[2][2]` after filling the table?

(Only can move right or down from top-left to bottom-right)

- A) 4
- B) 6
- C) 9
- D) 12

<details>
<summary>Show Answer</summary>

**B) 6**

```
DP Table (0-indexed):
[1, 1, 1]
[1, 2, 3]
[1, 3, 6]
```

Each cell = cell above + cell to the left.
dp[2][2] = 6 unique paths.

</details>

---

## Question 15: Problem Strategy

You need to find the minimum cost to reach the top of a staircase where each step has a cost. You can climb 1 or 2 steps. What's the DP recurrence?

- A) `dp[i] = min(dp[i-1], dp[i-2])`
- B) `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`
- C) `dp[i] = dp[i-1] + dp[i-2]`
- D) `dp[i] = max(dp[i-1], dp[i-2]) + cost[i]`

<details>
<summary>Show Answer</summary>

**B) `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`**

To reach step i with minimum cost:
1. We must pay `cost[i]`
2. We come from either step i-1 or i-2, whichever is cheaper

So the total minimum cost to reach step i is the cost of standing on step i plus the cheaper way to get there.

</details>

---

## Scoring

| Score | Level |
|-------|-------|
| 13-15 | ⭐⭐⭐ Expert |
| 10-12 | ⭐⭐ Proficient |
| 7-9 | ⭐ Intermediate |
| 0-6 | Keep studying! |

---

## Key Takeaways

1. **DP = Recursion + Memoization** — avoid redundant calculations
2. **Two approaches**: Top-down (memoization) vs Bottom-up (tabulation)
3. **Always define the state clearly** — what does dp[i] represent?
4. **Find the recurrence relation** — how to build from subproblems
5. **Consider space optimization** — often only need previous values
6. **Practice patterns** — most DP problems follow common templates

---

[Back to Dynamic Programming README](README.md) | [Next: Greedy Algorithms →](../05_greedy_algorithms/)
