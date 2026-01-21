"""
Dictionaries and Maps - Examples
================================
Run this file to see dictionaries in action!
"""

print("=" * 50)
print("DICTIONARIES AND MAPS - Examples")
print("=" * 50)

# =============================================================================
# CREATING DICTIONARIES
# =============================================================================
print("\n--- Creating Dictionaries ---\n")

# Empty dictionary
empty_dict = {}
print(f"Empty dict: {empty_dict}")

# With initial values
person = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"Person: {person}")

# From list of tuples
items = dict([("a", 1), ("b", 2), ("c", 3)])
print(f"From tuples: {items}")

# From keyword arguments
config = dict(debug=True, version="1.0", max_size=100)
print(f"From kwargs: {config}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares 1-5: {squares}")

# =============================================================================
# ACCESSING VALUES
# =============================================================================
print("\n--- Accessing Values ---\n")

person = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"Person: {person}")

# Bracket notation
print(f"\nperson['name']: {person['name']}")
print(f"person['age']: {person['age']}")

# Get method (safe access)
print(f"\nperson.get('city'): {person.get('city')}")
print(f"person.get('country'): {person.get('country')}")  # Returns None
print(f"person.get('country', 'USA'): {person.get('country', 'USA')}")  # With default

# =============================================================================
# MODIFYING DICTIONARIES
# =============================================================================
print("\n--- Modifying Dictionaries ---\n")

person = {"name": "Alice"}
print(f"Original: {person}")

# Add new key
person["age"] = 25
print(f"After adding age: {person}")

# Update existing key
person["name"] = "Alicia"
print(f"After updating name: {person}")

# Update multiple keys at once
person.update({"city": "NYC", "job": "Engineer"})
print(f"After update(): {person}")

# Remove with pop (returns value)
job = person.pop("job")
print(f"Popped job '{job}': {person}")

# Remove with del
del person["city"]
print(f"After del city: {person}")

# =============================================================================
# KEYS, VALUES, AND ITEMS
# =============================================================================
print("\n--- Keys, Values, and Items ---\n")

person = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"Dictionary: {person}")

print(f"\nKeys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# =============================================================================
# ITERATING
# =============================================================================
print("\n--- Iterating ---\n")

scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

print("Iterate over keys:")
for name in scores:
    print(f"  {name}")

print("\nIterate over values:")
for score in scores.values():
    print(f"  {score}")

print("\nIterate over items:")
for name, score in scores.items():
    print(f"  {name}: {score}")

# =============================================================================
# DICTIONARY COMPREHENSIONS
# =============================================================================
print("\n--- Dictionary Comprehensions ---\n")

# Basic comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From two lists using zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
print(f"Zipped dict: {people}")

# Transform keys
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# Invert dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# =============================================================================
# NESTED DICTIONARIES
# =============================================================================
print("\n--- Nested Dictionaries ---\n")

# Complex nested structure
school = {
    "class_a": {
        "teacher": "Mr. Smith",
        "students": ["Alice", "Bob", "Charlie"]
    },
    "class_b": {
        "teacher": "Ms. Jones",
        "students": ["David", "Eve", "Frank"]
    }
}

print("School structure:")
for class_name, data in school.items():
    print(f"  {class_name}:")
    print(f"    Teacher: {data['teacher']}")
    print(f"    Students: {data['students']}")

# Access nested values
print(f"\nClass A teacher: {school['class_a']['teacher']}")
print(f"First student in class B: {school['class_b']['students'][0]}")

# =============================================================================
# CHECKING KEYS
# =============================================================================
print("\n--- Checking Keys ---\n")

inventory = {"apples": 10, "bananas": 5, "oranges": 8}

print(f"Inventory: {inventory}")
print(f"'apples' in inventory: {'apples' in inventory}")
print(f"'grapes' in inventory: {'grapes' in inventory}")
print(f"'grapes' not in inventory: {'grapes' not in inventory}")

# =============================================================================
# COMMON PATTERNS
# =============================================================================
print("\n--- Common Patterns ---\n")

# Count occurrences
text = "mississippi"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
print(f"Character counts in '{text}':")
for char, count in sorted(counts.items()):
    print(f"  '{char}': {count}")

# Group items by first letter
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
by_letter = {}
for word in words:
    first = word[0]
    if first not in by_letter:
        by_letter[first] = []
    by_letter[first].append(word)
print(f"\nGrouped by first letter: {by_letter}")

# setdefault for grouping (cleaner)
by_letter2 = {}
for word in words:
    by_letter2.setdefault(word[0], []).append(word)
print(f"With setdefault: {by_letter2}")

# =============================================================================
# MERGING DICTIONARIES
# =============================================================================
print("\n--- Merging Dictionaries ---\n")

defaults = {"color": "red", "size": "medium", "quantity": 1}
updates = {"size": "large", "quantity": 5}

print(f"Defaults: {defaults}")
print(f"Updates: {updates}")

# Using update() - modifies in place
merged = defaults.copy()
merged.update(updates)
print(f"Merged (update): {merged}")

# Using unpacking (Python 3.5+)
merged = {**defaults, **updates}
print(f"Merged (unpack): {merged}")

# Using | operator (Python 3.9+)
# merged = defaults | updates
# print(f"Merged (|): {merged}")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
