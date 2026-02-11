"""
Static Site Generator - Project 10
===================================
A command-line static site generator that converts Markdown files to HTML.
Features Markdown parsing, templating, navigation, and asset copying.
"""

import json
import re
import shutil
from html import escape
from pathlib import Path
from string import Template


# =============================================================================
# MARKDOWN PARSER
# =============================================================================

class MarkdownParser:
    """Parse Markdown and convert to HTML."""

    @staticmethod
    def parse(content):
        """Convert Markdown content to HTML."""
        lines = content.split('\n')
        result = []
        in_code_block = False
        code_block_lines = []
        list_items = []

        for line in lines:
            if line.strip().startswith('```'):
                if in_code_block:
                    if list_items:
                        result.append(MarkdownParser._wrap_list(list_items))
                        list_items = []
                    result.append(f'<pre><code>{escape(chr(10).join(code_block_lines))}</code></pre>')
                    code_block_lines = []
                    in_code_block = False
                else:
                    if list_items:
                        result.append(MarkdownParser._wrap_list(list_items))
                        list_items = []
                    in_code_block = True
                continue

            if in_code_block:
                code_block_lines.append(line)
                continue

            list_type = MarkdownParser._get_list_type(line)
            if list_type:
                if list_items and list_items[-1]['type'] != list_type:
                    result.append(MarkdownParser._wrap_list(list_items))
                    list_items = []
                text = line.strip()[2:].strip() if list_type == 'ul' else line.split('.', 1)[1].strip()
                list_items.append({'type': list_type, 'text': MarkdownParser._parse_inline(text)})
            else:
                if list_items:
                    result.append(MarkdownParser._wrap_list(list_items))
                    list_items = []

                if line.startswith('#'):
                    result.append(MarkdownParser._parse_header(line))
                elif line.strip() == '---' or line.strip() == '***':
                    result.append('<hr>')
                elif not line.strip():
                    result.append('')
                else:
                    result.append(f'<p>{MarkdownParser._parse_inline(line)}</p>')

        if list_items:
            result.append(MarkdownParser._wrap_list(list_items))

        return '\n'.join(result)

    @staticmethod
    def _get_list_type(line):
        """Determine if line is a list item and return type."""
        stripped = line.strip()
        if stripped.startswith('* ') or stripped.startswith('- '):
            return 'ul'
        if re.match(r'^\d+\.', stripped):
            return 'ol'
        return None

    @staticmethod
    def _wrap_list(items):
        """Wrap list items in appropriate tags."""
        if not items:
            return ''
        tag = items[0]['type']
        content = '\n'.join(f'  <li>{item["text"]}</li>' for item in items)
        return f'<{tag}>\n{content}\n</{tag}>'

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
    def _parse_inline(text):
        """Parse inline Markdown elements."""
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(?!\*)(.*?)\*', r'<em>\1</em>', text)
        text = re.sub(r'_(?!_)(.*?)_', r'<em>\1</em>', text)
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        return text


# =============================================================================
# FRONTMATTER PARSER
# =============================================================================

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

        for line in lines[1:]:
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


# =============================================================================
# TEMPLATE LOADER
# =============================================================================

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


# =============================================================================
# TEMPLATE RENDERER
# =============================================================================

class TemplateRenderer:
    """Render templates with context."""

    @staticmethod
    def render(template, context):
        """Render template with context dictionary."""
        safe_context = {}
        for k, v in context.items():
            if k == 'content' or k == 'nav':
                safe_context[k] = str(v)
            else:
                safe_context[k] = escape(str(v))
        try:
            return template.substitute(**safe_context)
        except KeyError as e:
            raise KeyError(f"Missing template variable: {e}")


# =============================================================================
# PAGE CLASS
# =============================================================================

class Page:
    """Represents a single page in the site."""

    def __init__(self, path, content, metadata):
        """Initialize page with path, content, and metadata."""
        self.path = Path(path)
        self.content = content
        self.metadata = metadata
        self.html = None

        self.title = metadata.get('title', self._extract_title(content))
        self.date = metadata.get('date', '')
        self.author = metadata.get('author', '')
        self.tags = [t.strip() for t in metadata.get('tags', '').split(',')] if metadata.get('tags') else []
        self.draft = metadata.get('draft', 'false').lower() == 'true'

        self.relative_path = self._calculate_output_path()
        self.output_path = None

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


# =============================================================================
# CONTENT LOADER
# =============================================================================

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


# =============================================================================
# NAVIGATION BUILDER
# =============================================================================

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


# =============================================================================
# ASSET COPIER
# =============================================================================

class AssetCopier:
    """Copy static assets to output directory."""

    @staticmethod
    def copy(source_dir, output_dir):
        """Copy all files from source to output directory."""
        source_path = Path(source_dir)
        output_path = Path(str(output_dir)) / 'static'

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


# =============================================================================
# SITE GENERATOR
# =============================================================================

class StaticSiteGenerator:
    """Main static site generator."""

    def __init__(self, site_dir, output_dir='output'):
        """Initialize generator with site and output directories."""
        self.site_dir = Path(str(site_dir))
        self.output_dir = Path(str(output_dir))

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

        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)

        print("\nLoading content...")
        pages = self.content_loader.load_all()
        print(f"  Loaded {len(pages)} pages")

        print("\nLoading templates...")
        base_template = self.template_loader.load('base')
        print("  Loaded base template")

        print("\nGenerating navigation...")
        sorted_pages = self.content_loader.get_pages_sorted()
        nav_html = NavigationBuilder.build(sorted_pages)
        print("  Navigation generated")

        print("\nRendering pages...")
        for page in sorted_pages:
            page_html = page.render_html(base_template, nav_html, self.config)
            output_path = self.output_dir / page.relative_path
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(page_html)

            page.output_path = output_path
            print(f"  {page.relative_path}")

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


# =============================================================================
# CLI APPLICATION
# =============================================================================

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
        """Build site."""
        self.generator = StaticSiteGenerator(str(self.site_dir), str(self.output_dir))
        try:
            self.generator.build()
        except Exception as e:
            print(f"\nError building site: {e}")

    def preview_site(self):
        """Preview what will be generated."""
        print("\n--- Site Preview ---")
        generator = StaticSiteGenerator(str(self.site_dir), str(self.output_dir))

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
        generator = StaticSiteGenerator(str(self.site_dir), str(self.output_dir))
        generator.clean()

    def view_config(self):
        """View site configuration."""
        print("\n--- Site Configuration ---")
        generator = StaticSiteGenerator(str(self.site_dir), str(self.output_dir))
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


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Entry point for the Static Site Generator."""
    try:
        app = SSGApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!")


if __name__ == "__main__":
    main()
