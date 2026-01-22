"""
07_solid_principles/exercises.py

Practice refactoring code to follow SOLID principles!
"""

# -----------------------------------------------------------------------------
# Exercise 1: Refactor to SRP
# -----------------------------------------------------------------------------
# The following class violates SRP. Break it down into 3 classes:
# 1. `Report` (holds data)
# 2. `ReportPrinter` (formatting/printing)
# 3. `ReportSaver` (saving to file)

# --- Original (Violates SRP) ---
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def generate_report(self):
        return f"{self.title}\n{self.content}"
    
    def print_report(self):
        print(f"Printing: {self.title}...")
        print(self.content)
    
    def save_to_file(self, filename):
        print(f"Saving to {filename}...")
        # (Imagine file writing logic here)

# --- Your Refactoring Below ---

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        return f"{self.title}\n{self.content}"

class ReportPrinter:
    def print_report(self, report):
        print(f"Printing: {report.title}...")
        print(report.content)

class ReportSaver:
    def save(self, report, filename):
        print(f"Saving to {filename}...")
        # (Imagine file writing logic here)

# Tests
print("\n--- Exercise 1 Output ---")

report = Report("Weekly", "All systems operational.")
printer = ReportPrinter()
saver = ReportSaver()

print(report.generate())
printer.print_report(report)
saver.save(report, "weekly.txt")


# -----------------------------------------------------------------------------
# Exercise 2: Refactor to OCP
# -----------------------------------------------------------------------------
# The `DiscountCalculator` violates OCP. If we want to add a "VIP" discount,
# we have to modify the class. 
# Refactor it using inheritance/polymorphism so that new discount types 
# can be added without changing the calculator logic.

# --- Original (Violates OCP) ---
class DiscountCalculator:
    def calculate(self, customer_type, price):
        if customer_type == "Regular":
            return price
        elif customer_type == "Member":
            return price * 0.90
        elif customer_type == "SuperMember": # Had to modify this to add new type
            return price * 0.85

# --- Your Refactoring Below ---

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class RegularDiscount(DiscountStrategy):
    def apply(self, price):
        return price


class MemberDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.90


class VipDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.85


class DiscountCalculator:
    def calculate(self, strategy, price):
        return strategy.apply(price)

# Tests
print("\n--- Exercise 2 Output ---")

calc = DiscountCalculator()
price = 100
print(calc.calculate(RegularDiscount(), price))
print(calc.calculate(MemberDiscount(), price))
print(calc.calculate(VipDiscount(), price))
