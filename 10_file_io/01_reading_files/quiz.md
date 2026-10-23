# 🧠 Reading Files Quiz

---

## Question 1
Why is `with open(...) as f:` recommended?

- A) It makes files load faster
- B) It automatically closes the file even if an error happens
- C) It prevents all exceptions
- D) It encrypts the file

<details>
<summary>Show Answer</summary>

**B)** The context manager closes the file reliably.

</details>

---

## Question 2
Which is the most memory-friendly way to process a huge text file?

- A) `f.read()`
- B) `f.readlines()`
- C) `for line in f:`
- D) `json.load(f)`

<details>
<summary>Show Answer</summary>

**C)** Iterating line-by-line avoids loading the entire file at once.

</details>

---

## Question 3
What does `encoding="utf-8"` affect?

- A) How Python stores integers
- B) How bytes are decoded into text (characters)
- C) The file extension
- D) The file permissions

<details>
<summary>Show Answer</summary>

**B)** Encoding defines how to interpret bytes as characters.

</details>

---

## Question 4
What does `f.readline()` return when the file has no more lines?

- A) `None`
- B) An empty string `""`
- C) It raises `EOFError`
- D) The last line again

<details>
<summary>Show Answer</summary>

**B)** At end-of-file, `readline()` returns an empty string `""` — this is the
classic signal used in `while` loops (`if not line: break`).

</details>

---

## Question 5
What happens if you call `open("missing.txt", "r", encoding="utf-8")` and the file does not exist?

- A) An empty file is created
- B) The program returns `None`
- C) It raises `FileNotFoundError`
- D) It raises `PermissionError`

<details>
<summary>Show Answer</summary>

**C)** Reading a non-existent path raises `FileNotFoundError`. Only write modes
like `"w"` or `"a"` create the file.

</details>

---

## Question 6
After `with open("notes.txt") as f:` block ends, what is true about `f`?

- A) The file content disappears from disk
- B) The file is closed — further reads raise `ValueError: I/O operation on closed file`
- C) The file stays open until the program exits
- D) `f` becomes `None`

<details>
<summary>Show Answer</summary>

**B)** The `with` block closes the file. Using `f` afterwards (e.g. `f.read()`)
raises `ValueError` because the file is closed.

</details>

---

[Back to Reading Files README](README.md)
