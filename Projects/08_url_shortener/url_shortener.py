"""
URL Shortener Project
=====================
A command-line URL shortener that maps long URLs to short codes.
Features code generation, JSON persistence, click tracking, and statistics.
"""

import json
import os
import random
import re
import string
from datetime import datetime


# =============================================================================
# CONSTANTS AND CONFIGURATION
# =============================================================================

# Base62 characters for short codes (a-z, A-Z, 0-9)
BASE62 = string.ascii_letters + string.digits

# Default short code length
DEFAULT_CODE_LENGTH = 6


# =============================================================================
# URL VALIDATION FUNCTIONS
# =============================================================================

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
    """Normalize URL by adding protocol if missing.
    
    Args:
        url: URL string to normalize
    
    Returns:
        str: Normalized URL with protocol
    """
    url = url.strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url


# =============================================================================
# SHORT CODE GENERATION
# =============================================================================

def generate_short_code(length=DEFAULT_CODE_LENGTH):
    """Generate a random short code.
    
    Args:
        length: Length of the short code (default 6)
    
    Returns:
        str: Random short code
    """
    return ''.join(random.choices(BASE62, k=length))


def generate_unique_code(existing_codes, length=DEFAULT_CODE_LENGTH, max_attempts=100):
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


# =============================================================================
# URL ENTRY CREATION
# =============================================================================

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


# =============================================================================
# URL STORAGE CLASS
# =============================================================================

class URLStorage:
    """Manages URL mappings storage using JSON file."""
    
    def __init__(self, filename="urls.json"):
        """Initialize storage with filename.
        
        Args:
            filename: Name of the JSON file for storage
        """
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
        """Save URLs to JSON file.
        
        Returns:
            bool: True if saved successfully
        """
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump({"urls": self.urls}, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def add_url(self, original_url, short_code):
        """Add a new URL mapping.
        
        Args:
            original_url: The original long URL
            short_code: The short code to map to it
        
        Returns:
            dict: The created URL entry
        """
        entry = create_url_entry(original_url, short_code)
        self.urls[short_code] = entry
        self.save()
        return entry
    
    def get_url(self, short_code):
        """Get URL entry by short code.
        
        Args:
            short_code: The short code to look up
        
        Returns:
            dict or None: URL entry if found, None otherwise
        """
        return self.urls.get(short_code)
    
    def increment_clicks(self, short_code):
        """Increment click count for a URL.
        
        Args:
            short_code: The short code to update
        """
        if short_code in self.urls:
            self.urls[short_code]["clicks"] += 1
            self.urls[short_code]["last_accessed"] = datetime.now().isoformat()
            self.save()
    
    def delete_url(self, short_code):
        """Delete a URL mapping.
        
        Args:
            short_code: The short code to delete
        
        Returns:
            bool: True if deleted successfully
        """
        if short_code in self.urls:
            del self.urls[short_code]
            self.save()
            return True
        return False
    
    def get_all_urls(self):
        """Get all URL mappings.
        
        Returns:
            dict: Dictionary of all URL entries
        """
        return self.urls
    
    def code_exists(self, short_code):
        """Check if a short code already exists.
        
        Args:
            short_code: The short code to check
        
        Returns:
            bool: True if code exists
        """
        return short_code in self.urls
    
    def get_existing_codes(self):
        """Get set of all existing short codes.
        
        Returns:
            set: Set of all short codes
        """
        return set(self.urls.keys())


# =============================================================================
# URL SHORTENER CLASS
# =============================================================================

class URLShortener:
    """Main URL shortener application logic."""
    
    def __init__(self):
        """Initialize the URL shortener with storage."""
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


# =============================================================================
# CLI APPLICATION CLASS
# =============================================================================

class URLShortenerApp:
    """Main application class with CLI interface."""
    
    def __init__(self):
        """Initialize the application."""
        self.shortener = URLShortener()
    
    def display_welcome(self):
        """Display welcome screen."""
        print("\n" + "=" * 60)
        print("     WELCOME TO URL SHORTENER")
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
            print(f"\n✓ URL shortened successfully!")
            print(f"Short code: {result}")
            print(f"Short URL: short.url/{result}")
        else:
            print(f"\n✗ Error: {result}")
    
    def resolve_url_menu(self):
        """Handle URL resolution."""
        print("\n--- Resolve URL ---")
        code = input("Enter short code: ").strip()
        
        if not code:
            print("Error: Short code cannot be empty")
            return
        
        success, result = self.shortener.resolve_url(code)
        
        if success:
            print(f"\n✓ Original URL: {result}")
            print(f"Click count updated!")
        else:
            print(f"\n✗ Error: {result}")
    
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
                print(f"\nStatistics for '{code}':")
                print(f"  Original URL: {stats['original_url']}")
                print(f"  Short Code: {stats['short_code']}")
                print(f"  Created: {stats['created_at']}")
                print(f"  Total Clicks: {stats['clicks']}")
                if stats['last_accessed']:
                    print(f"  Last Accessed: {stats['last_accessed']}")
                else:
                    print(f"  Last Accessed: Never")
            else:
                print(f"\n✗ Short code '{code}' not found")
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
                    print("\n✓ URL deleted successfully!")
                else:
                    print("\n✗ Error deleting URL")
            else:
                print("\nDeletion cancelled.")
        else:
            print(f"\n✗ Short code '{code}' not found")
    
    def get_choice(self, min_val, max_val):
        """Get valid menu choice from user.
        
        Args:
            min_val: Minimum valid choice
            max_val: Maximum valid choice
        
        Returns:
            int: Valid menu choice
        """
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


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Entry point for the URL shortener."""
    try:
        app = URLShortenerApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!")


if __name__ == "__main__":
    main()
