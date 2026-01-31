"""
06_composition_vs_inheritance/exercises.py

Practice Composition!
"""

# -----------------------------------------------------------------------------
# Exercise 1: Computer Assembly
# -----------------------------------------------------------------------------
# 1. Create a class `CPU` with a method `process()`.
# 2. Create a class `RAM` with a method `load()`.
# 3. Create a class `Computer` that:
#    - Accepts `cpu` and `ram` objects in its `__init__`.
#    - Has a `start()` method that calls `ram.load()` and `cpu.process()`.
# 4. Assemble a computer and start it.

class CPU:
    def process(self):
        print("CPU processing instructions...")

class RAM:
    def load(self):
        print("RAM loading data...")

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def start(self):
        self.ram.load()
        self.cpu.process()

# Tests
print("\n--- Exercise 1 Output ---")

computer = Computer(CPU(), RAM())
computer.start()


# -----------------------------------------------------------------------------
# Exercise 2: Car and Engine
# -----------------------------------------------------------------------------
# 1. Create a class `ElectricEngine` with `start()` ("Silent start").
# 2. Create a class `V8Engine` with `start()` ("Vroom Vroom").
# 3. Create a class `Car` that takes an `engine` in `__init__`.
# 4. Add a `drive()` method to `Car` that first starts the engine, then drives.
# 5. Create two cars with different engines and drive them.

class ElectricEngine:
    def start(self):
        print("Silent start.")

class V8Engine:
    def start(self):
        print("Vroom vroom.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is driving...")

# Tests
print("\n--- Exercise 2 Output ---")

eco_car = Car(ElectricEngine())
muscle_car = Car(V8Engine())

eco_car.drive()
muscle_car.drive()
