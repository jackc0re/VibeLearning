"""
Functions Basics - Exercises
============================
Practice creating and using functions!
"""

print("=" * 50)
print("FUNCTIONS BASICS - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: Temperature Converter
# =============================================================================
print("\n--- Exercise 1: Temperature Converter ---\n")
"""
Create two functions:
1. celsius_to_fahrenheit(celsius) - returns fahrenheit
2. fahrenheit_to_celsius(fahrenheit) - returns celsius

Formulas:
- F = C * 9/5 + 32
- C = (F - 32) * 5/9

Test with: 0°C, 100°C, 32°F, 212°F
"""

# Your code here:


# =============================================================================
# EXERCISE 2: Is Prime
# =============================================================================
print("\n--- Exercise 2: Is Prime ---\n")
"""
Create a function is_prime(n) that returns True if n is prime, False otherwise.
A prime number is only divisible by 1 and itself.

Test with: 2, 3, 4, 17, 20, 97
"""

# Your code here:


# =============================================================================
# EXERCISE 3: Word Counter
# =============================================================================
print("\n--- Exercise 3: Word Counter ---\n")
"""
Create a function count_words(text) that returns the number of words.
Words are separated by spaces.

Test with: "Hello World", "The quick brown fox", ""
"""

# Your code here:


# =============================================================================
# EXERCISE 4: Shopping Cart
# =============================================================================
print("\n--- Exercise 4: Shopping Cart ---\n")
"""
Create a function calculate_total(*prices, tax_rate=0.08) that:
- Takes any number of prices
- Applies tax (default 8%)
- Returns the total

Test with various prices and tax rates.
"""

# Your code here:


# =============================================================================
# EXERCISE 5: Build a User Profile
# =============================================================================
print("\n--- Exercise 5: User Profile ---\n")
"""
Create a function build_profile(first, last, **user_info) that:
- Takes required first and last name
- Takes any additional info as keyword arguments
- Returns a dictionary with all the info

Example:
build_profile("Albert", "Einstein", location="Princeton", field="Physics")
Should return: {'first': 'Albert', 'last': 'Einstein', 'location': 'Princeton', 'field': 'Physics'}
"""

# Your code here:


# =============================================================================
# EXERCISE 6: List Operations
# =============================================================================
print("\n--- Exercise 6: List Operations ---\n")
"""
Create functions that take a list and return:
1. get_sum(numbers) - sum of all numbers
2. get_average(numbers) - average
3. get_stats(numbers) - tuple of (min, max, sum, average)

All should handle empty lists gracefully.
"""

# Your code here:


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

print(f"0°C = {celsius_to_fahrenheit(0):.1f}°F")
print(f"100°C = {celsius_to_fahrenheit(100):.1f}°F")
print(f"32°F = {fahrenheit_to_celsius(32):.1f}°C")
print(f"212°F = {fahrenheit_to_celsius(212):.1f}°C")

# SOLUTION 2
print("\n--- Solution 2 ---")

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in [2, 3, 4, 17, 20, 97]:
    print(f"{num} is prime: {is_prime(num)}")

# SOLUTION 3
print("\n--- Solution 3 ---")

def count_words(text):
    """Count words in a text."""
    if not text.strip():
        return 0
    return len(text.split())

print(f"'Hello World' has {count_words('Hello World')} words")
print(f"'The quick brown fox' has {count_words('The quick brown fox')} words")
print(f"'' (empty) has {count_words('')} words")

# SOLUTION 4
print("\n--- Solution 4 ---")

def calculate_total(*prices, tax_rate=0.08):
    """Calculate total with tax."""
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    return subtotal + tax

print(f"Items: $10, $20, $30")
print(f"Total (8% tax): ${calculate_total(10, 20, 30):.2f}")
print(f"Total (10% tax): ${calculate_total(10, 20, 30, tax_rate=0.10):.2f}")

# SOLUTION 5
print("\n--- Solution 5 ---")

def build_profile(first, last, **user_info):
    """Build a user profile dictionary."""
    profile = {'first': first, 'last': last}
    profile.update(user_info)
    return profile

user1 = build_profile("Albert", "Einstein", location="Princeton", field="Physics")
print(f"User 1: {user1}")

user2 = build_profile("Ada", "Lovelace", title="Countess", skill="Mathematics")
print(f"User 2: {user2}")

# SOLUTION 6
print("\n--- Solution 6 ---")

def get_sum(numbers):
    """Return sum of numbers."""
    if not numbers:
        return 0
    return sum(numbers)

def get_average(numbers):
    """Return average of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def get_stats(numbers):
    """Return (min, max, sum, average) tuple."""
    if not numbers:
        return (0, 0, 0, 0)
    return (min(numbers), max(numbers), sum(numbers), sum(numbers) / len(numbers))

nums = [10, 20, 30, 40, 50]
print(f"Numbers: {nums}")
print(f"Sum: {get_sum(nums)}")
print(f"Average: {get_average(nums)}")
print(f"Stats (min, max, sum, avg): {get_stats(nums)}")

print(f"\nEmpty list stats: {get_stats([])}")

print("\n" + "=" * 50)
print("Great job! Move on to 06_input_output next.")
print("=" * 50)
