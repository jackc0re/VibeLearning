# 🎨 HTML & CSS Overview

> Understanding the building blocks of web pages

---

## What is HTML?

**HTML** (HyperText Markup Language) is the skeleton of web pages. It defines the structure and content using **tags** that tell the browser what each element is.

Think of HTML like the structure of a house:
- Walls, rooms, doors = HTML elements
- The blueprint = HTML document structure

---

## Basic HTML Document Structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

| Part | Purpose |
|------|---------|
| `<!DOCTYPE html>` | Tells browser this is HTML5 |
| `<html>` | Root element of the page |
| `<head>` | Metadata (title, styles, scripts) |
| `<title>` | Text shown in browser tab |
| `<body>` | Visible content of the page |

---

## Common HTML Tags

### Text Elements

| Tag | Purpose | Example |
|-----|---------|---------|
| `<h1>` - `<h6>` | Headings (largest to smallest) | `<h1>Main Title</h1>` |
| `<p>` | Paragraph | `<p>Some text here</p>` |
| `<a>` | Link (anchor) | `<a href="url">Click me</a>` |
| `<strong>` | Bold/important text | `<strong>Warning!</strong>` |
| `<em>` | Italic/emphasized text | `<em>Note:</em>` |
| `<br>` | Line break | `Line 1<br>Line 2` |
| `<hr>` | Horizontal rule (divider) | `<hr>` |

### Lists

```html
<!-- Unordered list (bullets) -->
<ul>
    <li>First item</li>
    <li>Second item</li>
</ul>

<!-- Ordered list (numbers) -->
<ol>
    <li>Step one</li>
    <li>Step two</li>
</ol>
```

### Tables

```html
<table>
    <tr>  <!-- Table row -->
        <th>Name</th>  <!-- Table header -->
        <th>Age</th>
    </tr>
    <tr>
        <td>Alice</td>  <!-- Table data -->
        <td>25</td>
    </tr>
</table>
```

### Forms & Input

```html
<form action="/submit" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    
    <button type="submit">Submit</button>
</form>
```

### Container Elements

| Tag | Purpose |
|-----|---------|
| `<div>` | Generic block container |
| `<span>` | Generic inline container |
| `<header>` | Page/site header |
| `<nav>` | Navigation links |
| `<main>` | Main content area |
| `<footer>` | Page footer |
| `<section>` | Thematic grouping |
| `<article>` | Self-contained content |

---

## HTML Attributes

Attributes provide additional information about elements:

```html
<!-- Common attributes -->
<a href="https://example.com" target="_blank" class="link">Link</a>
<img src="photo.jpg" alt="Description" width="300">
<div id="main" class="container highlighted">Content</div>
<input type="text" name="username" placeholder="Enter username" required>
```

| Attribute | Purpose |
|-----------|---------|
| `id` | Unique identifier (one per page) |
| `class` | Classification (can have multiple) |
| `href` | Link destination |
| `src` | Source file path |
| `alt` | Alternative text for images |
| `name` | Form field name |
| `value` | Input value |
| `placeholder` | Hint text in inputs |
| `required` | Makes field mandatory |

---

## What is CSS?

**CSS** (Cascading Style Sheets) is the skin and makeup of web pages. It controls how HTML elements look:
- Colors, fonts, sizes
- Spacing and positioning
- Layout and responsiveness

---

## Ways to Add CSS

### 1. Inline Style (directly on element)
```html
<p style="color: blue; font-size: 18px;">Blue text</p>
```

### 2. Internal Style Sheet (in `<head>`)
```html
<head>
    <style>
        p { color: blue; font-size: 18px; }
    </style>
</head>
```

### 3. External Style Sheet (recommended)
```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

---

## CSS Selectors

Selectors determine which elements get styled:

```css
/* Element selector - all paragraphs */
p { color: blue; }

/* Class selector - elements with class="highlight" */
.highlight { background: yellow; }

/* ID selector - element with id="header" */
#header { font-size: 24px; }

/* Descendant selector - links inside nav */
nav a { text-decoration: none; }

/* Multiple selectors */
h1, h2, h3 { font-family: Arial; }
```

---

## Common CSS Properties

### Colors & Backgrounds
```css
body {
    color: #333333;           /* Text color */
    background-color: #f0f0f0; /* Page background */
    background-image: url('bg.jpg');
}
```

### Text & Fonts
```css
h1 {
    font-family: Arial, sans-serif;
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    line-height: 1.5;
}
```

### Box Model (Spacing)
```css
div {
    /* Content area */
    width: 300px;
    height: 200px;
    
    /* Spacing inside the box */
    padding: 20px;
    
    /* Border around the box */
    border: 2px solid black;
    
    /* Spacing outside the box */
    margin: 10px;
}
```

**Box Model Visualization:**
```
┌─────────────────────────────┐
│          MARGIN             │
│   ┌─────────────────────┐   │
│   │       BORDER        │   │
│   │   ┌─────────────┐   │   │
│   │   │   PADDING   │   │   │
│   │   │   ┌─────┐   │   │   │
│   │   │   │CONTENT│   │   │   │
│   │   │   └─────┘   │   │   │
│   │   └─────────────┘   │   │
│   └─────────────────────┘   │
└─────────────────────────────┘
```

### Layout Properties
```css
.container {
    display: flex;           /* or block, inline, grid */
    justify-content: center; /* Horizontal alignment */
    align-items: center;     /* Vertical alignment */
}

/* Common display values */
.block { display: block; }      /* Takes full width */
.inline { display: inline; }    /* Flows with text */
.inline-block { display: inline-block; } /* Hybrid */
.hidden { display: none; }       /* Not visible */
```

---

## Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        
        header {
            background: #333;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px;
        }
        
        h1 { margin: 0; }
        
        .card {
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .highlight {
            color: #007bff;
            font-weight: bold;
        }
        
        footer {
            text-align: center;
            color: #666;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to My Site</h1>
    </header>
    
    <div class="card">
        <h2>About Me</h2>
        <p>I am a <span class="highlight">Python developer</span> 
           learning web development.</p>
    </div>
    
    <div class="card">
        <h2>Projects</h2>
        <ul>
            <li>Calculator App</li>
            <li>To-Do List</li>
            <li>Weather Dashboard</li>
        </ul>
    </div>
    
    <footer>
        <p>&copy; 2026 My Portfolio</p>
    </footer>
</body>
</html>
```

---

## Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| Forgetting closing tags | Breaks page structure | Always close tags: `<p></p>` |
| Using `<br>` for spacing | Semantically wrong, hard to style | Use CSS `margin` instead |
| Multiple elements with same `id` | IDs must be unique | Use `class` for styling groups |
| Inline styles everywhere | Hard to maintain | Use external CSS files |
| Tables for layout | Wrong semantic meaning | Use `<div>` or semantic elements |

---

## Quick Reference

```html
<!-- Document template -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <!-- Content here -->
</body>
</html>
```

```css
/* Common reset styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* Center container */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
```

---

## Next Steps

Now that you understand HTML and CSS basics, let's see how to serve these pages with Python!

→ Continue to [02: HTTP Server](../02_http_server/)
