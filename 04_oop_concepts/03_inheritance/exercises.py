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
    # TODO: Implement this class
    pass

class Rectangle(Shape):
    # TODO: Implement this class
    pass

class Circle(Shape):
    # TODO: Implement this class
    pass

# TODO: Test your classes
print("\n--- Exercise 1 Output ---")


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
    # TODO: Implement this class
    pass

class Warrior(Character):
    # TODO: Implement this class
    pass

class Mage(Character):
    # TODO: Implement this class
    pass

# TODO: Test your battle
print("\n--- Exercise 2 Output ---")
