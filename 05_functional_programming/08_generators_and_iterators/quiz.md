# 🧠 Generators and Iterators Quiz

Test your understanding of generators and iterators.

---

## Question 1
What is the first thing a `for` loop does with an iterable?

- A) Prints it
- B) Calls `iter()` to get an iterator
- C) Calls `len()` on it
- D) Copies it into a list

<details>
<summary>Show Answer</summary>

**B)** `for` calls `iter()` once, then `next()` repeatedly until `StopIteration`.

</details>

---

## Question 2
Which exception tells a `for` loop that there are no more values?

- A) `ValueError`
- B) `IndexError`
- C) `StopIteration`
- D) `KeyError`

<details>
<summary>Show Answer</summary>

**C)** `StopIteration` is the "no more values" signal raised by an iterator's
`__next__`.

</details>

---

## Question 3
What happens when you *call* a generator function, e.g. `gen = my_gen()`?

- A) The whole function body runs immediately
- B) A generator object is returned and the body has not started yet
- C) It returns the first yielded value
- D) It raises `TypeError`

<details>
<summary>Show Answer</summary>

**B)** Calling a generator function creates a generator object; the body only runs
when you pull values with `next()` or a `for` loop.

</details>

---

## Question 4
What is the difference between `[x * x for x in range(3)]` and
`(x * x for x in range(3))`?

- A) No difference, just style
- B) The brackets version is faster to type but wrong
- C) Brackets build the whole list now; parentheses give a lazy generator
- D) Parentheses create a tuple of results

<details>
<summary>Show Answer</summary>

**C)** Square brackets are a list comprehension (all values built immediately);
round parentheses are a generator expression (values produced one at a time, on
demand).

</details>

---

## Question 5
You iterate a generator to the end, then iterate it a second time. What do you get?

- A) The same values again
- B) Nothing - the generator is exhausted
- C) An exception
- D) The generator restarts from the beginning

<details>
<summary>Show Answer</summary>

**B)** Generators are one-shot. Once exhausted, every later pass is empty. Use a list
if you need to walk the values twice.

</details>

---

## Question 6
What does `next(it, "done")` return when `it` has no values left?

- A) It raises `StopIteration`
- B) `None`
- C) `"done"`
- D) `0`

<details>
<summary>Show Answer</summary>

**C)** `next(it, default)` returns the default instead of raising `StopIteration`.

</details>

---

## Question 7
What does `yield from sublist` do inside a generator?

- A) Yields the `sublist` object itself
- B) Yields every item of `sublist`, one by one
- C) Returns from the function immediately
- D) Turns `sublist` into a generator

<details>
<summary>Show Answer</summary>

**B)** `yield from` delegates to another iterable - it is shorthand for the inner
`for item in sublist: yield item` loop.

</details>

---

## Question 8
For the numbers 0..999999, which uses far less memory?

- A) `[x * 2 for x in range(1_000_000)]`
- B) `(x * 2 for x in range(1_000_000))`
- C) They are the same size

<details>
<summary>Show Answer</summary>

**B)** The list stores all million values (megabytes); the generator expression
stores only its recipe (about 200 bytes) and computes each value on demand.

</details>

---

[Back to Generators and Iterators README](README.md)
