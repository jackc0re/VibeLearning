"""
Lists and Arrays - Exercises
============================
Try to solve each exercise before looking at the solution!
Solutions are provided at the bottom of this file.
"""

print("=" * 50)
print("LISTS AND ARRAYS - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: List Basics
# =============================================================================
print("\n--- Exercise 1: List Basics ---\n")
"""
Create a list called 'colors' with 5 of your favorite colors.
Then:
1. Print the first color
2. Print the last color
3. Print the middle 3 colors (using slicing)
4. Add a new color to the end
5. Remove the second color
6. Print the final list
"""

# Your code here:
# colors = ...


# =============================================================================
# EXERCISE 2: List Comprehension
# =============================================================================
print("\n--- Exercise 2: List Comprehension ---\n")
"""
Use list comprehension to create:
1. A list of cubes from 1 to 10 (1³, 2³, 3³, ... 10³)
2. A list of all numbers from 1-50 that are divisible by 3
3. A list where each word from ['apple', 'banana', 'cherry'] is reversed
"""

# Your code here:
# cubes = ...
# divisible_by_3 = ...
# reversed_words = ...


# =============================================================================
# EXERCISE 3: Find the Second Largest
# =============================================================================
print("\n--- Exercise 3: Find the Second Largest ---\n")
"""
Given a list of numbers, find the second largest number.
Do NOT use sort() - try to do it with a single pass through the list.

Test with: [10, 5, 20, 8, 15]
Expected output: 15
"""

test_numbers = [10, 5, 20, 8, 15]

# Your code here:
# second_largest = ...


# =============================================================================
# EXERCISE 4: Remove Duplicates (Keep Order)
# =============================================================================
print("\n--- Exercise 4: Remove Duplicates ---\n")
"""
Remove duplicates from a list while keeping the original order.
(Hint: You can't just convert to set because sets don't keep order)

Test with: [1, 2, 2, 3, 4, 3, 5, 1, 6]
Expected output: [1, 2, 3, 4, 5, 6]
"""

test_list = [1, 2, 2, 3, 4, 3, 5, 1, 6]

# Your code here:
# unique = ...


# =============================================================================
# EXERCISE 5: Rotate a List
# =============================================================================
print("\n--- Exercise 5: Rotate a List ---\n")
"""
Rotate a list to the right by k positions.
Example: rotate [1, 2, 3, 4, 5] by 2 positions -> [4, 5, 1, 2, 3]

Test with: [1, 2, 3, 4, 5], k=2
"""

def rotate_list(lst, k):
    # Your code here:
    pass

# Test
# rotated = rotate_list([1, 2, 3, 4, 5], 2)
# print(f"Rotated: {rotated}")


# =============================================================================
# EXERCISE 6: Matrix Diagonal
# =============================================================================
print("\n--- Exercise 6: Matrix Diagonal ---\n")
"""
Given a square matrix (2D list), extract the main diagonal.
Main diagonal: elements where row index equals column index.

Test with:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Expected output: [1, 5, 9]
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Your code here:
# diagonal = ...


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")
colors = ["blue", "green", "purple", "orange", "red"]
print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print(f"Middle 3: {colors[1:4]}")
colors.append("pink")
print(f"After append: {colors}")
colors.pop(1)
print(f"Final list: {colors}")

# SOLUTION 2
print("\n--- Solution 2 ---")
cubes = [x ** 3 for x in range(1, 11)]
print(f"Cubes 1-10: {cubes}")

divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print(f"Divisible by 3: {divisible_by_3}")

words = ['apple', 'banana', 'cherry']
reversed_words = [w[::-1] for w in words]
print(f"Reversed words: {reversed_words}")

# SOLUTION 3
print("\n--- Solution 3 ---")
test_numbers = [10, 5, 20, 8, 15]
largest = second = float('-inf')
for num in test_numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(f"List: {test_numbers}")
print(f"Second largest: {second}")

# SOLUTION 4
print("\n--- Solution 4 ---")
test_list = [1, 2, 2, 3, 4, 3, 5, 1, 6]
seen = set()
unique = []
for item in test_list:
    if item not in seen:
        unique.append(item)
        seen.add(item)
print(f"Original: {test_list}")
print(f"Unique: {unique}")

# SOLUTION 5
print("\n--- Solution 5 ---")
def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)  # Handle k > len(lst)
    return lst[-k:] + lst[:-k]

original = [1, 2, 3, 4, 5]
rotated = rotate_list(original, 2)
print(f"Original: {original}")
print(f"Rotated by 2: {rotated}")

# SOLUTION 6
print("\n--- Solution 6 ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal = [matrix[i][i] for i in range(len(matrix))]
print("Matrix:")
for row in matrix:
    print(f"  {row}")
print(f"Diagonal: {diagonal}")

print("\n" + "=" * 50)
print("Great job! Move on to 02_strings next.")
print("=" * 50)
