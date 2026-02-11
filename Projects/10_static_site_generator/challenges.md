# 🏆 Static Site Generator - Challenges

Extend your static site generator with these advanced features!

---

## Challenge 1: Syntax Highlighting

Add syntax highlighting to code blocks with color coding.

### Requirements
- Detect programming language in code blocks (````python`, ```javascript, etc.)
- Apply different colors for keywords, strings, comments
- Wrap code in span tags with CSS classes

### Hints
- Use regex to identify Python keywords (`def`, `class`, `import`, etc.)
- Create a dictionary mapping languages to keyword lists
- Generate CSS classes for each syntax element

### Sample Output
```html
<pre><code><span class="keyword">def</span> <span class="function">greet</span>(<span class="param">name</span>):
    <span class="string">return</span> <span class="string">f"Hello, {name}!"</span></code></pre>
```

---

## Challenge 2: RSS Feed Generation

Generate an RSS XML feed for blog posts.

### Requirements
- Create RSS 2.0 compliant XML
- Include recent blog posts (last 10)
- Add site metadata (title, description, URL)
- Generate RSS.xml file in output directory

### RSS Format
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>My Blog</title>
    <link>https://myblog.com</link>
    <description>My awesome blog</description>
    <item>
      <title>Post Title</title>
      <link>https://myblog.com/post.html</link>
      <pubDate>Mon, 01 Jan 2026 12:00:00 +0000</pubDate>
      <description>Post description...</description>
    </item>
  </channel>
</rss>
```

### Hints
- Use XML templates or string formatting
- Format dates properly for RFC 822
- Generate feed after rendering all pages

---

## Challenge 3: Sitemap Generation

Generate a sitemap.xml file for SEO.

### Requirements
- List all HTML pages in output directory
- Format as XML sitemap protocol
- Include last modified dates
- Add priority and optional change frequency

### Sitemap Format
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://myblog.com/index.html</loc>
    <lastmod>2026-02-11</lastmod>
    <priority>1.0</priority>
  </url>
</urlset>
```

### Hints
- Iterate through all generated pages
- Use page metadata for last modified dates
- Set higher priority for homepage

---

## Challenge 4: Pagination

Split long lists of posts into multiple pages.

### Requirements
- Limit posts per page (configurable, e.g., 5)
- Generate multiple HTML pages (page1, page2, etc.)
- Add "Previous" and "Next" navigation links
- Update page numbering in URLs

### Implementation
1. Add `posts_per_page` to config.json
2. Split pages list into chunks
3. For each chunk, generate a page
4. Add pagination controls at bottom of pages

### Hints
- Use list slicing: `pages[0:5]`, `pages[5:10]`, etc.
- Generate pagination HTML with page links
- Handle first and last page edge cases

---

## Challenge 5: Tags and Categories

Organize posts by tags and create tag pages.

### Requirements
- Parse `tags` from frontmatter (comma-separated)
- Generate individual tag pages (e.g., `tag-python.html`)
- List all posts with that tag
- Add tag cloud to sidebar

### Sample Implementation
```python
def generate_tag_pages(pages, template):
    """Generate pages for each unique tag."""
    all_tags = set()
    for page in pages:
        all_tags.update(page.tags)

    for tag in sorted(all_tags):
        tagged_pages = [p for p in pages if tag in p.tags]
        # Generate tag page with tagged_pages
```

### Tag Page Template
Add `$tag_name` and `$tagged_posts` variables to template.

---

## Challenge 6: Client-Side Search

Add a search feature using JavaScript.

### Requirements
- Create a searchable index of all pages
- Generate search.js with page titles and URLs
- Add search input to navigation
- Filter pages as user types

### Implementation
```javascript
// search.js
const pages = [
    {title: "Post 1", url: "post1.html", content: "..."},
    {title: "Post 2", url: "post2.html", content: "..."}
];

function search(query) {
    const results = pages.filter(page =>
        page.title.toLowerCase().includes(query.toLowerCase()) ||
        page.content.toLowerCase().includes(query.toLowerCase())
    );
    displayResults(results);
}
```

### Hints
- Strip HTML from content before indexing
- Include search.js in static assets
- Add search input field to base template

---

## Challenge 7: HTML/CSS Minification

Reduce file size by removing whitespace.

### Requirements
- Remove unnecessary whitespace from HTML
- Minify CSS files
- Create separate production build mode
- Maintain readability in development mode

### HTML Minifier
```python
def minify_html(html):
    """Remove unnecessary whitespace from HTML."""
    # Remove spaces between tags
    html = re.sub(r'>\s+<', '><', html)
    # Remove comments
    html = re.sub(r'<!--.*?-->', '', html)
    return html.strip()
```

### CSS Minifier
```python
def minify_css(css):
    """Minify CSS by removing whitespace."""
    css = re.sub(r'/\*.*?\*/', '', css)  # Remove comments
    css = re.sub(r'\s+', ' ', css)  # Collapse whitespace
    css = re.sub(r';\s*}', '}', css)  # Remove semicolons before closing braces
    return css.strip()
```

---

## Challenge 8: Custom Themes

Support multiple template themes.

### Requirements
- Add `themes/` directory with multiple base templates
- Allow theme selection in config.json
- Support theme-specific assets (CSS, images)
- Provide theme switcher in CLI

### Directory Structure
```
themes/
├── default/
│   ├── base.html
│   └── static/
│       └── style.css
└── dark/
    ├── base.html
    └── static/
        └── style.css
```

### Implementation
1. Update TemplateLoader to use theme directory
2. Load assets from theme-specific static folder
3. Add `theme` option to config.json

---

## Challenge 9: Watch Mode

Automatically rebuild when files change.

### Requirements
- Monitor content directory for changes
- Trigger rebuild when files are modified
- Display real-time build status
- Show which files changed

### Implementation
Use `os.path.getmtime()` to check modification times:

```python
import time
import os

def watch_site(site_dir, build_callback):
    """Watch site directory for changes."""
    file_times = {}
    
    # Initial scan
    for md_file in Path(site_dir).rglob('*.md'):
        file_times[str(md_file)] = os.path.getmtime(md_file)
    
    while True:
        for md_file in Path(site_dir).rglob('*.md'):
            current_mtime = os.path.getmtime(md_file)
            if current_mtime != file_times.get(str(md_file)):
                print(f"Detected change: {md_file}")
                build_callback()
                file_times[str(md_file)] = current_mtime
        time.sleep(1)
```

### Hints
- Add `--watch` command-line option
- Handle KeyboardInterrupt for clean exit
- Skip rebuild on temporary file changes

---

## Challenge 10: Deployment Support

Add deployment to hosting platforms.

### Requirements
- Support GitHub Pages deployment
- Support FTP upload
- Deploy from CLI menu
- Provide deployment feedback

### GitHub Pages Deployment
```python
def deploy_to_github(repo, branch='gh-pages'):
    """Deploy to GitHub Pages."""
    import subprocess
    subprocess.run(['git', 'checkout', 'gh-pages'])
    subprocess.run(['git', 'rm', '-rf', '.'])
    shutil.copytree('output', '.')
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Deploy site'])
    subprocess.run(['git', 'push', 'origin', 'gh-pages'])
    subprocess.run(['git', 'checkout', 'main'])
```

### FTP Deployment
```python
import ftplib

def deploy_ftp(host, username, password, output_dir):
    """Upload site via FTP."""
    with ftplib.FTP(host) as ftp:
        ftp.login(username, password)
        
        for file in Path(output_dir).rglob('*'):
            if file.is_file():
                with open(file, 'rb') as f:
                    ftp.storbinary(f'STOR {file.name}', f)
```

### Hints
- Add deployment settings to config.json
- Ask for credentials interactively (don't store in file)
- Provide deployment logs and error messages

---

## Bonus Challenge: Draft Preview Server

Start a local web server to preview generated site.

### Requirements
- Use Python's built-in `http.server`
- Serve files from output directory
- Auto-reload when files change
- Open browser automatically

### Implementation
```python
import http.server
import webbrowser

def serve_preview(output_dir, port=8000):
    """Start local preview server."""
    import os
    os.chdir(output_dir)
    
    server = http.server.HTTPServer(('', port), http.server.SimpleHTTPRequestHandler)
    print(f"Serving at http://localhost:{port}")
    
    webbrowser.open(f'http://localhost:{port}')
    server.serve_forever()
```

### Usage
Add "Preview" menu option that:
1. Builds the site
2. Starts preview server
3. Handles Ctrl+C to stop

---

## Challenge Tracker

Track your progress with this checklist:

| Challenge | Status | Date Completed |
|-----------|---------|----------------|
| 1. Syntax Highlighting | [ ] | |
| 2. RSS Feed | [ ] | |
| 3. Sitemap | [ ] | |
| 4. Pagination | [ ] | |
| 5. Tags & Categories | [ ] | |
| 6. Search | [ ] | |
| 7. Minification | [ ] | |
| 8. Custom Themes | [ ] | |
| 9. Watch Mode | [ ] | |
| 10. Deployment | [ ] | |
| Bonus: Preview Server | [ ] | |

---

## Tips for Success

1. **Start Simple** - Begin with easier challenges (RSS, Sitemap)
2. **Test Incrementally** - Verify each feature before moving on
3. **Refactor Often** - Keep code clean and organized
4. **Read Documentation** - Check Python docs for standard libraries
5. **Ask for Help** - Join communities if you get stuck

---

**Ready to level up your SSG? Pick a challenge and start coding! 🚀**
