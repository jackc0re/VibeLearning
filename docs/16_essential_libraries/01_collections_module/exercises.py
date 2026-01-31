"""
Collections Module - Exercises
==============================
Practice problems for Counter, defaultdict, namedtuple, and deque.
"""

print("=" * 60)
print("COLLECTIONS MODULE - Exercises")
print("=" * 60)

from collections import Counter, defaultdict, namedtuple, deque

# =============================================================================
# EXERCISE 1: Word Frequency Analysis
# =============================================================================
print("\n--- Exercise 1: Word Frequency Analysis ---\n")
"""
Given a paragraph of text, find:
1. The 5 most common words
2. How many unique words there are
3. Words that appear exactly 3 times

Text to analyze:
"The quick brown fox jumps over the lazy dog. The dog was not amused.
The fox however was quite proud of his jumping skills."
"""

text = """The quick brown fox jumps over the lazy dog. The dog was not amused.
The fox however was quite proud of his jumping skills."""

# Your code here:
# 1. Normalize (lowercase, remove punctuation)
# 2. Count words
# 3. Find most common, unique count, and words with exactly 3 occurrences

# TODO: Implement your solution

# =============================================================================
# EXERCISE 2: Group Students by Grade
# =============================================================================
print("\n--- Exercise 2: Group Students by Grade ---\n")
"""
Given a list of (student_name, score) tuples, group students by grade:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

Use defaultdict to group them, then print each group.
"""

students = [
    ("Alice", 95),
    ("Bob", 82),
    ("Charlie", 78),
    ("Diana", 91),
    ("Eve", 65),
    ("Frank", 55),
    ("Grace", 88),
    ("Henry", 73),
]

# Your code here:
# Create a function to convert score to grade
# Use defaultdict(list) to group students
# Print each grade group

# TODO: Implement your solution

# =============================================================================
# EXERCISE 3: Inventory Management with namedtuple
# =============================================================================
print("\n--- Exercise 3: Inventory Management ---\n")
"""
Create an inventory system using namedtuple:
- Define an Item namedtuple with: name, quantity, price
- Create a list of items
- Calculate total inventory value
- Find items with quantity below 10 (reorder alert)
"""

# Your code here:
# 1. Define Item namedtuple
# 2. Create inventory list with at least 5 items
# 3. Calculate total value (sum of quantity * price for all items)
# 4. Identify items needing reorder

# TODO: Implement your solution

# =============================================================================
# EXERCISE 4: Palindrome Checker Using Deque
# =============================================================================
print("\n--- Exercise 4: Palindrome Checker Using Deque ---\n")
"""
Use a deque to check if a string is a palindrome.
A palindrome reads the same forwards and backwards (e.g., "radar", "level").

Strategy:
- Add characters to deque
- Pop from both ends and compare
- If all match, it's a palindrome
"""

def is_palindrome(text):
    """
    Check if text is a palindrome using deque.
    Ignore case and non-alphanumeric characters.
    """
    # Your code here
    # 1. Create deque
    # 2. Add only alphanumeric characters (lowercase)
    # 3. Compare from both ends
    # 4. Return True if palindrome, False otherwise
    pass  # TODO: Implement

# Test cases
test_strings = ["radar", "hello", "A man a plan a canal Panama", "Was it a car or a cat I saw"]

# TODO: Test your function

# =============================================================================
# EXERCISE 5: Sliding Window Maximum
# =============================================================================
print("\n--- Exercise 5: Sliding Window Maximum ---\n")
"""
Given a list of numbers and a window size k, find the maximum in each
contiguous subarray (window) of size k as it slides through the list.

Example: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Windows: [1,3,-1], [3,-1,-3], [-1,-3,5], [-3,5,3], [5,3,6], [3,6,7]
Maximums: [3, 3, 5, 5, 6, 7]

Use deque to efficiently solve this problem.
"""

def sliding_window_maximum(nums, k):
    """
    Find maximum in each window of size k.
    Use deque to store indices of useful elements.
    """
    # Your code here
    # Hint: Use deque to store indices of elements in decreasing order
    # Remove elements outside the current window
    # The front of deque is always the maximum for current window
    pass  # TODO: Implement

# Test
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# TODO: Test your function

# =============================================================================
# EXERCISE 6: Anagram Groups
# =============================================================================
print("\n--- Exercise 6: Anagram Groups ---\n")
"""
Group a list of words by their anagrams.
Anagrams are words with the same letters (e.g., "listen", "silent").

Use defaultdict to group words that are anagrams of each other.
"""

words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "cat"]

# Your code here:
# 1. Create function to generate a key for anagrams (sorted letters)
# 2. Use defaultdict to group words by their sorted letter key
# 3. Print groups with more than 1 word

# TODO: Implement your solution

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# =============================================================================
# SOLUTION 1: Word Frequency Analysis
# =============================================================================
print("\n--- Solution 1: Word Frequency Analysis ---\n")

text = """The quick brown fox jumps over the lazy dog. The dog was not amused.
The fox however was quite proud of his jumping skills."""

# Normalize text
import string
cleaned = text.lower()
for char in string.punctuation:
    cleaned = cleaned.replace(char, "")

words = cleaned.split()
word_counts = Counter(words)

print(f"Total words: {len(words)}")
print(f"Unique words: {len(word_counts)}")
print(f"Top 5 most common: {word_counts.most_common(5)}")
print(f"Words appearing exactly 3 times: {[w for w, c in word_counts.items() if c == 3]}")

# =============================================================================
# SOLUTION 2: Group Students by Grade
# =============================================================================
print("\n--- Solution 2: Group Students by Grade ---\n")

students = [
    ("Alice", 95),
    ("Bob", 82),
    ("Charlie", 78),
    ("Diana", 91),
    ("Eve", 65),
    ("Frank", 55),
    ("Grace", 88),
    ("Henry", 73),
]

def score_to_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

by_grade = defaultdict(list)
for name, score in students:
    grade = score_to_grade(score)
    by_grade[grade].append((name, score))

for grade in ["A", "B", "C", "D", "F"]:
    if grade in by_grade:
        print(f"Grade {grade}:")
        for name, score in by_grade[grade]:
            print(f"  {name}: {score}")

# =============================================================================
# SOLUTION 3: Inventory Management
# =============================================================================
print("\n--- Solution 3: Inventory Management ---\n")

Item = namedtuple('Item', ['name', 'quantity', 'price'])

inventory = [
    Item("Laptop", 15, 999.99),
    Item("Mouse", 50, 25.99),
    Item("Keyboard", 8, 79.99),
    Item("Monitor", 5, 299.99),
    Item("USB Cable", 200, 9.99),
    Item("Webcam", 3, 89.99),
]

total_value = sum(item.quantity * item.price for item in inventory)
print(f"Total inventory value: ${total_value:.2f}")

print("\nItems needing reorder (quantity < 10):")
for item in inventory:
    if item.quantity < 10:
        print(f"  {item.name}: {item.quantity} in stock")

# =============================================================================
# SOLUTION 4: Palindrome Checker
# =============================================================================
print("\n--- Solution 4: Palindrome Checker ---\n")

def is_palindrome_solution(text):
    d = deque()
    for char in text.lower():
        if char.isalnum():
            d.append(char)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

test_strings = ["radar", "hello", "A man a plan a canal Panama", "Was it a car or a cat I saw"]
for s in test_strings:
    result = is_palindrome_solution(s)
    print(f"'{s}' -> {result}")

# =============================================================================
# SOLUTION 5: Sliding Window Maximum
# =============================================================================
print("\n--- Solution 5: Sliding Window Maximum ---\n")

def sliding_window_maximum_solution(nums, k):
    from collections import deque
    result = []
    dq = deque()  # Store indices

    for i, num in enumerate(nums):
        # Remove indices that are out of the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices of elements smaller than current
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Add to result once window is full
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sliding_window_maximum_solution(nums, k)
print(f"Input: {nums}")
print(f"Window size: {k}")
print(f"Maximums: {result}")

# =============================================================================
# SOLUTION 6: Anagram Groups
# =============================================================================
print("\n--- Solution 6: Anagram Groups ---\n")

words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "cat"]

anagram_groups = defaultdict(list)
for word in words:
    key = "".join(sorted(word))
    anagram_groups[key].append(word)

print("Anagram groups:")
for key, group in anagram_groups.items():
    if len(group) > 1:
        print(f"  {group}")

print("\n" + "=" * 60)
print("Exercises complete!")
print("=" * 60)
