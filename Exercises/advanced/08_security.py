"""
Advanced Exercise 8: Security
=============================
Password hashing with PBKDF2, unguessable session tokens,
strict input validation, and SQL injection prevention with
parameterized queries. No real passwords or secrets are used.
"""

print("=" * 50)
print("EXERCISE 8: Security")
print("=" * 50)


# =============================================================================
# EXERCISE 8.1: Password Hashing
# =============================================================================
print("\n--- Exercise 8.1: Password Hashing ---")
"""
NEVER store a raw password. Store salt + slow hash instead:

- hash_password(password): make a random 16-byte salt with
  secrets.token_bytes, derive a key with hashlib.pbkdf2_hmac
  ("sha256", password, salt, iterations), and return the string
  "salt_hex$hash_hex" so both parts can be stored together
- verify_password(password, stored): split stored, re-derive the
  hash with the SAME salt, and compare with hmac.compare_digest
  (never == - use a constant-time comparison)
"""

import hashlib
import hmac
import secrets


# Your code below:
ITERATIONS = 60_000  # low for a fast demo; real apps use far more


def hash_password(password, iterations=ITERATIONS):
    """Return 'salt_hex$hash_hex' for the password."""
    pass


def verify_password(password, stored, iterations=ITERATIONS):
    """Return True only if password matches the stored hash."""
    pass


# Test (uncomment after implementing)
# stored = hash_password("correct horse battery staple")
# print(verify_password("correct horse battery staple", stored))


# =============================================================================
# EXERCISE 8.2: Secure Tokens (Sessions)
# =============================================================================
print("\n--- Exercise 8.2: Secure Tokens (Sessions) ---")
"""
Session IDs must be unguessable: use secrets.token_urlsafe(32),
never random.random() or a counter.

Write SessionStore:
- create(username) -> a fresh random token, remembered server-side
- validate(token) -> username or None, comparing with
  hmac.compare_digest
- invalidate(token) -> True if a session was removed
The solution then shows a tampered token is rejected.
"""


# Your code below:
class SessionStore:
    """Tracks active sessions keyed by unguessable tokens."""

    pass


# Test (uncomment after implementing)
# store = SessionStore()
# token = store.create("alice")
# print(store.validate(token))  # alice


# =============================================================================
# EXERCISE 8.3: Input Validation
# =============================================================================
print("\n--- Exercise 8.3: Input Validation ---")
"""
Validate at the boundary, fail closed:

- validate_username(name): 3-16 characters, letters/digits/_ only,
  must start with a letter or underscore (re.fullmatch)
- validate_password(pw): at least 10 characters, at least one
  uppercase, one lowercase, one digit, and not on a small
  denylist of common passwords
Both return (ok, reason).
"""

import re


# Your code below:
COMMON_PASSWORDS = {
    "password123", "qwerty12345", "letmein1234", "iloveyou123",
    "admin123456", "welcome123", "monkey12345", "dragon12345",
}


def validate_username(name):
    """Return (ok, reason) for a proposed username."""
    pass


def validate_password(pw):
    """Return (ok, reason) for a proposed password."""
    pass


# Test (uncomment after implementing)
# print(validate_username("ada_99"))
# print(validate_username("9bad"))


# =============================================================================
# EXERCISE 8.4: SQL Injection Prevention
# =============================================================================
print("\n--- Exercise 8.4: SQL Injection Prevention ---")
"""
Build SQL from user input and the input becomes CODE:

- vulnerable_lookup(conn, username): glue the username into the
  query with an f-string (DANGEROUS - for comparison only)
- safe_lookup(conn, username): use a ? placeholder and pass the
  value separately so it is ALWAYS treated as data

The solution seeds an in-memory SQLite table and shows the same
malicious input ("' OR '1'='1") flowing through both functions.
"""

import sqlite3


# Your code below:
def vulnerable_lookup(conn, username):
    """DANGEROUS: builds SQL by gluing strings together."""
    pass


def safe_lookup(conn, username):
    """Safe: the driver treats the value as data, never as SQL."""
    pass


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 8.1
print("\n--- Solution 8.1 ---")


def hash_password(password, iterations=ITERATIONS):
    """Return 'salt_hex$hash_hex' for the password."""
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return f"{salt.hex()}${digest.hex()}"


def verify_password(password, stored, iterations=ITERATIONS):
    """Return True only if password matches the stored hash."""
    salt_hex, digest_hex = stored.split("$", 1)
    salt = bytes.fromhex(salt_hex)
    expected = bytes.fromhex(digest_hex)
    actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return hmac.compare_digest(actual, expected)


stored = hash_password("correct horse battery staple")
print(f"Stored value: {stored[:24]}... (salt_hex$hash_hex)")
right = verify_password("correct horse battery staple", stored)
wrong = verify_password("Tr0ub4dor&3", stored)
print(f"Correct password verifies : {'PASS' if right else 'FAIL'}")
print(f"Wrong password rejected   : {'PASS' if not wrong else 'FAIL'}")
second = hash_password("correct horse battery staple")
print(f"Same password, new salt, different hash: {stored != second}")

# SOLUTION 8.2
print("\n--- Solution 8.2 ---")


class SessionStore:
    """Tracks active sessions keyed by unguessable tokens."""

    def __init__(self):
        self._sessions = {}

    def create(self, username):
        """Issue a fresh unguessable token for username."""
        token = secrets.token_urlsafe(32)
        self._sessions[token] = username
        return token

    def validate(self, token):
        """Return the username for a valid token, else None."""
        for known_token, username in self._sessions.items():
            if hmac.compare_digest(known_token, token):
                return username
        return None

    def invalidate(self, token):
        """Remove a session; True if it existed."""
        return self._sessions.pop(token, None) is not None


store = SessionStore()
token = store.create("alice")
print(f"Issued token: {token[:12]}... ({len(token)} chars, url-safe)")
print(f"Valid token -> {store.validate(token)!r}")
tampered = token[:-2] + "xx"
print(f"Tampered token -> {store.validate(tampered)!r} (rejected)")
print(f"Forged empty token -> {store.validate('')!r} (rejected)")
print(f"Logout worked: {'PASS' if store.invalidate(token) and store.validate(token) is None else 'FAIL'}")

# SOLUTION 8.3
print("\n--- Solution 8.3 ---")

USERNAME_PATTERN = re.compile(r"[A-Za-z_][A-Za-z0-9_]{2,15}")


def validate_username(name):
    """Return (ok, reason) for a proposed username."""
    if not re.fullmatch(USERNAME_PATTERN, name):
        return False, "3-16 chars: letter or _ first, then letters, digits, _"
    return True, "ok"


def validate_password(pw):
    """Return (ok, reason) for a proposed password."""
    if len(pw) < 10:
        return False, "must be at least 10 characters"
    if not re.search(r"[A-Z]", pw):
        return False, "add an uppercase letter"
    if not re.search(r"[a-z]", pw):
        return False, "add a lowercase letter"
    if not re.search(r"[0-9]", pw):
        return False, "add a digit"
    if pw.lower() in COMMON_PASSWORDS:
        return False, "appears on the common-password denylist"
    return True, "ok"


for name in ["ada_99", "9bad", "x"]:
    ok, reason = validate_username(name)
    print(f"  username {name!r:10s} -> {'PASS' if ok else 'blocked'} ({reason})")

for pw in ["Str0ngPassphrase!", "short1A", "Password123"]:
    ok, reason = validate_password(pw)
    print(f"  password {pw!r:20s} -> {'PASS' if ok else 'blocked'} ({reason})")

# SOLUTION 8.4
print("\n--- Solution 8.4 ---")

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (username TEXT, email TEXT)")
conn.executemany(
    "INSERT INTO users VALUES (?, ?)",
    [
        ("alice", "alice@example.com"),
        ("bob", "bob@example.com"),
        ("carol", "carol@example.com"),
    ],
)
conn.commit()


def vulnerable_lookup(conn, username):
    """DANGEROUS: builds SQL by gluing strings together."""
    query = f"SELECT username FROM users WHERE username = '{username}'"
    return [row[0] for row in conn.execute(query).fetchall()]


def safe_lookup(conn, username):
    """Safe: the driver treats the value as data, never as SQL."""
    query = "SELECT username FROM users WHERE username = ?"
    return [row[0] for row in conn.execute(query, (username,)).fetchall()]


normal = "alice"
evil = "' OR '1'='1"

print("Normal input:")
print(f"  vulnerable: {vulnerable_lookup(conn, normal)}")
print(f"  safe      : {safe_lookup(conn, normal)}")
print(f"Injection input: {evil!r}")
print(f"  vulnerable: {vulnerable_lookup(conn, evil)}  <- the string rewrote the query")
print(f"  safe      : {safe_lookup(conn, evil)}  <- treated as a literal username")
safe_rejects = safe_lookup(conn, evil) == []
print(f"Parameterized query blocked the injection: {'PASS' if safe_rejects else 'FAIL'}")
conn.close()

print("\n" + "=" * 50)
print("Great job! You completed every advanced exercise.")
print("=" * 50)
