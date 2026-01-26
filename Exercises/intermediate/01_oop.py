"""
Intermediate Exercise 1: Object-Oriented Programming
=================================================
Practice classes, inheritance, polymorphism, and OOP principles.
"""

print("=" * 50)
print("EXERCISE 1: Object-Oriented Programming")
print("=" * 50)


# =============================================================================
# EXERCISE 1.1: Create a Class
# =============================================================================
print("\n--- Exercise 1.1: Create a Class ---")
"""
Create a Rectangle class with:
- Attributes: width, height
- Methods: area(), perimeter(), __str__()
"""


# Your code below:
class Rectangle:
    """A rectangle with width and height."""

    pass


# Test (uncomment after implementing)
# rect = Rectangle(5, 3)
# print(f"Rectangle: {rect}")
# print(f"Area: {rect.area()}")
# print(f"Perimeter: {rect.perimeter()}")


# =============================================================================
# EXERCISE 1.2: Inheritance
# =============================================================================
print("\n--- Exercise 1.2: Inheritance ---")
"""
Create a Square class that inherits from Rectangle.
Square should only take one side length.
"""


# Your code below:
class Square(Rectangle):
    """A square is a rectangle with equal sides."""

    pass


# Test (uncomment after implementing)
# square = Square(4)
# print(f"Square: {square}")
# print(f"Area: {square.area()}")


# =============================================================================
# EXERCISE 1.3: Encapsulation
# =============================================================================
print("\n--- Exercise 1.3: Encapsulation ---")
"""
Create a BankAccount class with:
- Private attributes: balance, account_number
- Public methods: deposit(), withdraw(), get_balance()
- Withdraw should prevent negative balance
"""


# Your code below:
class BankAccount:
    """A bank account with encapsulated data."""

    pass


# Test (uncomment after implementing)
# account = BankAccount("12345", 100)
# account.deposit(50)
# account.withdraw(30)
# print(f"Balance: ${account.get_balance()}")
# account.withdraw(200)  # Should fail


# =============================================================================
# EXERCISE 1.4: Polymorphism
# =============================================================================
print("\n--- Exercise 1.4: Polymorphism ---")
"""
Create a Shape base class with an abstract area() method.
Create Circle and Triangle subclasses.
"""

from abc import ABC, abstractmethod
import math


# Your code below:
class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    """A circle shape."""

    pass


class Triangle(Shape):
    """A triangle shape."""

    pass


# Test (uncomment after implementing)
# shapes = [Circle(5), Triangle(3, 4)]
# for shape in shapes:
#     print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


# =============================================================================
# EXERCISE 1.5: Composition
# =============================================================================
print("\n--- Exercise 1.5: Composition ---")
"""
Create an Engine and Car class.
Car should have an Engine as a component (not inherit).
"""


# Your code below:
class Engine:
    """An engine for a car."""

    pass


class Car:
    """A car with an engine."""

    pass


# Test (uncomment after implementing)
# car = Car("Toyota", "V6")
# car.start()
# print(car)


# =============================================================================
# EXERCISE 1.6: Class Methods and Static Methods
# =============================================================================
print("\n--- Exercise 1.6: Class and Static Methods ---")
"""
Create a Temperature class with:
- Static method: celsius_to_fahrenheit()
- Class method: from_kelvin()
"""


# Your code below:
class Temperature:
    """Temperature conversion utility."""

    pass


# Test (uncomment after implementing)
# temp1 = Temperature.celsius_to_fahrenheit(25)
# temp2 = Temperature.from_kelvin(300)
# print(f"25°C = {temp1}°F")
# print(f"300K = {temp2}°C")


# =============================================================================
# EXERCISE 1.7: Property Decorators
# =============================================================================
print("\n--- Exercise 1.7: Property Decorators ---")
"""
Create a Person class with name and age.
Use @property for age to enforce minimum age of 0.
"""


# Your code below:
class Person:
    """A person with name and age."""

    pass


# Test (uncomment after implementing)
# person = Person("Alice", 25)
# print(person)
# person.age = 30
# print(f"Updated age: {person.age}")
# person.age = -5  # Should fail


# =============================================================================
# EXERCISE 1.8: Magic Methods
# =============================================================================
print("\n--- Exercise 1.8: Magic Methods ---")
"""
Create a Vector class with:
- __add__, __sub__, __mul__ (scalar multiplication)
- __eq__, __len__
- __repr__
"""


# Your code below:
class Vector:
    """A 2D vector."""

    pass


# Test (uncomment after implementing)
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
# print(f"v1 = {v1}")
# print(f"v2 = {v2}")
# print(f"v1 + v2 = {v1 + v2}")
# print(f"v1 - v2 = {v1 - v2}")
# print(f"v1 * 2 = {v1 * 2}")
# print(f"v1 == v2 = {v1 == v2}")
# print(f"len(v1) = {len(v1)}")


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1.1
print("\n--- Solution 1.1 ---")


class Rectangle:
    """A rectangle with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


rect = Rectangle(5, 3)
print(f"Rectangle: {rect}")
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

# SOLUTION 1.2
print("\n--- Solution 1.2 ---")


class Square(Rectangle):
    """A square is a rectangle with equal sides."""

    def __init__(self, side):
        super().__init__(side, side)


square = Square(4)
print(f"Square: {square}")
print(f"Area: {square.area()}")

# SOLUTION 1.3
print("\n--- Solution 1.3 ---")


class BankAccount:
    """A bank account with encapsulated data."""

    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance


account = BankAccount("12345", 100)
account.deposit(50)
account.withdraw(30)
print(f"Balance: ${account.get_balance()}")
success = account.withdraw(200)
print(f"Withdraw $200: {'Success' if success else 'Failed'}")

# SOLUTION 1.4
print("\n--- Solution 1.4 ---")
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    """A circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Triangle(Shape):
    """A triangle shape."""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(5), Triangle(3, 4)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")

# SOLUTION 1.5
print("\n--- Solution 1.5 ---")


class Engine:
    """An engine for a car."""

    def __init__(self, type_):
        self.type = type_

    def start(self):
        return f"{self.type} engine started"


class Car:
    """A car with an engine."""

    def __init__(self, brand, engine_type):
        self.brand = brand
        self.engine = Engine(engine_type)

    def start(self):
        return f"{self.brand} - {self.engine.start()}"

    def __str__(self):
        return f"{self.brand} with {self.engine.type} engine"


car = Car("Toyota", "V6")
print(car.start())
print(car)

# SOLUTION 1.6
print("\n--- Solution 1.6 ---")


class Temperature:
    """Temperature conversion utility."""

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    @classmethod
    def from_kelvin(cls, kelvin):
        celsius = kelvin - 273.15
        return cls(celsius)

    def __init__(self, celsius):
        self.celsius = celsius


temp1 = Temperature.celsius_to_fahrenheit(25)
temp2 = Temperature.from_kelvin(300)
print(f"25°C = {temp1}°F")
print(f"300K = {temp2.celsius}°C")

# SOLUTION 1.7
print("\n--- Solution 1.7 ---")


class Person:
    """A person with name and age."""

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative")

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


person = Person("Alice", 25)
print(person)
person.age = 30
print(f"Updated age: {person.age}")
try:
    person.age = -5
except ValueError as e:
    print(f"Error: {e}")

# SOLUTION 1.8
print("\n--- Solution 1.8 ---")


class Vector:
    """A 2D vector."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 == v2 = {v1 == v2}")
print(f"len(v1) = {len(v1)}")

print("\n" + "=" * 50)
print("Great job! Move on to 02_functional.py")
print("=" * 50)
