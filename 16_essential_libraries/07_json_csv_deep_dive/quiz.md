# 📊 JSON & CSV Deep Dive - Quiz

Test your knowledge of advanced JSON and CSV!

---

## Question 1
**How do you handle non-serializable types (like datetime) in JSON?**

A) Convert to string manually before serializing
B) Use a custom JSONEncoder subclass
C) Use json.dumps with special=True
D) Both A and B

<details>
<summary>Click for answer</summary>

**D) Both A and B**

You can either convert manually or subclass `JSONEncoder` and override `default()`.
</details>

---

## Question 2
**What is JSON Lines format?**

A) A JSON array with each element on its own line
B) A format where each line is a separate JSON object
C) JSON with line numbers
D) Minified JSON

<details>
<summary>Click for answer</summary>

**B) A format where each line is a separate JSON object**

JSONL (or JSON Lines) has one JSON object per line, useful for streaming.
</details>

---

## Question 3
**What is the purpose of `newline=''` when opening CSV files?**

A) To handle empty lines
B) To prevent extra blank lines on Windows
C) To enable universal newlines
D) It's required by Python 3

<details>
<summary>Click for answer</summary>

**B) To prevent extra blank lines on Windows**

CSV module handles newlines itself; `newline=''` prevents double newlines on Windows.
</details>

---

## Question 4
**What does `csv.DictReader` return for each row?**

A) A list of values
B) A dictionary with column headers as keys
C) A named tuple
D) A custom Row object

<details>
<summary>Click for answer</summary>

**B) A dictionary with column headers as keys**

Each row is a dict where keys are from the header row and values are the cell data.
</details>

---

## Question 5
**How do you stream large JSON Lines files without loading all into memory?**

A) Use json.load with stream=True
B) Read line by line and parse each with json.loads
C) Use json.loads with chunks=True
D) You can't, JSON must be loaded entirely

<details>
<summary>Click for answer</summary>

**B) Read line by line and parse each with json.loads**

JSON Lines is designed for streaming - read one line, parse one object.
</details>

---

## Question 6
**What encoding should you use for CSV files that work well with Excel?**

A) utf-8
B) utf-8-sig
C) ascii
D) latin-1

<details>
<summary>Click for answer</summary>

**B) utf-8-sig**

`utf-8-sig` includes a BOM that Excel recognizes for proper UTF-8 handling.
</details>

---

## Question 7
**In JSON's `object_hook`, what is passed to the function?**

A) The entire JSON string
B) Each dict as it's decoded
C) Each value in the JSON
D) The final parsed object

<details>
<summary>Click for answer</summary>

**B) Each dict as it's decoded**

`object_hook` is called with every JSON object (dict) during parsing, allowing custom conversion.
</details>

---

## Question 8
**What does `csv.register_dialect()` do?**

A) Registers a CSV file for reading
B) Creates a named CSV format configuration
C) Validates CSV format
D) Converts dialects

<details>
<summary>Click for answer</summary>

**B) Creates a named CSV format configuration**

Define custom formats (delimiter, quoting, etc.) once and reuse by name.
</details>

---

## Question 9
**Why might you choose JSON Lines over regular JSON for large datasets?**

A) It's smaller
B) It can be streamed/processed line by line
C) It's faster to parse
D) It supports more data types

<details>
<summary>Click for answer</summary>

**B) It can be streamed/processed line by line**

JSON Lines allows processing huge files without loading everything into memory.
</details>

---

## Question 10
**What happens when `json.dumps()` encounters a non-serializable type?**

A) It converts it to null
B) It raises TypeError
C) It calls str() on it
D) It skips the value

<details>
<summary>Click for answer</summary>

**B) It raises TypeError**

By default, non-serializable types cause a TypeError. You must handle them with a custom encoder.
</details>

---

**How did you do?** Check `examples.py` for more practice!
