# 👨‍👦 Inheritance

Inheritance allows a class (the **child** or **derived** class) to inherit attributes and methods from another class (the **parent** or **base** class).

This promotes code **reusability**. Instead of rewriting logic, you extend it!

## 🧬 Basic Inheritance

To inherit from a class, you put the parent class name in parentheses when defining the child class.

```python
class Animal:
    def eat(self):
        print("Munch munch...")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Woof!")

d = Dog()
d.eat()   # Inherited from Animal!
d.bark()  # Defined in Dog
```

## 🦸 The `super()` Function

When you want to use the parent's method but also add something extra, you use `super()`. This is very common in the `__init__` method.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent's __init__ to handle the name
        super().__init__(name)
        self.breed = breed
```

## 🔄 Overriding Methods

A child class can provide a different implementation for a method that is already defined in its parent class. This is called **method overriding**.

```python
class Cat(Animal):
    def eat(self):
        print("The cat eats gracefully.")

c = Cat("Whiskers")
c.eat() # Output: The cat eats gracefully.
```

## 🌳 Multi-level Inheritance

You can inherit from a class that inherits from another class.

`Animal` -> `Mammal` -> `Dog`

## 🕸️ Multiple Inheritance

Python supports inheriting from multiple classes at once (less common, can be complex).

```python
class FlyingCar(Car, Airplane):
    pass
```

## 🔑 Key Takeaways

1. **Inheritance**: Creates a hierarchy (Parent -> Child).
2. **Reusability**: Child classes get parent features for free.
3. **`super()`**: Access parent methods.
4. **Overriding**: Change inherited behavior in the child class.
5. **`isinstance(obj, Class)`**: Check if an object belongs to a class or its parents.

---

[Next: Polymorphism](../04_polymorphism/README.md)
