"""
05_abstraction/exercises.py

Practice creating abstract base classes!
"""

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# Exercise 1: Animal Kingdom
# -----------------------------------------------------------------------------
# 1. Create an abstract class `Animal` using ABC.
# 2. Define an abstract method `make_sound()`.
# 3. Define an abstract method `move()`.
# 4. Create concrete classes `Bird` and `Fish` that inherit from `Animal`.
#    - Bird: make_sound -> "Chirp", move -> "Flying"
#    - Fish: make_sound -> "Blub", move -> "Swimming"
# 5. Try to instantiate `Animal` (it should fail).
# 6. Instantiate Bird and Fish and call their methods.

class Animal(ABC):
    # TODO: Implement this abstract class
    pass

class Bird(Animal):
    # TODO: Implement this class
    pass

class Fish(Animal):
    # TODO: Implement this class
    pass

# TODO: Test your code
print("\n--- Exercise 1 Output ---")


# -----------------------------------------------------------------------------
# Exercise 2: Appliance Interface
# -----------------------------------------------------------------------------
# 1. Create an abstract class `Appliance`.
# 2. Abstract methods: `turn_on()`, `turn_off()`.
# 3. Concrete method in `Appliance`: `plug_in()` whch prints "Appliance plugged in.".
# 4. Create a `WashingMachine` class.
#    - Implement turn_on/off.
# 5. Create a `Microwave` class.
#    - Implement turn_on/off.
# 6. Create a function `operate(appliance)` that plugs it in, turns it on, then turns it off.

class Appliance(ABC):
    # TODO: Implement this abstract class
    pass

class WashingMachine(Appliance):
    # TODO: Implement this class
    pass

class Microwave(Appliance):
    # TODO: Implement this class
    pass

# TODO: Test your code
print("\n--- Exercise 2 Output ---")
