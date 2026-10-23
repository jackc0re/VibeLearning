# 🎯 Greedy Algorithms

> Making locally optimal choices to find globally optimal solutions

---

## 📋 Table of Contents

1. [What are Greedy Algorithms?](#what-are-greedy-algorithms)
2. [Key Properties](#key-properties)
3. [When Greedy Works](#when-greedy-works)
4. [When Greedy Fails](#when-greedy-fails)
5. [Classic Problems](#classic-problems)
6. [Greedy vs Dynamic Programming](#greedy-vs-dynamic-programming)
7. [Design Strategy](#design-strategy)

---

## What are Greedy Algorithms?

Greedy algorithms make the **locally optimal choice** at each step, hoping to find a **globally optimal solution**.

> "Take the best you can get right now, and don't worry about the future."

### Simple Example: Coin Change (US Coins)

To make 67 cents with coins [1, 5, 10, 25]:

```
Step 1: Take the largest coin ≤ 67 → 25¢ (Remaining: 42¢)
Step 2: Take the largest coin ≤ 42 → 25¢ (Remaining: 17¢)
Step 3: Take the largest coin ≤ 17 → 10¢ (Remaining: 7¢)
Step 4: Take the largest coin ≤ 7  → 5¢  (Remaining: 2¢)
Step 5: Take the largest coin ≤ 2  → 1¢  (Remaining: 1¢)
Step 6: Take the largest coin ≤ 1  → 1¢  (Remaining: 0¢)

Total: 25 + 25 + 10 + 5 + 1 + 1 = 67¢ (6 coins)
```

This greedy approach works for US coins!

---

## Key Properties

For greedy to work optimally, the problem must have:

### 1. Greedy Choice Property

A locally optimal choice leads to a globally optimal solution.

> "The choice that looks best now IS the best choice."

### 2. Optimal Substructure

An optimal solution contains optimal solutions to subproblems.

> "After making a choice, we're left with a smaller problem of the same type."

---

## When Greedy Works

### ✅ Activity Selection

Choose maximum non-overlapping activities:

```python
def activity_selection(activities):
    """
    Select maximum non-overlapping activities.
    Activities are (start, end) tuples.
    
    Greedy: Always pick the activity that ends earliest.
    """
    # Sort by end time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    selected = [sorted_activities[0]]
    last_end = sorted_activities[0][1]
    
    for start, end in sorted_activities[1:]:
        if start >= last_end:  # No overlap
            selected.append((start, end))
            last_end = end
    
    return selected

# Example
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
print(activity_selection(activities))
# Output: [(1, 4), (5, 7), (8, 11)] - 3 activities
```

**Why it works:** Picking the earliest-ending activity leaves the most time for remaining activities.

### ✅ Fractional Knapsack

Maximize value when items can be divided:

```python
def fractional_knapsack(weights, values, capacity):
    """
    Fractional Knapsack: Take fractions of items.
    
    Greedy: Take items with highest value/weight ratio first.
    """
    items = list(zip(weights, values))
    # Sort by value/weight ratio (descending)
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_value = 0
    remaining = capacity
    
    for weight, value in items:
        if weight <= remaining:
            # Take whole item
            total_value += value
            remaining -= weight
        else:
            # Take fraction
            fraction = remaining / weight
            total_value += value * fraction
            break
    
    return total_value
```

**Why it works:** Value per unit weight is the best measure of item efficiency.

### ✅ Huffman Coding

Build optimal prefix-free codes for compression:

```python
import heapq

def huffman_encoding(frequencies):
    """
    Build Huffman tree for optimal encoding.
    
    Greedy: Always merge the two lowest-frequency nodes.
    """
    # Create heap of (frequency, character)
    heap = [[freq, [char, ""]] for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        
        # Add '0' to all codes in lo, '1' to all codes in hi
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        
        # Merge and push back
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return sorted(heap[0][1:], key=lambda p: (len(p[1]), p))
```

---

## When Greedy Fails

### ❌ Coin Change with Arbitrary Denominations

```python
# Coins: [1, 3, 4]
# Amount: 6

# Greedy approach:
# Take 4 → remaining 2
# Take 1 → remaining 1
# Take 1 → remaining 0
# Total: 3 coins (4 + 1 + 1)

# Optimal solution:
# Take 3 + 3 = 6
# Total: 2 coins!
```

**Why greedy fails:** The largest coin first isn't always optimal.

### ❌ 0/1 Knapsack

When items cannot be divided, greedy doesn't guarantee optimality:

```python
# Items: weight=[2, 3, 4], value=[3, 4, 5]
# Capacity: 5

# Greedy by value/weight ratio:
# Ratios: [3/2=1.5, 4/3=1.33, 5/4=1.25]
# Take item 0 (weight 2, value 3) → remaining capacity 3
# Take item 1 (weight 3, value 4) → remaining capacity 0
# Total value: 7

# Optimal (using DP):
# Take items 0 and 2 (weight 2+4=6 > 5? No...)
# Take item 1 and 0 (weight 5, value 7) ✓
# OR take item 2 alone (weight 4, value 5)
# Best is actually item 0 + item 1 = 7

# In this case greedy works, but in general it doesn't!
```

### ❌ Traveling Salesman Problem (TSP)

Greedy (nearest neighbor) doesn't find the shortest tour:

```
Cities: A, B, C, D arranged in a square
Distances: AB=1, BC=10, CD=1, DA=10, AC=100, BD=100

Greedy from A: A→B→C→D→A = 1+10+1+10 = 22
Optimal path: A→B→D→C→A might be different
```

---

## Classic Problems

### 1. Interval Scheduling

Select maximum non-overlapping intervals:

```python
def max_intervals(intervals):
    """Sort by end time, greedily select non-overlapping."""
    intervals.sort(key=lambda x: x[1])
    count = 0
    last_end = float('-inf')
    
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    
    return count
```

### 2. Job Sequencing with Deadlines

Maximize profit by scheduling jobs before deadlines:

```python
def job_sequencing(jobs):
    """
    jobs: list of (job_id, deadline, profit)
    Greedy: Sort by profit, assign to latest available slot.
    """
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    
    slots = [-1] * (max_deadline + 1)  # Track assigned jobs
    total_profit = 0
    
    for job_id, deadline, profit in jobs:
        # Find latest available slot before deadline
        for slot in range(deadline, 0, -1):
            if slots[slot] == -1:
                slots[slot] = job_id
                total_profit += profit
                break
    
    return total_profit, [s for s in slots[1:] if s != -1]
```

### 3. Minimum Spanning Tree (Prim's/Kruskal's)

Both are greedy algorithms for finding MST:

```python
def kruskal_mst(edges, num_vertices):
    """
    Kruskal's algorithm: Greedy by edge weight.
    Always add the smallest edge that doesn't create a cycle.
    """
    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])
    
    # Union-Find data structure
    parent = list(range(num_vertices))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)
    
    mst = []
    for u, v, weight in edges:
        if find(u) != find(v):  # No cycle
            union(u, v)
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:
                break
    
    return mst
```

### 4. Dijkstra's Shortest Path

Greedy approach to single-source shortest paths:

```python
import heapq

def dijkstra(graph, start):
    """
    Greedy: Always process the closest unvisited node.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, node = heapq.heappop(pq)
        
        if curr_dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

---

## Greedy vs Dynamic Programming

| Aspect | Greedy | Dynamic Programming |
|--------|--------|---------------------|
| Approach | Make locally optimal choice | Consider all options |
| Subproblems | Solve once, move on | Solve and remember all |
| Correctness | Must prove greedy choice is safe | Always correct (if applicable) |
| Efficiency | Usually O(n) or O(n log n) | Often O(n²) or worse |
| When to use | Greedy choice property holds | Overlapping subproblems |

### Decision Flow

```
                    Is there optimal substructure?
                              │
                    ┌─────────┴─────────┐
                    │ No                │ Yes
                    ▼                   ▼
              Use other         Does greedy choice
              techniques        property hold?
                                       │
                              ┌────────┴────────┐
                              │ No              │ Yes
                              ▼                 ▼
                    Use Dynamic           Use Greedy
                    Programming           Algorithm
```

---

## Design Strategy

### Step 1: Identify the Greedy Choice

What's the "locally best" option at each step?

### Step 2: Prove It Works

Show that choosing greedy doesn't eliminate the optimal solution.

### Step 3: Check for Counterexamples

Try edge cases where greedy might fail.

### Step 4: Implement and Test

```python
def greedy_template():
    """
    General greedy algorithm structure.
    """
    # 1. Sort by some criteria (if needed)
    # 2. Initialize solution
    # 3. Iterate through choices
    #    - Make greedy choice
    #    - Update state
    # 4. Return solution
    pass
```

---

## 🔑 Key Takeaways

1. **Greedy is simple** — make the best choice now, don't look back
2. **Not always optimal** — must prove greedy choice property
3. **Often efficient** — usually O(n log n) due to sorting
4. **Classic problems**: Activity selection, Huffman, MST, Dijkstra
5. **When in doubt, use DP** — it's always correct if applicable
6. **Test with counterexamples** — verify greedy works for your problem

---

## 🔗 Next Steps

- Practice with [`exercises.py`](exercises.py)
- Test your knowledge with [`quiz.md`](quiz.md)
- Move on to [06_divide_and_conquer](../06_divide_and_conquer/README.md)
