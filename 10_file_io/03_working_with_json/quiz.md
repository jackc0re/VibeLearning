# 🧠 JSON Quiz

---

## Question 1
Which function writes JSON to a file object?

- A) `json.dumps`
- B) `json.dump`
- C) `json.parse`
- D) `json.load`

<details>
<summary>Show Answer</summary>

**B)** `json.dump(obj, file)` writes JSON to an open file handle.

</details>

---

## Question 2
What is JSON best described as?

- A) A binary format for images
- B) A text format for structured data
- C) A Python-only object format
- D) A database engine

<details>
<summary>Show Answer</summary>

**B)** JSON is human-readable text that represents nested structures.

</details>

---

## Question 3
What does `json.loads(text)` do?

- A) Writes a string to a file
- B) Parses a JSON **string** into Python objects
- C) Converts Python objects into a JSON string
- D) Sorts the JSON keys

<details>
<summary>Show Answer</summary>

**B)** `loads` = "load **s**tring": it turns a JSON string into Python objects
(`json.load` does the same but reads from a file object).

</details>

---

## Question 4
After `json.loads('["a", "b", "c"]')`, what Python type do you get?

- A) `tuple`
- B) `set`
- C) `list`
- D) `dict`

<details>
<summary>Show Answer</summary>

**C)** A JSON array becomes a Python `list`. (Its items here become `str`.)

</details>

---

## Question 5
What happens if you call `json.dumps({"tags": {"python", "math"}})` (a `set` inside)?

- A) The set becomes a JSON array
- B) The set becomes a JSON object
- C) It raises `TypeError` because sets are not JSON-serializable
- D) The set is silently dropped

<details>
<summary>Show Answer</summary>

**C)** JSON has no "set" concept; `json.dumps` raises
`TypeError: Object of type set is not JSON serializable`. Convert to a `list`
first if you need one.

</details>

---

## Question 6
Which pair of arguments makes `json.dump` write a file that is easy for humans to read?

- A) `sort_keys=False, compact=True`
- B) `indent=2`
- C) `pretty="yes"`
- D) `newline=2`

<details>
<summary>Show Answer</summary>

**B)** `indent=2` (any positive indent works) pretty-prints the JSON with
indented nested structures.

</details>

---

[Back to JSON README](README.md)
