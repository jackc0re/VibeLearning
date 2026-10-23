"""
Heaps and Priority Queues - Exercises
=====================================
Six exercises on sift-up, sift-down, kth-largest, merging sorted streams,
a PriorityQueue wrapper class, and validating the heap property.

How this file works:
1. Run it as-is. Every check prints FAIL - that is expected, because every
   function is still a stub. The file still runs to the end and exits 0.
2. Implement one exercise at a time (find its TODO), re-run, and watch its
   checks flip to PASS.
3. Worked solutions are at the bottom. They are verified by their own
   self-check section, so you can always see what passing looks like.
"""

import heapq

print("=" * 50)
print("HEAPS AND PRIORITY QUEUES - Exercises")
print("=" * 50)


# =============================================================================
# TEST HELPER
# =============================================================================
def check(label, got, expected):
    """Print PASS or FAIL for one expected result. Returns True on PASS."""
    if got == expected:
        print(f"PASS {label}")
        return True
    print(f"FAIL {label}: got {got!r}, expected {expected!r}")
    return False


# =============================================================================
# EXERCISE 1: Sift-Up
# =============================================================================
print("\n--- Exercise 1: Sift-Up ---\n")
"""
Implement sift_up(data, i): the value at index i was just appended, and the
list may now violate the min-heap property. While data[i] is smaller than
its parent (at index (i - 1) // 2), swap them and keep climbing. Return the
list when the property holds again.
"""


def sift_up(data, i):
    """Restore the min-heap property by moving data[i] toward the root."""
    # TODO: swap data[i] with its parent while data[i] < data[(i - 1) // 2]
    return None


print("Checks for Exercise 1:")
check("sift_up([3, 5, 8, 1], 3)", sift_up([3, 5, 8, 1], 3), [1, 3, 8, 5])
check("sift_up([1, 3, 2], 2) (no move)", sift_up([1, 3, 2], 2), [1, 3, 2])
check("sift_up([5, 4], 1)", sift_up([5, 4], 1), [4, 5])


# =============================================================================
# EXERCISE 2: Sift-Down
# =============================================================================
print("\n--- Exercise 2: Sift-Down ---\n")
"""
Implement sift_down(data, i): the value at index i was just moved to the
root spot and may be too big. While it is bigger than its smallest child
(left child at 2*i + 1, right child at 2*i + 2), swap it with that SMALLER
child. Picking the left child blindly can break the property! Return the
list when both children are bigger (or there are none).
"""


def sift_down(data, i):
    """Restore the min-heap property by moving data[i] toward the leaves."""
    # TODO: swap with the smaller child until both children are bigger
    return None


print("Checks for Exercise 2:")
check("sift_down([8, 3, 2, 5, 9], 0)", sift_down([8, 3, 2, 5, 9], 0),
      [2, 3, 8, 5, 9])
check("sift_down([9, 5, 8, 3], 0)", sift_down([9, 5, 8, 3], 0), [5, 3, 8, 9])
check("sift_down([1, 5, 2], 0) (no move)", sift_down([1, 5, 2], 0), [1, 5, 2])


# =============================================================================
# EXERCISE 3: Kth Largest With a Heap
# =============================================================================
print("\n--- Exercise 3: Kth Largest With a Heap ---\n")
"""
Implement kth_largest(nums, k): return the k-th largest value in nums
(k = 1 means the maximum). Use heapq - either heapq.nlargest, or push
negated values onto a min-heap. Duplicates count, so the 2nd largest of
[5, 5, 5] is 5.
"""


def kth_largest(nums, k):
    """Return the k-th largest value in nums (1-based)."""
    # TODO: solve it with heapq, not sorted() alone
    return None


print("Checks for Exercise 3:")
check("kth_largest([91, 55, 78, 84, 62], 1)", kth_largest([91, 55, 78, 84, 62], 1), 91)
check("kth_largest([91, 55, 78, 84, 62], 3)", kth_largest([91, 55, 78, 84, 62], 3), 78)
check("kth_largest([5, 5, 5], 2)", kth_largest([5, 5, 5], 2), 5)
check("kth_largest([7], 1)", kth_largest([7], 1), 7)


# =============================================================================
# EXERCISE 4: Merge Two Sorted Streams With a Heap
# =============================================================================
print("\n--- Exercise 4: Merge Two Sorted Streams ---\n")
"""
Implement merge_two_streams(a, b): a and b are already-sorted lists.
Return one sorted list holding all their values, driving the merge with a
HEAP instead of sorted(a + b). Hint: keep a heap of
(value, stream_id, index) triples - pop the smallest, then push that
stream's next value. (In real code, heapq.merge() does this for you.)
"""


def merge_two_streams(a, b):
    """Merge two sorted lists into one sorted list using a heap."""
    # TODO: pop (value, stream_id, index) from a heap, refill from that stream
    return None


print("Checks for Exercise 4:")
check("merge_two_streams([1, 4, 9], [2, 3, 10])",
      merge_two_streams([1, 4, 9], [2, 3, 10]), [1, 2, 3, 4, 9, 10])
check("merge_two_streams([], [1, 2])", merge_two_streams([], [1, 2]), [1, 2])
check("merge_two_streams([5], [5])", merge_two_streams([5], [5]), [5, 5])
check("merge_two_streams([1, 2, 3], [])", merge_two_streams([1, 2, 3], []),
      [1, 2, 3])


# =============================================================================
# EXERCISE 5: PriorityQueue Wrapper Class
# =============================================================================
print("\n--- Exercise 5: PriorityQueue Wrapper Class ---\n")
"""
Build a PriorityQueue class around heapq:
  - push(task, priority): lower number = more urgent
  - pop(): remove and return the most urgent task (None if empty)
  - peek(): most urgent task without removing it (None if empty)
  - __len__(): number of waiting tasks
Store entries as (priority, counter, task) tuples. The counter matters:
tasks here will be DICTS, which cannot be compared - the counter must be
the tie-breaker so the task object is never compared.
"""


class PriorityQueue:
    """A priority queue that never compares its tasks directly."""

    def __init__(self):
        # TODO: store a heap list and a counter
        pass

    def push(self, task, priority):
        # TODO: heappush a (priority, counter, task) tuple
        pass

    def pop(self):
        # TODO: heappop and return just the task (None if empty)
        return None

    def peek(self):
        # TODO: return the front task without removing it (None if empty)
        return None

    def __len__(self):
        # TODO: return the number of waiting tasks
        return 0


print("Checks for Exercise 5:")
pq = PriorityQueue()
pq.push({"job": "clean"}, 3)
pq.push({"job": "alarm"}, 1)
pq.push({"job": "reply"}, 2)
check("len after 3 pushes", len(pq), 3)
check("first pop is the priority-1 task", pq.pop(), {"job": "alarm"})
check("second pop", pq.pop(), {"job": "reply"})
check("third pop", pq.pop(), {"job": "clean"})
check("pop on empty returns None", pq.pop(), None)
check("peek on empty returns None", pq.peek(), None)

pq = PriorityQueue()
pq.push({"a": 1}, 5)
pq.push({"b": 2}, 5)
check("tie broken by arrival, not by comparing dicts", pq.pop(), {"a": 1})


# =============================================================================
# EXERCISE 6: Is It a Min-Heap?
# =============================================================================
print("\n--- Exercise 6: Is It a Min-Heap? ---\n")
"""
Implement is_min_heap(data): return True if the list satisfies the min-heap
property - every parent (index (i - 1) // 2) must be <= its children.
An empty list and a single-element list are both valid heaps. Remember: the
array does NOT have to be sorted, so do not check that!
"""


def is_min_heap(data):
    """Return True if data satisfies the min-heap property."""
    # TODO: check every child against its parent
    return None


print("Checks for Exercise 6:")
check("is_min_heap([1, 3, 2, 7, 4, 6, 8])",
      is_min_heap([1, 3, 2, 7, 4, 6, 8]), True)
check("is_min_heap([1, 2, 3, 0])", is_min_heap([1, 2, 3, 0]), False)
check("is_min_heap([])", is_min_heap([]), True)
check("is_min_heap([42])", is_min_heap([42]), True)
check("is_min_heap([2, 1])", is_min_heap([2, 1]), False)


# =============================================================================
# SOLUTIONS
# =============================================================================
# Worked answers to all six exercises. They shadow the stubs above (the
# stubs have already been checked by now), and the self-check at the very
# bottom verifies them so you can see what passing output looks like.

print("\n--- Solutions ---\n")


def sift_up(data, i):
    """Restore the min-heap property by moving data[i] toward the root."""
    while i > 0:
        parent = (i - 1) // 2
        if data[i] < data[parent]:
            data[i], data[parent] = data[parent], data[i]
            i = parent
        else:
            break
    return data


def sift_down(data, i):
    """Restore the min-heap property by moving data[i] toward the leaves."""
    n = len(data)
    while True:
        left, right = 2 * i + 1, 2 * i + 2
        smallest = i
        if left < n and data[left] < data[smallest]:
            smallest = left
        if right < n and data[right] < data[smallest]:
            smallest = right
        if smallest == i:
            return data
        data[i], data[smallest] = data[smallest], data[i]
        i = smallest


def kth_largest(nums, k):
    """Return the k-th largest value in nums (1-based)."""
    heap = [-value for value in nums]     # negate: max-heap becomes min-heap
    heapq.heapify(heap)
    for _ in range(k - 1):
        heapq.heappop(heap)
    return -heapq.heappop(heap)


def merge_two_streams(a, b):
    """Merge two sorted lists into one sorted list using a heap."""
    result = []
    streams = {0: a, 1: b}
    stream_heap = []                      # holds (value, stream_id, index)
    for stream_id in (0, 1):
        if streams[stream_id]:
            heapq.heappush(stream_heap, (streams[stream_id][0], stream_id, 0))
    while stream_heap:
        value, stream_id, index = heapq.heappop(stream_heap)
        result.append(value)
        nxt = index + 1
        if nxt < len(streams[stream_id]):
            heapq.heappush(
                stream_heap, (streams[stream_id][nxt], stream_id, nxt)
            )
    return result


class PriorityQueue:
    """A priority queue that never compares its tasks directly."""

    def __init__(self):
        self._heap = []
        self._counter = 0                 # tie-breaker: arrival order

    def push(self, task, priority):
        heapq.heappush(self._heap, (priority, self._counter, task))
        self._counter += 1

    def pop(self):
        if not self._heap:
            return None
        priority, _, task = heapq.heappop(self._heap)
        return task

    def peek(self):
        if not self._heap:
            return None
        priority, _, task = self._heap[0]
        return task

    def __len__(self):
        return len(self._heap)


def is_min_heap(data):
    """Return True if data satisfies the min-heap property."""
    for i in range(1, len(data)):
        if data[(i - 1) // 2] > data[i]:
            return False
    return True


# =============================================================================
# SOLUTION SELF-CHECK
# =============================================================================
print("--- Solution self-check (what passing looks like) ---\n")

check("solution sift_up([3, 5, 8, 1], 3)", sift_up([3, 5, 8, 1], 3), [1, 3, 8, 5])
check("solution sift_down([8, 3, 2, 5, 9], 0)",
      sift_down([8, 3, 2, 5, 9], 0), [2, 3, 8, 5, 9])
check("solution kth_largest([91, 55, 78, 84, 62], 3)",
      kth_largest([91, 55, 78, 84, 62], 3), 78)
check("solution merge_two_streams([1, 4, 9], [2, 3, 10])",
      merge_two_streams([1, 4, 9], [2, 3, 10]), [1, 2, 3, 4, 9, 10])

solution_pq = PriorityQueue()
solution_pq.push({"job": "clean"}, 3)
solution_pq.push({"job": "alarm"}, 1)
check("solution PriorityQueue order", solution_pq.pop(), {"job": "alarm"})
check("solution PriorityQueue length", len(solution_pq), 1)

check("solution is_min_heap([1, 3, 2, 7, 4, 6, 8])",
      is_min_heap([1, 3, 2, 7, 4, 6, 8]), True)
check("solution is_min_heap([1, 2, 3, 0])", is_min_heap([1, 2, 3, 0]), False)

print("\n" + "=" * 50)
print("Great job! Check yourself with quiz.md next.")
print("=" * 50)
