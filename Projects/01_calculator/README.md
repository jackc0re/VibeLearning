# 🧮 Project 1: Calculator

Build a command-line calculator that performs basic arithmetic operations and keeps track of calculation history.

---

## 📋 Project Overview

This project helps you practice:
- Functions and control flow
- Input validation
- Error handling
- User interaction

### Features to Build

1. ✅ Basic Operations
   - Addition
   - Subtraction
   - Multiplication
   - Division (with zero-division check)

2. ✅ History Tracking
   - Store past calculations
   - Display history
   - Clear history option

3. ✅ User Interface
   - Menu-driven interface
   - Clear prompts and feedback
   - Easy to use

---

## 💻 Requirements

### Prerequisites

Complete these modules before starting:
- [00_getting_started](../../00_getting_started/README.md)
- [01_foundations](../../01_foundations/README.md)

### Skills You'll Use

- **Functions** — Write reusable code for operations
- **Control flow** — Handle user choices with if/elif/else
- **Error handling** — Use try/except for invalid input
- **Lists** — Store calculation history
- **Loops** — Main program loop

---

## 🚀 Development Steps

### Step 1: Setup (5 minutes)

Create a new file `calculator.py` and add the main function:

```python
def main():
    print("Welcome to the Calculator!")
    print("--------------------------")


if __name__ == "__main__":
    main()
```

Run it to ensure it works.

### Step 2: Basic Operations (20 minutes)

Create functions for each operation:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Test each function with sample inputs.

### Step 3: Input Validation (15 minutes)

Create a function to get valid numbers:

```python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
```

### Step 4: History System (15 minutes)

Store calculations in a list:

```python
history = []

def add_to_history(operation, num1, num2, result):
    history.append(f"{num1} {operation} {num2} = {result}")

def show_history():
    if not history:
        print("No calculations performed yet.")
    else:
        for i, calc in enumerate(history, 1):
            print(f"{i}. {calc}")
```

### Step 5: User Interface (20 minutes)

Create the main menu:

```python
def display_menu():
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Clear History")
    print("7. Exit")

def get_choice():
    while True:
        try:
            choice = int(input("\nEnter your choice (1-7): "))
            if 1 <= choice <= 7:
                return choice
            print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")
```

### Step 6: Main Loop (15 minutes)

Put it all together:

```python
def main():
    history = []
    
    print("Welcome to the Calculator!")
    print("--------------------------")
    
    while True:
        display_menu()
        choice = get_choice()
        
        if choice == 1:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            result = add(num1, num2)
            print(f"Result: {result}")
            add_to_history("+", num1, num2, result)
        
        elif choice == 2:
            # Implement subtraction
            pass
        
        elif choice == 3:
            # Implement multiplication
            pass
        
        elif choice == 4:
            # Implement division
            pass
        
        elif choice == 5:
            show_history()
        
        elif choice == 6:
            history.clear()
            print("History cleared!")
        
        elif choice == 7:
            print("Thank you for using the Calculator!")
            break
```

---

## 🧪 Testing

Test your calculator with these scenarios:

1. **Basic Operations**
   - 5 + 3 = 8
   - 10 - 4 = 6
   - 6 * 7 = 42
   - 15 / 3 = 5
   - 15 / 0 = Error message

2. **Invalid Input**
   - Enter "abc" instead of a number
   - Enter a menu choice outside 1-7

3. **History**
   - Perform several operations
   - View history
   - Clear history
   - View history again (should be empty)

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How to write and use functions with parameters
- ✅ How to handle user input and validate it
- ✅ How to use try/except blocks for error handling
- ✅ How to store and display data with lists
- ✅ How to create a menu-driven interface
- ✅ How to structure a program with multiple functions

---

## 🏆 Challenges

Complete these challenges to enhance your calculator:

1. **Advanced Operations** — Add exponentiation, modulo, and power operations
2. **Scientific Mode** — Add trigonometric functions (sin, cos, tan)
3. **Save History** — Save history to a file and load it on startup
4. **Memory Feature** — Store a value in memory and recall it later
5. **Color Output** — Add colored text for better UX (using colorama library)
6. **History Search** — Allow searching history for specific calculations

See [challenges.md](challenges.md) for detailed instructions.

---

## 📁 File Structure

```
01_calculator/
├── README.md          # This file
├── calculator.py      # Your main implementation
└── challenges.md      # Additional challenge tasks
```

---

**Ready to start?** Create `calculator.py` and begin building! 🚀