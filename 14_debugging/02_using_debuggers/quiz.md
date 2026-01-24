# 🧠 Using Debuggers Quiz

---

## Question 1
What does `breakpoint()` do in Python 3.7+?

- A) Stops the program permanently
- B) Pauses execution and enters the debugger
- C) Prints the current line number
- D) Creates a checkpoint to restore later

<details>
<summary>Show Answer</summary>

**B)** `breakpoint()` pauses execution and drops you into the Python debugger (pdb by default), where you can inspect variables and step through code.

</details>

---

## Question 2
What's the difference between `n` (next) and `s` (step) in pdb?

- A) `n` is faster than `s`
- B) `n` steps OVER function calls, `s` steps INTO them
- C) `n` goes to next breakpoint, `s` goes to next line
- D) They do the same thing

<details>
<summary>Show Answer</summary>

**B)** `n` (next) executes the line and stops at the next line in the current function. `s` (step) enters function calls, allowing you to debug inside them.

</details>

---

## Question 3
How do you view the current call stack in pdb?

- A) `stack`
- B) `w` or `where`
- C) `trace`
- D) `bt`

<details>
<summary>Show Answer</summary>

**B)** The `w` or `where` command shows the call stack, with the current frame marked. You can then use `u` (up) and `d` (down) to navigate.

</details>

---

## Question 4
How can you disable `breakpoint()` calls without modifying code?

- A) Set `DEBUG=False`
- B) Set `PYTHONBREAKPOINT=0` environment variable
- C) Run Python with `--no-debug` flag
- D) It's not possible

<details>
<summary>Show Answer</summary>

**B)** Setting `PYTHONBREAKPOINT=0` disables all `breakpoint()` calls. This is useful for running code in production that has debug breakpoints.

</details>

---

## Question 5
What does `pdb.post_mortem()` do?

- A) Cleans up after debugging
- B) Saves the debug session to a file
- C) Enters debugger at the point where an exception occurred
- D) Automatically fixes bugs

<details>
<summary>Show Answer</summary>

**C)** `pdb.post_mortem()` lets you debug after an exception has occurred, allowing you to inspect the state at the point of failure.

</details>

---

[Back to Using Debuggers README](README.md)
