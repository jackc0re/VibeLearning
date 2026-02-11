# 🏆 Password Manager Challenges

Extend your password manager with these advanced features.

---

## Challenge 1: Clipboard Integration ⭐

### Goal
Copy passwords directly to clipboard for easy pasting.

### Requirements
1. Add a "Copy Password" menu option
2. Use `pyperclip` library (first external dependency!)
3. Clear clipboard after 30 seconds
4. Show confirmation message when copied

### Implementation Hints

First, you'll need to install pyperclip:
```bash
pip install pyperclip
```

Add to PasswordManager class:
```python
import pyperclip
import time
import threading

def _copy_password(self):
    """Copy password to clipboard with auto-clear."""
    print("\n--- Copy Password ---\n")
    
    if not self.entries:
        print("No passwords stored.")
        return
    
    self._list_passwords()
    
    try:
        index = int(input("\nEnter entry number: ")) - 1
        if 0 <= index < len(self.entries):
            entry = self.entries[index]
            pyperclip.copy(entry.password)
            print(f"\nPassword for {entry.service} copied to clipboard!")
            print("Clipboard will be cleared in 30 seconds...")
            
            # Clear clipboard after 30 seconds
            def clear_clipboard():
                time.sleep(30)
                pyperclip.copy("")
            
            thread = threading.Thread(target=clear_clipboard, daemon=True)
            thread.start()
    except ValueError:
        print("Invalid input.")
```

---

## Challenge 2: Password Categories ⭐⭐

### Goal
Organize passwords into categories (e.g., Social, Work, Finance).

### Requirements
1. Add `category` field to PasswordEntry
2. Create categories: Social, Work, Finance, Shopping, Entertainment, Other
3. Add "List by Category" menu option
4. Filter entries by category

### Implementation Hints

Update PasswordEntry class:
```python
def __init__(self, service: str, username: str, password: str, 
             url: str = "", notes: str = "", category: str = "Other",
             created_date: Optional[str] = None):
    self.service = service
    self.username = username
    self.password = password
    self.url = url
    self.notes = notes
    self.category = category
    self.created_date = created_date or datetime.now().isoformat()

def to_dict(self) -> Dict:
    return {
        "service": self.service,
        "username": self.username,
        "password": self.password,
        "url": self.url,
        "notes": self.notes,
        "category": self.category,
        "created_date": self.created_date
    }
```

Add category selection method:
```python
def _select_category(self) -> str:
    """Display categories and get user selection."""
    categories = ["Social", "Work", "Finance", "Shopping", "Entertainment", "Other"]
    
    print("\nSelect Category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    try:
        choice = int(input("Enter choice: ")) - 1
        if 0 <= choice < len(categories):
            return categories[choice]
    except ValueError:
        pass
    
    return "Other"
```

---

## Challenge 3: Password Expiry Tracking ⭐⭐

### Goal
Track password age and warn about expired passwords.

### Requirements
1. Add `last_modified` field to PasswordEntry
2. Add expiry date configuration (e.g., 90 days)
3. Warn about passwords older than expiry threshold
4. Color-code entries by age (green < 30 days, yellow < 60, red < 90, dark red >= 90)

### Implementation Hints

Update PasswordEntry with last_modified:
```python
def __init__(self, service: str, username: str, password: str, 
             url: str = "", notes: str = "", category: str = "Other",
             created_date: Optional[str] = None, last_modified: Optional[str] = None):
    # ... other fields ...
    self.last_modified = last_modified or datetime.now().isoformat()

def update_password(self, new_password: str):
    """Update password and timestamp."""
    self.password = new_password
    self.last_modified = datetime.now().isoformat()
```

Add age checking method:
```python
def _check_password_age(self, entry: PasswordEntry, expiry_days: int = 90) -> Tuple[int, str]:
    """Check password age and return (days_old, status_color)."""
    last_mod = datetime.fromisoformat(entry.last_modified)
    age_days = (datetime.now() - last_mod).days
    
    if age_days < 30:
        return age_days, "GREEN"
    elif age_days < 60:
        return age_days, "YELLOW"
    elif age_days < expiry_days:
        return age_days, "RED"
    else:
        return age_days, "EXPIRED"

def _show_expired_passwords(self, expiry_days: int = 90):
    """Show all expired or expiring passwords."""
    print(f"\n--- Passwords Older Than {expiry_days} Days ---\n")
    
    expired = []
    for entry in self.entries:
        age, status = self._check_password_age(entry, expiry_days)
        if status == "EXPIRED":
            expired.append((entry, age))
    
    if not expired:
        print("No expired passwords!")
        return
    
    print(f"Found {len(expired)} expired password(s):\n")
    for entry, age in expired:
        print(f"• {entry.service} ({entry.username}) - {age} days old")
```

---

## Challenge 4: Import/Export Functionality ⭐⭐

### Goal
Import passwords from CSV and export to encrypted backup.

### Requirements
1. Export all passwords to CSV file
2. Import passwords from CSV file
3. Create encrypted backup (.bak) files
4. Restore from backup

### Implementation Hints

Add CSV export:
```python
import csv

def _export_to_csv(self, filename: str):
    """Export passwords to CSV file."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Service', 'Username', 'Password', 'URL', 'Notes', 
                           'Category', 'Created', 'Last Modified'])
            
            for entry in self.entries:
                writer.writerow([
                    entry.service,
                    entry.username,
                    entry.password,
                    entry.url,
                    entry.notes,
                    entry.category,
                    entry.created_date,
                    entry.last_modified
                ])
        
        print(f"\nExported {len(self.entries)} passwords to {filename}")
        return True
    except Exception as e:
        print(f"\nExport failed: {e}")
        return False
```

Add CSV import:
```python
def _import_from_csv(self, filename: str):
    """Import passwords from CSV file."""
    try:
        imported = 0
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                entry = PasswordEntry(
                    service=row['Service'],
                    username=row['Username'],
                    password=row['Password'],
                    url=row.get('URL', ''),
                    notes=row.get('Notes', ''),
                    category=row.get('Category', 'Other'),
                    created_date=row.get('Created'),
                    last_modified=row.get('Last Modified')
                )
                self.entries.append(entry)
                imported += 1
        
        self._save_vault()
        print(f"\nImported {imported} passwords from {filename}")
        return True
    except Exception as e:
        print(f"\nImport failed: {e}")
        return False
```

Add encrypted backup:
```python
def _create_backup(self, filename: str):
    """Create encrypted backup of vault."""
    try:
        vault_data = self.storage.load_vault(self.master_password)
        if vault_data:
            encrypted = SimpleEncryption.encrypt(json.dumps(vault_data), self.master_password)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(encrypted)
            
            print(f"\nBackup created: {filename}")
            return True
    except Exception as e:
        print(f"\nBackup failed: {e}")
    return False

def _restore_backup(self, filename: str):
    """Restore vault from encrypted backup."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            encrypted = f.read()
        
        decrypted = SimpleEncryption.decrypt(encrypted, self.master_password)
        vault_data = json.loads(decrypted)
        
        self.entries = [PasswordEntry.from_dict(e) for e in vault_data.get("entries", [])]
        self._save_vault()
        
        print(f"\nRestored vault from {filename}")
        return True
    except Exception as e:
        print(f"\nRestore failed: {e}")
    return False
```

---

## Challenge 5: Two-Factor Authentication (TOTP) ⭐⭐⭐

### Goal
Store TOTP secrets and generate 2FA codes.

### Requirements
1. Add `totp_secret` field to PasswordEntry
2. Generate TOTP codes using HMAC-SHA1
3. Display remaining time until code expires
4. Validate TOTP codes

### Implementation Hints

First, understand TOTP (Time-based One-Time Password):
- Uses HMAC-SHA1 with a secret key
- Code changes every 30 seconds
- Based on current Unix timestamp

```python
import hmac
import struct
import time

class TOTPGenerator:
    """Generate TOTP codes for 2FA."""
    
    @staticmethod
    def generate_totp(secret: str, digits: int = 6, period: int = 30) -> str:
        """Generate TOTP code from base32 secret."""
        import base64
        
        # Remove spaces and padding
        secret = secret.replace(' ', '').replace('=', '')
        
        # Add padding if needed
        while len(secret) % 8 != 0:
            secret += '='
        
        try:
            # Decode base32 secret
            key = base64.b32decode(secret.upper(), casefold=True)
        except Exception:
            raise ValueError("Invalid TOTP secret")
        
        # Calculate time counter
        counter = int(time.time()) // period
        
        # HMAC-SHA1
        hmac_digest = hmac.new(key, struct.pack('>Q', counter), hashlib.sha1).digest()
        
        # Dynamic truncation
        offset = hmac_digest[-1] & 0x0F
        code = struct.unpack('>I', hmac_digest[offset:offset + 4])[0]
        code &= 0x7FFFFFFF
        code %= 10 ** digits
        
        return str(code).zfill(digits)
    
    @staticmethod
    def get_time_remaining(period: int = 30) -> int:
        """Get seconds remaining until next code."""
        return period - (int(time.time()) % period)
    
    @staticmethod
    def generate_secret() -> str:
        """Generate a new random TOTP secret."""
        import base64
        random_bytes = secrets.token_bytes(20)
        return base64.b32encode(random_bytes).decode('utf-8')
```

Add to PasswordEntry:
```python
def __init__(self, ... totp_secret: str = ""):
    # ... other fields ...
    self.totp_secret = totp_secret
```

Add display method:
```python
def _show_totp(self):
    """Show TOTP code for an entry."""
    print("\n--- 2FA Code ---\n")
    
    if not self.entries:
        print("No passwords stored.")
        return
    
    self._list_passwords()
    
    try:
        index = int(input("\nEnter entry number: ")) - 1
        if 0 <= index < len(self.entries):
            entry = self.entries[index]
            
            if not entry.totp_secret:
                print("No 2FA configured for this entry.")
                return
            
            code = TOTPGenerator.generate_totp(entry.totp_secret)
            remaining = TOTPGenerator.get_time_remaining()
            
            print(f"\n{'=' * 40}")
            print(f"Service: {entry.service}")
            print(f"2FA Code: {code}")
            print(f"Expires in: {remaining} seconds")
            print(f"{'=' * 40}")
    except ValueError:
        print("Invalid input.")
```

---

## Challenge 6: Password Health Report ⭐⭐

### Goal
Generate a comprehensive report on password security.

### Requirements
1. Check for duplicate passwords
2. Check for weak passwords
3. Check for reused usernames
4. Show password age distribution
5. Generate overall security score (0-100)

### Implementation Hints

```python
def _generate_health_report(self):
    """Generate and display password health report."""
    print("\n" + "=" * 50)
    print("      PASSWORD HEALTH REPORT")
    print("=" * 50)
    
    if not self.entries:
        print("No passwords to analyze.")
        return
    
    # Check for duplicate passwords
    password_counts = {}
    for entry in self.entries:
        if entry.password in password_counts:
            password_counts[entry.password].append(entry.service)
        else:
            password_counts[entry.password] = [entry.service]
    
    duplicates = {pw: services for pw, services in password_counts.items() if len(services) > 1}
    
    # Check weak passwords
    weak_passwords = []
    for entry in self.entries:
        strength, _ = PasswordStrengthChecker.check(entry.password)
        if strength in ["Very Weak", "Weak"]:
            weak_passwords.append(entry.service)
    
    # Check old passwords
    old_passwords = []
    for entry in self.entries:
        age = (datetime.now() - datetime.fromisoformat(entry.last_modified)).days
        if age > 90:
            old_passwords.append((entry.service, age))
    
    # Calculate score
    score = 100
    score -= len(duplicates) * 10
    score -= len(weak_passwords) * 5
    score -= len(old_passwords) * 3
    score = max(0, score)
    
    # Display report
    print(f"\nTotal Passwords: {len(self.entries)}")
    print(f"Security Score: {score}/100")
    
    if duplicates:
        print(f"\n⚠️  Duplicate Passwords ({len(duplicates)}):")
        for pw, services in duplicates.items():
            print(f"   • {', '.join(services)}")
    
    if weak_passwords:
        print(f"\n⚠️  Weak Passwords ({len(weak_passwords)}):")
        for service in weak_passwords:
            print(f"   • {service}")
    
    if old_passwords:
        print(f"\n⚠️  Old Passwords ({len(old_passwords)}):")
        for service, age in old_passwords:
            print(f"   • {service} ({age} days)")
    
    print("\n" + "=" * 50)
```

---

## Challenge 7: Password Sharing ⭐⭐⭐

### Goal
Generate shareable links with expiration for temporary password access.

### Requirements
1. Create share tokens with expiration time
2. Encrypt shared password separately
3. Generate shareable "links" (base64 tokens)
4. Validate share tokens and decrypt password
5. Track shared passwords

### Implementation Hints

```python
class ShareManager:
    """Manage password sharing with expiration."""
    
    def __init__(self):
        self.shares: Dict[str, Dict] = {}
    
    def create_share(self, password: str, expiry_hours: int = 24) -> str:
        """Create a share token with expiration."""
        token_id = secrets.token_urlsafe(16)
        expires_at = datetime.now() + timedelta(hours=expiry_hours)
        
        # Encrypt the password for sharing
        share_key = secrets.token_bytes(32)
        encrypted = SimpleEncryption.encrypt(password, share_key.hex())
        
        self.shares[token_id] = {
            "encrypted_password": encrypted,
            "key": share_key.hex(),
            "expires_at": expires_at.isoformat()
        }
        
        # Create shareable link
        share_data = {
            "token": token_id,
            "key": share_key.hex()
        }
        
        return base64.b64encode(json.dumps(share_data).encode()).decode()
    
    def get_shared_password(self, share_link: str) -> Optional[str]:
        """Retrieve password from share link."""
        try:
            share_data = json.loads(base64.b64decode(share_link).decode())
            token_id = share_data["token"]
            key = share_data["key"]
            
            if token_id not in self.shares:
                return None
            
            share = self.shares[token_id]
            
            # Check expiration
            expires_at = datetime.fromisoformat(share["expires_at"])
            if datetime.now() > expires_at:
                del self.shares[token_id]
                return None
            
            # Decrypt password
            return SimpleEncryption.decrypt(share["encrypted_password"], key)
        
        except Exception:
            return None
```

---

## Challenge 8: Cloud Storage Integration ⭐⭐⭐

### Goal
Support multiple storage backends (local file, cloud storage).

### Requirements
1. Create storage interface (abstract base class)
2. Implement local file storage (current)
3. Implement cloud storage simulation (using file paths)
4. Allow selecting storage backend
5. Support syncing between multiple devices

### Implementation Hints

```python
from abc import ABC, abstractmethod

class StorageBackend(ABC):
    """Abstract base class for storage backends."""
    
    @abstractmethod
    def exists(self) -> bool:
        """Check if storage exists."""
        pass
    
    @abstractmethod
    def read(self) -> str:
        """Read encrypted data from storage."""
        pass
    
    @abstractmethod
    def write(self, data: str) -> bool:
        """Write encrypted data to storage."""
        pass
    
    @abstractmethod
    def delete(self) -> bool:
        """Delete storage."""
        pass


class LocalFileStorage(StorageBackend):
    """Local file storage backend."""
    
    def __init__(self, path: str):
        self.path = path
    
    def exists(self) -> bool:
        return os.path.exists(self.path)
    
    def read(self) -> str:
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write(self, data: str) -> bool:
        try:
            with open(self.path, 'w', encoding='utf-8') as f:
                f.write(data)
            return True
        except Exception:
            return False
    
    def delete(self) -> bool:
        try:
            os.remove(self.path)
            return True
        except Exception:
            return False


class CloudStorage(StorageBackend):
    """Simulated cloud storage backend."""
    
    def __init__(self, service_name: str, account_id: str):
        self.service_name = service_name
        self.account_id = account_id
        self._data: Dict[str, str] = {}
        self._key = f"{service_name}:{account_id}"
    
    def exists(self) -> bool:
        return self._key in self._data
    
    def read(self) -> str:
        return self._data.get(self._key, "")
    
    def write(self, data: str) -> bool:
        self._data[self._key] = data
        return True
    
    def delete(self) -> bool:
        if self._key in self._data:
            del self._data[self._key]
            return True
        return False
```

Update VaultStorage to use backend:
```python
class VaultStorage:
    """Handle vault storage with configurable backend."""
    
    def __init__(self, backend: Optional[StorageBackend] = None):
        self.backend = backend or LocalFileStorage(".password_vault")
    
    def vault_exists(self) -> bool:
        return self.backend.exists()
    
    def load_vault(self, master_password: str) -> Optional[Dict]:
        try:
            encrypted = self.backend.read()
            decrypted = SimpleEncryption.decrypt(encrypted, master_password)
            return json.loads(decrypted)
        except Exception:
            return None
    
    def save_vault(self, vault_data: Dict, master_password: str) -> bool:
        try:
            vault_json = json.dumps(vault_data, indent=2)
            encrypted = SimpleEncryption.encrypt(vault_json, master_password)
            return self.backend.write(encrypted)
        except Exception:
            return False
```

---

## Challenge 9: Autocomplete/Fuzzy Search ⭐

### Goal
Add fuzzy search for quick password finding.

### Requirements
1. Implement fuzzy string matching
2. Search by service name, username, URL
3. Display search relevance scores
4. Support keyboard shortcuts in CLI

### Implementation Hints

```python
def fuzzy_match(query: str, text: str) -> float:
    """Calculate fuzzy match score (0.0 to 1.0)."""
    query = query.lower()
    text = text.lower()
    
    if query == text:
        return 1.0
    
    if query in text:
        return 0.9
    
    # Calculate character overlap
    query_chars = set(query)
    text_chars = set(text)
    overlap = len(query_chars & text_chars)
    return overlap / len(query_chars) if query_chars else 0.0


def _fuzzy_search(self):
    """Fuzzy search for passwords."""
    print("\n--- Fuzzy Search ---\n")
    
    if not self.entries:
        print("No passwords stored.")
        return
    
    query = input("Search query: ").strip()
    if not query:
        return
    
    results = []
    for entry in self.entries:
        scores = [
            fuzzy_match(query, entry.service),
            fuzzy_match(query, entry.username),
            fuzzy_match(query, entry.url),
            fuzzy_match(query, entry.notes)
        ]
        max_score = max(scores)
        
        if max_score > 0.3:
            results.append((entry, max_score))
    
    results.sort(key=lambda x: x[1], reverse=True)
    
    if not results:
        print(f"No results found for '{query}'.")
        return
    
    print(f"\nFound {len(results)} result(s):\n")
    for entry, score in results[:10]:
        relevance = int(score * 100)
        print(f"• {entry.service} ({entry.username}) - {relevance}% match")
```

---

## Challenge 10: Configuration File ⭐

### Goal
Load settings from configuration file.

### Requirements
1. Create `.pmconfig` file for settings
2. Store default vault path, expiry days, etc.
3. Load config on startup
4. Save config changes

### Implementation Hints

```python
import json

class Config:
    """Configuration manager for password manager."""
    
    DEFAULT_CONFIG = {
        "vault_path": ".password_vault",
        "expiry_days": 90,
        "default_password_length": 16,
        "clipboard_timeout": 30,
        "auto_lock_minutes": 5
    }
    
    def __init__(self, config_path: str = ".pmconfig"):
        self.config_path = config_path
        self.settings = self._load()
    
    def _load(self) -> Dict:
        """Load configuration from file."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    return {**self.DEFAULT_CONFIG, **json.load(f)}
            except Exception:
                pass
        return self.DEFAULT_CONFIG.copy()
    
    def save(self):
        """Save configuration to file."""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, indent=2)
    
    def get(self, key: str, default=None):
        """Get configuration value."""
        return self.settings.get(key, default)
    
    def set(self, key: str, value):
        """Set configuration value."""
        self.settings[key] = value
        self.save()
```

---

## 🎯 Challenge Progress Tracker

Track your completed challenges:

| Challenge | Difficulty | Status |
|-----------|------------|--------|
| Clipboard Integration | ⭐ | ☐ |
| Password Categories | ⭐⭐ | ☐ |
| Password Expiry | ⭐⭐ | ☐ |
| Import/Export | ⭐⭐ | ☐ |
| TOTP 2FA | ⭐⭐⭐ | ☐ |
| Health Report | ⭐⭐ | ☐ |
| Password Sharing | ⭐⭐⭐ | ☐ |
| Cloud Storage | ⭐⭐⭐ | ☐ |
| Fuzzy Search | ⭐ | ☐ |
| Configuration File | ⭐ | ☐ |

---

**Choose a challenge and start coding! 💪**
