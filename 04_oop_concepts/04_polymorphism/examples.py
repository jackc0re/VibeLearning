"""
04_polymorphism/examples.py

Demonstrating polymorphism, duck typing, and operator overloading.
"""

# -----------------------------------------------------------------------------
# 1. Polymorphism with Functions (Duck Typing)
# -----------------------------------------------------------------------------
print("\n--- 1. Duck Typing ---")

class English:
    def greet(self):
        return "Hello!"

class Spanish:
    def greet(self):
        return "Hola!"

class French:
    def greet(self):
        return "Bonjour!"

def say_hello(person):
    # The function doesn't care what class 'person' belongs to
    print(person.greet())

people = [English(), Spanish(), French()]

for p in people:
    say_hello(p)


# -----------------------------------------------------------------------------
# 2. Polymorphism with Inheritance
# -----------------------------------------------------------------------------
print("\n--- 2. Polymorphism via Inheritance ---")

import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

shapes = [Rectangle(10, 20), Circle(5), Rectangle(2, 3)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")


# -----------------------------------------------------------------------------
# 3. Operator Overloading (Magic Methods)
# -----------------------------------------------------------------------------
print("\n--- 3. Operator Overloading ---")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation (for print())
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Addition (+)
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Equality (==)
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    # Multiplication (*) - Scalar multiplication
    def __mul__(self, other):
        if isinstance(other, (int, float)):
             return Vector(self.x * other, self.y * other)
        return NotImplemented

v1 = Vector(2, 4)
v2 = Vector(3, 1)

print(f"v1: {v1}")
print(f"v2: {v2}")

# Using +
v3 = v1 + v2
print(f"v1 + v2 = {v3}") # Output: Vector(5, 5)

# Using ==
print(f"v1 == v2? {v1 == v2}")
print(f"v1 == Vector(2, 4)? {v1 == Vector(2, 4)}")

# Using *
v4 = v1 * 3
print(f"v1 * 3 = {v4}") # Output: Vector(6, 12)
