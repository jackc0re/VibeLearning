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
    # TODO: Implement this class
    pass

class RAM:
    # TODO: Implement this class
    pass

class Computer:
    # TODO: Implement this class
    pass

# TODO: Test your code
print("\n--- Exercise 1 Output ---")


# -----------------------------------------------------------------------------
# Exercise 2: Car and Engine
# -----------------------------------------------------------------------------
# 1. Create a class `ElectricEngine` with `start()` ("Silent start").
# 2. Create a class `V8Engine` with `start()` ("Vroom Vroom").
# 3. Create a class `Car` that takes an `engine` in `__init__`.
# 4. Add a `drive()` method to `Car` that first starts the engine, then drives.
# 5. Create two cars with different engines and drive them.

class ElectricEngine:
    # TODO: Implement this class
    pass

class V8Engine:
    # TODO: Implement this class
    pass

class Car:
    # TODO: Implement this class
    pass

# TODO: Test your code
print("\n--- Exercise 2 Output ---")
