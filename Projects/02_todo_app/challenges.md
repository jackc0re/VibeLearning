# 🎯 Todo App Challenges

Extend your todo application with these advanced features. Each challenge helps you practice more complex concepts.

---

## Challenge 1: Categories and Tags

Add organization features to group and tag your tasks.

### Features to Add

1. **Categories** — Assign each task to a category (Work, Personal, Shopping, etc.)
2. **Tags** — Add multiple tags to tasks for flexible filtering
3. **Category Management** — List, add, and delete categories
4. **Filter by Category/Tag** — Show tasks matching specific categories or tags

### Implementation

```python
class Task:
    def __init__(self, description, priority="Medium", due_date=None, category=None, tags=None):
        # ... existing code ...
        self.category = category
        self.tags = tags or []
    
    def add_tag(self, tag):
        """Add a tag to the task."""
        if tag.lower() not in [t.lower() for t in self.tags]:
            self.tags.append(tag)
    
    def remove_tag(self, tag):
        """Remove a tag from the task."""
        self.tags = [t for t in self.tags if t.lower() != tag.lower()]
    
    def to_dict(self):
        """Convert task to dictionary."""
        return {
            # ... existing fields ...
            'category': self.category,
            'tags': self.tags
        }

class TodoApp:
    def __init__(self):
        # ... existing code ...
        self.categories = ["Work", "Personal", "Shopping", "Health"]
    
    def filter_by_category(self, category):
        """Filter tasks by category."""
        return [task for task in self.tasks if task.category == category]
    
    def filter_by_tag(self, tag):
        """Filter tasks by tag."""
        return [task for task in self.tasks if tag.lower() in [t.lower() for t in task.tags]]
    
    def get_all_tags(self):
        """Get all unique tags from all tasks."""
        tags = set()
        for task in self.tasks:
            tags.update(task.tags)
        return sorted(list(tags))
```

### New Menu Options

- Add category when creating task
- New menu: "13. Manage Categories"
- New menu: "14. Manage Tags"
- Filter options: "By Category" and "By Tag"

---

## Challenge 2: Subtasks

Add ability to create subtasks within main tasks.

### Features to Add

1. **Add Subtasks** — Create subtasks within a task
2. **Complete Subtasks** — Mark subtasks as complete
3. **Progress Tracking** — Show completion percentage based on subtasks
4. **Delete Subtasks** — Remove subtasks from tasks

### Implementation

```python
class Subtask:
    """Represents a subtask within a task."""
    
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.created_at = datetime.now()

class Task:
    def __init__(self, description, priority="Medium", due_date=None):
        # ... existing code ...
        self.subtasks = []
    
    def add_subtask(self, description):
        """Add a subtask."""
        subtask = Subtask(description)
        self.subtasks.append(subtask)
    
    def toggle_subtask(self, index):
        """Toggle subtask completion."""
        if 1 <= index <= len(self.subtasks):
            self.subtasks[index - 1].completed = not self.subtasks[index - 1].completed
    
    def delete_subtask(self, index):
        """Delete a subtask."""
        if 1 <= index <= len(self.subtasks):
            del self.subtasks[index - 1]
    
    def get_progress(self):
        """Get completion percentage based on subtasks."""
        if not self.subtasks:
            return 100 if self.completed else 0
        completed = sum(1 for s in self.subtasks if s.completed)
        return (completed / len(self.subtasks)) * 100
    
    def to_dict(self):
        """Convert task to dictionary."""
        return {
            # ... existing fields ...
            'subtasks': [s.description for s in self.subtasks]
        }
```

### Display Enhancement

```python
def display_tasks(self, tasks=None):
    """Display tasks with subtask progress."""
    # ... existing code ...
    
    for i, task in enumerate(tasks, 1):
        # ... existing display code ...
        
        if task.subtasks:
            completed_subs = sum(1 for s in task.subtasks if s.completed)
            total_subs = len(task.subtasks)
            progress = (completed_subs / total_subs) * 100
            print(f"    [{completed_subs}/{total_subs} subtasks] {progress:.0f}%")
```

---

## Challenge 3: Task Dependencies

Add dependency relationships between tasks.

### Features to Add

1. **Add Dependencies** — Make one task depend on another
2. **Check Dependencies** — Show tasks blocking other tasks
3. **Dependency View** — Display dependency chains
4. **Auto-completion** — Auto-complete dependent tasks when parent completes

### Implementation

```python
class Task:
    def __init__(self, description, priority="Medium", due_date=None):
        # ... existing code ...
        self.dependencies = []  # Task IDs this task depends on
    
    def add_dependency(self, task_id):
        """Add a task dependency."""
        if task_id not in self.dependencies:
            self.dependencies.append(task_id)
    
    def remove_dependency(self, task_id):
        """Remove a task dependency."""
        self.dependencies = [d for d in self.dependencies if d != task_id]
    
    def can_complete(self):
        """Check if task can be completed (all dependencies complete)."""
        return True  # Implementation depends on task tracking


class TodoApp:
    def get_blocking_tasks(self):
        """Get all incomplete tasks blocking others."""
        blocking = []
        for task in self.tasks:
            if not task.completed:
                for other in self.tasks:
                    if not other.completed and task.id in other.dependencies:
                        blocking.append((task, other))
        return blocking
    
    def display_dependency_tree(self):
        """Display tasks as a dependency tree."""
        for task in self.tasks:
            if not task.dependencies:
                self.display_task_with_dependents(task, depth=0)
```

---

## Challenge 4: CSV Export/Import

Support CSV format for task data import/export.

### Features to Add

1. **Export to CSV** — Save tasks as CSV file
2. **Import from CSV** — Load tasks from CSV file
3. **Custom Formats** — Support different CSV formats
4. **Batch Operations** — Import large datasets

### Implementation

```python
import csv

class TodoApp:
    def export_to_csv(self, filename="tasks_export.csv"):
        """Export tasks to CSV file."""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Description', 'Priority', 'Due Date', 'Status', 'Category'])
                
                for task in self.tasks:
                    due_date = task.due_date.strftime('%Y-%m-%d') if task.due_date else ''
                    status = 'Complete' if task.completed else 'Incomplete'
                    writer.writerow([
                        task.description,
                        task.priority,
                        due_date,
                        status,
                        task.category or ''
                    ])
            return filename
        except Exception as e:
            print(f"Export error: {e}")
            return None
    
    def import_from_csv(self, filename):
        """Import tasks from CSV file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                imported = 0
                
                for row in reader:
                    description = row.get('Description', '').strip()
                    if not description:
                        continue
                    
                    priority = row.get('Priority', 'Medium')
                    due_date = None
                    
                    due_str = row.get('Due Date', '').strip()
                    if due_str:
                        try:
                            due_date = datetime.strptime(due_str, '%Y-%m-%d').date()
                        except ValueError:
                            pass
                    
                    task = Task(description, priority, due_date)
                    task.category = row.get('Category', '').strip() or None
                    
                    status = row.get('Status', '').strip()
                    if status.lower() == 'complete':
                        task.mark_complete()
                    
                    self.tasks.append(task)
                    imported += 1
                
                return imported
        except Exception as e:
            print(f"Import error: {e}")
            return 0
```

---

## Challenge 5: Repeating Tasks

Support tasks that repeat on a schedule.

### Features to Add

1. **Repeat Options** — Daily, Weekly, Monthly, Yearly
2. **Auto-creation** — Create next occurrence when task completes
3. **Repeat Count** — Set maximum number of repetitions
4. **Repeat Until** — Set end date for repetitions

### Implementation

```python
from datetime import timedelta, date

class Task:
    def __init__(self, description, priority="Medium", due_date=None):
        # ... existing code ...
        self.repeat_type = None  # 'daily', 'weekly', 'monthly', 'yearly'
        self.repeat_count = 0
        self.repeat_max = None
        self.repeat_until = None
    
    def set_repeat(self, repeat_type, repeat_max=None, repeat_until=None):
        """Set repeat settings."""
        self.repeat_type = repeat_type
        self.repeat_max = repeat_max
        self.repeat_until = repeat_until
    
    def should_repeat(self):
        """Check if task should repeat."""
        if not self.repeat_type:
            return False
        if self.repeat_max and self.repeat_count >= self.repeat_max:
            return False
        if self.repeat_until and date.today() > self.repeat_until:
            return False
        return True
    
    def create_next_occurrence(self):
        """Create the next occurrence of a repeating task."""
        if not self.should_repeat():
            return None
        
        next_due = None
        if self.due_date:
            if self.repeat_type == 'daily':
                next_due = self.due_date + timedelta(days=1)
            elif self.repeat_type == 'weekly':
                next_due = self.due_date + timedelta(weeks=1)
            elif self.repeat_type == 'monthly':
                next_due = self.get_next_month(self.due_date)
            elif self.repeat_type == 'yearly':
                next_due = self.get_next_year(self.due_date)
        
        next_task = Task(self.description, self.priority, next_due)
        next_task.repeat_type = self.repeat_type
        next_task.repeat_max = self.repeat_max
        next_task.repeat_until = self.repeat_until
        next_task.repeat_count = self.repeat_count + 1
        
        return next_task
    
    def get_next_month(self, due_date):
        """Calculate due date for next month."""
        if due_date.month == 12:
            return date(due_date.year + 1, 1, due_date.day)
        else:
            try:
                return date(due_date.year, due_date.month + 1, due_date.day)
            except ValueError:
                return date(due_date.year, due_date.month + 1, 28)
    
    def get_next_year(self, due_date):
        """Calculate due date for next year."""
        return date(due_date.year + 1, due_date.month, due_date.day)
```

### Update TodoApp for Repeating Tasks

```python
class TodoApp:
    def complete_task(self, index):
        """Complete task and create next occurrence if repeating."""
        task = self.get_task(index)
        if task:
            task.mark_complete()
            
            if task.should_repeat():
                next_task = task.create_next_occurrence()
                if next_task:
                    self.tasks.append(next_task)
                    print(f"Created next occurrence: {next_task.description}")
            
            return task
        return None
```

---

## Challenge 6: Task Notes

Add detailed notes to each task.

### Features to Add

1. **Add Notes** — attach multi-line notes to tasks
2. **Edit Notes** — Modify existing notes
3. **Delete Notes** — Remove notes from tasks
4. **Search Notes** — Search within notes content

### Implementation

```python
class Task:
    def __init__(self, description, priority="Medium", due_date=None):
        # ... existing code ...
        self.notes = ""
    
    def add_notes(self, notes):
        """Add or update task notes."""
        self.notes = notes
    
    def append_note(self, note):
        """Append a note to existing notes."""
        if self.notes:
            self.notes += "\n\n" + note
        else:
            self.notes = note
    
    def clear_notes(self):
        """Clear task notes."""
        self.notes = ""
    
    def to_dict(self):
        """Convert task to dictionary."""
        return {
            # ... existing fields ...
            'notes': self.notes
        }
```

### New Menu Options

- When viewing task details: "View/Edit Notes"
- Add note option when creating task
- Search filter: "Search in Notes"

---

## Challenge 7: Task Templates

Create reusable task templates.

### Features to Add

1. **Create Templates** — Save task configurations as templates
2. **Apply Templates** — Create new tasks from templates
3. **Template Library** — Manage saved templates
4. **Template Variables** — Use variables in templates

### Implementation

```python
class TaskTemplate:
    """Reusable task template."""
    
    def __init__(self, name, description, priority="Medium", category=None, tags=None):
        self.name = name
        self.description = description
        self.priority = priority
        self.category = category
        self.tags = tags or []
    
    def create_task(self, **variables):
        """Create a task from this template."""
        desc = self.description
        for key, value in variables.items():
            desc = desc.replace(f"{{{key}}}", str(value))
        
        task = Task(desc, self.priority)
        task.category = self.category
        task.tags = self.tags.copy()
        return task


class TodoApp:
    def __init__(self):
        # ... existing code ...
        self.templates = self.load_templates()
    
    def add_template(self, template):
        """Add a task template."""
        self.templates.append(template)
    
    def get_template(self, name):
        """Get template by name."""
        for template in self.templates:
            if template.name.lower() == name.lower():
                return template
        return None
    
    def create_from_template(self, name, **variables):
        """Create task from template."""
        template = self.get_template(name)
        if template:
            task = template.create_task(**variables)
            self.tasks.append(task)
            return task
        return None
    
    def list_templates(self):
        """List all templates."""
        print("\n--- Task Templates ---")
        for template in self.templates:
            print(f"- {template.name}")
            print(f"  Description: {template.description}")
            print(f"  Priority: {template.priority}")
            print()
```

### Example Templates

```python
# Create templates
weekly_review = TaskTemplate(
    "Weekly Review",
    "Review {project} tasks for week {week}",
    priority="High",
    category="Work"
)

meeting_reminder = TaskTemplate(
    "Meeting",
    "Prepare for {meeting_name} meeting at {time}",
    priority="Medium",
    category="Work",
    tags=["meeting"]
)

# Use templates
app.create_from_template("Weekly Review", project="Project A", week="42")
app.create_from_template("Meeting", meeting_name="Team Standup", time="10:00 AM")
```

---

## Challenge 8: Advanced Statistics

Add more detailed statistics and visualizations.

### Features to Add

1. **Completion Rate** — Track completion rate over time
2. **Priority Analysis** — Analyze task priority distribution
3. **Category Breakdown** — Show tasks by category
4. **Time Tracking** — Track time to complete tasks

### Implementation

```python
class TodoApp:
    def get_detailed_statistics(self):
        """Get comprehensive statistics."""
        stats = self.get_statistics()
        
        # Completion rate
        total_tasks = len(self.tasks)
        completion_rate = (stats['complete'] / total_tasks * 100) if total_tasks else 0
        
        # Priority distribution
        priority_dist = {}
        for task in self.tasks:
            priority_dist[task.priority] = priority_dist.get(task.priority, 0) + 1
        
        # Category distribution
        category_dist = {}
        for task in self.tasks:
            category = task.category or "Uncategorized"
            category_dist[category] = category_dist.get(category, 0) + 1
        
        # Overdue by priority
        overdue_by_priority = {}
        for task in self.tasks:
            if task.is_overdue():
                overdue_by_priority[task.priority] = overdue_by_priority.get(task.priority, 0) + 1
        
        return {
            **stats,
            'completion_rate': completion_rate,
            'priority_distribution': priority_dist,
            'category_distribution': category_dist,
            'overdue_by_priority': overdue_by_priority
        }
    
    def display_statistics(self):
        """Display detailed statistics."""
        stats = self.get_detailed_statistics()
        
        print("\n" + "=" * 50)
        print("           DETAILED STATISTICS")
        print("=" * 50)
        
        completion_bar = "█" * int(stats['completion_rate'] / 5)
        print(f"Completion Rate: {completion_bar} {stats['completion_rate']:.1f}%")
        
        print("\nPriority Distribution:")
        for priority, count in stats['priority_distribution'].items():
            icon = self.PRIORITY_COLORS.get(priority, '⚪')
            percentage = (count / stats['total'] * 100) if stats['total'] else 0
            bar = "█" * int(percentage / 5)
            print(f"  {icon} {priority}: {count} ({percentage:.1f}%) {bar}")
        
        print("\nCategory Distribution:")
        for category, count in sorted(stats['category_distribution'].items()):
            percentage = (count / stats['total'] * 100) if stats['total'] else 0
            bar = "█" * int(percentage / 5)
            print(f"  {category}: {count} ({percentage:.1f}%) {bar}")
        
        print("=" * 50)
```

---

## 🏆 Challenge Completion

Track your progress:

- [ ] Challenge 1: Categories and Tags
- [ ] Challenge 2: Subtasks
- [ ] Challenge 3: Task Dependencies
- [ ] Challenge 4: CSV Export/Import
- [ ] Challenge 5: Repeating Tasks
- [ ] Challenge 6: Task Notes
- [ ] Challenge 7: Task Templates
- [ ] Challenge 8: Advanced Statistics

---

**Tip:** Complete challenges in any order. Each one teaches valuable programming skills!