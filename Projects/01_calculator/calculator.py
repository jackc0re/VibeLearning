"""
Calculator Project
==================
A command-line calculator with basic operations and history tracking.
"""

import math


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers with zero-division check."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b."""
    return math.pow(a, b)


def modulo(a, b):
    """Calculate the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b


def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_choice(min_choice, max_choice):
    """Get a valid menu choice from user input."""
    while True:
        try:
            choice = int(input(f"Enter your choice ({min_choice}-{max_choice}): "))
            if min_choice <= choice <= max_choice:
                return choice
            print(f"Please enter a number between {min_choice} and {max_choice}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_menu():
    """Display the main calculator menu."""
    print("\n" + "=" * 40)
    print("           CALCULATOR MENU")
    print("=" * 40)
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Modulo (%)")
    print("7. Show History")
    print("8. Clear History")
    print("9. Exit")
    print("=" * 40)


def add_to_history(history, operation, num1, num2, result):
    """Add a calculation to the history list."""
    formatted_num1 = int(num1) if num1 == int(num1) else num1
    formatted_num2 = int(num2) if num2 == int(num2) else num2
    formatted_result = int(result) if result == int(result) else result
    
    history.append(f"{formatted_num1} {operation} {formatted_num2} = {formatted_result}")


def show_history(history):
    """Display the calculation history."""
    if not history:
        print("\nNo calculations performed yet.")
    else:
        print("\n" + "=" * 40)
        print("           CALCULATION HISTORY")
        print("=" * 40)
        for i, calc in enumerate(history, 1):
            print(f"{i:2d}. {calc}")
        print("=" * 40)


def perform_operation(choice):
    """Perform the selected operation and return details."""
    operations = {
        1: ("+", add),
        2: ("-", subtract),
        3: ("*", multiply),
        4: ("/", divide),
        5: ("^", power),
        6: ("%", modulo)
    }
    
    symbol, operation = operations[choice]
    
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    
    try:
        result = operation(num1, num2)
        return symbol, num1, num2, result
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    """Main calculator program."""
    history = []
    
    print("=" * 40)
    print("       WELCOME TO CALCULATOR")
    print("=" * 40)
    print("Enter \"clear\" to clear history at any time")
    print("=" * 40)
    
    while True:
        display_menu()
        choice = get_choice(1, 9)
        
        if choice in [1, 2, 3, 4, 5, 6]:
            result = perform_operation(choice)
            if result:
                symbol, num1, num2, calc_result = result
                
                formatted_num1 = int(num1) if num1 == int(num1) else num1
                formatted_num2 = int(num2) if num2 == int(num2) else num2
                formatted_result = int(calc_result) if calc_result == int(calc_result) else calc_result
                
                print(f"\n{formatted_num1} {symbol} {formatted_num2} = {formatted_result}")
                add_to_history(history, symbol, num1, num2, calc_result)
        
        elif choice == 7:
            show_history(history)
        
        elif choice == 8:
            history.clear()
            print("\nHistory cleared!")
        
        elif choice == 9:
            if history:
                print("\nThank you for using the Calculator!")
                print(f"Total calculations performed: {len(history)}")
            else:
                print("\nThank you for using the Calculator!")
            break


if __name__ == "__main__":
    main()