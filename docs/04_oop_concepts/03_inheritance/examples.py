"""
03_inheritance/examples.py

Demonstrating inheritance and super().
"""

# -----------------------------------------------------------------------------
# 1. Basic Inheritance
# -----------------------------------------------------------------------------
print("\n--- 1. Basic Inheritance ---")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} engine started.")

    def stop(self):
        print(f"{self.brand} engine stopped.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving on the road.")

class Boat(Vehicle):
    def sail(self):
        print("Boat is sailing on the water.")

# Creating objects
my_car = Car("Toyota")
my_boat = Boat("Yamaha")

# Using inherited methods
my_car.start() # output: Toyota engine started.
my_car.drive() # output: Car is driving on the road.
my_car.stop()  # output: Toyota engine stopped.

my_boat.start() # output: Yamaha engine started.
my_boat.sail()  # output: Boat is sailing on the water.
# my_boat.drive() # Error! Boat doesn't have drive()


# -----------------------------------------------------------------------------
# 2. Using super() and Method Overriding
# -----------------------------------------------------------------------------
print("\n--- 2. super() and Overriding ---")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working..."

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Use super() to initialize parent attributes
        super().__init__(name, salary)
        self.programming_language = programming_language

    # Overriding the work method
    def work(self):
        # We can also call the parent's work method using super()
        base_work = super().work()
        return f"{base_work} writing code in {self.programming_language}!"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        return f"{self.name} is managing a team of {self.team_size} people."

dev = Developer("Alice", 90000, "Python")
mgr = Manager("Bob", 110000, 5)

print(dev.work()) # Output: Alice is working... writing code in Python!
print(mgr.work()) # Output: Bob is managing a team of 5 people.

# -----------------------------------------------------------------------------
# 3. isinstance() and issubclass()
# -----------------------------------------------------------------------------
print("\n--- 3. Type Checking ---")

print(f"Is dev a Developer? {isinstance(dev, Developer)}") # True
print(f"Is dev an Employee? {isinstance(dev, Employee)}")   # True (Inherited)
print(f"Is dev a Manager? {isinstance(dev, Manager)}")     # False

print(f"Is Developer a subclass of Employee? {issubclass(Developer, Employee)}") # True
print(f"Is Employee a subclass of Developer? {issubclass(Employee, Developer)}") # False
