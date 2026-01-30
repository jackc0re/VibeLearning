"""
Todo App
========
A task management application with file persistence, priorities, and search features.
"""

import json
from datetime import datetime, timedelta


class Task:
    """Represents a single task in the todo list."""
    
    def __init__(self, description, priority="Medium", due_date=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now()
    
    def mark_complete(self):
        """Mark task as completed."""
        self.completed = True
    
    def mark_incomplete(self):
        """Mark task as incomplete."""
        self.completed = False
    
    def is_overdue(self):
        """Check if task is overdue."""
        if self.due_date and not self.completed:
            return datetime.now() > self.due_date
        return False
    
    def to_dict(self):
        """Convert task to dictionary for JSON serialization."""
        return {
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary."""
        task = cls(data['description'], data['priority'])
        if data['due_date']:
            task.due_date = datetime.fromisoformat(data['due_date'])
        task.completed = data['completed']
        task.created_at = datetime.fromisoformat(data['created_at'])
        return task


class TodoApp:
    """Main todo application class."""
    
    PRIORITY_ORDER = {'High': 1, 'Medium': 2, 'Low': 3}
    PRIORITY_COLORS = {'High': '🔴', 'Medium': '🟡', 'Low': '🟢'}
    
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()
    
    def add_task(self, description, priority="Medium", due_date=None):
        """Add a new task."""
        task = Task(description, priority, due_date)
        self.tasks.append(task)
    
    def get_task(self, index):
        """Get task by index (1-based for user)."""
        if 1 <= index <= len(self.tasks):
            return self.tasks[index - 1]
        return None
    
    def delete_task(self, index):
        """Delete task by index."""
        if self.get_task(index):
            del self.tasks[index - 1]
            return True
        return False
    
    def toggle_task(self, index):
        """Toggle task completion status."""
        task = self.get_task(index)
        if task:
            if task.completed:
                task.mark_incomplete()
            else:
                task.mark_complete()
            return True
        return False
    
    def edit_task(self, index, new_description, new_priority=None, new_due_date=None):
        """Edit task details."""
        task = self.get_task(index)
        if task:
            task.description = new_description
            if new_priority:
                task.priority = new_priority
            if new_due_date is not None:
                task.due_date = new_due_date
            return True
        return False
    
    def search_tasks(self, query):
        """Search tasks by description."""
        query = query.lower()
        return [task for task in self.tasks if query in task.description.lower()]
    
    def filter_by_status(self, status=None):
        """Filter tasks by completion status."""
        if status is None:
            return self.tasks[:]
        if status == 'complete':
            return [task for task in self.tasks if task.completed]
        elif status == 'incomplete':
            return [task for task in self.tasks if not task.completed]
        return []
    
    def filter_by_priority(self, priority):
        """Filter tasks by priority."""
        return [task for task in self.tasks if task.priority == priority]
    
    def get_overdue_tasks(self):
        """Get all overdue incomplete tasks."""
        return [task for task in self.tasks if task.is_overdue()]
    
    def sort_tasks(self, by='priority'):
        """Sort tasks by specified field."""
        sorted_tasks = self.tasks[:]
        if by == 'priority':
            sorted_tasks.sort(key=lambda t: (self.PRIORITY_ORDER.get(t.priority, 99), not t.completed))
        elif by == 'due_date':
            sorted_tasks.sort(key=lambda t: (t.due_date if t.due_date else datetime.max, not t.completed))
        elif by == 'status':
            sorted_tasks.sort(key=lambda t: t.completed)
        elif by == 'created':
            sorted_tasks.sort(key=lambda t: t.created_at, reverse=True)
        return sorted_tasks
    
    def save_tasks(self):
        """Save tasks to file."""
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def load_tasks(self):
        """Load tasks from file."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            self.tasks = []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
    
    def backup_tasks(self):
        """Create a backup of current tasks."""
        backup_filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(backup_filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            return backup_filename
        except Exception as e:
            print(f"Error creating backup: {e}")
            return None
    
    def get_statistics(self):
        """Get task statistics."""
        complete = sum(1 for task in self.tasks if task.completed)
        incomplete = len(self.tasks) - complete
        overdue = sum(1 for task in self.tasks if task.is_overdue())
        high_priority = sum(1 for task in self.tasks if task.priority == 'High' and not task.completed)
        return {
            'total': len(self.tasks),
            'complete': complete,
            'incomplete': incomplete,
            'overdue': overdue,
            'high_priority': high_priority
        }
    
    def display_tasks(self, tasks=None):
        """Display tasks in a formatted list."""
        if tasks is None:
            tasks = self.tasks
        
        if not tasks:
            print("\nNo tasks to display.")
            return
        
        print("\n" + "=" * 80)
        print(" " * 25 + "TASK LIST")
        print("=" * 80)
        print(f"{'#':<4} {'Status':<8} {'Priority':<10} {'Description':<35} {'Due':<12} {'Created':<12}")
        print("-" * 80)
        
        for i, task in enumerate(tasks, 1):
            status = "✓" if task.completed else "○"
            priority_icon = self.PRIORITY_COLORS.get(task.priority, '⚪')
            
            due_str = ""
            if task.due_date:
                due_str = task.due_date.strftime("%b %d")
                if task.is_overdue():
                    due_str += "!"
            
            created_str = task.created_at.strftime("%b %d")
            desc = task.description[:32] + "..." if len(task.description) > 32 else task.description
            
            print(f"{i:<4} {status:<8} {priority_icon} {task.priority:<8} {desc:<35} {due_str:<12} {created_str:<12}")
        
        print("=" * 80)
        stats = self.get_statistics()
        print(f"Total: {stats['total']} | Complete: {stats['complete']} | Incomplete: {stats['incomplete']} | Overdue: {stats['overdue']}")
        print("    " + f"Priority Distribution: Low 🟢 {sum(1 for t in tasks if t.priority == 'Low')} | Medium 🟡 {sum(1 for t in tasks if t.priority == 'Medium')} | High 🔴 {sum(1 for t in tasks if t.priority == 'High')}")
    
    def display_menu(self):
        """Display main menu."""
        print("\n" + "=" * 40)
        print("         TODO APP MENU")
        print("=" * 40)
        print("1. View All Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Toggle Task Status")
        print("6. Search Tasks")
        print("7. Filter Tasks")
        print("8. Sort Tasks")
        print("9. Show Statistics")
        print("10. Save Tasks")
        print("11. Create Backup")
        print("12. Exit")
        print("=" * 40)


def get_priority_choice():
    """Get priority choice from user."""
    priorities = ['High', 'Medium', 'Low']
    for i, p in enumerate(priorities, 1):
        icon = TodoApp.PRIORITY_COLORS[p]
        print(f"{i}. {icon} {p}")
    
    while True:
        try:
            choice = int(input(f"Select priority (1-{len(priorities)}): "))
            if 1 <= choice <= len(priorities):
                return priorities[choice - 1]
            print(f"Please enter a number between 1 and {len(priorities)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_due_date():
    """Get due date from user."""
    while True:
        due_str = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
        if not due_str:
            return None
        try:
            return datetime.strptime(due_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD (e.g., 2024-12-25)")


def main():
    """Run the todo application."""
    app = TodoApp()
    
    print("=" * 40)
    print("       WELCOME TO TODO APP")
    print("=" * 40)
    print("Your tasks have been loaded!")
    
    while True:
        app.display_menu()
        
        try:
            choice = input("\nEnter your choice (1-12): ").strip()
            if not choice.isdigit():
                print("Please enter a number.")
                continue
            
            choice = int(choice)
            
            if choice == 1:
                app.display_tasks()
            
            elif choice == 2:
                print("\n--- Add New Task ---")
                desc = input("Enter task description: ").strip()
                if desc:
                    print("\nSelect priority:")
                    priority = get_priority_choice()
                    due_date = get_due_date()
                    app.add_task(desc, priority, due_date)
                    print("Task added successfully!")
                else:
                    print("Task description cannot be empty.")
            
            elif choice == 3:
                app.display_tasks()
                if not app.tasks:
                    continue
                try:
                    index = int(input("\nEnter task number to edit: "))
                    task = app.get_task(index)
                    if task:
                        print(f"\nCurrent task: {task.description}")
                        new_desc = input(f"New description [{task.description}]: ").strip()
                        new_priority = None
                        change_priority = input("Change priority? (y/n): ").lower() == 'y'
                        if change_priority:
                            print("\nSelect new priority:")
                            new_priority = get_priority_choice()
                        new_due_date = None
                        change_due = input("Change due date? (y/n): ").lower() == 'y'
                        if change_due:
                            new_due_date = get_due_date()
                        
                        app.edit_task(index, new_desc or task.description, new_priority, new_due_date)
                        print("Task updated successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid task number.")
            
            elif choice == 4:
                app.display_tasks()
                if not app.tasks:
                    continue
                try:
                    index = int(input("\nEnter task number to delete: "))
                    if app.delete_task(index):
                        print("Task deleted successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid task number.")
            
            elif choice == 5:
                app.display_tasks()
                if not app.tasks:
                    continue
                try:
                    index = int(input("\nEnter task number to toggle status: "))
                    if app.toggle_task(index):
                        task = app.get_task(index)
                        status = "completed" if task.completed else "incomplete"
                        print(f"Task marked as {status}!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid task number.")
            
            elif choice == 6:
                query = input("\nEnter search term: ").strip().lower()
                results = app.search_tasks(query)
                if results:
                    print(f"\nFound {len(results)} matching task(s):")
                    app.display_tasks(results)
                else:
                    print("No matching tasks found.")
            
            elif choice == 7:
                print("\n--- Filter Tasks ---")
                print("1. All tasks")
                print("2. Complete tasks")
                print("3. Incomplete tasks")
                print("4. By priority")
                try:
                    filter_choice = int(input("Select filter (1-4): "))
                    if filter_choice == 1:
                        app.display_tasks()
                    elif filter_choice == 2:
                        filtered = app.filter_by_status('complete')
                        app.display_tasks(filtered)
                    elif filter_choice == 3:
                        filtered = app.filter_by_status('incomplete')
                        app.display_tasks(filtered)
                    elif filter_choice == 4:
                        priority = get_priority_choice()
                        filtered = app.filter_by_priority(priority)
                        app.display_tasks(filtered)
                except ValueError:
                    print("Invalid choice.")
            
            elif choice == 8:
                print("\n--- Sort Tasks ---")
                print("1. By priority")
                print("2. By due date")
                print("3. By status")
                print("4. By creation date")
                try:
                    sort_choice = int(input("Select sort option (1-4): "))
                    sort_by = ['priority', 'due_date', 'status', 'created'][sort_choice - 1]
                    sorted_tasks = app.sort_tasks(sort_by)
                    app.display_tasks(sorted_tasks)
                except (ValueError, IndexError):
                    print("Invalid choice.")
            
            elif choice == 9:
                stats = app.get_statistics()
                print("\n" + "=" * 40)
                print("        STATISTICS")
                print("=" * 40)
                print(f"Total tasks:          {stats['total']}")
                print(f"Completed:            {stats['complete']} ({stats['complete']/max(stats['total'], 1)*100:.1f}%)")
                print(f"Incomplete:           {stats['incomplete']} ({stats['incomplete']/max(stats['total'], 1)*100:.1f}%)")
                print(f"Overdue:              {stats['overdue']}")
                print(f"High priority pending: {stats['high_priority']}")
                print("=" * 40)
            
            elif choice == 10:
                if app.save_tasks():
                    print(f"Tasks saved to {app.filename}!")
                else:
                    print("Failed to save tasks.")
            
            elif choice == 11:
                backup_file = app.backup_tasks()
                if backup_file:
                    print(f"Backup created: {backup_file}")
                else:
                    print("Failed to create backup.")
            
            elif choice == 12:
                if app.save_tasks():
                    print("Tasks saved. Goodbye!")
                else:
                    print("Warning: Failed to save tasks.")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 12.")
        
        except KeyboardInterrupt:
            print("\n\nSaving tasks...")
            app.save_tasks()
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()