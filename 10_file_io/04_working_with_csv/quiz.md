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

## Question 3
Which argument is **required** when creating a `csv.DictWriter`?

- A) `delimiter`
- B) `fieldnames`
- C) `header=True`
- D) `columns`

<details>
<summary>Show Answer</summary>

**B)** `DictWriter(f, fieldnames=[...])` needs the column names — it uses them
for `writeheader()` and to pull values from each dict row.

</details>

---

## Question 4
After reading rows with `csv.reader`, what type is every cell value?

- A) A string — even `"30"` stays a string
- B) The most specific type Python can infer
- C) Always a float
- D) Bytes

<details>
<summary>Show Answer</summary>

**A)** The `csv` module returns everything as strings. Convert with `int(row[1])`
or `float(...)` yourself when you need numbers.

</details>

---

## Question 5
Why not just read a CSV with `line.split(",")`?

- A) `split` is slower than the `csv` module
- B) It breaks when a field itself contains a comma or quoted text like `"Smith, Ada"`
- C) It only works on Windows
- D) `split(",")` strips quotes automatically

<details>
<summary>Show Answer</summary>

**B)** Quoted fields may contain commas, so naive splitting produces extra
columns. The `csv` module understands the quoting rules.

</details>

---

## Question 6
Which method writes a list of rows in one call?

- A) `writer.save_rows(rows)`
- B) `writer.writerows(rows)`
- C) `writer.put_rows(rows)`
- D) `csv.write_all(f, rows)`

<details>
<summary>Show Answer</summary>

**B)** `writer.writerows(rows)` writes every row; `writer.writerow(row)` writes a
single row. (`DictWriter` also needs `writeheader()` called first.)

</details>

---

[Back to CSV README](README.md)
