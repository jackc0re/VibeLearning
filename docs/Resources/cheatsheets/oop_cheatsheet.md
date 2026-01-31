# OOP Cheatsheet

Quick reference for Object-Oriented Programming in Python: classes, inheritance, polymorphism, magic methods, and SOLID principles.

---

## Classes & Objects

### Defining a Class
```python
class Dog:
    """A simple dog class."""

    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, age):
        """Initialize instance attributes."""
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute

    def bark(self):
        """Instance method."""
        return f"{self.name} says Woof!"

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Class method - alternative constructor."""
        age = 2024 - birth_year
        return cls(name, age)

    @staticmethod
    def is_valid_age(age):
        """Static method - no self/cls."""
        return 0 <= age <= 30
```

### Creating & Using Objects
```python
# Create instance
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Access attributes
print(dog1.name)        # "Buddy"
print(dog1.species)     # "Canis familiaris" (class attribute)

# Call methods
print(dog1.bark())      # "Buddy says Woof!"

# Class method
dog3 = Dog.from_birth_year("Luna", 2018)

# Static method
print(Dog.is_valid_age(3))  # True
```

---

## Encapsulation

### Public, Protected, Private
```python
class Account:
    def __init__(self, balance):
        self.balance = balance           # Public attribute
        self._pin = "1234"              # Protected (convention)
        self.__password = "secret"      # Private (name mangling)

    def get_balance(self):
        """Getter method."""
        return self.balance

    def set_balance(self, balance):
        """Setter method with validation."""
        if balance >= 0:
            self.balance = balance

    @property
    def balance(self):
        """Property - accessed like an attribute."""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Property setter."""
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative")
```

---

## Inheritance

### Basic Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Call parent __init__
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage
dog = Dog("Buddy", "Labrador")
print(dog.name)         # "Buddy"
print(dog.speak())       # "Woof!"
```

### Multiple Inheritance
```python
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "Quack!"

# Method Resolution Order (MRO)
print(Duck.mro())
# [<class 'Duck'>, <class 'Animal'>, <class 'Flyable'>,
#  <class 'Swimmable'>, <class 'object'>]
```

### Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class."""

    @abstractmethod
    def area(self):
        """Abstract method - must be implemented."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method - must be implemented."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Cannot instantiate abstract class
# shape = Shape()  # TypeError

rect = Rectangle(5, 3)
print(rect.area())      # 15
```

---

## Polymorphism

### Method Overriding
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"      # Override parent method

class Cat(Animal):
    def speak(self):
        return "Meow!"      # Override parent method

# Polymorphic usage
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())  # "Woof!", "Meow!"
```

### Duck Typing
```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

def make_quack(obj):
    """Function works with any object with quack()."""
    return obj.quack()

# Both work - duck typing
make_quack(Duck())      # "Quack!"
make_quack(Person())    # "I'm quacking like a duck!"
```

---

## Magic (Dunder) Methods

### String Representation
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.name} ({self.age})"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 25)
print(person)           # "Alice (25)" - uses __str__
print(repr(person))     # "Person(name='Alice', age=25)" - uses __repr__
```

### Comparison Operators
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __le__(self, other):
        return self <= other

    def __gt__(self, other):
        return self > other

    def __ge__(self, other):
        return self >= other

p1 = Point(1, 2)
p2 = Point(3, 4)

p1 < p2                 # True
p1 == p1                # True
```

### Arithmetic Operators
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)          # Vector(6, 8)
print(v1 * 2)           # Vector(4, 6)
```

### Container Methods
```python
class MyList:
    def __init__(self, items=None):
        self.items = items or []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

# Usage
my_list = MyList([1, 2, 3])
print(len(my_list))     # 3
print(my_list[0])       # 1
my_list[0] = 10         # Modify
2 in my_list            # True
for item in my_list:
    print(item)         # Iteration
```

### Callable Objects
```python
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        return self.count

counter = Counter(5)
print(counter())        # 6
print(counter())        # 7
```

---

## Decorators for Classes

### @property
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter with validation."""
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Computed property (read-only)."""
        return 3.14 * self._radius ** 2

circle = Circle(5)
print(circle.radius)     # 5
print(circle.area)       # 78.5
circle.radius = 10      # Valid
```

### @staticmethod & @classmethod
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        """No access to class or instance."""
        return a + b

    @classmethod
    def from_string(cls, s):
        """Alternative constructor."""
        parts = s.split()
        return cls(int(parts[0]), int(parts[1]))

result = MathUtils.add(1, 2)    # 3
```

### Dataclasses
```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Employee:
    name: str
    age: int
    salary: float
    skills: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Called after initialization."""
        if self.age < 18:
            raise ValueError("Employee must be 18+")

# Automatically gets __init__, __repr__, __eq__
emp = Employee("Alice", 25, 50000, ["Python", "SQL"])
print(emp)  # Employee(name='Alice', age=25, salary=50000, skills=['Python', 'SQL'])
```

---

## SOLID Principles

### S - Single Responsibility
```python
# Bad: Multiple responsibilities
class User:
    def __init__(self, name):
        self.name = name

    def save_to_db(self):
        pass  # Database logic mixed with user logic

# Good: Separated concerns
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        pass  # Database logic
```

### O - Open/Closed Principle
```python
# Bad: Must modify to add new shape
class AreaCalculator:
    def calculate(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * shape.radius ** 2

# Good: Open for extension, closed for modification
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class AreaCalculator:
    def calculate(self, shape):
        return shape.area()  # Works with any Shape
```

### L - Liskov Substitution Principle
```python
# Bad: Violates LSP
class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")

# Good: Separate behaviors
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Penguin(Bird):
    def swim(self):
        pass
```

### I - Interface Segregation Principle
```python
# Bad: Large interface
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

# Good: Segregated interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass
```

### D - Dependency Inversion Principle
```python
# Bad: High-level depends on low-level
class LightSwitch:
    def __init__(self):
        self.bulb = LightBulb()

    def toggle(self):
        self.bulb.turn_on()

# Good: Depends on abstraction
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class LightSwitch:
    def __init__(self, device: Switchable):
        self.device = device

    def toggle(self):
        self.device.turn_on()
```

---

## Common Patterns

### Singleton
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

### Factory
```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animals = {
            "dog": Dog,
            "cat": Cat,
            "bird": Bird
        }
        return animals.get(animal_type)()
```

### Observer
```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)
```

---

## Quick Reference

| Concept | Syntax | Purpose |
|---------|--------|---------|
| **Class** | `class Name:` | Define class |
| **Init** | `def __init__(self):` | Constructor |
| **Property** | `@property` | Computed attribute |
| **Static Method** | `@staticmethod` | Class utility |
| **Class Method** | `@classmethod` | Alternative constructor |
| **Abstract** | `@abstractmethod` | Force implementation |
| **Inheritance** | `class Child(Parent):` | Extend class |
| **Super** | `super().__init__()` | Call parent method |

**Back to [Resources](../README.md)**
