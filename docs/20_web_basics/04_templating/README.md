# 📝 Templating

> Generating dynamic HTML with Python string templating

---

## What is Templating?

**Templating** is the process of generating dynamic content by combining static templates with variable data. Instead of hardcoding HTML in Python strings, you create reusable templates with placeholders.

Think of it like a **mad libs** game:
- Template: "Once upon a time, there was a {adjective} {noun}."
- Data: adjective="brave", noun="knight"
- Result: "Once upon a time, there was a brave knight."

---

## Python's Built-in Templating Options

### 1. F-Strings (Simple Cases)

```python
name = "Alice"
age = 25
html = f"<h1>Hello, {name}!</h1><p>You are {age} years old.</p>"
```

### 2. str.format()

```python
template = "<h1>Hello, {name}!</h1><p>You are {age} years old.</p>"
html = template.format(name="Alice", age=25)
```

### 3. string.Template (Safer, Standard Library)

```python
from string import Template

template = Template("<h1>Hello, $name!</h1><p>You are $age years old.</p>")
html = template.substitute(name="Alice", age=25)
```

### 4. Template Files (Best for Complex Pages)

```python
# template.html
html_template = """<!DOCTYPE html>
<html>
<head><title>$title</title></head>
<body>
    <h1>$heading</h1>
    <p>$content</p>
</body>
</html>"""

template = Template(html_template)
html = template.substitute(
    title="My Page",
    heading="Welcome",
    content="This is the content."
)
```

---

## Building a Simple Template Engine

Create a more powerful templating system:

```python
import re
from html import escape

class SimpleTemplate:
    """A minimal template engine with variable substitution and basic control flow."""
    
    def __init__(self, template):
        self.template = template
    
    def render(self, context=None, safe=False):
        """Render template with context dictionary."""
        if context is None:
            context = {}
        
        result = self.template
        
        # Handle conditionals: {% if condition %}...{% endif %}
        result = self._process_conditionals(result, context)
        
        # Handle loops: {% for item in items %}...{% endfor %}
        result = self._process_loops(result, context)
        
        # Variable substitution: {{ variable }}
        def replace_var(match):
            var_name = match.group(1).strip()
            value = context.get(var_name, '')
            if not safe:
                value = escape(str(value))
            return str(value)
        
        result = re.sub(r'\{\{\s*(\w+)\s*\}\}', replace_var, result)
        
        return result
    
    def _process_conditionals(self, template, context):
        """Process {% if %}...{% endif %} blocks."""
        pattern = r'\{%\s*if\s+(\w+)\s*%\}(.*?)\{%\s*endif\s*%\}'
        
        def replace_if(match):
            condition = match.group(1)
            content = match.group(2)
            if context.get(condition):
                return content
            return ''
        
        return re.sub(pattern, replace_if, template, flags=re.DOTALL)
    
    def _process_loops(self, template, context):
        """Process {% for %}...{% endfor %} blocks."""
        pattern = r'\{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%\}(.*?)\{%\s*endfor\s*%\}'
        
        def replace_for(match):
            item_name = match.group(1)
            list_name = match.group(2)
            content = match.group(3)
            
            items = context.get(list_name, [])
            result = []
            for item in items:
                # Replace item variable in content
                item_content = content.replace(f'{{{{ {item_name} }}}}', escape(str(item)))
                result.append(item_content)
            
            return ''.join(result)
        
        return re.sub(pattern, replace_for, template, flags=re.DOTALL)

# Usage
template_str = """
<h1>{{ title }}</h1>
{% if user %}
    <p>Welcome, {{ user }}!</p>
{% endif %}
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
"""

template = SimpleTemplate(template_str)
html = template.render({
    'title': 'My Page',
    'user': 'Alice',
    'items': ['Apple', 'Banana', 'Cherry']
})
```

---

## HTML Escaping (Security!)

**Always escape user input** to prevent XSS (Cross-Site Scripting) attacks:

```python
from html import escape

user_input = '<script>alert("hacked")</script>'

# DANGEROUS - Don't do this!
html = f"<p>{user_input}</p>"  # Executes the script!

# SAFE - Escaped
html = f"<p>{escape(user_input)}</p>"
# Result: <p>&lt;script&gt;alert(&quot;hacked&quot;)&lt;/script&gt;</p>
```

**Built-in escape function:**

| Character | Escaped |
|-----------|---------|
| `<` | `&lt;` |
| `>` | `&gt;` |
| `&` | `&amp;` |
| `"` | `&quot;` |
| `'` | `&#x27;` |

---

## Template Inheritance

Create a base template that others can extend:

```python
base_template = """<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        nav { background: #333; padding: 10px; }
        nav a { color: white; margin-right: 15px; text-decoration: none; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
    </nav>
    <main>
        {{ content }}
    </main>
    <footer>
        <p>&copy; 2026 My Site</p>
    </footer>
</body>
</html>"""

def render_page(title, content):
    """Render a page using the base template."""
    template = Template(base_template)
    return template.substitute(title=title, content=content)

# Usage
page_content = "<h1>Welcome</h1><p>This is the home page.</p>"
html = render_page("Home", page_content)
```

---

## Common Template Patterns

### List Rendering

```python
def render_list(items, empty_message="No items"):
    if not items:
        return f"<p>{empty_message}</p>"
    
    items_html = "\n".join(f"    <li>{escape(str(item))}</li>" for item in items)
    return f"<ul>\n{items_html}\n</ul>"
```

### Table Rendering

```python
def render_table(headers, rows):
    headers_html = "".join(f"<th>{escape(h)}</th>" for h in headers)
    rows_html = ""
    for row in rows:
        cells = "".join(f"<td>{escape(str(cell))}</td>" for cell in row)
        rows_html += f"    <tr>{cells}</tr>\n"
    
    return f"""<table border="1">
    <thead><tr>{headers_html}</tr></thead>
    <tbody>
{rows_html}    </tbody>
</table>"""
```

### Form Rendering

```python
def render_input(name, label, type="text", value="", required=False):
    req_attr = " required" if required else ""
    return f"""<div class="field">
    <label for="{name}">{escape(label)}:</label>
    <input type="{type}" name="{name}" id="{name}" value="{escape(value)}"{req_attr}>
</div>"""
```

---

## Complete Example: Page Components

```python
"""
templating_system.py - A complete templating example
"""
from string import Template
from html import escape

class PageBuilder:
    """Build complete HTML pages with components."""
    
    # Base template for all pages
    BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title</title>
    <style>
        * { box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        header { background: #333; color: white; padding: 1rem; border-radius: 8px; }
        header h1 { margin: 0; }
        nav { margin-top: 1rem; }
        nav a { color: #ddd; margin-right: 20px; text-decoration: none; }
        nav a:hover { color: white; }
        main { 
            background: white; 
            padding: 2rem; 
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        footer { text-align: center; color: #666; margin-top: 40px; }
        .alert { padding: 15px; border-radius: 4px; margin: 15px 0; }
        .alert-success { background: #d4edda; color: #155724; }
        .alert-error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <header>
        <h1>🐍 My Website</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    
    <main>
        $content
    </main>
    
    <footer>
        <p>&copy; 2026 Built with Python http.server</p>
    </footer>
</body>
</html>"""
    
    @classmethod
    def page(cls, title, content):
        """Build a complete page."""
        template = Template(cls.BASE_TEMPLATE)
        return template.substitute(
            title=escape(title),
            content=content
        )
    
    @classmethod
    def alert(cls, message, type="success"):
        """Build an alert component."""
        return f'<div class="alert alert-{type}">{escape(message)}</div>'
    
    @classmethod
    def card(cls, title, body):
        """Build a card component."""
        return f"""<div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin: 15px 0;">
    <h3>{escape(title)}</h3>
    <p>{escape(body)}</p>
</div>"""

# Usage
home_content = """
<h2>Welcome to My Site</h2>
<p>This page was built with Python templating!</p>
""" + PageBuilder.card("Feature 1", "Amazing functionality") \
    + PageBuilder.card("Feature 2", "Incredible performance")

html = PageBuilder.page("Home", home_content)
```

---

## Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| Not escaping user input | XSS security vulnerability | Always use `html.escape()` on dynamic content |
| Mixing logic and templates | Hard to maintain | Separate template files from business logic |
| String concatenation in loops | Inefficient | Use list + `join()` pattern |
| Complex logic in templates | Templates should be simple | Do data preparation in Python, not templates |
| Not handling missing variables | Template errors | Use `.get()` with defaults or check existence |

---

## Quick Reference

```python
from string import Template
from html import escape

# Simple substitution
template = Template("Hello, $name!")
result = template.substitute(name="Alice")

# Safe substitution (won't error on missing keys)
result = template.safe_substitute(name="Alice")

# Escape HTML
user_input = "<script>alert('xss')</script>"
safe = escape(user_input)  # &lt;script&gt;...

# Template with conditionals
page = Template("""
{% if user %}
    <p>Welcome, $user!</p>
{% endif %}
""")
```

---

## Next Steps

Now you can generate dynamic HTML! Let's learn how to handle user input through forms.

→ Continue to [05: Forms Handling](../05_forms_handling/)
