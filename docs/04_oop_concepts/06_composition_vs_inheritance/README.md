# 🧩 Composition vs Inheritance

In OOP, we often need to choose how to relate two classes.
- **Inheritance**: "Is-A" relationship.
- **Composition**: "Has-A" relationship.

## 👨‍👦 Inheritance ("Is-A")

Use inheritance when the child class *is a* type of the parent class and shares its behavior.
- Examples: `Car` is a `Vehicle`, `Manager` is an `Employee`.

**Pros:**
- Code reuse (don't repeat common logic).
- Polymorphism (treat child as parent).

**Cons:**
- Tightly coupled (changes in parent affect all children).
- Can lead to deep, confusing hierarchies.

## 🧱 Composition ("Has-A")

Use composition when the class *has a* component or part. Instead of inheriting, the class creates an instance of another class inside itself.
- Examples: `Car` has an `Engine`, `Computer` has a `CPU`.

**Pros:**
- Flexible (can change components at runtime).
- Loosely coupled.
- Avoids the "fragile base class" problem.

## 🧪 Example Comparison

**Inheritance Approach:**
```python
class Engine:
    def start(self): pass

class Car(Engine): # Weird: A Car IS NOT An Engine
    pass
```

**Composition Approach:**
```python
class Engine:
    def start(self): pass

class Car:
    def __init__(self):
        self.engine = Engine() # Correct: A Car HAS An Engine
    
    def start(self):
        self.engine.start() # Delegation
```

## ⚖️ The Rule of Thumb

> "Favor object composition over class inheritance." — *Design Patterns (GoF)*

Unless there is a clear "Is-A" relationship, composition is usually safer and more flexible.

---

[Next: SOLID Principles](../07_solid_principles/README.md)
