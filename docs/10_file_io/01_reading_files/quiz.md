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

[Back to Reading Files README](README.md)

