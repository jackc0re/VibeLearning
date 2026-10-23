# 🧠 Context Managers Quiz

Check your understanding of `with`, `__enter__`/`__exit__`, and contextlib helpers.

---

## Question 1
What does the `with` statement guarantee?

- A) The body never raises an exception
- B) `__exit__` runs even if the body raises
- C) The code runs faster
- D) The object is copied before use

<details>
<summary>Show Answer</summary>

**B)** The whole point of a context manager is that cleanup (`__exit__`)
happens on success *and* on failure — it is `try/finally` built into the
language.

</details>

---

## Question 2
What is bound to the name after `as`?

- A) The context manager class
- B) Whatever `__enter__` returns
- C) Whatever `__exit__` returns
- D) The exception, if one occurs

<details>
<summary>Show Answer</summary>

**B)** `__enter__`'s return value is bound by `as`. Classes usually return
`self`; `open()` returns the file object.

</details>

---

## Question 3
The body raises `ValueError("boom")`. What does `__exit__` receive?

- A) Nothing — `__exit__` is skipped when the body raises
- B) Only the error message string
- C) The exception type, the exception value, and the traceback
- D) Three empty strings

<details>
<summary>Show Answer</summary>

**C)** `__exit__(exc_type, exc_val, exc_tb)` gets the type (`ValueError`),
the value (the `ValueError("boom")` instance), and the traceback. On a clean
exit, all three are `None`.

</details>

---

## Question 4
What happens if `__exit__` returns `True` while an exception is in flight?

- A) Nothing — the return value is ignored
- B) The exception is suppressed and execution continues
- C) The exception is raised again after the block
- D) Python exits the program

<details>
<summary>Show Answer</summary>

**B)** Returning `True` suppresses the exception. It hides *every* error,
including real bugs, so use it sparingly — `contextlib.suppress` with a
specific type is usually the right tool.

</details>

---

## Question 5
`__exit__` has no `return` statement and an exception is in flight. What happens?

- A) The exception is suppressed
- B) The exception propagates normally
- C) Python raises a `SyntaxError`
- D) The exception is converted to a warning

<details>
<summary>Show Answer</summary>

**B)** A function with no `return` returns `None`, and `None` means "do not
suppress" — which is usually exactly what you want. Only `True` suppresses.

</details>

---

## Question 6
In a `@contextmanager` generator, what does the `yield` mark?

- A) Where the function returns its final value
- B) Where the `with` body runs
- C) The end of the program
- D) An optional cleanup step

<details>
<summary>Show Answer</summary>

**B)** Code before the `yield` acts as `__enter__`, the body runs at the
`yield`, and code after it acts as `__exit__`. Wrap the `yield` in
`try/finally` so the cleanup runs even when the body raises.

</details>

---

## Question 7
When is `contextlib.suppress` the right tool?

- A) To hide every possible bug in a block
- B) To ignore one specific, expected exception type
- C) To make the program exit silently
- D) To retry a failed operation

<details>
<summary>Show Answer</summary>

**B)** `with suppress(FileNotFoundError):` documents exactly which error is
okay and lets everything else propagate — much safer than a bare
`except: pass`.

</details>

---

## Question 8
When do you need `ExitStack` instead of `with a, b, c:`?

- A) When the managers raise exceptions
- B) When the number of managers is not known until runtime
- C) When you want the managers to exit in random order
- D) When the managers are generator-based

<details>
<summary>Show Answer</summary>

**B)** `with a, b, c:` needs the names in advance. `ExitStack.enter_context`
registers any number of managers at runtime and exits them all — in reverse
order — when the block ends.

</details>

---

[Back to Context Managers README](README.md) | [Next: Why Testing →](../../09_testing/01_why_testing/README.md)
