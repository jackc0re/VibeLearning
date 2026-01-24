# 🎯 File Organizer Challenges

Extend your file organizer with these advanced features for more sophisticated file management.

---

## Challenge 1: Rules Editor

Add a user interface to dynamically edit and manage file type rules.

### Features to Add

1. **Add New Categories** — Create custom categories
2. **Edit Existing Categories** — Modify category names and extensions
3. **Add Extensions** — Add file extensions to categories
4. **Remove Extensions** — Remove extensions from categories
5. **Save and Load Rules** — Persist custom rules to file

### Implementation

```python
class FileOrganizer:
    def add_category(self, category_name):
        """Add a new category."""
        if category_name not in self.categories:
            self.categories[category_name] = []
            self.logger.info(f"Added category: {category_name}")
        else:
            print(f"Category '{category_name}' already exists.")
    
    def add_extension(self, category_name, extension):
        """Add an extension to a category."""
        if not extension.startswith('.'):
            extension = '.' + extension
        
        if category_name in self.categories:
            if extension not in self.categories[category_name]:
                self.categories[category_name].append(extension)
                self.logger.info(f"Added {extension} to {category_name}")
        else:
            print(f"Category '{category_name}' does not exist.")
    
    def remove_extension(self, category_name, extension):
        """Remove an extension from a category."""
        if category_name in self.categories:
            if extension in self.categories[category_name]:
                self.categories[category_name].remove(extension)
                self.logger.info(f"Removed {extension} from {category_name}")
    
    def save_rules(self, filename="organizer_rules.json"):
        """Save current rules to file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.categories, f, indent=2)
            self.logger.info(f"Rules saved to {filename}")
            return True
        except Exception as e:
            self.logger.error(f"Error saving rules: {e}")
            return False
    
    def load_rules(self, filename="organizer_rules.json"):
        """Load rules from file."""
        try:
            with open(filename, 'r') as f:
                self.categories = json.load(f)
            self.logger.info(f"Rules loaded from {filename}")
            return True
        except FileNotFoundError:
            self.logger.info(f"Rules file not found: {filename}")
            return False
        except Exception as e:
            self.logger.error(f"Error loading rules: {e}")
            return False
```

### New Menu Options

- "11. Manage Rules"
- Submenu: Add category, Add extension, Save rules, Load rules

---

## Challenge 2: Recursive Mode

Add ability to organize files in subdirectories recursively.

### Features to Add

1. **Recursive Scan** — Scan all subdirectories
2. **Flattened Organization** — Move all files to root categories
3. **Tree Organization** — Maintain directory structure in categories
4. **Depth Control** — Set maximum recursion depth

### Implementation

```python
class FileOrganizer:
    def __init__(self, source_dir, recursive=False, max_depth=None):
        # ... existing code ...
        self.recursive = recursive
        self.max_depth = max_depth
    
    def get_files_to_organize(self):
        """Get all files including subdirectories if recursive."""
        files = []
        
        if self.recursive:
            for item in self.source_dir.rglob('*'):
                if item.is_file():
                    depth = len(item.relative_to(self.source_dir).parts) - 1
                    if self.max_depth is None or depth <= self.max_depth:
                        if item.suffix.lower() not in IGNORED_EXTENSIONS:
                            files.append(item)
            self.logger.info(f"Recursive scan found {len(files)} files")
        else:
            for item in self.source_dir.iterdir():
                if item.is_file():
                    if item.suffix.lower() not in IGNORED_EXTENSIONS:
                        files.append(item)
        
        return files
    
    def get_relative_path(self, file_path):
        """Get the path relative to source directory."""
        return file_path.relative_to(self.source_dir)
    
    def organize_file_preserving_path(self, file_path, category):
        """Organize file while preserving relative path."""
        category_dir = self.source_dir / category
        
        relative_path = self.get_relative_path(file_path)
        
        if relative_path.parent != Path('.'):
            dest_dir = category_dir / relative_path.parent
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            dest_dir = category_dir
        
        destination = dest_dir / file_path.name
        
        if destination.exists():
            destination = self.get_unique_filename(
                destination,
                file_path.stem,
                file_path.suffix
            )
        
        # ... rest of move logic ...
```

### New Options

- "12. Toggle Recursive Mode"
- "13. Set Recursion Depth"

---

## Challenge 3: File Renaming

Add comprehensive file renaming capabilities.

### Features to Add

1. **Pattern Renaming** — Rename files using patterns (e.g., "IMG_001", "DOC_001")
2. **Case Conversion** — Convert to lowercase, uppercase, title case
3. **Remove Words** — Remove specific words from filenames
4. **Replace Text** — Find and replace text in filenames
5. **Date/Time Stamps** — Add timestamps to filenames

### Implementation

```python
import re

class FileOrganizer:
    def batch_rename(self, files, pattern="{counter:03d}{ext}"):
        """Rename files using a pattern."""
        renamed = 0
        
        for i, file_path in enumerate(files, 1):
            try:
                old_name = file_path.stem
                ext = file_path.suffix
                
                new_name = pattern.format(
                    counter=i,
                    name=old_name,
                    ext=ext,
                    date=datetime.now().strftime('%Y%m%d')
                )
                
                new_path = file_path.parent / (new_name + ext)
                
                if not new_path.exists():
                    if not self.dry_run:
                        shutil.move(file_path, new_path)
                        self.logger.info(f"Renamed: {file_path.name} -> {new_name}{ext}")
                    else:
                        self.logger.info(f"[DRY RUN] Would rename: {file_path.name}")
                    
                    renamed += 1
                    self.operations.append({
                        'action': 'rename',
                        'source': file_path,
                        'destination': new_path,
                        'status': 'success' if not self.dry_run else 'dry_run'
                    })
                else:
                    self.logger.warning(f"File exists: {new_name}{ext}")
            
            except Exception as e:
                self.logger.error(f"Error renaming {file_path.name}: {e}")
        
        return renamed
    
    def remove_words(self, files, words):
        """Remove specified words from filenames."""
        renamed = 0
        
        for file_path in files:
            old_name = file_path.stem
            
            new_name = old_name
            for word in words:
                new_name = new_name.replace(word, '').strip()
            
            new_name = re.sub(r'\s+', '_', new_name)
            
            if new_name != old_name:
                new_path = file_path.parent / (new_name + file_path.suffix)
                
                if not self.dry_run:
                    shutil.move(file_path, new_path)
                else:
                    self.logger.info(f"[DRY RUN] Would rename: {file_path.name} -> {new_name}{file_path.suffix}")
                
                renamed += 1
        
        return renamed
    
    def convert_case(self, files, case_type='lower'):
        """Convert filename case."""
        renamed = 0
        
        for file_path in files:
            old_name = file_path.stem
            
            if case_type == 'lower':
                new_name = old_name.lower()
            elif case_type == 'upper':
                new_name = old_name.upper()
            elif case_type == 'title':
                new_name = old_name.title()
            elif case_type == 'snake':
                new_name = re.sub(r'([a-z])([A-Z])', r'\1_\2', old_name).lower()
            
            new_path = file_path.parent / (new_name + file_path.suffix)
            
            if not self.dry_run:
                shutil.move(file_path, new_path)
            else:
                self.logger.info(f"[DRY RUN] Would rename: {file_path.name}")
            
            renamed += 1
        
        return renamed
```

### New Menu Options

- "14. Batch Rename"
- "15. Convert Case"
- "16. Remove Words"

---

## Challenge 4: Size Limits

Add filtering based on file size.

### Features to Add

1. **Minimum Size Filter** — Only organize files above a certain size
2. **Maximum Size Filter** — Only organize files below a certain size
3. **Size Range** — Filter by size range
4. **Large File Detection** — Identify and report large files

### Implementation

```python
def parse_size(size_str):
    """Parse size string (e.g., '10MB', '1GB') to bytes."""
    size_str = size_str.upper().strip()
    
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
        'TB': 1024 ** 4
    }
    
    for unit, multiplier in sorted(units.items(), key=lambda x: -len(x[1])):
        if size_str.endswith(unit):
            number = float(size_str[:-len(unit)])
            return int(number * multiplier)
    
    try:
        return int(size_str)
    except ValueError:
        return 0


class FileOrganizer:
    def __init__(self, source_dir, min_size=None, max_size=None):
        # ... existing code ...
        self.min_size = min_size
        self.max_size = max_size
    
    def get_files_to_organize(self):
        """Get files filtered by size."""
        all_files = super().get_files_to_organize()
        filtered = []
        
        for file_path in all_files:
            file_size = file_path.stat().st_size
            
            if self.min_size and file_size < self.min_size:
                self.logger.info(f"Skipped (too small): {file_path.name} ({file_size} bytes)")
                continue
            
            if self.max_size and file_size > self.max_size:
                self.logger.info(f"Skipped (too large): {file_path.name} ({file_size} bytes)")
                continue
            
            filtered.append(file_path)
        
        return filtered
    
    def get_large_files(self, threshold='100MB'):
        """Get files larger than threshold."""
        threshold_bytes = parse_size(threshold)
        large_files = []
        
        for file_path in self.source_dir.rglob('*'):
            if file_path.is_file():
                size = file_path.stat().st_size
                if size > threshold_bytes:
                    large_files.append({
                        'path': file_path,
                        'size': size,
                        'size_human': format_size(size)
                    })
        
        return sorted(large_files, key=lambda x: x['size'], reverse=True)


def format_size(size_bytes):
    """Format bytes to human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f}PB"
```

---

## Challenge 5: Date Filtering

Add organization based on file creation/modification dates.

### Features to Add

1. **Organize by Date** — Create folders by date (year, month, day)
2. **Date Range Filter** — Only organize files from specific dates
3. **Recent Files Only** — Organize only recent files
4. **Old Files Only** — Organize only old files

### Implementation

```python
class FileOrganizer:
    def organize_by_date(self, file_path, date_type='modified', date_format='%Y%m'):
        """Organize file by date."""
        if date_type == 'modified':
            file_date = datetime.fromtimestamp(file_path.stat().st_mtime)
        elif date_type == 'created':
            file_date = datetime.fromtimestamp(file_path.st_ctime)
        else:
            file_date = datetime.now()
        
        date_folder = file_date.strftime(date_format)
        
        category = self.get_file_category(file_path)
        destination_dir = self.source_dir / category / date_folder
        
        # ... rest of move logic ...
    
    def filter_by_date_range(self, start_date, end_date):
        """Get files modified within date range."""
        files = []
        
        for file_path in self.source_dir.rglob('*'):
            if file_path.is_file():
                mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                
                if start_date <= mod_time <= end_date:
                    files.append(file_path)
        
        return files
    
    def get_recent_files(self, days=7):
        """Get files modified in the last N days."""
        from datetime import timedelta
        cutoff = datetime.now() - timedelta(days=days)
        return self.filter_by_date_range(cutoff, datetime.now())
    
    def organize_by_month(self):
        """Organize all files into month-based folders within categories."""
        files = self.get_files_to_organize()
        
        for file_path in files:
            category = self.get_file_category(file_path)
            mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
            month_folder = mod_time.strftime('%Y-%m')
            
            category_month_dir = self.source_dir / category / month_folder
            
            # ... move file to category/month/ ...
```

### New Menu Options

- "17. Organize by Date"
- "18. Set Date Range"

---

## Challenge 6: Duplicate Detection

Add duplicate file detection and handling.

### Features to Add

1. **Find Duplicates** — Detect duplicate files by name or content
2. **Hash Comparison** — Compare files using SHA256 hashes
3. **Delete Duplicates** — Remove duplicate files
4. **Move Duplicates** — Move duplicates to separate folder

### Implementation

```python
import hashlib

def compute_file_hash(file_path, chunk_size=8192):
    """Compute SHA256 hash of a file."""
    hasher = hashlib.sha256()
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    
    return hasher.hexdigest()


class FileOrganizer:
    def find_duplicates(self, method='name'):
        """Find duplicate files."""
        duplicates = {}
        
        if method == 'name':
            for file_path in self.source_dir.rglob('*'):
                if file_path.is_file():
                    name = file_path.name
                    if name not in duplicates:
                        duplicates[name] = []
                    duplicates[name].append(file_path)
        
        elif method == 'hash':
            for file_path in self.source_dir.rglob('*'):
                if file_path.is_file():
                    try:
                        file_hash = compute_file_hash(file_path)
                        if file_hash not in duplicates:
                            duplicates[file_hash] = []
                        duplicates[file_hash].append(file_path)
                    except Exception as e:
                        self.logger.error(f"Error hashing {file_path}: {e}")
        
        return {k: v for k, v in duplicates.items() if len(v) > 1}
    
    def handle_duplicates(self, duplicates, action='move'):
        """Handle duplicate files."""
        removed = 0
        
        for dup_hash, files in duplicates.items():
            if len(files) < 2:
                continue
            
            keep = files[0]
            to_process = files[1:]
            
            for file_path in to_process:
                if action == 'delete':
                    if not self.dry_run:
                        file_path.unlink()
                        self.logger.info(f"Deleted duplicate: {file_path}")
                    removed += 1
                
                elif action == 'move':
                    dup_dir = self.source_dir / 'Duplicates'
                    dup_dir.mkdir(exist_ok=True)
                    
                    dest = dup_dir / f"{file_path.stem}_dup{file_path.suffix}"
                    
                    if not self.dry_run:
                        shutil.move(file_path, dest)
                        self.logger.info(f"Moved duplicate: {file_path} -> Duplicates/")
                    removed += 1
        
        return removed
```

### New Menu Options

- "19. Find Duplicates (by Name)"
- "20. Find Duplicates (by Content)"

---

## Challenge 7: Search and Find

Add powerful search capabilities.

### Features to Add

1. **Search by Name** — Find files by name pattern
2. **Search by Content** — Search within text files
3. **Advanced Filters** — Combine multiple filters
4. **Save Searches** — Save frequently used searches

### Implementation

```python
import re

class FileOrganizer:
    def search_files(self, pattern, search_type='name', case_sensitive=False):
        """Search for files matching pattern."""
        results = []
        
        if not case_sensitive:
            pattern = pattern.lower()
        
        for file_path in self.source_dir.rglob('*'):
            if file_path.is_file():
                match = False
                
                if search_type == 'name':
                    name_to_search = file_path.name if case_sensitive else file_path.name.lower()
                    if pattern in name_to_search:
                        match = True
                
                elif search_type == 'regex':
                    try:
                        flags = 0 if case_sensitive else re.IGNORECASE
                        if re.search(pattern, file_path.name, flags):
                            match = True
                    except re.error:
                        pass
                
                elif search_type == 'extension':
                    ext_to_search = file_path.suffix.lower()
                    if pattern.lower() == ext_to_search or pattern.lower() in ext_to_search:
                        match = True
                
                if match:
                    results.append({
                        'path': file_path,
                        'name': file_path.name,
                        'size': file_path.stat().st_size,
                        'modified': datetime.fromtimestamp(file_path.stat().st_mtime)
                    })
        
        return results
    
    def search_content(self, pattern, extensions=None):
        """Search within text files for pattern."""
        results = []
        
        if extensions is None:
            extensions = ['.txt', '.py', '.js', '.html', '.css', '.json', '.md']
        
        for file_path in self.source_dir.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in extensions:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line_num, line in enumerate(f, 1):
                            if pattern.lower() in line.lower():
                                results.append({
                                    'path': file_path,
                                    'line': line_num,
                                    'content': line.strip(),
                                    'name': file_path.name
                                })
                except Exception:
                    pass
        
        return results
```

---

## Challenge 8: Configuration Files

Add support for configuration files to save settings.

### Features to Add

1. **Save Configuration** — Save all organizer settings
2. **Load Configuration** — Load saved settings
3. **Profiles** — Multiple configuration profiles
4. **Presets** — Predefined configurations for common needs

### Implementation

```python
class FileOrganizerConfig:
    """Configuration manager for the file organizer."""
    
    def __init__(self):
        self.categories = DEFAULT_CATEGORIES.copy()
        self.recursive = False
        self.max_depth = None
        self.dry_run = False
        self.min_size = None
        self.max_size = None
        self.ignored_extensions = IGNORED_EXTENSIONS.copy()
    
    def to_dict(self):
        """Convert to dictionary."""
        return {
            'categories': self.categories,
            'recursive': self.recursive,
            'max_depth': self.max_depth,
            'dry_run': self.dry_run,
            'min_size': self.min_size,
            'max_size': self.max_size,
            'ignored_extensions': self.ignored_extensions
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create from dictionary."""
        config = cls()
        config.categories = data.get('categories', {})
        config.recursive = data.get('recursive', False)
        config.max_depth = data.get('max_depth')
        config.dry_run = data.get('dry_run', False)
        config.min_size = data.get('min_size')
        config.max_size = data.get('max_size')
        config.ignored_extensions = data.get('ignored_extensions', [])
        return config
    
    def save(self, filename='organizer_config.json'):
        """Save configuration to file."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load(cls, filename='organizer_config.json'):
        """Load configuration from file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)


PRESETS = {
    'Photos': {
        'categories': {'Photos': ['.jpg', '.jpeg', '.png', '.gif', '.bmp']},
        'recursive': True,
        'ignored_extensions': ['.tmp', '.dshot']
    },
    'Code': {
        'categories': {'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp']},
        'recursive': True
    },
    'Documents': {
        'categories': {'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx']},
        'recursive': False
    }
}
```

---

## 🏆 Challenge Completion

Track your progress:

- [ ] Challenge 1: Rules Editor
- [ ] Challenge 2: Recursive Mode
- [ ] Challenge 3: File Renaming
- [ ] Challenge 4: Size Limits
- [ ] Challenge 5: Date Filtering
- [ ] Challenge 6: Duplicate Detection
- [ ] Challenge 7: Search and Find
- [ ] Challenge 8: Configuration Files

---

**Tip:** Each challenge can be implemented independently. Start with features you find most useful!