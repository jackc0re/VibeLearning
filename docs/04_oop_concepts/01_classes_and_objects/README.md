# 🏗️ Classes and Objects

Welcome to the world of **Object-Oriented Programming (OOP)**! OOP is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods).

## 📚 What are Classes and Objects?

Think of a **Class** as a **blueprint** or a **template**. It defines how something should look and behave.
Think of an **Object** as a distinct **instance** created from that blueprint.

**Real-world Analogy:**
- **Class**: The blueprint for a Car (specifies it has wheels, color, model, and can drive).
- **Object**: A specific red Toyota Corolla in your driveway.

## 🛠️ Defining a Class

In Python, we use the `class` keyword.

```python
class Dog:
    pass
```

## 🏭 Creating an Object

To create an object (instance), we call the class like a function.

```python
my_dog = Dog()
```

## 🧬 Attributes and `__init__`

Attributes are variables that belong to an object. We usually initialize them in a special method called `__init__` (the constructor).

- **`self`**: Represents the specific instance of the class. It allows each object to store its own data.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name   # Attribute
        self.breed = breed # Attribute
```

## ⚡ Methods

Methods are functions defined inside a class that describe the behaviors of an object.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"
```

## 📝 Example

```python
# 1. Define the class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I got a {self.grade}!")

# 2. Create objects
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

# 3. Access attributes and methods
student1.introduce() # Output: Hi, I'm Alice and I got a A!
print(student2.name) # Output: Bob
```

## 🔍 Key Takeaways

1. **Class**: The template.
2. **Object**: The instance.
3. **Attributes**: Data stored in the object (`self.variable`).
4. **Methods**: Functions that operate on the object's data.
5. **`self`**: A reference to the current instance.

---

[Next: Encapsulation](../02_encapsulation/README.md)
