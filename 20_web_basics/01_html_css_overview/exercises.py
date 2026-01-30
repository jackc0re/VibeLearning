"""
HTML & CSS Overview - Exercises
===============================
Practice generating HTML with Python.

Try to solve each exercise before looking at the solution!
"""

print("=" * 60)
print("HTML & CSS OVERVIEW - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Personal Introduction Page
# =============================================================================
print("\n--- Exercise 1: Personal Introduction Page ---\n")
"""
Create a function `create_intro_page(name, bio, hobbies)` that generates
an HTML page introducing a person.

The page should include:
- A title with the person's name
- A paragraph with their bio
- An unordered list of their hobbies

Example output structure:
<!DOCTYPE html>
<html>
<head><title>About [name]</title></head>
<body>
    <h1>[name]</h1>
    <p>[bio]</p>
    <h2>Hobbies</h2>
    <ul><li>hobby1</li>...</ul>
</body>
</html>
"""

# Your code here:


# =============================================================================
# EXERCISE 2: Product Card Generator
# =============================================================================
print("\n--- Exercise 2: Product Card Generator ---\n")
"""
Create a function `create_product_card(product)` that generates HTML for
a product card.

The product dictionary has: name, price, description, in_stock

Requirements:
- Display the product name as a heading
- Show the price formatted as $XX.XX
- Include the description
- Show "In Stock" or "Out of Stock" with different colors
  (green for in stock, red for out of stock)

Use inline styles for the stock status colors.
"""

# Your code here:


# =============================================================================
# EXERCISE 3: Blog Post Preview
# =============================================================================
print("\n--- Exercise 3: Blog Post Preview ---\n")
"""
Create a function `create_blog_preview(posts)` that generates HTML for
a list of blog post previews.

Each post has: title, author, date, excerpt, url

Requirements:
- Each post should be in an <article> tag
- Title should link to the post URL
- Show author and date on one line
- Show excerpt as a paragraph
- Add CSS styling to make it look nice

Return the complete HTML document.
"""

# Your code here:


# =============================================================================
# EXERCISE 4: Data Table with Styling
# =============================================================================
print("\n--- Exercise 4: Data Table with Styling ---\n")
"""
Create a function `create_styled_table(data, striped=True)` that generates
an HTML table with CSS styling.

The data parameter is a dictionary with 'headers' (list) and 'rows' (list of lists).

Requirements:
- Generate a table with the provided headers and rows
- Add CSS to style the header with a dark background
- If striped=True, alternate row colors (white/light gray)
- Add border-collapse to remove gaps between cells
- Make the table width 100%
"""

# Your code here:


# =============================================================================
# EXERCISE 5: Form Builder
# =============================================================================
print("\n--- Exercise 5: Form Builder ---\n")
"""
Create a function `create_form(fields, action, method='POST')` that
generates an HTML form from a field specification.

The fields parameter is a list of dictionaries, each with:
- type: 'text', 'email', 'password', 'textarea', 'select'
- name: the field name
- label: the display label
- required: boolean (optional)
- options: list of choices for select type (optional)

Example field:
{'type': 'text', 'name': 'username', 'label': 'Username', 'required': True}

Generate appropriate HTML for each field type.
"""

# Your code here:


# =============================================================================
# EXERCISE 6: Responsive Grid Layout
# =============================================================================
print("\n--- Exercise 6: Responsive Grid Layout ---\n")
"""
Create a function `create_grid_layout(items, columns=3)` that generates
a responsive grid of items.

Requirements:
- Each item should be in a div with class "grid-item"
- Use CSS Grid or Flexbox for layout
- The grid should have the specified number of columns
- Add gap between items
- Each item should have a border and padding
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
print("\n--- Solution 1: Personal Introduction Page ---\n")

def create_intro_page(name, bio, hobbies):
    hobbies_html = "\n        ".join(f"<li>{h}</li>" for h in hobbies)
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>About {name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; }}
        h1 {{ color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }}
        ul {{ line-height: 1.8; }}
    </style>
</head>
<body>
    <h1>{name}</h1>
    <p>{bio}</p>
    <h2>Hobbies</h2>
    <ul>
        {hobbies_html}
    </ul>
</body>
</html>"""

# Test
html = create_intro_page(
    "Alice Johnson",
    "A passionate developer who loves creating things.",
    ["Coding", "Hiking", "Photography", "Reading"]
)
print(html[:500] + "...")

# -------------------------------------------------------------------------
# Solution 2
# -------------------------------------------------------------------------
print("\n--- Solution 2: Product Card Generator ---\n")

def create_product_card(product):
    in_stock = product.get('in_stock', False)
    stock_color = "green" if in_stock else "red"
    stock_text = "In Stock" if in_stock else "Out of Stock"
    price = f"${product['price']:.2f}"
    
    return f"""<div class="product-card" style="border: 1px solid #ddd; padding: 20px; max-width: 300px; border-radius: 8px;">
    <h2>{product['name']}</h2>
    <p class="price" style="font-size: 24px; font-weight: bold; color: #007bff;">{price}</p>
    <p class="description">{product['description']}</p>
    <p class="stock" style="color: {stock_color}; font-weight: bold;">{stock_text}</p>
</div>"""

# Test
product = {
    'name': 'Wireless Headphones',
    'price': 79.99,
    'description': 'High-quality wireless headphones with noise cancellation.',
    'in_stock': True
}
print(create_product_card(product))

# -------------------------------------------------------------------------
# Solution 3
# -------------------------------------------------------------------------
print("\n--- Solution 3: Blog Post Preview ---\n")

def create_blog_preview(posts):
    articles = []
    for post in posts:
        article = f"""    <article style="margin-bottom: 30px; padding: 20px; background: #f9f9f9; border-radius: 8px;">
        <h2><a href="{post['url']}" style="color: #333; text-decoration: none;">{post['title']}</a></h2>
        <p style="color: #666; font-size: 0.9em;">By {post['author']} on {post['date']}</p>
        <p>{post['excerpt']}</p>
        <a href="{post['url']}" style="color: #007bff;">Read more →</a>
    </article>"""
        articles.append(article)
    
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Blog</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
    </style>
</head>
<body>
    <h1>Latest Posts</h1>
{chr(10).join(articles)}
</body>
</html>"""

# Test
posts = [
    {
        'title': 'Getting Started with Python',
        'author': 'Jane Doe',
        'date': '2026-01-15',
        'excerpt': 'Python is a versatile language perfect for beginners...',
        'url': '/posts/python-intro'
    },
    {
        'title': 'Web Development Basics',
        'author': 'John Smith',
        'date': '2026-01-20',
        'excerpt': 'Understanding HTML and CSS is essential for web development...',
        'url': '/posts/web-basics'
    }
]
print(create_blog_preview(posts)[:800] + "...")

# -------------------------------------------------------------------------
# Solution 4
# -------------------------------------------------------------------------
print("\n--- Solution 4: Data Table with Styling ---\n")

def create_styled_table(data, striped=True):
    headers = data['headers']
    rows = data['rows']
    
    header_html = "".join(f"<th>{h}</th>" for h in headers)
    
    rows_html = ""
    for i, row in enumerate(rows):
        row_style = "background: #f2f2f2;" if (striped and i % 2 == 1) else ""
        cells = "".join(f"<td>{cell}</td>" for cell in row)
        rows_html += f"            <tr style='{row_style}'>{cells}</tr>\n"
    
    return f"""<table style="width: 100%; border-collapse: collapse; font-family: Arial;">
    <thead>
        <tr style="background: #333; color: white;">
            {header_html}
        </tr>
    </thead>
    <tbody>
{rows_html}    </tbody>
</table>"""

# Test
data = {
    'headers': ['Product', 'Price', 'Stock'],
    'rows': [
        ['Laptop', '$999', '15'],
        ['Mouse', '$29', '50'],
        ['Keyboard', '$79', '30'],
        ['Monitor', '$299', '10']
    ]
}
print(create_styled_table(data))

# -------------------------------------------------------------------------
# Solution 5
# -------------------------------------------------------------------------
print("\n--- Solution 5: Form Builder ---\n")

def create_form(fields, action, method='POST'):
    fields_html = []
    
    for field in fields:
        ftype = field['type']
        name = field['name']
        label = field['label']
        required = ' required' if field.get('required') else ''
        
        if ftype == 'textarea':
            input_html = f'<textarea name="{name}" id="{name}"{required}></textarea>'
        elif ftype == 'select':
            options = "\n                ".join(
                f'<option value="{opt}">{opt}</option>' 
                for opt in field.get('options', [])
            )
            input_html = f'<select name="{name}" id="{name}"{required}>\n                {options}\n            </select>'
        else:
            input_html = f'<input type="{ftype}" name="{name}" id="{name}"{required}>'
        
        field_html = f"""    <div style="margin-bottom: 15px;">
        <label for="{name}" style="display: block; margin-bottom: 5px; font-weight: bold;">{label}:</label>
        {input_html}
    </div>"""
        fields_html.append(field_html)
    
    return f"""<form action="{action}" method="{method}" style="max-width: 400px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
{chr(10).join(fields_html)}
    <button type="submit" style="background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Submit</button>
</form>"""

# Test
fields = [
    {'type': 'text', 'name': 'username', 'label': 'Username', 'required': True},
    {'type': 'email', 'name': 'email', 'label': 'Email', 'required': True},
    {'type': 'select', 'name': 'country', 'label': 'Country', 
     'options': ['USA', 'UK', 'Canada', 'Australia']},
    {'type': 'textarea', 'name': 'bio', 'label': 'Bio'}
]
print(create_form(fields, '/submit'))

# -------------------------------------------------------------------------
# Solution 6
# -------------------------------------------------------------------------
print("\n--- Solution 6: Responsive Grid Layout ---\n")

def create_grid_layout(items, columns=3):
    items_html = "\n    ".join(
        f'<div class="grid-item" style="border: 1px solid #ddd; padding: 20px; border-radius: 4px;">{item}</div>' 
        for item in items
    )
    
    return f"""<div class="grid" style="display: grid; grid-template-columns: repeat({columns}, 1fr); gap: 20px;">
    {items_html}
</div>"""

# Test
items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6']
print(create_grid_layout(items, columns=3))

print("\n" + "=" * 60)
print("All solutions complete! Great job practicing!")
print("=" * 60)
