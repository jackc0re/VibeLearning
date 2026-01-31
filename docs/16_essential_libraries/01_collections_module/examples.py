"""
Collections Module - Examples
=============================
Demonstrating Counter, defaultdict, namedtuple, and deque.
"""

print("=" * 60)
print("COLLECTIONS MODULE - Examples")
print("=" * 60)

# =============================================================================
# COUNTER - Counting elements easily
# =============================================================================
print("\n--- Counter: Counting Elements ---\n")

from collections import Counter

# Count characters in a string
text = "hello world"
char_count = Counter(text)
print(f"Text: '{text}'")
print(f"Character counts: {dict(char_count)}")

# Count words in a sentence
sentence = "the quick brown fox jumps over the lazy dog the fox was quick"
words = sentence.split()
word_count = Counter(words)
print(f"\nSentence: {sentence}")
print(f"Word counts: {dict(word_count)}")
print(f"Most common words: {word_count.most_common(3)}")

# Counter arithmetic
counter1 = Counter(a=3, b=1)
counter2 = Counter(a=1, b=2, c=3)
print(f"\nCounter 1: {dict(counter1)}")
print(f"Counter 2: {dict(counter2)}")
print(f"Addition: {dict(counter1 + counter2)}")
print(f"Subtraction: {dict(counter1 - counter2)}")

# =============================================================================
# DEFAULTDICT - Automatic default values
# =============================================================================
print("\n--- defaultdict: No More KeyError ---\n")

from collections import defaultdict

# Group items by category
items = [
    ("fruit", "apple"),
    ("vegetable", "carrot"),
    ("fruit", "banana"),
    ("fruit", "cherry"),
    ("vegetable", "spinach"),
]

grouped = defaultdict(list)
for category, item in items:
    grouped[category].append(item)

print("Grouped items:")
for category, items_list in grouped.items():
    print(f"  {category}: {items_list}")

# Counting with defaultdict
letter_counts = defaultdict(int)
for letter in "mississippi":
    letter_counts[letter] += 1

print(f"\nLetter counts: {dict(letter_counts)}")

# =============================================================================
# NAMEDTUPLE - Self-documenting tuples
# =============================================================================
print("\n--- namedtuple: Readable Tuples ---\n")

from collections import namedtuple

# Define a named tuple for a 2D point
Point = namedtuple('Point', ['x', 'y'])

p1 = Point(3, 4)
p2 = Point(0, 0)

print(f"Point 1: x={p1.x}, y={p1.y}")
print(f"Point 2: {p2}")

# Calculate distance (using tuple unpacking)
dx = p1.x - p2.x
dy = p1.y - p2.y
distance = (dx ** 2 + dy ** 2) ** 0.5
print(f"Distance between points: {distance}")

# Using namedtuple for structured data
Person = namedtuple('Person', ['name', 'age', 'city'])
people = [
    Person("Alice", 30, "New York"),
    Person("Bob", 25, "London"),
    Person("Charlie", 35, "Tokyo"),
]

print("\nPeople:")
for person in people:
    print(f"  {person.name}, {person.age} years old, from {person.city}")

# Convert to dictionary
alice_dict = people[0]._asdict()
print(f"\nAs dictionary: {alice_dict}")

# =============================================================================
# DEQUE - Double-ended queue
# =============================================================================
print("\n--- deque: Fast Operations at Both Ends ---\n")

from collections import deque

# Basic operations
d = deque([1, 2, 3])
print(f"Initial deque: {list(d)}")

d.append(4)           # Add to right
print(f"After append(4): {list(d)}")

d.appendleft(0)       # Add to left
print(f"After appendleft(0): {list(d)}")

right = d.pop()       # Remove from right
print(f"Popped from right: {right}, deque: {list(d)}")

left = d.popleft()    # Remove from left
print(f"Popped from left: {left}, deque: {list(d)}")

# Using maxlen for a sliding window (history)
history = deque(maxlen=3)
for i in range(10):
    history.append(i)
    print(f"Added {i}, history (last 3): {list(history)}")

# Rotate elements
d2 = deque([1, 2, 3, 4, 5])
print(f"\nOriginal: {list(d2)}")
d2.rotate(2)          # Rotate right by 2
print(f"After rotate(2): {list(d2)}")
d2.rotate(-2)         # Rotate left by 2
print(f"After rotate(-2): {list(d2)}")

# =============================================================================
# PRACTICAL EXAMPLE: Processing log entries
# =============================================================================
print("\n--- Practical Example: Log Processing ---\n")

# Simulate log entries: (timestamp, level, message)
LogEntry = namedtuple('LogEntry', ['timestamp', 'level', 'message'])

logs = [
    LogEntry("10:00:01", "INFO", "Server started"),
    LogEntry("10:00:05", "ERROR", "Connection failed"),
    LogEntry("10:00:10", "INFO", "Request received"),
    LogEntry("10:00:12", "WARNING", "High memory usage"),
    LogEntry("10:00:15", "ERROR", "Database timeout"),
    LogEntry("10:00:20", "INFO", "Request completed"),
]

# Count log levels
level_counts = Counter(log.level for log in logs)
print(f"Log level counts: {dict(level_counts)}")

# Group logs by level
logs_by_level = defaultdict(list)
for log in logs:
    logs_by_level[log.level].append(log)

print("\nLogs grouped by level:")
for level, entries in sorted(logs_by_level.items()):
    print(f"  {level}: {len(entries)} entries")

# Keep last 3 ERROR logs
error_history = deque(maxlen=3)
for log in logs:
    if log.level == "ERROR":
        error_history.append(log)

print(f"\nLast {len(error_history)} ERROR logs:")
for log in error_history:
    print(f"  [{log.timestamp}] {log.message}")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
