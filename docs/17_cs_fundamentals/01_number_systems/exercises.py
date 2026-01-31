"""
Number Systems - Exercises
==========================
Practice converting between decimal, binary, octal, and hexadecimal.
"""

print("=" * 60)
print("NUMBER SYSTEMS - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Binary to Decimal
# =============================================================================
print("\n--- Exercise 1: Binary to Decimal ---")
print("""
Convert the following binary numbers to decimal:
a) 1010
b) 1111
c) 10000
d) 11001100

Hint: Each position represents a power of 2 (1, 2, 4, 8, 16, 32, 64, 128...)
""")

# Your code here:
# exercise_1a = ...
# exercise_1b = ...
# exercise_1c = ...
# exercise_1d = ...

# =============================================================================
# EXERCISE 2: Decimal to Binary
# =============================================================================
print("\n--- Exercise 2: Decimal to Binary ---")
print("""
Convert the following decimal numbers to binary:
a) 5
b) 12
c) 50
d) 200

Hint: Repeatedly divide by 2 and collect the remainders (read bottom-up).
""")

# Your code here:
# exercise_2a = ...
# exercise_2b = ...
# exercise_2c = ...
# exercise_2d = ...

# =============================================================================
# EXERCISE 3: Hexadecimal Conversions
# =============================================================================
print("\n--- Exercise 3: Hexadecimal Conversions ---")
print("""
a) Convert hex FF to decimal
b) Convert hex 1A3 to decimal
c) Convert decimal 100 to hex
d) Convert hex ABC to binary (hint: convert each hex digit to 4 bits)
""")

# Your code here:
# exercise_3a = ...
# exercise_3b = ...
# exercise_3c = ...
# exercise_3d = ...

# =============================================================================
# EXERCISE 4: Octal Conversions
# =============================================================================
print("\n--- Exercise 4: Octal Conversions ---")
print("""
a) Convert octal 77 to decimal
b) Convert octal 100 to decimal
c) Convert decimal 64 to octal
d) Convert octal 52 to binary (hint: each octal digit = 3 bits)
""")

# Your code here:
# exercise_4a = ...
# exercise_4b = ...
# exercise_4c = ...
# exercise_4d = ...

# =============================================================================
# EXERCISE 5: Color Code Parser
# =============================================================================
print("\n--- Exercise 5: Color Code Parser ---")
print("""
Write a function that converts a hex color code (like "#FF5733") to
its RGB components (red, green, blue as decimal values).

Example: "#FF5733" → Red: 255, Green: 87, Blue: 51
""")

def hex_to_rgb(hex_color):
    """
    Convert a hex color string to RGB tuple.

    Args:
        hex_color: String like "#FF5733" or "FF5733"

    Returns:
        Tuple of (red, green, blue) as integers (0-255)
    """
    # Your code here:
    pass

# Test your function
# print(hex_to_rgb("#FF5733"))  # Expected: (255, 87, 51)
# print(hex_to_rgb("#00FF00"))  # Expected: (0, 255, 0)
# print(hex_to_rgb("#000000"))  # Expected: (0, 0, 0)

# =============================================================================
# EXERCISE 6: Binary Addition
# =============================================================================
print("\n--- Exercise 6: Binary Addition ---")
print("""
Implement binary addition without converting to decimal.
Rules:
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (0 with carry 1)
- 1 + 1 + 1 = 11 (1 with carry 1)
""")

def binary_add(a, b):
    """
    Add two binary strings and return the result as a binary string.

    Args:
        a: Binary string (e.g., "1010")
        b: Binary string (e.g., "1100")

    Returns:
        Binary string result (e.g., "10110")
    """
    # Your code here:
    pass

# Test your function
# print(binary_add("1010", "1100"))   # Expected: "10110" (10 + 12 = 22)
# print(binary_add("1111", "1"))      # Expected: "10000" (15 + 1 = 16)
# print(binary_add("0", "0"))         # Expected: "0"

# =============================================================================
# EXERCISE 7: Bit Counter
# =============================================================================
print("\n--- Exercise 7: Bit Counter ---")
print("""
Write a function that counts the number of 1 bits in a number's binary
representation (population count).

Example: 13 = 1101 in binary → 3 bits set
""")

def count_set_bits(n):
    """
    Count the number of 1 bits in the binary representation of n.

    Args:
        n: Positive integer

    Returns:
        Number of set bits
    """
    # Your code here:
    pass

# Test your function
# print(count_set_bits(0))     # Expected: 0
# print(count_set_bits(1))     # Expected: 1
# print(count_set_bits(13))    # Expected: 3 (1101)
# print(count_set_bits(255))   # Expected: 8 (11111111)

# =============================================================================
# EXERCISE 8: Number Guessing Game
# =============================================================================
print("\n--- Exercise 8: Number Guessing Game (Binary Edition) ---")
print("""
Create a number guessing game where the player thinks of a number between
1 and 100, and the computer guesses it using binary search.

The player should respond with:
- 'h' if the guess is too high
- 'l' if the guess is too low
- 'c' if the guess is correct
""")

def binary_search_guess():
    """
    Guess the user's number using binary search.
    """
    print("Think of a number between 1 and 100.")
    print("Respond with: 'h' (too high), 'l' (too low), or 'c' (correct)")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        # Your code here:
        pass

# Uncomment to play:
# binary_search_guess()

print("\n" + "=" * 60)
print("Exercises complete! Check your answers below.")
print("=" * 60)

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("\n--- Exercise 1: Binary to Decimal ---")
print("a) 1010 = 10")
print("   Calculation: 1×8 + 0×4 + 1×2 + 0×1 = 10")
print("b) 1111 = 15")
print("   Calculation: 1×8 + 1×4 + 1×2 + 1×1 = 15")
print("c) 10000 = 16")
print("   Calculation: 1×16 = 16")
print("d) 11001100 = 204")
print("   Calculation: 128 + 64 + 0 + 0 + 8 + 4 + 0 + 0 = 204")

print("\n--- Exercise 2: Decimal to Binary ---")
print("a) 5 = 101")
print("   5 ÷ 2 = 2 R 1")
print("   2 ÷ 2 = 1 R 0")
print("   1 ÷ 2 = 0 R 1")
print("   Read bottom-up: 101")
print("b) 12 = 1100")
print("c) 50 = 110010")
print("d) 200 = 11001000")

print("\n--- Exercise 3: Hexadecimal Conversions ---")
print("a) FF = 255")
print("   F(15) × 16 + F(15) × 1 = 255")
print("b) 1A3 = 419")
print("   1×256 + 10×16 + 3×1 = 419")
print("c) 100 = 0x64")
print("d) ABC = 101010111100")
print("   A=1010, B=1011, C=1100")

print("\n--- Exercise 4: Octal Conversions ---")
print("a) 77 = 63")
print("   7×8 + 7×1 = 63")
print("b) 100 = 64")
print("   1×64 = 64")
print("c) 64 = 0o100")
print("d) 52 = 101010")
print("   5=101, 2=010")

print("\n--- Exercise 5: Color Code Parser (Solution) ---")
solution_5 = '''
def hex_to_rgb(hex_color):
    # Remove # if present
    hex_color = hex_color.lstrip("#")

    # Convert each pair of hex digits
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    return (red, green, blue)
'''
print(solution_5)

print("\n--- Exercise 6: Binary Addition (Solution) ---")
solution_6 = '''
def binary_add(a, b):
    result = []
    carry = 0

    # Pad shorter string with zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Add from right to left
    for i in range(max_len - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result.append(str(bit_sum % 2))
        carry = bit_sum // 2

    # Don't forget final carry
    if carry:
        result.append("1")

    # Reverse to get correct order
    return "".join(reversed(result))
'''
print(solution_6)

print("\n--- Exercise 7: Bit Counter (Solution) ---")
solution_7 = '''
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1  # Check if last bit is 1
        n >>= 1         # Shift right
    return count

# Alternative solution:
def count_set_bits_v2(n):
    return bin(n).count("1")
'''
print(solution_7)

print("\n--- Exercise 8: Number Guessing Game (Solution) ---")
solution_8 = '''
def binary_search_guess():
    print("Think of a number between 1 and 100.")
    print("Respond with: 'h' (too high), 'l' (too low), or 'c' (correct)")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        response = input(f"Is your number {guess}? ").lower()

        if response == 'c':
            print(f"I guessed it in {attempts} attempts!")
            return
        elif response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1
        else:
            print("Please respond with 'h', 'l', or 'c'")

    print("I couldn't guess your number. Did you change it?")
'''
print(solution_8)

print("\n" + "=" * 60)
print("All solutions provided. Keep practicing!")
print("=" * 60)
