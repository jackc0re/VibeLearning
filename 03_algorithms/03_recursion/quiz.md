# 🧠 Recursion Quiz

Test your understanding of recursion!

---

## Question 1: Base Case

What happens if a recursive function doesn't have a base case?

- A) The function returns None
- B) The function runs in O(1) time
- C) The function causes infinite recursion (stack overflow)
- D) The function automatically terminates after 10 calls

<details>
<summary>Show Answer</summary>

**C) The function causes infinite recursion (stack overflow)**

Without a base case, the function keeps calling itself forever, eventually exceeding the call stack limit and raising a `RecursionError`.

</details>

---

## Question 2: Factorial Implementation

What is returned by this factorial function when called with `factorial(5)`?

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

- A) 0
- B) 5
- C) 120
- D) Error

<details>
<summary>Show Answer</summary>

**C) 120**

```
factorial(5) = 5 * factorial(4)
             = 5 * 4 * factorial(3)
             = 5 * 4 * 3 * factorial(2)
             = 5 * 4 * 3 * 2 * factorial(1)
             = 5 * 4 * 3 * 2 * 1 * factorial(0)
             = 5 * 4 * 3 * 2 * 1 * 1
             = 120
```

</details>

---

## Question 3: Call Stack Depth

How many function calls are on the call stack when `sum_to(4)` reaches its base case?

```python
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)
```

- A) 3
- B) 4
- C) 5
- D) 6

<details>
<summary>Show Answer</summary>

**C) 5**

The call stack at the base case:
1. `sum_to(4)` - waiting
2. `sum_to(3)` - waiting
3. `sum_to(2)` - waiting
4. `sum_to(1)` - waiting
5. `sum_to(0)` - base case reached

</details>

---

## Question 4: Space Complexity

What is the space complexity of a basic recursive factorial function?

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

<details>
<summary>Show Answer</summary>

**C) O(n)**

Each recursive call adds a new frame to the call stack. For factorial(n), there are n+1 frames, giving O(n) space complexity.

</details>

---

## Question 5: Fibonacci Efficiency

Why is the naive recursive Fibonacci function inefficient?

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

- A) It uses too much memory
- B) It recalculates the same values many times
- C) The base case is wrong
- D) It doesn't handle negative numbers

<details>
<summary>Show Answer</summary>

**B) It recalculates the same values many times**

For `fib(5)`, `fib(2)` is calculated 3 times, `fib(3)` is calculated 2 times, etc.

This exponential redundancy gives O(2^n) time complexity.

The fix: Use memoization or iteration.

</details>

---

## Question 6: Bug Identification

What's wrong with this code?

```python
def count(n):
    if n == 0:
        return 0
    return 1 + count(n)
```

- A) Base case returns wrong value
- B) Doesn't make progress toward base case
- C) Missing return statement
- D) Nothing is wrong

<details>
<summary>Show Answer</summary>

**B) Doesn't make progress toward base case**

The recursive call `count(n)` passes the same value of `n`, so `n` never reaches 0.

Fix: `return 1 + count(n - 1)`

</details>

---

## Question 7: Code Output

What does this function return for `mystery([1, 2, 3, 4])`?

```python
def mystery(arr):
    if not arr:
        return 0
    return 1 + mystery(arr[1:])
```

- A) 0
- B) 4
- C) 10
- D) [1, 2, 3, 4]

<details>
<summary>Show Answer</summary>

**B) 4**

This function counts the elements in the list:
```
mystery([1,2,3,4]) = 1 + mystery([2,3,4])
                   = 1 + 1 + mystery([3,4])
                   = 1 + 1 + 1 + mystery([4])
                   = 1 + 1 + 1 + 1 + mystery([])
                   = 1 + 1 + 1 + 1 + 0
                   = 4
```

</details>

---

## Question 8: Tail Recursion

Which of these is a **tail recursive** function?

```python
# Option A
def sum_a(n):
    if n == 0:
        return 0
    return n + sum_a(n - 1)

# Option B
def sum_b(n, acc=0):
    if n == 0:
        return acc
    return sum_b(n - 1, acc + n)
```

- A) Option A
- B) Option B
- C) Both
- D) Neither

<details>
<summary>Show Answer</summary>

**B) Option B**

In tail recursion, the recursive call is the **last operation** in the function.

- **Option A**: The last operation is addition (`n + ...`), not the recursive call
- **Option B**: The recursive call `sum_b(n-1, acc+n)` is the last operation

</details>

---

## Question 9: Recursion vs Iteration

Which statement about recursion vs iteration is TRUE?

- A) Recursion is always faster than iteration
- B) Every recursive solution can be converted to an iterative one
- C) Recursion always uses less memory
- D) Iteration is always more readable

<details>
<summary>Show Answer</summary>

**B) Every recursive solution can be converted to an iterative one**

Any recursive algorithm can be implemented iteratively using an explicit stack.

In fact:
- Iteration is often faster (no function call overhead)
- Iteration usually uses less memory (no call stack)
- Readability depends on the problem structure

</details>

---

## Question 10: Recursive GCD

What is the value of `gcd(48, 18)` using the Euclidean algorithm?

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

- A) 2
- B) 6
- C) 12
- D) 18

<details>
<summary>Show Answer</summary>

**B) 6**

```
gcd(48, 18) = gcd(18, 48 % 18) = gcd(18, 12)
gcd(18, 12) = gcd(12, 18 % 12) = gcd(12, 6)
gcd(12, 6)  = gcd(6, 12 % 6)   = gcd(6, 0)
gcd(6, 0)   = 6  (base case)
```

</details>

---

## Question 11: Missing Return

What's wrong with this recursive search function?

```python
def search(arr, target):
    if not arr:
        return False
    if arr[0] == target:
        return True
    search(arr[1:], target)  # Bug here
```

- A) Base case is incorrect
- B) Should use arr[-1] instead of arr[0]
- C) Missing return statement in recursive call
- D) Wrong slice syntax

<details>
<summary>Show Answer</summary>

**C) Missing return statement in recursive call**

The recursive call `search(arr[1:], target)` doesn't return its result.

Fix: `return search(arr[1:], target)`

Without the return, the function returns `None` for successful searches.

</details>

---

## Question 12: Complexity

What is the time complexity of this function?

```python
def sum_pairs(arr):
    if len(arr) <= 1:
        return 0
    return arr[0] + arr[1] + sum_pairs(arr[2:])
```

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

<details>
<summary>Show Answer</summary>

**C) O(n)**

The function processes 2 elements at a time, making n/2 recursive calls.
Each call does O(1) work (two additions).

Total: n/2 × O(1) = O(n)

Note: The slice `arr[2:]` creates a new list, which could add overhead, but the algorithmic complexity is still O(n).

</details>

---

## Question 13: Backtracking

In generating all permutations recursively, how many recursive calls (approximately) are made for a list of n elements?

- A) n
- B) n²
- C) n!
- D) 2^n

<details>
<summary>Show Answer</summary>

**C) n!**

For permutations:
- First position: n choices
- Second position: n-1 choices
- Third position: n-2 choices
- ...and so on

Total: n × (n-1) × (n-2) × ... × 1 = n!

Each path from root to leaf represents one permutation.

</details>

---

## Question 14: Memoization

What does memoization do to optimize recursive functions?

- A) Converts recursion to iteration
- B) Reduces the number of base cases
- C) Caches results to avoid redundant calculations
- D) Removes the call stack

<details>
<summary>Show Answer</summary>

**C) Caches results to avoid redundant calculations**

Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again.

For Fibonacci:
- Without memoization: O(2^n) time
- With memoization: O(n) time

Python's `@lru_cache` decorator provides easy memoization.

</details>

---

## Question 15: Practical Application

Which problem is BEST solved with recursion?

- A) Finding the maximum in a flat list
- B) Counting from 1 to n
- C) Traversing a tree structure
- D) Iterating through a string

<details>
<summary>Show Answer</summary>

**C) Traversing a tree structure**

Trees are inherently recursive structures (a tree is a node with subtrees).

Recursive traversal is natural and elegant:
```python
def traverse(node):
    if node is None:
        return
    process(node)
    traverse(node.left)
    traverse(node.right)
```

The other problems are more naturally solved with simple loops.

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

1. **Every recursion needs a base case** to terminate
2. **Must make progress** toward the base case each call
3. **Space complexity** is at least O(depth) due to call stack
4. **Memoization** can drastically improve time complexity
5. **Recursion excels** for tree/graph traversal and divide-and-conquer
6. **Return values** must be passed back up the call chain

---

[Back to Recursion README](README.md) | [Next: Dynamic Programming →](../04_dynamic_programming/)
