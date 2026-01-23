# 🧠 Separation of Concerns Quiz

Test your understanding of separation of concerns.

---

## Question 1
What is separation of concerns (SoC)?

- A) Putting all code in one file
- B) Splitting a program into parts that each handle a distinct responsibility
- C) Avoiding functions
- D) Using only classes

<details>
<summary>Show Answer</summary>

**B)** SoC organizes code by responsibility.

</details>

---

## Question 2
Why does SoC often improve testability?

- A) It removes the need for inputs
- B) It lets you test business logic without I/O
- C) It makes code longer
- D) It forces recursion

<details>
<summary>Show Answer</summary>

**B)** Pure logic is easier to test than code that reads/writes externally.

</details>

---

## Question 3
Which concern is best kept at the edges of the program?

- A) Core calculations
- B) Business rules
- C) Reading user input / writing to files
- D) Data transformations

<details>
<summary>Show Answer</summary>

**C)** I/O is typically an edge concern.

</details>

---

## Question 4
What’s a common symptom of mixed concerns?

- A) Small functions
- B) Clear module boundaries
- C) A function that parses, computes, and prints all at once
- D) Low coupling

<details>
<summary>Show Answer</summary>

**C)** Mixed responsibilities make change risky.

</details>

---

## Question 5
Which refactor best supports SoC?

- A) Combine parsing and printing into one function
- B) Extract business logic into pure functions
- C) Add more global variables
- D) Remove unit tests

<details>
<summary>Show Answer</summary>

**B)** Isolating logic from I/O makes code easier to change and test.

</details>

---

[Back to SoC README](README.md) | [Next: Coupling and Cohesion →](../05_coupling_and_cohesion/README.md)
