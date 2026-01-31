"""
Sets - Exercises
================
Try to solve each exercise before looking at the solution!
Solutions are provided at the bottom of this file.
"""

print("=" * 50)
print("SETS - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: Find Unique Characters
# =============================================================================
print("\n--- Exercise 1: Find Unique Characters ---\n")
"""
Write a function that returns unique characters from a string,
excluding spaces and punctuation. Case insensitive.

Example: "Hello, World!" -> {'h', 'e', 'l', 'o', 'w', 'r', 'd'}
"""

def unique_chars(text):
    # Your code here:
    pass

# Test:
# print(unique_chars("Hello, World!"))


# =============================================================================
# EXERCISE 2: Missing Numbers
# =============================================================================
print("\n--- Exercise 2: Missing Numbers ---\n")
"""
Given two lists: one complete range and one with missing numbers,
find the missing numbers.

Example:
  complete = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  partial = [1, 2, 4, 6, 8, 10]
  Missing: {3, 5, 7, 9}
"""

def find_missing(complete, partial):
    # Your code here:
    pass

# Test:
# print(find_missing([1,2,3,4,5,6,7,8,9,10], [1,2,4,6,8,10]))


# =============================================================================
# EXERCISE 3: Common Friends
# =============================================================================
print("\n--- Exercise 3: Common Friends ---\n")
"""
Given a dictionary of people and their friends (as sets),
find common friends between two people.

Example:
  friends = {
      "Alice": {"Bob", "Charlie", "David"},
      "Eve": {"Bob", "Frank", "David"}
  }
  Common friends of Alice and Eve: {"Bob", "David"}
"""

def common_friends(friends_dict, person1, person2):
    # Your code here:
    pass

# Test:
# friends = {
#     "Alice": {"Bob", "Charlie", "David"},
#     "Eve": {"Bob", "Frank", "David"}
# }
# print(common_friends(friends, "Alice", "Eve"))


# =============================================================================
# EXERCISE 4: Pangram Checker
# =============================================================================
print("\n--- Exercise 4: Pangram Checker ---\n")
"""
A pangram contains every letter of the alphabet.
Write a function to check if a string is a pangram.

Example:
  "The quick brown fox jumps over the lazy dog" -> True
  "Hello World" -> False
"""

def is_pangram(text):
    # Your code here:
    pass

# Test:
# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("Hello World"))


# =============================================================================
# EXERCISE 5: Set Operations Quiz
# =============================================================================
print("\n--- Exercise 5: Set Operations ---\n")
"""
Given two sets of students:
  math_students = {"Alice", "Bob", "Charlie", "David"}
  science_students = {"Bob", "David", "Eve", "Frank"}

Find:
1. Students taking both classes
2. Students taking only math
3. Students taking only science
4. All students
5. Students taking exactly one class
"""

math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Bob", "David", "Eve", "Frank"}

# Your code here:
# both = ...
# only_math = ...
# only_science = ...
# all_students = ...
# exactly_one = ...


# =============================================================================
# EXERCISE 6: Longest Substring Without Repeating
# =============================================================================
print("\n--- Exercise 6: Longest Unique Substring ---\n")
"""
Find the length of the longest substring without repeating characters.
Use a set to track characters in the current window.

Examples:
  "abcabcbb" -> 3 ("abc")
  "bbbbb" -> 1 ("b")
  "pwwkew" -> 3 ("wke")
"""

def longest_unique_substring(s):
    # Your code here:
    pass

# Test:
# print(longest_unique_substring("abcabcbb"))
# print(longest_unique_substring("bbbbb"))
# print(longest_unique_substring("pwwkew"))


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")
def unique_chars(text):
    return {c.lower() for c in text if c.isalpha()}

print(f"'Hello, World!': {unique_chars('Hello, World!')}")

# SOLUTION 2
print("\n--- Solution 2 ---")
def find_missing(complete, partial):
    return set(complete) - set(partial)

complete = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
partial = [1, 2, 4, 6, 8, 10]
print(f"Complete: {complete}")
print(f"Partial: {partial}")
print(f"Missing: {find_missing(complete, partial)}")

# SOLUTION 3
print("\n--- Solution 3 ---")
def common_friends(friends_dict, person1, person2):
    return friends_dict.get(person1, set()) & friends_dict.get(person2, set())

friends = {
    "Alice": {"Bob", "Charlie", "David"},
    "Eve": {"Bob", "Frank", "David"}
}
print(f"Alice's friends: {friends['Alice']}")
print(f"Eve's friends: {friends['Eve']}")
print(f"Common friends: {common_friends(friends, 'Alice', 'Eve')}")

# SOLUTION 4
print("\n--- Solution 4 ---")
import string

def is_pangram(text):
    alphabet = set(string.ascii_lowercase)
    text_letters = set(text.lower())
    return alphabet.issubset(text_letters)

print(f"'The quick brown fox jumps over the lazy dog': {is_pangram('The quick brown fox jumps over the lazy dog')}")
print(f"'Hello World': {is_pangram('Hello World')}")

# SOLUTION 5
print("\n--- Solution 5 ---")
math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Bob", "David", "Eve", "Frank"}

both = math_students & science_students
only_math = math_students - science_students
only_science = science_students - math_students
all_students = math_students | science_students
exactly_one = math_students ^ science_students

print(f"Math: {math_students}")
print(f"Science: {science_students}")
print(f"\nBoth classes: {both}")
print(f"Only math: {only_math}")
print(f"Only science: {only_science}")
print(f"All students: {all_students}")
print(f"Exactly one class: {exactly_one}")

# SOLUTION 6
print("\n--- Solution 6 ---")
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(f"'abcabcbb': {longest_unique_substring('abcabcbb')}")
print(f"'bbbbb': {longest_unique_substring('bbbbb')}")
print(f"'pwwkew': {longest_unique_substring('pwwkew')}")

print("\n" + "=" * 50)
print("Great job! Move on to 05_tuples next.")
print("=" * 50)
