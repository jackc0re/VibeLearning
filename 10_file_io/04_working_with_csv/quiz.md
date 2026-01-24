# 🧠 CSV Quiz

---

## Question 1
Why should CSV files usually be opened with `newline=""`?

- A) It makes numbers parse correctly
- B) It avoids extra blank lines on some platforms (especially Windows)
- C) It automatically adds headers
- D) It switches to binary mode

<details>
<summary>Show Answer</summary>

**B)** The `csv` module expects `newline=""` to handle newlines consistently.

</details>

---

## Question 2
Which reader is best when the CSV has headers?

- A) `csv.reader`
- B) `csv.DictReader`
- C) `csv.BinaryReader`
- D) `csv.load`

<details>
<summary>Show Answer</summary>

**B)** `DictReader` maps each row to a dict using the header row.

</details>

---

[Back to CSV README](README.md)

