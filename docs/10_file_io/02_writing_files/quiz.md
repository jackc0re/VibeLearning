# 🧠 Writing Files Quiz

---

## Question 1
What does opening a file with mode `"w"` do?

- A) It appends to the file
- B) It overwrites the file (or creates it)
- C) It reads the file only
- D) It opens the file in binary mode

<details>
<summary>Show Answer</summary>

**B)** `"w"` truncates the file to empty first (overwrite).

</details>

---

## Question 2
Why should you usually prefer `with open(...) as f:` when writing?

- A) It makes writing faster
- B) It ensures flushing/closing even on exceptions
- C) It prevents the file from being created
- D) It automatically encrypts the file

<details>
<summary>Show Answer</summary>

**B)** It ensures data is flushed and file handles are released.

</details>

---

[Back to Writing Files README](README.md)

