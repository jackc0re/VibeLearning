# 🧠 Greedy Algorithms Quiz

Test your understanding of greedy algorithms!

---

## Question 1: Core Concept

What is the main characteristic of a greedy algorithm?

- A) It considers all possible solutions
- B) It makes the locally optimal choice at each step
- C) It uses recursion with memoization
- D) It always finds the globally optimal solution

<details>
<summary>Show Answer</summary>

**B) It makes the locally optimal choice at each step**

Greedy algorithms make the best decision at each step without considering the overall problem. This "local" optimization hopefully leads to a "global" optimal solution, but not always.

</details>

---

## Question 2: Required Properties

For a greedy algorithm to guarantee an optimal solution, the problem must have:

- A) Only overlapping subproblems
- B) Greedy choice property and optimal substructure
- C) Binary search capability
- D) A polynomial time complexity

<details>
<summary>Show Answer</summary>

**B) Greedy choice property and optimal substructure**

- **Greedy choice property**: A locally optimal choice leads to a globally optimal solution
- **Optimal substructure**: An optimal solution contains optimal solutions to subproblems

</details>

---

## Question 3: Coin Change

Using a greedy approach with coins [25, 10, 5, 1], what is the minimum number of coins for 63 cents?

- A) 5 coins
- B) 6 coins
- C) 7 coins
- D) 8 coins

<details>
<summary>Show Answer</summary>

**B) 6 coins**

Greedy selection:
- 63 ÷ 25 = 2 (50¢), remaining: 13¢
- 13 ÷ 10 = 1 (10¢), remaining: 3¢
- 3 ÷ 5 = 0
- 3 ÷ 1 = 3 (3¢), remaining: 0¢

Total: 25 + 25 + 10 + 1 + 1 + 1 = 6 coins

</details>

---

## Question 4: When Greedy Fails

With coins [1, 3, 4], what amount demonstrates that greedy gives a suboptimal solution?

- A) 5
- B) 6
- C) 7
- D) 8

<details>
<summary>Show Answer</summary>

**B) 6**

Greedy: 4 + 1 + 1 = 3 coins
Optimal: 3 + 3 = 2 coins

Greedy takes the largest coin (4) first, but the optimal solution uses two 3-cent coins.

</details>

---

## Question 5: Activity Selection

In activity selection, which greedy strategy finds the maximum number of non-overlapping activities?

- A) Select the activity that starts earliest
- B) Select the activity that ends earliest
- C) Select the shortest activity
- D) Select the activity with longest duration

<details>
<summary>Show Answer</summary>

**B) Select the activity that ends earliest**

Selecting the activity that ends earliest leaves the maximum amount of time for remaining activities. This greedy choice is proven to give the optimal solution.

</details>

---

## Question 6: Fractional Knapsack

Why does greedy work for fractional knapsack but not 0/1 knapsack?

- A) Fractional knapsack has smaller inputs
- B) 0/1 knapsack has overlapping subproblems
- C) In fractional knapsack, you can take parts of items to maximize value
- D) Fractional knapsack uses different data structures

<details>
<summary>Show Answer</summary>

**C) In fractional knapsack, you can take parts of items to maximize value**

When items can be divided:
- Taking items by value/weight ratio is always optimal
- You can fill remaining capacity with a fraction of the best remaining item

In 0/1 knapsack:
- Taking the best ratio item might leave space that could hold a more valuable combination
- Greedy choice doesn't guarantee optimality

</details>

---

## Question 7: Code Analysis

```python
def mystery(nums):
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True
```

What does this function determine?

- A) If array can be sorted
- B) If you can reach the last index (Jump Game)
- C) If array has duplicates
- D) Maximum sum subarray

<details>
<summary>Show Answer</summary>

**B) If you can reach the last index (Jump Game)**

This greedy algorithm tracks the farthest reachable index. If we ever reach a position beyond our farthest reach, we return False.

</details>

---

## Question 8: Complexity

What is the typical time complexity of greedy algorithms?

- A) Always O(n)
- B) Often O(n log n) due to sorting
- C) Always O(n²)
- D) Always O(2^n)

<details>
<summary>Show Answer</summary>

**B) Often O(n log n) due to sorting**

Many greedy algorithms require sorting the input first:
- Activity selection: Sort by end time O(n log n)
- Fractional knapsack: Sort by value/weight O(n log n)
- Job sequencing: Sort by profit O(n log n)

The actual greedy selection is usually O(n).

</details>

---

## Question 9: Huffman Coding

In Huffman coding, what is the greedy choice?

- A) Assign shortest codes to most frequent characters
- B) Always merge the two nodes with lowest frequencies
- C) Process characters alphabetically
- D) Use fixed-length codes for all characters

<details>
<summary>Show Answer</summary>

**B) Always merge the two nodes with lowest frequencies**

Huffman's greedy strategy builds a binary tree by repeatedly merging the two lowest-frequency nodes. This naturally gives shorter codes to more frequent characters.

</details>

---

## Question 10: Greedy vs DP

When should you use DP instead of greedy?

- A) When greedy is too slow
- B) When the problem has optimal substructure but not greedy choice property
- C) When input size is small
- D) When you need to minimize time complexity

<details>
<summary>Show Answer</summary>

**B) When the problem has optimal substructure but not greedy choice property**

If greedy choice property doesn't hold, the locally optimal choice might not lead to a globally optimal solution. In such cases, DP considers all possibilities.

Example: 0/1 Knapsack has optimal substructure but not greedy choice property → use DP.

</details>

---

## Question 11: Job Sequencing

In job sequencing with deadlines, what is the greedy strategy?

- A) Process jobs by earliest deadline
- B) Process jobs by shortest duration
- C) Process jobs by highest profit first
- D) Process jobs in given order

<details>
<summary>Show Answer</summary>

**C) Process jobs by highest profit first**

Strategy:
1. Sort jobs by profit (descending)
2. For each job, assign it to the latest available slot before its deadline
3. This maximizes total profit

</details>

---

## Question 12: Interval Problems

For finding minimum number of arrows to burst balloons (intervals), what should you sort by?

- A) Start position
- B) End position
- C) Interval length
- D) Middle point

<details>
<summary>Show Answer</summary>

**B) End position**

Sort by end position and shoot at each end:
- This ensures we hit the current balloon
- It might also hit overlapping balloons
- When we find a balloon not hit, we need a new arrow

This is similar to activity selection - ending earliest leaves room for more.

</details>

---

## Question 13: Proof Requirement

Why must greedy algorithms be proven correct?

- A) They are always inefficient
- B) Local optimum doesn't guarantee global optimum
- C) They use more memory
- D) They always need sorting

<details>
<summary>Show Answer</summary>

**B) Local optimum doesn't guarantee global optimum**

Greedy algorithms choose what looks best now. This doesn't always lead to the best overall solution. We must prove:
1. Making the greedy choice doesn't eliminate the optimal solution
2. After making the choice, remaining problem has the same structure

</details>

---

## Question 14: Application

Which algorithm uses a greedy approach?

- A) Floyd-Warshall shortest paths
- B) Dijkstra's shortest path (positive weights)
- C) Dynamic programming Fibonacci
- D) Binary search

<details>
<summary>Show Answer</summary>

**B) Dijkstra's shortest path (positive weights)**

Dijkstra's algorithm greedily selects the unvisited node with the smallest distance. This works for graphs with non-negative edge weights.

Note: It fails with negative edges (use Bellman-Ford instead).

</details>

---

## Question 15: Problem Classification

Which problem is best solved with a greedy approach?

- A) Longest common subsequence
- B) Edit distance
- C) Activity selection (maximum non-overlapping intervals)
- D) 0/1 Knapsack

<details>
<summary>Show Answer</summary>

**C) Activity selection (maximum non-overlapping intervals)**

Activity selection has the greedy choice property: selecting the earliest-ending activity always leads to an optimal solution.

The other problems require DP:
- LCS: Need to consider all alignments
- Edit distance: Need to consider all operations
- 0/1 Knapsack: Taking best ratio might waste capacity

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

1. **Greedy = local best choice** at each step
2. **Must prove correctness** — greedy doesn't always work
3. **Often requires sorting** — O(n log n) typical
4. **Compare with DP** — if greedy choice property fails, use DP
5. **Classic problems**: Activity selection, Huffman, MST, Dijkstra
6. **Test with counterexamples** — verify greedy works

---

[Back to Greedy Algorithms README](README.md) | [Next: Divide and Conquer →](../06_divide_and_conquer/)
