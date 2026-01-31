# 📝 Functions Basics - Quiz

Test your function knowledge!

---

## Question 1
What does `def` stand for?

A) Default  
B) Define  
C) Defer  
D) Defend

<details>
<summary>Click for answer</summary>

**B) Define**

`def` is short for "define" - it defines a new function.

</details>

---

## Question 2
What does this function return?
```python
def mystery():
    x = 5
```

A) 5  
B) x  
C) None  
D) Error

<details>
<summary>Click for answer</summary>

**C) None**

Functions without a `return` statement implicitly return `None`.

</details>

---

## Question 3
What's the output?
```python
def greet(name="World"):
    return f"Hello, {name}"

print(greet())
```

A) Hello,  
B) Hello, World  
C) Hello, name  
D) Error

<details>
<summary>Click for answer</summary>

**B) Hello, World**

When no argument is passed, the default value "World" is used.

</details>

---

## Question 4
What does `*args` do?

A) Creates a pointer  
B) Multiplies arguments  
C) Collects variable positional arguments  
D) Makes arguments optional

<details>
<summary>Click for answer</summary>

**C) Collects variable positional arguments**

`*args` collects any number of positional arguments into a tuple.

</details>

---

## Question 5
What's the output?
```python
def add(a, b):
    return a + b

result = add(b=5, a=3)
print(result)
```

A) Error  
B) 8  
C) 53  
D) 35

<details>
<summary>Click for answer</summary>

**B) 8**

Keyword arguments can be in any order. `a=3, b=5`, so 3 + 5 = 8.

</details>

---

## Question 6
What will happen?
```python
x = 10

def change():
    x = 20

change()
print(x)
```

A) 10  
B) 20  
C) Error  
D) None

<details>
<summary>Click for answer</summary>

**A) 10**

The `x = 20` inside the function creates a local variable. The global `x` remains unchanged.

</details>

---

## Question 7
Which is a valid lambda?

A) `lambda: x * 2`  
B) `lambda x: x * 2`  
C) `def lambda(x): return x * 2`  
D) `lambda x: return x * 2`

<details>
<summary>Click for answer</summary>

**B) `lambda x: x * 2`**

Lambda syntax: `lambda parameters: expression`. No `return` keyword needed.

</details>

---

## Question 8
What's returned?
```python
def split_name(full_name):
    parts = full_name.split()
    return parts[0], parts[1]

first, last = split_name("John Doe")
```

A) "John Doe"  
B) ("John", "Doe")  
C) ["John", "Doe"]  
D) Error

<details>
<summary>Click for answer</summary>

**B) ("John", "Doe")**

Returning multiple values separated by commas creates a tuple.

</details>

---

## Question 9
What does `**kwargs` capture?

A) All arguments  
B) Variable positional arguments  
C) Variable keyword arguments  
D) Default arguments

<details>
<summary>Click for answer</summary>

**C) Variable keyword arguments**

`**kwargs` collects extra keyword arguments into a dictionary.

</details>

---

## Question 10
What's wrong with this?
```python
def add(a=0, b):
    return a + b
```

A) Nothing  
B) Default must come after non-default  
C) Can't have default for first parameter  
D) Wrong syntax for default

<details>
<summary>Click for answer</summary>

**B) Default must come after non-default**

Parameters with defaults must come after parameters without defaults.

</details>

---

## How did you do?

- **9-10 correct:** Function pro! 🏆
- **7-8 correct:** Strong understanding!
- **5-6 correct:** Keep practicing.
- **0-4 correct:** Review the README and examples.
