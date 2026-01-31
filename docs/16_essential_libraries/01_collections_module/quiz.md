# 📊 Collections Module - Quiz

Test your knowledge of the collections module!

---

## Question 1
**What does `Counter` return for elements that don't exist in the count?**

A) KeyError
B) 0
C) None
D) Empty list

<details>
<summary>Click for answer</summary>

**B) 0**

Counter returns 0 for missing keys instead of raising KeyError, similar to defaultdict.
</details>

---

## Question 2
**Which of these is the best use case for `deque` over a regular list?**

A) Sorting elements
B) Frequent appends/pops from both ends
C) Random access by index
D) Finding elements by value

<details>
<summary>Click for answer</summary>

**B) Frequent appends/pops from both ends**

Deque is O(1) for operations at both ends, while list is O(n) for operations at the beginning.
</details>

---

## Question 3
**What is the output of this code?**
```python
from collections import defaultdict
d = defaultdict(list)
print(d['missing'])
```

A) KeyError
B) []
C) None
D) 'missing'

<details>
<summary>Click for answer</summary>

**B) []**

`defaultdict(list)` calls `list()` (which returns []) when a key is missing.
</details>

---

## Question 4
**Can you modify a field in a namedtuple after creation?**

A) Yes, using dot notation
B) Yes, using index assignment
C) No, namedtuples are immutable
D) Only if you use mutable fields

<details>
<summary>Click for answer</summary>

**C) No, namedtuples are immutable**

Like regular tuples, namedtuples are immutable. Use `_replace()` to create a new instance with modified values.
</details>

---

## Question 5
**What is the most common way to find the top 3 elements in a Counter?**

A) `counter.top(3)`
B) `counter.most_common(3)`
C) `sorted(counter)[:3]`
D) `counter[:3]`

<details>
<summary>Click for answer</summary>

**B) `counter.most_common(3)`**

`most_common(n)` returns the n most common elements as a list of (element, count) tuples.
</details>

---

## Question 6
**What happens when you create a deque with `maxlen=3` and add a 4th element?**

A) Raises an error
B) Ignores the new element
C) Automatically removes the oldest element
D) Grows beyond the limit

<details>
<summary>Click for answer</summary>

**C) Automatically removes the oldest element**

Deque with maxlen acts as a circular buffer, automatically discarding elements from the opposite end when full.
</details>

---

## Question 7
**Which factory function would you use with defaultdict to automatically create nested dictionaries?**

A) `dict`
B) `lambda: defaultdict(dict)`
C) `list`
D) `set`

<details>
<summary>Click for answer</summary>

**B) `lambda: defaultdict(dict)`**

For nested structures, you need a lambda that returns a new defaultdict.
</details>

---

## Question 8
**What is the advantage of namedtuple over a regular class?**

A) It's mutable
B) It uses less memory
C) It has methods for database access
D) It supports inheritance better

<details>
<summary>Click for answer</summary>

**B) It uses less memory**

Namedtuples are lightweight and memory-efficient compared to regular classes because they don't have a per-instance `__dict__`.
</details>

---

## Question 9
**What does `Counter.elements()` return?**

A) A list of unique elements
B) An iterator over elements repeating each as many times as its count
C) The count of all elements
D) A sorted list of elements

<details>
<summary>Click for answer</summary>

**B) An iterator over elements repeating each as many times as its count**

`elements()` expands the Counter back to the original iterable.
</details>

---

## Question 10
**Which collections class is best for implementing a LRU (Least Recently Used) cache?**

A) Counter
B) defaultdict
C) OrderedDict (or dict in Python 3.7+)
D) deque with maxlen

<details>
<summary>Click for answer</summary>

**C) OrderedDict (or dict in Python 3.7+)**

While deque can work, OrderedDict (or regular dict in Python 3.7+) combined with move_to_end() is the standard approach for LRU cache implementation.
</details>

---

**How did you do?** Check `examples.py` for more practice!
