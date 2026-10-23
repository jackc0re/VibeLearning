# 📝 Heaps and Priority Queues - Quiz

---

## Question 1
In a min-heap stored as an array, which position is guaranteed to hold the minimum?

A) The middle of the array  
B) The last element  
C) Index 0  
D) Any leaf

<details>
<summary>Click for answer</summary>

**C) Index 0**

The root has no parent, so nothing can be smaller. The rest of the array is NOT sorted.

</details>

---

## Question 2
The children of the node at index `i` live at indices...?

A) `i + 1` and `i + 2`  
B) `2*i + 1` and `2*i + 2`  
C) `i // 2` and `i // 2 + 1`  
D) `2*i` and `2*i + 1`

<details>
<summary>Click for answer</summary>

**B) `2*i + 1` and `2*i + 2`**

The parent is at `(i - 1) // 2` - that one formula is the whole tree.

</details>

---

## Question 3
What is the cost of `peek` (looking at, not removing, the minimum)?

A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n log n)

<details>
<summary>Click for answer</summary>

**A) O(1)**

It just sits at index 0 - no sifting, no searching.

</details>

---

## Question 4
What is the cost of `heapq.heappush` on a heap with n items?

A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n²)

<details>
<summary>Click for answer</summary>

**B) O(log n)**

Sift-up swaps along one root-to-leaf path, and a complete tree has height about log2(n).

</details>

---

## Question 5
Which call rearranges an existing list into a valid heap in place, in O(n)?

A) `heapq.sort(heap)`  
B) `heapq.heapify(heap)`  
C) `heapq.nsmallest(len(heap), heap)`  
D) `sorted(heap)`

<details>
<summary>Click for answer</summary>

**B) `heapq.heapify(heap)`**

It reorders the list in place in O(n) - cheaper than n separate pushes.

</details>

---

## Question 6
Why does the task-scheduler idiom use `(priority, counter, task)` tuples instead of `(priority, task)`?

A) Tuples of length 3 are faster to compare  
B) The counter uses less memory than the task  
C) On a priority tie, the counter is compared instead of the task, which may not support `<`  
D) heapq only accepts integer elements

<details>
<summary>Click for answer</summary>

**C) On a priority tie, the counter is compared instead of the task**

Tuples compare element by element. Without the counter, a tie would compare the tasks themselves - dicts, functions, and most objects raise `TypeError`. The counter also keeps equal-priority tasks in arrival order.

</details>

---

## Question 7
Is `[1, 3, 2, 7, 4, 6, 8]` a valid min-heap?

A) No - the array is not sorted  
B) No - index 1 should hold the second-smallest value  
C) Yes - every parent is <= its children  
D) No - it has no valid tree shape

<details>
<summary>Click for answer</summary>

**C) Yes**

Check the pairs: 1 <= 3, 1 <= 2, 3 <= 7, 3 <= 4, 2 <= 6, 2 <= 8. A heap never promises sorted order - only parent <= children.

</details>

---

## Question 8
How do you get max-heap behavior out of Python's min-heap-based `heapq`?

A) Reverse the list after every push  
B) Negate values on the way in and negate the result on the way out  
C) Use `heapq.nlargest` for every operation  
D) You cannot - write a class from scratch

<details>
<summary>Click for answer</summary>

**B) Negate values on the way in and negate the result on the way out**

`heappush(heap, -value)` makes the biggest value the smallest after negation, so it sits at index 0; `-heappop(heap)` restores it.

</details>

---

## How did you do?

- **7-8 correct:** Excellent!
- **5-6 correct:** Good, review the ones you missed.
- **0-4 correct:** Re-read the README, then try again.
