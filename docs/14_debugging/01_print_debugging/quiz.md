# 🧠 Print Debugging Quiz

---

## Question 1
What does `print(f"{x=}")` output when x=42?

- A) `42`
- B) `x42`
- C) `x=42`
- D) `{x=42}`

<details>
<summary>Show Answer</summary>

**C)** The `=` inside f-strings (Python 3.8+) automatically includes the variable name and its value: `x=42`

</details>

---

## Question 2
What does `!r` do in an f-string like `f"{name!r}"`?

- A) Makes the output red
- B) Reverses the string
- C) Uses repr() instead of str()
- D) Removes quotes

<details>
<summary>Show Answer</summary>

**C)** The `!r` conversion uses `repr()` instead of `str()`. For strings, this shows quotes: `f"{'hello'!r}"` outputs `'hello'` with quotes.

</details>

---

## Question 3
Why might you prefer `logging` over `print()` for debugging?

- A) logging is faster
- B) logging can be turned on/off without changing code
- C) print doesn't work in Python 3
- D) logging uses less memory

<details>
<summary>Show Answer</summary>

**B)** The logging module can be configured to show or hide messages based on level, and can output to different destinations, all without modifying the debug statements themselves.

</details>

---

## Question 4
What's the main drawback of print debugging?

- A) Print statements are slow
- B) You must remember to remove debug prints before committing
- C) Print only works with strings
- D) Print can't show variable values

<details>
<summary>Show Answer</summary>

**B)** The main drawback is that debug print statements can be accidentally left in code. They clutter output and may expose sensitive information.

</details>

---

## Question 5
When tracing function execution, what should you print?

- A) Only the final result
- B) Entry, exit, and key state changes
- C) Every single line of code
- D) Only errors

<details>
<summary>Show Answer</summary>

**B)** Effective tracing shows function entry (with arguments), exit (with return value), and important state changes. Too much output is as bad as too little.

</details>

---

[Back to Print Debugging README](README.md)
