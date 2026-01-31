# 🌫️ Abstraction

Abstraction is about hiding the complex implementation details and showing only the essential features of the object. It reduces complexity and allows the programmer to focus on interactions on a higher level.

In Python, we achieve abstraction primarily using **Abstract Base Classes (ABCs)**.

## 🧱 Abstract Base Classes (ABCs)

An abstract class is a blueprint that **cannot be instantiated**. It is meant to be inherited by other classes.

It often contains **abstract methods**: methods that are declared but contain no implementation. Child classes **MUST** implement these methods.

To use ABCs in Python, we import from the `abc` module.

```python
from abc import ABC, abstractmethod

class Shape(ABC): # Inherit from ABC
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# s = Shape() # Error! Cannot instantiate abstract class
```

## 🏗️ Implementing Concrete Classes

Concrete classes are valid classes that inherit from the abstract class and implement all its abstract methods.

```python
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self): # Must implement this
        return self.side * self.side
    
    def perimeter(self): # Must implement this
        return 4 * self.side

s = Square(5)
print(s.area()) # 25
```

## 🔌 Interfaces

In many languages (like Java), there is a distinction between `abstract class` and `interface`. In Python, abstract Base Classes with *only* abstract methods act as interfaces. They define a contract that subclasses must follow.

## 🔑 Key Takeaways

1. **Abstraction**: Hiding details, showing essentials.
2. **ABC**: Abstract Base Class (from `abc` module).
3. **`@abstractmethod`**: Decorator to define a method that *must* be implemented by children.
4. **Enforcing Contracts**: ABCs ensure that all subclasses have the required methods.

---

[Next: Composition vs Inheritance](../06_composition_vs_inheritance/README.md)
