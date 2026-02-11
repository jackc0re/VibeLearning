---
title: About
date: 2026-02-11
author: Your Name
---

# About This Site

Welcome to the about page! Here you can learn more about this Static Site Generator project.

## What is a Static Site Generator?

A **Static Site Generator (SSG)** is a tool that takes content (usually Markdown) and templates (HTML) and generates a complete website of static HTML files.

### Why Use a Static Site?

Static sites have many advantages:

- **Performance** - No server-side processing, just serve HTML
- **Security** - No database, no server vulnerabilities
- **Cost** - Host anywhere for free (GitHub Pages, Netlify, Vercel)
- **Simplicity** - Easy to deploy and maintain
- **Version Control** - Content is just text files

## How This SSG Works

This Static Site Generator is built with Python and includes:

### Features

1. **Markdown Parsing** - Convert Markdown to HTML with regex
   - Headers (h1-h6)
   - Bold, italic, and emphasis
   - Links and images
   - Lists (ordered and unordered)
   - Code blocks with syntax highlighting
   - Tables and blockquotes

2. **Template System** - Reusable HTML layouts
   - Base template for all pages
   - Variable substitution
   - Navigation menu
   - HTML escaping for security

3. **Content Management** - Organize your content
   - Load Markdown files
   - Extract frontmatter (metadata)
   - Generate navigation
   - Handle drafts

4. **Asset Handling** - Include static resources
   - Copy CSS, JS, and images
   - Preserve directory structure
   - Handle missing assets gracefully

## Project Structure

```
site/
├── config.json       # Site configuration
├── content/          # Markdown files
│   ├── index.md
│   ├── about.md
│   └── blog/
├── templates/        # HTML templates
│   └── base.html
└── static/           # CSS, JS, images
    └── style.css
```

## Technology Stack

This project uses only the Python standard library:

- `re` - Regular expressions for Markdown parsing
- `string.Template` - HTML template substitution
- `pathlib` - Cross-platform file paths
- `json` - Site configuration
- `html.escape` - HTML escaping for security
- `shutil` - File and directory operations

## Future Enhancements

Planned features for this SSG:

- Syntax highlighting for code blocks
- RSS feed generation
- Sitemap.xml for SEO
- Tags and categories
- Search functionality
- Pagination
- Multiple template themes
- Watch mode for auto-rebuild

## License

This project is part of the VibeLearning educational repository.

---

*Happy building!*
