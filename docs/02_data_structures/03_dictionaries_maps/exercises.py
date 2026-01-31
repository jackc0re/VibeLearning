"""
Dictionaries and Maps - Exercises
=================================
Try to solve each exercise before looking at the solution!
Solutions are provided at the bottom of this file.
"""

print("=" * 50)
print("DICTIONARIES AND MAPS - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: Word Frequency Counter
# =============================================================================
print("\n--- Exercise 1: Word Frequency Counter ---\n")
"""
Write a function that counts the frequency of each word in a sentence.
Words should be case-insensitive and stripped of punctuation.

Example: "Hello, hello world!" -> {"hello": 2, "world": 1}
"""

def word_frequency(sentence):
    # Your code here:
    pass

# Test:
# print(word_frequency("Hello, hello world!"))


# =============================================================================
# EXERCISE 2: Merge Dictionaries with Sum
# =============================================================================
print("\n--- Exercise 2: Merge Dictionaries with Sum ---\n")
"""
Merge two dictionaries. If a key exists in both, sum the values.

Example:
  d1 = {"a": 1, "b": 2}
  d2 = {"b": 3, "c": 4}
  Result: {"a": 1, "b": 5, "c": 4}
"""

def merge_with_sum(d1, d2):
    # Your code here:
    pass

# Test:
# print(merge_with_sum({"a": 1, "b": 2}, {"b": 3, "c": 4}))


# =============================================================================
# EXERCISE 3: Invert Dictionary (Handle Duplicates)
# =============================================================================
print("\n--- Exercise 3: Invert Dictionary ---\n")
"""
Invert a dictionary (swap keys and values).
If multiple keys have the same value, collect them in a list.

Example:
  {"a": 1, "b": 2, "c": 1} -> {1: ["a", "c"], 2: ["b"]}
"""

def invert_dict(d):
    # Your code here:
    pass

# Test:
# print(invert_dict({"a": 1, "b": 2, "c": 1}))


# =============================================================================
# EXERCISE 4: Deep Get (Nested Access)
# =============================================================================
print("\n--- Exercise 4: Deep Get ---\n")
"""
Write a function that safely gets a value from nested dictionaries
using a list of keys. Return a default if any key is missing.

Example:
  data = {"a": {"b": {"c": 42}}}
  deep_get(data, ["a", "b", "c"]) -> 42
  deep_get(data, ["a", "x", "c"]) -> None
"""

def deep_get(d, keys, default=None):
    # Your code here:
    pass

# Test:
# data = {"a": {"b": {"c": 42}}}
# print(deep_get(data, ["a", "b", "c"]))
# print(deep_get(data, ["a", "x", "c"]))


# =============================================================================
# EXERCISE 5: Group By
# =============================================================================
print("\n--- Exercise 5: Group By ---\n")
"""
Group a list of dictionaries by a specified key.

Example:
  people = [
      {"name": "Alice", "city": "NYC"},
      {"name": "Bob", "city": "LA"},
      {"name": "Charlie", "city": "NYC"}
  ]
  group_by(people, "city") -> {
      "NYC": [{"name": "Alice", "city": "NYC"}, {"name": "Charlie", "city": "NYC"}],
      "LA": [{"name": "Bob", "city": "LA"}]
  }
"""

def group_by(items, key):
    # Your code here:
    pass

# Test:
# people = [
#     {"name": "Alice", "city": "NYC"},
#     {"name": "Bob", "city": "LA"},
#     {"name": "Charlie", "city": "NYC"}
# ]
# print(group_by(people, "city"))


# =============================================================================
# EXERCISE 6: Two Sum with Dict
# =============================================================================
print("\n--- Exercise 6: Two Sum ---\n")
"""
Given a list of numbers and a target sum, find two numbers that add up
to the target. Return their indices. Use a dictionary for O(n) solution.

Example:
  nums = [2, 7, 11, 15], target = 9
  Return: (0, 1) because nums[0] + nums[1] == 9
"""

def two_sum(nums, target):
    # Your code here:
    pass

# Test:
# print(two_sum([2, 7, 11, 15], 9))


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")
import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    clean = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    words = clean.split()
    
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

print(word_frequency("Hello, hello world!"))
print(word_frequency("The quick brown fox jumps over the lazy dog. The dog barks."))

# SOLUTION 2
print("\n--- Solution 2 ---")
def merge_with_sum(d1, d2):
    result = d1.copy()  # Start with copy of d1
    for key, value in d2.items():
        result[key] = result.get(key, 0) + value
    return result

print(f"Merge {'{a:1, b:2}'} + {'{b:3, c:4}'} = {merge_with_sum({'a': 1, 'b': 2}, {'b': 3, 'c': 4})}")

# SOLUTION 3
print("\n--- Solution 3 ---")
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted

original = {"a": 1, "b": 2, "c": 1}
print(f"Original: {original}")
print(f"Inverted: {invert_dict(original)}")

# SOLUTION 4
print("\n--- Solution 4 ---")
def deep_get(d, keys, default=None):
    current = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

data = {"a": {"b": {"c": 42}}}
print(f"Data: {data}")
print(f"deep_get(['a', 'b', 'c']): {deep_get(data, ['a', 'b', 'c'])}")
print(f"deep_get(['a', 'x', 'c']): {deep_get(data, ['a', 'x', 'c'])}")
print(f"deep_get(['a', 'b']): {deep_get(data, ['a', 'b'])}")

# SOLUTION 5
print("\n--- Solution 5 ---")
def group_by(items, key):
    groups = {}
    for item in items:
        group_key = item.get(key)
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(item)
    return groups

people = [
    {"name": "Alice", "city": "NYC"},
    {"name": "Bob", "city": "LA"},
    {"name": "Charlie", "city": "NYC"}
]
print("People grouped by city:")
for city, members in group_by(people, "city").items():
    print(f"  {city}: {[p['name'] for p in members]}")

# SOLUTION 6
print("\n--- Solution 6 ---")
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

print(f"two_sum([2, 7, 11, 15], 9): {two_sum([2, 7, 11, 15], 9)}")
print(f"two_sum([3, 2, 4], 6): {two_sum([3, 2, 4], 6)}")

print("\n" + "=" * 50)
print("Great job! Move on to 04_sets next.")
print("=" * 50)
