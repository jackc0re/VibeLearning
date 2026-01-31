# 🧠 Defensive Programming Quiz

Check your understanding of defensive techniques.

---

## Question 1
What is the main goal of defensive programming?

- A) Make code shorter
- B) Prevent errors before they happen
- C) Avoid tests
- D) Increase execution speed

<details>
<summary>Show Answer</summary>

**B)** Defensive programming prevents failures with validation and guards.

</details>

---

## Question 2
What is a guard clause?

- A) A long if/else chain
- B) An early return or raise for invalid states
- C) A loop that checks each item
- D) A global variable

<details>
<summary>Show Answer</summary>

**B)** Guard clauses fail fast before the main logic runs.

</details>

---

## Question 3
When should you use assertions?

- A) For user input validation
- B) For internal assumptions in code
- C) To replace error handling
- D) Only in production

<details>
<summary>Show Answer</summary>

**B)** Assertions document and check developer assumptions.

</details>

---

## Question 4
What happens if an assertion fails?

- A) The program ignores it
- B) An AssertionError is raised
- C) The program retries automatically
- D) A warning is printed but continues

<details>
<summary>Show Answer</summary>

**B)** Python raises `AssertionError`.

</details>

---

## Question 5
Which is a good defensive check for a percentage value?

- A) `value > 1000`
- B) `0 <= value <= 100`
- C) `value == 50`
- D) `value % 2 == 0`

<details>
<summary>Show Answer</summary>

**B)** Percentages should stay within 0 to 100.

</details>

---

[Back to Defensive Programming README](README.md) | [Next: Logging →](../05_logging/README.md)
