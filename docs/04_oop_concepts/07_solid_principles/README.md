# 🏗️ SOLID Principles

SOLID is an acronym for five design principles intended to make software designs more understandable, flexible, and maintainable.

## 1. Single Responsibility Principle (SRP)
> "A class should have only one reason to change."

Each class should focus on **one single job**.
- **Bad**: `User` class handles database saving, email sending, AND logic.
- **Good**: `User` class handles logic. `UserRepository` handles database. `EmailService` handles email.

## 2. Open/Closed Principle (OCP)
> "Software entities should be open for extension, but closed for modification."

You should be able to add new functionality without changing existing code.
- **How**: Use inheritance or interfaces (Polymorphism).

## 3. Liskov Substitution Principle (LSP)
> "Objects of a superclass shall be replaceable with objects of its subclasses without breaking the application."

If `Dog` is a subclass of `Animal`, you should be able to plug `Dog` in anywhere `Animal` is used, and it should just work.

## 4. Interface Segregation Principle (ISP)
> "Clients should not be forced to depend upon interfaces that they do not use."

Don't create massive "God Interfaces". Break them down into smaller, specific ones.
- **Bad**: `ISmartDevice` with `print`, `scan`, `fax`. (A printer doesn't need to fax).
- **Good**: `IPrinter`, `IScanner`, `IFax`.

## 5. Dependency Inversion Principle (DIP)
> "Depend upon abstractions, not concretions."

High-level modules (logic) should not depend on low-level modules (database/API). Both should depend on abstractions (interfaces).
- **How**: Dependency Injection.

---

[Return to Module Overview](../README.md)
