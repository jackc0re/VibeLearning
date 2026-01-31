"""
07_solid_principles/examples.py

A brief demonstration of SRP and OCP.
"""

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# 1. Single Responsibility Principle (SRP)
# -----------------------------------------------------------------------------
print("\n--- 1. SRP ---")

# BAD:
# class Order:
#     def calculate_total(self): ...
#     def save_to_database(self): ...
#     def send_confirmation_email(self): ...

# GOOD:
class Order:
    def __init__(self, items):
        self.items = items
    
    def calculate_total(self):
        return sum(item['price'] for item in self.items)

class OrderRepository:
    def save(self, order):
        print("Saving order to database...")

class EmailService:
    def send_confirmation(self, order):
        print("Sending email confirmation...")

order = Order([{'name': 'Apple', 'price': 2}, {'name': 'Banana', 'price': 1}])
repo = OrderRepository()
mailer = EmailService()

print(f"Total: ${order.calculate_total()}")
repo.save(order)
mailer.send_confirmation(order)


# -----------------------------------------------------------------------------
# 2. Open/Closed Principle (OCP)
# -----------------------------------------------------------------------------
print("\n--- 2. OCP ---")

# We want to calculate area for different shapes.
# BAD: Modifying the AreaCalculator every time we add a shape.
# class AreaCalculator:
#     def area(self, shape):
#         if isinstance(shape, Rectangle): ...
#         elif isinstance(shape, Circle): ... 

# GOOD: Shapes define their own area. Calculator just calls it.

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

class AreaCalculator:
    def total_area(self, shapes):
        return sum(shape.area() for shape in shapes)

shapes = [Rectangle(10, 20), Circle(5)]
calc = AreaCalculator()
print(f"Total Area: {calc.total_area(shapes)}")
