# 🔄 Recursion

> Solving problems by breaking them into smaller versions of themselves

---

## 📋 Table of Contents

1. [What is Recursion?](#what-is-recursion)
2. [Anatomy of a Recursive Function](#anatomy-of-a-recursive-function)
3. [The Call Stack](#the-call-stack)
4. [Classic Examples](#classic-examples)
5. [Recursion vs Iteration](#recursion-vs-iteration)
6. [Common Pitfalls](#common-pitfalls)
7. [Tail Recursion](#tail-recursion)
8. [When to Use Recursion](#when-to-use-recursion)

---

## What is Recursion?

Recursion is when a function calls itself to solve a smaller version of the same problem.

> "To understand recursion, you must first understand recursion." — Anonymous

### Simple Example

```python
def countdown(n):
    if n <= 0:           # Base case
        print("Liftoff!")
    else:
        print(n)
        countdown(n - 1)  # Recursive call

countdown(3)
# Output: 3, 2, 1, Liftoff!
```

### The Key Insight

Every recursive problem can be broken down into:
1. **Base case(s)** — When to stop (simplest case with a known answer)
2. **Recursive case(s)** — How to break the problem into smaller pieces

---

## Anatomy of a Recursive Function

```python
def recursive_function(problem):
    # 1. BASE CASE - When to stop
    if problem is simple enough:
        return simple_answer
    
    # 2. RECURSIVE CASE - Break down the problem
    smaller_problem = make_problem_smaller(problem)
    
    # 3. RECURSIVE CALL - Solve smaller problem
    result = recursive_function(smaller_problem)
    
    # 4. COMBINE - Use result to solve original problem
    return combine(result)
```

### Example: Factorial

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# factorial(4) = 4 * factorial(3)
#              = 4 * 3 * factorial(2)
#              = 4 * 3 * 2 * factorial(1)
#              = 4 * 3 * 2 * 1
#              = 24
```

### The Three Questions

Before writing recursive code, answer:

1. **What is the base case?** (When do we stop?)
2. **What is the recursive case?** (How do we break it down?)
3. **Are we making progress toward the base case?** (Will it terminate?)

---

## The Call Stack

Each recursive call creates a new "frame" on the call stack.

### Visualizing factorial(4):

```
Call Stack Growth:
┌─────────────────┐
│ factorial(1)=1  │ ← Base case reached
├─────────────────┤
│ factorial(2)    │
├─────────────────┤
│ factorial(3)    │
├─────────────────┤
│ factorial(4)    │
└─────────────────┘

Stack Unwinding:
factorial(1) returns 1
factorial(2) returns 2 * 1 = 2
factorial(3) returns 3 * 2 = 6
factorial(4) returns 4 * 6 = 24
```

### Stack Overflow

Too many recursive calls can exceed the stack limit:

```python
def infinite_recursion():
    return infinite_recursion()  # Never stops!

# This will raise: RecursionError: maximum recursion depth exceeded
```

Python's default recursion limit is ~1000. You can check/change it:

```python
import sys
print(sys.getrecursionlimit())  # Default: 1000
sys.setrecursionlimit(5000)     # Increase (use carefully!)
```

---

## Classic Examples

### 1. Fibonacci Numbers

```python
def fibonacci(n):
    """
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2)
    
    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    """
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)
```

⚠️ **Warning**: This is O(2ⁿ) — very slow! See Dynamic Programming for optimization.

### 2. Sum of a List

```python
def sum_list(arr):
    """Sum all elements in a list recursively."""
    # Base case: empty list
    if not arr:
        return 0
    
    # Recursive case: first element + sum of rest
    return arr[0] + sum_list(arr[1:])

# sum_list([1, 2, 3, 4]) = 1 + sum_list([2, 3, 4])
#                        = 1 + 2 + sum_list([3, 4])
#                        = 1 + 2 + 3 + sum_list([4])
#                        = 1 + 2 + 3 + 4 + sum_list([])
#                        = 1 + 2 + 3 + 4 + 0 = 10
```

### 3. String Reversal

```python
def reverse_string(s):
    """Reverse a string recursively."""
    # Base case: empty or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: last char + reverse of rest
    return s[-1] + reverse_string(s[:-1])

# reverse_string("hello")
# = "o" + reverse_string("hell")
# = "o" + "l" + reverse_string("hel")
# = "o" + "l" + "l" + reverse_string("he")
# = "o" + "l" + "l" + "e" + reverse_string("h")
# = "o" + "l" + "l" + "e" + "h"
# = "olleh"
```

### 4. Power Function

```python
def power(base, exp):
    """Calculate base^exp recursively."""
    # Base case
    if exp == 0:
        return 1
    
    # Recursive case
    return base * power(base, exp - 1)

# power(2, 4) = 2 * power(2, 3)
#             = 2 * 2 * power(2, 2)
#             = 2 * 2 * 2 * power(2, 1)
#             = 2 * 2 * 2 * 2 * power(2, 0)
#             = 2 * 2 * 2 * 2 * 1 = 16
```

### 5. Binary Search (Recursive)

```python
def binary_search(arr, target, left=0, right=None):
    """Search for target in sorted array."""
    if right is None:
        right = len(arr) - 1
    
    # Base case: not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Base case: found
    if arr[mid] == target:
        return mid
    
    # Recursive case
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
```

---

## Recursion vs Iteration

Every recursive solution can be written iteratively, and vice versa.

### Factorial Comparison

```python
# Recursive
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### When to Choose Each

| Recursion | Iteration |
|-----------|-----------|
| Naturally recursive problems (trees, graphs) | Simple loops |
| Code clarity matters | Performance critical |
| Divide and conquer algorithms | Large input sizes |
| Problem has recursive structure | Avoiding stack overflow |

### Trade-offs

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Code clarity | Often cleaner | Can be verbose |
| Memory | Uses call stack | Usually less memory |
| Performance | Function call overhead | Generally faster |
| Stack overflow risk | Yes | No |

---

## Common Pitfalls

### 1. Missing Base Case

```python
# ❌ WRONG - no base case
def count_down(n):
    print(n)
    count_down(n - 1)  # Infinite recursion!

# ✅ CORRECT
def count_down(n):
    if n <= 0:  # Base case
        return
    print(n)
    count_down(n - 1)
```

### 2. Not Making Progress

```python
# ❌ WRONG - doesn't approach base case
def bad_sum(n):
    if n == 0:
        return 0
    return n + bad_sum(n)  # n never changes!

# ✅ CORRECT
def good_sum(n):
    if n == 0:
        return 0
    return n + good_sum(n - 1)  # n decreases
```

### 3. Redundant Calculations

```python
# ❌ INEFFICIENT - calculates same values many times
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

# fib_slow(5) calculates fib(3) twice, fib(2) three times, etc.

# ✅ EFFICIENT - use memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_fast(n):
    if n <= 1:
        return n
    return fib_fast(n-1) + fib_fast(n-2)
```

### 4. Wrong Return Value Handling

```python
# ❌ WRONG - ignores return value
def find_value(arr, target):
    if not arr:
        return False
    if arr[0] == target:
        return True
    find_value(arr[1:], target)  # Missing return!

# ✅ CORRECT
def find_value(arr, target):
    if not arr:
        return False
    if arr[0] == target:
        return True
    return find_value(arr[1:], target)  # Return the result!
```

---

## Tail Recursion

Tail recursion is when the recursive call is the **last** operation in the function.

### Non-Tail Recursive

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # Multiplication happens AFTER recursive call
```

### Tail Recursive

```python
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)  # No operation after call
```

### Why It Matters

- Tail-recursive functions can be optimized to use O(1) stack space
- Some languages (not Python!) automatically optimize tail calls
- Python doesn't optimize tail recursion, so iterative is often better for deep recursion

---

## When to Use Recursion

### ✅ Good Use Cases

1. **Tree traversal** — Navigate tree structures (file systems, DOM)
2. **Graph algorithms** — DFS, finding paths
3. **Divide and conquer** — Merge sort, Quick sort
4. **Backtracking** — Puzzles, permutations, combinations
5. **Mathematical definitions** — Factorial, Fibonacci, GCD
6. **Nested structures** — JSON parsing, nested lists

### ❌ When to Avoid

1. **Simple iterations** — Use loops instead
2. **Large input sizes** — Risk of stack overflow
3. **Performance critical** — Function call overhead
4. **No natural recursive structure** — Forced recursion is confusing

---

## 🔑 Key Takeaways

1. **Every recursion needs a base case** — otherwise infinite loop
2. **Must make progress toward base case** — smaller input each call
3. **Understand the call stack** — each call uses memory
4. **Recursion isn't always best** — sometimes iteration is simpler
5. **Memoization helps** — avoid redundant calculations
6. **Think recursively** — "assume smaller problems are solved"

---

## 📚 The Recursive Leap of Faith

When writing recursive code, trust that the recursive call works correctly for smaller inputs. Focus on:

1. Is the base case correct?
2. Is the recursive case breaking down the problem?
3. Does the combination of results produce the right answer?

If yes to all three, the recursion works!

---

## 🔗 Next Steps

- Practice with [`exercises.py`](exercises.py)
- Test your knowledge with [`quiz.md`](quiz.md)
- Move on to [04_dynamic_programming](../04_dynamic_programming/)
