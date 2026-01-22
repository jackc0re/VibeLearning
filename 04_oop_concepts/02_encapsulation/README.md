# 🔒 Encapsulation

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent likely accidental modification of data.

To put it simply, an object should keep its private state ... private!

## 🙈 Public vs. Protected vs. Private

In Python, we don't have strict access modifiers like `public`, `private`, or `protected` in languages like Java or C++. Instead, we use **naming conventions**.

### 1. Public
- Accessible from anywhere.
- No underscores.
- Example: `self.name`

### 2. Protected
- Should not be accessed outside the class or its subclasses (but technically still can be).
- One underscore prefix.
- Example: `self._internal_id`

### 3. Private
- Should NOT be accessed outside the class. Python performs name mangling to make it harder (but not impossible) to access.
- Two underscore prefix.
- Example: `self.__password`

## 🛡️ Getters and Setters

To control access to variables, we often use methods to "get" (read) or "set" (write) the values. This allows us to add validation logic.

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative!")
        else:
            self._age = age
```

## 🎩 The `@property` Decorator

Python provides a "Pythonic" way to use getters and setters using the `@property` decorator. It allows you to access a method like an attribute.

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value

p = Person(25)
p.age = -5  # Triggers the validation in the setter!
```

## 🔑 Key Takeaways

1. **Encapsulation**: Bundling data and methods, restricting direct access.
2. **`_variable`**: Protected (convention).
3. **`__variable`**: Private (name mangling).
4. **Getters/Setters**: Methods to control access.
5. **`@property`**: The elegant way to implement getters/setters in Python.

---

[Next: Inheritance](../03_inheritance/README.md)
