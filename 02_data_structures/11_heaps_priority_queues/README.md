# 🏥 Heaps and Priority Queues

The data structure behind Python's `heapq` module — always ready to hand you
the **most urgent** item in **O(log n)**.

---

## The Priority Problem

An ordinary queue is fair but blind: first in, first out. Real life is not
always like that.

Think of an **emergency room**. Patients are not treated in arrival order —
someone with a sprained finger waits behind someone with chest pain. The ER
runs a **priority queue**: whoever is *most urgent* goes next, no matter when
they arrived.

```
ordinary queue:  A(urgent=3) -> B(urgent=1) -> C(urgent=2)   serves A first
priority queue:  serves B first (1 = most urgent, arrived second)
```

A sorted list could do the job, but inserting into the middle costs O(n).
A **heap** does push and pop in O(log n) and peek in O(1).

---

## A Heap Is Just an Array

A heap is a **complete binary tree** — every level full except possibly the
last, which fills left to right — stored flat in a plain Python list. The
tree shape is *implied by index math*, not by pointers:

```
array:  [1, 3, 2, 7, 4, 6, 8]
index:   0  1  2  3  4  5  6

tree:                1                <- index 0
                   /   \
                 3       2            <- indices 1, 2
                / \     / \
               7   4   6   8          <- indices 3, 4, 5, 6

for the node at index i:
  parent      = (i - 1) // 2
  left child  = 2 * i + 1
  right child = 2 * i + 2
```

Check it with index 1 (the value 3): parent `(1 - 1) // 2 = 0` — the 1 — and
children `2*1+1 = 3` (the 7) and `2*1+2 = 4` (the 4). That is the whole trick.
No `.left` or `.right` attributes anywhere — just arithmetic.

---

## The Min-Heap Property

> **Every parent is <= both of its children.**

One rule, one powerful consequence: `array[0]` is always the **minimum** of
the entire heap. But notice what the rule does *not* say — the array is **not
sorted**. In the picture above, `array[1]` is 3 and `array[2]` is 2, so the
"second smallest" is *not* at index 1.

A **max-heap** is the mirror image: every parent >= its children, so index 0
holds the maximum. Python's `heapq` module is a **min-heap**; to get
max-heap behavior you negate values on the way in and out (shown below).

---

## Building a MinHeap From Scratch

> 💡 **First time seeing `class`?** Start with the [10-line primer in Stacks and Queues](../06_stacks_queues/README.md#stack-class-implementation) - a class is a blueprint, `__init__` sets it up, `self` is the instance. Full treatment in [Module 04](../../04_oop_concepts/01_classes_and_objects/README.md).

```python
class MinHeap:
    def __init__(self):
        self.data = []          # the whole heap lives in a plain list

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)  # lets you write `while heap:`

    def peek(self):
        """Smallest value, without removing it (None if empty)."""
        return self.data[0] if self.data else None

    def push(self, value):
        """Add value, then sift it up until its parent is smaller."""
        self.data.append(value)              # 1. park it at the end
        i = len(self.data) - 1
        while i > 0:                         # 2. sift up
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = (
                    self.data[parent], self.data[i]
                )
                i = parent
            else:
                break                        # parent is smaller: done

    def pop(self):
        """Remove and return the smallest value (None if empty)."""
        if not self.data:
            return None
        smallest = self.data[0]
        last = self.data.pop()               # 1. take the LAST item out
        if self.data:
            self.data[0] = last              # 2. move it to the root...
            i = 0
            while True:                      # 3. ...and sift it down
                left, right = 2 * i + 1, 2 * i + 2
                smallest_child = i
                if left < len(self.data) and self.data[left] < self.data[smallest_child]:
                    smallest_child = left
                if right < len(self.data) and self.data[right] < self.data[smallest_child]:
                    smallest_child = right
                if smallest_child == i:
                    break                    # both children are bigger: done
                self.data[i], self.data[smallest_child] = (
                    self.data[smallest_child], self.data[i]
                )
                i = smallest_child
        return smallest
```

**Insert = sift-up.** Park the new value at the end, then keep swapping it
with its parent while it is smaller. It bubbles toward the top at most one
path's worth of steps.

**Pop-min = sift-down.** The minimum sits at index 0. Remove it, move the
*last* item into the root spot, then keep swapping it with its **smaller**
child until both children are bigger. (Swap with the smaller child — picking
the left one blindly can break the property.)

---

## Time Complexity

| Operation | Complexity | Why |
|-----------|------------|-----|
| push (insert) | O(log n) | sift-up climbs at most the tree height |
| pop (remove min) | O(log n) | sift-down descends at most the tree height |
| peek (look at min) | O(1) | it just sits at index 0 |
| build heap from n items | O(n) | bottom-up `heapify`, cheaper than n pushes |
| search for an arbitrary item | O(n) | the property only compares parents to children |

The height of a complete tree holding n items is about log2(n) — that is
where every log n comes from.

---

## Python's heapq Module

You will rarely hand-roll a heap — Python ships one in `heapq`:

```python
import heapq

data = [7, 2, 9, 4, 1]
heapq.heapify(data)         # rearrange IN PLACE into a min-heap, O(n)
data[0]                     # the minimum, O(1)

heapq.heappush(data, 0)     # insert, O(log n)
smallest = heapq.heappop(data)   # remove + return the min, O(log n)

# Two "do both at once" helpers (each costs one sift, not two):
heapq.heappushpop(data, 5)  # push 5 first, THEN pop the min
heapq.heapreplace(data, 5)  # pop the min first, THEN push 5

heapq.nsmallest(3, [91, 55, 78, 84, 62])   # [55, 62, 78]
heapq.nlargest(2, [91, 55, 78, 84, 62])    # [91, 84]

# Max-heap: negate on the way in, negate again on the way out
heap = []
heapq.heappush(heap, -4)
heapq.heappush(heap, -9)
-heap[0]                    # 9 - the LARGEST value, O(1)
```

`heappushpop` vs `heapreplace`: they run the same two steps in the opposite
order. Push-then-pop can return the value you just pushed (if it is the new
minimum); pop-then-push always returns the *old* minimum, even if the new
value is smaller.

---

## A Real Priority Queue: Task Scheduler

The classic heapq idiom is a queue of `(priority, counter, task)` tuples:

```python
import heapq

schedule = []
counter = 0
for priority, task in [(3, "water plants"), (1, "fix leak"), (1, "call client")]:
    heapq.heappush(schedule, (priority, counter, task))
    counter += 1

while schedule:
    priority, _, task = heapq.heappop(schedule)
    print(f"running: {task} (priority {priority})")
```

**Why the counter?** Tuples compare element by element. When two priorities
tie, Python compares the *next* element. Without the counter that is the task
itself — strings happen to compare fine, but task objects that cannot be
compared (dicts, functions, class instances without `__lt__`) raise
`TypeError`. The counter is a guaranteed-comparable tie-breaker, and as a
bonus it keeps equal-priority tasks in **arrival order** (FIFO).

---

## Heaps Already in This Repo

Heaps are quiet workhorses. You have already met them here:

- [Dijkstra's Algorithm](../../03_algorithms/07_graph_algorithms/README.md#dijkstras-algorithm)
  keeps a heap of `(distance, node)` pairs and always expands the closest
  unvisited node.
- [Prim's Algorithm](../../03_algorithms/07_graph_algorithms/README.md#prims-algorithm)
  grows a minimum spanning tree from a heap of candidate edges.
- [Huffman Coding](../../03_algorithms/05_greedy_algorithms/README.md#huffman-coding)
  builds its tree by repeatedly merging the two least-frequent nodes — which
  is exactly a min-heap pop, pop, push.
- Heap *sort* — pop a max-heap until it is empty and the output comes out in
  order — belongs to the family of
  [efficient sorting algorithms](../../03_algorithms/02_sorting/README.md#efficient-sorting-algorithms)
  along with merge sort and quick sort.

---

## Common Mistakes

### 1. Indexing the heap as if it were sorted
```python
import heapq
h = [3, 1, 2]
heapq.heapify(h)
h[0]            # ❌ believing h[1] is the second smallest
h[1]            #    it is 3 - but the second smallest is 2!

# ✅ The only promise: h[0] is the minimum
heapq.nsmallest(2, h)   # [1, 2] - ordered access done for you
```
The heap property bounds parents against *children only*. Siblings are not
ordered, whole levels are not ordered — index 0 is the one guaranteed slot.

### 2. Forgetting the tie-breaker tuple
```python
import heapq
pq = []
heapq.heappush(pq, (1, {"job": "clean"}))   # ❌ TypeError: '<' not supported

# ✅ Insert a counter between priority and task
heapq.heappush(pq, (1, 0, {"job": "clean"}))
```
The counter is compared instead of the task, so the task never needs to
support `<` — and equal-priority tasks stay in arrival order.

### 3. Faking a priority queue with a list
```python
waiting = [(1, "fix leak"), (3, "water plants")]
waiting.sort()          # ❌ O(n log n) every time you need the next item
waiting.pop(0)          # ❌ O(n) - shifts every remaining element left

# ✅ heapify once, then push/pop in O(log n)
import heapq
heapq.heapify(waiting)
priority, task = heapq.heappop(waiting)
```
`min(waiting)` + `waiting.remove(...)` is the same trap: each call scans the
whole list. Under constant insert/remove pressure the heap wins easily.

---

## Quick Reference

```python
import heapq

data = [7, 2, 9]
heapq.heapify(data)          # in place, O(n)
heapq.heappush(data, 1)      # O(log n)
data[0]                      # peek, O(1)
heapq.heappop(data)          # remove + return min, O(log n)
heapq.heappushpop(data, 5)   # push 5, then pop min
heapq.heapreplace(data, 5)   # pop min, then push 5
heapq.nsmallest(3, data)     # 3 smallest, sorted
heapq.nlargest(2, data)      # 2 largest, sorted

# Max-heap: negate going in and coming out
heapq.heappush(heap, -priority)
urgent = -heapq.heappop(heap)

# Safe priority-queue entry: (priority, counter, task)
counter += 1
heapq.heappush(pq, (priority, counter, task))
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
