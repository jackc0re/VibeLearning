# 🔐 Project 7: Password Manager

Build a CLI-based password manager with authenticated encryption and password
generation — and learn first-hand why "don't roll your own crypto" is real advice.

---

## 📋 Project Overview

This project helps you practice:
- **hashlib module** — Cryptographic hashing, PBKDF2 key derivation, SHAKE-256 keystreams
- **hmac module** — Tamper detection with encrypt-then-MAC and `compare_digest`
- **secrets module** — Secure random number generation
- **Encryption concepts** — Salt, nonce, keystream, and authentication tags
- **base64 encoding** — Binary-to-text encoding for storage
- **JSON file I/O** — Persistent encrypted storage
- **OOP design** — Multiple classes working together
- **CLI design** — Menu-driven user interface with secure input

### Features to Build

1. ✅ Password Storage
   - Store service, username, password, URL, notes
   - Entry creation and modification dates
   - Search and filter entries

2. ✅ Password Generation
   - Configurable length and character sets
   - Secure random generation using secrets module
   - Options for uppercase, lowercase, digits, special characters

3. ✅ Password Strength Checking
   - Evaluate password strength (Very Weak to Very Strong)
   - Provide improvement suggestions
   - Check multiple criteria (length, character variety)

4. ✅ Vault Encryption
   - Master password protection
   - PBKDF2-HMAC-SHA256 key derivation (100,000 iterations), split into separate encryption and MAC keys
   - SHAKE-256 keystream encryption (key material never repeats within a message)
   - HMAC-SHA256 tamper check, verified with `hmac.compare_digest` before decrypting
   - Base64 encoding for storage

5. ✅ Vault Management
   - Create new vault with master password
   - Lock/unlock vault functionality
   - Persistent encrypted storage in JSON format

6. ✅ CRUD Operations
   - Add new password entries
   - List all passwords
   - View specific entry details
   - Edit existing entries
   - Delete entries with confirmation

---

## 💻 Requirements

### Prerequisites

Complete these modules before starting:
- [00_getting_started](../../00_getting_started/README.md)
- [01_foundations](../../01_foundations/README.md) — especially file I/O
- [02_data_structures](../../02_data_structures/README.md)
- [04_oop_concepts](../../04_oop_concepts/README.md)
- [08_error_handling](../../08_error_handling/README.md)
- [10_file_io](../../10_file_io/README.md) — especially JSON

### Skills You'll Use

- **hashlib** — PBKDF2 key derivation and SHAKE-256 keystreams
- **hmac** — Tamper detection (encrypt-then-MAC, constant-time comparison)
- **secrets** — Cryptographically secure random numbers
- **base64** — Encoding binary data as text
- **Classes** — PasswordEntry, PasswordGenerator, PasswordStrengthChecker, VaultCrypto, VaultStorage, PasswordManager
- **getpass** — Secure password input (no echo)
- **JSON** — Serialization/deserialization of vault data
- **Control Flow** — Menu navigation and validation

---

## 🚀 Development Steps

### Step 1: PasswordEntry Class (15 minutes)

Create a class to represent a single password entry:

```python
from datetime import datetime
from typing import Dict, Optional

class PasswordEntry:
    """Represents a single password entry in the vault."""
    
    def __init__(self, service: str, username: str, password: str, 
                 url: str = "", notes: str = "", created_date: Optional[str] = None):
        self.service = service
        self.username = username
        self.password = password
        self.url = url
        self.notes = notes
        self.created_date = created_date or datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert entry to dictionary for JSON serialization."""
        return {
            "service": self.service,
            "username": self.username,
            "password": self.password,
            "url": self.url,
            "notes": self.notes,
            "created_date": self.created_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'PasswordEntry':
        """Create PasswordEntry from dictionary."""
        return cls(
            service=data["service"],
            username=data["username"],
            password=data["password"],
            url=data.get("url", ""),
            notes=data.get("notes", ""),
            created_date=data.get("created_date")
        )
```

### Step 2: PasswordGenerator Class (20 minutes)

Create a class to generate secure random passwords:

```python
import secrets
from typing import ClassVar

class PasswordGenerator:
    """Generate secure random passwords using the secrets module."""
    
    LOWERCASE: ClassVar[str] = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE: ClassVar[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS: ClassVar[str] = "0123456789"
    SPECIAL: ClassVar[str] = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    
    @classmethod
    def generate(cls, length: int = 16, include_upper: bool = True,
                 include_lower: bool = True, include_digits: bool = True,
                 include_special: bool = True) -> str:
        """Generate a secure random password."""
        if length < 8:
            length = 8
        
        charset = ""
        if include_lower:
            charset += cls.LOWERCASE
        if include_upper:
            charset += cls.UPPERCASE
        if include_digits:
            charset += cls.DIGITS
        if include_special:
            charset += cls.SPECIAL
        
        if not charset:
            charset = cls.LOWERCASE + cls.DIGITS
        
        password = ''.join(secrets.choice(charset) for _ in range(length))
        return password
```

### Step 3: PasswordStrengthChecker Class (20 minutes)

Create a class to evaluate password strength:

```python
from typing import List, Tuple

class PasswordStrengthChecker:
    """Evaluate password strength based on various criteria."""
    
    @staticmethod
    def check(password: str) -> Tuple[str, List[str]]:
        """Check password strength and return rating with feedback."""
        if len(password) < 8:
            return "Very Weak", [
                "Password is too short (minimum 8 characters)"
            ]
        
        suggestions = []
        score = 0
        
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        
        if any(c.islower() for c in password):
            score += 1
        else:
            suggestions.append("Add lowercase letters")
        
        if any(c.isupper() for c in password):
            score += 1
        else:
            suggestions.append("Add uppercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            suggestions.append("Add numbers")
        
        if any(c in PasswordGenerator.SPECIAL for c in password):
            score += 1
        else:
            suggestions.append("Add special characters")
        
        if score >= 6:
            return "Very Strong", suggestions
        elif score >= 5:
            return "Strong", suggestions
        elif score >= 4:
            return "Medium", suggestions
        elif score >= 2:
            return "Weak", suggestions
        else:
            return "Very Weak", suggestions
```

### Step 4: VaultCrypto Class (25 minutes)

Create a class for authenticated encryption and decryption. The stored blob has
the layout `salt(16) | nonce(16) | ciphertext | tag(32)`:

```python
import hashlib
import hmac
import secrets
import base64

class VaultCrypto:
    """Authenticated encryption for the vault, built from hashlib + hmac.

    TEACHING CODE, not a production cipher (see the Security Notes).
    """

    SALT_SIZE = 16
    NONCE_SIZE = 16
    TAG_SIZE = 32
    ITERATIONS = 100000

    @classmethod
    def derive_keys(cls, password: str, salt: bytes) -> tuple:
        """Derive (encryption_key, mac_key) from the master password."""
        block = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), salt, cls.ITERATIONS, dklen=64
        )
        return block[:32], block[32:]

    @classmethod
    def _keystream(cls, key: bytes, nonce: bytes, length: int) -> bytes:
        """Key material exactly as long as the message (SHAKE-256)."""
        return hashlib.shake_256(key + nonce).digest(length)

    @classmethod
    def encrypt(cls, plaintext: str, password: str) -> str:
        """Encrypt plaintext -> base64(salt | nonce | ciphertext | tag)."""
        salt = secrets.token_bytes(cls.SALT_SIZE)
        nonce = secrets.token_bytes(cls.NONCE_SIZE)
        enc_key, mac_key = cls.derive_keys(password, salt)

        plaintext_bytes = plaintext.encode('utf-8')
        stream = cls._keystream(enc_key, nonce, len(plaintext_bytes))
        ciphertext = bytes(a ^ b for a, b in zip(plaintext_bytes, stream))

        tag = hmac.new(mac_key, nonce + ciphertext, 'sha256').digest()
        blob = salt + nonce + ciphertext + tag
        return base64.b64encode(blob).decode('ascii')

    @classmethod
    def decrypt(cls, ciphertext: str, password: str) -> str:
        """Verify the tag first, then decrypt. Raises ValueError on failure."""
        try:
            blob = base64.b64decode(ciphertext.encode('ascii'))
            split = cls.SALT_SIZE + cls.NONCE_SIZE
            if len(blob) < split + cls.TAG_SIZE:
                raise ValueError("truncated blob")

            salt = blob[:cls.SALT_SIZE]
            nonce = blob[cls.SALT_SIZE:split]
            body = blob[split:-cls.TAG_SIZE]
            tag = blob[-cls.TAG_SIZE:]

            enc_key, mac_key = cls.derive_keys(password, salt)
            expected = hmac.new(mac_key, nonce + body, 'sha256').digest()
            if not hmac.compare_digest(tag, expected):
                raise ValueError("authentication failed")

            stream = cls._keystream(enc_key, nonce, len(body))
            return bytes(a ^ b for a, b in zip(body, stream)).decode('utf-8')
        except ValueError as e:
            raise ValueError(
                "Decryption failed - incorrect password or corrupted data"
            ) from e
```

**Why it is built this way** — each piece fixes a real weakness of the naive
"XOR with a repeating key" approach:

| Piece | Weakness it prevents |
|-------|----------------------|
| Fresh random `salt` per save | Same password always producing identical key material |
| Separate MAC key | One key doing two jobs (a classic crypto mistake) |
| SHAKE-256 keystream, message-length | The key **repeating** every 32 bytes — the breakable part of repeating-key XOR |
| HMAC tag checked with `compare_digest` | Tampered files and wrong passwords decrypting to silent garbage |

### Step 5: VaultStorage Class (20 minutes)

Create a class to handle vault file operations:

```python
import json
import os
from typing import Dict, Optional

class VaultStorage:
    """Handle file I/O for encrypted vault storage."""
    
    def __init__(self, vault_path: str = ".password_vault"):
        self.vault_path = vault_path
    
    def vault_exists(self) -> bool:
        """Check if vault file exists."""
        return os.path.exists(self.vault_path)
    
    def create_vault(self, master_password: str) -> bool:
        """Create a new vault with master password."""
        if self.vault_exists():
            return False
        
        vault_data = json.dumps({
            "version": "1.0",
            "entries": [],
            "created": datetime.now().isoformat(),
            "modified": datetime.now().isoformat()
        })
        
        encrypted = SimpleEncryption.encrypt(vault_data, master_password)
        
        with open(self.vault_path, 'w', encoding='utf-8') as f:
            f.write(encrypted)
        
        return True
    
    def load_vault(self, master_password: str) -> Optional[Dict]:
        """Load and decrypt vault."""
        try:
            with open(self.vault_path, 'r', encoding='utf-8') as f:
                encrypted = f.read()
            
            decrypted = SimpleEncryption.decrypt(encrypted, master_password)
            return json.loads(decrypted)
        except (ValueError, json.JSONDecodeError, FileNotFoundError):
            return None
```

### Step 6: PasswordManager Class (45 minutes)

Create the main application class with CLI interface:

```python
import getpass
from typing import List

class PasswordManager:
    """Main CLI password manager application."""
    
    def __init__(self):
        self.storage = VaultStorage()
        self.master_password = None
        self.entries: List[PasswordEntry] = []
        self.unlocked = False
    
    def run(self):
        """Run the password manager application."""
        print("=" * 50)
        print("      PASSWORD MANAGER")
        print("=" * 50)
        
        if not self.storage.vault_exists():
            self._setup_new_vault()
        else:
            if not self._unlock_vault():
                print("\nAccess denied. Goodbye!")
                return
        
        self.unlocked = True
        self._main_loop()
    
    def _display_menu(self):
        """Display main menu."""
        print("\n" + "=" * 50)
        print("           MAIN MENU")
        print("=" * 50)
        print("1. Add Password")
        print("2. List All Passwords")
        print("3. View Password")
        print("4. Search Passwords")
        print("5. Generate Password")
        print("6. Edit Password")
        print("7. Delete Password")
        print("8. Check Password Strength")
        print("9. Lock Vault")
        print("10. Exit")
        print("=" * 50)
```

---

## 🧪 Testing

Test your password manager with these scenarios:

### Basic Operations
1. **Create Vault** — Create new vault with master password
2. **Unlock Vault** — Unlock with correct and incorrect passwords
3. **Add Entry** — Add password with all fields
4. **List Entries** — Display all stored passwords
5. **View Entry** — View specific entry details
6. **Edit Entry** — Modify existing entry
7. **Delete Entry** — Remove entry with confirmation

### Password Generation
1. **Default Generation** — Generate 16-character password
2. **Custom Length** — Generate 8, 12, 24 character passwords
4. **Character Sets** — Test with various combinations

### Password Strength
1. **Weak Password** — Test "password123"
2. **Medium Password** — Test "MyPass#2024"
3. **Strong Password** — Test "xK9#mP2$vL5@nQ8!"
4. **Suggestions** — Check improvement feedback

### Encryption
1. **Vault Persistence** — Close and reopen application
2. **Wrong Password** — Try to unlock with wrong password (fails the HMAC tag check)
3. **Vault Corruption** — Flip a byte in the vault file, then unlock (tag check must reject it)
4. **No Silent Garbage** — A wrong password raises `ValueError`, it never "decrypts" to junk

### Edge Cases
1. **Empty Vault** — Test with no entries
2. **Special Characters** — Test passwords with unicode
3. **Long Entries** — Test with very long notes
4. **Search Results** — Test keyword matching

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How to use hashlib for key derivation (PBKDF2) and keystreams (SHAKE-256)
- ✅ How to use secrets for cryptographically secure random generation
- ✅ Why keys must never repeat and why encryption needs a separate MAC key
- ✅ How encrypt-then-MAC detects tampering with `hmac.compare_digest`
- ✅ How base64 encoding converts binary data to text
- ✅ How to implement password strength checking
- ✅ How to use getpass for secure password input
- ✅ How to design multiple cooperating classes
- ✅ How to create a menu-driven CLI application
- ✅ How to handle encrypted file persistence
- ✅ Why real applications use vetted crypto libraries instead of hand-rolled ciphers

---

## 🏆 Challenges

Complete these challenges to enhance your password manager:

1. **Clipboard Integration** — Copy password to clipboard
2. **Password Categories** — Group passwords by category
3. **Password Expiry** — Track and warn about old passwords
4. **Import/Export** — Import from CSV, export to encrypted backup
5. **Two-Factor Auth** — Store TOTP secrets for 2FA codes
6. **Password Sharing** — Generate share links with expiry
7. **Browser Extension** — Create companion extension for auto-fill
8. **Cross-Platform Sync** — Support cloud storage backends

See [challenges.md](challenges.md) for detailed instructions.

---

## 📁 File Structure

```
07_password_manager/
├── README.md           # This file
├── password_manager.py # Main implementation
└── challenges.md       # Additional challenge tasks
```

---

## 🎨 Sample Output

### Welcome Screen
```
==================================================
      PASSWORD MANAGER
==================================================

--- Create New Vault ---

Create master password: ********
Confirm master password: ********

Vault created successfully!

Vault unlocked successfully!
```

### Main Menu
```
==================================================
           MAIN MENU
==================================================
1. Add Password
2. List All Passwords
3. View Password
4. Search Passwords
5. Generate Password
6. Edit Password
7. Delete Password
8. Check Password Strength
9. Lock Vault
10. Exit
==================================================
```

### List Passwords
```
--- All Passwords ---

#  Service              Username                    URL
--------------------------------------------------------------------------------
1  Gmail                alice@example.com           https://gmail.com
2  GitHub               dev_alice                   https://github.com
3  Netflix              alice.smith@provider.com    https://netflix.com
```

### Generate Password
```
--- Generate Password ---

Length (default 16): 20
Include uppercase? (Y/n): Y
Include lowercase? (Y/n): Y
Include digits? (Y/n): Y
Include special chars? (Y/n): Y

Generated password: 9&xK2$mP4#vL6@nQ8!zR
Strength: Very Strong
```

---

## 🔒 Security Notes

This password manager uses:
- **PBKDF2-HMAC-SHA256** for key derivation (100,000 iterations, 64-byte output
  split into separate encryption and MAC keys)
- **SHAKE-256 keystream** encryption whose key material never repeats within a message
- **HMAC-SHA256 tag** verified with `hmac.compare_digest` before decrypting
  (encrypt-then-MAC), so wrong passwords and tampered files are rejected
- **Cryptographically secure** random values via the secrets module

**⚠️ Important:** This implementation is for **educational purposes only**.
It is a hand-rolled construction assembled to *teach* how the pieces fit
together — which is exactly why it must never guard real passwords. Real
systems are broken by subtle details (side channels, nonce reuse under
failure conditions, key storage) that no tutorial-sized code can get right.

For production use:
- Use a vetted library and its high-level recipes (e.g. the `cryptography`
  package's `Fernet`, which is AES-128-CBC + HMAC-SHA256), not primitives you wired up yourself
- Use a memory-hard KDF (Argon2id, scrypt) instead of PBKDF2 for password *storage*
- Prefer an established password manager over any self-built vault
- The honest takeaway from this project: you now know enough crypto to be
  dangerous — which is precisely when to reach for vetted tools

---

## 📚 Related Topics

| Topic | Location |
|-------|----------|
| Hashlib & Secrets | [16_essential_libraries/08_hashlib_secrets](../../16_essential_libraries/08_hashlib_secrets/README.md) |
| File I/O | [10_file_io](../../10_file_io/README.md) |
| Classes | [04_oop_concepts](../../04_oop_concepts/README.md) |
| Error Handling | [08_error_handling](../../08_error_handling/README.md) |

---

**Ready to start?** Run `python password_manager.py` and begin building! 🚀
