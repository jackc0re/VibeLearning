"""
Pathlib Module - Exercises
==========================
Practice problems for pathlib.
"""

print("=" * 60)
print("PATHLIB MODULE - Exercises")
print("=" * 60)

from pathlib import Path
import tempfile

# =============================================================================
# EXERCISE 1: Path Builder
# =============================================================================
print("\n--- Exercise 1: Path Builder ---\n")
"""
Write a function that builds a configuration file path based on:
- Application name
- Configuration directory (default: ~/.config)
- Environment (dev, prod, test)

The path should be: config_dir / app_name / f"config.{environment}.json"
"""

def build_config_path(app_name, environment='dev', config_dir=None):
    """
    Build configuration file path.
    If config_dir is None, use user's home directory + .config
    """
    # Your code here
    # Determine config_dir if not provided
    # Build path using / operator
    # Return the Path object
    pass  # TODO: Implement

# Test
# print(build_config_path('myapp', 'prod'))
# print(build_config_path('myapp', 'dev', Path('/custom/config')))

# =============================================================================
# EXERCISE 2: File Organizer
# =============================================================================
print("\n--- Exercise 2: File Organizer ---\n")
"""
Write a function that organizes files in a directory by extension.
Create subdirectories for each extension and move files into them.

Example:
    Before: dir/file.txt, dir/file.py, dir/other.txt
    After:  dir/txt/file.txt, dir/txt/other.txt, dir/py/file.py
"""

def organize_by_extension(directory):
    """
    Organize files in directory by their extension.
    Create subdirectories and move files.
    Return count of files moved.
    """
    # Your code here
    # Iterate through files in directory
    # Skip directories
    # Create extension subdirectory if needed
    # Move file to subdirectory
    pass  # TODO: Implement

# Test in temp directory
# with tempfile.TemporaryDirectory() as tmpdir:
#     base = Path(tmpdir)
#     (base / 'doc.txt').write_text('text')
#     (base / 'script.py').write_text('python')
#     (base / 'notes.txt').write_text('more text')
#     count = organize_by_extension(base)
#     print(f"Moved {count} files")

# =============================================================================
# EXERCISE 3: Duplicate File Finder
# =============================================================================
print("\n--- Exercise 3: Duplicate File Finder ---\n")
"""
Write a function that finds duplicate files in a directory tree based on:
1. File size first (quick check)
2. Content hash (if sizes match)

Return groups of duplicate files.
"""

def find_duplicates(directory):
    """
    Find duplicate files in directory tree.
    Return dict: {hash: [file_paths]}
    Only include groups with 2+ files.
    """
    # Your code here
    # Group files by size first
    # For groups with multiple files, compare by content
    # Return groups of actual duplicates
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 4: Log File Analyzer
# =============================================================================
print("\n--- Exercise 4: Log File Analyzer ---\n")
"""
Write a function that analyzes log files in a directory:
- Count total lines across all .log files
- Find the largest log file
- Calculate total size of all logs
"""

def analyze_logs(log_directory):
    """
    Analyze log files in directory.
    Return dict with:
    - total_files
    - total_lines
    - total_size_bytes
    - largest_file (path)
    - largest_size
    """
    # Your code here
    # Find all .log files
    # Count lines in each
    # Track sizes
    # Return summary statistics
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 5: Safe File Operations
# =============================================================================
print("\n--- Exercise 5: Safe File Operations ---\n")
"""
Write a function that safely writes content to a file:
- Creates parent directories if they don't exist
- Creates backup of existing file
- Writes atomically (temp file then rename)
- Returns True on success, False on failure
"""

def safe_write_file(path, content, backup=True):
    """
    Safely write content to file.
    - Create directories
    - Backup existing
    - Atomic write
    """
    # Your code here
    # Create parent directories
    # Backup if needed
    # Write to temp file then rename (atomic)
    # Handle errors gracefully
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 6: Project Structure Validator
# =============================================================================
print("\n--- Exercise 6: Project Structure Validator ---\n")
"""
Write a function that validates a Python project structure:
- Must have README.md
- Must have at least one .py file
- Must not have __pycache__ directories
- Returns (is_valid, list_of_issues)
"""

def validate_project(project_path):
    """
    Validate Python project structure.
    Return (is_valid, issues_list).
    """
    # Your code here
    # Check for README.md
    # Check for .py files
    # Check for __pycache__
    # Return validation result
    pass  # TODO: Implement

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# =============================================================================
# SOLUTION 1: Path Builder
# =============================================================================
print("\n--- Solution 1: Path Builder ---\n")

def build_config_path_solution(app_name, environment='dev', config_dir=None):
    if config_dir is None:
        config_dir = Path.home() / '.config'
    return config_dir / app_name / f"config.{environment}.json"

print(build_config_path_solution('myapp', 'prod'))
print(build_config_path_solution('myapp', 'dev', Path('/custom/config')))

# =============================================================================
# SOLUTION 2: File Organizer
# =============================================================================
print("\n--- Solution 2: File Organizer ---\n")

def organize_by_extension_solution(directory):
    directory = Path(directory)
    moved = 0

    for file_path in directory.iterdir():
        if file_path.is_file():
            ext = file_path.suffix.lstrip('.') or 'no_extension'
            dest_dir = directory / ext
            dest_dir.mkdir(exist_ok=True)

            dest_path = dest_dir / file_path.name
            file_path.rename(dest_path)
            moved += 1

    return moved

with tempfile.TemporaryDirectory() as tmpdir:
    base = Path(tmpdir)
    (base / 'doc.txt').write_text('text')
    (base / 'script.py').write_text('python')
    (base / 'notes.txt').write_text('more text')
    (base / 'archive.tar.gz').write_text('archive')

    count = organize_by_extension_solution(base)
    print(f"Moved {count} files")

    # Show structure
    for item in base.rglob('*'):
        if item.is_file():
            print(f"  {item.relative_to(base)}")

# =============================================================================
# SOLUTION 3: Duplicate File Finder (simplified)
# =============================================================================
print("\n--- Solution 3: Duplicate File Finder ---\n")

import hashlib

def file_hash(file_path):
    """Compute MD5 hash of file content."""
    h = hashlib.md5()
    h.update(file_path.read_bytes())
    return h.hexdigest()

def find_duplicates_solution(directory):
    directory = Path(directory)
    files_by_size = {}

    # Group by size
    for file_path in directory.rglob('*'):
        if file_path.is_file():
            size = file_path.stat().st_size
            files_by_size.setdefault(size, []).append(file_path)

    # For groups with same size, check hash
    duplicates = {}
    for size, files in files_by_size.items():
        if len(files) > 1:
            for f in files:
                h = file_hash(f)
                duplicates.setdefault(h, []).append(f)

    # Return only actual duplicates
    return {h: files for h, files in duplicates.items() if len(files) > 1}

with tempfile.TemporaryDirectory() as tmpdir:
    base = Path(tmpdir)
    (base / 'file1.txt').write_text('duplicate content')
    (base / 'file2.txt').write_text('duplicate content')
    (base / 'file3.txt').write_text('unique content')

    dups = find_duplicates_solution(base)
    print(f"Found {len(dups)} duplicate groups:")
    for h, files in dups.items():
        print(f"  Hash {h[:8]}...: {[f.name for f in files]}")

# =============================================================================
# SOLUTION 4: Log File Analyzer
# =============================================================================
print("\n--- Solution 4: Log File Analyzer ---\n")

def analyze_logs_solution(log_directory):
    log_directory = Path(log_directory)
    log_files = list(log_directory.rglob('*.log'))

    total_lines = 0
    total_size = 0
    largest_file = None
    largest_size = 0

    for log_file in log_files:
        size = log_file.stat().st_size
        total_size += size

        if size > largest_size:
            largest_size = size
            largest_file = log_file

        # Count lines
        try:
            lines = len(log_file.read_text().splitlines())
            total_lines += lines
        except:
            pass

    return {
        'total_files': len(log_files),
        'total_lines': total_lines,
        'total_size_bytes': total_size,
        'largest_file': largest_file,
        'largest_size': largest_size,
    }

with tempfile.TemporaryDirectory() as tmpdir:
    base = Path(tmpdir)
    (base / 'app.log').write_text("Line 1\nLine 2\nLine 3")
    (base / 'error.log').write_text("Error 1\nError 2")

    stats = analyze_logs_solution(base)
    print(f"Total files: {stats['total_files']}")
    print(f"Total lines: {stats['total_lines']}")
    print(f"Total size: {stats['total_size_bytes']} bytes")
    print(f"Largest: {stats['largest_file'].name if stats['largest_file'] else None}")

# =============================================================================
# SOLUTION 5: Safe File Operations
# =============================================================================
print("\n--- Solution 5: Safe File Operations ---\n")

def safe_write_file_solution(path, content, backup=True):
    try:
        path = Path(path)

        # Create parent directories
        path.parent.mkdir(parents=True, exist_ok=True)

        # Backup existing
        if backup and path.exists():
            backup_path = path.with_suffix(path.suffix + '.backup')
            path.rename(backup_path)

        # Write to temp file
        temp_path = path.with_suffix(path.suffix + '.tmp')
        temp_path.write_text(content, encoding='utf-8')

        # Atomic rename
        temp_path.rename(path)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

with tempfile.TemporaryDirectory() as tmpdir:
    test_file = Path(tmpdir) / 'subdir' / 'test.txt'

    # First write
    result = safe_write_file_solution(test_file, 'First content')
    print(f"First write: {result}")
    print(f"Content: {test_file.read_text()}")

    # Second write (creates backup)
    result = safe_write_file_solution(test_file, 'Second content')
    print(f"Second write: {result}")
    print(f"Content: {test_file.read_text()}")

# =============================================================================
# SOLUTION 6: Project Structure Validator
# =============================================================================
print("\n--- Solution 6: Project Structure Validator ---\n")

def validate_project_solution(project_path):
    project_path = Path(project_path)
    issues = []

    # Check for README
    readme = project_path / 'README.md'
    if not readme.exists():
        issues.append("Missing README.md")

    # Check for Python files
    py_files = list(project_path.rglob('*.py'))
    if not py_files:
        issues.append("No Python files found")

    # Check for __pycache__
    pycache_dirs = list(project_path.rglob('__pycache__'))
    if pycache_dirs:
        issues.append(f"Found __pycache__ directories: {len(pycache_dirs)}")

    return (len(issues) == 0, issues)

with tempfile.TemporaryDirectory() as tmpdir:
    base = Path(tmpdir)

    # Invalid project
    (base / 'random.txt').write_text('text')
    is_valid, issues = validate_project_solution(base)
    print(f"Invalid project: {is_valid}, issues: {issues}")

    # Valid project
    (base / 'README.md').write_text('# Project')
    (base / 'main.py').write_text('print("hello")')
    is_valid, issues = validate_project_solution(base)
    print(f"Valid project: {is_valid}, issues: {issues}")

print("\n" + "=" * 60)
print("Exercises complete!")
print("=" * 60)
