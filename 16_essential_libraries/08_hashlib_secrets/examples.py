"""
Hashlib & Secrets - Examples
============================
Hashing and secure random generation.
"""

print("=" * 60)
print("HASHLIB & SECRETS - Examples")
print("=" * 60)

import hashlib
import secrets
import tempfile
from pathlib import Path

# =============================================================================
# BASIC HASHING
# =============================================================================
print("\n--- Basic Hashing ---\n")

# Simple string hash
data = b"Hello, World!"
hash_result = hashlib.sha256(data).hexdigest()
print(f"Data: {data}")
print(f"SHA-256: {hash_result}")
print(f"Length: {len(hash_result)} characters")

# Different algorithms
print("\nSame data, different algorithms:")
algorithms = ['md5', 'sha1', 'sha256', 'sha512']
for algo in algorithms:
    h = hashlib.new(algo)
    h.update(data)
    print(f"  {algo:8}: {h.hexdigest()[:32]}...")

# Update in parts
print("\nUpdating hash in parts:")
hash_obj = hashlib.sha256()
hash_obj.update(b"Hello, ")
hash_obj.update(b"World!")
print(f"  Same result: {hash_obj.hexdigest() == hash_result}")

# =============================================================================
# FILE HASHING
# =============================================================================
print("\n--- File Hashing ---\n")

def hash_file(filepath, algorithm='sha256'):
    """Calculate hash of a file in chunks."""
    hash_obj = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):  # Read 8KB at a time
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# Create test file
with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
    f.write("This is test content for hashing.\n" * 100)
    test_file = f.name

# Hash the file
file_hash = hash_file(test_file)
print(f"File: {test_file}")
print(f"SHA-256: {file_hash}")

# Verify file integrity
def verify_file(filepath, expected_hash):
    """Verify file integrity using constant-time comparison."""
    actual_hash = hash_file(filepath)
    return secrets.compare_digest(actual_hash, expected_hash)

print(f"\nVerification (correct hash): {verify_file(test_file, file_hash)}")
print(f"Verification (wrong hash): {verify_file(test_file, '0' * 64)}")

# Cleanup
Path(test_file).unlink()

# =============================================================================
# SECURE RANDOM GENERATION
# =============================================================================
print("\n--- Secure Random Generation ---\n")

# Random integers
print("Random integers:")
print(f"  randbelow(100): {secrets.randbelow(100)}")
print(f"  randbelow(100): {secrets.randbelow(100)}")
print(f"  randbits(32): {secrets.randbits(32)}")

# Random choice
fruits = ['apple', 'banana', 'cherry', 'date']
print(f"\nRandom choice from {fruits}:")
print(f"  {secrets.choice(fruits)}")

# Secure tokens
print("\nSecure tokens:")
print(f"  URL-safe (16 bytes): {secrets.token_urlsafe(16)}")
print(f"  URL-safe (32 bytes): {secrets.token_urlsafe(32)}")
print(f"  Hex (16 bytes): {secrets.token_hex(16)}")
print(f"  Hex (32 bytes): {secrets.token_hex(32)}")

# Token lengths
print("\nToken lengths:")
for nbytes in [16, 32, 64]:
    urlsafe = secrets.token_urlsafe(nbytes)
    hex_token = secrets.token_hex(nbytes)
    print(f"  {nbytes:2} bytes: urlsafe={len(urlsafe):2}, hex={len(hex_token)}")

# =============================================================================
# PASSWORD TOKEN GENERATION
# =============================================================================
print("\n--- Password Reset Tokens ---\n")

def generate_reset_token():
    """Generate a secure password reset token."""
    return secrets.token_urlsafe(32)

def generate_api_key():
    """Generate a secure API key."""
    return f"ak_{secrets.token_hex(32)}"

token = generate_reset_token()
api_key = generate_api_key()

print(f"Reset token: {token}")
print(f"API key: {api_key}")

# =============================================================================
# PASSWORD HASHING (Conceptual - use bcrypt in production)
# =============================================================================
print("\n--- Password Hashing (Conceptual) ---\n")

# Note: This is for educational purposes only!
# In production, use bcrypt, argon2, or scrypt

def simple_salted_hash(password: str, salt: bytes = None) -> tuple:
    """
    Demonstrate salted hashing concept.
    DO NOT USE IN PRODUCTION - use bcrypt instead!
    """
    if salt is None:
        salt = secrets.token_bytes(16)

    # Combine password and salt
    salted = salt + password.encode()

    # Multiple iterations (stretching)
    hash_obj = hashlib.sha256()
    for _ in range(100000):  # High iteration count
        hash_obj.update(salted)
        salted = hash_obj.digest()

    return salt, hash_obj.hexdigest()

def verify_salted_hash(password: str, salt: bytes, hash_value: str) -> bool:
    """Verify a salted hash."""
    _, new_hash = simple_salted_hash(password, salt)
    return secrets.compare_digest(new_hash, hash_value)

# Example
password = "my_secret_password"
salt, hashed = simple_salted_hash(password)

print(f"Password: {password}")
print(f"Salt: {salt.hex()}")
print(f"Hash: {hashed}")
print(f"\nVerification (correct): {verify_salted_hash(password, salt, hashed)}")
print(f"Verification (wrong): {verify_salted_hash('wrong_password', salt, hashed)}")

print("\n⚠️  Note: Use bcrypt/argon2/scrypt in production, not this!")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n--- Practical Examples ---\n")

# Example 1: Data deduplication
def deduplicate_files(directory):
    """Find duplicate files by hash."""
    hashes = {}
    for filepath in Path(directory).rglob('*'):
        if filepath.is_file():
            h = hash_file(filepath)
            hashes.setdefault(h, []).append(filepath)

    # Return only duplicates
    return {h: paths for h, paths in hashes.items() if len(paths) > 1}

# Example 2: Session token manager
class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id: str) -> str:
        """Create a new session token."""
        token = secrets.token_urlsafe(32)
        self.sessions[token] = {
            'user_id': user_id,
            'created': secrets.randbelow(1000000000)
        }
        return token

    def validate_session(self, token: str) -> bool:
        """Validate a session token."""
        # Use constant-time comparison
        for stored_token in self.sessions:
            if secrets.compare_digest(token, stored_token):
                return True
        return False

manager = SessionManager()
token = manager.create_session("user123")
print(f"Created session token: {token[:20]}...")
print(f"Valid: {manager.validate_session(token)}")
print(f"Invalid: {manager.validate_session('fake_token')}")

# Example 3: CSRF token generation
def generate_csrf_token():
    """Generate a CSRF protection token."""
    return secrets.token_hex(16)

def verify_csrf_token(token, stored_token):
    """Verify CSRF token using constant-time comparison."""
    return secrets.compare_digest(token, stored_token)

csrf = generate_csrf_token()
print(f"\nCSRF token: {csrf}")
print(f"Verification: {verify_csrf_token(csrf, csrf)}")

# Example 4: Lottery / random draw (fair)
participants = ['Alice', 'Bob', 'Carol', 'David', 'Eve']
winner = secrets.choice(participants)
print(f"\nLottery winner from {participants}: {winner}")

# Example 5: Secure temporary filename
def secure_temp_filename(extension='.tmp'):
    """Generate a secure temporary filename."""
    return f"tmp_{secrets.token_hex(8)}{extension}"

print(f"\nSecure temp filenames:")
for _ in range(3):
    print(f"  {secure_temp_filename('.txt')}")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
