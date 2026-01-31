"""
Pathlib Module - Examples
=========================
Object-oriented filesystem paths.
"""

print("=" * 60)
print("PATHLIB MODULE - Examples")
print("=" * 60)

from pathlib import Path
import tempfile
import os

# =============================================================================
# CREATING PATHS
# =============================================================================
print("\n--- Creating Paths ---\n")

# Current working directory
cwd = Path.cwd()
print(f"Current directory: {cwd}")

# Home directory
home = Path.home()
print(f"Home directory: {home}")

# Building paths with /
config_path = Path('config') / 'app' / 'settings.json'
print(f"\nBuilt path: {config_path}")
print(f"Absolute: {config_path.absolute()}")

# From string
readme = Path('README.md')
print(f"\nFrom string: {readme}")

# =============================================================================
# PATH COMPONENTS
# =============================================================================
print("\n--- Path Components ---\n")

# Create an example path
p = Path('/home/user/documents/report.pdf')
# For Windows demonstration, let's use a different approach
if os.name == 'nt':
    p = Path('C:/Users/user/documents/report.pdf')

print(f"Full path: {p}")
print(f"  name: {p.name}")       # Filename with extension
print(f"  stem: {p.stem}")       # Filename without extension
print(f"  suffix: {p.suffix}")   # Extension
print(f"  suffixes: {p.suffixes}")  # All extensions
print(f"  parent: {p.parent}")   # Parent directory
print(f"  parents[0]: {p.parents[0]}")
print(f"  parts: {p.parts}")     # Path components
print(f"  anchor: {p.anchor}")   # Root/drive

# =============================================================================
# CHECKING PATHS
# =============================================================================
print("\n--- Checking Paths ---\n")

# Check various properties
test_paths = [
    Path('README.md'),
    Path('.'),
    Path('nonexistent.txt'),
]

for p in test_paths:
    print(f"\nPath: {p}")
    print(f"  exists: {p.exists()}")
    print(f"  is_file: {p.is_file()}")
    print(f"  is_dir: {p.is_dir()}")
    print(f"  is_absolute: {p.is_absolute()}")

    if p.exists() and p.is_file():
        stat = p.stat()
        print(f"  size: {stat.st_size} bytes")
        print(f"  modified: {stat.st_mtime}")

# =============================================================================
# READING AND WRITING FILES
# =============================================================================
print("\n--- Reading and Writing Files ---\n")

# Create a temporary directory for examples
with tempfile.TemporaryDirectory() as tmpdir:
    tmp_path = Path(tmpdir)

    # Write text
    text_file = tmp_path / 'example.txt'
    text_file.write_text('Hello, Pathlib!\nSecond line.', encoding='utf-8')
    print(f"Created: {text_file}")

    # Read text
    content = text_file.read_text(encoding='utf-8')
    print(f"Content: {repr(content)}")

    # Read lines
    lines = content.splitlines()
    print(f"Lines: {lines}")

    # Write bytes
    bin_file = tmp_path / 'data.bin'
    bin_file.write_bytes(b'\x00\x01\x02\x03')
    print(f"\nCreated binary: {bin_file}")
    print(f"Bytes: {bin_file.read_bytes()}")

# =============================================================================
# DIRECTORY OPERATIONS
# =============================================================================
print("\n--- Directory Operations ---\n")

with tempfile.TemporaryDirectory() as tmpdir:
    base = Path(tmpdir)

    # Create directory
    new_dir = base / 'my_folder'
    new_dir.mkdir()
    print(f"Created directory: {new_dir}")

    # Create nested directories
    nested = base / 'a' / 'b' / 'c'
    nested.mkdir(parents=True, exist_ok=True)
    print(f"Created nested: {nested}")

    # Create some files
    (base / 'file1.txt').write_text('content1')
    (base / 'file2.py').write_text('content2')
    (new_dir / 'file3.txt').write_text('content3')

    # List directory
    print(f"\nContents of {base}:")
    for item in base.iterdir():
        item_type = 'DIR' if item.is_dir() else 'FILE'
        print(f"  [{item_type}] {item.name}")

# =============================================================================
# GLOB PATTERNS
# =============================================================================
print("\n--- Glob Patterns ---\n")

# List Python files in current directory
cwd = Path('.')
py_files = list(cwd.glob('*.py'))
print(f"Python files here: {len(py_files)}")
for f in py_files[:5]:  # Show first 5
    print(f"  {f}")

# Recursive search
all_md = list(cwd.rglob('*.md'))
print(f"\nTotal .md files in project: {len(all_md)}")

# Pattern matching
for p in [Path('document.txt'), Path('script.py'), Path('README.md')]:
    print(f"{p.name} matches '*.txt': {p.match('*.txt')}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n--- Practical Examples ---\n")

# Example 1: Find all files by extension
def find_files_by_extension(start_path, extension):
    """Find all files with given extension recursively."""
    return list(Path(start_path).rglob(f'*.{extension}'))

# Example 2: Get file sizes
def get_file_sizes(directory):
    """Get sizes of all files in directory."""
    sizes = {}
    for file_path in Path(directory).rglob('*'):
        if file_path.is_file():
            sizes[file_path] = file_path.stat().st_size
    return sizes

# Example 3: Safe file writer
def safe_write(path, content, backup=True):
    """Write file with optional backup of existing file."""
    path = Path(path)
    if backup and path.exists():
        backup_path = path.with_suffix(path.suffix + '.backup')
        path.rename(backup_path)
        print(f"Backed up to: {backup_path}")
    path.write_text(content, encoding='utf-8')
    print(f"Written to: {path}")

# Example 4: Directory tree printer
def print_tree(path, prefix='', max_depth=3, current_depth=0):
    """Print directory tree structure."""
    if current_depth > max_depth:
        return

    path = Path(path)
    if not path.is_dir():
        return

    items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        connector = '└── ' if is_last else '├── '
        print(f"{prefix}{connector}{item.name}")

        if item.is_dir():
            extension = '    ' if is_last else '│   '
            print_tree(item, prefix + extension, max_depth, current_depth + 1)

# Example 5: Batch rename
def batch_rename(directory, old_ext, new_ext):
    """Rename all files with old_ext to new_ext."""
    count = 0
    for file_path in Path(directory).glob(f'*.{old_ext}'):
        new_path = file_path.with_suffix(f'.{new_ext}')
        file_path.rename(new_path)
        count += 1
    return count

# Demo with temp directory
with tempfile.TemporaryDirectory() as tmpdir:
    base = Path(tmpdir)

    # Create test structure
    (base / 'docs').mkdir()
    (base / 'docs' / 'readme.txt').write_text('Hello')
    (base / 'docs' / 'notes.txt').write_text('Notes')
    (base / 'src').mkdir()
    (base / 'src' / 'main.py').write_text('print("hi")')

    print("Directory tree:")
    print_tree(base, max_depth=2)

    print(f"\nText files found: {len(find_files_by_extension(base, 'txt'))}")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
