"""
Bitwise Operations - Exercises
==============================
Practice using bitwise operators.
"""

print("=" * 60)
print("BITWISE OPERATIONS - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Basic Operations
# =============================================================================
print("\n--- Exercise 1: Basic Operations ---")
print("""
Calculate the following without using Python first, then verify:
a) 12 & 10
b) 12 | 10
c) 12 ^ 10
d) ~5 (in 8-bit)
""")

# Your code here:
# exercise_1a = ...
# exercise_1b = ...
# exercise_1c = ...
# exercise_1d = ...

# =============================================================================
# EXERCISE 2: Shift Operations
# =============================================================================
print("\n--- Exercise 2: Shift Operations ---")
print("""
What is the result of:
a) 8 << 2
b) 32 >> 3
c) 1 << 8
d) 255 >> 4

Explain what each operation does mathematically.
""")

# Your code here:
# exercise_2a = ...
# exercise_2b = ...
# exercise_2c = ...
# exercise_2d = ...

# =============================================================================
# EXERCISE 3: Permission System
# =============================================================================
print("\n--- Exercise 3: Permission System ---")
print("""
Create a permission system with these flags:
- VIEW = 1
- EDIT = 2
- DELETE = 4
- ADMIN = 8

a) Create a user with VIEW and EDIT permissions
b) Check if this user can DELETE
c) Add DELETE permission to the user
d) Remove EDIT permission
e) Toggle ADMIN permission twice
""")

# Your code here:
# VIEW = ...
# EDIT = ...
# DELETE = ...
# ADMIN = ...

# =============================================================================
# EXERCISE 4: Is Power of Two
# =============================================================================
print("\n--- Exercise 4: Is Power of Two ---")
print("""
Write a function that checks if a number is a power of 2.

Hint: Powers of 2 in binary have exactly one bit set:
- 1 = 0001
- 2 = 0010
- 4 = 0100
- 8 = 1000

What happens when you do n & (n-1) for a power of 2?
""")

def is_power_of_two(n):
    """
    Return True if n is a power of 2, False otherwise.

    Args:
        n: Positive integer

    Returns:
        Boolean
    """
    # Your code here:
    pass

# Test your function
# print(is_power_of_two(1))    # Expected: True
# print(is_power_of_two(2))    # Expected: True
# print(is_power_of_two(3))    # Expected: False
# print(is_power_of_two(16))   # Expected: True
# print(is_power_of_two(18))   # Expected: False
# print(is_power_of_two(256))  # Expected: True

# =============================================================================
# EXERCISE 5: Count Set Bits
# =============================================================================
print("\n--- Exercise 5: Count Set Bits ---")
print("""
Write a function that counts the number of 1 bits in a number.

Challenge: Can you do this without converting to a string?
""")

def count_set_bits(n):
    """
    Count the number of 1 bits in n.

    Args:
        n: Non-negative integer

    Returns:
        Count of set bits
    """
    # Your code here:
    pass

# Test your function
# print(count_set_bits(0))      # Expected: 0
# print(count_set_bits(1))      # Expected: 1
# print(count_set_bits(7))      # Expected: 3 (111)
# print(count_set_bits(15))     # Expected: 4 (1111)
# print(count_set_bits(255))    # Expected: 8 (11111111)

# =============================================================================
# EXERCISE 6: Get/Set/Clear/Toggle Bit
# =============================================================================
print("\n--- Exercise 6: Bit Manipulation Functions ---")
print("""
Implement these utility functions:
- get_bit(value, position): Return True if bit at position is 1
- set_bit(value, position): Set bit at position to 1
- clear_bit(value, position): Set bit at position to 0
- toggle_bit(value, position): Flip bit at position
""")

def get_bit(value, position):
    """Get the bit at the given position (0-indexed from right)."""
    # Your code here:
    pass

def set_bit(value, position):
    """Set the bit at the given position to 1."""
    # Your code here:
    pass

def clear_bit(value, position):
    """Clear the bit at the given position (set to 0)."""
    # Your code here:
    pass

def toggle_bit(value, position):
    """Toggle the bit at the given position."""
    # Your code here:
    pass

# Test your functions
# value = 0b10101010  # 170
# print(f"Original: {value:08b}")
# print(f"Get bit 3: {get_bit(value, 3)}")      # Expected: False
# print(f"Get bit 1: {get_bit(value, 1)}")      # Expected: True
# print(f"Set bit 3: {set_bit(value, 3):08b}")  # Expected: 10101110
# print(f"Clear bit 1: {clear_bit(value, 1):08b}")  # Expected: 10101000
# print(f"Toggle bit 0: {toggle_bit(value, 0):08b}")  # Expected: 10101011

# =============================================================================
# EXERCISE 7: Reverse Bits
# =============================================================================
print("\n--- Exercise 7: Reverse Bits ---")
print("""
Write a function that reverses the bits of an 8-bit number.

Example: 0b10110010 → 0b01001101
""")

def reverse_bits(n):
    """
    Reverse the bits of an 8-bit number.

    Args:
        n: 8-bit integer (0-255)

    Returns:
        Integer with bits reversed
    """
    # Your code here:
    pass

# Test your function
# print(f"{0b10110010:08b} reversed = {reverse_bits(0b10110010):08b}")  # 01001101
# print(f"{0b11110000:08b} reversed = {reverse_bits(0b11110000):08b}")  # 00001111
# print(f"{0b00000001:08b} reversed = {reverse_bits(0b00000001):08b}")  # 10000000

# =============================================================================
# EXERCISE 8: Find the Odd One Out
# =============================================================================
print("\n--- Exercise 8: Find the Odd One Out ---")
print("""
You have a list of integers where every number appears twice except one.
Find the number that appears only once using XOR.

Example: [4, 3, 4, 5, 3] → 5

Hint: A ^ A = 0, and A ^ 0 = A
""")

def find_odd_one_out(numbers):
    """
    Find the number that appears only once.

    Args:
        numbers: List of integers where one appears once, rest appear twice

    Returns:
        The number that appears only once
    """
    # Your code here:
    pass

# Test your function
# print(find_odd_one_out([4, 3, 4, 5, 3]))       # Expected: 5
# print(find_odd_one_out([1, 2, 1, 3, 2]))       # Expected: 3
# print(find_odd_one_out([7, 7, 8, 8, 9]))       # Expected: 9
# print(find_odd_one_out([42]))                   # Expected: 42

print("\n" + "=" * 60)
print("Exercises complete! Check your answers below.")
print("=" * 60)

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("\n--- Exercise 1: Basic Operations ---")
print("a) 12 & 10 = 8")
print("   1100 & 1010 = 1000")
print("b) 12 | 10 = 14")
print("   1100 | 1010 = 1110")
print("c) 12 ^ 10 = 6")
print("   1100 ^ 1010 = 0110")
print("d) ~5 in 8-bit = 250")
print("   ~00000101 & 11111111 = 11111010 = 250")

print("\n--- Exercise 2: Shift Operations ---")
print("a) 8 << 2 = 32  (8 × 4)")
print("b) 32 >> 3 = 4  (32 ÷ 8)")
print("c) 1 << 8 = 256  (1 × 256)")
print("d) 255 >> 4 = 15  (255 ÷ 16 = 15.9375 → 15)")

print("\n--- Exercise 3: Permission System (Solution) ---")
solution_3 = '''
VIEW = 1 << 0    # 1
EDIT = 1 << 1    # 2
DELETE = 1 << 2  # 4
ADMIN = 1 << 3   # 8

# a) Create user with VIEW and EDIT
user = VIEW | EDIT  # 3

# b) Check if can DELETE
can_delete = (user & DELETE) != 0  # False

# c) Add DELETE
user |= DELETE  # Now 7

# d) Remove EDIT
user &= ~EDIT   # Now 5

# e) Toggle ADMIN twice
user ^= ADMIN   # Now 13
user ^= ADMIN   # Back to 5
'''
print(solution_3)

print("\n--- Exercise 4: Is Power of Two (Solution) ---")
solution_4 = '''
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Explanation:
# Powers of 2 have exactly one bit set.
# For 8 (1000): 8 - 1 = 7 (0111)
# 8 & 7 = 1000 & 0111 = 0000
# So n & (n-1) == 0 for powers of 2
'''
print(solution_4)

print("\n--- Exercise 5: Count Set Bits (Solution) ---")
solution_5 = '''
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Alternative (Brian Kernighan's algorithm):
def count_set_bits_v2(n):
    count = 0
    while n:
        n &= n - 1  # Clear the lowest set bit
        count += 1
    return count
'''
print(solution_5)

print("\n--- Exercise 6: Bit Manipulation Functions (Solution) ---")
solution_6 = '''
def get_bit(value, position):
    return (value >> position) & 1
    # OR: return (value & (1 << position)) != 0

def set_bit(value, position):
    return value | (1 << position)

def clear_bit(value, position):
    return value & ~(1 << position)

def toggle_bit(value, position):
    return value ^ (1 << position)
'''
print(solution_6)

print("\n--- Exercise 7: Reverse Bits (Solution) ---")
solution_7 = '''
def reverse_bits(n):
    result = 0
    for i in range(8):
        # Get bit at position i and place it at position (7-i)
        bit = (n >> i) & 1
        result |= bit << (7 - i)
    return result

# Alternative: lookup table (faster for many operations)
def reverse_bits_lookup(n):
    lookup = [
        0x00, 0x80, 0x40, 0xC0, 0x20, 0xA0, 0x60, 0xE0,
        # ... (full 256-entry table would go here)
    ]
    return lookup[n]
'''
print(solution_7)

print("\n--- Exercise 8: Find the Odd One Out (Solution) ---")
solution_8 = '''
def find_odd_one_out(numbers):
    result = 0
    for num in numbers:
        result ^= num
    return result

# Explanation:
# XOR of a number with itself is 0
# XOR is commutative and associative
# So: 4 ^ 3 ^ 4 ^ 5 ^ 3 = (4 ^ 4) ^ (3 ^ 3) ^ 5 = 0 ^ 0 ^ 5 = 5
'''
print(solution_8)

print("\n" + "=" * 60)
print("All solutions provided. Keep practicing!")
print("=" * 60)
