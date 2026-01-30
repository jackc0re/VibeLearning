"""
Templating - Examples
=====================
Demonstrates HTML templating techniques with Python.
"""

print("=" * 60)
print("TEMPLATING - Examples")
print("=" * 60)

# =============================================================================
# SECTION 1: Basic String Templating
# =============================================================================
print("\n--- 1: Basic String Templating ---\n")

# Using % formatting (older style)
name = "Alice"
age = 25
html_old = "<p>Name: %s, Age: %d</p>" % (name, age)
print(f"% formatting: {html_old}")

# Using str.format()
html_format = "<p>Name: {}, Age: {}</p>".format(name, age)
print(f"str.format(): {html_format}")

# Using f-strings (recommended for simple cases)
html_fstring = f"<p>Name: {name}, Age: {age}</p>"
print(f"f-string: {html_fstring}")

# Named placeholders with format()
template = "<h1>{title}</h1><p>By {author}</p>"
html_named = template.format(title="My Article", author="Bob")
print(f"Named format: {html_named}")

# =============================================================================
# SECTION 2: string.Template (Standard Library)
# =============================================================================
print("\n--- 2: string.Template ---\n")

from string import Template

# Basic usage
template = Template("<h1>Hello, $name!</h1><p>You are $age years old.</p>")
html = template.substitute(name="Alice", age=25)
print("Template substitution:")
print(html)

# safe_substitute (won't error on missing keys)
template = Template("<p>User: $name, Role: $role</p>")
html_safe = template.safe_substitute(name="Bob")  # role missing
print(f"\nSafe substitute (missing role): {html_safe}")

# Using dictionary
data = {'product': 'Laptop', 'price': 999.99}
template = Template("<p>$product costs $$${price}</p>")
html_dict = template.substitute(data)
print(f"\nDictionary substitution: {html_dict}")

# Note: $$ escapes to literal $

# =============================================================================
# SECTION 3: HTML Escaping for Security
# =============================================================================
print("\n--- 3: HTML Escaping ---\n")

from html import escape

# Dangerous user input
user_input = '<script>alert("XSS Attack!")</script>'

# WRONG - vulnerable to XSS
vulnerable = f"<p>Comment: {user_input}</p>"
print(f"VULNERABLE: {vulnerable[:50]}...")

# CORRECT - escaped
safe = f"<p>Comment: {escape(user_input)}</p>"
print(f"SAFE: {safe}")

# What escape() does
print("\nEscape mappings:")
test_chars = ['<', '>', '&', '"', "'"]
for char in test_chars:
    print(f"  {char!r:5} → {escape(char)!r}")

# =============================================================================
# SECTION 4: Simple Template Engine
# =============================================================================
print("\n--- 4: Simple Template Engine ---\n")

import re

class SimpleTemplate:
    """Minimal template engine with variables and conditionals."""
    
    def __init__(self, source):
        self.source = source
    
    def render(self, context=None):
        """Render template with context dictionary."""
        if context is None:
            context = {}
        
        result = self.source
        
        # Process conditionals: {% if var %}...{% endif %}
        result = self._process_conditionals(result, context)
        
        # Process loops: {% for x in list %}...{% endfor %}
        result = self._process_loops(result, context)
        
        # Variable substitution: {{ var }}
        def replace_var(match):
            var_name = match.group(1).strip()
            value = context.get(var_name, '')
            return escape(str(value))
        
        result = re.sub(r'\{\{\s*(\w+)\s*\}\}', replace_var, result)
        
        return result
    
    def _process_conditionals(self, template, context):
        """Process {% if %} blocks."""
        pattern = r'\{%\s*if\s+(\w+)\s*%\}(.*?)\{%\s*endif\s*%\}'
        
        def replace_if(match):
            condition = match.group(1)
            content = match.group(2)
            return content if context.get(condition) else ''
        
        return re.sub(pattern, replace_if, template, flags=re.DOTALL)
    
    def _process_loops(self, template, context):
        """Process {% for %} blocks."""
        pattern = r'\{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%\}(.*?)\{%\s*endfor\s*%\}'
        
        def replace_for(match):
            item_name = match.group(1)
            list_name = match.group(2)
            content = match.group(3)
            
            items = context.get(list_name, [])
            results = []
            for item in items:
                item_str = escape(str(item))
                results.append(content.replace(f'{{{{ {item_name} }}}}', item_str))
            
            return ''.join(results)
        
        return re.sub(pattern, replace_for, template, flags=re.DOTALL)

# Test template
template_str = """<article>
    <h2>{{ title }}</h2>
    {% if author %}
    <p class="author">By {{ author }}</p>
    {% endif %}
    <div class="content">{{ content }}</div>
    {% if tags %}
    <ul class="tags">
        {% for tag in tags %}
        <li>{{ tag }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</article>"""

template = SimpleTemplate(template_str)
result = template.render({
    'title': 'Python Templating',
    'author': 'Alice',
    'content': 'Learn how to generate HTML with Python.',
    'tags': ['python', 'web', 'tutorial']
})

print("Template result:")
print(result)

# =============================================================================
# SECTION 5: Component-Based Templating
# =============================================================================
print("\n--- 5: Component-Based Templating ---\n")

class Components:
    """Reusable HTML components."""
    
    @staticmethod
    def button(text, type="button", primary=True):
        style = "background: #007bff; color: white;" if primary else "background: #6c757d; color: white;"
        return f'<button type="{type}" style="{style} padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">{escape(text)}</button>'
    
    @staticmethod
    def alert(message, type="info"):
        colors = {
            'info': ('#d1ecf1', '#0c5460'),
            'success': ('#d4edda', '#155724'),
            'warning': ('#fff3cd', '#856404'),
            'error': ('#f8d7da', '#721c24')
        }
        bg, text = colors.get(type, colors['info'])
        return f'<div style="background: {bg}; color: {text}; padding: 12px; border-radius: 4px; margin: 10px 0;">{escape(message)}</div>'
    
    @staticmethod
    def card(title, content):
        return f"""<div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin: 15px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    <h3 style="margin-top: 0; color: #333;">{escape(title)}</h3>
    <p style="color: #666;">{escape(content)}</p>
</div>"""
    
    @staticmethod
    def list(items, ordered=False):
        if not items:
            return '<p><em>No items</em></p>'
        
        tag = 'ol' if ordered else 'ul'
        items_html = '\n'.join(f'    <li>{escape(str(item))}</li>' for item in items)
        return f"<{tag}>\n{items_html}\n</{tag}>"
    
    @staticmethod
    def table(headers, rows):
        headers_html = ''.join(f'<th style="background: #333; color: white; padding: 10px;">{escape(h)}</th>' for h in headers)
        rows_html = ''
        for i, row in enumerate(rows):
            bg = '#f9f9f9' if i % 2 else 'white'
            cells = ''.join(f'<td style="padding: 10px; border-bottom: 1px solid #ddd;">{escape(str(c))}</td>' for c in row)
            rows_html += f'<tr style="background: {bg};">{cells}</tr>\n'
        
        return f"""<table style="width: 100%; border-collapse: collapse;">
    <thead><tr>{headers_html}</tr></thead>
    <tbody>
        {rows_html}    </tbody>
</table>"""

# Test components
print("Components:")
print(Components.button("Submit", primary=True))
print()
print(Components.alert("Operation successful!", "success"))
print()
print(Components.card("Feature", "This is a feature card"))
print()
print(Components.list(['Apple', 'Banana', 'Cherry']))
print()
print(Components.table(
    ['Name', 'Role', 'Status'],
    [['Alice', 'Admin', 'Active'], ['Bob', 'User', 'Active'], ['Carol', 'User', 'Inactive']]
))

# =============================================================================
# SECTION 6: Page Builder with Inheritance
# =============================================================================
print("\n--- 6: Page Builder with Inheritance ---\n")

from string import Template

class PageBuilder:
    """Build complete HTML pages with layout inheritance."""
    
    BASE_LAYOUT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>$title</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        header { background: #333; color: white; padding: 20px; margin: -20px -20px 20px; }
        nav a { color: #ddd; margin-right: 20px; text-decoration: none; }
        .content { background: white; padding: 20px; border-radius: 8px; }
    </style>
</head>
<body>
    <header>
        <h1>$site_name</h1>
        <nav>$nav</nav>
    </header>
    <div class="content">
        $content
    </div>
    <footer style="margin-top: 40px; text-align: center; color: #666;">
        <p>&copy; 2026 $site_name</p>
    </footer>
</body>
</html>"""
    
    @classmethod
    def render(cls, title, content, site_name="My Site"):
        """Render a full page."""
        nav = cls._build_nav(['Home', 'About', 'Contact'])
        template = Template(cls.BASE_LAYOUT)
        return template.substitute(
            title=escape(title),
            content=content,
            site_name=escape(site_name),
            nav=nav
        )
    
    @classmethod
    def _build_nav(cls, items):
        """Build navigation links."""
        links = [f'<a href="/{item.lower()}">{item}</a>' for item in items]
        return ' '.join(links)

# Build a page
page_content = """
<h2>Welcome to Our Site</h2>
<p>This page demonstrates template inheritance.</p>
"""

full_page = PageBuilder.render("Home", page_content, "Awesome Site")
print("Generated page (first 800 chars):")
print(full_page[:800] + "...")

# =============================================================================
# SECTION 7: File-Based Templates
# =============================================================================
print("\n--- 7: File-Based Templates ---\n")

# In a real application, you'd load templates from files
template_content = """<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>
    <h1>{{ heading }}</h1>
    {{ content }}
</body>
</html>"""

class FileTemplate:
    """Simple file-based template loader."""
    
    def __init__(self, source):
        self.template = Template(source.replace('{{', '$').replace('}}', ''))
    
    def render(self, **context):
        """Render with context."""
        # Escape all context values
        safe_context = {k: escape(str(v)) for k, v in context.items()}
        return self.template.substitute(safe_context)

# Usage
template = FileTemplate(template_content)
html = template.render(
    title="My Page",
    heading="Welcome",
    content="<p>This is the content.</p>"  # Will be escaped
)
print("File-based template result:")
print(html)

# =============================================================================
# SECTION 8: Form Template Helpers
# =============================================================================
print("\n--- 8: Form Template Helpers ---\n")

class FormBuilder:
    """Build HTML forms programmatically."""
    
    @staticmethod
    def input_field(name, label, type="text", value="", required=False):
        req = " required" if required else ""
        return f"""<div style="margin-bottom: 15px;">
    <label for="{name}" style="display: block; margin-bottom: 5px; font-weight: bold;">{escape(label)}:</label>
    <input type="{type}" name="{name}" id="{name}" value="{escape(value)}" style="padding: 8px; border: 1px solid #ddd; border-radius: 4px; width: 100%;"{req}>
</div>"""
    
    @staticmethod
    def textarea(name, label, rows=4, required=False):
        req = " required" if required else ""
        return f"""<div style="margin-bottom: 15px;">
    <label for="{name}" style="display: block; margin-bottom: 5px; font-weight: bold;">{escape(label)}:</label>
    <textarea name="{name}" id="{name}" rows="{rows}" style="padding: 8px; border: 1px solid #ddd; border-radius: 4px; width: 100%; resize: vertical;"{req}></textarea>
</div>"""
    
    @staticmethod
    def select(name, label, options, required=False):
        req = " required" if required else ""
        options_html = '\n'.join(f'        <option value="{escape(opt)}">{escape(opt)}</option>' for opt in options)
        return f"""<div style="margin-bottom: 15px;">
    <label for="{name}" style="display: block; margin-bottom: 5px; font-weight: bold;">{escape(label)}:</label>
    <select name="{name}" id="{name}" style="padding: 8px; border: 1px solid #ddd; border-radius: 4px; width: 100%;"{req}>
        <option value="">-- Select --</option>
{options_html}
    </select>
</div>"""
    
    @staticmethod
    def submit(text="Submit"):
        return f'<button type="submit" style="background: #007bff; color: white; padding: 10px 30px; border: none; border-radius: 4px; cursor: pointer;">{escape(text)}</button>'
    
    @classmethod
    def build(cls, action, method="POST", fields=None):
        """Build complete form."""
        if fields is None:
            fields = []
        
        fields_html = '\n'.join(fields)
        return f"""<form action="{action}" method="{method}" style="max-width: 400px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
{fields_html}
    {cls.submit()}
</form>"""

# Build a form
form = FormBuilder.build(
    action="/submit",
    fields=[
        FormBuilder.input_field("name", "Full Name", required=True),
        FormBuilder.input_field("email", "Email", type="email", required=True),
        FormBuilder.select("country", "Country", ["USA", "UK", "Canada"]),
        FormBuilder.textarea("message", "Message", rows=5)
    ]
)

print("Generated form:")
print(form)

# =============================================================================
# SECTION 9: Template Caching
# =============================================================================
print("\n--- 9: Template Caching ---\n")

class CachedTemplate:
    """Template with caching for performance."""
    
    _cache = {}
    
    def __init__(self, source):
        self.source = source
        self.template = None
    
    def compile(self):
        """Compile template (cached)."""
        if self.source not in self._cache:
            self._cache[self.source] = Template(self.source)
        return self._cache[self.source]
    
    def render(self, **context):
        """Render with compiled template."""
        template = self.compile()
        safe_context = {k: escape(str(v)) for k, v in context.items()}
        return template.substitute(safe_context)

# Test caching
cached = CachedTemplate("<p>Hello, $name!</p>")
print("Template caching example:")
print(cached.render(name="Alice"))
print(cached.render(name="Bob"))  # Uses cached compiled template

# =============================================================================
# SECTION 10: Best Practices Summary
# =============================================================================
print("\n--- 10: Templating Best Practices ---\n")

print("""
1. ALWAYS escape user input:
   from html import escape
   html = f"<p>{escape(user_input)}</p>"

2. Use string.Template for complex templates:
   from string import Template
   t = Template("<h1>$title</h1>")
   html = t.substitute(title="Page")

3. Separate templates from logic:
   - Store templates in separate files/variables
   - Do data processing in Python, not templates

4. Use components for reusability:
   - Create functions for common UI elements
   - Build pages by composing components

5. Cache compiled templates:
   - Compiling templates is expensive
   - Cache when rendering multiple times

6. Keep templates simple:
   - Avoid complex logic in templates
   - Templates should focus on presentation
""")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
