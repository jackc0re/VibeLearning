# 🧠 Binary Files Quiz

---

## Question 1
Which mode should you use to read bytes from a file?

- A) `"r"`
- B) `"rb"`
- C) `"w"`
- D) `"a"`

<details>
<summary>Show Answer</summary>

**B)** `"rb"` opens a file for reading in binary mode.

</details>

---

## Question 2
Why use chunked reads when hashing a very large file?

- A) It changes the hash result
- B) It reduces memory usage
- C) It makes the file smaller
- D) It converts binary to text

<details>
<summary>Show Answer</summary>

**B)** Chunking avoids loading the entire file into memory.

</details>

---

## Question 3
In binary mode, what type does `f.read()` return?

- A) `str`
- B) `bytes`
- C) `list` of ints
- D) `bytearray` only

<details>
<summary>Show Answer</summary>

**B)** Binary mode gives you `bytes` (e.g. `b"\x89PNG"`), not `str` — there is no
text decoding step.

</details>

---

## Question 4
What is the difference between `"w"` and `"wb"`?

- A) None — they are aliases
- B) `"wb"` is slower but safer
- C) `"w"` writes text (Python encodes it, translates newlines); `"wb"` writes raw bytes exactly as given
- D) `"wb"` appends instead of overwriting

<details>
<summary>Show Answer</summary>

**C)** In text mode you write `str` and Python handles encoding/newlines; in
binary mode you must write `bytes` and nothing is translated.

</details>

---

## Question 5
In the chunked-reading loop, how do you detect the end of the file?

- A) `f.eof` becomes `True`
- B) `f.read(chunk_size)` returns an empty bytes object `b""`
- C) The loop raises `EOFError`
- D) `len(f)` reaches zero

<details>
<summary>Show Answer</summary>

**B)** When `read` returns `b""` (an empty `bytes`), the file is exhausted — that
is what `if not chunk: break` checks.

</details>

---

## Question 6
Which of these is a typical job for binary mode?

- A) Editing a Python source file
- B) Appending a line to a log
- C) Copying a PNG image or computing a file's SHA-256 hash
- D) Reading a settings JSON

<details>
<summary>Show Answer</summary>

**C)** Images and hashes work on raw bytes. Python source, logs, and JSON are
text and are better handled in text mode with an encoding.

</details>

---

[Back to Binary Files README](README.md)
