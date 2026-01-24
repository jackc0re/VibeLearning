# 📁 Project 3: File Organizer

Build a utility to automatically organize files into folders by their type, with customizable rules and batch processing capabilities.

---

## 📋 Project Overview

This project helps you practice:
- File system operations using pathlib and os
- Directory tree traversal
- File type detection by extension
- Error handling for file operations
- Logging and debugging
- User interface design

### Features to Build

1. ✅ File Organization
   - Sort files into folders by extension
   - Support common file types (images, documents, videos, etc.)
   - Custom organization rules

2. ✅ Batch Processing
   - Organize entire directories
   - Preview changes before applying
   - Undo functionality

3. ✅ Logging
   - Log all operations
   - Track moved/renamed files
   - Error logging

4. ✅ User Interface
   - Menu-driven interface
   - Progress indicators
   - Clear status messages

---

## 💻 Requirements

### Prerequisites

Complete these modules before starting:
- [00_getting_started](../../00_getting_started/README.md)
- [01_foundations](../../01_foundations/README.md)
- [02_data_structures](../../02_data_structures/README.md)
- [10_file_io](../../10_file_io/README.md)
- [13_modules_packages](../../13_modules_packages/README.md)

### Skills You'll Use

- **pathlib** — Modern path manipulation
- **os and shutil** — File system operations
- **Logging** — Track operations and errors
- **Dictionaries** — Store file type mappings
- **Error handling** — Handle file access errors
- **User interaction** — Command-line interface

---

## 🚀 Development Steps

### Step 1: File Type Mappings (15 minutes)

Create mappings for file types to folders:

```python
import os
import shutil
import logging
from pathlib import Path
from datetime import datetime

DEFAULT_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.php', '.rb', '.go', '.ts'],
    'Data': ['.json', '.xml', '.csv', '.sql', '.db', '.sqlite'],
    'Executables': ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
    'Ebooks': ['.epub', '.mobi', '.azw3', '.pdf'],
}

IGNORED_EXTENSIONS = ['.tmp', '.bak', '.swp', '.DS_Store', '.thumbs.db']
```

### Step 2: FileOrganizer Class (30 minutes)

Create the main organizer class:

```python
class FileOrganizer:
    """Main file organizer class."""
    
    def __init__(self, source_dir, categories=None, dry_run=False):
        self.source_dir = Path(source_dir)
        self.categories = categories or DEFAULT_CATEGORIES.copy()
        self.dry_run = dry_run
        self.operations = []
        self.errors = []
        
        self.setup_logging()
    
    def setup_logging(self):
        """Setup logging for the organizer."""
        log_filename = f"organizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"File Organizer initialized for: {self.source_dir}")
```

### Step 3: File Detection (20 minutes)

Add methods to detect file types:

```python
def get_file_category(self, file_path):
    """Determine the category of a file based on its extension."""
    extension = file_path.suffix.lower()
    
    for category, extensions in self.categories.items():
        if extension in extensions:
            return category
    
    return 'Other'

def get_files_to_organize(self):
    """Get all files that need to be organized."""
    files = []
    
    for item in self.source_dir.iterdir():
        if item.is_file():
            if item.suffix.lower() not in IGNORED_EXTENSIONS:
                files.append(item)
            else:
                self.logger.info(f"Ignoring file: {item.name}")
    
    return files

def scan_directory(self):
    """Scan the source directory and return file statistics."""
    files = self.get_files_to_organize()
    stats = {}
    
    for file_path in files:
        category = self.get_file_category(file_path)
        stats[category] = stats.get(category, 0) + 1
    
    return stats, len(files)
```

### Step 4: File Operations (25 minutes)

Add methods to move files:

```python
def move_file(self, file_path, category):
    """Move a file to its category folder."""
    category_dir = self.source_dir / category
    
    if not category_dir.exists():
        category_dir.mkdir(parents=True, exist_ok=True)
        self.logger.info(f"Created directory: {category_dir}")
    
    destination = category_dir / file_path.name
    
    if destination.exists():
        counter = 1
        name = file_path.stem
        ext = file_path.suffix
        while destination.exists():
            new_name = f"{name}_{counter}{ext}"
            destination = category_dir / new_name
            counter += 1
    
    operation = {
        'action': 'move',
        'source': file_path,
        'destination': destination,
        'category': category
    }
    
    if not self.dry_run:
        try:
            shutil.move(str(file_path), str(destination))
            self.logger.info(f"Moved: {file_path.name} -> {category}/")
            operation['status'] = 'success'
        except Exception as e:
            self.logger.error(f"Error moving {file_path.name}: {e}")
            self.errors.append(str(e))
            operation['status'] = 'error'
            operation['error'] = str(e)
    else:
        self.logger.info(f"[DRY RUN] Would move: {file_path.name} -> {category}/")
        operation['status'] = 'dry_run'
    
    self.operations.append(operation)
    return operation

def organize_files(self):
    """Organize all files in the source directory."""
    files = self.get_files_to_organize()
    
    if not files:
        self.logger.info("No files to organize.")
        return 0
    
    self.logger.info(f"Found {len(files)} files to organize.")
    
    organized = 0
    for file_path in files:
        category = self.get_file_category(file_path)
        operation = self.move_file(file_path, category)
        if operation['status'] in ['success', 'dry_run']:
            organized += 1
    
    return organized
```

### Step 5: Preview and Statistics (20 minutes)

Add methods to show what will happen:

```python
def preview_organization(self):
    """Show preview of how files will be organized."""
    files = self.get_files_to_organize()
    
    print("\n" + "=" * 60)
    print(" ORGANIZATION PREVIEW")
    print("=" * 60)
    
    categories = {}
    for file_path in files:
        category = self.get_file_category(file_path)
        if category not in categories:
            categories[category] = []
        categories[category].append(file_path)
    
    for category in sorted(categories.keys()):
        print(f"\n{category}/")
        print("-" * 60)
        for file_path in categories[category]:
            print(f"  {file_path.name}")
    
    print("=" * 60)
    print(f"Total files: {len(files)}")
    print(f"Categories: {len(categories)}")
    print("=" * 60)
    
    return categories

def display_statistics(self):
    """Display statistics of completed operations."""
    print("\n" + "=" * 60)
    print(" ORGANIZATION STATISTICS")
    print("=" * 60)
    
    total = len(self.operations)
    successful = sum(1 for op in self.operations if op['status'] == 'success')
    errors = len(self.errors)
    
    print(f"\nTotal operations: {total}")
    print(f"Successful: {successful}")
    print(f"Errors: {errors}")
    
    if self.operations:
        print("\nFiles by category:")
        category_counts = {}
        for op in self.operations:
            category = op['category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        for category, count in sorted(category_counts.items()):
            print(f"  {category}: {count}")
    
    if self.errors:
        print("\nErrors encountered:")
        for error in self.errors:
            print(f"  ✗ {error}")
    
    print("=" * 60)
```

### Step 6: Undo Functionality (15 minutes)

Add ability to undo operations:

```python
def undo_last_operation(self):
    """Undo the last move operation."""
    if not self.operations:
        self.logger.info("No operations to undo.")
        return False
    
    last_op = self.operations[-1]
    
    if last_op['status'] != 'success':
        self.logger.info("Last operation was not successful, cannot undo.")
        return False
    
    source = last_op['destination']
    destination = last_op['source']
    
    if not source.exists():
        self.logger.error(f"Source file not found: {source}")
        return False
    
    try:
        shutil.move(str(source), str(destination))
        self.logger.info(f"Undone: Moved {source.name} back to parent directory")
        last_op['status'] = 'undone'
        return True
    except Exception as e:
        self.logger.error(f"Error undoing operation: {e}")
        return False

def undo_all(self):
    """Undo all successful operations."""
    undone = 0
    
    for _ in range(len(self.operations)):
        if self.undo_last_operation():
            undone += 1
    
    return undone
```

### Step 7: Main Application (30 minutes)

Create the main menu and application loop:

```python
def display_menu():
    """Display main menu."""
    print("\n" + "=" * 40)
    print("    FILE ORGANIZER MENU")
    print("=" * 40)
    print("1. Set Source Directory")
    print("2. Preview Organization")
    print("3. Organize Files")
    print("4. Organize Files (Dry Run)")
    print("5. View Statistics")
    print("6. Undo Last Operation")
    print("7. Undo All Operations")
    print("8. Change Rules")
    print("9. Exit")
    print("=" * 40)

def get_directory_input(prompt):
    """Get directory path from user with validation."""
    while True:
        path = input(prompt).strip()
        if not path:
            return None
        
        path_obj = Path(path)
        if not path_obj.exists():
            print(f"Directory does not exist: {path}")
        elif not path_obj.is_dir():
            print(f"Not a directory: {path}")
        else:
            return path_obj

def main():
    """Main application function."""
    print("=" * 40)
    print("      FILE ORGANIZER")
    print("=" * 40)
    print("Automatically organize files by type")
    print("=" * 40)
    
    current_dir = Path.cwd()
    organizer = None
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-9): ").strip()
            
            if not choice.isdigit():
                print("Please enter a number.")
                continue
            
            choice = int(choice)
            
            if choice == 1:
                print(f"\nCurrent directory: {current_dir}")
                new_dir = get_directory_input("Enter directory path (or press Enter to keep current): ")
                if new_dir:
                    current_dir = new_dir
                    organizer = FileOrganizer(current_dir)
                    print(f"Source directory set to: {current_dir}")
            
            elif choice == 2:
                if not organizer:
                    print("Please set a source directory first.")
                else:
                    organizer.preview_organization()
            
            elif choice == 3:
                if not organizer:
                    print("Please set a source directory first.")
                else:
                    confirm = input("Organize files in this directory? (y/n): ").lower()
                    if confirm == 'y':
                        organized = organizer.organize_files()
                        print(f"\nOrganized {organized} files!")
                        organizer.display_statistics()
            
            elif choice == 4:
                if not organizer:
                    print("Please set a source directory first.")
                else:
                    print("\nDRY RUN MODE - No files will be moved")
                    organizer.dry_run = True
                    organized = organizer.organize_files()
                    print(f"\nWould organize {organized} files (dry run)")
                    organizer.display_statistics()
                    organizer.dry_run = False
            
            elif choice == 5:
                if not organizer:
                    print("No operations performed yet.")
                else:
                    organizer.display_statistics()
            
            elif choice == 6:
                if not organizer:
                    print("No operations performed yet.")
                else:
                    if organizer.undo_last_operation():
                        print("Last operation undone!")
                    else:
                        print("Could not undo last operation.")
            
            elif choice == 7:
                if not organizer:
                    print("No operations performed yet.")
                else:
                    confirm = input("Undo all operations? (y/n): ").lower()
                    if confirm == 'y':
                        undone = organizer.undo_all()
                        print(f"Undone {undone} operations!")
            
            elif choice == 8:
                print("\n" + "=" * 40)
                print("Current file type rules:")
                print("=" * 40)
                for category, extensions in DEFAULT_CATEGORIES.items():
                    print(f"\n{category}:")
                    print(f"  {', '.join(extensions)}")
                print("\nTo customize rules, edit the DEFAULT_CATEGORIES in the code.")
            
            elif choice == 9:
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

---

## 🧪 Testing

Test your organizer with these scenarios:

1. **Basic Organization**
   - Create test directory with various file types
   - Preview organization
   - Organize files
   - Verify files are in correct folders

2. **Dry Run Mode**
   - Test with dry run enabled
   - Verify no files are actually moved
   - Check log messages

3. **Duplicate Handling**
   - Create files with same names in different categories
   - Organize and verify renaming

4. **Error Handling**
   - Try organizing without permissions
   - Test with invalid directories
   - Verify error logging

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How to use pathlib for path manipulation
- ✅ How to iterate through directories
- ✅ How to move and copy files with shutil
- ✅ How to handle file system errors
- ✅ How to implement logging
- ✅ How to create a CLI application
- ✅ How to design a file management utility

---

## 🏆 Challenges

Complete these challenges to enhance your file organizer:

1. **Rules Editor** — Add UI to edit file type rules
2. **Recursive Mode** — Organize files in subdirectories
3. **File Renaming** — Add file renaming capabilities
4. **Size Limits** — Filter files by size
5. **Date Filtering** — Organize by creation/modification date
6. **Conflict Resolution** — More options for handling duplicates
7. **Batch Rename** — Rename multiple files with patterns
8. **Search and Find** — Find files by pattern

See [challenges.md](challenges.md) for detailed instructions.

---

## 📁 File Structure

```
03_file_organizer/
├── README.md          # This file
├── organizer.py       # Your main implementation
└── challenges.md      # Additional challenge tasks
```

---

**Ready to start?** Create `organizer.py` and begin building! 🚀