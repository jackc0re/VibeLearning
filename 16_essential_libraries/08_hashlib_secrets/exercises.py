"""
Hashlib & Secrets - Exercises
=============================
Practice problems for hashing and secure random generation.
"""

print("=" * 60)
print("HASHLIB & SECRETS - Exercises")
print("=" * 60)

import hashlib
import secrets
import tempfile
from pathlib import Path

# =============================================================================
# EXERCISE 1: File Integrity Checker
# =============================================================================
print("\n--- Exercise 1: File Integrity Checker ---\n")
"""
Write a function that creates a manifest file containing hashes of all files
in a directory. Then write a function to verify integrity against the manifest.

Manifest format (JSON):
{
    "algorithm": "sha256",
    "files": {
        "file1.txt": "abc123...",
        "file2.txt": "def456..."
    }
}
"""

def create_manifest(directory, output_file, algorithm='sha256'):
    """
    Create a manifest of file hashes for all files in directory.
    """
    # Your code here
    pass  # TODO: Implement

def verify_manifest(directory, manifest_file):
    """
    Verify files against manifest.
    Return (all_ok, list_of_changed_files, list_of_missing_files).
    """
    # Your code here
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 2: Password Generator
# =============================================================================
print("\n--- Exercise 2: Secure Password Generator ---\n")
"""
Write a function that generates secure passwords with:
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character
- Specified minimum length
"""

def generate_password(length=16):
    """
    Generate a secure password meeting complexity requirements.
    """
    # Your code here
    pass  # TODO: Implement

# Test
# for _ in range(5):
#     print(generate_password())

# =============================================================================
# EXERCISE 3: URL Token Generator
# =============================================================================
print("\n--- Exercise 3: URL Token Generator ---\n")
"""
Write a function that generates time-limited, single-use URL tokens.
Tokens should:
- Be URL-safe
- Contain embedded expiration timestamp
- Be verifiable (not tampered with)

Hint: Use HMAC or simple hash of token+secret for verification.
"""

def generate_url_token(data: str, secret: bytes, expiry_hours: int = 24) -> str:
    """
    Generate a signed URL token with expiration.
    """
    # Your code here
    pass  # TODO: Implement

def verify_url_token(token: str, secret: bytes) -> tuple:
    """
    Verify a URL token.
    Return (is_valid, data, is_expired).
    """
    # Your code here
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 4: Deterministic Password
# =============================================================================
print("\n--- Exercise 4: Deterministic Password ---\n")
"""
Write a function that generates a deterministic password from:
- A master password
- A service name
- Optional counter (for password rotation)

Same inputs should always produce the same password.
Useful for password managers (but use proper ones in practice!).
"""

def deterministic_password(master: str, service: str, counter: int = 1, length: int = 16) -> str:
    """
    Generate deterministic password from master + service + counter.
    """
    # Your code here
    pass  # TODO: Implement

# Test
# print(deterministic_password("my_master_pass", "gmail.com"))
# print(deterministic_password("my_master_pass", "gmail.com"))  # Same output
# print(deterministic_password("my_master_pass", "github.com"))  # Different

# =============================================================================
# EXERCISE 5: Salt Generator
# =============================================================================
print("\n--- Exercise 5: Unique Salt Generator ---\n")
"""
Write a function that generates unique salts for password hashing.
Salts should:
- Be unique (no collisions in reasonable number of generations)
- Be appropriate length (16+ bytes)
- Be stored alongside the hash
"""

class SaltManager:
    def __init__(self):
        self.used_salts = set()

    def generate_salt(self, length: int = 16) -> bytes:
        """
        Generate a unique salt.
        """
        # Your code here
        pass  # TODO: Implement

    def is_salt_unique(self, salt: bytes) -> bool:
        """
        Check if salt has been used before.
        """
        # Your code here
        pass  # TODO: Implement

# =============================================================================
# EXERCISE 6: Random Shuffle
# =============================================================================
print("\n--- Exercise 6: Secure Random Shuffle ---\n")
"""
Write a function that shuffles a list using cryptographically secure random.

Hint: Use secrets.randbelow or secrets.choice in Fisher-Yates shuffle.
"""

def secure_shuffle(items: list) -> list:
    """
    Cryptographically secure shuffle of a list.
    Returns new shuffled list (doesn't modify original).
    """
    # Your code here
    pass  # TODO: Implement

# Test
# cards = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']
# print(secure_shuffle(cards))

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# =============================================================================
# SOLUTION 1: File Integrity Checker
# =============================================================================
print("\n--- Solution 1: File Integrity Checker ---\n")

def create_manifest_solution(directory, output_file, algorithm='sha256'):
    directory = Path(directory)
    manifest = {'algorithm': algorithm, 'files': {}}

    for filepath in directory.rglob('*'):
        if filepath.is_file() and filepath.name != output_file:
            h = hashlib.new(algorithm)
            with open(filepath, 'rb') as f:
                while chunk := f.read(8192):
                    h.update(chunk)
            relative_path = str(filepath.relative_to(directory))
            manifest['files'][relative_path] = h.hexdigest()

    with open(output_file, 'w') as f:
        json.dump(manifest, f, indent=2)

    return len(manifest['files'])

def verify_manifest_solution(directory, manifest_file):
    import json

    directory = Path(directory)
    with open(manifest_file) as f:
        manifest = json.load(f)

    algorithm = manifest['algorithm']
    changed = []
    missing = []

    for filepath, expected_hash in manifest['files'].items():
        full_path = directory / filepath

        if not full_path.exists():
            missing.append(filepath)
            continue

        h = hashlib.new(algorithm)
        with open(full_path, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)

        if not secrets.compare_digest(h.hexdigest(), expected_hash):
            changed.append(filepath)

    return (len(changed) == 0 and len(missing) == 0, changed, missing)

# Test
with tempfile.TemporaryDirectory() as tmpdir:
    base = Path(tmpdir)
    (base / 'file1.txt').write_text('content1')
    (base / 'file2.txt').write_text('content2')

    manifest_file = base / 'manifest.json'
    count = create_manifest_solution(base, manifest_file)
    print(f"Created manifest with {count} files")

    ok, changed, missing = verify_manifest_solution(base, manifest_file)
    print(f"Verification: ok={ok}, changed={changed}, missing={missing}")

    # Modify a file
    (base / 'file1.txt').write_text('modified')
    ok, changed, missing = verify_manifest_solution(base, manifest_file)
    print(f"After modification: ok={ok}, changed={changed}")

# =============================================================================
# SOLUTION 2: Password Generator
# =============================================================================
print("\n--- Solution 2: Password Generator ---\n")

def generate_password_solution(length=16):
    if length < 4:
        raise ValueError("Length must be at least 4")

    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special = '!@#$%^&*'

    all_chars = uppercase + lowercase + digits + special

    while True:
        password = ''.join(secrets.choice(all_chars) for _ in range(length))

        # Check requirements
        has_upper = any(c in uppercase for c in password)
        has_lower = any(c in lowercase for c in password)
        has_digit = any(c in digits for c in password)
        has_special = any(c in special for c in password)

        if has_upper and has_lower and has_digit and has_special:
            return password

print("Generated passwords:")
for _ in range(3):
    print(f"  {generate_password_solution()}")

# =============================================================================
# SOLUTION 3: URL Token
# =============================================================================
print("\n--- Solution 3: URL Token Generator ---\n")

import base64
import struct
import time

def generate_url_token_solution(data: str, secret: bytes, expiry_hours: int = 24) -> str:
    expiry = int(time.time()) + (expiry_hours * 3600)

    # Create payload: expiry + data
    payload = struct.pack('>I', expiry) + data.encode()

    # Sign payload
    signature = hashlib.sha256(payload + secret).hexdigest()[:16]

    # Combine and encode
    token = base64.urlsafe_b64encode(payload).decode().rstrip('=') + '.' + signature
    return token

def verify_url_token_solution(token: str, secret: bytes) -> tuple:
    try:
        # Split payload and signature
        payload_b64, signature = token.split('.')

        # Decode payload
        padding = 4 - len(payload_b64) % 4
        if padding != 4:
            payload_b64 += '=' * padding
        payload = base64.urlsafe_b64decode(payload_b64)

        # Verify signature
        expected_sig = hashlib.sha256(payload + secret).hexdigest()[:16]
        if not secrets.compare_digest(signature, expected_sig):
            return (False, None, False)

        # Extract expiry and data
        expiry = struct.unpack('>I', payload[:4])[0]
        data = payload[4:].decode()

        is_expired = time.time() > expiry
        return (True, data, is_expired)
    except Exception:
        return (False, None, False)

secret = secrets.token_bytes(16)
token = generate_url_token_solution("user123", secret, expiry_hours=1)
print(f"Token: {token}")

valid, data, expired = verify_url_token_solution(token, secret)
print(f"Valid: {valid}, Data: {data}, Expired: {expired}")

# Test tampering
tampered = token[:-5] + 'XXXXX'
valid, data, expired = verify_url_token_solution(tampered, secret)
print(f"Tampered token valid: {valid}")

# =============================================================================
# SOLUTION 4: Deterministic Password
# =============================================================================
print("\n--- Solution 4: Deterministic Password ---\n")

def deterministic_password_solution(master: str, service: str, counter: int = 1, length: int = 16) -> str:
    # Combine inputs
    combined = f"{master}:{service}:{counter}"

    # Hash
    hash_obj = hashlib.sha256(combined.encode())
    hash_hex = hash_obj.hexdigest()

    # Convert hash to password characters
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    password = ''

    for i in range(0, len(hash_hex), 2):
        byte = int(hash_hex[i:i+2], 16)
        password += chars[byte % len(chars)]
        if len(password) >= length:
            break

    return password

print("Deterministic passwords:")
print(f"  gmail.com: {deterministic_password_solution('master123', 'gmail.com')}")
print(f"  gmail.com: {deterministic_password_solution('master123', 'gmail.com')}")  # Same
print(f"  github.com: {deterministic_password_solution('master123', 'github.com')}")  # Different

# =============================================================================
# SOLUTION 5: Salt Manager
# =============================================================================
print("\n--- Solution 5: Salt Manager ---\n")

class SaltManagerSolution:
    def __init__(self):
        self.used_salts = set()

    def generate_salt(self, length: int = 16) -> bytes:
        while True:
            salt = secrets.token_bytes(length)
            if salt not in self.used_salts:
                self.used_salts.add(salt)
                return salt

    def is_salt_unique(self, salt: bytes) -> bool:
        return salt not in self.used_salts

manager = SaltManagerSolution()
print("Generated salts:")
for _ in range(3):
    salt = manager.generate_salt()
    print(f"  {salt.hex()}")

# =============================================================================
# SOLUTION 6: Secure Shuffle
# =============================================================================
print("\n--- Solution 6: Secure Shuffle ---\n")

def secure_shuffle_solution(items: list) -> list:
    # Fisher-Yates shuffle with secure random
    result = list(items)  # Don't modify original

    for i in range(len(result) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        result[i], result[j] = result[j], result[i]

    return result

cards = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']
shuffled = secure_shuffle_solution(cards)
print(f"Original: {cards}")
print(f"Shuffled: {shuffled}")

print("\n" + "=" * 60)
print("Exercises complete!")
print("=" * 60)
