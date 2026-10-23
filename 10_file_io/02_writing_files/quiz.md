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

## Question 3
Which mode writes new content **at the end** of an existing file without erasing it?

- A) `"w"`
- B) `"x"`
- C) `"a"`
- D) `"r+"`

<details>
<summary>Show Answer</summary>

**C)** `"a"` (append) keeps existing content and writes at the end; it also
creates the file if it does not exist yet.

</details>

---

## Question 4
What happens when you open an **existing** file with mode `"x"`?

- A) The file is overwritten
- B) It raises `FileExistsError`
- C) The file is opened for reading
- D) It appends to the file

<details>
<summary>Show Answer</summary>

**B)** `"x"` means "exclusive creation" — it fails with `FileExistsError` if the
path already exists. Use it when overwriting would be a bug.

</details>

---

## Question 5
If you write with `f.write(...)` but never close the file and your program crashes, what can happen?

- A) Nothing — writes are always instant
- B) Some data may still be sitting in the buffer and never reach the disk
- C) Python automatically saves everything on crash
- D) The file is deleted

<details>
<summary>Show Answer</summary>

**B)** Writes go to an in-memory buffer first. If the file is never closed/flushed,
buffered data can be lost — another reason `with` is the standard pattern.

</details>

---

## Question 6
Which snippet correctly writes two lines to a text file?

- A) `open("f.txt").write("a\nb\n")`
- B) `f.write("a\nb\n")` with no `open()`
- C) `with open("f.txt", "w", encoding="utf-8") as f: f.write("a\nb\n")`
- D) `with open("f.txt", "r") as f: f.write("a\nb\n")`

<details>
<summary>Show Answer</summary>

**C)** Open in write mode inside a `with` block. Option A never closes the file;
B has no file object; D opens read-only, so writing raises `io.UnsupportedOperation`.

</details>

---

[Back to Writing Files README](README.md)
