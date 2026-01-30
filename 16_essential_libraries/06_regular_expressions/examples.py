"""
Regular Expressions - Examples
==============================
Pattern matching with the re module.
"""

print("=" * 60)
print("REGULAR EXPRESSIONS - Examples")
print("=" * 60)

import re

# =============================================================================
# BASIC PATTERNS
# =============================================================================
print("\n--- Basic Patterns ---\n")

# Literal matching
text = "The quick brown fox jumps over the lazy dog"
print(f"Text: '{text}'")
print(f"'fox' in text: {bool(re.search(r'fox', text))}")
print(f"'cat' in text: {bool(re.search(r'cat', text))}")

# Dot matches any character
print(f"\n'f.x' matches: {re.findall(r'f.x', text)}")  # fox

# Anchors
print(f"'^The' matches start: {bool(re.search(r'^The', text))}")
print(f"'dog$' matches end: {bool(re.search(r'dog$', text))}")

# Quantifiers
repeat_text = "color colour colouur"
print(f"\n'colou?r' (u optional): {re.findall(r'colou?r', repeat_text)}")
print(f"'colou+r' (1+ u's): {re.findall(r'colou+r', repeat_text)}")
print(f"'colou*r' (0+ u's): {re.findall(r'colou*r', repeat_text)}")

# =============================================================================
# CHARACTER CLASSES
# =============================================================================
print("\n--- Character Classes ---\n")

text = "Room 101: Price $99.50, Code AB-123-XY"

# Digits
print(f"All digits: {re.findall(r'\d', text)}")
print(f"Digit sequences: {re.findall(r'\d+', text)}")

# Words
print(f"\nWord characters: {re.findall(r'\w+', text)}")

# Whitespace
print(f"\nSplit by whitespace: {re.split(r'\s+', text)}")

# Custom classes
print(f"\nUppercase letters: {re.findall(r'[A-Z]', text)}")
print(f"Vowels: {re.findall(r'[aeiou]', text)}")
print(f"Non-vowels: {re.findall(r'[^aeiou\s\d\W]', text)}")  # Just consonants

# =============================================================================
# GROUPS
# =============================================================================
print("\n--- Groups ---\n")

# Basic groups
text = "Name: John Smith, Age: 30"
pattern = r'Name: (\w+) (\w+), Age: (\d+)'
match = re.search(pattern, text)

if match:
    print(f"Full match: {match.group(0)}")
    print(f"First name: {match.group(1)}")
    print(f"Last name: {match.group(2)}")
    print(f"Age: {match.group(3)}")
    print(f"All groups: {match.groups()}")

# Named groups
text = "2024-03-15"
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, text)

if match:
    print(f"\nNamed groups:")
    print(f"  Year: {match.group('year')}")
    print(f"  Month: {match.group('month')}")
    print(f"  Day: {match.group('day')}")
    print(f"  Dict: {match.groupdict()}")

# Non-capturing groups
text = "color colour"
matches = re.findall(r'colou(?:r|rl)', text)  # Matches color, colour
print(f"\nNon-capturing: {matches}")

# =============================================================================
# RE MODULE FUNCTIONS
# =============================================================================
print("\n--- re Module Functions ---\n")

text = "Contact us at support@example.com or sales@company.org"

# findall
emails = re.findall(r'\w+@\w+\.\w+', text)
print(f"All emails: {emails}")

# finditer
print(f"\nUsing finditer:")
for match in re.finditer(r'\w+@\w+\.\w+', text):
    print(f"  {match.group()} at position {match.start()}-{match.end()}")

# sub - replacement
text = "My phone is 123-456-7890 and office is 987-654-3210"
masked = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
print(f"\nOriginal: {text}")
print(f"Masked: {masked}")

# sub with groups
date = "2024-03-15"
us_date = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', date)
print(f"\nISO date: {date}")
print(f"US date: {us_date}")

# split
log = "ERROR:2024-03-15:Connection failed:timeout"
parts = re.split(r':', log)
print(f"\nSplit log: {parts}")

# split with maxsplit
parts = re.split(r':', log, 2)
print(f"Split (max 2): {parts}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n--- Practical Examples ---\n")

# Example 1: Validate email
def is_valid_email(email):
    """Basic email validation."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

test_emails = ["user@example.com", "invalid.email", "test+tag@domain.co.uk"]
print("Email validation:")
for email in test_emails:
    print(f"  {email}: {is_valid_email(email)}")

# Example 2: Extract phone numbers
def extract_phones(text):
    """Extract US phone numbers in various formats."""
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

text = "Call 555-123-4567 or (555) 987-6543, or 555.456.7890"
print(f"\nPhones found: {extract_phones(text)}")

# Example 3: Parse URL
def parse_url(url):
    """Parse URL into components."""
    pattern = r'^(?:(?P<scheme>https?):)?//(?P<host>[^/]+)(?P<path>/.*)?$'
    match = re.match(pattern, url)
    return match.groupdict() if match else None

url = "https://example.com/path/to/page"
print(f"\nParsed URL: {parse_url(url)}")

# Example 4: Password strength check
def check_password(password):
    """Check password strength."""
    checks = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*]', password)),
    }
    score = sum(checks.values())
    return checks, score

passwords = ["weak", "Strong1", "Str0ng!Pass"]
print("\nPassword checks:")
for pwd in passwords:
    checks, score = check_password(pwd)
    print(f"  '{pwd}': {score}/5 - {checks}")

# Example 5: Find and replace markdown links
def convert_markdown_links(text):
    """Convert markdown links to HTML."""
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, r'<a href="\2">\1</a>', text)

md = "Check out [Python](https://python.org) and [GitHub](https://github.com)"
html = convert_markdown_links(md)
print(f"\nMarkdown: {md}")
print(f"HTML: {html}")

# Example 6: Log parser
def parse_log_line(line):
    """Parse Apache-style log line."""
    pattern = r'^(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+)'
    match = re.match(pattern, line)
    return match.groupdict() if match else None

log = '192.168.1.1 - - [15/Mar/2024:10:30:00 +0000] "GET /index.html HTTP/1.1" 200'
parsed = parse_log_line(log)
print(f"\nLog parse:")
for key, value in parsed.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
