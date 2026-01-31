# 🔐 Hashlib & Secrets

> **Hashing and secure random generation**

---

## 🎯 Learning Objectives

By the end of this section, you'll understand:
- How to generate secure hashes with hashlib
- The difference between hashing and encryption
- How to generate secure random numbers and tokens
- Best practices for password handling

---

## 🔑 Hashing vs Encryption

| Hashing | Encryption |
|---------|------------|
| One-way (irreversible) | Two-way (reversible) |
| Same input = same output | Requires a key to decrypt |
| Used for verification | Used for confidentiality |
| Examples: MD5, SHA-256 | Examples: AES, RSA |

### Real-World Analogy

- **Hashing** is like making a smoothie - you can't un-blend it
- **Encryption** is like locking a box - you can unlock it with the key

---

## 📦 Hashlib Module

### Basic Hashing

```python
import hashlib

# Create a hash object
hash_obj = hashlib.sha256()

# Add data (can be called multiple times)
hash_obj.update(b'Hello, World!')

# Get the digest
print(hash_obj.hexdigest())
# dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f
```

### One-line hashing

```python
import hashlib

# Hash a string
digest = hashlib.sha256(b'Hello, World!').hexdigest()

# Hash a file
def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
    return sha256.hexdigest()
```

---

## 🔒 Available Algorithms

| Algorithm | Digest Size | Security |
|-----------|-------------|----------|
| md5 | 128 bits | ❌ Broken |
| sha1 | 160 bits | ❌ Weak |
| sha256 | 256 bits | ✅ Good |
| sha3_256 | 256 bits | ✅ Good |
| blake2b | 512 bits | ✅ Fast & secure |

```python
import hashlib

# List available algorithms
print(hashlib.algorithms_available)

# Recommended for most uses
data = b'important data'
hashlib.sha256(data).hexdigest()
hashlib.sha3_256(data).hexdigest()
```

---

## 🔐 Secrets Module

The `secrets` module is designed for security-sensitive applications.

### Secure Random Numbers

```python
import secrets

# Random integer
secrets.randbelow(100)        # 0 to 99
secrets.randbits(32)          # 32 random bits

# Choice from sequence
secrets.choice(['apple', 'banana', 'cherry'])
```

### Secure Tokens

```python
import secrets

# URL-safe token
secrets.token_urlsafe(16)     # e.g., 'Drmhze6EPcv0fN_81Bj-nA'

# Hex token
secrets.token_hex(16)         # e.g., 'f7b5d5c5d7e8f9a0b1c2d3e4f5a6b7c8'

# Bytes token
secrets.token_bytes(16)       # Random bytes
```

### Token Sizes

| Bytes | Hex Length | URL-Safe Length | Use Case |
|-------|------------|-----------------|----------|
| 16 | 32 | ~22 | Temporary URLs |
| 32 | 64 | ~43 | Session tokens |
| 64 | 128 | ~86 | Long-term secrets |

---

## 🔑 Password Hashing Best Practices

### What NOT to do

```python
import hashlib

# ❌ BAD - Simple hash is vulnerable to rainbow tables
def bad_hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
```

### What TO do (Concept)

```python
# ✅ GOOD - Use proper password hashing library
# In real applications, use: bcrypt, argon2, or scrypt
# These handle salting and stretching automatically

# Example with bcrypt (requires: pip install bcrypt)
import bcrypt

# Hash a password
password = b'super secret'
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

# Verify
bcrypt.checkpw(password, hashed)  # True
```

### Key Points

1. **Always salt** - Random data added to each password
2. **Use slow hashes** - Make brute force expensive
3. **Never use MD5/SHA1** for passwords
4. **Use specialized libraries** - bcrypt, argon2, scrypt

---

## 📁 File Integrity Checking

```python
import hashlib
from pathlib import Path

def calculate_hash(filepath, algorithm='sha256'):
    """Calculate hash of a file."""
    hash_obj = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def verify_file(filepath, expected_hash, algorithm='sha256'):
    """Verify file integrity."""
    actual_hash = calculate_hash(filepath, algorithm)
    return secrets.compare_digest(actual_hash, expected_hash)
    # compare_digest prevents timing attacks
```

---

## ⚠️ Common Mistakes

1. **Using MD5/SHA1 for security** - They're broken for cryptographic purposes
2. **Not using salts** - Rainbow tables can crack unsalted hashes
3. **Using random instead of secrets** - `random` is not cryptographically secure
4. **Hashing passwords with SHA-256** - Too fast, vulnerable to brute force

---

## 📝 Quick Reference

```python
import hashlib
import secrets

# Hashing
digest = hashlib.sha256(b'data').hexdigest()

# Secure random
secrets.token_urlsafe(32)
secrets.randbelow(100)

# File integrity
def file_hash(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

# Compare securely
secrets.compare_digest(hash1, hash2)
```

---

## 🎓 Next Steps

Run `examples.py` to see these in action, then try `exercises.py`!
