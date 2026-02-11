"""
Password Manager - Main Application
====================================
A secure CLI-based password manager with encryption and password generation.
"""

import hashlib
import secrets
import base64
import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional, Tuple


# =============================================================================
# PASSWORD ENTRY
# =============================================================================

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
    
    def __repr__(self) -> str:
        return f"PasswordEntry(service='{self.service}', username='{self.username}')"


# =============================================================================
# PASSWORD GENERATOR
# =============================================================================

class PasswordGenerator:
    """Generate secure random passwords using the secrets module."""
    
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    
    @classmethod
    def generate(cls, length: int = 16, include_upper: bool = True,
                 include_lower: bool = True, include_digits: bool = True,
                 include_special: bool = True) -> str:
        """Generate a secure random password.
        
        Args:
            length: Password length (minimum 8)
            include_upper: Include uppercase letters
            include_lower: Include lowercase letters
            include_digits: Include digits
            include_special: Include special characters
        
        Returns:
            Generated password string
        """
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


# =============================================================================
# PASSWORD STRENGTH CHECKER
# =============================================================================

class PasswordStrengthChecker:
    """Evaluate password strength based on various criteria."""
    
    @staticmethod
    def check(password: str) -> Tuple[str, List[str]]:
        """Check password strength and return rating with feedback.
        
        Args:
            password: Password to check
        
        Returns:
            Tuple of (strength_rating, list_of_suggestions)
        """
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
        else:
            suggestions.append("Use at least 8 characters")
        
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
        
        if len(password) >= 16:
            score += 1
        
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


# =============================================================================
# SIMPLE ENCRYPTION
# =============================================================================

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
        """Encrypt plaintext using XOR cipher with derived key.
        
        Args:
            plaintext: Text to encrypt
            password: Password for key derivation
        
        Returns:
            Base64-encoded encrypted data with salt
        """
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
        """Decrypt ciphertext using XOR cipher with derived key.
        
        Args:
            ciphertext: Base64-encoded encrypted data
            password: Password for key derivation
        
        Returns:
            Decrypted plaintext
        
        Raises:
            ValueError: If decryption fails
        """
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
        except Exception as e:
            raise ValueError("Decryption failed - incorrect password or corrupted data")


# =============================================================================
# VAULT STORAGE
# =============================================================================

class VaultStorage:
    """Handle file I/O for encrypted vault storage."""
    
    def __init__(self, vault_path: str = ".password_vault"):
        self.vault_path = vault_path
    
    def vault_exists(self) -> bool:
        """Check if vault file exists."""
        return os.path.exists(self.vault_path)
    
    def create_vault(self, master_password: str) -> bool:
        """Create a new vault with master password.
        
        Args:
            master_password: Master password for vault
        
        Returns:
            True if successful
        """
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
        """Load and decrypt vault.
        
        Args:
            master_password: Master password for decryption
        
        Returns:
            Vault data dictionary or None if failed
        """
        try:
            with open(self.vault_path, 'r', encoding='utf-8') as f:
                encrypted = f.read()
            
            decrypted = SimpleEncryption.decrypt(encrypted, master_password)
            return json.loads(decrypted)
        except (ValueError, json.JSONDecodeError, FileNotFoundError):
            return None
    
    def save_vault(self, vault_data: Dict, master_password: str) -> bool:
        """Encrypt and save vault.
        
        Args:
            vault_data: Vault data dictionary
            master_password: Master password for encryption
        
        Returns:
            True if successful
        """
        try:
            vault_data["modified"] = datetime.now().isoformat()
            vault_json = json.dumps(vault_data, indent=2)
            encrypted = SimpleEncryption.encrypt(vault_json, master_password)
            
            with open(self.vault_path, 'w', encoding='utf-8') as f:
                f.write(encrypted)
            
            return True
        except Exception:
            return False
    
    def verify_password(self, master_password: str) -> bool:
        """Verify master password by attempting to decrypt vault.
        
        Args:
            master_password: Password to verify
        
        Returns:
            True if password is correct
        """
        return self.load_vault(master_password) is not None


# =============================================================================
# PASSWORD MANAGER
# =============================================================================

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
        print("\nVault unlocked successfully!")
        
        self._main_loop()
    
    def _setup_new_vault(self):
        """Setup a new password vault."""
        print("\n--- Create New Vault ---\n")
        
        while True:
            password = self._get_password("Create master password: ")
            confirm = self._get_password("Confirm master password: ")
            
            if password == confirm:
                if len(password) < 8:
                    print("Password must be at least 8 characters. Try again.")
                    continue
                
                self.master_password = password
                self.storage.create_vault(password)
                print("\nVault created successfully!")
                break
            else:
                print("Passwords don't match. Try again.")
    
    def _unlock_vault(self) -> bool:
        """Unlock existing vault."""
        print("\n--- Unlock Vault ---\n")
        
        attempts = 3
        for i in range(attempts):
            password = self._get_password("Enter master password: ")
            
            if self.storage.verify_password(password):
                self.master_password = password
                vault_data = self.storage.load_vault(password)
                if vault_data is None:
                    return False
                self.entries = [
                    PasswordEntry.from_dict(e) 
                    for e in vault_data.get("entries", [])
                ]
                return True
            else:
                remaining = attempts - i - 1
                print(f"Incorrect password. {remaining} attempts remaining.")
        
        return False
    
    def _save_vault(self):
        """Save current entries to vault."""
        if self.master_password is None:
            raise RuntimeError("Vault is locked")
        vault_data = {
            "version": "1.0",
            "entries": [e.to_dict() for e in self.entries],
            "created": datetime.now().isoformat(),
            "modified": datetime.now().isoformat()
        }
        self.storage.save_vault(vault_data, self.master_password)
    
    def _get_password(self, prompt: str) -> str:
        """Get password input without echo."""
        import getpass
        return getpass.getpass(prompt)
    
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
    
    def _get_choice(self, min_val: int, max_val: int) -> int:
        """Get and validate user choice."""
        while True:
            try:
                choice = int(input(f"\nEnter choice ({min_val}-{max_val}): "))
                if min_val <= choice <= max_val:
                    return choice
                print(f"Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def _main_loop(self):
        """Main application loop."""
        while self.unlocked:
            self._display_menu()
            choice = self._get_choice(1, 10)
            
            if choice == 1:
                self._add_password()
            elif choice == 2:
                self._list_passwords()
            elif choice == 3:
                self._view_password()
            elif choice == 4:
                self._search_passwords()
            elif choice == 5:
                self._generate_password()
            elif choice == 6:
                self._edit_password()
            elif choice == 7:
                self._delete_password()
            elif choice == 8:
                self._check_strength()
            elif choice == 9:
                self._lock_vault()
            elif choice == 10:
                print("\nGoodbye!")
                break
    
    def _add_password(self):
        """Add a new password entry."""
        print("\n--- Add Password ---\n")
        
        service = input("Service name: ").strip()
        if not service:
            print("Service name is required.")
            return
        
        username = input("Username/Email: ").strip()
        if not username:
            print("Username is required.")
            return
        
        password = self._get_password("Password: ")
        if not password:
            print("Password is required.")
            return
        
        use_generated = input("Use generated password? (y/n): ").strip().lower()
        if use_generated == 'y':
            generated = PasswordGenerator.generate()
            print(f"\nGenerated password: {generated}")
            confirm = input("Use this password? (y/n): ").strip().lower()
            if confirm == 'y':
                password = generated
        
        url = input("URL (optional): ").strip()
        notes = input("Notes (optional): ").strip()
        
        entry = PasswordEntry(service, username, password, url, notes)
        self.entries.append(entry)
        self._save_vault()
        print("\nPassword added successfully!")
    
    def _list_passwords(self):
        """List all password entries."""
        print("\n--- All Passwords ---\n")
        
        if not self.entries:
            print("No passwords stored.")
            return
        
        print(f"{'#':<3} {'Service':<20} {'Username':<25} {'URL':<30}")
        print("-" * 80)
        
        for i, entry in enumerate(self.entries, 1):
            url = entry.url[:27] + "..." if len(entry.url) > 27 else entry.url
            print(f"{i:<3} {entry.service:<20} {entry.username:<25} {url:<30}")
    
    def _view_password(self):
        """View a specific password entry."""
        print("\n--- View Password ---\n")
        
        if not self.entries:
            print("No passwords stored.")
            return
        
        self._list_passwords()
        
        try:
            index = int(input("\nEnter entry number: ")) - 1
            if 0 <= index < len(self.entries):
                entry = self.entries[index]
                print("\n" + "=" * 50)
                print(f"Service:    {entry.service}")
                print(f"Username:   {entry.username}")
                print(f"Password:   {entry.password}")
                print(f"URL:        {entry.url or 'N/A'}")
                print(f"Notes:      {entry.notes or 'N/A'}")
                print(f"Created:    {entry.created_date[:10]}")
                print("=" * 50)
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Invalid input.")
    
    def _search_passwords(self):
        """Search password entries."""
        print("\n--- Search Passwords ---\n")
        
        if not self.entries:
            print("No passwords stored.")
            return
        
        keyword = input("Search keyword: ").strip().lower()
        if not keyword:
            print("Keyword is required.")
            return
        
        results = [
            e for e in self.entries
            if keyword in e.service.lower() or 
               keyword in e.username.lower() or
               keyword in e.notes.lower()
        ]
        
        if not results:
            print(f"\nNo results found for '{keyword}'.")
            return
        
        print(f"\nFound {len(results)} result(s):")
        print(f"{'#':<3} {'Service':<20} {'Username':<25}")
        print("-" * 50)
        
        for i, entry in enumerate(results, 1):
            index = self.entries.index(entry) + 1
            print(f"{index:<3} {entry.service:<20} {entry.username:<25}")
    
    def _generate_password(self):
        """Generate and display a secure password."""
        print("\n--- Generate Password ---\n")
        
        try:
            length = int(input("Length (default 16): ") or "16")
        except ValueError:
            length = 16
        
        include_upper = input("Include uppercase? (Y/n): ").strip().lower() != 'n'
        include_lower = input("Include lowercase? (Y/n): ").strip().lower() != 'n'
        include_digits = input("Include digits? (Y/n): ").strip().lower() != 'n'
        include_special = input("Include special chars? (Y/n): ").strip().lower() != 'n'
        
        password = PasswordGenerator.generate(
            length=length,
            include_upper=include_upper,
            include_lower=include_lower,
            include_digits=include_digits,
            include_special=include_special
        )
        
        print(f"\nGenerated password: {password}")
        
        strength, suggestions = PasswordStrengthChecker.check(password)
        print(f"Strength: {strength}")
        
        if suggestions:
            print("Suggestions:")
            for s in suggestions:
                print(f"  - {s}")
    
    def _edit_password(self):
        """Edit an existing password entry."""
        print("\n--- Edit Password ---\n")
        
        if not self.entries:
            print("No passwords stored.")
            return
        
        self._list_passwords()
        
        try:
            index = int(input("\nEnter entry number: ")) - 1
            if 0 <= index < len(self.entries):
                entry = self.entries[index]
                
                print(f"\nEditing: {entry.service} - {entry.username}")
                print("Leave blank to keep current value\n")
                
                new_service = input(f"Service [{entry.service}]: ").strip()
                if new_service:
                    entry.service = new_service
                
                new_username = input(f"Username [{entry.username}]: ").strip()
                if new_username:
                    entry.username = new_username
                
                new_password = self._get_password(f"Password [*****]: ")
                if new_password:
                    entry.password = new_password
                
                new_url = input(f"URL [{entry.url}]: ").strip()
                new_url = "" if new_url == "N/A" else new_url
                if new_url:
                    entry.url = new_url
                
                new_notes = input(f"Notes [{entry.notes}]: ").strip()
                new_notes = "" if new_notes == "N/A" else new_notes
                if new_notes:
                    entry.notes = new_notes
                
                self._save_vault()
                print("\nPassword updated successfully!")
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Invalid input.")
    
    def _delete_password(self):
        """Delete a password entry."""
        print("\n--- Delete Password ---\n")
        
        if not self.entries:
            print("No passwords stored.")
            return
        
        self._list_passwords()
        
        try:
            index = int(input("\nEnter entry number: ")) - 1
            if 0 <= index < len(self.entries):
                entry = self.entries[index]
                print(f"\nDeleting: {entry.service} - {entry.username}")
                confirm = input("Are you sure? (y/N): ").strip().lower()
                
                if confirm == 'y':
                    self.entries.pop(index)
                    self._save_vault()
                    print("Password deleted successfully!")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Invalid input.")
    
    def _check_strength(self):
        """Check password strength."""
        print("\n--- Check Password Strength ---\n")
        
        password = self._get_password("Enter password to check: ")
        
        strength, suggestions = PasswordStrengthChecker.check(password)
        
        print(f"\nPassword Strength: {strength}")
        
        if suggestions:
            print("\nSuggestions to improve:")
            for s in suggestions:
                print(f"  - {s}")
        else:
            print("\nYour password is very strong!")
    
    def _lock_vault(self):
        """Lock the vault and require password to unlock."""
        print("\n--- Lock Vault ---\n")
        self.unlocked = False
        print("Vault locked.")
        
        if not self._unlock_vault():
            print("\nAccess denied. Goodbye!")
            sys.exit(0)


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Main entry point for the password manager."""
    app = PasswordManager()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
