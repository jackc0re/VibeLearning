# 📓 Project 6: Personal Journal

Build a CLI-based personal journal application for daily entries with search and export functionality.

---

## 📋 Project Overview

This project helps you practice:
- **datetime module** — Date/time handling, formatting, and parsing
- **JSON file I/O** — Persistent storage of journal entries
- **Text processing** — String manipulation and search
- **OOP design** — Entry and Journal classes
- **CLI design** — Menu-driven user interface

### Features to Build

1. ✅ Create Entry
   - Add new journal entry with date, title, mood, content
   - Support for tags to organize entries
   - Multi-line content input

2. ✅ View Entry
   - Display a specific entry by number
   - Show full content with formatting

3. ✅ List All Entries
   - Show all entries sorted by date
   - Display entry details

4. ✅ Search Entries
   - Search by date range
   - Search by keyword in title/content
   - Search by tag

5. ✅ Export Journal
   - Export to Markdown (.md) format
   - Export to plain text (.txt) format

6. ✅ Delete Entry
   - Remove entries with confirmation

7. ✅ Statistics
   - Total entries and word count
   - Mood distribution
   - Most used tags

8. ✅ Writing Prompts
   - Random prompts to inspire writing
   - Start entry directly from prompt

---

## 💻 Requirements

### Prerequisites

Complete these modules before starting:
- [00_getting_started](../../00_getting_started/README.md)
- [01_foundations](../../01_foundations/README.md) — especially datetime
- [02_data_structures](../../02_data_structures/README.md)
- [04_oop_concepts](../../04_oop_concepts/README.md)
- [10_file_io](../../10_file_io/README.md) — especially JSON

### Skills You'll Use

- **datetime** — Handle dates and times for entries
- **JSON** — Store and load journal entries
- **Classes** — Create Entry and Journal classes
- **String Methods** — Search and format text
- **File Operations** — Read prompts, export entries
- **Control Flow** — Menu navigation and validation

---

## 🚀 Development Steps

### Step 1: Entry Class (20 minutes)

Create a class to represent a single journal entry:

```python
from datetime import datetime

class Entry:
    """Represents a single journal entry."""
    
    def __init__(self, title, content, mood="neutral", date=None, tags=None):
        self.id = self._generate_id()
        self.date = date if date else datetime.now()
        self.title = title
        self.mood = mood.lower()
        self.content = content
        self.tags = tags if tags else []
    
    def _generate_id(self):
        """Generate unique ID using timestamp."""
        return datetime.now().strftime("%Y%m%d%H%M%S%f")[:16]
    
    def to_dict(self):
        """Convert entry to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "title": self.title,
            "mood": self.mood,
            "content": self.content,
            "tags": self.tags
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Entry from dictionary."""
        return cls(
            title=data["title"],
            content=data["content"],
            mood=data.get("mood", "neutral"),
            date=datetime.fromisoformat(data["date"]),
            tags=data.get("tags", [])
        )
```

### Step 2: Journal Class (30 minutes)

Create a class to manage all entries:

```python
import json
from pathlib import Path

class Journal:
    """Manages journal entries and persistence."""
    
    def __init__(self, filename="entries.json"):
        script_dir = Path(__file__).parent
        self.filename = script_dir / filename
        self.entries = []
        self.load()
    
    def load(self):
        """Load entries from JSON file."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.entries = [Entry.from_dict(e) for e in data.get("entries", [])]
        except FileNotFoundError:
            self.entries = []
    
    def save(self):
        """Save entries to JSON file."""
        data = {"entries": [e.to_dict() for e in self.entries]}
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def add_entry(self, title, content, mood="neutral", tags=None):
        """Create and add a new entry."""
        entry = Entry(title, content, mood, tags=tags)
        self.entries.append(entry)
        self.save()
        return entry
    
    def get_all(self, sort_desc=True):
        """Get all entries, sorted by date."""
        return sorted(self.entries, key=lambda e: e.date, reverse=sort_desc)
```

### Step 3: Search Functions (20 minutes)

Add search capabilities to the Journal class:

```python
from datetime import timedelta

def search_by_date_range(self, start_date, end_date):
    """Find entries within a date range."""
    results = []
    for entry in self.entries:
        if start_date <= entry.date <= end_date:
            results.append(entry)
    return sorted(results, key=lambda e: e.date, reverse=True)

def search_by_keyword(self, keyword):
    """Find entries containing keyword in title or content."""
    keyword = keyword.lower()
    results = []
    for entry in self.entries:
        if (keyword in entry.title.lower() or 
            keyword in entry.content.lower()):
            results.append(entry)
    return sorted(results, key=lambda e: e.date, reverse=True)

def search_by_tag(self, tag):
    """Find entries with a specific tag."""
    tag = tag.lower()
    results = []
    for entry in self.entries:
        if tag in [t.lower() for t in entry.tags]:
            results.append(entry)
    return sorted(results, key=lambda e: e.date, reverse=True)
```

### Step 4: Export Functions (15 minutes)

Add export functionality:

```python
def export_to_file(self, filename, format="markdown"):
    """Export all entries to a file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            if format == "markdown":
                f.write("# Personal Journal Export\n\n")
                for entry in self.get_all():
                    f.write(entry.to_markdown())
            else:
                for entry in self.get_all():
                    f.write(entry.to_plain_text())
        return True
    except Exception as e:
        print(f"Error exporting: {e}")
        return False
```

### Step 5: CLI Interface (40 minutes)

Create the main application class:

```python
class JournalApp:
    """Main application class for CLI interface."""
    
    def __init__(self):
        self.journal = Journal()
        self.prompts = self._load_prompts()
    
    def run(self):
        """Main application loop."""
        self._display_welcome()
        
        while True:
            self._display_menu()
            choice = self._get_choice(1, 9)
            
            if choice == 1:
                self._create_entry()
            elif choice == 2:
                self._view_entry()
            # ... handle other choices
            elif choice == 9:
                print("\nThanks for journaling! Goodbye!")
                break
    
    def _display_menu(self):
        """Display main menu."""
        print("\n" + "=" * 40)
        print("           MAIN MENU")
        print("=" * 40)
        print("1. New Entry")
        print("2. View Entry")
        print("3. List All Entries")
        print("4. Search Entries")
        print("5. Export Journal")
        print("6. Delete Entry")
        print("7. Statistics")
        print("8. Writing Prompt")
        print("9. Exit")
        print("=" * 40)
```

### Step 6: Create Prompts File (5 minutes)

Create `prompts.txt` with writing prompts:

```
What made you smile today?
What are you grateful for right now?
Describe a challenge you overcame recently.
What is something new you learned this week?
Write about a person who inspires you.
What would your perfect day look like?
What's on your mind right now?
Describe a goal you're working towards.
What's a memory that makes you happy?
Write about something you're looking forward to.
```

---

## 🧪 Testing

Test your journal application with these scenarios:

### Basic Operations
1. **Create Entry** — Add a new entry with all fields
2. **View Entry** — View a specific entry
3. **List Entries** — Display all entries
4. **Delete Entry** — Remove an entry

### Search Tests
1. **Date Range** — Find entries from last week
2. **Keyword Search** — Find entries containing "happy"
3. **Tag Search** — Find entries with specific tag

### Export Tests
1. **Markdown Export** — Export to .md file
2. **Text Export** — Export to .txt file
3. **Verify Content** — Check exported file format

### Edge Cases
1. **Empty Journal** — Test with no entries
2. **Long Content** — Test with very long entry
3. **Special Characters** — Test with emojis and unicode
4. **Invalid Input** — Test error handling

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How to work with datetime for timestamps and date ranges
- ✅ How to serialize/deserialize objects with JSON
- ✅ How to design classes that work together
- ✅ How to implement search functionality
- ✅ How to create a menu-driven CLI application
- ✅ How to handle file I/O for persistence

---

## 🏆 Challenges

Complete these challenges to enhance your journal:

1. **Mood Statistics** — Visualize mood distribution over time
2. **Word Count Goals** — Set and track daily/weekly word goals
3. **Entry Templates** — Create reusable templates
4. **Backup System** — Auto-backup entries
5. **Import Feature** — Import entries from text files
6. **Encryption** — Add password protection
7. **Reminders** — Set daily reminder messages
8. **Multi-Journal** — Support multiple journals

See [challenges.md](challenges.md) for detailed instructions.

---

## 📁 File Structure

```
06_personal_journal/
├── README.md          # This file
├── journal.py         # Main implementation
├── entries.json       # Journal entries (created at runtime)
├── prompts.txt        # Writing prompts
└── challenges.md      # Additional challenge tasks
```

---

## 🎨 Sample Output

### Welcome Screen
```
============================================================
          PERSONAL JOURNAL
============================================================

Your private space for thoughts, ideas, and reflections.

You have 5 entries in your journal.
Last entry: 2026-02-10

============================================================
```

### Entry Display
```
============================================================
                    ENTRY
============================================================
ID: 20260210143022
Date: 2026-02-10 14:30
Mood: 😊 Happy

Title: Great Day at the Park
--------------------------------------------------
Today I went to the park and had a wonderful time.
The weather was perfect and I saw some beautiful
flowers blooming...

Tags: nature, outdoor, spring
============================================================
```

### Statistics
```
==================================================
           JOURNAL STATISTICS
==================================================

Total Entries: 10
Total Words: 2450
Average Words per Entry: 245

First Entry: 2026-01-15
Last Entry: 2026-02-10
Journaling Span: 26 days

Mood Distribution:
  happy     : *** (3)
  neutral   : **** (4)
  excited   : *** (3)

Most Used Tags:
  personal: 5 entries
  ideas: 3 entries
  work: 2 entries
==================================================
```

---

## 📚 Related Topics

| Topic | Location |
|-------|----------|
| datetime basics | [01_foundations/06_datetime](../../01_foundations/06_datetime/) |
| JSON file I/O | [10_file_io/03_working_with_json](../../10_file_io/03_working_with_json/) |
| Classes | [04_oop_concepts/01_classes](../../04_oop_concepts/01_classes/) |
| String methods | [01_foundations/03_strings](../../01_foundations/03_strings/) |

---

**Ready to start?** Create `journal.py` and `prompts.txt`, then begin building! 🚀
