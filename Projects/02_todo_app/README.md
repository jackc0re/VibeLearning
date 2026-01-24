# ✅ Project 2: Todo App

Build a complete task management application with file persistence, priority levels, and advanced features.

---

## 📋 Project Overview

This project helps you practice:
- Object-oriented programming (classes and objects)
- File I/O for data persistence
- Data structures for task management
- User interface design

### Features to Build

1. ✅ Task Management
   - Add new tasks
   - Edit existing tasks
   - Delete tasks
   - Mark tasks as complete/incomplete

2. ✅ Task Properties
   - Task description
   - Priority levels (High, Medium, Low)
   - Due dates
   - Completion status

3. ✅ Data Persistence
   - Save tasks to file
   - Load tasks on startup
   - Automatic backup

4. ✅ Search & Filter
   - Search by task description
   - Filter by status (all, complete, incomplete)
   - Filter by priority

5. ✅ User Interface
   - Menu-driven interface
   - Task lists with formatting
   - Clear prompts and feedback

---

## 💻 Requirements

### Prerequisites

Complete these modules before starting:
- [00_getting_started](../../00_getting_started/README.md)
- [01_foundations](../../01_foundations/README.md)
- [02_data_structures](../../02_data_structures/README.md)
- [04_oop_concepts](../../04_oop_concepts/README.md)
- [10_file_io](../../10_file_io/README.md)

### Skills You'll Use

- **Classes & Objects** — Create a Task class and TodoApp class
- **Lists & Dictionaries** — Store and manage tasks
- **File I/O** — Save and load tasks using JSON
- **Control Flow** — Handle user choices and menu navigation
- **Error Handling** — Validate input and handle exceptions

---

## 🚀 Development Steps

### Step 1: Task Class (20 minutes)

Create a class to represent a single task:

```python
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
```

### Step 2: TodoApp Class (30 minutes)

Create the main application class:

```python
class TodoApp:
    """Main todo application class."""
    
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
```

### Step 3: Search and Filter (20 minutes)

Add methods to find and filter tasks:

```python
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
```

### Step 4: File I/O (20 minutes)

Add methods to save and load tasks:

```python
def save_tasks(self):
    """Save tasks to file."""
    try:
        data = [task.to_dict() for task in self.tasks]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def load_tasks(self):
    """Load tasks from file."""
    try:
        with open(self.filename, 'r') as f:
            data = json.load(f)
            self.tasks = [Task.from_dict(task_data) for task_data in data]
        return True
    except FileNotFoundError:
        self.tasks = []
        return True
    except Exception as e:
        print(f"Error loading tasks: {e}")
        self.tasks = []
        return False

def backup_tasks(self):
    """Create a backup of current tasks."""
    backup_filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    try:
        data = [task.to_dict() for task in self.tasks]
        with open(backup_filename, 'w') as f:
            json.dump(data, f, indent=2)
        return backup_filename
    except Exception as e:
        print(f"Error creating backup: {e}")
        return None
```

### Step 5: Display Methods (20 minutes)

Add methods to display tasks:

```python
def display_tasks(self, tasks=None):
    """Display tasks in a formatted list."""
    if tasks is None:
        tasks = self.tasks
    
    if not tasks:
        print("\nNo tasks to display.")
        return
    
    print("\n" + "=" * 60)
    print("                        TASKS")
    print("=" * 60)
    print(f"{'#':<4} {'Status':<8} {'Priority':<10} {'Description':<30} {'Due':<12}")
    print("-" * 60)
    
    for i, task in enumerate(tasks, 1):
        status = "✓" if task.completed else "○"
        priority_colors = {
            'High': '🔴',
            'Medium': '🟡',
            'Low': '🟢'
        }
        priority_icon = priority_colors.get(task.priority, '⚪')
        
        due_str = ""
        if task.due_date:
            due_str = task.due_date.strftime("%b %d")
            if task.is_overdue():
                due_str += "!"
        
        desc = task.description[:26] + "..." if len(task.description) > 26 else task.description
        
        print(f"{i:<4} {status:<8} {priority_icon} {task.priority:<8} {desc:<30} {due_str:<12}")
    
    print("=" * 60)
    
    stats = self.get_statistics()
    print(f"Total: {stats['total']} | Complete: {stats['complete']} | Incomplete: {stats['incomplete']} | Overdue: {stats['overdue']}")

def get_statistics(self):
    """Get task statistics."""
    complete = sum(1 for task in self.tasks if task.completed)
    incomplete = len(self.tasks) - complete
    overdue = sum(1 for task in self.tasks if task.is_overdue())
    return {
        'total': len(self.tasks),
        'complete': complete,
        'incomplete': incomplete,
        'overdue': overdue
    }
```

### Step 6: User Input Helpers (15 minutes)

Add helper functions for user input:

```python
def get_priority_choice():
    """Get priority choice from user."""
    while True:
        print("\nPriority levels:")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        try:
            choice = int(input("Select priority (1-3): "))
            priorities = {1: "High", 2: "Medium", 3: "Low"}
            if choice in priorities:
                return priorities[choice]
            print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_due_date():
    """Get due date from user."""
    while True:
        due_str = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
        if not due_str:
            return None
        try:
            return datetime.strptime(due_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD (e.g., 2024-12-25)")
```

### Step 7: Menu and Main Loop (30 minutes)

Create the menu and main application loop:

```python
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
    print("8. Show Statistics")
    print("9. Save Tasks")
    print("10. Create Backup")
    print("11. Exit")
    print("=" * 40)

def run(self):
    """Run the todo application."""
    print("=" * 40)
    print("       WELCOME TO TODO APP")
    print("=" * 40)
    
    while True:
        self.display_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-11): "))
            
            if choice == 1:
                self.display_tasks()
            
            elif choice == 2:
                desc = input("Enter task description: ").strip()
                if desc:
                    priority = get_priority_choice()
                    due_date = get_due_date()
                    self.add_task(desc, priority, due_date)
                    print("Task added successfully!")
                else:
                    print("Task description cannot be empty.")
            
            elif choice == 3:
                self.display_tasks()
                index = int(input("Enter task number to edit: "))
                task = self.get_task(index)
                if task:
                    new_desc = input(f"Description [{task.description}]: ").strip()
                    new_priority = None
                    change_priority = input("Change priority? (y/n): ").lower() == 'y'
                    if change_priority:
                        new_priority = get_priority_choice()
                    new_due_date = None
                    change_due = input("Change due date? (y/n): ").lower() == 'y'
                    if change_due:
                        new_due_date = get_due_date()
                    
                    self.edit_task(index, new_desc or task.description, new_priority, new_due_date)
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
            
            # Continue with remaining menu options...
            
            elif choice == 11:
                if self.save_tasks():
                    print("Tasks saved. Goodbye!")
                break
            
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nSaving tasks...")
            self.save_tasks()
            print("Goodbye!")
            break
```

---

## 🧪 Testing

Test your app with these scenarios:

1. **Basic Operations**
   - Add a few tasks
   - Mark some as complete
   - Delete a task
   - Display tasks

2. **Search and Filter**
   - Add multiple tasks
   - Search for specific tasks
   - Filter by status
   - Filter by priority

3. **Data Persistence**
   - Add tasks and save
   - Exit the app
   - Restart and verify tasks are loaded

4. **Edge Cases**
   - Empty description
   - Invalid task numbers
   - Invalid date format
   - Overdue tasks

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How to design and implement classes
- ✅ How to use class methods and static methods
- ✅ How to work with lists and list comprehensions
- ✅ How to read and write JSON files
- ✅ How to handle dates and times
- ✅ How to create a menu-driven CLI application
- ✅ How to structure a complete application

---

## 🏆 Challenges

Complete these challenges to enhance your todo app:

1. **Categories and Tags** — Add categories and tag support
2. **Subtasks** — Add ability to create subtasks within tasks
3. **Task Reminders** — Add reminder notifications
4. **CSV Export/Import** — Support CSV format for tasks
5. **Priority Sorting** — Auto-sort tasks by priority
6. **Recurring Tasks** — Support recurring/repeating tasks
7. **Task Notes** — Add detailed notes to each task

See [challenges.md](challenges.md) for detailed instructions.

---

## 📁 File Structure

```
02_todo_app/
├── README.md          # This file
├── todo.py            # Your main implementation
└── challenges.md      # Additional challenge tasks
```

---

**Ready to start?** Create `todo.py` and begin building! 🚀