# 🔐 Project 7: Password Manager

Build a secure CLI-based password manager with encryption and password generation.

---

## 📋 Project Overview

This project helps you practice:
- **hashlib module** — Cryptographic hashing and key derivation
- **secrets module** — Secure random number generation
- **Encryption concepts** — XOR encryption with PBKDF2 key derivation
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
   - PBKDF2 key derivation (100,000 iterations)
   - XOR cipher for data encryption
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

- **hashlib** — PBKDF2 key derivation for encryption
- **secrets** — Cryptographically secure random numbers
- **base64** — Encoding binary data as text
- **Classes** — PasswordEntry, PasswordGenerator, PasswordStrengthChecker, SimpleEncryption, VaultStorage, PasswordManager
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

### Step 4: SimpleEncryption Class (25 minutes)

Create a class for encryption and decryption:

```python
import hashlib
import secrets
import base64

class SimpleEncryption:
    """Simple XOR encryption with PBKDF2 key derivation."""
    
    SALT_SIZE = 16
    ITERATIONS = 100000
    
    @classmethod
    def derive_key(cls, password: str, salt: bytes) -> bytes:
        """Derive encryption key from password using PBKDF2."""
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, cls.ITERATIONS)
    
    @classmethod
    def encrypt(cls, plaintext: str, password: str) -> str:
        """Encrypt plaintext using XOR cipher with derived key."""
        salt = secrets.token_bytes(cls.SALT_SIZE)
        key = cls.derive_key(password, salt)
        
        plaintext_bytes = plaintext.encode('utf-8')
        encrypted_bytes = bytearray()
        
        for i, byte in enumerate(plaintext_bytes):
            key_byte = key[i % len(key)]
            encrypted_bytes.append(byte ^ key_byte)
        
        combined = salt + bytes(encrypted_bytes)
        return base64.b64encode(combined).decode('utf-8')
    
    @classmethod
    def decrypt(cls, ciphertext: str, password: str) -> str:
        """Decrypt ciphertext using XOR cipher with derived key."""
        try:
            combined = base64.b64decode(ciphertext.encode('utf-8'))
            salt = combined[:cls.SALT_SIZE]
            encrypted_bytes = combined[cls.SALT_SIZE:]
            
            key = cls.derive_key(password, salt)
            
            decrypted_bytes = bytearray()
            for i, byte in enumerate(encrypted_bytes):
                key_byte = key[i % len(key)]
                decrypted_bytes.append(byte ^ key_byte)
            
            return decrypted_bytes.decode('utf-8')
        except Exception:
            raise ValueError("Decryption failed")
```

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
2. **Wrong Password** — Try to unlock with wrong password
3. **Vault Corruption** — Test handling of corrupted vault file

### Edge Cases
1. **Empty Vault** — Test with no entries
2. **Special Characters** — Test passwords with unicode
3. **Long Entries** — Test with very long notes
4. **Search Results** — Test keyword matching

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How to use hashlib for key derivation (PBKDF2)
- ✅ How to use secrets for cryptographically secure random generation
- ✅ How XOR encryption works at a basic level
- ✅ How base64 encoding converts binary data to text
- ✅ How to implement password strength checking
- ✅ How to use getpass for secure password input
- ✅ How to design multiple cooperating classes
- ✅ How to create a menu-driven CLI application
- ✅ How to handle encrypted file persistence

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
- **PBKDF2-HMAC-SHA256** for key derivation (100,000 iterations)
- **XOR cipher** for data encryption (educational purposes)
- **Cryptographically secure** random generation via secrets module

**⚠️ Important:** This implementation is for **educational purposes only**. 
For production use, consider:
- AES-256-GCM instead of XOR cipher
- Argon2id for key derivation (if available)
- Proper memory handling and secure key storage
- Regular security audits

---

## 📚 Related Topics

| Topic | Location |
|-------|----------|
| hashlib | [11_memory_performance/02_hash_functions](../../11_memory_performance/02_hash_functions/) |
| File I/O | [10_file_io](../../10_file_io/README.md) |
| Classes | [04_oop_concepts](../../04_oop_concepts/README.md) |
| Error Handling | [08_error_handling](../../08_error_handling/README.md) |

---

**Ready to start?** Run `python password_manager.py` and begin building! 🚀
