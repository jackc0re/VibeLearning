"""
Strings Deep Dive - Examples
============================
Run this file to see string operations in action!
"""

print("=" * 50)
print("STRINGS DEEP DIVE - Examples")
print("=" * 50)

# =============================================================================
# CREATING STRINGS
# =============================================================================
print("\n--- Creating Strings ---\n")

# Different quote styles
single = 'Hello'
double = "World"
triple = """This is a
multiline string"""

print(f"Single quotes: {single}")
print(f"Double quotes: {double}")
print(f"Triple quotes:\n{triple}")

# Raw strings (for paths, regex, etc.)
path = r"C:\Users\name\folder"
print(f"\nRaw string path: {path}")

# =============================================================================
# INDEXING AND SLICING
# =============================================================================
print("\n--- Indexing and Slicing ---\n")

text = "Python Programming"
print(f"Text: '{text}'")

# Indexing
print(f"\nIndexing:")
print(f"  text[0] = '{text[0]}' (first)")
print(f"  text[-1] = '{text[-1]}' (last)")
print(f"  text[7] = '{text[7]}' (8th character)")

# Slicing
print(f"\nSlicing:")
print(f"  text[0:6] = '{text[0:6]}'")
print(f"  text[7:] = '{text[7:]}'")
print(f"  text[::-1] = '{text[::-1]}' (reversed)")
print(f"  text[::2] = '{text[::2]}' (every 2nd)")

# =============================================================================
# CASE CONVERSION
# =============================================================================
print("\n--- Case Conversion ---\n")

sample = "hello WORLD"
print(f"Original: '{sample}'")
print(f"upper(): '{sample.upper()}'")
print(f"lower(): '{sample.lower()}'")
print(f"title(): '{sample.title()}'")
print(f"capitalize(): '{sample.capitalize()}'")
print(f"swapcase(): '{sample.swapcase()}'")

# =============================================================================
# SEARCHING STRINGS
# =============================================================================
print("\n--- Searching Strings ---\n")

message = "Hello, World! Hello, Python!"
print(f"Text: '{message}'")

print(f"\nfind('Hello'): {message.find('Hello')}")
print(f"find('Hello', 8): {message.find('Hello', 8)}")  # Start from index 8
print(f"find('Java'): {message.find('Java')}")  # -1 if not found

print(f"\ncount('Hello'): {message.count('Hello')}")
print(f"count('l'): {message.count('l')}")

print(f"\nstartswith('Hello'): {message.startswith('Hello')}")
print(f"endswith('!'): {message.endswith('!')}")
print(f"'World' in message: {'World' in message}")

# =============================================================================
# MODIFYING STRINGS
# =============================================================================
print("\n--- Modifying Strings ---\n")

# Replace
text = "Hello, World!"
print(f"Original: '{text}'")
print(f"replace('World', 'Python'): '{text.replace('World', 'Python')}'")

# Strip whitespace
padded = "   some text   "
print(f"\nPadded string: '{padded}'")
print(f"strip(): '{padded.strip()}'")
print(f"lstrip(): '{padded.lstrip()}'")
print(f"rstrip(): '{padded.rstrip()}'")

# Strip specific characters
dashes = "---title---"
print(f"\n'{dashes}'.strip('-'): '{dashes.strip('-')}'")

# =============================================================================
# SPLITTING AND JOINING
# =============================================================================
print("\n--- Splitting and Joining ---\n")

# Split
csv_line = "apple,banana,cherry,date"
print(f"CSV: '{csv_line}'")
fruits = csv_line.split(",")
print(f"split(','): {fruits}")

sentence = "The quick brown fox"
words = sentence.split()  # Split on whitespace
print(f"\n'{sentence}'.split(): {words}")

multiline = "line1\nline2\nline3"
lines = multiline.splitlines()
print(f"\nSplitlines: {lines}")

# Join
print(f"\n' - '.join(fruits): '{' - '.join(fruits)}'")
print(f"''.join(['P','y','t','h','o','n']): '{''.join(['P','y','t','h','o','n'])}'")

# =============================================================================
# F-STRING FORMATTING
# =============================================================================
print("\n--- F-String Formatting ---\n")

name = "Alice"
age = 25
score = 95.567

# Basic
print(f"Name: {name}, Age: {age}")

# Expressions
print(f"Next year: {age + 1}")
print(f"Name length: {len(name)}")

# Width and alignment
print("\nAlignment (10 char width):")
print(f"  Left:   |{name:<10}|")
print(f"  Center: |{name:^10}|")
print(f"  Right:  |{name:>10}|")

# Number formatting
print("\nNumber formatting:")
print(f"  Default: {score}")
print(f"  1 decimal: {score:.1f}")
print(f"  2 decimals: {score:.2f}")

big_number = 1234567890
print(f"  Thousands separator: {big_number:,}")
print(f"  Percentage: {0.8567:.1%}")

# Padding with zeros
num = 42
print(f"  Zero-padded: {num:05d}")

# =============================================================================
# CHECKING STRING CONTENT
# =============================================================================
print("\n--- Checking String Content ---\n")

examples = [
    ("hello", "isalpha()"),
    ("12345", "isdigit()"),
    ("hello123", "isalnum()"),
    ("   ", "isspace()"),
    ("HELLO", "isupper()"),
    ("hello", "islower()"),
    ("Hello World", "istitle()"),
]

for text, method in examples:
    result = eval(f"'{text}'.{method}")
    print(f"'{text}'.{method}: {result}")

# =============================================================================
# COMMON PATTERNS
# =============================================================================
print("\n--- Common Patterns ---\n")

# Reverse a string
text = "Hello, World!"
reversed_text = text[::-1]
print(f"Reversed '{text}': '{reversed_text}'")

# Check palindrome
def is_palindrome(s):
    clean = s.lower().replace(" ", "")
    return clean == clean[::-1]

test_words = ["radar", "hello", "level", "A man a plan a canal Panama"]
print("\nPalindrome check:")
for word in test_words:
    print(f"  '{word}': {is_palindrome(word)}")

# Count words
sentence = "The quick brown fox jumps over the lazy dog"
word_count = len(sentence.split())
print(f"\nWord count in '{sentence}': {word_count}")

# Find all occurrences
text = "banana"
char = "a"
indices = [i for i, c in enumerate(text) if c == char]
print(f"\nAll '{char}' in '{text}': indexes {indices}")

# =============================================================================
# STRING IMMUTABILITY
# =============================================================================
print("\n--- String Immutability ---\n")

original = "Hello"
print(f"Original: '{original}', id: {id(original)}")

# Each operation creates a new string
modified = original + " World"
print(f"After concatenation: '{modified}', id: {id(modified)}")

upper = original.upper()
print(f"After upper(): '{upper}', id: {id(upper)}")

print(f"\nOriginal unchanged: '{original}'")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
