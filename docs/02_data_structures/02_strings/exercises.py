"""
Strings Deep Dive - Exercises
=============================
Try to solve each exercise before looking at the solution!
Solutions are provided at the bottom of this file.
"""

print("=" * 50)
print("STRINGS DEEP DIVE - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: String Analysis
# =============================================================================
print("\n--- Exercise 1: String Analysis ---\n")
"""
Write a function that takes a string and returns a dictionary with:
- 'length': total length
- 'words': number of words
- 'uppercase': number of uppercase letters
- 'lowercase': number of lowercase letters
- 'digits': number of digits
- 'spaces': number of spaces

Test with: "Hello World 123"
"""

def analyze_string(text):
    # Your code here:
    pass

# Test:
# result = analyze_string("Hello World 123")
# print(result)


# =============================================================================
# EXERCISE 2: Title Case Converter
# =============================================================================
print("\n--- Exercise 2: Title Case Converter ---\n")
"""
Write a function that converts a sentence to title case,
but keeps certain words lowercase (a, an, the, and, or, but, in, on, at)
unless they're the first word.

Example: "the lord of the rings" -> "The Lord of the Rings"
"""

def smart_title(text):
    # Your code here:
    pass

# Test:
# print(smart_title("the lord of the rings"))
# print(smart_title("a tale of two cities"))


# =============================================================================
# EXERCISE 3: Vowel Remover
# =============================================================================
print("\n--- Exercise 3: Vowel Remover ---\n")
"""
Remove all vowels (a, e, i, o, u) from a string.
Make it work for both uppercase and lowercase.

Test with: "Hello World"
Expected: "Hll Wrld"
"""

def remove_vowels(text):
    # Your code here:
    pass

# Test:
# print(remove_vowels("Hello World"))


# =============================================================================
# EXERCISE 4: Anagram Checker
# =============================================================================
print("\n--- Exercise 4: Anagram Checker ---\n")
"""
Write a function that checks if two strings are anagrams.
Anagrams use the same letters in different arrangements.
Ignore spaces and case.

Examples:
- "listen" and "silent" -> True
- "hello" and "world" -> False
- "Astronomer" and "Moon starer" -> True
"""

def is_anagram(str1, str2):
    # Your code here:
    pass

# Test:
# print(is_anagram("listen", "silent"))
# print(is_anagram("Astronomer", "Moon starer"))


# =============================================================================
# EXERCISE 5: String Compression
# =============================================================================
print("\n--- Exercise 5: String Compression ---\n")
"""
Implement basic string compression using counts of repeated characters.
If the compressed string isn't shorter, return the original.

Examples:
- "aabcccccaaa" -> "a2b1c5a3"
- "abcd" -> "abcd" (compressed would be "a1b1c1d1", longer!)
"""

def compress_string(text):
    # Your code here:
    pass

# Test:
# print(compress_string("aabcccccaaa"))
# print(compress_string("abcd"))


# =============================================================================
# EXERCISE 6: Format Phone Number
# =============================================================================
print("\n--- Exercise 6: Format Phone Number ---\n")
"""
Write a function that takes a 10-digit string and formats it
as a phone number: (XXX) XXX-XXXX

If the input is invalid (not 10 digits), return "Invalid"

Examples:
- "1234567890" -> "(123) 456-7890"
- "123456789" -> "Invalid"
- "12345678ab" -> "Invalid"
"""

def format_phone(digits):
    # Your code here:
    pass

# Test:
# print(format_phone("1234567890"))
# print(format_phone("123456789"))


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")
def analyze_string(text):
    return {
        'length': len(text),
        'words': len(text.split()),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower()),
        'digits': sum(1 for c in text if c.isdigit()),
        'spaces': text.count(' ')
    }

result = analyze_string("Hello World 123")
print(f"Analysis of 'Hello World 123':")
for key, value in result.items():
    print(f"  {key}: {value}")

# SOLUTION 2
print("\n--- Solution 2 ---")
def smart_title(text):
    small_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'of'}
    words = text.lower().split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word)
    return ' '.join(result)

print(f"'the lord of the rings' -> '{smart_title('the lord of the rings')}'")
print(f"'a tale of two cities' -> '{smart_title('a tale of two cities')}'")

# SOLUTION 3
print("\n--- Solution 3 ---")
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(c for c in text if c not in vowels)

print(f"'Hello World' -> '{remove_vowels('Hello World')}'")
print(f"'UPPERCASE' -> '{remove_vowels('UPPERCASE')}'")

# SOLUTION 4
print("\n--- Solution 4 ---")
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    clean1 = str1.replace(" ", "").lower()
    clean2 = str2.replace(" ", "").lower()
    # Sort characters and compare
    return sorted(clean1) == sorted(clean2)

print(f"'listen' vs 'silent': {is_anagram('listen', 'silent')}")
print(f"'Astronomer' vs 'Moon starer': {is_anagram('Astronomer', 'Moon starer')}")
print(f"'hello' vs 'world': {is_anagram('hello', 'world')}")

# SOLUTION 5
print("\n--- Solution 5 ---")
def compress_string(text):
    if not text:
        return text
    
    compressed = []
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            compressed.append(text[i-1] + str(count))
            count = 1
    
    # Don't forget the last group
    compressed.append(text[-1] + str(count))
    
    result = ''.join(compressed)
    return result if len(result) < len(text) else text

print(f"'aabcccccaaa' -> '{compress_string('aabcccccaaa')}'")
print(f"'abcd' -> '{compress_string('abcd')}'")
print(f"'aaa' -> '{compress_string('aaa')}'")

# SOLUTION 6
print("\n--- Solution 6 ---")
def format_phone(digits):
    # Remove any non-digit characters first
    clean = ''.join(c for c in digits if c.isdigit())
    
    if len(clean) != 10:
        return "Invalid"
    
    return f"({clean[:3]}) {clean[3:6]}-{clean[6:]}"

print(f"'1234567890' -> '{format_phone('1234567890')}'")
print(f"'123456789' -> '{format_phone('123456789')}'")
print(f"'12345678ab' -> '{format_phone('12345678ab')}'")

print("\n" + "=" * 50)
print("Great job! Move on to 03_dictionaries_maps next.")
print("=" * 50)
