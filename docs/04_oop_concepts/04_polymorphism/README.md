# 🎭 Polymorphism

**Polymorphism** means "many forms". In programming, it refers to the ability of different objects to respond to the same method call in their own way.

## 🦆 Duck Typing

Python is a dynamic language that relies on **duck typing**:
> "If it walks like a duck and quacks like a duck, then it must be a duck."

We don't care about the *type* of the object, only if it has the method we want to call.

```python
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

def make_it_speak(animal):
    # We don't care if animal is a Dog or a Cat, 
    # as long as it has a speak() method.
    animal.speak()

make_it_speak(Dog()) # Woof
make_it_speak(Cat()) # Meow
```

## ➕ Operator Overloading

Polymorphism also allows us to define how operators like `+`, `-`, `*`, `==` behave for our custom objects using "magic methods" (dunder methods).

- `__str__(self)`: String representation (user-friendly).
- `__add__(self, other)`: Behavior for `+`.
- `__eq__(self, other)`: Behavior for `==`.
- `__len__(self)`: Behavior for `len()`.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Defines behavior for: point1 + point2
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3) # Output: (4, 6)
```

## 🔑 Key Takeaways

1. **Polymorphism**: Different objects responding to the same interface.
2. **Duck Typing**: Focus on what an object *can do*, not what it *is*.
3. **Magic Methods**: Special methods like `__init__`, `__str__`, `__add__` that allow operator overloading.
4. **Flexibility**: Makes code more generic and reusable.

---

[Next: Abstraction](../05_abstraction/README.md)
