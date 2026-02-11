# 🌐 Project 10: Static Site Generator

Build a command-line static site generator that converts Markdown files to HTML websites with templating, navigation, and asset copying. Create a complete website from content and templates!

---

## 📋 Project Overview

This project helps you practice:
- **Markdown parsing** — Convert Markdown to HTML with regex
- **Templating** — Use `string.Template` for HTML layouts
- **File processing** — Read/write files, copy directories
- **OOP design** — Classes for pages, templates, and generators
- **CLI design** — Menu-driven user interface
- **Project architecture** — Organize content, templates, and assets

### Features to Build

1. **Markdown to HTML Conversion**
   - Headers, bold, italic, links, images
   - Lists (ordered and unordered)
   - Code blocks and inline code
   - Frontmatter extraction (metadata)

2. **Template System**
   - Base HTML layout
   - Variable substitution
   - Navigation generation
   - HTML escaping for security

3. **Content Management**
   - Load Markdown files
   - Parse content and metadata
   - Generate page objects
   - Build navigation menu

4. **Asset Handling**
   - Copy CSS, JS, images
   - Preserve directory structure
   - Handle missing assets gracefully

5. **CLI Interface**
   - Build site from content
   - Preview generation plan
   - Clean output directory
   - Configuration management

---

## 💻 Requirements

### Prerequisites

Complete these modules before starting:
- [00_getting_started](../../00_getting_started/README.md)
- [01_foundations](../../01_foundations/README.md) — especially strings, files
- [02_data_structures](../../02_data_structures/README.md)
- [10_file_io](../../10_file_io/README.md) — file reading/writing, JSON
- [20_web_basics](../../20_web_basics/README.md) — HTML, templates

### Skills You'll Use

- **Regular Expressions** — Parse Markdown syntax
- **string.Template** — Substitute template variables
- **File I/O** — Read content, write HTML, copy assets
- **pathlib** — Handle file paths correctly
- **JSON** — Store site configuration
- **HTML** — Generate valid markup
- **Classes** — Create Page, Template, and Generator classes

---

## 🚀 Development Steps

### Step 1: Markdown Parser (40 minutes)

Create functions to convert Markdown to HTML:

```python
import re
from html import escape

class MarkdownParser:
    """Parse Markdown and convert to HTML."""

    @staticmethod
    def parse(content):
        """Convert Markdown content to HTML."""
        lines = content.split('\n')
        result = []
        in_code_block = False
        code_block_lines = []

        for line in lines:
            # Handle code blocks
            if line.strip().startswith('```'):
                if in_code_block:
                    result.append(f'<pre><code>{escape(chr(10).join(code_block_lines))}</code></pre>')
                    code_block_lines = []
                    in_code_block = False
                else:
                    in_code_block = True
                continue

            if in_code_block:
                code_block_lines.append(line)
                continue

            # Headers
            if line.startswith('#'):
                result.append(MarkdownParser._parse_header(line))
            # Unordered lists
            elif line.strip().startswith('* ') or line.strip().startswith('- '):
                result.append(MarkdownParser._parse_list_item(line, 'ul'))
            # Ordered lists
            elif re.match(r'^\d+\.', line.strip()):
                result.append(MarkdownParser._parse_list_item(line, 'ol'))
            # Horizontal rule
            elif line.strip() == '---' or line.strip() == '***':
                result.append('<hr>')
            # Empty line (paragraph break)
            elif not line.strip():
                result.append('')
            else:
                # Paragraph with inline elements
                result.append(MarkdownParser._parse_inline(line))

        return '\n'.join(result)

    @staticmethod
    def _parse_header(line):
        """Parse Markdown header to HTML."""
        level = len(line) - len(line.lstrip('#'))
        if level > 6:
            level = 6
        text = line.lstrip('#').strip()
        text = MarkdownParser._parse_inline(text)
        return f'<h{level}>{text}</h{level}>'

    @staticmethod
    def _parse_list_item(line, list_type):
        """Parse list item to HTML."""
        text = line.strip()[2:].strip() if list_type == 'ul' else line.split('.', 1)[1].strip()
        text = MarkdownParser._parse_inline(text)
        tag = 'li'
        return f'<{tag}>{text}</{tag}>'

    @staticmethod
    def _parse_inline(text):
        """Parse inline Markdown elements."""
        # Bold: **text** or __text__
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)

        # Italic: *text* or _text_
        text = re.sub(r'\*(?!\*)(.*?)\*', r'<em>\1</em>', text)
        text = re.sub(r'_(?!_)(.*?)_', r'<em>\1</em>', text)

        # Links: [text](url)
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

        # Images: ![alt](url)
        text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)

        # Inline code: `code`
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

        return text
```

### Step 2: Frontmatter Parser (15 minutes)

Extract metadata from Markdown files:

```python
class FrontmatterParser:
    """Parse YAML-style frontmatter from Markdown files."""

    @staticmethod
    def parse(content):
        """Extract frontmatter and return metadata and remaining content."""
        lines = content.split('\n')
        if not lines or lines[0].strip() != '---':
            return {}, content

        metadata = {}
        content_lines = []
        in_frontmatter = True

        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                in_frontmatter = False
                continue
            elif in_frontmatter:
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
            else:
                content_lines.append(line)

        return metadata, '\n'.join(content_lines)
```

### Step 3: Template System (30 minutes)

Create template loader and renderer:

```python
from string import Template
from pathlib import Path

class TemplateLoader:
    """Load HTML templates from files."""

    def __init__(self, template_dir):
        """Initialize with template directory path."""
        self.template_dir = Path(template_dir)
        self.cache = {}

    def load(self, name):
        """Load template by name."""
        if name in self.cache:
            return self.cache[name]

        template_path = self.template_dir / f"{name}.html"
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.cache[name] = Template(content)
            return self.cache[name]
        except FileNotFoundError:
            raise FileNotFoundError(f"Template not found: {template_path}")


class TemplateRenderer:
    """Render templates with context."""

    @staticmethod
    def render(template, context):
        """Render template with context dictionary."""
        # Escape all context values for security
        safe_context = {k: escape(str(v)) for k, v in context.items()}
        try:
            return template.substitute(**safe_context)
        except KeyError as e:
            raise KeyError(f"Missing template variable: {e}")
```

### Step 4: Page Class (25 minutes)

Create a class to represent a page:

```python
class Page:
    """Represents a single page in the site."""

    def __init__(self, path, content, metadata):
        """Initialize page with path, content, and metadata."""
        self.path = Path(path)
        self.content = content
        self.metadata = metadata
        self.html = None

        # Extract metadata with defaults
        self.title = metadata.get('title', self._extract_title(content))
        self.date = metadata.get('date', '')
        self.author = metadata.get('author', '')
        self.tags = [t.strip() for t in metadata.get('tags', '').split(',')] if metadata.get('tags') else []
        self.draft = metadata.get('draft', 'false').lower() == 'true'

        # Calculate output path
        self.relative_path = self._calculate_output_path()
        self.output_path = None  # Set by generator

    def _extract_title(self, content):
        """Extract title from first header."""
        for line in content.split('\n'):
            if line.startswith('#'):
                return line.lstrip('#').strip()
        return 'Untitled'

    def _calculate_output_path(self):
        """Calculate relative output path from input path."""
        if self.path.name == 'index.md':
            return 'index.html'

        stem = self.path.stem
        parent = self.path.parent.name if self.path.parent.name != 'content' else ''

        if parent:
            return f"{parent}/{stem}.html"
        return f"{stem}.html"

    def render_html(self, template, nav_html, site_config):
        """Render page to HTML using template."""
        context = {
            'title': self.title,
            'content': MarkdownParser.parse(self.content),
            'nav': nav_html,
            'site_name': site_config.get('site_name', 'My Site'),
            'site_url': site_config.get('site_url', ''),
            'author': self.author,
            'date': self.date
        }

        renderer = TemplateRenderer()
        self.html = renderer.render(template, context)
        return self.html

    def is_draft(self):
        """Check if page is marked as draft."""
        return self.draft
```

### Step 5: Content Manager (25 minutes)

Create a class to load and manage all content:

```python
import json

class ContentLoader:
    """Load and manage all Markdown content."""

    def __init__(self, content_dir):
        """Initialize with content directory path."""
        self.content_dir = Path(content_dir)
        self.pages = []

    def load_all(self):
        """Load all Markdown files from content directory."""
        self.pages = []
        md_files = list(self.content_dir.rglob('*.md'))

        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                metadata, content = FrontmatterParser.parse(content)
                page = Page(md_file, content, metadata)

                if not page.is_draft():
                    self.pages.append(page)
            except Exception as e:
                print(f"Error loading {md_file}: {e}")

        return self.pages

    def get_pages_sorted(self, sort_by='date', reverse=True):
        """Get pages sorted by field."""
        if sort_by == 'date':
            return sorted(self.pages, key=lambda p: p.date, reverse=reverse)
        elif sort_by == 'title':
            return sorted(self.pages, key=lambda p: p.title, reverse=reverse)
        else:
            return self.pages
```

### Step 6: Navigation Generator (20 minutes)

Create navigation generation:

```python
class NavigationBuilder:
    """Build navigation HTML from pages."""

    @staticmethod
    def build(pages, current_page=None):
        """Build navigation menu HTML."""
        nav_items = []

        for page in pages:
            link_class = 'active' if current_page and page.relative_path == current_page.relative_path else ''
            active_class = f' class="{link_class}"' if link_class else ''
            nav_items.append(f'<a href="{page.relative_path}"{active_class}>{escape(page.title)}</a>')

        return ' | '.join(nav_items)
```

### Step 7: Asset Copier (20 minutes)

Create asset copying functionality:

```python
import shutil

class AssetCopier:
    """Copy static assets to output directory."""

    @staticmethod
    def copy(source_dir, output_dir):
        """Copy all files from source to output directory."""
        source_path = Path(source_dir)
        output_path = Path(output_dir) / 'static'

        if not source_path.exists():
            print(f"Warning: Static directory not found: {source_path}")
            return 0

        try:
            if output_path.exists():
                shutil.rmtree(output_path)
            shutil.copytree(source_path, output_path)
            return len(list(output_path.rglob('*')))
        except Exception as e:
            print(f"Error copying assets: {e}")
            return 0
```

### Step 8: Site Generator (30 minutes)

Create the main generator class:

```python
class StaticSiteGenerator:
    """Main static site generator."""

    def __init__(self, site_dir, output_dir='output'):
        """Initialize generator with site and output directories."""
        self.site_dir = Path(site_dir)
        self.output_dir = Path(output_dir)

        self.config = self._load_config()
        self.content_loader = ContentLoader(self.site_dir / 'content')
        self.template_loader = TemplateLoader(self.site_dir / 'templates')

    def _load_config(self):
        """Load site configuration from config.json."""
        config_path = self.site_dir / 'config.json'
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {'site_name': 'My Site', 'site_url': ''}

    def build(self):
        """Build the entire static site."""
        print("\n" + "=" * 50)
        print("BUILDING STATIC SITE")
        print("=" * 50)

        # Create output directory
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)

        # Load content
        print("\nLoading content...")
        pages = self.content_loader.load_all()
        print(f"  Loaded {len(pages)} pages")

        # Load base template
        print("\nLoading templates...")
        base_template = self.template_loader.load('base')
        print("  Loaded base template")

        # Generate navigation
        print("\nGenerating navigation...")
        sorted_pages = self.content_loader.get_pages_sorted()
        nav_html = NavigationBuilder.build(sorted_pages)
        print("  Navigation generated")

        # Render and write pages
        print("\nRendering pages...")
        for page in sorted_pages:
            page_html = page.render_html(base_template, nav_html, self.config)
            output_path = self.output_dir / page.relative_path
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(page_html)

            page.output_path = output_path
            print(f"  {page.relative_path}")

        # Copy static assets
        print("\nCopying static assets...")
        static_dir = self.site_dir / 'static'
        asset_count = AssetCopier.copy(static_dir, self.output_dir)
        print(f"  Copied {asset_count} files")

        print("\n" + "=" * 50)
        print(f"Site built successfully: {len(pages)} pages, {asset_count} assets")
        print(f"Output directory: {self.output_dir.absolute()}")
        print("=" * 50)

        return True

    def clean(self):
        """Clean output directory."""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
            print(f"\nCleaned: {self.output_dir}")
            return True
        print("\nNothing to clean")
        return False
```

### Step 9: CLI Interface (30 minutes)

Create the menu-driven CLI:

```python
class SSGApp:
    """Static Site Generator CLI application."""

    def __init__(self):
        """Initialize application."""
        self.site_dir = Path(__file__).parent / 'sample_site'
        self.output_dir = Path(__file__).parent / 'output'
        self.generator = None

    def display_welcome(self):
        """Display welcome screen."""
        print("\n" + "=" * 60)
        print("     STATIC SITE GENERATOR")
        print("=" * 60)
        print("\nConvert Markdown files to a static HTML website!")
        print("Build blogs, portfolios, and documentation sites.")
        print("\n" + "=" * 60)

    def display_menu(self):
        """Display main menu."""
        print("\n" + "=" * 40)
        print("           MAIN MENU")
        print("=" * 40)
        print("1. Build Site")
        print("2. Preview Site")
        print("3. Clean Output")
        print("4. View Config")
        print("5. Exit")
        print("=" * 40)

    def build_site(self):
        """Build the site."""
        self.generator = StaticSiteGenerator(self.site_dir, self.output_dir)
        try:
            self.generator.build()
        except Exception as e:
            print(f"\nError building site: {e}")

    def preview_site(self):
        """Preview what will be generated."""
        print("\n--- Site Preview ---")
        generator = StaticSiteGenerator(self.site_dir, self.output_dir)

        print(f"\nSite Directory: {self.site_dir.absolute()}")
        print(f"Output Directory: {self.output_dir.absolute()}")

        pages = generator.content_loader.load_all()
        print(f"\nPages ({len(pages)}):")

        for page in pages:
            status = "[DRAFT]" if page.is_draft() else ""
            print(f"  {page.relative_path:30s} {page.title:30s} {status}")

    def clean_output(self):
        """Clean output directory."""
        print("\n--- Clean Output ---")
        generator = StaticSiteGenerator(self.site_dir, self.output_dir)
        generator.clean()

    def view_config(self):
        """View site configuration."""
        print("\n--- Site Configuration ---")
        generator = StaticSiteGenerator(self.site_dir, self.output_dir)
        print(json.dumps(generator.config, indent=2))

    def get_choice(self, min_val, max_val):
        """Get valid menu choice."""
        while True:
            try:
                choice = int(input(f"\nEnter choice ({min_val}-{max_val}): "))
                if min_val <= choice <= max_val:
                    return choice
                print(f"Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run(self):
        """Main application loop."""
        self.display_welcome()

        while True:
            self.display_menu()
            choice = self.get_choice(1, 5)

            if choice == 1:
                self.build_site()
            elif choice == 2:
                self.preview_site()
            elif choice == 3:
                self.clean_output()
            elif choice == 4:
                self.view_config()
            elif choice == 5:
                print("\nThanks for using Static Site Generator! Goodbye!")
                break


def main():
    """Entry point for the Static Site Generator."""
    try:
        app = SSGApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!")


if __name__ == "__main__":
    main()
```

---

## 🧪 Testing

Test your static site generator with these scenarios:

### Basic Build
1. Run "Build Site" command
2. Verify HTML files are generated
3. Check navigation links work
4. Verify static assets are copied

### Markdown Parsing
1. Test headers (h1-h6)
2. Test bold and italic
3. Test links and images
4. Test lists (ordered and unordered)
5. Test code blocks

### Template Rendering
1. Verify base template is applied
2. Check variables are substituted
3. Verify navigation is generated
4. Check HTML escaping works

### Navigation
1. Test navigation menu is generated
2. Check current page highlighting
3. Verify links point to correct pages

### Assets
1. Test CSS is copied
2. Test images are copied
3. Test directory structure preserved
4. Test missing static directory handling

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How to parse Markdown with regex
- ✅ How to build a template system
- ✅ How to manage multi-file projects
- ✅ How to generate HTML programmatically
- ✅ How to handle file paths correctly
- ✅ How to build a CLI application

---

## 🏆 Challenges

Complete these challenges to enhance your static site generator:

1. **Syntax Highlighting** — Highlight code blocks with color
2. **RSS Feed** — Generate RSS XML for blog posts
3. **Sitemap** — Generate sitemap.xml for SEO
4. **Pagination** — Split long content into multiple pages
5. **Tags/Categories** — Filter pages by metadata
6. **Search** — Add client-side search functionality
7. **Minification** — Minify HTML/CSS output
8. **Custom Themes** — Switch between different templates
9. **Watch Mode** — Auto-rebuild on file changes
10. **Deployment** — Upload to FTP or GitHub Pages

See [challenges.md](challenges.md) for detailed instructions.

---

## 📁 File Structure

```
10_static_site_generator/
├── README.md              # This file
├── generator.py           # Main implementation
├── sample_site/          # Sample site for testing
│   ├── config.json       # Site configuration
│   ├── content/          # Markdown files
│   │   ├── index.md
│   │   ├── about.md
│   │   └── blog/
│   │       ├── first-post.md
│   │       └── second-post.md
│   ├── templates/        # HTML templates
│   │   └── base.html
│   └── static/           # CSS, JS, images
│       └── style.css
└── challenges.md          # Additional challenge tasks
```

---

## 📚 Related Topics

| Topic | Location |
|-------|----------|
| File I/O | [10_file_io](../../10_file_io/README.md) |
| HTML/Templates | [20_web_basics](../../20_web_basics/README.md) |
| JSON | [10_file_io/03_working_with_json](../../10_file_io/03_working_with_json/) |
| Regular Expressions | [01_foundations/07_strings](../../01_foundations/07_strings/) |

---

**Ready to start?** Create `generator.py` and begin building! 🚀
