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
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

    def move(self):
        return "Flying"

class Fish(Animal):
    def make_sound(self):
        return "Blub"

    def move(self):
        return "Swimming"

# Tests
print("\n--- Exercise 1 Output ---")

bird = Bird()
fish = Fish()
print(bird.make_sound())
print(bird.move())
print(fish.make_sound())
print(fish.move())


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
    def plug_in(self):
        print("Appliance plugged in.")

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine on.")

    def turn_off(self):
        print("Washing machine off.")

class Microwave(Appliance):
    def turn_on(self):
        print("Microwave on.")

    def turn_off(self):
        print("Microwave off.")

# Tests
print("\n--- Exercise 2 Output ---")

def operate(appliance):
    appliance.plug_in()
    appliance.turn_on()
    appliance.turn_off()

operate(WashingMachine())
operate(Microwave())
