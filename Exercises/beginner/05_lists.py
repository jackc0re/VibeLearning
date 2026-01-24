"""
Beginner Exercise 5: Lists and Arrays
=====================================
Practice list operations, slicing, and manipulation.
"""

print("=" * 50)
print("EXERCISE 5: Lists and Arrays")
print("=" * 50)


# =============================================================================
# EXERCISE 5.1: List Operations
# =============================================================================
print("\n--- Exercise 5.1: List Operations ---")
"""
Given a list of numbers:
1. Add 10 to the end
2. Insert 5 at position 2
3. Remove the first occurrence of 3
4. Remove and return the last element
"""

numbers = [1, 2, 3, 4, 5]

# Your code below:
# operations here

print(f"Result: {numbers}")


# =============================================================================
# EXERCISE 5.2: List Slicing
# =============================================================================
print("\n--- Exercise 5.2: List Slicing ---")
"""
Given a list, extract:
1. First 3 elements
2. Last 3 elements
3. Every second element
4. Reverse the list
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Your code below:
first_three =  # First 3 elements
last_three =  # Last 3 elements
every_second =  # Every second element
reversed_list =  # Reversed list

print(f"Original: {numbers}")
print(f"First three: {first_three}")
print(f"Last three: {last_three}")
print(f"Every second: {every_second}")
print(f"Reversed: {reversed_list}")


# =============================================================================
# EXERCISE 5.3: Find in List
# =============================================================================
print("\n--- Exercise 5.3: Find in List ---")
"""
Find the index of a value in a list.
Return -1 if not found (don't use .index() directly, implement manually).
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# Your code below:
index =  # Find index of target
print(f"List: {numbers}")
print(f"Index of {target}: {index}")


# =============================================================================
# EXERCISE 5.4: Remove Duplicates
# =============================================================================
print("\n--- Exercise 5.4: Remove Duplicates ---")
"""
Remove duplicates from a list while preserving order.
"""

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 7, 7]

# Your code below:
unique_numbers =  # Remove duplicates, preserve order
print(f"Original: {numbers}")
print(f"Unique: {unique_numbers}")


# =============================================================================
# EXERCISE 5.5: Rotate List
# =============================================================================
print("\n--- Exercise 5.5: Rotate List ---")
"""
Rotate a list to the left by n positions.
Example: [1,2,3,4,5] rotated by 2 -> [3,4,5,1,2]
"""

numbers = [1, 2, 3, 4, 5]
n = 2

# Your code below:
rotated =  # Rotate list by n positions
print(f"Original: {numbers}")
print(f"Rotated by {n}: {rotated}")


# =============================================================================
# EXERCISE 5.6: Merge Sorted Lists
# =============================================================================
print("\n--- Exercise 5.6: Merge Sorted Lists ---")
"""
Merge two sorted lists into one sorted list.
"""

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

# Your code below:
merged =  # Merge two sorted lists
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged: {merged}")


# =============================================================================
# EXERCISE 5.7: Find Common Elements
# =============================================================================
print("\n--- Exercise 5.7: Find Common Elements ---")
"""
Find elements common to both lists.
"""

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Your code below:
common =  # Find common elements
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common: {common}")


# =============================================================================
# EXERCISE 5.8: Flatten Nested List
# =============================================================================
print("\n--- Exercise 5.8: Flatten Nested List ---")
"""
Flatten a nested list into a single-level list.
"""

nested = [[1, 2], [3, 4], [5, 6, 7], [8, 9, 10]]

# Your code below:
flat =  # Flatten the nested list
print(f"Nested: {nested}")
print(f"Flattened: {flat}")


# =============================================================================
# EXERCISE 5.9: List Partition
# =============================================================================
print("\n--- Exercise 5.9: List Partition ---")
"""
Partition a list into even and odd numbers.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Your code below:
evens =  # Even numbers
odds =  # Odd numbers

print(f"Original: {numbers}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")


# =============================================================================
# EXERCISE 5.10: Second Largest
# =============================================================================
print("\n--- Exercise 5.10: Second Largest ---")
"""
Find the second largest element in a list.
"""

numbers = [1, 5, 2, 8, 3, 9, 4, 7, 6]

# Your code below:
second_largest =  # Find second largest element
print(f"List: {numbers}")
print(f"Second largest: {second_largest}")


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 5.1
print("\n--- Solution 5.1 ---")
numbers = [1, 2, 3, 4, 5]
numbers.append(10)
numbers.insert(2, 5)
numbers.remove(3)
last = numbers.pop()
print(f"Result: {numbers}")
print(f"Popped: {last}")

# SOLUTION 5.2
print("\n--- Solution 5.2 ---")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
first_three = numbers[:3]
last_three = numbers[-3:]
every_second = numbers[::2]
reversed_list = numbers[::-1]
print(f"Original: {numbers}")
print(f"First three: {first_three}")
print(f"Last three: {last_three}")
print(f"Every second: {every_second}")
print(f"Reversed: {reversed_list}")

# SOLUTION 5.3
print("\n--- Solution 5.3 ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
index = -1
for i, num in enumerate(numbers):
    if num == target:
        index = i
        break
print(f"List: {numbers}")
print(f"Index of {target}: {index}")

# SOLUTION 5.4
print("\n--- Solution 5.4 ---")
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 7, 7]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"Original: {numbers}")
print(f"Unique: {unique_numbers}")

# SOLUTION 5.5
print("\n--- Solution 5.5 ---")
numbers = [1, 2, 3, 4, 5]
n = 2
rotated = numbers[n:] + numbers[:n]
print(f"Original: {numbers}")
print(f"Rotated by {n}: {rotated}")

# SOLUTION 5.6
print("\n--- Solution 5.6 ---")
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
merged = sorted(list1 + list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged: {merged}")

# SOLUTION 5.7
print("\n--- Solution 5.7 ---")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = [num for num in list1 if num in list2]
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common: {common}")

# SOLUTION 5.8
print("\n--- Solution 5.8 ---")
nested = [[1, 2], [3, 4], [5, 6, 7], [8, 9, 10]]
flat = [item for sublist in nested for item in sublist]
print(f"Nested: {nested}")
print(f"Flattened: {flat}")

# SOLUTION 5.9
print("\n--- Solution 5.9 ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(f"Original: {numbers}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# SOLUTION 5.10
print("\n--- Solution 5.10 ---")
numbers = [1, 5, 2, 8, 3, 9, 4, 7, 6]
sorted_numbers = sorted(numbers)
second_largest = sorted_numbers[-2]
print(f"List: {numbers}")
print(f"Second largest: {second_largest}")

print("\n" + "=" * 50)
print("Great job! Move on to 06_strings.py")
print("=" * 50)
