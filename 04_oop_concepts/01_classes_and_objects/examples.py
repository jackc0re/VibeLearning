"""
01_classes_and_objects/examples.py

This file demonstrates the basics of classes and objects in Python.
"""

# -----------------------------------------------------------------------------
# 1. A Simple Class
# -----------------------------------------------------------------------------
print("\n--- 1. Simple Class ---")

class Car:
    """A simple class representing a car."""
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute
        self.model = model  # Attribute
        self.year = year    # Attribute
        self.is_running = False

    def start_engine(self):
        """Method to start the car."""
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.brand} {self.model} starts with a roar!")
        else:
            print("Engine is already on.")

    def stop_engine(self):
        """Method to stop the car."""
        if self.is_running:
            self.is_running = False
            print("Engine stopped.")
        else:
            print("Engine is already off.")

    def drive(self):
        """Method to drive the car."""
        if self.is_running:
            print(f"Driving the {self.model}...")
        else:
            print("You need to start the engine first!")

# Creating Instances (Objects)
my_car = Car("Toyota", "Corolla", 2022)
dream_car = Car("Tesla", "Model S", 2024)

# Using Attributes
print(f"My car: {my_car.brand} {my_car.model}")
print(f"Dream car: {dream_car.brand} {dream_car.model}")

# Using Methods
my_car.start_engine()
my_car.drive()
my_car.stop_engine()

# Each object has its own state
print(f"Is my_car running? {my_car.is_running}")
print(f"Is dream_car running? {dream_car.is_running}")


# -----------------------------------------------------------------------------
# 2. Class vs Instance Attributes
# -----------------------------------------------------------------------------
print("\n--- 2. Class vs Instance Attributes ---")

class Robot:
    population = 0  # Class Attribute (shared by all instances)

    def __init__(self, name):
        self.name = name  # Instance Attribute (unique to each instance)
        Robot.population += 1
        print(f"{self.name} has been created!")

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

droid1 = Robot("R2-D2")
droid2 = Robot("C-3PO")

print(f"Current robot population: {Robot.population}")

droid1.die()
print(f"Current robot population: {Robot.population}")
