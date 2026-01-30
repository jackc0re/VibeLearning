"""
Templating - Exercises
======================
Practice generating dynamic HTML with Python.
"""

print("=" * 60)
print("TEMPLATING - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Product Card Template
# =============================================================================
print("\n--- Exercise 1: Product Card Template ---\n")
"""
Create a function `render_product_card(product)` that generates HTML
for a product card.

The product dictionary has:
- name, price, description, image_url, in_stock, category

Requirements:
- Show product name as heading
- Display price formatted as $XX.XX
- Show category as a badge/tag
- Display "In Stock" or "Out of Stock" with different colors
- Include product image if image_url is provided
- Use proper HTML escaping for all text content
"""

# Your code here:


# =============================================================================
# EXERCISE 2: Blog Post Template
# =============================================================================
print("\n--- Exercise 2: Blog Post Template ---\n")
"""
Create a function `render_blog_post(post)` that generates HTML for a blog post.

The post dictionary has:
- title, author, date, content, tags (list), comments (list of dicts)

Each comment has: author, date, content

Requirements:
- Article semantic element
- Header with title, author, and date
- Main content
- Tags as styled spans
- Comments section with all comments
- Proper escaping of all dynamic content
"""

# Your code here:


# =============================================================================
# EXERCISE 3: Data Table Template
# =============================================================================
print("\n--- Exercise 3: Data Table Template ---\n")
"""
Create a function `render_data_table(data, options=None)` that generates
a styled HTML table.

The data dictionary has:
- headers: list of column names
- rows: list of lists (each row is a list of cell values)

Options dictionary (all optional):
- striped: bool (alternate row colors)
- bordered: bool (table borders)
- hover: bool (highlight on hover)
- caption: str (table caption)

Requirements:
- Apply CSS classes based on options
- Include caption if provided
- Proper escaping
"""

# Your code here:


# =============================================================================
# EXERCISE 4: Page Layout System
# =============================================================================
print("\n--- Exercise 4: Page Layout System ---\n")
"""
Create a PageLayout class that provides:
- A base layout with header, navigation, main content, and footer
- Methods for adding navigation items
- A render(page_title, content) method

The navigation should be built from a list of (name, url) tuples.

Include basic CSS styling in the template.
"""

# Your code here:


# =============================================================================
# EXERCISE 5: Form Generator
# =============================================================================
print("\n--- Exercise 5: Form Generator ---\n")
"""
Create a FormGenerator class that can build HTML forms from a specification.

The class should have:
- add_field(type, name, label, **options) method
- set_action(url) and set_method(method) methods
- render() method that returns complete form HTML

Support field types:
- text, email, password, number, textarea, select, checkbox

Options include:
- required: bool
- placeholder: str
- value: str (default value)
- options: list (for select type)
"""

# Your code here:


# =============================================================================
# EXERCISE 6: Simple Template Engine
# =============================================================================
print("\n--- Exercise 6: Simple Template Engine ---\n")
"""
Create a MiniTemplate class that supports:
- Variable substitution: {{ variable }}
- Conditionals: {% if variable %}...{% endif %}
- Loops: {% for item in list %}...{% endfor %}

The render(context) method should:
- Replace variables with context values (escaped)
- Include conditional blocks only if variable is truthy
- Repeat loop blocks for each item in the list

Example:
    template = MiniTemplate("<h1>{{ title }}</h1>{% if show_list %}<ul>{% for item in items %}<li>{{ item }}</li>{% endfor %}</ul>{% endif %}")
    template.render({'title': 'Hello', 'show_list': True, 'items': ['A', 'B']})
"""

# Your code here:


# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# -------------------------------------------------------------------------
# Solution 1
# -------------------------------------------------------------------------
print("\n--- Solution 1: Product Card Template ---\n")

from html import escape

def render_product_card(product):
    """Generate HTML for a product card."""
    name = escape(product.get('name', 'Unnamed Product'))
    price = product.get('price', 0)
    description = escape(product.get('description', ''))
    image_url = product.get('image_url')
    in_stock = product.get('in_stock', False)
    category = escape(product.get('category', 'Uncategorized'))
    
    # Format price
    price_display = f"${price:.2f}"
    
    # Stock status
    stock_color = '#28a745' if in_stock else '#dc3545'
    stock_text = 'In Stock' if in_stock else 'Out of Stock'
    
    # Image HTML
    image_html = ''
    if image_url:
        image_html = f'<img src="{escape(image_url)}" alt="{name}" style="width: 100%; max-width: 300px; border-radius: 4px;">'
    
    return f"""<div class="product-card" style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; max-width: 350px; margin: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    {image_html}
    <span class="category" style="display: inline-block; background: #6c757d; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.85em; margin: 10px 0;">{category}</span>
    <h3 style="margin: 10px 0; color: #333;">{name}</h3>
    <p class="description" style="color: #666; line-height: 1.5;">{description}</p>
    <p class="price" style="font-size: 24px; font-weight: bold; color: #007bff; margin: 10px 0;">{price_display}</p>
    <span class="stock-status" style="color: {stock_color}; font-weight: bold;">{stock_text}</span>
</div>"""

# Test
product = {
    'name': 'Wireless Headphones',
    'price': 79.99,
    'description': 'Premium noise-cancelling headphones with 30-hour battery.',
    'image_url': '/images/headphones.jpg',
    'in_stock': True,
    'category': 'Electronics'
}

print("Product card:")
print(render_product_card(product)[:500] + "...")

# -------------------------------------------------------------------------
# Solution 2
# -------------------------------------------------------------------------
print("\n--- Solution 2: Blog Post Template ---\n")

def render_blog_post(post):
    """Generate HTML for a blog post."""
    title = escape(post.get('title', 'Untitled'))
    author = escape(post.get('author', 'Anonymous'))
    date = escape(post.get('date', ''))
    content = escape(post.get('content', ''))
    tags = post.get('tags', [])
    comments = post.get('comments', [])
    
    # Build tags HTML
    tags_html = ''
    if tags:
        tag_spans = [f'<span style="background: #e9ecef; padding: 4px 12px; border-radius: 12px; margin-right: 8px; font-size: 0.85em;">{escape(tag)}</span>' for tag in tags]
        tags_html = '<div class="tags" style="margin: 15px 0;">' + ''.join(tag_spans) + '</div>'
    
    # Build comments HTML
    comments_html = '<p><em>No comments yet.</em></p>'
    if comments:
        comment_items = []
        for comment in comments:
            c_author = escape(comment.get('author', 'Anonymous'))
            c_date = escape(comment.get('date', ''))
            c_content = escape(comment.get('content', ''))
            comment_items.append(f"""<div class="comment" style="border-bottom: 1px solid #eee; padding: 15px 0;">
            <p style="margin: 0; font-weight: bold; color: #333;">{c_author} <span style="font-weight: normal; color: #999; font-size: 0.9em;">on {c_date}</span></p>
            <p style="margin: 8px 0 0; color: #555;">{c_content}</p>
        </div>""")
        comments_html = '\n'.join(comment_items)
    
    return f"""<article style="max-width: 800px; margin: 0 auto; padding: 20px;">
    <header style="border-bottom: 2px solid #eee; padding-bottom: 20px; margin-bottom: 30px;">
        <h1 style="color: #333; margin: 0 0 15px;">{title}</h1>
        <p style="color: #666; margin: 0;">By <strong>{author}</strong> on {date}</p>
    </header>
    
    <div class="content" style="line-height: 1.8; color: #444; font-size: 1.1em;">
        {content}
    </div>
    
    {tags_html}
    
    <section class="comments" style="margin-top: 40px; padding-top: 30px; border-top: 2px solid #eee;">
        <h3 style="color: #333;">Comments ({len(comments)})</h3>
        {comments_html}
    </section>
</article>"""

# Test
post = {
    'title': 'Getting Started with Python',
    'author': 'Jane Doe',
    'date': 'January 30, 2026',
    'content': 'Python is an amazing programming language that is easy to learn and powerful enough for professional use.',
    'tags': ['python', 'tutorial', 'beginners'],
    'comments': [
        {'author': 'Alice', 'date': 'Jan 31', 'content': 'Great article!'},
        {'author': 'Bob', 'date': 'Feb 1', 'content': 'Very helpful, thanks!'}
    ]
}

print("Blog post:")
print(render_blog_post(post)[:800] + "...")

# -------------------------------------------------------------------------
# Solution 3
# -------------------------------------------------------------------------
print("\n--- Solution 3: Data Table Template ---\n")

def render_data_table(data, options=None):
    """Generate HTML table with options."""
    if options is None:
        options = {}
    
    headers = data.get('headers', [])
    rows = data.get('rows', [])
    
    # Build styles based on options
    styles = ['width: 100%; border-collapse: collapse; font-family: Arial;']
    
    if options.get('bordered'):
        styles.append('border: 1px solid #ddd;')
    
    table_style = ' '.join(styles)
    
    # Headers
    headers_html = ''.join(
        f'<th style="background: #333; color: white; padding: 12px; text-align: left;">{escape(h)}</th>' 
        for h in headers
    )
    
    # Rows
    rows_html = ''
    for i, row in enumerate(rows):
        row_styles = []
        
        if options.get('striped') and i % 2 == 1:
            row_styles.append('background: #f9f9f9;')
        
        if options.get('hover'):
            row_styles.append('transition: background 0.2s;')
        
        row_style = ' '.join(row_styles) if row_styles else ''
        hover_attr = ' onmouseover="this.style.background=\'#f5f5f5\'" onmouseout="this.style.background=\'\'"' if options.get('hover') else ''
        
        cells = ''.join(f'<td style="padding: 12px; border-bottom: 1px solid #eee;">{escape(str(cell))}</td>' for cell in row)
        rows_html += f'        <tr style="{row_style}"{hover_attr}>{cells}</tr>\n'
    
    # Caption
    caption_html = ''
    if options.get('caption'):
        caption_html = f'<caption style="caption-side: top; text-align: left; font-weight: bold; padding: 10px;">{escape(options["caption"])}</caption>'
    
    return f"""<table style="{table_style}">
    {caption_html}
    <thead>
        <tr>{headers_html}</tr>
    </thead>
    <tbody>
{rows_html}    </tbody>
</table>"""

# Test
data = {
    'headers': ['Name', 'Role', 'Department', 'Status'],
    'rows': [
        ['Alice Johnson', 'Manager', 'Engineering', 'Active'],
        ['Bob Smith', 'Developer', 'Engineering', 'Active'],
        ['Carol White', 'Designer', 'Design', 'Away'],
        ['David Brown', 'Developer', 'Engineering', 'Active']
    ]
}

print("Table (striped=True):")
print(render_data_table(data, {'striped': True, 'caption': 'Employee Directory'}))

# -------------------------------------------------------------------------
# Solution 4
# -------------------------------------------------------------------------
print("\n--- Solution 4: Page Layout System ---\n")

from string import Template

class PageLayout:
    """Page layout with header, nav, content, footer."""
    
    BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$page_title</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            background: #f5f5f5;
        }
        header { 
            background: #2c3e50; 
            color: white; 
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        header h1 { margin: 0 0 15px; }
        nav ul { 
            list-style: none; 
            display: flex; 
            gap: 20px;
        }
        nav a { 
            color: #ecf0f1; 
            text-decoration: none;
            padding: 5px 10px;
            border-radius: 4px;
            transition: background 0.2s;
        }
        nav a:hover { background: rgba(255,255,255,0.1); }
        main { 
            max-width: 1000px; 
            margin: 30px auto; 
            padding: 0 20px;
        }
        .content { 
            background: white; 
            padding: 30px; 
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        footer { 
            text-align: center; 
            padding: 30px;
            color: #7f8c8d;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <header>
        <h1>$site_name</h1>
        <nav>
            <ul>
$nav_items
            </ul>
        </nav>
    </header>
    
    <main>
        <div class="content">
$page_content
        </div>
    </main>
    
    <footer>
        <p>&copy; 2026 $site_name. All rights reserved.</p>
    </footer>
</body>
</html>"""
    
    def __init__(self, site_name="My Site"):
        self.site_name = escape(site_name)
        self.nav_items = []
    
    def add_nav_item(self, name, url):
        """Add navigation item."""
        self.nav_items.append((name, url))
    
    def render(self, page_title, content):
        """Render complete page."""
        # Build nav HTML
        nav_html = '\n'.join(
            f'                <li><a href="{escape(url)}">{escape(name)}</a></li>'
            for name, url in self.nav_items
        )
        
        template = Template(self.BASE_TEMPLATE)
        return template.substitute(
            page_title=escape(page_title),
            site_name=self.site_name,
            nav_items=nav_html,
            page_content=content
        )

# Test
layout = PageLayout("Awesome Site")
layout.add_nav_item("Home", "/")
layout.add_nav_item("About", "/about")
layout.add_nav_item("Contact", "/contact")

page = layout.render("Welcome", "<h2>Hello World</h2><p>This is the content.</p>")
print("Page layout generated (first 700 chars):")
print(page[:700] + "...")

# -------------------------------------------------------------------------
# Solution 5
# -------------------------------------------------------------------------
print("\n--- Solution 5: Form Generator ---\n")

class FormGenerator:
    """Generate HTML forms from specifications."""
    
    def __init__(self):
        self.fields = []
        self.action = ''
        self.method = 'POST'
    
    def set_action(self, url):
        self.action = url
    
    def set_method(self, method):
        self.method = method
    
    def add_field(self, field_type, name, label, **options):
        """Add a field to the form."""
        field = {
            'type': field_type,
            'name': name,
            'label': label,
            'required': options.get('required', False),
            'placeholder': options.get('placeholder', ''),
            'value': options.get('value', ''),
            'options': options.get('options', [])
        }
        self.fields.append(field)
    
    def _render_field(self, field):
        """Render a single field."""
        ftype = field['type']
        name = escape(field['name'])
        label = escape(field['label'])
        required = ' required' if field['required'] else ''
        placeholder = escape(field['placeholder'])
        value = escape(field['value'])
        
        label_html = f'<label for="{name}" style="display: block; margin-bottom: 5px; font-weight: bold;">{label}:</label>'
        
        if ftype == 'textarea':
            input_html = f'<textarea name="{name}" id="{name}" placeholder="{placeholder}" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; resize: vertical;" rows="4"{required}></textarea>'
        
        elif ftype == 'select':
            options_html = '\n'.join(f'                    <option value="{escape(opt)}">{escape(opt)}</option>' for opt in field['options'])
            input_html = f"""<select name="{name}" id="{name}" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"{required}>
                    <option value="">-- Select --</option>
{options_html}
                </select>"""
        
        elif ftype == 'checkbox':
            checked = ' checked' if value else ''
            return f"""<div style="margin-bottom: 15px; display: flex; align-items: center; gap: 8px;">
                <input type="checkbox" name="{name}" id="{name}" value="1"{checked}{required}>
                <label for="{name}">{label}</label>
            </div>"""
        
        else:
            input_html = f'<input type="{ftype}" name="{name}" id="{name}" value="{value}" placeholder="{placeholder}" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"{required}>'
        
        return f"""<div style="margin-bottom: 15px;">
            {label_html}
            {input_html}
        </div>"""
    
    def render(self):
        """Render complete form."""
        fields_html = '\n'.join(self._render_field(f) for f in self.fields)
        
        return f"""<form action="{escape(self.action)}" method="{self.method}" style="max-width: 400px; padding: 25px; border: 1px solid #ddd; border-radius: 8px; background: white;">
{fields_html}
            <button type="submit" style="background: #007bff; color: white; padding: 10px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px;">Submit</button>
        </form>"""

# Test
form = FormGenerator()
form.set_action('/submit')
form.set_method('POST')
form.add_field('text', 'name', 'Full Name', required=True, placeholder='Enter your name')
form.add_field('email', 'email', 'Email Address', required=True)
form.add_field('select', 'country', 'Country', options=['USA', 'UK', 'Canada', 'Australia'])
form.add_field('textarea', 'message', 'Message', placeholder='Your message here...')
form.add_field('checkbox', 'newsletter', 'Subscribe to newsletter')

print("Generated form:")
print(form.render())

# -------------------------------------------------------------------------
# Solution 6
# -------------------------------------------------------------------------
print("\n--- Solution 6: Simple Template Engine ---\n")

import re

class MiniTemplate:
    """Minimal template engine with variables, conditionals, and loops."""
    
    def __init__(self, source):
        self.source = source
    
    def render(self, context=None):
        """Render template with context."""
        if context is None:
            context = {}
        
        result = self.source
        
        # Process conditionals
        result = self._process_conditionals(result, context)
        
        # Process loops
        result = self._process_loops(result, context)
        
        # Variable substitution (remaining {{ vars }})
        def replace_var(match):
            var_name = match.group(1).strip()
            value = context.get(var_name, '')
            return escape(str(value))
        
        result = re.sub(r'\{\{\s*(\w+)\s*\}\}', replace_var, result)
        
        return result
    
    def _process_conditionals(self, template, context):
        """Process {% if var %} blocks."""
        pattern = r'\{%\s*if\s+(\w+)\s*%\}(.*?)\{%\s*endif\s*%\}'
        
        def replace_if(match):
            condition = match.group(1)
            content = match.group(2)
            return content if context.get(condition) else ''
        
        return re.sub(pattern, replace_if, template, flags=re.DOTALL)
    
    def _process_loops(self, template, context):
        """Process {% for item in list %} blocks."""
        pattern = r'\{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%\}(.*?)\{%\s*endfor\s*%\}'
        
        def replace_for(match):
            item_name = match.group(1)
            list_name = match.group(2)
            content = match.group(3)
            
            items = context.get(list_name, [])
            results = []
            for item in items:
                # Replace item variable
                item_content = content.replace(f'{{{{ {item_name} }}}}', escape(str(item)))
                results.append(item_content)
            
            return ''.join(results)
        
        return re.sub(pattern, replace_for, template, flags=re.DOTALL)

# Test
template = MiniTemplate("""
<h1>{{ title }}</h1>
{% if show_list %}
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
{% endif %}
<p>Count: {{ count }}</p>
""")

result = template.render({
    'title': 'My List',
    'show_list': True,
    'items': ['Apple', 'Banana', 'Cherry'],
    'count': 3
})

print("Template result:")
print(result)

print("\n" + "=" * 60)
print("All solutions complete! Great job!")
print("=" * 60)
