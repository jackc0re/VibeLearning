# 📝 Dictionaries and Maps - Quiz

Test your understanding! Try to answer without looking back.

---

## Question 1
What will this code print?
```python
d = {"a": 1, "b": 2}
print(d.get("c", 0))
```

A) None  
B) 0  
C) KeyError  
D) "c"

<details>
<summary>Click for answer</summary>

**B) 0**

`get()` returns the default value (0) when the key doesn't exist, unlike bracket notation which raises KeyError.

</details>

---

## Question 2
What is the output?
```python
d = {"a": 1, "b": 2, "c": 3}
print(list(d.keys()))
```

A) [1, 2, 3]  
B) ["a", "b", "c"]  
C) [("a", 1), ("b", 2), ("c", 3)]  
D) {"a", "b", "c"}

<details>
<summary>Click for answer</summary>

**B) ["a", "b", "c"]**

`keys()` returns a view of dictionary keys. Use `values()` for values or `items()` for key-value tuples.

</details>

---

## Question 3
Which of these is NOT a valid dictionary key?
```python
# Which would cause an error?
d = {}
d[1] = "int key"
d["a"] = "string key"
d[(1, 2)] = "tuple key"
d[[1, 2]] = "list key"
```

A) Integer  
B) String  
C) Tuple  
D) List

<details>
<summary>Click for answer</summary>

**D) List**

Dictionary keys must be hashable (immutable). Lists are mutable, so they can't be keys. Tuples work because they're immutable.

</details>

---

## Question 4
What will `d.pop("x")` do if "x" doesn't exist?

A) Return None  
B) Return an empty dict  
C) Raise KeyError  
D) Do nothing

<details>
<summary>Click for answer</summary>

**C) Raise KeyError**

Unlike `get()`, `pop()` raises KeyError when the key doesn't exist. Use `d.pop("x", default_value)` to provide a default.

</details>

---

## Question 5
What is the result?
```python
d = {"a": 1}
d.update({"b": 2, "a": 9})
print(d)
```

A) {"a": 1, "b": 2}  
B) {"a": 9, "b": 2}  
C) {"a": 1, "b": 2, "a": 9}  
D) Error

<details>
<summary>Click for answer</summary>

**B) {"a": 9, "b": 2}**

`update()` adds new keys and overwrites existing ones. The value of "a" changes from 1 to 9.

</details>

---

## Question 6
How do you safely access a nested value?
```python
data = {"a": {"b": 1}}
```

A) `data["a"]["x"]`  
B) `data.get("a").get("x")`  
C) `data.get("a", {}).get("x")`  
D) `data["a"].get("x")`

<details>
<summary>Click for answer</summary>

**C) `data.get("a", {}).get("x")`**

This safely handles missing keys at any level. Option B would fail if "a" doesn't exist (None has no .get method).

</details>

---

## Question 7
What does this dictionary comprehension create?
```python
result = {x: x**2 for x in range(3)}
```

A) {0: 0, 1: 1, 2: 4}  
B) {1: 1, 2: 4, 3: 9}  
C) [0, 1, 4]  
D) {0, 1, 4}

<details>
<summary>Click for answer</summary>

**A) {0: 0, 1: 1, 2: 4}**

`range(3)` produces 0, 1, 2. Each becomes a key with its square as the value.

</details>

---

## Question 8
What happens here?
```python
d = {"a": 1, "b": 2}
for key in d:
    if d[key] == 1:
        del d[key]
```

A) d becomes {"b": 2}  
B) RuntimeError  
C) d is unchanged  
D) KeyError

<details>
<summary>Click for answer</summary>

**B) RuntimeError**

You can't modify a dictionary's size while iterating over it. Use `for key in list(d.keys())` instead.

</details>

---

## Question 9
What is `"key" in d` checking?

A) If "key" is a value in d  
B) If "key" is a key in d  
C) If "key" is anywhere in d  
D) If d contains the string "key"

<details>
<summary>Click for answer</summary>

**B) If "key" is a key in d**

The `in` operator checks dictionary keys. To check values, use `"value" in d.values()`.

</details>

---

## Question 10
What's the difference between `d.copy()` and `d`?
```python
original = {"a": [1, 2, 3]}
shallow = original.copy()
shallow["a"].append(4)
print(original["a"])
```

A) [1, 2, 3]  
B) [1, 2, 3, 4]  
C) Error  
D) None

<details>
<summary>Click for answer</summary>

**B) [1, 2, 3, 4]**

`copy()` creates a shallow copy — the dictionary is new, but nested objects are shared. For full independence, use `copy.deepcopy()`.

</details>

---

## How did you do?

- **9-10 correct:** Excellent! You've mastered dictionaries.
- **7-8 correct:** Good job! Review the ones you missed.
- **5-6 correct:** Keep practicing with the examples.
- **0-4 correct:** Re-read the README and run the examples again.
