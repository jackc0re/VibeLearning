"""
Personal Journal Project
========================
A CLI-based personal journal application for daily entries
with search and export functionality.
"""

import json
import os
import random
from datetime import datetime, timedelta
from pathlib import Path


# =============================================================================
# ENTRY CLASS
# =============================================================================

class Entry:
    """Represents a single journal entry.
    
    Attributes:
        id: Unique identifier based on timestamp
        date: When the entry was created
        title: Entry title
        mood: Mood indicator (happy, sad, neutral, excited, etc.)
        content: The main journal content
        tags: List of tags for organization
    """
    
    def __init__(self, title, content, mood="neutral", date=None, tags=None):
        """Initialize a new journal entry.
        
        Args:
            title: The entry title
            content: The main content text
            mood: Mood indicator (default: "neutral")
            date: Entry date (default: now)
            tags: List of tags (default: empty list)
        """
        self.id = self._generate_id()
        self.date = date if date else datetime.now()
        self.title = title
        self.mood = mood.lower()
        self.content = content
        self.tags = tags if tags else []
    
    def _generate_id(self):
        """Generate a unique ID using timestamp.
        
        Returns:
            str: Unique identifier string
        """
        return datetime.now().strftime("%Y%m%d%H%M%S%f")[:16]
    
    def to_dict(self):
        """Convert entry to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the entry
        """
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
        """Create an Entry from a dictionary.
        
        Args:
            data: Dictionary containing entry data
            
        Returns:
            Entry: New Entry instance
        """
        return cls(
            title=data["title"],
            content=data["content"],
            mood=data.get("mood", "neutral"),
            date=datetime.fromisoformat(data["date"]),
            tags=data.get("tags", [])
        )
    
    def display(self, show_full=True):
        """Display the entry in formatted output.
        
        Args:
            show_full: If True, show full content; otherwise show summary
        """
        mood_emoji = self._get_mood_emoji()
        
        print("\n" + "=" * 60)
        print("                    ENTRY")
        print("=" * 60)
        print(f"ID: {self.id}")
        print(f"Date: {self.date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Mood: {mood_emoji} {self.mood.capitalize()}")
        print(f"\nTitle: {self.title}")
        print("-" * 60)
        
        if show_full:
            # Word wrap for better readability
            self._print_wrapped(self.content)
        else:
            # Show first 100 characters
            preview = self.content[:100] + "..." if len(self.content) > 100 else self.content
            print(preview)
        
        if self.tags:
            print(f"\nTags: {', '.join(self.tags)}")
        
        print("=" * 60)
    
    def _get_mood_emoji(self):
        """Get emoji for current mood.
        
        Returns:
            str: Emoji representing the mood
        """
        mood_map = {
            "happy": "😊",
            "sad": "😢",
            "neutral": "😐",
            "excited": "🎉",
            "anxious": "😰",
            "calm": "😌",
            "angry": "😠",
            "grateful": "🙏",
            "tired": "😴",
            "inspired": "💡"
        }
        return mood_map.get(self.mood, "📝")
    
    def _print_wrapped(self, text, width=60):
        """Print text with word wrapping.
        
        Args:
            text: Text to print
            width: Maximum line width
        """
        words = text.split()
        line = ""
        for word in words:
            if len(line) + len(word) + 1 <= width:
                line += (" " if line else "") + word
            else:
                print(line)
                line = word
        if line:
            print(line)
    
    def to_markdown(self):
        """Convert entry to Markdown format.
        
        Returns:
            str: Markdown formatted string
        """
        tags_str = ", ".join(self.tags) if self.tags else "none"
        return f"""# {self.title}

**Date:** {self.date.strftime('%Y-%m-%d %H:%M')}  
**Mood:** {self.mood.capitalize()}

{self.content}

**Tags:** {tags_str}

---

"""
    
    def to_plain_text(self):
        """Convert entry to plain text format.
        
        Returns:
            str: Plain text formatted string
        """
        tags_str = ", ".join(self.tags) if self.tags else "none"
        return f"""Entry: {self.title}
Date: {self.date.strftime('%Y-%m-%d %H:%M')}
Mood: {self.mood.capitalize()}
Tags: {tags_str}

{self.content}

{'=' * 60}

"""


# =============================================================================
# JOURNAL CLASS
# =============================================================================

class Journal:
    """Manages journal entries and persistence.
    
    Attributes:
        filename: Path to the JSON storage file
        entries: List of Entry objects
    """
    
    def __init__(self, filename="entries.json"):
        """Initialize the journal.
        
        Args:
            filename: Name of the JSON storage file
        """
        # Get the directory of the current script for relative paths
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
            # First run - no entries file yet
            self.entries = []
        except json.JSONDecodeError:
            print(f"Warning: Could not parse {self.filename}. Starting fresh.")
            self.entries = []
    
    def save(self):
        """Save entries to JSON file."""
        try:
            data = {
                "entries": [e.to_dict() for e in self.entries]
            }
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving journal: {e}")
            return False
    
    def add_entry(self, title, content, mood="neutral", tags=None):
        """Create and add a new entry.
        
        Args:
            title: Entry title
            content: Entry content
            mood: Mood indicator
            tags: List of tags
            
        Returns:
            Entry: The newly created entry
        """
        entry = Entry(title, content, mood, tags=tags)
        self.entries.append(entry)
        self.save()
        return entry
    
    def get_entry(self, entry_id):
        """Get entry by ID.
        
        Args:
            entry_id: The entry ID to find
            
        Returns:
            Entry or None: The entry if found, None otherwise
        """
        for entry in self.entries:
            if entry.id == entry_id:
                return entry
        return None
    
    def get_entry_by_index(self, index):
        """Get entry by index (1-based for user convenience).
        
        Args:
            index: 1-based index of the entry
            
        Returns:
            Entry or None: The entry if found, None otherwise
        """
        if 1 <= index <= len(self.entries):
            return self.entries[index - 1]
        return None
    
    def delete_entry(self, entry_id):
        """Delete entry by ID.
        
        Args:
            entry_id: The entry ID to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        for i, entry in enumerate(self.entries):
            if entry.id == entry_id:
                deleted_entry = self.entries.pop(i)
                self.save()
                return True
        return False
    
    def search_by_date_range(self, start_date, end_date):
        """Find entries within a date range.
        
        Args:
            start_date: Start of date range (datetime)
            end_date: End of date range (datetime)
            
        Returns:
            list: List of matching Entry objects
        """
        results = []
        for entry in self.entries:
            if start_date <= entry.date <= end_date:
                results.append(entry)
        return sorted(results, key=lambda e: e.date, reverse=True)
    
    def search_by_keyword(self, keyword):
        """Find entries containing keyword in title or content.
        
        Args:
            keyword: Search term
            
        Returns:
            list: List of matching Entry objects
        """
        keyword = keyword.lower()
        results = []
        for entry in self.entries:
            if (keyword in entry.title.lower() or 
                keyword in entry.content.lower()):
                results.append(entry)
        return sorted(results, key=lambda e: e.date, reverse=True)
    
    def search_by_tag(self, tag):
        """Find entries with a specific tag.
        
        Args:
            tag: Tag to search for
            
        Returns:
            list: List of matching Entry objects
        """
        tag = tag.lower()
        results = []
        for entry in self.entries:
            if tag in [t.lower() for t in entry.tags]:
                results.append(entry)
        return sorted(results, key=lambda e: e.date, reverse=True)
    
    def get_all(self, sort_desc=True):
        """Get all entries, sorted by date.
        
        Args:
            sort_desc: If True, sort newest first
            
        Returns:
            list: Sorted list of Entry objects
        """
        return sorted(self.entries, key=lambda e: e.date, reverse=sort_desc)
    
    def get_recent(self, count=5):
        """Get most recent entries.
        
        Args:
            count: Number of entries to return
            
        Returns:
            list: Most recent Entry objects
        """
        sorted_entries = self.get_all()
        return sorted_entries[:count]
    
    def export_to_file(self, filename, format="markdown"):
        """Export all entries to a file.
        
        Args:
            filename: Output filename
            format: "markdown" or "text"
            
        Returns:
            bool: True if successful
        """
        try:
            # Ensure the filename has correct extension
            if format == "markdown" and not filename.endswith('.md'):
                filename += '.md'
            elif format == "text" and not filename.endswith('.txt'):
                filename += '.txt'
            
            with open(filename, 'w', encoding='utf-8') as f:
                if format == "markdown":
                    f.write("# Personal Journal Export\n\n")
                    f.write(f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
                    f.write("---\n\n")
                    for entry in self.get_all():
                        f.write(entry.to_markdown())
                else:
                    f.write("PERSONAL JOURNAL EXPORT\n")
                    f.write(f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                    f.write("=" * 60 + "\n\n")
                    for entry in self.get_all():
                        f.write(entry.to_plain_text())
            
            return True
        except Exception as e:
            print(f"Error exporting journal: {e}")
            return False
    
    def get_statistics(self):
        """Get journal statistics.
        
        Returns:
            dict: Statistics about the journal
        """
        if not self.entries:
            return {
                "total_entries": 0,
                "total_words": 0,
                "first_entry": None,
                "last_entry": None,
                "moods": {},
                "tags": {}
            }
        
        total_words = sum(len(e.content.split()) for e in self.entries)
        moods = {}
        tags = {}
        
        for entry in self.entries:
            moods[entry.mood] = moods.get(entry.mood, 0) + 1
            for tag in entry.tags:
                tags[tag] = tags.get(tag, 0) + 1
        
        sorted_entries = self.get_all()
        
        return {
            "total_entries": len(self.entries),
            "total_words": total_words,
            "first_entry": sorted_entries[-1].date if sorted_entries else None,
            "last_entry": sorted_entries[0].date if sorted_entries else None,
            "moods": moods,
            "tags": tags
        }


# =============================================================================
# JOURNAL APP CLASS (CLI Interface)
# =============================================================================

class JournalApp:
    """Main application class for CLI interface.
    
    Attributes:
        journal: Journal instance
        prompts: List of writing prompts
    """
    
    def __init__(self):
        """Initialize the journal application."""
        self.journal = Journal()
        self.prompts = self._load_prompts()
    
    def _load_prompts(self):
        """Load writing prompts from file.
        
        Returns:
            list: List of prompt strings
        """
        script_dir = Path(__file__).parent
        prompts_file = script_dir / "prompts.txt"
        
        try:
            with open(prompts_file, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            # Default prompts if file not found
            return [
                "What made you smile today?",
                "What are you grateful for right now?",
                "Describe a challenge you overcame recently.",
                "What is something new you learned this week?",
                "Write about a person who inspires you.",
                "What would your perfect day look like?",
                "What's on your mind right now?",
                "Describe a goal you're working towards.",
                "What's a memory that makes you happy?",
                "Write about something you're looking forward to."
            ]
    
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
            elif choice == 3:
                self._list_entries()
            elif choice == 4:
                self._search_entries()
            elif choice == 5:
                self._export_journal()
            elif choice == 6:
                self._delete_entry()
            elif choice == 7:
                self._show_statistics()
            elif choice == 8:
                self._show_prompt()
            elif choice == 9:
                print("\nThanks for journaling! Goodbye!")
                break
    
    def _display_welcome(self):
        """Display welcome screen."""
        print("\n" + "=" * 60)
        print("          PERSONAL JOURNAL")
        print("=" * 60)
        print("\nYour private space for thoughts, ideas, and reflections.")
        
        stats = self.journal.get_statistics()
        if stats["total_entries"] > 0:
            print(f"\nYou have {stats['total_entries']} entries in your journal.")
            print(f"Last entry: {stats['last_entry'].strftime('%Y-%m-%d')}")
        else:
            print("\nYour journal is empty. Start writing!")
        
        print("\n" + "=" * 60)
    
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
    
    def _get_choice(self, min_val, max_val):
        """Get valid menu choice.
        
        Args:
            min_val: Minimum valid choice
            max_val: Maximum valid choice
            
        Returns:
            int: User's valid choice
        """
        while True:
            try:
                choice = int(input(f"\nEnter choice ({min_val}-{max_val}): "))
                if min_val <= choice <= max_val:
                    return choice
                print(f"Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def _create_entry(self):
        """Interactive entry creation."""
        print("\n" + "-" * 40)
        print("           NEW ENTRY")
        print("-" * 40)
        
        # Get title
        title = input("\nEnter title: ").strip()
        if not title:
            print("Title is required. Entry cancelled.")
            return
        
        # Get mood
        print("\nMood options: happy, sad, neutral, excited, anxious,")
        print("              calm, angry, grateful, tired, inspired")
        mood = input("How are you feeling? (press Enter for 'neutral'): ").strip()
        if not mood:
            mood = "neutral"
        
        # Get content (multi-line)
        print("\nEnter your journal entry (type 'END' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        
        content = "\n".join(lines)
        if not content.strip():
            print("Content is required. Entry cancelled.")
            return
        
        # Get tags
        tags_input = input("\nEnter tags (comma-separated, or press Enter to skip): ").strip()
        tags = [t.strip() for t in tags_input.split(",") if t.strip()] if tags_input else []
        
        # Create entry
        entry = self.journal.add_entry(title, content, mood, tags)
        print(f"\nEntry saved! ID: {entry.id}")
    
    def _view_entry(self):
        """View a specific entry."""
        if not self.journal.entries:
            print("\nNo entries yet. Create one first!")
            return
        
        self._list_entries_brief()
        
        choice = input("\nEnter entry number to view (or press Enter to cancel): ").strip()
        if not choice:
            return
        
        try:
            index = int(choice)
            entry = self.journal.get_entry_by_index(index)
            if entry:
                entry.display()
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def _list_entries(self):
        """List all entries with details."""
        entries = self.journal.get_all()
        
        if not entries:
            print("\nNo entries yet. Create one first!")
            return
        
        print("\n" + "=" * 60)
        print("              ALL ENTRIES")
        print("=" * 60)
        
        for i, entry in enumerate(entries, 1):
            print(f"\n--- Entry {i} ---")
            entry.display(show_full=True)
    
    def _list_entries_brief(self):
        """List entries with brief summaries."""
        entries = self.journal.get_all()
        
        if not entries:
            print("\nNo entries yet.")
            return
        
        print("\n" + "-" * 60)
        print(f"{'#':<4} {'Date':<12} {'Mood':<10} {'Title':<30}")
        print("-" * 60)
        
        for i, entry in enumerate(entries, 1):
            mood_emoji = entry._get_mood_emoji()
            title_display = entry.title[:27] + "..." if len(entry.title) > 30 else entry.title
            print(f"{i:<4} {entry.date.strftime('%Y-%m-%d'):<12} "
                  f"{mood_emoji} {entry.mood:<8} {title_display}")
        
        print("-" * 60)
        print(f"Total: {len(entries)} entries")
    
    def _search_entries(self):
        """Search entries by date, keyword, or tag."""
        if not self.journal.entries:
            print("\nNo entries to search. Create some first!")
            return
        
        print("\n" + "-" * 40)
        print("           SEARCH ENTRIES")
        print("-" * 40)
        print("1. Search by date range")
        print("2. Search by keyword")
        print("3. Search by tag")
        print("-" * 40)
        
        choice = self._get_choice(1, 3)
        
        if choice == 1:
            self._search_by_date()
        elif choice == 2:
            self._search_by_keyword()
        elif choice == 3:
            self._search_by_tag()
    
    def _search_by_date(self):
        """Search entries by date range."""
        print("\nEnter date range (YYYY-MM-DD format)")
        
        try:
            start_str = input("Start date (or press Enter for 30 days ago): ").strip()
            end_str = input("End date (or press Enter for today): ").strip()
            
            if end_str:
                end_date = datetime.strptime(end_str, "%Y-%m-%d")
                end_date = end_date.replace(hour=23, minute=59, second=59)
            else:
                end_date = datetime.now()
            
            if start_str:
                start_date = datetime.strptime(start_str, "%Y-%m-%d")
            else:
                start_date = end_date - timedelta(days=30)
            
            results = self.journal.search_by_date_range(start_date, end_date)
            
            if results:
                print(f"\nFound {len(results)} entries:")
                for entry in results:
                    entry.display(show_full=False)
            else:
                print("\nNo entries found in that date range.")
                
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
    
    def _search_by_keyword(self):
        """Search entries by keyword."""
        keyword = input("\nEnter search term: ").strip()
        
        if not keyword:
            print("Search term required.")
            return
        
        results = self.journal.search_by_keyword(keyword)
        
        if results:
            print(f"\nFound {len(results)} entries matching '{keyword}':")
            for entry in results:
                entry.display(show_full=False)
        else:
            print(f"\nNo entries found matching '{keyword}'.")
    
    def _search_by_tag(self):
        """Search entries by tag."""
        # Show available tags
        stats = self.journal.get_statistics()
        if stats["tags"]:
            print("\nAvailable tags:", ", ".join(sorted(stats["tags"].keys())))
        
        tag = input("\nEnter tag to search: ").strip()
        
        if not tag:
            print("Tag required.")
            return
        
        results = self.journal.search_by_tag(tag)
        
        if results:
            print(f"\nFound {len(results)} entries with tag '{tag}':")
            for entry in results:
                entry.display(show_full=False)
        else:
            print(f"\nNo entries found with tag '{tag}'.")
    
    def _export_journal(self):
        """Export journal to file."""
        if not self.journal.entries:
            print("\nNo entries to export.")
            return
        
        print("\n" + "-" * 40)
        print("           EXPORT JOURNAL")
        print("-" * 40)
        print("1. Export as Markdown (.md)")
        print("2. Export as Plain Text (.txt)")
        print("-" * 40)
        
        choice = self._get_choice(1, 2)
        
        filename = input("\nEnter filename (without extension): ").strip()
        if not filename:
            filename = f"journal_export_{datetime.now().strftime('%Y%m%d')}"
        
        format_type = "markdown" if choice == 1 else "text"
        
        if self.journal.export_to_file(filename, format_type):
            extension = ".md" if format_type == "markdown" else ".txt"
            print(f"\nJournal exported successfully to {filename}{extension}")
        else:
            print("\nExport failed.")
    
    def _delete_entry(self):
        """Delete an entry."""
        if not self.journal.entries:
            print("\nNo entries to delete.")
            return
        
        self._list_entries_brief()
        
        choice = input("\nEnter entry number to delete (or press Enter to cancel): ").strip()
        if not choice:
            return
        
        try:
            index = int(choice)
            entry = self.journal.get_entry_by_index(index)
            if entry:
                print(f"\nYou are about to delete: '{entry.title}'")
                confirm = input("Are you sure? (yes/no): ").strip().lower()
                if confirm == "yes":
                    self.journal.delete_entry(entry.id)
                    print("Entry deleted.")
                else:
                    print("Cancelled.")
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def _show_statistics(self):
        """Display journal statistics."""
        stats = self.journal.get_statistics()
        
        print("\n" + "=" * 50)
        print("           JOURNAL STATISTICS")
        print("=" * 50)
        
        if stats["total_entries"] == 0:
            print("\nNo entries yet. Start writing!")
            return
        
        print(f"\nTotal Entries: {stats['total_entries']}")
        print(f"Total Words: {stats['total_words']}")
        print(f"Average Words per Entry: {stats['total_words'] // stats['total_entries']}")
        
        if stats["first_entry"]:
            print(f"\nFirst Entry: {stats['first_entry'].strftime('%Y-%m-%d')}")
            print(f"Last Entry: {stats['last_entry'].strftime('%Y-%m-%d')}")
            
            days = (stats['last_entry'] - stats['first_entry']).days
            print(f"Journaling Span: {days} days")
        
        if stats["moods"]:
            print("\nMood Distribution:")
            for mood, count in sorted(stats["moods"].items(), 
                                     key=lambda x: x[1], reverse=True):
                bar = "*" * count
                print(f"  {mood:<10}: {bar} ({count})")
        
        if stats["tags"]:
            print("\nMost Used Tags:")
            sorted_tags = sorted(stats["tags"].items(), 
                                key=lambda x: x[1], reverse=True)[:5]
            for tag, count in sorted_tags:
                print(f"  {tag}: {count} entries")
        
        print("=" * 50)
    
    def _show_prompt(self):
        """Display a random writing prompt."""
        if self.prompts:
            prompt = random.choice(self.prompts)
            print("\n" + "=" * 50)
            print("           WRITING PROMPT")
            print("=" * 50)
            print(f"\n{prompt}")
            print("\n" + "=" * 50)
            
            start = input("\nStart writing with this prompt? (yes/no): ").strip().lower()
            if start == "yes":
                self._create_entry_with_prompt(prompt)
        else:
            print("\nNo prompts available.")
    
    def _create_entry_with_prompt(self, prompt):
        """Create entry with prompt as inspiration."""
        print("\n" + "-" * 40)
        print("           NEW ENTRY")
        print("-" * 40)
        print(f"\nPrompt: {prompt}")
        
        # Get title
        title = input("\nEnter title (or press Enter to use prompt): ").strip()
        if not title:
            title = prompt[:50]  # Use first 50 chars of prompt as title
        
        # Get mood
        print("\nMood options: happy, sad, neutral, excited, anxious,")
        print("              calm, angry, grateful, tired, inspired")
        mood = input("How are you feeling? (press Enter for 'neutral'): ").strip()
        if not mood:
            mood = "neutral"
        
        # Get content
        print("\nWrite your response (type 'END' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        
        content = "\n".join(lines)
        if not content.strip():
            print("Content is required. Entry cancelled.")
            return
        
        # Get tags
        tags_input = input("\nEnter tags (comma-separated, or press Enter to skip): ").strip()
        tags = [t.strip() for t in tags_input.split(",") if t.strip()] if tags_input else []
        
        # Create entry
        entry = self.journal.add_entry(title, content, mood, tags)
        print(f"\nEntry saved! ID: {entry.id}")


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Entry point for the journal application."""
    try:
        app = JournalApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nJournal closed. Your entries are saved!")


if __name__ == "__main__":
    main()
