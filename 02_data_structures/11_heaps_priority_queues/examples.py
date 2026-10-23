"""
Heaps and Priority Queues - Examples
====================================
Builds a min-heap from scratch with printed sift traces, shows that the
heap is really just an array, demonstrates the heapq module, and finishes
with a priority-queue task scheduler.
"""

import heapq

print("=" * 50)
print("HEAPS AND PRIORITY QUEUES - Examples")
print("=" * 50)


# =============================================================================
# MIN-HEAP IMPLEMENTATION (WITH OPTIONAL TRACE OUTPUT)
# =============================================================================

class MinHeap:
    """A min-heap stored in a plain list: data[0] is always the minimum."""

    def __init__(self, trace=False):
        self.data = []
        self.trace = trace

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)

    def peek(self):
        """Smallest value, without removing it (None if empty)."""
        return self.data[0] if self.data else None

    def push(self, value):
        """Add value, then sift it up until its parent is smaller."""
        self.data.append(value)
        if self.trace:
            print(f"  push {value}: appended at index {len(self.data) - 1}")
        self._sift_up(len(self.data) - 1)

    def pop(self):
        """Remove and return the smallest value (None if empty)."""
        if not self.data:
            return None
        smallest = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            if self.trace:
                print(f"  pop {smallest}: moved last item {last} to the root")
            self._sift_down(0)
        else:
            if self.trace:
                print(f"  pop {smallest}: heap is now empty")
        return smallest

    def _sift_up(self, i):
        """Swap data[i] with its parent while it is smaller."""
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                if self.trace:
                    print(f"    sift-up: {self.data[i]} < parent "
                          f"{self.data[parent]}, swap")
                self.data[i], self.data[parent] = (
                    self.data[parent], self.data[i]
                )
                i = parent
            else:
                if self.trace:
                    print(f"    sift-up: {self.data[i]} >= parent "
                          f"{self.data[parent]}, stop")
                break

    def _sift_down(self, i):
        """Swap data[i] with its SMALLER child until both children are bigger."""
        n = len(self.data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            if left >= n:
                if self.trace:
                    print(f"    sift-down: {self.data[i]} has no children, stop")
                return
            smallest = i
            if self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                if self.trace:
                    print(f"    sift-down: {self.data[i]} <= both children, stop")
                return
            if self.trace:
                print(f"    sift-down: swap {self.data[i]} with smaller "
                      f"child {self.data[smallest]}")
            self.data[i], self.data[smallest] = (
                self.data[smallest], self.data[i]
            )
            i = smallest


# =============================================================================
# BUILDING THE HEAP, WATCHING THE SIFTS
# =============================================================================
print("\n--- Building a Min-Heap, Watching the Sifts ---\n")

heap = MinHeap(trace=True)
for value in [5, 3, 8, 1, 9, 2]:
    heap.push(value)
    print(f"    array now: {heap.data}")

print("\nNow pop the minimum three times:")
for _ in range(3):
    popped = heap.pop()
    print(f"    popped {popped}, array now: {heap.data}")

print(f"\npeek() without removing: {heap.peek()}")
print(f"len(heap): {len(heap)}")


# =============================================================================
# THE HEAP IS AN ARRAY (INDEX MATH)
# =============================================================================
print("\n--- The Heap Is an Array (index math) ---\n")

data = [1, 3, 2, 7, 4, 6, 8]
print("Every node's family, computed with index math only:\n")
for i, value in enumerate(data):
    parent = data[(i - 1) // 2] if i > 0 else None
    left, right = 2 * i + 1, 2 * i + 2
    children = []
    if left < len(data):
        children.append(str(data[left]))
    if right < len(data):
        children.append(str(data[right]))
    parent_text = str(parent) if parent is not None else "none (root)"
    child_text = ", ".join(children) if children else "none"
    print(f"  index {i}: value {value} | parent: {parent_text} | "
          f"children: {child_text}")

print("""
  The same array drawn as a tree:

               1
             /   \\
            3     2
           / \\   / \\
          7   4 6   8
""")
print("  Notice the array is NOT sorted: index 1 holds 3, index 2 holds 2.")
print("  The only guarantee is that every parent is <= its children,")
print("  which makes data[0] the global minimum.")


# =============================================================================
# PEEK, LEN, AND TRUTHINESS
# =============================================================================
print("\n--- Peek, len(), and Truthiness ---\n")

h = MinHeap()
print(f"peek() on an empty heap: {h.peek()}")
print(f"bool() on an empty heap: {bool(h)}")
h.push(4)
h.push(2)
print(f"after pushing 4, 2:  len={len(h)}, peek={h.peek()}, bool={bool(h)}")
print("draining with 'while h:':")
while h:
    print(f"  popped {h.pop()}, {len(h)} left")


# =============================================================================
# THE HEAPQ MODULE
# =============================================================================
print("\n--- The heapq Module ---\n")

data = [7, 2, 9, 4, 1]
heapq.heapify(data)
print(f"heapify([7, 2, 9, 4, 1]) -> {data}  (same items, heap order)")
print(f"data[0] is the minimum:  {data[0]}")

heapq.heappush(data, 0)
print(f"heappush(data, 0)      -> {data}")
smallest = heapq.heappop(data)
print(f"heappop(data)          -> {smallest}, data now {data}")

# heappushpop vs heapreplace: same two steps, opposite order
a = [1, 3, 2]
heapq.heapify(a)
result = heapq.heappushpop(a, 0)
print(f"\nheappushpop([1,3,2], 0): pushed 0 first, popped it back -> {result}")
b = [1, 3, 2]
heapq.heapify(b)
result = heapq.heapreplace(b, 0)
print(f"heapreplace([1,3,2], 0): popped the OLD min first      -> {result}, "
      f"0 is still inside: {b}")

scores = [91, 55, 78, 84, 62]
print(f"\nnsmallest(2, {scores}) -> {heapq.nsmallest(2, scores)}")
print(f"nlargest(2, {scores}) -> {heapq.nlargest(2, scores)}")

# Max-heap: negate going in and coming out
maxheap = []
for value in [4, 9, 1, 7]:
    heapq.heappush(maxheap, -value)
print(f"\npushed 4, 9, 1, 7 negated: {maxheap}")
print(f"the largest value is -maxheap[0] = {-maxheap[0]}")
drained = []
while maxheap:
    drained.append(-heapq.heappop(maxheap))
print(f"popping drains it largest-first: {drained}")


# =============================================================================
# TASK SCHEDULER: A REAL PRIORITY QUEUE
# =============================================================================
print("\n--- Task Scheduler: a Real Priority Queue ---\n")

# WHY the counter? Tuples compare element by element. When two priorities
# tie, Python moves on to the next element - which is the task itself if we
# do not add a counter. Dicts and most objects cannot be compared with '<':
schedule = []
try:
    heapq.heappush(schedule, (1, {"job": "send report"}))
except TypeError as error:
    print(f"pushing (priority, dict-task) crashes -> {type(error).__name__}: {error}")

# The counter fixes that: it is always comparable, so the task object is
# never compared at all - and equal-priority tasks keep arrival order (FIFO).
tasks = [
    (3, "water the plants"),
    (1, "fix the leak"),
    (2, "reply to review"),
    (1, "call the client"),
]
schedule = []
counter = 0
print("\nQueuing tasks:")
for priority, description in tasks:
    heapq.heappush(schedule, (priority, counter, description))
    counter += 1
    print(f"  queued {description!r} at priority {priority} "
          f"(counter was {counter - 1})")

print("\nRunning order (most urgent first, ties in arrival order):")
while schedule:
    priority, _, description = heapq.heappop(schedule)
    print(f"  runs: {description} (priority {priority})")


print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
