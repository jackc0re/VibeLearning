"""
Loops - Exercises
=================
Practice repetition and iteration!
"""

print("=" * 50)
print("LOOPS - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: Sum of Numbers
# =============================================================================
print("\n--- Exercise 1: Sum of Numbers ---\n")
"""
Calculate the sum of numbers from 1 to 100 using a for loop.
Print the result.
"""

# Your code here:


# =============================================================================
# EXERCISE 2: Factorial
# =============================================================================
print("\n--- Exercise 2: Factorial ---\n")
"""
Calculate the factorial of 5 (5! = 5 × 4 × 3 × 2 × 1 = 120)
Use a for loop.
"""

n = 5

# Your code here:


# =============================================================================
# EXERCISE 3: Countdown Timer
# =============================================================================
print("\n--- Exercise 3: Countdown ---\n")
"""
Create a countdown from 10 to 1, then print "Blast off!"
Use a while loop.
"""

# Your code here:


# =============================================================================
# EXERCISE 4: Find the First Vowel
# =============================================================================
print("\n--- Exercise 4: First Vowel ---\n")
"""
Given a word, find and print the first vowel and its position.
Use break to exit once found.
Vowels are: a, e, i, o, u
"""

word = "python"

# Your code here:


# =============================================================================
# EXERCISE 5: Skip Negative Numbers
# =============================================================================
print("\n--- Exercise 5: Skip Negatives ---\n")
"""
Given a list of numbers, calculate the sum of only positive numbers.
Use continue to skip negative numbers.
"""

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

# Your code here:


# =============================================================================
# EXERCISE 6: Multiplication Table
# =============================================================================
print("\n--- Exercise 6: Multiplication Table ---\n")
"""
Print a multiplication table for numbers 1-5.
Format it nicely!
"""

# Your code here:


# =============================================================================
# EXERCISE 7: Password Attempts
# =============================================================================
print("\n--- Exercise 7: Password (Simulated) ---\n")
"""
Simulate 3 password attempts.
Correct password is "secret"
After 3 wrong attempts, print "Account locked"
If correct, print "Welcome!"
(We'll use a list to simulate user input)
"""

attempts = ["wrong1", "wrong2", "secret"]  # Simulated inputs

# Your code here:


# =============================================================================
# EXERCISE 8: Prime Numbers
# =============================================================================
print("\n--- Exercise 8: Prime Numbers ---\n")
"""
Print all prime numbers between 2 and 30.
A prime number is only divisible by 1 and itself.
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
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100: {total}")

# Formula: n(n+1)/2 = 100*101/2 = 5050

# SOLUTION 2
print("\n--- Solution 2 ---")
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# SOLUTION 3
print("\n--- Solution 3 ---")
count = 10
while count > 0:
    print(count, end=" ")
    count -= 1
print("\nBlast off! 🚀")

# SOLUTION 4
print("\n--- Solution 4 ---")
word = "python"
vowels = "aeiou"
for i, char in enumerate(word):
    if char.lower() in vowels:
        print(f"First vowel: '{char}' at position {i}")
        break
else:
    print("No vowels found")

# SOLUTION 5
print("\n--- Solution 5 ---")
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_sum = 0
for num in numbers:
    if num < 0:
        continue
    positive_sum += num
print(f"Sum of positives: {positive_sum}")  # 1+3+5+7+9 = 25

# SOLUTION 6
print("\n--- Solution 6 ---")
print("    ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print()
print("   " + "----" * 5)

for i in range(1, 6):
    print(f"{i} |", end="")
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# SOLUTION 7
print("\n--- Solution 7 ---")
attempts = ["wrong1", "wrong2", "secret"]
correct_password = "secret"
max_attempts = 3

for i, attempt in enumerate(attempts):
    if attempt == correct_password:
        print("Welcome! ✓")
        break
    else:
        print(f"Attempt {i+1}: Wrong password")
else:
    print("Account locked! 🔒")

# SOLUTION 8
print("\n--- Solution 8 ---")
print("Prime numbers between 2 and 30:")
for num in range(2, 31):
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

print("\n" + "=" * 50)
print("Great job! Move on to 05_functions_basics next.")
print("=" * 50)
