# 🔄 Itertools Module - Quiz

Test your knowledge of itertools!

---

## Question 1
**What does `itertools.count(10, 2)` produce?**

A) [10, 12, 14, 16, ...] up to infinity
B) [10, 11, 12, 13, ...] up to infinity
C) [2, 4, 6, 8, 10]
D) [10]

<details>
<summary>Click for answer</summary>

**A) [10, 12, 14, 16, ...] up to infinity**

`count(10, 2)` starts at 10 and counts by 2 indefinitely.
</details>

---

## Question 2
**What is the difference between `permutations` and `combinations`?**

A) None, they are the same
B) Permutations considers order, combinations does not
C) Combinations is faster
D) Permutations allows repetition

<details>
<summary>Click for answer</summary>

**B) Permutations considers order, combinations does not**

`(A, B)` and `(B, A)` are different permutations but the same combination.
</details>

---

## Question 3
**What does `itertools.chain([1, 2], [3, 4])` return?**

A) [(1, 2), (3, 4)]
B) [[1, 2], [3, 4]]
C) An iterator yielding 1, 2, 3, 4
D) [(1, 3), (2, 4)]

<details>
<summary>Click for answer</summary>

**C) An iterator yielding 1, 2, 3, 4**

`chain` concatenates iterables into a single iterator.
</details>

---

## Question 4
**When using `groupby`, what must you do first?**

A) Convert to list
B) Sort the data by the grouping key
C) Reverse the data
D) Nothing, it works on any data

<details>
<summary>Click for answer</summary>

**B) Sort the data by the grouping key**

`groupby` only groups consecutive equal elements, so sorting is usually necessary.
</details>

---

## Question 5
**What is `zip_longest` useful for?**

A) Making longer lists
B) Zipping iterables of different lengths without truncation
C) Sorting zipped iterables
D) Reversing zip operations

<details>
<summary>Click for answer</summary>

**B) Zipping iterables of different lengths without truncation**

`zip_longest` continues until the longest iterable is exhausted, filling missing values.
</details>

---

## Question 6
**What does `islice(count(), 5, 10)` return?**

A) 0, 1, 2, 3, 4
B) 5, 6, 7, 8, 9
C) 5, 6, 7, 8, 9, 10
D) Error

<details>
<summary>Click for answer</summary>

**B) 5, 6, 7, 8, 9**

`islice(start, stop)` - starts at index 5, stops before 10.
</details>

---

## Question 7
**Which itertools function creates the Cartesian product?**

A) `chain`
B) `product`
C) `zip`
D) `compress`

<details>
<summary>Click for answer</summary>

**B) `product`**

`product(A, B)` generates all pairs (a, b) where a is from A and b is from B.
</details>

---

## Question 8
**What does `cycle(['a', 'b'])` do?**

A) Returns ['a', 'b', 'a', 'b'] once
B) Repeats 'a', 'b' indefinitely
C) Returns ['a', 'b']
D) Returns ['b', 'a']

<details>
<summary>Click for answer</summary>

**B) Repeats 'a', 'b' indefinitely**

`cycle` infinitely repeats the sequence.
</details>

---

## Question 9
**What is the output of `list(combinations([1, 2, 3], 2))`?**

A) [(1, 2), (1, 3), (2, 3)]
B) [(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)]
C) [(1, 1), (2, 2), (3, 3)]
D) [(1, 2, 3)]

<details>
<summary>Click for answer</summary>

**A) [(1, 2), (1, 3), (2, 3)]**

Combinations don't consider order, so (1, 2) is the same as (2, 1).
</details>

---

## Question 10
**Which function filters elements using a selector list?**

A) `filter`
B) `compress`
C) `dropwhile`
D) `filterfalse`

<details>
<summary>Click for answer</summary>

**B) `compress`**

`compress(data, selectors)` returns elements from data where the corresponding selector is True.
</details>

---

**How did you do?** Check `examples.py` for more practice!
