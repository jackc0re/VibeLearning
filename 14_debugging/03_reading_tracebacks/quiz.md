# 🧠 Reading Tracebacks Quiz

---

## Question 1
In which order should you read a Python traceback?

- A) Top to bottom
- B) Bottom to top
- C) Middle outward
- D) It doesn't matter

<details>
<summary>Show Answer</summary>

**B)** Read tracebacks bottom to top. The exception type/message is at the bottom, telling you what happened. The frames above show how you got there.

</details>

---

## Question 2
What does this traceback tell you: `KeyError: 'username'`?

- A) The variable 'username' is not defined
- B) The key 'username' was not found in a dictionary
- C) The string 'username' has an error
- D) A function named 'username' doesn't exist

<details>
<summary>Show Answer</summary>

**B)** A `KeyError` means you tried to access a dictionary key that doesn't exist. The code tried `some_dict['username']` but that key wasn't present.

</details>

---

## Question 3
What does `AttributeError: 'NoneType' object has no attribute 'split'` mean?

- A) The split function is broken
- B) You called .split() on a variable that is None
- C) NoneType is not a valid type
- D) The attribute 'split' doesn't exist in Python

<details>
<summary>Show Answer</summary>

**B)** The variable you called `.split()` on is `None`. Somewhere upstream, a function returned `None` instead of the string you expected.

</details>

---

## Question 4
In this traceback frame, what line caused the error?

```
  File "app/views.py", line 42, in get_user
    return users[name]
```

- A) Line 41
- B) Line 42
- C) Line 43
- D) Cannot determine

<details>
<summary>Show Answer</summary>

**B)** Line 42. The frame shows `line 42` and even displays the code on that line (`return users[name]`). This is where the error occurred.

</details>

---

## Question 5
What does "During handling of the above exception, another exception occurred" mean?

- A) Two separate errors happened at the same time
- B) An exception occurred while inside an except block handling another exception
- C) The same exception happened twice
- D) Python couldn't determine which exception occurred

<details>
<summary>Show Answer</summary>

**B)** This indicates exception chaining - while handling one exception (in an except block), another exception was raised. Read both tracebacks to understand the full picture.

</details>

---

[Back to Reading Tracebacks README](README.md)
