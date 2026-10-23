"""
SOLID Principles - Examples
===========================
Run this file to see all five SOLID principles in action:
SRP, OCP, LSP, ISP, and DIP.
"""

from abc import ABC, abstractmethod

print("=" * 50)
print("SOLID PRINCIPLES - Examples")
print("=" * 50)

# =============================================================================
# 1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# One class = one job = one reason to change.
# =============================================================================
print("\n--- 1. Single Responsibility Principle ---\n")

# BAD: Order does math, database work, AND email.
# class Order:
#     def calculate_total(self): ...
#     def save_to_database(self): ...
#     def send_confirmation_email(self): ...

# GOOD: split each job into its own class.
class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

class OrderRepository:
    def save(self, order):
        print("Saving order to database...")

class EmailService:
    def send_confirmation(self, order):
        print("Sending confirmation email...")

order = Order([{"name": "Apple", "price": 2.0}, {"name": "Banana", "price": 1.0}])
print(f"Order total: ${order.calculate_total()}")
OrderRepository().save(order)
EmailService().send_confirmation(order)


# =============================================================================
# 2. OPEN/CLOSED PRINCIPLE (OCP)
# Open for extension, closed for modification.
# =============================================================================
print("\n--- 2. Open/Closed Principle ---\n")

# BAD: adding a Triangle means editing AreaCalculator's if/elif chain.
# class AreaCalculator:
#     def total_area(self, shapes):
#         total = 0
#         for shape in shapes:
#             if isinstance(shape, Rectangle): ...
#             elif isinstance(shape, Circle): ...

# GOOD: new shapes plug in; the calculator never changes.
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

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    # Added LATER, without touching AreaCalculator at all.
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class AreaCalculator:
    def total_area(self, shapes):
        return sum(shape.area() for shape in shapes)

shapes = [Rectangle(10, 20), Circle(5), Triangle(6, 4)]
print(f"Total area of 3 shapes: {AreaCalculator().total_area(shapes)}")


# =============================================================================
# 3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
# A subclass must keep every promise its parent class makes.
# =============================================================================
print("\n--- 3. Liskov Substitution Principle ---\n")

# BAD: Bird promises fly(), but a Penguin is a Bird that cannot fly.
class Bird:
    def fly(self):
        print("Flying!")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins cannot fly!")

def make_it_fly(bird):
    bird.fly()   # promised to work for ANY Bird... supposedly

try:
    make_it_fly(Penguin())   # substitute a Penguin where a Bird is expected
    print("FAIL: expected the Penguin substitution to break")
except NotImplementedError:
    print("FAIL: substituting Penguin for Bird broke the code")

# GOOD: the base class only promises "move"; only flying birds add fly().
class Animal:
    def move(self):
        return "moving"

class FlyingBird(Animal):
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying!")

class SwimmingBird(Animal):
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f"{self.name} is swimming!")

zoo = [FlyingBird("Eagle"), SwimmingBird("Penguin")]
for creature in zoo:
    print(f"{creature.name}: {creature.move()}")
zoo[0].fly()
zoo[1].swim()
print("PASS: every subclass keeps the promises of its base class")


# =============================================================================
# 4. INTERFACE SEGREGATION PRINCIPLE (ISP)
# No class should be forced to implement methods it does not use.
# =============================================================================
print("\n--- 4. Interface Segregation Principle ---\n")

# BAD: one fat interface forces a simple printer to fake scanning and faxing.
class OfficeMachine(ABC):
    @abstractmethod
    def print_doc(self): ...
    @abstractmethod
    def scan_doc(self): ...
    @abstractmethod
    def fax_doc(self): ...

class SimplePrinter(OfficeMachine):
    def print_doc(self):
        print("SimplePrinter: printing document...")

    def scan_doc(self):
        raise NotImplementedError("I cannot scan!")   # forced to fake it

    def fax_doc(self):
        raise NotImplementedError("I cannot fax!")    # forced to fake it

try:
    SimplePrinter().scan_doc()
    print("FAIL: expected the forced scan_doc call to break")
except NotImplementedError:
    print("FAIL: SimplePrinter was forced to promise scanning")

# GOOD: several small interfaces; classes implement only what they really do.
class Printer(ABC):
    @abstractmethod
    def print_doc(self): ...

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self): ...

class AllInOne(Printer, Scanner):
    def print_doc(self):
        print("AllInOne: printing document...")

    def scan_doc(self):
        print("AllInOne: scanning document...")

class BasicPrinter(Printer):
    def print_doc(self):
        print("BasicPrinter: printing document...")

for machine in (AllInOne(), BasicPrinter()):
    machine.print_doc()   # every Printer can print: no surprises
print("PASS: no machine implements a method it does not use")


# =============================================================================
# 5. DEPENDENCY INVERSION PRINCIPLE (DIP)
# Depend on abstractions, not on concrete classes.
# =============================================================================
print("\n--- 5. Dependency Inversion Principle ---\n")

# BAD: the service builds its own dependency -- hard to swap, hard to test.
# class NotificationService:
#     def __init__(self):
#         self.sender = EmailSender()          # welded to one provider

# GOOD: the service depends on a Notifier abstraction; callers inject one.
class Notifier(ABC):
    @abstractmethod
    def send(self, message): ...

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Email: {message}")

class SmsNotifier(Notifier):
    def send(self, message):
        print(f"SMS:   {message}")

class NotificationService:
    def __init__(self, notifier):
        self.notifier = notifier   # accepts ANY Notifier

    def notify(self, message):
        self.notifier.send(message)

for notifier in (EmailNotifier(), SmsNotifier()):
    service = NotificationService(notifier)   # swap with zero code changes
    service.notify("Your order has shipped!")
print("PASS: the service never changed -- only the injected dependency did")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
