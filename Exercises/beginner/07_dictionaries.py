"""
Beginner Exercise 7: Dictionaries
=================================
Practice dictionary operations and manipulations.
"""

print("=" * 50)
print("EXERCISE 7: Dictionaries")
print("=" * 50)


# =============================================================================
# EXERCISE 7.1: Basic Dictionary Operations
# =============================================================================
print("\n--- Exercise 7.1: Basic Operations ---")
"""
Given a dictionary:
1. Add a new key-value pair
2. Update an existing value
3. Delete a key
4. Get a value (with default if key doesn't exist)
"""

person = {"name": "Alice", "age": 25, "city": "NYC"}

# Your code below:
# operations here

print(f"Result: {person}")


# =============================================================================
# EXERCISE 7.2: Dictionary Iteration
# =============================================================================
print("\n--- Exercise 7.2: Dictionary Iteration ---")
"""
Iterate over a dictionary and print:
1. All keys
2. All values
3. All key-value pairs
"""

person = {"name": "Alice", "age": 25, "city": "NYC"}

# Your code below:
print("Keys:")
# iterate keys

print("\nValues:")
# iterate values

print("\nItems:")
# iterate items


# =============================================================================
# EXERCISE 7.3: Dictionary Comprehension
# =============================================================================
print("\n--- Exercise 7.3: Dictionary Comprehension ---")
"""
Create a new dictionary from a list, where:
- Keys: numbers from 1 to 10
- Values: squares of the numbers
"""

# Your code below:
squares = {}  # Dictionary comprehension
print(f"Squares: {squares}")


# =============================================================================
# EXERCISE 7.4: Merge Dictionaries
# =============================================================================
print("\n--- Exercise 7.4: Merge Dictionaries ---")
"""
Merge two dictionaries.
"""

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "d": 5, "e": 6}

# Your code below:
merged = None  # Merge dictionaries
print(f"Dict 1: {dict1}")
print(f"Dict 2: {dict2}")
print(f"Merged: {merged}")


# =============================================================================
# EXERCISE 7.5: Count Words
# =============================================================================
print("\n--- Exercise 7.5: Count Words ---")
"""
Count the frequency of each word in a sentence.
"""

text = "the quick brown fox jumps over the lazy dog the fox"

# Your code below:
word_counts = {}  # Dictionary of word counts

print(f"Text: {text}")
print("Word counts:")
for word, count in sorted(word_counts.items()):
    print(f"  '{word}': {count}")


# =============================================================================
# EXERCISE 7.6: Find Keys by Value
# =============================================================================
print("\n--- Exercise 7.6: Find Keys by Value ---")
"""
Find all keys that have a specific value.
"""

scores = {"Alice": 95, "Bob": 87, "Charlie": 95, "David": 82, "Eve": 95}
target_score = 95

# Your code below:
top_scorers = None  # Keys with target value

print(f"Scores: {scores}")
print(f"Students with score {target_score}: {top_scorers}")


# =============================================================================
# EXERCISE 7.7: Sort Dictionary by Value
# =============================================================================
print("\n--- Exercise 7.7: Sort by Value ---")
"""
Sort a dictionary by its values.
"""

scores = {"Alice": 95, "Bob": 87, "Charlie": 95, "David": 82}

# Your code below:
sorted_by_value = None  # Dictionary sorted by values

print(f"Original: {scores}")
print(f"Sorted by value: {sorted_by_value}")


# =============================================================================
# EXERCISE 7.8: Nested Dictionary Access
# =============================================================================
print("\n--- Exercise 7.8: Nested Dictionary ---")
"""
Access nested dictionary values safely.
"""

data = {
    "user": {
        "name": "Alice",
        "contact": {"email": "alice@example.com", "phone": "123-456-7890"},
    }
}

# Your code below:
email = None  # Get email safely
phone = None  # Get phone safely
address = None  # Get address safely (may not exist)

print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Address: {address}")


# =============================================================================
# EXERCISE 7.9: Invert Dictionary
# =============================================================================
print("\n--- Exercise 7.9: Invert Dictionary ---")
"""
Invert a dictionary (swap keys and values).
If values are duplicates, store keys in a list.
"""

original = {"a": 1, "b": 2, "c": 3, "d": 2}

# Your code below:
inverted = None  # Inverted dictionary
print(f"Original: {original}")
print(f"Inverted: {inverted}")


# =============================================================================
# EXERCISE 7.10: Deep Copy
# =============================================================================
print("\n--- Exercise 7.10: Deep Copy ---")
"""
Create a deep copy of a nested dictionary and modify it.
Verify the original is unchanged.
"""

original = {"nested": {"value": 42}}

# Your code below:
import copy

deep_copied = None  # Deep copy
# Modify the copy
# Verify original is unchanged

print(f"Original: {original}")
print(f"Copy: {deep_copied}")


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 7.1
print("\n--- Solution 7.1 ---")
person = {"name": "Alice", "age": 25, "city": "NYC"}
person["email"] = "alice@example.com"
person["age"] = 26
del person["city"]
country = person.get("country", "Unknown")
print(f"Result: {person}")
print(f"Country: {country}")

# SOLUTION 7.2
print("\n--- Solution 7.2 ---")
person = {"name": "Alice", "age": 25, "city": "NYC"}
print("Keys:")
for key in person.keys():
    print(f"  {key}")

print("\nValues:")
for value in person.values():
    print(f"  {value}")

print("\nItems:")
for key, value in person.items():
    print(f"  {key}: {value}")

# SOLUTION 7.3
print("\n--- Solution 7.3 ---")
squares = {i: i**2 for i in range(1, 11)}
print(f"Squares: {squares}")

# SOLUTION 7.4
print("\n--- Solution 7.4 ---")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "d": 5, "e": 6}
merged = {**dict1, **dict2}
print(f"Dict 1: {dict1}")
print(f"Dict 2: {dict2}")
print(f"Merged: {merged}")

# SOLUTION 7.5
print("\n--- Solution 7.5 ---")
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(f"Text: {text}")
print("Word counts:")
for word, count in sorted(word_counts.items()):
    print(f"  '{word}': {count}")

# SOLUTION 7.6
print("\n--- Solution 7.6 ---")
scores = {"Alice": 95, "Bob": 87, "Charlie": 95, "David": 82, "Eve": 95}
target_score = 95
top_scorers = [name for name, score in scores.items() if score == target_score]
print(f"Scores: {scores}")
print(f"Students with score {target_score}: {top_scorers}")

# SOLUTION 7.7
print("\n--- Solution 7.7 ---")
scores = {"Alice": 95, "Bob": 87, "Charlie": 95, "David": 82}
sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1]))
print(f"Original: {scores}")
print(f"Sorted by value: {sorted_by_value}")

# SOLUTION 7.8
print("\n--- Solution 7.8 ---")
data = {
    "user": {
        "name": "Alice",
        "contact": {"email": "alice@example.com", "phone": "123-456-7890"},
    }
}
email = data.get("user", {}).get("contact", {}).get("email", "Not found")
phone = data.get("user", {}).get("contact", {}).get("phone", "Not found")
address = data.get("user", {}).get("contact", {}).get("address", "Not found")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Address: {address}")

# SOLUTION 7.9
print("\n--- Solution 7.9 ---")
original = {"a": 1, "b": 2, "c": 3, "d": 2}
inverted = {}
for key, value in original.items():
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = [key]
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# SOLUTION 7.10
print("\n--- Solution 7.10 ---")
import copy

original = {"nested": {"value": 42}}
deep_copied = copy.deepcopy(original)
deep_copied["nested"]["value"] = 99
print(f"Original: {original}")
print(f"Copy: {deep_copied}")

print("\n" + "=" * 50)
print("Great job! Move on to 08_sets_tuples.py")
print("=" * 50)
