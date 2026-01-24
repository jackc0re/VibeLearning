# 📖 Programming Glossary

A comprehensive dictionary of programming terms you'll encounter throughout this course.

---

## Table of Contents

- [A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [Y](#y) | [Z](#z)

---

## A

### Abstraction
Hiding complex implementation details and showing only essential features to the user. In OOP, this means using classes to group related data and functions while hiding internal logic.

**Python Context:** Abstract base classes (ABCs) define methods that subclasses must implement.

**Related Terms:** Encapsulation, Interface, Class

---

### Algorithm
A step-by-step procedure for solving a problem or completing a task. Algorithms are the core of computer programming and range from simple to highly complex.

**Python Context:** Built-in functions like `sorted()` use algorithms. You'll implement algorithms for searching, sorting, and more.

**Related Terms:** Big O, Time Complexity, Data Structure

---

### Argument
The actual value passed to a function when it's called. Arguments are assigned to the function's parameters.

**Python Context:** `greet("Alice")` — `"Alice"` is the argument passed to the `greet()` function.

**Related Terms:** Parameter, Function Call, Return Value

---

### Array
A collection of elements stored at contiguous memory locations. In Python, lists are dynamic arrays that can grow or shrink.

**Python Context:** Python lists (`[1, 2, 3]`) are the array equivalent, though they have more features.

**Related Terms:** List, Index, Element

---

### Asynchronous
A programming model where operations can run independently without blocking each other. Unlike synchronous code, async code doesn't wait for one operation to complete before starting the next.

**Python Context:** `async def` and `await` keywords for asynchronous programming with `asyncio` library.

**Related Terms:** Asyncio, Await, Concurrency

---

## B

### Big O Notation
A mathematical notation that describes the limiting behavior of a function, commonly used to analyze algorithm efficiency in terms of time and space complexity.

**Python Context:** `O(n)` means linear time, `O(log n)` means logarithmic time, `O(1)` means constant time.

**Related Terms:** Algorithm, Time Complexity, Space Complexity, Optimization

---

### Binary
A number system with base 2 (only 0s and 1s). Computers store all data in binary format.

**Python Context:** Binary literals start with `0b` (e.g., `0b1010` equals 10 in decimal).

**Related Terms:** Bit, Byte, Hexadecimal

---

### Boolean
A data type that can have only two values: `True` or `False`. Named after George Boole.

**Python Context:** Built-in `bool` type. Any value can be evaluated as boolean (falsy: `0`, `""`, `[]`, `None`; truthy: everything else).

**Related Terms:** Logical Operator, Condition, Truthy/Falsy

---

### Bug
An error, flaw, or fault in a computer program that causes it to produce incorrect or unexpected results.

**Python Context:** Python raises exceptions (e.g., `NameError`, `TypeError`) to help identify and fix bugs.

**Related Terms:** Debugging, Exception, Error

---

### Byte
A unit of digital information consisting of 8 bits. Can represent values from 0 to 255 or a single ASCII character.

**Python Context:** `bytes` type for binary data. String methods like `.encode()` convert strings to bytes.

**Related Terms:** Binary, Bit, Unicode, UTF-8

---

## C

### Call Stack
A data structure that keeps track of function calls. When a function is called, it's added to the stack; when it returns, it's removed.

**Python Context:** The call stack is visible in traceback errors, showing the sequence of function calls.

**Related Terms:** Recursion, Traceback, Function, Stack

---

### Callback
A function passed as an argument to another function, to be executed later.

**Python Context:** Common in event-driven programming and libraries like `asyncio` or GUI frameworks.

**Related Terms:** Higher-Order Function, Lambda, Event Loop

---

### Class
A blueprint for creating objects. Classes define attributes (data) and methods (functions) that objects will have.

**Python Context:** Defined using the `class` keyword: `class Dog: def __init__(self, name): self.name = name`.

**Related Terms:** Object, Instance, Method, OOP

---

### Closure
A function that remembers the environment in which it was created, even after the outer function has finished executing.

**Python Context:** Inner functions that reference variables from outer functions create closures.

**Related Terms:** Nested Function, Scope, Decorator

---

### Code Smell
A surface indication that usually corresponds to a deeper problem in the code. Not a bug, but a sign that code might be difficult to maintain.

**Python Context:** Duplicated code, overly long functions, unclear variable names are common code smells.

**Related Terms:** Refactoring, Clean Code, Technical Debt

---

### Concurrency
Executing multiple tasks at overlapping time periods, not necessarily simultaneously. Concurrency improves responsiveness and resource utilization.

**Python Context:** Threads and `asyncio` provide concurrency. Python's GIL limits CPU-bound parallelism.

**Related Terms:** Parallelism, Thread, Async, GIL

---

### Constructor
A special method automatically called when creating a new instance of a class. Used to initialize the object's state.

**Python Context:** The `__init__` method is the constructor in Python classes.

**Related Terms:** Class, Instance, Initialization, __init__

---

## D

### Data Structure
A way of organizing and storing data so that it can be accessed and modified efficiently.

**Python Context:** Built-in: lists, tuples, sets, dictionaries. Custom: stacks, queues, linked lists, trees, graphs.

**Related Terms:** Algorithm, Array, Linked List, Tree, Graph

---

### Decorator
A design pattern that allows adding functionality to an existing function or method without modifying its structure.

**Python Context:** Functions prefixed with `@decorator_name` syntax. Common decorators: `@property`, `@staticmethod`, `@classmethod`.

**Related Terms:** Higher-Order Function, Wrapper, Closure

---

### Dictionary (Dict)
A data structure that stores key-value pairs. Keys must be unique and immutable.

**Python Context:** Created with `{}` or `dict()`: `my_dict = {"name": "Alice", "age": 25}`. Fast lookup O(1).

**Related Terms:** Hash Table, Key-Value, Hashable, Map

---

### Duck Typing
A programming style where an object's suitability is determined by the presence of certain methods and properties, rather than its type.

**Python Context:** Python uses duck typing extensively: "If it walks like a duck and quacks like a duck, it's a duck."

**Related Terms:** Dynamic Typing, Polymorphism, Interface

---

### Dynamic Programming
An optimization technique that breaks complex problems into simpler subproblems and stores the results to avoid redundant calculations.

**Python Context:** Memoization (caching function results) and tabulation (building a table of results).

**Related Terms:** Recursion, Memoization, Optimization, Algorithm

---

## E

### Exception
An event that occurs during program execution that disrupts the normal flow. Exceptions are used to handle errors gracefully.

**Python Context:** `try...except` blocks handle exceptions. Custom exceptions can be created by inheriting from `Exception`.

**Related Terms:** Error Handling, Try-Except-Finally, Runtime Error

---

### Expression
A combination of values, variables, operators, and function calls that produces a value.

**Python Context:** `3 + 5` is an expression that evaluates to `8`. `x * 2` is an expression if `x` is defined.

**Related Terms:** Statement, Variable, Operator

---

## F

### Function
A reusable block of code that performs a specific task. Functions take inputs (parameters) and return outputs.

**Python Context:** Defined with `def` keyword: `def greet(name): return f"Hello, {name}!"`.

**Related Terms:** Parameter, Argument, Return, Call

---

## G

### Generator
A special type of iterator that generates values on demand instead of storing them all in memory. More memory-efficient for large datasets.

**Python Context:** Functions using `yield` keyword are generators. Generator expressions: `(x for x in range(10))`.

**Related Terms:** Iterator, Yield, Lazy Evaluation

---

### Global Interpreter Lock (GIL)
A mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes simultaneously in CPython.

**Python Context:** The GIL means Python threads can't run CPU-bound code in parallel. Use `multiprocessing` for CPU-bound tasks.

**Related Terms:** Thread, Concurrency, Parallelism, CPython

---

## H

### Hash
A fixed-size string generated from input data, used to uniquely identify it. Hash functions are deterministic (same input always produces same hash).

**Python Context:** The `hash()` function returns hash values for hashable objects. Dictionaries use hashing for fast lookups.

**Related Terms:** Hash Table, Dictionary, Key, Hashable

---

### Hash Table
A data structure that implements an associative array, mapping keys to values using a hash function. Provides average O(1) lookup time.

**Python Context:** Python dictionaries are implemented as hash tables.

**Related Terms:** Dictionary, Hash, Key-Value, Array

---

### Higher-Order Function
A function that takes other functions as arguments or returns a function as its result.

**Python Context:** `map()`, `filter()`, `reduce()` are higher-order functions. Custom functions can also be higher-order.

**Related Terms:** Function, Callback, Lambda, Closure

---

## I

### Immutable
An object that cannot be changed after creation. Any modification creates a new object.

**Python Context:** Tuples, strings, and frozensets are immutable. Integers and floats are also immutable.

**Related Terms:** Mutable, Tuple, String, Side Effect

---

### Inheritance
A mechanism where a new class derives properties and behavior from an existing class. Promotes code reuse and establishes relationships.

**Python Context:** `class Dog(Animal):` creates `Dog` class inheriting from `Animal`.

**Related Terms:** Class, Subclass, Superclass, OOP

---

### Instance
A specific occurrence of a class. An instance has the attributes and methods defined by its class.

**Python Context:** Creating an instance: `my_dog = Dog("Buddy")` creates a `Dog` instance named `my_dog`.

**Related Terms:** Class, Object, Instantiation, Method

---

### Iterator
An object that implements the iterator protocol, allowing iteration over a sequence of values. Uses `__iter__()` and `__next__()` methods.

**Python Context:** Lists, strings, and dictionaries are iterable. The `iter()` function returns an iterator.

**Related Terms:** Iterable, Generator, Loop, __next__

---

## K

### Key-Value Pair
A data representation where a unique key maps to a specific value. The foundation of dictionaries and hash tables.

**Python Context:** In `{"name": "Alice"}`, `"name"` is the key and `"Alice"` is the value.

**Related Terms:** Dictionary, Hash Table, Map, Entry

---

## L

### Lambda
An anonymous, inline function defined using the `lambda` keyword. Useful for short, simple functions.

**Python Context:** `square = lambda x: x ** 2` creates a lambda function. Commonly used with `map()` and `filter()`.

**Related Terms:** Anonymous Function, Higher-Order Function, Expression

---

### Linked List
A linear data structure where elements are stored in nodes. Each node contains data and a reference (pointer) to the next node.

**Python Context:** Not a built-in type, but can be implemented using classes with `next` references.

**Related Terms:** Node, Pointer, Data Structure, Tree

---

### List Comprehension
A concise way to create lists in Python using a single line of code with a for loop and optional condition.

**Python Context:** `[x ** 2 for x in range(10) if x % 2 == 0]` creates a list of even squares.

**Related Terms:** List, Generator Expression, For Loop, Filter

---

## M

### Memoization
An optimization technique that stores the results of expensive function calls and returns the cached result when the same inputs occur again.

**Python Context:** Can be implemented with dictionaries or using `@functools.lru_cache` decorator.

**Related Terms:** Caching, Dynamic Programming, Decorator, Optimization

---

### Method
A function that belongs to a class and operates on instances of that class. Methods define the behavior of objects.

**Python Context:** Methods are defined inside classes and take `self` as the first parameter: `class Dog: def bark(self): ...`.

**Related Terms:** Class, Instance, Function, Object

---

### Module
A file containing Python definitions and statements. Modules organize code and provide namespaces.

**Python Context:** Import modules with `import` or `from module import name`. Example: `import math`.

**Related Terms:** Package, Import, Namespace, Library

---

### Mutable
An object that can be changed after creation. Modifications affect the same object in memory.

**Python Context:** Lists, dictionaries, and sets are mutable. Operations modify the object in place.

**Related Terms:** Immutable, List, Dictionary, Side Effect

---

## N

### Namespace
A mapping from names to objects. Namespaces help avoid naming conflicts by organizing names in different scopes.

**Python Context:** Each module has its own namespace. Functions have local namespaces, scripts have global namespace.

**Related Terms:** Scope, Variable, Module, Class

---

### Node
A fundamental part of data structures like linked lists, trees, and graphs. A node contains data and references to other nodes.

**Python Context:** In a tree node: `class Node: def __init__(self, data): self.data = data; self.children = []`.

**Related Terms:** Linked List, Tree, Graph, Data Structure

---

## O

### Object
An instance of a class. Objects have state (attributes) and behavior (methods).

**Python Context:** Everything in Python is an object: numbers, strings, functions, classes themselves.

**Related Terms:** Class, Instance, OOP, Attribute

---

### OOP (Object-Oriented Programming)
A programming paradigm based on the concept of objects, which can contain data and code. Main principles: encapsulation, inheritance, polymorphism, abstraction.

**Python Context:** Python is a multi-paradigm language with strong OOP support via classes and objects.

**Related Terms:** Class, Object, Inheritance, Polymorphism, Encapsulation, Abstraction

---

### Operator Precedence
The order in which operators are evaluated in an expression. Higher precedence operators are evaluated first.

**Python Context:** Multiplication (`*`) has higher precedence than addition (`+`): `2 + 3 * 4` equals `14`.

**Related Terms:** Operator, Expression, Parentheses

---

## P

### Parameter
A named entity in a function definition that specifies the input the function expects.

**Python Context:** In `def greet(name):`, `name` is a parameter. When called with `greet("Alice")`, `"Alice"` is the argument.

**Related Terms:** Argument, Function, Variable

---

### Parallelism
Executing multiple tasks simultaneously, truly running at the same time. Unlike concurrency, parallelism requires multiple processors/cores.

**Python Context:** The `multiprocessing` module enables parallelism by using separate processes (bypassing GIL).

**Related Terms:** Concurrency, Multiprocessing, GIL, CPU Core

---

### Polymorphism
The ability of different classes to be treated as instances of the same superclass. Allows code to work with objects of different types.

**Python Context:** Method overriding (subclass redefines parent method) and duck typing are forms of polymorphism.

**Related Terms:** Inheritance, OOP, Method Overriding, Duck Typing

---

### Prototype
An early sample or model of a product built to test a concept or process. In programming, a prototype helps validate ideas before full implementation.

**Python Context:** Python's interactive mode (`python -i`) is great for prototyping code quickly.

**Related Terms:** MVP (Minimum Viable Product), Iteration, Development

---

## R

### Race Condition
A situation where the output depends on the timing of uncontrollable events. Occurs in concurrent programming when multiple threads access shared data.

**Python Context:** Use locks (`threading.Lock`) to prevent race conditions when modifying shared data.

**Related Terms:** Thread, Concurrency, Lock, Synchronization

---

### Recursion
A method where the solution to a problem depends on solutions to smaller instances of the same problem. A recursive function calls itself.

**Python Context:** `def factorial(n): return 1 if n <= 1 else n * factorial(n-1)`.

**Related Terms:** Base Case, Call Stack, Recursive Function

---

### Refactoring
The process of restructuring existing code without changing its external behavior. Improves code quality, readability, and maintainability.

**Python Context:** Common refactoring: extracting functions, renaming variables, eliminating code duplication.

**Related Terms:** Code Quality, Technical Debt, Clean Code

---

## S

### Scope
The region of code where a variable is visible and accessible. Python has local, enclosing, global, and built-in scopes (LEGB rule).

**Python Context:** Variables defined inside functions have local scope. Global variables are accessible throughout the module.

**Related Terms:** Namespace, Variable, Local, Global

---

### Side Effect
Any observable effect of a function beyond returning a value. Examples: modifying a global variable, printing to console, writing to a file.

**Python Context:** Functions with side effects are harder to test and reason about. Pure functions have no side effects.

**Related Terms:** Pure Function, Mutable, Global Variable

---

### SOLID Principles
Five design principles that make software designs more understandable, flexible, and maintainable.

**Python Context:**
- **S**ingle Responsibility - Class should have one reason to change
- **O**pen/Closed - Open for extension, closed for modification
- **L**iskov Substitution - Subtypes must be substitutable
- **I**nterface Segregation - Small, focused interfaces
- **D**ependency Inversion - Depend on abstractions, not concretions

**Related Terms:** Design Pattern, Clean Code, OOP, Software Design

---

### Stack
A linear data structure following Last-In-First-Out (LIFO) principle. Elements are added and removed from the same end.

**Python Context:** Python lists can be used as stacks: `stack.append(x)` to push, `stack.pop()` to pop.

**Related Terms:** Queue, Data Structure, LIFO, Call Stack

---

### Statement
A unit of code that performs an action. Unlike expressions, statements don't evaluate to a value.

**Python Context:** `x = 5` (assignment), `if x > 0:` (conditional), `for i in range(5):` (loop) are statements.

**Related Terms:** Expression, Control Flow, Assignment

---

### String
A sequence of characters. In Python, strings are immutable sequences of Unicode characters.

**Python Context:** `"Hello"` or `'Hello'`. Strings support slicing, concatenation, and many methods (`.upper()`, `.split()`, etc.).

**Related Terms:** Unicode, Character, Sequence, Immutable

---

## T

### Technical Debt
The implied cost of additional rework caused by choosing an easy/fast solution now instead of a better approach that would take longer.

**Python Context:** Accumulates when using quick fixes, skipping tests, or not refactoring. Must be "paid back" with cleanup work.

**Related Terms:** Refactoring, Code Smell, Maintenance, Quality

---

### Thread
The smallest unit of execution within a process. Threads in the same process share memory and resources.

**Python Context:** `threading.Thread` creates threads. Due to GIL, best for I/O-bound tasks, not CPU-bound.

**Related Terms:** Process, Concurrency, GIL, Multiprocessing

---

### Traceback
A report of the function calls that led to an error. Helps identify where and why an error occurred.

**Python Context:** When Python encounters an uncaught exception, it prints the traceback showing the call stack.

**Related Terms:** Exception, Call Stack, Debugging, Error

---

### Tree
A hierarchical data structure with nodes connected by edges. Each tree has a root node and child nodes.

**Python Context:** Common types: binary trees, binary search trees, decision trees. Implemented using classes with left/right children.

**Related Terms:** Node, Graph, Binary Tree, Data Structure

---

### Tuple
An ordered, immutable sequence. Similar to lists but cannot be modified after creation.

**Python Context:** Created with parentheses: `(1, 2, 3)`. Use for data that shouldn't change, like coordinates or database records.

**Related Terms:** List, Sequence, Immutable, Data Structure

---

### Type Conversion
Changing a value from one data type to another. Can be implicit (automatic) or explicit (manual).

**Python Context:** `int("42")`, `str(3.14)`, `bool(1)` are explicit conversions. Python also performs implicit conversions in expressions.

**Related Terms:** Data Type, Casting, Integer, Float, String

---

## U

### Unicode
A universal character encoding standard that assigns a unique number to each character across all languages and writing systems.

**Python Context:** Python 3 uses Unicode for all strings by default. Characters can include emojis and international text.

**Related Terms:** String, Encoding, UTF-8, ASCII

---

## V

### Variable
A named storage location that holds a value. Variables allow us to reference and manipulate data using meaningful names.

**Python Context:** Variables are dynamically typed: `x = 5` creates an integer, `x = "hello"` reassigns it to a string.

**Related Terms:** Assignment, Data Type, Scope, Name

---

## W

### Wrapper
A function or class that provides a simplified interface to another, often more complex, component.

**Python Context:** Decorators wrap functions to add functionality. Wrapper classes adapt interfaces between incompatible types.

**Related Terms:** Decorator, Adapter, Interface, Abstraction

---

## Y

### Yield
A keyword used in generator functions to return a value without terminating the function. Creates a generator that can be iterated over.

**Python Context:** `def count_up_to(n): for i in range(n): yield i` creates a generator.

**Related Terms:** Generator, Iterator, Lazy Evaluation

---

## Z

### Zero-Based Indexing
A convention where sequences (lists, strings, arrays) start counting from index 0 instead of 1.

**Python Context:** `"Hello"[0]` is `"H"`, not `"e"`. Common in many programming languages.

**Related Terms:** Index, List, String, Sequence

---

## Quick Reference

### Data Types
- **Immutable:** int, float, str, tuple, bool, frozenset, bytes
- **Mutable:** list, dict, set, bytearray

### Complexity Notation
- **O(1):** Constant — always takes same time
- **O(log n):** Logarithmic — halves input each time
- **O(n):** Linear — proportional to input size
- **O(n log n):** Linearithmic — most efficient sorts
- **O(n²):** Quadratic — nested loops
- **O(2ⁿ):** Exponential — very slow, avoid

### Key Concepts
- **Encapsulation:** Bundling data with methods
- **Inheritance:** Deriving from parent classes
- **Polymorphism:** Same interface, different behavior
- **Abstraction:** Hiding implementation details

---

**Back to [Resources](README.md)**
