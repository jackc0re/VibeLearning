"""
File Organizer
==============
Automatically organize files into folders by type with batch processing and logging.
"""

import os
import shutil
import logging
from pathlib import Path
from datetime import datetime


DEFAULT_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', 
                  '.ppt', '.pptx', '.odf', '.ods', '.odp'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.3gp'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tgz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.php', '.rb', 
             '.go', '.ts', '.tsx', '.jsx', '.vue', '.swift', '.kt', '.rs', '.sh', '.bat'],
    'Data': ['.json', '.xml', '.csv', '.sql', '.db', '.sqlite', '.yaml', '.yml', '.toml'],
    'Executables': ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm', '.apk', '.appimage'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
    'Ebooks': ['.epub', '.mobi', '.azw3', '.lit', '.lrf'],
}

IGNORED_EXTENSIONS = ['.tmp', '.bak', '.swp', '.DS_Store', '.thumbs.db', '.part', '.crdownload']


class FileOrganizer:
    """Main file organizer class."""
    
    def __init__(self, source_dir, categories=None, dry_run=False):
        self.source_dir = Path(source_dir)
        self.categories = categories or DEFAULT_CATEGORIES.copy()
        self.dry_run = dry_run
        self.operations = []
        self.errors = []
        self.start_time = None
        
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
        self.logger.info(f"Mode: {'DRY RUN' if self.dry_run else 'ACTUAL'}")
    
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
    
    def get_unique_filename(self, destination, name, ext):
        """Generate a unique filename if destination already exists."""
        counter = 1
        while destination.exists():
            new_name = f"{name}_{counter}{ext}"
            destination = destination.parent / new_name
            counter += 1
        return destination
    
    def move_file(self, file_path, category):
        """Move a file to its category folder."""
        category_dir = self.source_dir / category
        
        if not category_dir.exists():
            category_dir.mkdir(parents=True, exist_ok=True)
            if not self.dry_run:
                self.logger.info(f"Created directory: {category_dir}")
            else:
                self.logger.info(f"[DRY RUN] Would create directory: {category_dir}")
        
        destination = category_dir / file_path.name
        
        if destination.exists():
            destination = self.get_unique_filename(
                destination, 
                file_path.stem, 
                file_path.suffix
            )
        
        operation = {
            'action': 'move',
            'source': file_path,
            'source_name': file_path.name,
            'destination': destination,
            'category': category,
            'timestamp': datetime.now().isoformat()
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
        self.start_time = datetime.now()
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
        
        elapsed = (datetime.now() - self.start_time).total_seconds()
        self.logger.info(f"Organization complete in {elapsed:.2f} seconds.")
        
        return organized
    
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
    
    def preview_organization(self):
        """Show preview of how files will be organized."""
        files = self.get_files_to_organize()
        
        print("\n" + "=" * 70)
        print(" " * 25 + "ORGANIZATION PREVIEW")
        print("=" * 70)
        
        categories = {}
        for file_path in files:
            category = self.get_file_category(file_path)
            if category not in categories:
                categories[category] = []
            categories[category].append(file_path)
        
        for category in sorted(categories.keys()):
            print(f"\n{category}/ ({len(categories[category])} files)")
            print("-" * 70)
            for i, file_path in enumerate(categories[category], 1):
                print(f"  {i:2d}. {file_path.name}")
        
        print("=" * 70)
        print(f"Total files: {len(files)}")
        print(f"Categories: {len(categories)}")
        print("=" * 70)
        
        return categories
    
    def display_statistics(self):
        """Display statistics of completed operations."""
        print("\n" + "=" * 70)
        print(" " * 25 + "ORGANIZATION STATISTICS")
        print("=" * 70)
        
        total = len(self.operations)
        successful = sum(1 for op in self.operations if op['status'] == 'success')
        errors = len(self.errors)
        dry_run = sum(1 for op in self.operations if op['status'] == 'dry_run')
        
        print(f"\nTotal operations:   {total}")
        print(f"Successful:         {successful}")
        print(f"Dry run:            {dry_run}")
        print(f"Errors:             {errors}")
        
        if self.start_time and successful > 0:
            elapsed = (datetime.now() - self.start_time).total_seconds()
            print(f"Time taken:         {elapsed:.2f} seconds")
            print(f"Time per file:     {elapsed/successful:.3f} seconds")
        
        if self.operations:
            print("\nFiles by category:")
            category_counts = {}
            for op in self.operations:
                category = op['category']
                category_counts[category] = category_counts.get(category, 0) + 1
            
            for category, count in sorted(category_counts.items()):
                bar = '█' * int(count * 50 / max(category_counts.values())) if category_counts else ''
                print(f"  {category:15s}: {count:3d} {bar}")
        
        if self.errors:
            print("\nErrors encountered:")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. ✗ {error}")
        
        print("=" * 70)
    
    def export_report(self, filename="organizer_report.txt"):
        """Export a detailed report of operations."""
        if not filename:
            filename = "organizer_report.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 70 + "\n")
                f.write(" " * 20 + "FILE ORGANIZER REPORT\n")
                f.write("=" * 70 + "\n\n")
                f.write(f"Source Directory: {self.source_dir}\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("OPERATIONS:\n")
                f.write("-" * 70 + "\n")
                
                for i, op in enumerate(self.operations, 1):
                    status_symbol = {
                        'success': '✓',
                        'error': '✗',
                        'dry_run': '○',
                        'undone': '↶'
                    }.get(op['status'], '?')
                    
                    f.write(f"{i:3d}. {status_symbol} {op['source_name']} -> {op['category']}/\n")
                    f.write(f"     Status: {op['status'].upper()}\n")
                    if 'error' in op:
                        f.write(f"     Error: {op['error']}\n")
                    f.write("\n")
                
                f.write("\nSUMMARY:\n")
                f.write("-" * 70 + "\n")
                f.write(f"Total operations: {len(self.operations)}\n")
                f.write(f"Successful: {sum(1 for op in self.operations if op['status'] == 'success')}\n")
                f.write(f"Errors: {len(self.errors)}\n")
            
            self.logger.info(f"Report exported to: {filename}")
            return filename
        except Exception as e:
            self.logger.error(f"Error exporting report: {e}")
            return None


def display_menu():
    """Display main menu."""
    print("\n" + "=" * 40)
    print("     FILE ORGANIZER MENU")
    print("=" * 40)
    print("1. Set Source Directory")
    print("2. Preview Organization")
    print("3. Organize Files")
    print("4. Organize Files (Dry Run)")
    print("5. View Statistics")
    print("6. Undo Last Operation")
    print("7. Undo All Operations")
    print("8. Export Report")
    print("9. View Rules")
    print("10. Exit")
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
            continue
        
        if not path_obj.is_dir():
            print(f"Not a directory: {path}")
            continue
        
        return path_obj


def main():
    """Main application function."""
    print("=" * 40)
    print("       FILE ORGANIZER")
    print("=" * 40)
    print("Automatically organize files by type")
    print("=" * 40)
    
    current_dir = Path.cwd()
    organizer = None
    
    while True:
        display_menu()
        
        if organizer:
            print(f"\nDirectory: {organizer.source_dir}")
        
        try:
            choice = input("\nEnter your choice (1-10): ").strip()
            
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
                elif organizer is None:
                    organizer = FileOrganizer(current_dir)
                    print(f"Using current directory: {current_dir}")
            
            elif choice == 2:
                if not organizer:
                    print("Please set a source directory first.")
                else:
                    organizer.preview_organization()
            
            elif choice == 3:
                if not organizer:
                    print("Please set a source directory first.")
                else:
                    stats, total = organizer.scan_directory()
                    print(f"\nWill organize {total} files:")
                    for category, count in sorted(stats.items()):
                        print(f"  {category}: {count}")
                    
                    confirm = input("\nOrganize files in this directory? (y/n): ").lower()
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
                if not organizer or not organizer.operations:
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
                    if not organizer.operations:
                        print("No operations to undo.")
                        continue
                    confirm = input("Undo all operations? (y/n): ").lower()
                    if confirm == 'y':
                        undone = organizer.undo_all()
                        print(f"Undone {undone} operations!")
            
            elif choice == 8:
                if not organizer:
                    print("No operations performed yet.")
                else:
                    filename = input("Enter report filename (or press Enter for default): ").strip()
                    if not filename:
                        filename = "organizer_report.txt"
                    report_file = organizer.export_report(filename)
                    if report_file:
                        print(f"Report exported to: {report_file}")
            
            elif choice == 9:
                print("\n" + "=" * 60)
                print("Current file type rules:")
                print("=" * 60)
                for category, extensions in DEFAULT_CATEGORIES.items():
                    print(f"\n{category}:")
                    print(f"  {', '.join(extensions)}")
                print("\nIgnored extensions:")
                print(f"  {', '.join(IGNORED_EXTENSIONS)}")
                print("\nTo customize rules, edit DEFAULT_CATEGORIES in the code.")
            
            elif choice == 10:
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 10.")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()