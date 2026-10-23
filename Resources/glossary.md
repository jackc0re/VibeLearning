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

### API (Application Programming Interface)
A contract that lets one program talk to another: a defined set of requests the program accepts and the responses it sends back. Web APIs let your Python code ask a server for data or actions over HTTP.

**Python Context:** The standard library's `urllib.request` sends requests; most APIs reply with JSON, which you parse into dictionaries and lists.

**Related Terms:** HTTP Method, HTTP Status Code, JSON, REST

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

### Assertion
A statement that claims something must be true at a certain point in the code; if it is not, the program stops with an error immediately. Assertions turn silent wrong behaviour into a loud, early failure.

**Python Context:** `assert total >= 0, "total went negative"` raises `AssertionError` when the condition is false. Assertions are also the building blocks of tests.

**Related Terms:** Unit Test, Test-Driven Development (TDD), Exception

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

### Bit Shift
Moving an integer's bits left or right. Shifting left (`x << n`) multiplies by 2 to the power n; shifting right (`x >> n`) divides by it, rounding down. Shifts are the natural way to build and read bit patterns.

**Python Context:** `1 << 3` is `8` — the value with only bit 3 set. `flags >> 3 & 1` extracts bit 3 of `flags`.

**Related Terms:** Bitwise Mask, Binary, Bit

---

### Bitwise Mask
A chosen bit pattern used with `&`, `|`, or `^` to inspect or change specific bits while leaving the rest untouched. Masks turn one integer into a row of on/off switches called flags.

**Python Context:** `value & 0b0001` tests the lowest bit (a non-zero result means it is set), `value | 0b0100` turns bit 2 on, and `value & ~0b0100` turns it off.

**Related Terms:** Bit Shift, Binary, Boolean

---

### Boolean
A data type that can have only two values: `True` or `False`. Named after George Boole.

**Python Context:** Built-in `bool` type. Any value can be evaluated as boolean (falsy: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`; truthy: everything else).

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

### Cohesion
A measure of how strongly the parts of a module belong together. High cohesion means a module does one job well; low cohesion means it is a grab-bag of unrelated tasks.

**Python Context:** `date_utils.py` containing only date helpers has high cohesion. Tossing unrelated string functions into it lowers cohesion and makes it harder to find things.

**Related Terms:** Coupling, Separation of Concerns, Refactoring

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

### Context Manager
An object that sets something up before a block of code runs and reliably cleans up afterwards, no matter how the block exits — even if an exception is raised. The pattern prevents leaked resources like open files.

**Python Context:** Classes with `__enter__`/`__exit__` methods (or functions using `contextlib.contextmanager`) work with the `with` statement: `with open("data.txt") as f: ...` always closes the file.

**Related Terms:** Exception, Immutable, Resource Management

---

### Counter
A dictionary subclass from the `collections` module that counts how many times each item appears. It returns `0` for missing keys instead of raising an error.

**Python Context:** `Counter("banana")["a"]` returns `3`, and `Counter(items).most_common(3)` gives the three most frequent items in one call.

**Related Terms:** Dictionary (Dict), Defaultdict, Hash Table

---

### Coupling
A measure of how much one module depends on another. Tight coupling means changing one module forces changes in many others; loose coupling means modules can change independently.

**Python Context:** A function that reaches into another module's private internals is tightly coupled. Passing plain arguments in and getting return values out keeps coupling loose.

**Related Terms:** Cohesion, Encapsulation, Separation of Concerns

---

## D

### Data Structure
A way of organizing and storing data so that it can be accessed and modified efficiently.

**Python Context:** Built-in: lists, tuples, sets, dictionaries. Custom: stacks, queues, linked lists, trees, graphs.

**Related Terms:** Algorithm, Array, Linked List, Tree, Graph

---

### Data Validation
Checking that input data has the expected type, shape, and range before you process it. Validation stops "garbage in" at the door, because garbage that gets in always comes back out as garbage results.

**Python Context:** Simple checks like `isinstance(age, int)` and `0 <= age <= 130`, or raising `ValueError` for bad values, catch most bad data early.

**Related Terms:** Defensive Programming, Exception, Parameterized Query

---

### Decorator
A design pattern that allows adding functionality to an existing function or method without modifying its structure.

**Python Context:** Functions prefixed with `@decorator_name` syntax. Common decorators: `@property`, `@staticmethod`, `@classmethod`.

**Related Terms:** Higher-Order Function, Wrapper, Closure

---

### Defaultdict
A dictionary subclass from the `collections` module that automatically creates a missing key with a default value instead of raising `KeyError`.

**Python Context:** After `d = defaultdict(list)`, `d["fruits"].append("apple")` works even on the very first append — no "is the key there yet?" check needed.

**Related Terms:** Dictionary (Dict), Counter, Key-Value Pair

---

### Dictionary (Dict)
A data structure that stores key-value pairs. Keys must be unique and immutable.

**Python Context:** Created with `{}` or `dict()`: `my_dict = {"name": "Alice", "age": 25}`. Fast lookup O(1).

**Related Terms:** Hash Table, Key-Value, Hashable, Map

---

### DRY (Don't Repeat Yourself)
The principle that every piece of knowledge in a program should have exactly one authoritative home. When the same logic lives in several places, a fix applied to one copy silently misses the others.

**Python Context:** Extract duplicated code into a function and call it from everywhere: one `format_price()` helper instead of five slightly different copies of the same two lines.

**Related Terms:** Code Smell, Refactoring, Abstraction

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

### Endianness
The byte order a computer uses to store multi-byte numbers. Big-endian puts the most significant byte first; little-endian puts the least significant byte first.

**Python Context:** `int.to_bytes(1000, 2, "big")` and `int.to_bytes(1000, 2, "little")` produce different byte orders — it matters when reading binary files or network protocols byte by byte.

**Related Terms:** Binary, Byte, Binary Files

---

### ETL (Extract, Transform, Load)
A pipeline pattern for moving data: extract it from a source, transform it into a clean, consistent shape, then load it into its destination (often a database). Most data-processing scripts are small ETL jobs.

**Python Context:** Read a messy CSV with the `csv` module, clean and reshape it with plain Python, then insert the rows into SQLite with `executemany()`.

**Related Terms:** Data Validation, SQL, Data Structure

---

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

### Hexadecimal
A base-16 number system using the digits 0-9 and A-F. One hex digit represents exactly 4 bits, which makes hexadecimal a compact, human-friendly way to write binary values.

**Python Context:** Hex literals start with `0x`: `0xFF` equals `255`, and `hex(255)` returns `'0xff'`. Color codes like `#1e1e2e` and memory addresses use the same idea.

**Related Terms:** Binary, Bit, Byte

---

### Higher-Order Function
A function that takes other functions as arguments or returns a function as its result.

**Python Context:** `map()`, `filter()`, `reduce()` are higher-order functions. Custom functions can also be higher-order.

**Related Terms:** Function, Callback, Lambda, Closure

---

### HTTP Header
A key-value pair that carries metadata about an HTTP request or response — the format of the body, its length, authentication tokens, caching rules. Headers travel before the body.

**Python Context:** `Content-Type: application/json` tells the client how to parse the response. With `urllib.request` you attach headers to a `Request` object before sending it.

**Related Terms:** HTTP Method, HTTP Status Code, API

---

### HTTP Method
The verb in an HTTP request that tells the server which action you want. The main ones: GET (read), POST (create), PUT (replace/update), and DELETE (remove).

**Python Context:** `urllib.request.Request(url, data=payload, method="POST")` sends a POST request. GET requests carry no body and should never change server data.

**Related Terms:** HTTP Header, HTTP Status Code, REST

---

### HTTP Status Code
A three-digit number the server returns with every response, summarising what happened: 2xx means success, 3xx a redirect, 4xx a problem with your request, 5xx a failure on the server side.

**Python Context:** `200 OK` is success, `404 Not Found` means the resource does not exist, and `500 Internal Server Error` means the server crashed. Always check the status code before parsing the body.

**Related Terms:** HTTP Method, HTTP Header, Exception

---

## I

### Idempotence
The property of an operation that has the same effect no matter how many times you repeat it. Idempotent operations are safe to retry; non-idempotent ones can double-charge a card or create a duplicate order.

**Python Context:** GET, PUT, and DELETE are idempotent HTTP methods; POST is not — retrying a failed POST may create the resource twice.

**Related Terms:** HTTP Method, REST, API

---

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

### Integration Test
A test that checks several pieces working together — your function plus a real temporary database, for example — instead of one unit in isolation. It catches wiring mistakes that unit tests miss.

**Python Context:** Create a throwaway SQLite database with the `tempfile` module, run a small end-to-end flow against it, then delete it afterwards.

**Related Terms:** Unit Test, Test Fixture, Mock

---

### Iterator
An object that implements the iterator protocol, allowing iteration over a sequence of values. Uses `__iter__()` and `__next__()` methods.

**Python Context:** Lists, strings, and dictionaries are iterable. The `iter()` function returns an iterator.

**Related Terms:** Iterable, Generator, Loop, __next__

---

## J

### JSON (JavaScript Object Notation)
A text format for structured data that nearly every programming language can read and write. JSON objects become Python dictionaries, arrays become lists, and the whole document is one (possibly long) string.

**Python Context:** `json.dumps(data)` turns Python objects into a JSON string; `json.loads(text)` turns JSON text back into Python objects. Note that JSON keys are always strings.

**Related Terms:** Dictionary (Dict), API, String

---

## K

### Key-Value Pair
A data representation where a unique key maps to a specific value. The foundation of dictionaries and hash tables.

**Python Context:** In `{"name": "Alice"}`, `"name"` is the key and `"Alice"` is the value.

**Related Terms:** Dictionary, Hash Table, Map, Entry

---

### KISS Principle (Keep It Simple, Stupid)
The principle that the simplest solution that works is usually the best one. Clever, intricate code impresses once and costs forever — future you still has to understand and maintain it.

**Python Context:** A three-line loop is often better than a nested one-liner stacking three comprehensions. Simple code is easier to test, debug, and change.

**Related Terms:** YAGNI (You Aren't Gonna Need It), DRY (Don't Repeat Yourself), Refactoring

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

### Mock
A stand-in object used in tests to replace something real — a network call, a database, the clock. A mock returns canned answers and records how it was used, so tests can verify interactions without touching the real thing.

**Python Context:** `unittest.mock.Mock()` remembers every call: `mock.fetch.assert_called_once_with("http://api.example.com")` checks the call happened exactly once, with that argument.

**Related Terms:** Stub, Unit Test, Integration Test

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

### Named Tuple
A tuple whose fields have names, so you can write `point.x` instead of `point[0]`. You get tuple-level immutability and low memory use plus readable, self-documenting field access.

**Python Context:** `Point = namedtuple("Point", ["x", "y"])` from the `collections` module, then `p = Point(3, 4)` and `p.x` returns `3`.

**Related Terms:** Tuple, Dictionary (Dict), Counter

---

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

### Parameterized Query
A SQL query with placeholders (`?`) for values, which are passed to the database separately instead of being pasted into the query string. The driver handles the quoting, so data can never be mistaken for SQL.

**Python Context:** `cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))` is safe. Building SQL with an f-string from user input is not — see SQL Injection.

**Related Terms:** SQL, SQL Injection, Primary Key

---

### Polymorphism
The ability of different classes to be treated as instances of the same superclass. Allows code to work with objects of different types.

**Python Context:** Method overriding (subclass redefines parent method) and duck typing are forms of polymorphism.

**Related Terms:** Inheritance, OOP, Method Overriding, Duck Typing

---

### Primary Key
A column (or combination of columns) that uniquely identifies each row in a database table. Databases use it to find, update, and link rows quickly, and to prevent duplicates.

**Python Context:** In `CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)`, SQLite automatically assigns increasing `id` values when you insert a row without one.

**Related Terms:** SQL, Parameterized Query, Key-Value Pair

---

### Prototype
An early sample or model of a product built to test a concept or process. In programming, a prototype helps validate ideas before full implementation.

**Python Context:** Python's interactive mode (`python` with no arguments) is great for prototyping code quickly.

**Related Terms:** MVP (Minimum Viable Product), Iteration, Development

---

## Q

### Query String
The part of a URL after a `?` that carries extra parameters, usually as `key=value` pairs joined by `&`. It is how GET forms and API filters hand small amounts of data to the server.

**Python Context:** In `/search?q=python&page=2`, `q` and `page` are parameters. `urllib.parse.parse_qs("q=python&page=2")` turns a query string into a dictionary.

**Related Terms:** URL, Route, HTTP Method

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

### Regression
A bug that reappears in something that used to work — usually because a later change broke it. A regression test is a test added at the moment you fix the bug, so the same bug cannot sneak back unnoticed.

**Python Context:** If `discount(price)` once mishandled `0`, add a `discount(0)` test case; every future test run then re-checks that exact situation.

**Related Terms:** Unit Test, Bug, Test-Driven Development (TDD)

---

### Regular Expression (Regex)
A compact pattern language for finding, extracting, and replacing text: "three digits", "a word followed by a colon", "an email-shaped string". Powerful, but easy to overuse when simple string methods would do.

**Python Context:** The `re` module: `re.findall(r"\d{3}-\d{4}", text)` finds phone-number-shaped strings. Raw strings (`r"..."`) keep backslashes from being eaten by Python.

**Related Terms:** String, Pattern Matching, Iterator

---

### REST (Representational State Transfer)
A style for designing web APIs around resources (nouns in the URL) combined with HTTP methods (the verbs): `GET /users/42` reads a user, `DELETE /users/42` removes it. A RESTful API is predictable once you know the pattern.

**Python Context:** Most public JSON APIs you call are REST-ish: combining the base URL, a resource path, and a method tells you what an endpoint does.

**Related Terms:** API, HTTP Method, JSON

---

### Route
A rule that maps a URL path (and usually an HTTP method) to the code that handles it. Routing is how a server answers `/about` with the about page and `/api/users` with user data.

**Python Context:** A tiny router is just a dictionary: `routes = {"/": home_page, "/about": about_page}` — look up the requested path and call the matching handler.

**Related Terms:** URL, Query String, HTTP Method

---

## S

### Scope
The region of code where a variable is visible and accessible. Python has local, enclosing, global, and built-in scopes (LEGB rule).

**Python Context:** Variables defined inside functions have local scope. Global variables are accessible throughout the module.

**Related Terms:** Namespace, Variable, Local, Global

---

### Separation of Concerns
Organising a program so that each part addresses one distinct responsibility. Parsing, business logic, and display live in separate functions or modules instead of being tangled together in one blob.

**Python Context:** Structure a report script in three layers: functions that read the data, functions that compute the totals, and functions that print. Each layer can change without breaking the others.

**Related Terms:** Cohesion, Coupling, Refactoring

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

### SQL (Structured Query Language)
The standard language for talking to relational databases: retrieving data (`SELECT`), adding it (`INSERT`), changing it (`UPDATE`), and removing it (`DELETE`).

**Python Context:** SQLite ships with Python: `import sqlite3`, open a database file, then `cursor.execute("SELECT name FROM users WHERE age > ?", (18,))`.

**Related Terms:** Parameterized Query, Primary Key, SQL Injection

---

### SQL Injection
A security hole where untrusted text is pasted directly into a SQL string, letting an attacker change the query's meaning — for example by ending the query early and adding their own SQL.

**Python Context:** `"SELECT * FROM users WHERE name = '" + user_input + "'"` is vulnerable. The fix is a parameterized query: values travel separately and are never parsed as SQL.

**Related Terms:** Parameterized Query, SQL, Bug

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

### Stub
A simplified stand-in for a dependency that always returns fixed, hard-coded answers — "when asked for the weather, always say sunny". Use one when the real thing is slow, random, or unavailable.

**Python Context:** Replace an HTTP call with a function that returns a saved JSON string, so the test runs offline in milliseconds. A Mock goes one step further and also records how it was called.

**Related Terms:** Mock, Unit Test, Integration Test

---

### Static File
A file a web server sends back exactly as it is stored on disk — HTML, CSS, JavaScript, images — without running any code. The opposite of a dynamic response, which a handler generates for each request.

**Python Context:** `python -m http.server` serves the files in the current directory automatically; real projects keep them in a `static/` folder behind a `/static/...` URL prefix.

**Related Terms:** Web Server, Template, Route

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

### Template
A text skeleton (usually HTML) with placeholders where the data goes. The program fills in real values at runtime, keeping layout and data separate.

**Python Context:** `f"<h1>{title}</h1>"` is the simplest template; `string.Template` offers `$title` placeholders and a `.substitute()` method.

**Related Terms:** Route, Static File, Separation of Concerns

---

### Test-Driven Development (TDD)
A workflow where you write a small failing test first, then just enough code to make it pass, then clean up. The red → green → refactor cycle keeps tests and features growing together.

**Python Context:** Write `test_discount_gives_10_percent()` before writing `discount()`; watch it fail, implement the function, watch it pass, then refactor with confidence.

**Related Terms:** Unit Test, Assertion, Regression

---

### Test Fixture
The fixed, known setup that tests need before they can run: sample data, temporary files, a test database. Fixtures keep each test independent and repeatable.

**Python Context:** In `unittest`, `setUp()` runs before each test to build the fixture and `tearDown()` cleans up afterwards — create a temporary SQLite database, drop it when done.

**Related Terms:** Unit Test, Integration Test, Mock

---

### Thread
The smallest unit of execution within a process. Threads in the same process share memory and resources.

**Python Context:** `threading.Thread` creates threads. Due to GIL, best for I/O-bound tasks, not CPU-bound.

**Related Terms:** Process, Concurrency, GIL, Multiprocessing

---

### Timezone-Aware Datetime
A datetime that knows which timezone it belongs to (it carries a `tzinfo`), as opposed to a naive datetime, which is just numbers with no anchor. Mixing the two in a comparison raises an error.

**Python Context:** `datetime.now(timezone.utc)` is aware; `datetime.now()` is naive. Store timestamps in UTC and convert them for display with the `zoneinfo` module.

**Related Terms:** UTC, Exception, String

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

### Truth Table
A table that lists every combination of input values for a logical expression and the output each combination produces. It is the surest way to reason about `and`, `or`, `not`, and combinations of them.

**Python Context:** `A or B` is `False` only when both are `False`; `not (A and B)` is `True` unless both are `True` — a four-row truth table proves it.

**Related Terms:** Boolean, Logical Operator, Condition

---

### Tuple
An ordered, immutable sequence. Similar to lists but cannot be modified after creation.

**Python Context:** Created with parentheses: `(1, 2, 3)`. Use for data that shouldn't change, like coordinates or database records.

**Related Terms:** List, Sequence, Immutable, Data Structure

---

### Two's Complement
The scheme computers use to represent negative integers: flip all the bits of the positive value and add 1. It lets the same circuits do signed and unsigned arithmetic.

**Python Context:** `~5` (bitwise NOT) returns `-6`, because Python integers behave like infinite-precision two's complement: `~n` always equals `-n - 1`.

**Related Terms:** Binary, Bitwise Mask, Bit Shift

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

### Unit Test
A small automated test that checks one piece of behaviour in isolation — usually a single function — with known inputs and an expected output. A suite of fast unit tests is a safety net for every change you make later.

**Python Context:** `unittest.TestCase` classes hold `test_` methods; each test calls your function and checks the result with `self.assertEqual(result, expected)`.

**Related Terms:** Integration Test, Assertion, Test Fixture

---

### URL (Uniform Resource Locator)
The address of a resource on the web, built from parts: the scheme (`https`), the host (`example.com`), the path (`/users/42`), and an optional query string (`?sort=name`).

**Python Context:** `urllib.parse.urlparse("https://example.com/users/42?sort=name")` splits a URL into those parts — the first step of most web and API lessons.

**Related Terms:** Query String, Route, HTTP Method

---

## V

### Variable
A named storage location that holds a value. Variables allow us to reference and manipulate data using meaningful names.

**Python Context:** Variables are dynamically typed: `x = 5` creates an integer, `x = "hello"` reassigns it to a string.

**Related Terms:** Assignment, Data Type, Scope, Name

---

## W

### Web Server
Software that listens for HTTP requests and sends back responses — files from disk for static content, or the output of your handler functions for dynamic pages.

**Python Context:** `python -m http.server 8000` starts a real web server from the standard library, and `http.server.BaseHTTPRequestHandler` lets you write custom request handlers.

**Related Terms:** HTTP Method, HTTP Status Code, Static File

---

### Wrapper
A function or class that provides a simplified interface to another, often more complex, component.

**Python Context:** Decorators wrap functions to add functionality. Wrapper classes adapt interfaces between incompatible types.

**Related Terms:** Decorator, Adapter, Interface, Abstraction

---

## Y

### YAGNI (You Aren't Gonna Need It)
The principle that you should not build a feature until you actually need it. Speculative code for imagined futures must be maintained, is rarely tested, and is usually wrong about the future anyway.

**Python Context:** Don't add a config file, a plugin system, or a database "just in case" — the ten-line script that solves today's problem is the right size.

**Related Terms:** KISS Principle (Keep It Simple, Stupid), Prototype, Technical Debt

---

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
