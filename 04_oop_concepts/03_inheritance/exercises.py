"""
03_inheritance/exercises.py

Practice inheritance!
"""

# -----------------------------------------------------------------------------
# Exercise 1: Shapes
# -----------------------------------------------------------------------------
# 1. Create a base class `Shape` with a method `area()` that returns 0.
# 2. Create a child class `Rectangle` that inherits from `Shape`.
#    - In `__init__`, accept `width` and `height`.
#    - Override `area()` to return `width * height`.
# 3. Create a child class `Circle` that inherits from `Shape`.
#    - In `__init__`, accept `radius`.
#    - Override `area()` to return `3.14 * radius * radius`.
# 4. Test both classes.

class Shape:
    def area(self):
        return 0

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
        return 3.14 * self.radius * self.radius

# Tests
print("\n--- Exercise 1 Output ---")

rect = Rectangle(5, 10)
circle = Circle(3)
print(f"Rectangle area: {rect.area()}")
print(f"Circle area: {circle.area()}")


# -----------------------------------------------------------------------------
# Exercise 2: Character Classes (Game)
# -----------------------------------------------------------------------------
# 1. Create a class `Character` with attributes `name` and `health`.
#    - Add a method `attack(target)` that prints "{name} attacks {target.name}!".
#    - Add a method `take_damage(amount)` that reduces health and prints new health.
# 2. Create a child class `Warrior` that inherits from `Character`.
#    - Override `attack` to print "{name} swings a sword at {target.name}!" AND call `target.take_damage(10)`.
# 3. Create a child class `Mage` that inherits from `Character`.
#    - Override `attack` to print "{name} casts a fireball at {target.name}!" AND call `target.take_damage(20)`.
# 4. Simulate a battle between a Warrior and a Mage.

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} now has {self.health} health.")

class Warrior(Character):
    def attack(self, target):
        print(f"{self.name} swings a sword at {target.name}!")
        target.take_damage(10)

class Mage(Character):
    def attack(self, target):
        print(f"{self.name} casts a fireball at {target.name}!")
        target.take_damage(20)

# Tests
print("\n--- Exercise 2 Output ---")

warrior = Warrior("Thorin", 100)
mage = Mage("Gandalf", 80)

warrior.attack(mage)
mage.attack(warrior)
