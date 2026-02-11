# 🏆 URL Shortener - Challenges

Ready to take your URL shortener to the next level? Complete these challenges to enhance your skills!

---

## Challenge 1: Custom Short Codes

**Difficulty:** ⭐⭐  
**Time:** 30-45 minutes

Allow users to specify their own custom short codes instead of auto-generated ones.

### Features to Add

1. **Custom Code Option**
   - Add menu option "Shorten with Custom Code"
   - Validate custom code (alphanumeric only, 3-20 characters)
   - Check for collisions

2. **Implementation**

```python
def shorten_with_custom_code(self, original_url, custom_code):
    """Shorten URL with a custom code."""
    # Validate custom code format
    if not re.match(r'^[a-zA-Z0-9]{3,20}$', custom_code):
        return False, "Custom code must be 3-20 alphanumeric characters"
    
    # Check if code already exists
    if self.storage.code_exists(custom_code):
        return False, "Custom code already in use"
    
    # Normalize and validate URL
    original_url = normalize_url(original_url)
    if not is_valid_url(original_url):
        return False, "Invalid URL format"
    
    # Save URL mapping
    self.storage.add_url(original_url, custom_code)
    return True, custom_code
```

3. **Update Menu**
   - Add option 7: "Shorten with Custom Code"
   - Prompt for custom code after URL input

---

## Challenge 2: URL Expiration

**Difficulty:** ⭐⭐⭐  
**Time:** 45-60 minutes

Add optional expiration dates to shortened URLs.

### Features to Add

1. **Expiration Field**
   - Add `expires_at` field to URL entries
   - Support formats: "1d", "1w", "1m", or specific date

2. **Expiration Check**

```python
from datetime import datetime, timedelta

def parse_expiration(expiration_str):
    """Parse expiration string into datetime.
    
    Supports: '1d' (1 day), '1w' (1 week), '1m' (1 month)
    """
    if expiration_str.endswith('d'):
        days = int(expiration_str[:-1])
        return datetime.now() + timedelta(days=days)
    elif expiration_str.endswith('w'):
        weeks = int(expiration_str[:-1])
        return datetime.now() + timedelta(weeks=weeks)
    elif expiration_str.endswith('m'):
        # Approximate month as 30 days
        months = int(expiration_str[:-1])
        return datetime.now() + timedelta(days=30*months)
    return None

def is_expired(entry):
    """Check if a URL entry has expired."""
    if 'expires_at' not in entry or entry['expires_at'] is None:
        return False
    expires = datetime.fromisoformat(entry['expires_at'])
    return datetime.now() > expires
```

3. **Expired URL Handling**
   - Check expiration when resolving URLs
   - Show expiration date in statistics
   - Auto-delete expired URLs (optional cleanup feature)

4. **Update Storage**

```python
def create_url_entry(original_url, short_code, expires_at=None):
    """Create a new URL entry with optional expiration."""
    entry = {
        "original_url": original_url,
        "short_code": short_code,
        "created_at": datetime.now().isoformat(),
        "expires_at": expires_at.isoformat() if expires_at else None,
        "clicks": 0,
        "last_accessed": None
    }
    return entry
```

---

## Challenge 3: Password Protection

**Difficulty:** ⭐⭐⭐  
**Time:** 45-60 minutes

Protect sensitive URLs with passwords.

### Features to Add

1. **Password Hashing**
   - Use hashlib to store password hashes (not plaintext)
   - Support optional password protection

```python
import hashlib
import secrets

def hash_password(password, salt=None):
    """Hash a password with salt."""
    if salt is None:
        salt = secrets.token_hex(16)
    
    # Combine password and salt, hash with SHA-256
    pwdhash = hashlib.sha256((password + salt).encode()).hexdigest()
    return pwdhash, salt

def verify_password(password, hashed, salt):
    """Verify a password against its hash."""
    pwdhash, _ = hash_password(password, salt)
    return pwdhash == hashed
```

2. **Protected URL Creation**
   - Add option to set password when shortening
   - Store hash and salt, not plaintext password

3. **Password Prompt**
   - When resolving protected URLs, prompt for password
   - Verify before showing original URL

4. **Update URL Entry**

```python
def create_url_entry(original_url, short_code, password=None, expires_at=None):
    """Create URL entry with optional password protection."""
    entry = {
        "original_url": original_url,
        "short_code": short_code,
        "created_at": datetime.now().isoformat(),
        "expires_at": expires_at.isoformat() if expires_at else None,
        "clicks": 0,
        "last_accessed": None,
        "password_hash": None,
        "password_salt": None
    }
    
    if password:
        pwdhash, salt = hash_password(password)
        entry["password_hash"] = pwdhash
        entry["password_salt"] = salt
    
    return entry
```

---

## Challenge 4: QR Code Generation (Text-Based)

**Difficulty:** ⭐⭐  
**Time:** 30-45 minutes

Generate simple text-based QR codes for shortened URLs.

### Features to Add

1. **ASCII QR Code**
   - Create a simple text-based representation
   - Display as ASCII art in terminal

```python
def generate_ascii_qr(text, size=2):
    """Generate a simple ASCII QR-like pattern.
    
    This is a simplified representation for demonstration.
    For real QR codes, you'd use a library like qrcode.
    """
    # Create a simple pattern based on text hash
    import hashlib
    hash_val = hashlib.md5(text.encode()).hexdigest()
    
    # Generate pattern
    pattern = []
    for i in range(0, len(hash_val), 2):
        val = int(hash_val[i:i+2], 16)
        row = ""
        for j in range(8):
            if val & (1 << j):
                row += "██"
            else:
                row += "  "
        pattern.append(row)
    
    # Add border
    border = "█" * 20
    qr = [border]
    for row in pattern[:8]:
        qr.append("█" + row[:18] + "█")
    qr.append(border)
    
    return "\n".join(qr)
```

2. **QR Display Menu**
   - Add option to display QR code for a short URL
   - Show alongside the short code

---

## Challenge 5: Bulk Import/Export

**Difficulty:** ⭐⭐⭐  
**Time:** 45-60 minutes

Support importing and exporting URLs in various formats.

### Features to Add

1. **CSV Export**
   - Export all URLs to CSV format
   - Include all metadata fields

```python
import csv

def export_to_csv(self, filename="urls_export.csv"):
    """Export all URLs to CSV file."""
    urls = self.storage.get_all_urls()
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write header
        writer.writerow(['short_code', 'original_url', 'created_at', 
                        'clicks', 'last_accessed'])
        # Write data
        for code, entry in urls.items():
            writer.writerow([
                entry['short_code'],
                entry['original_url'],
                entry['created_at'],
                entry['clicks'],
                entry.get('last_accessed', '')
            ])
    return True
```

2. **CSV Import**
   - Import URLs from CSV file
   - Handle duplicates gracefully

```python
def import_from_csv(self, filename):
    """Import URLs from CSV file."""
    imported = 0
    skipped = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row['short_code']
            url = row['original_url']
            
            # Skip if code already exists
            if self.storage.code_exists(code):
                skipped += 1
                continue
            
            # Add URL
            self.storage.add_url(url, code)
            imported += 1
    
    return imported, skipped
```

3. **JSON Export/Import**
   - Export to JSON format
   - Import from JSON (backup/restore)

4. **Menu Options**
   - Add "Export URLs" option
   - Add "Import URLs" option
   - Support format selection

---

## Challenge 6: Click Analytics

**Difficulty:** ⭐⭐⭐⭐  
**Time:** 60-90 minutes

Track detailed analytics for each click.

### Features to Add

1. **Detailed Click Log**
   - Store timestamp for each click
   - Track click history per URL

```python
def increment_clicks_detailed(self, short_code):
    """Increment click count with detailed logging."""
    if short_code in self.urls:
        self.urls[short_code]["clicks"] += 1
        self.urls[short_code]["last_accessed"] = datetime.now().isoformat()
        
        # Add to click history
        if "click_history" not in self.urls[short_code]:
            self.urls[short_code]["click_history"] = []
        
        self.urls[short_code]["click_history"].append({
            "timestamp": datetime.now().isoformat()
        })
        
        # Limit history to last 100 clicks
        self.urls[short_code]["click_history"] = \
            self.urls[short_code]["click_history"][-100:]
        
        self.save()
```

2. **Analytics Display**
   - Show click history for a URL
   - Display click frequency over time
   - Calculate clicks per day/week

```python
def get_click_analytics(self, short_code):
    """Get detailed analytics for a URL."""
    entry = self.storage.get_url(short_code)
    if not entry or "click_history" not in entry:
        return None
    
    history = entry["click_history"]
    
    # Calculate clicks per day
    from collections import defaultdict
    daily_clicks = defaultdict(int)
    
    for click in history:
        date = click["timestamp"][:10]  # YYYY-MM-DD
        daily_clicks[date] += 1
    
    return {
        "total_clicks": len(history),
        "daily_clicks": dict(daily_clicks),
        "first_click": history[0]["timestamp"] if history else None,
        "last_click": history[-1]["timestamp"] if history else None
    }
```

3. **Visual Analytics**
   - Display simple bar chart of daily clicks
   - Show trend over time

---

## Challenge 7: URL Categories/Tags

**Difficulty:** ⭐⭐  
**Time:** 30-45 minutes

Organize URLs with categories and tags.

### Features to Add

1. **Category Field**
   - Add optional category when shortening
   - Predefined categories: Work, Personal, Social, Shopping, etc.

2. **Tag System**
   - Support multiple tags per URL
   - Filter URLs by tags

```python
def create_url_entry(original_url, short_code, category="General", tags=None):
    """Create URL entry with category and tags."""
    entry = {
        "original_url": original_url,
        "short_code": short_code,
        "created_at": datetime.now().isoformat(),
        "clicks": 0,
        "last_accessed": None,
        "category": category,
        "tags": tags or []
    }
    return entry
```

3. **Filtering**
   - Filter URLs by category
   - Search by tags
   - Display category statistics

4. **Update List View**
   - Show category column
   - Allow filtering in list view

---

## Challenge 8: URL Preview

**Difficulty:** ⭐⭐⭐⭐  
**Time:** 60-90 minutes

Show page title and description when resolving URLs (simulated).

### Features to Add

1. **Metadata Extraction**
   - Simulate fetching page metadata
   - Store title and description

```python
def fetch_url_metadata(self, url):
    """Simulate fetching URL metadata.
    
    In a real implementation, you'd use urllib to fetch
    the page and parse HTML. Here we simulate it.
    """
    # Simulate different page types
    if "github.com" in url:
        return {
            "title": "GitHub - Where the world builds software",
            "description": "GitHub is where over 100 million developers..."
        }
    elif "python.org" in url:
        return {
            "title": "Welcome to Python.org",
            "description": "The official home of the Python Programming Language"
        }
    else:
        return {
            "title": f"Page at {url[:30]}...",
            "description": "No description available"
        }
```

2. **Preview Display**
   - Show preview when listing URLs
   - Display when resolving (optional)

3. **Update URL Entry**

```python
def create_url_entry(original_url, short_code):
    """Create URL entry with metadata."""
    entry = {
        "original_url": original_url,
        "short_code": short_code,
        "created_at": datetime.now().isoformat(),
        "clicks": 0,
        "last_accessed": None,
        "metadata": None
    }
    return entry

def update_metadata(self, short_code):
    """Update metadata for a URL."""
    entry = self.storage.get_url(short_code)
    if entry:
        metadata = self.fetch_url_metadata(entry["original_url"])
        entry["metadata"] = metadata
        self.storage.save()
```

---

## Completion Checklist

- [ ] Challenge 1: Custom Short Codes
- [ ] Challenge 2: URL Expiration
- [ ] Challenge 3: Password Protection
- [ ] Challenge 4: QR Code Generation
- [ ] Challenge 5: Bulk Import/Export
- [ ] Challenge 6: Click Analytics
- [ ] Challenge 7: URL Categories/Tags
- [ ] Challenge 8: URL Preview

---

**Congratulations on completing the challenges!** 🎉

You've built a feature-rich URL shortener with:
- Custom code support
- Expiration dates
- Password protection
- QR codes
- Import/export
- Analytics
- Categories
- Metadata

These skills translate directly to real-world web development! 🚀
