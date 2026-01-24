"""
Beginner Exercise 4: Functions
===============================
Practice writing and using functions.
"""

print("=" * 50)
print("EXERCISE 4: Functions")
print("=" * 50)


# =============================================================================
# EXERCISE 4.1: Basic Function
# =============================================================================
print("\n--- Exercise 4.1: Basic Function ---")
"""
Write a function called greet that takes a name and returns a greeting.
Default name should be "World".
"""

# Your code below:
def greet(name="World"):
    """Return a greeting message."""
    pass

print(greet())
print(greet("Alice"))


# =============================================================================
# EXERCISE 4.2: Multiple Parameters
# =============================================================================
print("\n--- Exercise 4.2: Multiple Parameters ---")
"""
Write a function called calculate_total that takes:
- price (float)
- quantity (int)
- tax_rate (float, default 0.1)
- discount (float, default 0)

Returns the total price after tax and discount.
"""

# Your code below:
def calculate_total(price, quantity, tax_rate=0.1, discount=0):
    """Calculate total price with tax and discount."""
    pass

print(f"Total: ${calculate_total(10.0, 2):.2f}")
print(f"Total with discount: ${calculate_total(10.0, 2, discount=0.1):.2f}")


# =============================================================================
# EXERCISE 4.3: Return Multiple Values
# =============================================================================
print("\n--- Exercise 4.3: Return Multiple Values ---")
"""
Write a function called get_min_max that takes a list of numbers
and returns both the minimum and maximum values.
"""

# Your code below:
def get_min_max(numbers):
    """Return the minimum and maximum from a list."""
    pass

nums = [4, 2, 9, 1, 7, 5]
minimum, maximum = get_min_max(nums)
print(f"List: {nums}")
print(f"Min: {minimum}, Max: {maximum}")


# =============================================================================
# EXERCISE 4.4: Recursive Function
# =============================================================================
print("\n--- Exercise 4.4: Recursive Function ---")
"""
Write a recursive function called factorial that calculates n!.
"""

# Your code below:
def factorial(n):
    """Calculate factorial of n recursively."""
    pass

print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")


# =============================================================================
# EXERCISE 4.5: Lambda Functions
# =============================================================================
print("\n--- Exercise 4.5: Lambda Functions ---")
"""
Create lambda functions for:
1. square: squares a number
2. add: adds two numbers
3. is_even: returns True if number is even
"""

# Your code below:
square =  # Lambda to square a number
add =  # Lambda to add two numbers
is_even =  # Lambda to check if even

print(f"square(5) = {square(5)}")
print(f"add(3, 4) = {add(3, 4)}")
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(7) = {is_even(7)}")


# =============================================================================
# EXERCISE 4.6: Function with Variable Arguments
# =============================================================================
print("\n--- Exercise 4.6: Variable Arguments ---")
"""
Write a function called calculate_average that takes any number of
arguments and returns their average.
"""

# Your code below:
def calculate_average(*args):
    """Calculate average of all arguments."""
    pass

print(f"Average: {calculate_average(1, 2, 3, 4, 5)}")
print(f"Average: {calculate_average(10, 20, 30)}")


# =============================================================================
# EXERCISE 4.7: Function with Keyword Arguments
# =============================================================================
print("\n--- Exercise 4.7: Keyword Arguments ---")
"""
Write a function called create_profile that accepts keyword arguments
for name, age, and city. Returns a formatted profile string.
"""

# Your code below:
def create_profile(**kwargs):
    """Create a profile from keyword arguments."""
    pass

print(create_profile(name="Alice", age=25, city="NYC"))
print(create_profile(name="Bob", city="LA"))


# =============================================================================
# EXERCISE 4.8: Higher-Order Function
# =============================================================================
print("\n--- Exercise 4.8: Higher-Order Function ---")
"""
Write a function called apply_operation that takes:
- A list of numbers
- A function that operates on each number

Returns a new list with the operation applied.
"""

# Your code below:
def apply_operation(numbers, operation):
    """Apply operation to each number in the list."""
    pass

nums = [1, 2, 3, 4, 5]
print(f"Original: {nums}")
print(f"Squared: {apply_operation(nums, lambda x: x ** 2)}")
print(f"Doubled: {apply_operation(nums, lambda x: x * 2)}")


# =============================================================================
# EXERCISE 4.9: Function Scope
# =============================================================================
print("\n--- Exercise 4.9: Function Scope ---")
"""
Complete the function to demonstrate variable scope.
Track how many times the function is called using a nonlocal variable.
"""

call_counter = 0

# Your code below:
def count_calls():
    """Count how many times this function is called."""
    # Use nonlocal to modify call_counter
    pass

for _ in range(5):
    count_calls()
print(f"Function called {call_counter} times")


# =============================================================================
# EXERCISE 4.10: Default Mutable Arguments (Tricky!)
# =============================================================================
print("\n--- Exercise 4.10: Default Mutable Arguments ---")
"""
Fix the function to avoid the mutable default argument pitfall.
The function should add items to a list, but each call should
start with an empty list by default.
"""

# Bug: Don't do this in production!
def buggy_add_item(item, items=[]):
    items.append(item)
    return items

# Your code below - write the fixed version:
def add_item(item, items=None):
    """Add item to list, starting with empty list by default."""
    pass

print("Buggy version:")
print(buggy_add_item(1))
print(buggy_add_item(2))

print("\nFixed version:")
print(add_item(1))
print(add_item(2))


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 4.1
print("\n--- Solution 4.1 ---")
def greet(name="World"):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))

# SOLUTION 4.2
print("\n--- Solution 4.2 ---")
def calculate_total(price, quantity, tax_rate=0.1, discount=0):
    """Calculate total price with tax and discount."""
    subtotal = price * quantity
    discounted = subtotal * (1 - discount)
    total = discounted * (1 + tax_rate)
    return total

print(f"Total: ${calculate_total(10.0, 2):.2f}")
print(f"Total with discount: ${calculate_total(10.0, 2, discount=0.1):.2f}")

# SOLUTION 4.3
print("\n--- Solution 4.3 ---")
def get_min_max(numbers):
    """Return the minimum and maximum from a list."""
    return min(numbers), max(numbers)

nums = [4, 2, 9, 1, 7, 5]
minimum, maximum = get_min_max(nums)
print(f"List: {nums}")
print(f"Min: {minimum}, Max: {maximum}")

# SOLUTION 4.4
print("\n--- Solution 4.4 ---")
def factorial(n):
    """Calculate factorial of n recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")

# SOLUTION 4.5
print("\n--- Solution 4.5 ---")
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

print(f"square(5) = {square(5)}")
print(f"add(3, 4) = {add(3, 4)}")
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(7) = {is_even(7)}")

# SOLUTION 4.6
print("\n--- Solution 4.6 ---")
def calculate_average(*args):
    """Calculate average of all arguments."""
    if not args:
        return 0
    return sum(args) / len(args)

print(f"Average: {calculate_average(1, 2, 3, 4, 5)}")
print(f"Average: {calculate_average(10, 20, 30)}")

# SOLUTION 4.7
print("\n--- Solution 4.7 ---")
def create_profile(**kwargs):
    """Create a profile from keyword arguments."""
    parts = []
    for key, value in kwargs.items():
        parts.append(f"{key}: {value}")
    return " | ".join(parts)

print(create_profile(name="Alice", age=25, city="NYC"))
print(create_profile(name="Bob", city="LA"))

# SOLUTION 4.8
print("\n--- Solution 4.8 ---")
def apply_operation(numbers, operation):
    """Apply operation to each number in the list."""
    return [operation(num) for num in numbers]

nums = [1, 2, 3, 4, 5]
print(f"Original: {nums}")
print(f"Squared: {apply_operation(nums, lambda x: x ** 2)}")
print(f"Doubled: {apply_operation(nums, lambda x: x * 2)}")

# SOLUTION 4.9
print("\n--- Solution 4.9 ---")
call_counter = 0

def count_calls():
    """Count how many times this function is called."""
    nonlocal call_counter
    call_counter += 1

for _ in range(5):
    count_calls()
print(f"Function called {call_counter} times")

# SOLUTION 4.10
print("\n--- Solution 4.10 ---")
def buggy_add_item(item, items=[]):
    items.append(item)
    return items

def add_item(item, items=None):
    """Add item to list, starting with empty list by default."""
    if items is None:
        items = []
    items.append(item)
    return items

print("Buggy version:")
print(buggy_add_item(1))
print(buggy_add_item(2))

print("\nFixed version:")
print(add_item(1))
print(add_item(2))

print("\n" + "=" * 50)
print("Great job! Move on to 05_lists.py")
print("=" * 50)
