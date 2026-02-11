# 🔗 Project 8: URL Shortener

Build a command-line URL shortener that maps long URLs to short, easy-to-share codes. Track clicks and manage your shortened links with a simple interface.

---

## 📋 Project Overview

This project helps you practice:
- Hashing and random string generation
- JSON file persistence
- URL validation and parsing
- Data structures for mapping short codes to URLs
- Command-line interface design
- Statistics tracking

### Features to Build

1. ✅ **Short Code Generation**
   - Generate unique 6-character short codes
   - Use Base62 alphabet (a-z, A-Z, 0-9)
   - Collision detection and handling

2. ✅ **URL Storage**
   - Save mappings to JSON file
   - Store original URL, short code, creation date
   - Track click statistics

3. ✅ **URL Resolution**
   - Look up original URL from short code
   - Validate URLs before shortening
   - Handle non-existent codes gracefully

4. ✅ **Statistics Tracking**
   - Count clicks per shortened URL
   - Track creation dates
   - Display usage analytics

5. ✅ **Management Interface**
   - Shorten new URLs
   - List all shortened URLs
   - View statistics
   - Delete URLs

---

## 💻 Requirements

### Prerequisites

Complete these modules before starting:
- [00_getting_started](../../00_getting_started/README.md)
- [01_foundations](../../01_foundations/README.md)
- [02_data_structures](../../02_data_structures/README.md)
- [10_file_io](../../10_file_io/README.md)

### Skills You'll Use

- **Random Module** — Generate random short codes
- **JSON** — Persist URL mappings to file
- **String Operations** — Validate and manipulate URLs
- **Dictionaries** — Map short codes to URL data
- **Datetime** — Track creation dates
- **Input Validation** — Ensure valid URLs and codes

---

## 🚀 Development Steps

### Step 1: URL Validation (15 minutes)

Create a function to validate URLs:

```python
import re

def is_valid_url(url):
    """Check if a URL is valid.
    
    Args:
        url: String to validate
    
    Returns:
        bool: True if valid URL
    """
    # Basic URL pattern
    pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return bool(pattern.match(url))


def normalize_url(url):
    """Normalize URL by adding protocol if missing."""
    url = url.strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url
```

### Step 2: Short Code Generation (20 minutes)

Create functions to generate unique short codes:

```python
import random
import string

# Base62 characters for short codes
BASE62 = string.ascii_letters + string.digits  # a-z, A-Z, 0-9

def generate_short_code(length=6):
    """Generate a random short code.
    
    Args:
        length: Length of the short code (default 6)
    
    Returns:
        str: Random short code
    """
    return ''.join(random.choices(BASE62, k=length))


def generate_unique_code(existing_codes, length=6, max_attempts=100):
    """Generate a unique short code not in existing codes.
    
    Args:
        existing_codes: Set of already used codes
        length: Length of the short code
        max_attempts: Maximum attempts to find unique code
    
    Returns:
        str: Unique short code or None if failed
    """
    for _ in range(max_attempts):
        code = generate_short_code(length)
        if code not in existing_codes:
            return code
    return None
```

### Step 3: URL Mapping Data Structure (15 minutes)

Design the data structure for storing URL mappings:

```python
from datetime import datetime

def create_url_entry(original_url, short_code):
    """Create a new URL entry.
    
    Args:
        original_url: The long URL to shorten
        short_code: The generated short code
    
    Returns:
        dict: URL entry with metadata
    """
    return {
        "original_url": original_url,
        "short_code": short_code,
        "created_at": datetime.now().isoformat(),
        "clicks": 0,
        "last_accessed": None
    }
```

### Step 4: Storage Manager Class (25 minutes)

Create a class to manage URL persistence:

```python
import json
import os

class URLStorage:
    """Manages URL mappings storage."""
    
    def __init__(self, filename="urls.json"):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(script_dir, filename)
        self.urls = {}  # short_code -> url_entry
        self.load()
    
    def load(self):
        """Load URLs from JSON file."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.urls = data.get("urls", {})
        except FileNotFoundError:
            self.urls = {}
        except json.JSONDecodeError:
            print("Warning: Corrupted data file. Starting fresh.")
            self.urls = {}
    
    def save(self):
        """Save URLs to JSON file."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump({"urls": self.urls}, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def add_url(self, original_url, short_code):
        """Add a new URL mapping."""
        entry = create_url_entry(original_url, short_code)
        self.urls[short_code] = entry
        self.save()
        return entry
    
    def get_url(self, short_code):
        """Get URL entry by short code."""
        return self.urls.get(short_code)
    
    def increment_clicks(self, short_code):
        """Increment click count for a URL."""
        if short_code in self.urls:
            self.urls[short_code]["clicks"] += 1
            self.urls[short_code]["last_accessed"] = datetime.now().isoformat()
            self.save()
    
    def delete_url(self, short_code):
        """Delete a URL mapping."""
        if short_code in self.urls:
            del self.urls[short_code]
            self.save()
            return True
        return False
    
    def get_all_urls(self):
        """Get all URL mappings."""
        return self.urls
    
    def code_exists(self, short_code):
        """Check if a short code already exists."""
        return short_code in self.urls
    
    def get_existing_codes(self):
        """Get set of all existing short codes."""
        return set(self.urls.keys())
```

### Step 5: URL Shortener Class (30 minutes)

Create the main URL shortener class:

```python
class URLShortener:
    """Main URL shortener application."""
    
    def __init__(self):
        self.storage = URLStorage()
    
    def shorten_url(self, original_url):
        """Shorten a URL and return the short code.
        
        Args:
            original_url: The URL to shorten
        
        Returns:
            tuple: (success, result) where result is short_code or error message
        """
        # Normalize URL
        original_url = normalize_url(original_url)
        
        # Validate URL
        if not is_valid_url(original_url):
            return False, "Invalid URL format"
        
        # Check if URL already exists
        for code, entry in self.storage.get_all_urls().items():
            if entry["original_url"] == original_url:
                return True, code
        
        # Generate unique short code
        existing_codes = self.storage.get_existing_codes()
        short_code = generate_unique_code(existing_codes)
        
        if not short_code:
            return False, "Failed to generate unique code"
        
        # Save URL mapping
        self.storage.add_url(original_url, short_code)
        return True, short_code
    
    def resolve_url(self, short_code):
        """Get original URL from short code.
        
        Args:
            short_code: The short code to resolve
        
        Returns:
            tuple: (success, result) where result is URL or error message
        """
        entry = self.storage.get_url(short_code)
        
        if not entry:
            return False, "Short code not found"
        
        # Increment click count
        self.storage.increment_clicks(short_code)
        
        return True, entry["original_url"]
    
    def get_stats(self, short_code=None):
        """Get statistics for a URL or all URLs.
        
        Args:
            short_code: Optional specific code to get stats for
        
        Returns:
            dict or list: Statistics data
        """
        if short_code:
            entry = self.storage.get_url(short_code)
            if entry:
                return entry
            return None
        
        # Return all stats
        return self.storage.get_all_urls()
    
    def delete_url(self, short_code):
        """Delete a shortened URL.
        
        Args:
            short_code: The short code to delete
        
        Returns:
            bool: True if deleted successfully
        """
        return self.storage.delete_url(short_code)
```

### Step 6: User Interface (25 minutes)

Create the menu-driven CLI interface:

```python
class URLShortenerApp:
    """Main application class with CLI interface."""
    
    def __init__(self):
        self.shortener = URLShortener()
    
    def display_welcome(self):
        """Display welcome screen."""
        print("\n" + "=" * 60)
        print("     🔗 WELCOME TO URL SHORTENER 🔗")
        print("=" * 60)
        print("\nShorten long URLs into compact, shareable links!")
        print("Track clicks and manage your links easily.")
        print("\n" + "=" * 60)
    
    def display_menu(self):
        """Display main menu."""
        print("\n" + "=" * 40)
        print("           MAIN MENU")
        print("=" * 40)
        print("1. Shorten URL")
        print("2. Resolve URL (Lookup)")
        print("3. List All URLs")
        print("4. View Statistics")
        print("5. Delete URL")
        print("6. Exit")
        print("=" * 40)
    
    def shorten_url_menu(self):
        """Handle URL shortening."""
        print("\n--- Shorten URL ---")
        url = input("Enter URL to shorten: ").strip()
        
        if not url:
            print("Error: URL cannot be empty")
            return
        
        success, result = self.shortener.shorten_url(url)
        
        if success:
            print(f"\n✅ URL shortened successfully!")
            print(f"Short code: {result}")
            print(f"Short URL: short.url/{result}")
        else:
            print(f"\n❌ Error: {result}")
    
    def resolve_url_menu(self):
        """Handle URL resolution."""
        print("\n--- Resolve URL ---")
        code = input("Enter short code: ").strip()
        
        if not code:
            print("Error: Short code cannot be empty")
            return
        
        success, result = self.shortener.resolve_url(code)
        
        if success:
            print(f"\n✅ Original URL: {result}")
            print(f"Click count updated!")
        else:
            print(f"\n❌ Error: {result}")
    
    def list_urls_menu(self):
        """Display all shortened URLs."""
        urls = self.shortener.get_stats()
        
        if not urls:
            print("\nNo URLs have been shortened yet.")
            return
        
        print("\n" + "=" * 80)
        print(f"{'Short Code':<12} {'Clicks':<8} {'Created':<20} {'Original URL':<30}")
        print("-" * 80)
        
        for code, entry in sorted(urls.items(), key=lambda x: x[1]["created_at"], reverse=True):
            created = entry["created_at"][:16]  # Trim to YYYY-MM-DD HH:MM
            original = entry["original_url"]
            if len(original) > 30:
                original = original[:27] + "..."
            print(f"{code:<12} {entry['clicks']:<8} {created:<20} {original:<30}")
        
        print("=" * 80)
        print(f"Total URLs: {len(urls)}")
    
    def view_stats_menu(self):
        """Display detailed statistics."""
        print("\n--- View Statistics ---")
        code = input("Enter short code (or press Enter for all): ").strip()
        
        if code:
            # Show stats for specific URL
            stats = self.shortener.get_stats(code)
            if stats:
                print(f"\n📊 Statistics for '{code}':")
                print(f"  Original URL: {stats['original_url']}")
                print(f"  Short Code: {stats['short_code']}")
                print(f"  Created: {stats['created_at']}")
                print(f"  Total Clicks: {stats['clicks']}")
                if stats['last_accessed']:
                    print(f"  Last Accessed: {stats['last_accessed']}")
                else:
                    print(f"  Last Accessed: Never")
            else:
                print(f"\n❌ Short code '{code}' not found")
        else:
            # Show overall stats
            urls = self.shortener.get_stats()
            if not urls:
                print("\nNo URLs have been shortened yet.")
                return
            
            total_urls = len(urls)
            total_clicks = sum(u["clicks"] for u in urls.values())
            avg_clicks = total_clicks / total_urls if total_urls > 0 else 0
            
            # Find most clicked
            most_clicked = max(urls.items(), key=lambda x: x[1]["clicks"])
            
            print("\n" + "=" * 50)
            print("              OVERALL STATISTICS")
            print("=" * 50)
            print(f"Total URLs: {total_urls}")
            print(f"Total Clicks: {total_clicks}")
            print(f"Average Clicks per URL: {avg_clicks:.1f}")
            print(f"Most Clicked: {most_clicked[0]} ({most_clicked[1]['clicks']} clicks)")
            print("=" * 50)
    
    def delete_url_menu(self):
        """Handle URL deletion."""
        print("\n--- Delete URL ---")
        code = input("Enter short code to delete: ").strip()
        
        if not code:
            print("Error: Short code cannot be empty")
            return
        
        # Confirm deletion
        entry = self.shortener.get_stats(code)
        if entry:
            print(f"\nURL: {entry['original_url']}")
            confirm = input("Are you sure you want to delete? (yes/no): ").strip().lower()
            
            if confirm == 'yes':
                if self.shortener.delete_url(code):
                    print("\n✅ URL deleted successfully!")
                else:
                    print("\n❌ Error deleting URL")
            else:
                print("\nDeletion cancelled.")
        else:
            print(f"\n❌ Short code '{code}' not found")
    
    def get_choice(self, min_val, max_val):
        """Get valid menu choice."""
        while True:
            try:
                choice = int(input(f"\nEnter choice ({min_val}-{max_val}): "))
                if min_val <= choice <= max_val:
                    return choice
                print(f"Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def run(self):
        """Main application loop."""
        self.display_welcome()
        
        while True:
            self.display_menu()
            choice = self.get_choice(1, 6)
            
            if choice == 1:
                self.shorten_url_menu()
            elif choice == 2:
                self.resolve_url_menu()
            elif choice == 3:
                self.list_urls_menu()
            elif choice == 4:
                self.view_stats_menu()
            elif choice == 5:
                self.delete_url_menu()
            elif choice == 6:
                print("\nThanks for using URL Shortener! Goodbye!")
                break


def main():
    """Entry point for the URL shortener."""
    try:
        app = URLShortenerApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!")


if __name__ == "__main__":
    main()
```

---

## 🧪 Testing

Test your URL shortener with these scenarios:

1. **Basic Shortening**
   - Shorten a valid URL (e.g., `https://www.example.com`)
   - Verify short code is generated
   - Check that the same URL returns the same code

2. **URL Resolution**
   - Resolve a valid short code
   - Verify click count increments
   - Try resolving non-existent code

3. **URL Validation**
   - Test with invalid URLs (missing protocol, bad format)
   - Test URLs without protocol (should auto-add https://)
   - Test edge cases (empty string, spaces)

4. **Statistics**
   - View stats for single URL
   - View overall statistics
   - Verify click tracking works

5. **Deletion**
   - Delete an existing URL
   - Try deleting non-existent URL
   - Verify confirmation prompt works

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How to generate random strings with specific character sets
- ✅ How to validate URLs using regular expressions
- ✅ How to persist data using JSON files
- ✅ How to implement collision detection for unique codes
- ✅ How to track statistics over time
- ✅ How to build a menu-driven CLI application

---

## 🏆 Challenges

Complete these challenges to enhance your URL shortener:

1. **Custom Short Codes** — Allow users to specify their own short codes
2. **Expiration Dates** — Add optional expiration dates to URLs
3. **Password Protection** — Protect URLs with passwords
4. **QR Code Generation** — Generate QR codes for shortened URLs (text-based)
5. **Bulk Import/Export** — Import URLs from CSV, export to various formats
6. **URL Preview** — Show page title when resolving (simulated)
7. **Click Analytics** — Track referrers, timestamps for each click
8. **URL Categories** — Organize URLs with tags/categories

See [challenges.md](challenges.md) for detailed instructions.

---

## 📁 File Structure

```
08_url_shortener/
├── README.md              # This file
├── url_shortener.py       # Your main implementation
└── challenges.md          # Additional challenge tasks
```

---

**Ready to start?** Create `url_shortener.py` and begin building! 🚀
