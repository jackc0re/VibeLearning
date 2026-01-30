"""
Regular Expressions - Exercises
===============================
Practice problems for regex.
"""

print("=" * 60)
print("REGULAR EXPRESSIONS - Exercises")
print("=" * 60)

import re

# =============================================================================
# EXERCISE 1: Validate Username
# =============================================================================
print("\n--- Exercise 1: Validate Username ---\n")
"""
Write a function to validate usernames with these rules:
- 3-20 characters long
- Can contain letters, numbers, underscores
- Must start with a letter
"""

def is_valid_username(username):
    """
    Check if username follows the rules.
    """
    # Your code here
    pass  # TODO: Implement

# Test
# test_names = ["user123", "_invalid", "ab", "valid_user", "2start", "way_too_long_username_here"]
# for name in test_names:
#     print(f"{name}: {is_valid_username(name)}")

# =============================================================================
# EXERCISE 2: Extract Hashtags
# =============================================================================
print("\n--- Exercise 2: Extract Hashtags ---\n")
"""
Write a function that extracts all hashtags from a tweet.
Rules:
- Starts with #
- Contains only letters, numbers, underscores
- At least 1 character after #
"""

def extract_hashtags(text):
    """
    Extract all hashtags from text.
    Return list of hashtags (without the #).
    """
    # Your code here
    pass  # TODO: Implement

# Test
# tweet = "Learning #Python and #regex with #Python3! #coding #100DaysOfCode"
# print(extract_hashtags(tweet))

# =============================================================================
# EXERCISE 3: Redact Sensitive Data
# =============================================================================
print("\n--- Exercise 3: Redact Sensitive Data ---\n")
"""
Write a function that redacts sensitive information:
- Credit card numbers: replace with XXXX-XXXX-XXXX-XXXX
- SSNs: replace with XXX-XX-XXXX
- Email addresses: keep domain, mask username (xxx@domain.com)
"""

def redact_sensitive(text):
    """
    Redact credit cards, SSNs, and emails.
    """
    # Your code here
    # Redact credit cards (various formats)
    # Redact SSNs
    # Redact emails
    pass  # TODO: Implement

# Test
# text = "Contact john.doe@email.com or call 555-1234. SSN: 123-45-6789. Card: 1234-5678-9012-3456"
# print(redact_sensitive(text))

# =============================================================================
# EXERCISE 4: Parse CSV Line
# =============================================================================
print("\n--- Exercise 4: Parse CSV Line ---\n")
"""
Write a function that parses a simple CSV line.
Handle quoted fields that may contain commas.

Example:
    'John,30,Engineer' -> ['John', '30', 'Engineer']
    '"Smith, John",30,Engineer' -> ['Smith, John', '30', 'Engineer']
"""

def parse_csv_line(line):
    """
    Parse a CSV line into fields.
    Handle quoted fields with commas.
    """
    # Your code here
    # This is a challenging regex exercise!
    # Hint: Use pattern that matches either quoted fields or unquoted fields
    pass  # TODO: Implement

# Test
# print(parse_csv_line('John,30,Engineer'))
# print(parse_csv_line('"Smith, John",30,"Senior Engineer"'))

# =============================================================================
# EXERCISE 5: Tokenize Math Expression
# =============================================================================
print("\n--- Exercise 5: Tokenize Math Expression ---\n")
"""
Write a function that tokenizes a math expression into:
- Numbers (integers or decimals)
- Operators (+, -, *, /, ^)
- Parentheses
- Variables (letters)

Example: "3.14 * x + (2 - y)" -> ['3.14', '*', 'x', '+', '(', '2', '-', 'y', ')']
"""

def tokenize_expression(expr):
    """
    Tokenize a math expression.
    """
    # Your code here
    pass  # TODO: Implement

# Test
# print(tokenize_expression("3.14 * x + (2 - y)"))
# print(tokenize_expression("(10+20)*3/2"))

# =============================================================================
# EXERCISE 6: Extract URLs
# =============================================================================
print("\n--- Exercise 6: Extract URLs ---\n")
"""
Write a function that extracts all URLs from text.
Support http, https, and www URLs.
"""

def extract_urls(text):
    """
    Extract all URLs from text.
    """
    # Your code here
    pass  # TODO: Implement

# Test
# text = "Visit https://example.com or http://test.org and www.google.com for more"
# print(extract_urls(text))

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# =============================================================================
# SOLUTION 1: Validate Username
# =============================================================================
print("\n--- Solution 1: Validate Username ---\n")

def is_valid_username_solution(username):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$'
    return bool(re.match(pattern, username))

test_names = ["user123", "_invalid", "ab", "valid_user", "2start", "way_too_long_username_here"]
for name in test_names:
    print(f"{name}: {is_valid_username_solution(name)}")

# =============================================================================
# SOLUTION 2: Extract Hashtags
# =============================================================================
print("\n--- Solution 2: Extract Hashtags ---\n")

def extract_hashtags_solution(text):
    pattern = r'#([a-zA-Z0-9_]+)'
    return re.findall(pattern, text)

tweet = "Learning #Python and #regex with #Python3! #coding #100DaysOfCode"
print(f"Hashtags: {extract_hashtags_solution(tweet)}")

# =============================================================================
# SOLUTION 3: Redact Sensitive Data
# =============================================================================
print("\n--- Solution 3: Redact Sensitive Data ---\n")

def redact_sensitive_solution(text):
    # Redact credit cards (16 digits with various separators)
    text = re.sub(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b', 'XXXX-XXXX-XXXX-XXXX', text)

    # Redact SSNs
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', 'XXX-XX-XXXX', text)

    # Redact emails - keep domain
    text = re.sub(r'\b([\w.-]+)@([\w.-]+\.[a-zA-Z]{2,})\b', r'xxx@\2', text)

    return text

text = "Contact john.doe@email.com or bob@company.org. SSN: 123-45-6789. Card: 1234-5678-9012-3456"
print(f"Original: {text}")
print(f"Redacted: {redact_sensitive_solution(text)}")

# =============================================================================
# SOLUTION 4: Parse CSV Line (simplified)
# =============================================================================
print("\n--- Solution 4: Parse CSV Line ---\n")

def parse_csv_line_solution(line):
    # Pattern for quoted or unquoted fields
    pattern = r'"([^"]*)"|([^,]+)'
    matches = re.findall(pattern, line)
    # Extract the non-empty group from each match
    return [quoted if quoted else unquoted for quoted, unquoted in matches]

print(parse_csv_line_solution('John,30,Engineer'))
print(parse_csv_line_solution('"Smith, John",30,"Senior Engineer"'))

# =============================================================================
# SOLUTION 5: Tokenize Math Expression
# =============================================================================
print("\n--- Solution 5: Tokenize Math Expression ---\n")

def tokenize_expression_solution(expr):
    # Remove whitespace
    expr = expr.replace(' ', '')
    # Pattern to match numbers, operators, parentheses, variables
    pattern = r'\d+\.?\d*|[+\-*/^()]|[a-zA-Z]+'
    return re.findall(pattern, expr)

print(tokenize_expression_solution("3.14 * x + (2 - y)"))
print(tokenize_expression_solution("(10+20)*3/2"))

# =============================================================================
# SOLUTION 6: Extract URLs
# =============================================================================
print("\n--- Solution 6: Extract URLs ---\n")

def extract_urls_solution(text):
    # Pattern for http/https/www URLs
    pattern = r'https?://[^\s<>"{}|\\^`\[\]]+|www\.[^\s<>"{}|\\^`\[\]]+'
    return re.findall(pattern, text)

text = "Visit https://example.com/page?query=1 or http://test.org and www.google.com for more"
urls = extract_urls_solution(text)
print(f"Found URLs: {urls}")

print("\n" + "=" * 60)
print("Exercises complete!")
print("=" * 60)
