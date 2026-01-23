# 🧠 DRY Principle Quiz

Test your understanding of DRY (Don't Repeat Yourself).

---

## Question 1
What is the main goal of the DRY principle?

- A) Make code shorter at all costs
- B) Ensure each piece of knowledge exists in one place
- C) Avoid using functions
- D) Use more classes

<details>
<summary>Show Answer</summary>

**B)** DRY is about a single source of truth for rules/knowledge.

</details>

---

## Question 2
Which is an example of duplication (DRY violation)?

- A) Using a helper function in two places
- B) Copy/pasting the same validation logic in multiple functions
- C) Writing tests
- D) Renaming variables for clarity

<details>
<summary>Show Answer</summary>

**B)** Duplicated rules or logic means multiple places to update.

</details>

---

## Question 3
When can duplication be acceptable?

- A) Always; DRY is optional
- B) Never; duplication is always wrong
- C) When code is likely to diverge soon and abstraction would be misleading
- D) Only in Python

<details>
<summary>Show Answer</summary>

**C)** Sometimes two similar things are not truly the same concept.

</details>

---

## Question 4
What is a common risk of applying DRY too aggressively?

- A) Too many tests
- B) Over-abstraction and hard-to-understand generic code
- C) Functions becoming shorter
- D) Fewer bugs

<details>
<summary>Show Answer</summary>

**B)** DRY done poorly can create complex indirection.

</details>

---

## Question 5
Which change best supports DRY?

- A) Replace duplicated blocks with a well-named helper
- B) Duplicate code so it's easier to read
- C) Put everything in one huge function
- D) Add more global variables

<details>
<summary>Show Answer</summary>

**A)** Extracting shared logic creates a single source of truth.

</details>

---

[Back to DRY README](README.md) | [Next: KISS →](../02_kiss_principle/README.md)
