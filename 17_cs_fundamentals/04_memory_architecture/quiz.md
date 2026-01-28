# 📝 Memory Architecture Quiz

Test your understanding of stack, heap, references, and memory management.

---

## Question 1

What is the primary difference between stack and heap memory?

- A) Stack is slower than heap
- B) Stack is automatically managed; heap requires manual management in some languages
- C) Heap can only store integers
- D) Stack is unlimited in size

---

## Question 2

In Python, what does the `id()` function return?

- A) The type of an object
- B) The memory address (or unique identifier) of an object
- C) The size of an object
- D) The reference count of an object

---

## Question 3

What happens when you do `x = 5; y = x` in Python?

- A) A copy of 5 is created for y
- B) Both x and y reference the same object
- C) x and y are completely independent
- D) An error occurs

---

## Question 4

What is a "stack overflow"?

- A) When the heap runs out of memory
- B) When too many function calls exceed the stack's capacity
- C) When a variable is too large
- D) When Python crashes

---

## Question 5

Which Python data type is immutable?

- A) List
- B) Dictionary
- C) String
- D) Set

---

## Question 6

What is the difference between `is` and `==` in Python?

- A) They are the same
- B) `is` compares identity (memory address), `==` compares value
- C) `is` compares value, `==` compares identity
- D) `is` only works for integers

---

## Question 7

What does `sys.getsizeof()` measure?

- A) The reference count
- B) The memory address
- C) The size of an object in bytes
- D) The type of an object

---

## Question 8

Why does `a += [4]` modify a list in place, but `a = a + [4]` creates a new list?

- A) They're the same operation
- B) `+=` calls `__iadd__` which modifies in place; `+` calls `__add__` which creates new
- C) It's a Python bug
- D) It depends on the Python version

---

## Question 9

What is the purpose of `__slots__` in a Python class?

- A) To make the class faster
- B) To prevent adding new attributes and save memory
- C) To make the class thread-safe
- D) To enable inheritance

---

## Question 10

In the context of the call stack, what is a "stack frame"?

- A) A data structure for storing frames of video
- B) A block of memory containing a function's local variables and return address
- C) A type of error message
- D) A GUI component

---

# Answers

<details>
<summary>Click to reveal answers</summary>

## Answer 1
**B) Stack is automatically managed; heap requires manual management in some languages**

The stack is automatically managed (pushed on function call, popped on return), while heap memory in languages like C/C++ requires manual allocation and deallocation. Python manages both automatically.

---

## Answer 2
**B) The memory address (or unique identifier) of an object**

In CPython, `id()` returns the memory address. In other Python implementations, it returns a unique identifier that stays constant for the object's lifetime.

---

## Answer 3
**B) Both x and y reference the same object**

Python uses reference semantics. Assignment never copies data; it just creates a new reference to the same object.

---

## Answer 4
**B) When too many function calls exceed the stack's capacity**

Stack overflow typically occurs with deep or infinite recursion. The stack has limited size, and each function call uses some of it.

---

## Answer 5
**C) String**

Strings in Python are immutable - you cannot change a string in place. Any operation that modifies a string creates a new string object.

---

## Answer 6
**B) `is` compares identity (memory address), `==` compares value**

- `is` checks if two variables reference the same object in memory
- `==` checks if two objects have equal values (calls `__eq__`)

---

## Answer 7
**C) The size of an object in bytes**

`sys.getsizeof()` returns the size of an object in bytes. Note that for containers, it only measures the container itself, not the objects it references.

---

## Answer 8
**B) `+=` calls `__iadd__` which modifies in place; `+` calls `__add__` which creates new**

- `a += b` is equivalent to `a = a.__iadd__(b)` (in-place addition)
- `a = a + b` is equivalent to `a = a.__add__(b)` (creates new object)

---

## Answer 9
**B) To prevent adding new attributes and save memory**

`__slots__` declares fixed attributes for a class, preventing the creation of `__dict__` for each instance. This saves memory and allows faster attribute access.

---

## Answer 10
**B) A block of memory containing a function's local variables and return address**

Each time a function is called, a new stack frame is created containing local variables, parameters, and the return address. When the function returns, the frame is popped off the stack.

</details>

---

## Scoring

- **9-10 correct:** 🏆 Memory Master!
- **7-8 correct:** 👍 Good understanding
- **5-6 correct:** 📚 Review the material
- **Below 5:** 🔄 Start with the README and examples

---

## Next Steps

Ready for the final topic? Move on to [How Python Works](../05_how_python_works/README.md) to learn about bytecode, the GIL, and Python internals!
