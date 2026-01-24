"""
Beginner Exercise 6: Strings
============================
Practice string manipulation and operations.
"""

print("=" * 50)
print("EXERCISE 6: Strings")
print("=" * 50)


# =============================================================================
# EXERCISE 6.1: String Basics
# =============================================================================
print("\n--- Exercise 6.1: String Basics ---")
"""
Given a string:
1. Get its length
2. Convert to uppercase
3. Convert to lowercase
4. Convert to title case
5. Swap case
"""

text = "Hello World"

# Your code below:
length =  # Get length
uppercase =  # Convert to uppercase
lowercase =  # Convert to lowercase
title_case =  # Convert to title case
swapped =  # Swap case

print(f"Original: {text}")
print(f"Length: {length}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Title case: {title_case}")
print(f"Swapped: {swapped}")


# =============================================================================
# EXERCISE 6.2: String Search
# =============================================================================
print("\n--- Exercise 6.2: String Search ---")
"""
Find if a substring exists in a string.
Return the index if found, -1 otherwise.
"""

text = "The quick brown fox jumps over the lazy dog"
substring = "fox"

# Your code below:
index =  # Find substring index
found =  # True if found

print(f"Text: {text}")
print(f"Substring: '{substring}'")
print(f"Found: {found}")
if found:
    print(f"Index: {index}")


# =============================================================================
# EXERCISE 6.3: Count Occurrences
# =============================================================================
print("\n--- Exercise 6.3: Count Occurrences ---
"""
Count occurrences of each character in a string (case-insensitive, ignore spaces).
"""

text = "Hello World"

# Your code below:
char_count =  # Dictionary of character counts

print(f"Text: {text}")
for char in sorted(char_count.keys()):
    print(f"  '{char}': {char_count[char]}")


# =============================================================================
# EXERCISE 6.4: Replace Substrings
# =============================================================================
print("\n--- Exercise 6.4: Replace Substrings ---"""
"""
Replace all occurrences of a substring with another.
"""

text = "I love cats. cats are great. cats, cats, cats!"
old = "cats"
new = "dogs"

# Your code below:
replaced =  # Replace old with new
print(f"Original: {text}")
print(f"Replaced: {replaced}")


# =============================================================================
# EXERCISE 6.5: Remove Whitespace
# =============================================================================
print("\n--- Exercise 6.5: Remove Whitespace ---"""
"""
Remove leading, trailing, and all whitespace from a string.
"""

text = "   Hello   World   "

# Your code below:
stripped =  # Remove leading and trailing whitespace
all_whitespace_removed =  # Remove ALL whitespace

print(f"Original: '{text}'")
print(f"Stripped: '{stripped}'")
print(f"No whitespace: '{all_whitespace_removed}'")


# =============================================================================
# EXERCISE 6.6: Split and Join
# =============================================================================
print("\n--- Exercise 6.6: Split and Join ---"""
"""
Given a sentence:
1. Split into words
2. Join with hyphens
3. Join with underscores
"""

text = "hello world this is a test"

# Your code below:
words =  # Split into words
hyphenated =  # Join with hyphens
underscored =  # Join with underscores

print(f"Original: {text}")
print(f"Words: {words}")
print(f"Hyphenated: {hyphenated}")
print(f"Underscored: {underscored}")


# =============================================================================
# EXERCISE 6.7: Check String Properties
# =============================================================================
print("\n--- Exercise 6.7: Check String Properties ---"""
"""
Check if a string is:
- Alphanumeric (letters and numbers only)
- All letters
- All digits
- All lowercase
- All uppercase
"""

strings = ["hello", "HELLO", "12345", "hello123", "Hello123"]

# Your code below:
for s in strings:
    results =  # Dictionary of results
    print(f"'{s}': {results}")


# =============================================================================
# EXERCISE 6.8: Word Count
# =============================================================================
print("\n--- Exercise 6.8: Word Count ---"""
"""
Count words in a sentence.
"""

text = "The quick brown fox jumps over the lazy dog"

# Your code below:
word_count =  # Count words
print(f"Text: {text}")
print(f"Word count: {word_count}")


# =============================================================================
# EXERCISE 6.9: Find Palindromes
# =============================================================================
print("\n--- Exercise 6.9: Find Palindromes ---"""
"""
Check if a string is a palindrome (reads same forwards and backwards).
Ignore case and spaces.
"""

texts = ["racecar", "hello", "A man a plan a canal Panama", "level"]

# Your code below:
for text in texts:
    is_palindrome =  # Check if palindrome
    print(f"'{text}': {'Palindrome' if is_palindrome else 'Not palindrome'}")


# =============================================================================
# EXERCISE 6.10: Format String
# =============================================================================
print("\n--- Exercise 6.10: Format String ---"""
"""
Create a formatted string using f-strings:
- Name
- Age
- City
- Occupation
Format: "Name: {name}, Age: {age}, City: {city}, Job: {occupation}"
"""

name = "Alice"
age = 30
city = "New York"
occupation = "Engineer"

# Your code below:
formatted =  # Format the string
print(formatted)


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 6.1
print("\n--- Solution 6.1 ---")
text = "Hello World"
length = len(text)
uppercase = text.upper()
lowercase = text.lower()
title_case = text.title()
swapped = text.swapcase()

print(f"Original: {text}")
print(f"Length: {length}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Title case: {title_case}")
print(f"Swapped: {swapped}")

# SOLUTION 6.2
print("\n--- Solution 6.2 ---")
text = "The quick brown fox jumps over the lazy dog"
substring = "fox"
found = substring in text
index = text.find(substring) if found else -1

print(f"Text: {text}")
print(f"Substring: '{substring}'")
print(f"Found: {found}")
if found:
    print(f"Index: {index}")

# SOLUTION 6.3
print("\n--- Solution 6.3 ---")
text = "Hello World"
char_count = {}
for char in text.lower():
    if char != " ":
        char_count[char] = char_count.get(char, 0) + 1

print(f"Text: {text}")
for char in sorted(char_count.keys()):
    print(f"  '{char}': {char_count[char]}")

# SOLUTION 6.4
print("\n--- Solution 6.4 ---")
text = "I love cats. cats are great. cats, cats, cats!"
old = "cats"
new = "dogs"
replaced = text.replace(old, new)

print(f"Original: {text}")
print(f"Replaced: {replaced}")

# SOLUTION 6.5
print("\n--- Solution 6.5 ---")
text = "   Hello   World   "
stripped = text.strip()
all_whitespace_removed = text.replace(" ", "")

print(f"Original: '{text}'")
print(f"Stripped: '{stripped}'")
print(f"No whitespace: '{all_whitespace_removed}'")

# SOLUTION 6.6
print("\n--- Solution 6.6 ---")
text = "hello world this is a test"
words = text.split()
hyphenated = "-".join(words)
underscored = "_".join(words)

print(f"Original: {text}")
print(f"Words: {words}")
print(f"Hyphenated: {hyphenated}")
print(f"Underscored: {underscored}")

# SOLUTION 6.7
print("\n--- Solution 6.7 ---")
strings = ["hello", "HELLO", "12345", "hello123", "Hello123"]

for s in strings:
    results = {
        "alphanumeric": s.isalnum(),
        "alpha": s.isalpha(),
        "digit": s.isdigit(),
        "lower": s.islower(),
        "upper": s.isupper()
    }
    print(f"'{s}': {results}")

# SOLUTION 6.8
print("\n--- Solution 6.8 ---")
text = "The quick brown fox jumps over the lazy dog"
word_count = len(text.split())

print(f"Text: {text}")
print(f"Word count: {word_count}")

# SOLUTION 6.9
print("\n--- Solution 6.9 ---")
texts = ["racecar", "hello", "A man a plan a canal Panama", "level"]

for text in texts:
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    is_palindrome = cleaned == cleaned[::-1]
    print(f"'{text}': {'Palindrome' if is_palindrome else 'Not palindrome'}")

# SOLUTION 6.10
print("\n--- Solution 6.10 ---")
name = "Alice"
age = 30
city = "New York"
occupation = "Engineer"

formatted = f"Name: {name}, Age: {age}, City: {city}, Job: {occupation}"
print(formatted)

print("\n" + "=" * 50)
print("Great job! Move on to 07_dictionaries.py")
print("=" * 50)
