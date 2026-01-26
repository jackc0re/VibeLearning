"""
Beginner Exercise 3: Loops
===========================
Practice iteration with for and while loops.
"""

print("=" * 50)
print("EXERCISE 3: Loops")
print("=" * 50)


# =============================================================================
# EXERCISE 3.1: Sum of Squares
# =============================================================================
print("\n--- Exercise 3.1: Sum of Squares ---")
"""
Calculate the sum of squares from 1 to n.
Example: n=3 -> 1² + 2² + 3² = 1 + 4 + 9 = 14
"""

n = 10

# Your code below:
sum_of_squares = None  # Calculate sum of squares from 1 to n
if sum_of_squares is not None:
    print(f"Sum of squares from 1 to {n}: {sum_of_squares}")


# =============================================================================
# EXERCISE 3.2: Find Factor
# =============================================================================
print("\n--- Exercise 3.2: Find Factor ---")
"""
Find all factors of a given number.
Example: n=12 -> [1, 2, 3, 4, 6, 12]
"""

number = 24

# Your code below:
factors = None  # List of all factors
if factors is not None:
    print(f"Factors of {number}: {factors}")


# =============================================================================
# EXERCISE 3.3: Fibonacci Sequence
# =============================================================================
print("\n--- Exercise 3.3: Fibonacci Sequence ---")
"""
Generate the first n numbers in the Fibonacci sequence.
Each number is the sum of the two preceding ones.
Example: n=8 -> [0, 1, 1, 2, 3, 5, 8, 13]
"""

n = 10

# Your code below:
fibonacci = None  # Generate first n Fibonacci numbers
if fibonacci is not None:
    print(f"First {n} Fibonacci numbers: {fibonacci}")


# =============================================================================
# EXERCISE 3.4: Reverse a String
# =============================================================================
print("\n--- Exercise 3.4: Reverse a String ---")
"""
Reverse a string using a loop (not [::-1] or reversed()).
"""

text = "Hello, World!"

# Your code below:
reversed_text = None  # Reverse the string using a loop
print(f"Original: {text}")
if reversed_text is not None:
    print(f"Reversed: {reversed_text}")


# =============================================================================
# EXERCISE 3.5: Count Characters
# =============================================================================
print("\n--- Exercise 3.5: Count Characters ---")
"""
Count the occurrences of each character in a string.
Ignore spaces and case.
"""

text = "Hello World"

# Your code below:
char_counts = {}  # Dictionary of character counts
print(f"Character counts in '{text}':")
for char, count in sorted(char_counts.items()):
    print(f"  '{char}': {count}")


# =============================================================================
# EXERCISE 3.6: Multiplication Table
# =============================================================================
print("\n--- Exercise 3.6: Multiplication Table ---")
"""
Print a multiplication table from 1 to n.
"""

n = 5

# Your code below:
# Print multiplication table
print("   ", end="")
for i in range(1, n + 1):
    print(f"{i:4}", end="")
print()
print("   " + "----" * n)
for i in range(1, n + 1):
    print(f"{i} |", end="")
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()


# =============================================================================
# EXERCISE 3.7: Find First Duplicate
# =============================================================================
print("\n--- Exercise 3.7: Find First Duplicate ---")
"""
Find the first duplicate element in a list.
Return the element if found, None otherwise.
Use a loop and break when found.
"""

numbers = [1, 2, 3, 4, 2, 5, 6, 3]

# Your code below:
first_duplicate = None  # Find first duplicate
print(f"List: {numbers}")
print(f"First duplicate: {first_duplicate}")


# =============================================================================
# EXERCISE 3.8: Filter Even Numbers
# =============================================================================
print("\n--- Exercise 3.8: Filter Even Numbers ---")
"""
Create a new list containing only even numbers from the original.
Use list comprehension.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Your code below:
evens = None  # Filter even numbers using list comprehension
print(f"Original: {numbers}")
if evens is not None:
    print(f"Evens: {evens}")


# =============================================================================
# EXERCISE 3.9: Guess the Number (Simulated)
# =============================================================================
print("\n--- Exercise 3.9: Guess the Number ---")
"""
Simulate a number guessing game.
Target is between 1 and 100.
Track guesses and count attempts.
Return "won" or "lost" after max attempts.
"""

target = 42
guesses = [50, 25, 35, 40, 42]
max_attempts = 5

# Your code below:
result = None  # "won" or "lost"
attempts = None  # Number of attempts made
print(f"Target: {target}")
print(f"Guesses: {guesses}")
if result is not None and attempts is not None:
    print(f"Result: {result} after {attempts} attempts")


# =============================================================================
# EXERCISE 3.10: Prime Numbers in Range
# =============================================================================
print("\n--- Exercise 3.10: Prime Numbers in Range ---")
"""
Find all prime numbers in a given range.
"""

start = 10
end = 30

# Your code below:
primes = None  # List of prime numbers in range
if primes is not None:
    print(f"Primes between {start} and {end}: {primes}")


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 3.1
print("\n--- Solution 3.1 ---")
n = 10
sum_of_squares = 0
for i in range(1, n + 1):
    sum_of_squares += i**2
print(f"Sum of squares from 1 to {n}: {sum_of_squares}")

# SOLUTION 3.2
print("\n--- Solution 3.2 ---")
number = 24
factors = []
for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)
print(f"Factors of {number}: {factors}")

# SOLUTION 3.3
print("\n--- Solution 3.3 ---")
n = 10
fibonacci = []
for i in range(n):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
print(f"First {n} Fibonacci numbers: {fibonacci}")

# SOLUTION 3.4
print("\n--- Solution 3.4 ---")
text = "Hello, World!"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")

# SOLUTION 3.5
print("\n--- Solution 3.5 ---")
text = "Hello World"
char_counts = {}
for char in text.lower():
    if char != " ":
        char_counts[char] = char_counts.get(char, 0) + 1
print(f"Character counts in '{text}':")
for char, count in sorted(char_counts.items()):
    print(f"  '{char}': {count}")

# SOLUTION 3.6
print("\n--- Solution 3.6 ---")
n = 5
print("   ", end="")
for i in range(1, n + 1):
    print(f"{i:4}", end="")
print()
print("   " + "----" * n)
for i in range(1, n + 1):
    print(f"{i} |", end="")
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()

# SOLUTION 3.7
print("\n--- Solution 3.7 ---")
numbers = [1, 2, 3, 4, 2, 5, 6, 3]
seen = set()
first_duplicate = None
for num in numbers:
    if num in seen:
        first_duplicate = num
        break
    seen.add(num)
print(f"List: {numbers}")
print(f"First duplicate: {first_duplicate}")

# SOLUTION 3.8
print("\n--- Solution 3.8 ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print(f"Original: {numbers}")
print(f"Evens: {evens}")

# SOLUTION 3.9
print("\n--- Solution 3.9 ---")
target = 42
guesses = [50, 25, 35, 40, 42]
max_attempts = 5

result = "lost"
attempts = 0
for i, guess in enumerate(guesses):
    attempts = i + 1
    if guess == target:
        result = "won"
        break
    if attempts >= max_attempts:
        break

print(f"Target: {target}")
print(f"Guesses: {guesses}")
print(f"Result: {result} after {attempts} attempts")

# SOLUTION 3.10
print("\n--- Solution 3.10 ---")
start = 10
end = 30
primes = []
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
print(f"Primes between {start} and {end}: {primes}")

print("\n" + "=" * 50)
print("Great job! Move on to 04_functions.py")
print("=" * 50)
