# 🧠 Common Bugs Quiz

---

## Question 1
What's wrong with this function definition?

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

- A) Lists can't be default arguments
- B) The default list is shared across all calls
- C) append() doesn't work on default arguments
- D) Nothing, it's correct

<details>
<summary>Show Answer</summary>

**B)** The default list `[]` is created once when the function is defined, not on each call. All calls share the same list, causing items to accumulate unexpectedly.

</details>

---

## Question 2
Why does this loop miss some items?

```python
items = [2, 4, 6, 8]
for item in items:
    items.remove(item)
```

- A) remove() is slow
- B) Modifying a list while iterating causes skipped items
- C) The for loop is wrong syntax
- D) remove() doesn't work with integers

<details>
<summary>Show Answer</summary>

**B)** When you remove an item, the list shifts. The iterator doesn't know and skips the next item. After removing 2, index 0 now holds 4, but the iterator moves to index 1 (which is 6).

</details>

---

## Question 3
What's the bug in this closure?

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)
print([f() for f in funcs])
```

- A) lambda can't be used in loops
- B) All lambdas capture the final value of i (late binding)
- C) The list comprehension is wrong
- D) range(3) is incorrect

<details>
<summary>Show Answer</summary>

**B)** All lambdas capture the variable `i`, not its value. When called, they all see `i=2` (the final value). Fix with `lambda i=i: i` to capture the current value.

</details>

---

## Question 4
What does `[1, 2].copy()` create for nested lists like `[[1, 2], [3, 4]]`?

- A) A completely independent copy
- B) A shallow copy - inner lists are still shared
- C) An error - nested lists can't be copied
- D) A frozen copy that can't be modified

<details>
<summary>Show Answer</summary>

**B)** `.copy()` creates a shallow copy. The outer list is new, but the inner lists are the same objects. Use `copy.deepcopy()` for nested structures.

</details>

---

## Question 5
What's the correct way to check if a variable is None?

- A) `if x == None:`
- B) `if x is None:`
- C) `if None in x:`
- D) `if not x:`

<details>
<summary>Show Answer</summary>

**B)** Use `is` for None comparisons. `is` checks identity (same object), while `==` checks equality. None is a singleton, so `is None` is more explicit and slightly faster.

</details>

---

[Back to Common Bugs README](README.md)
