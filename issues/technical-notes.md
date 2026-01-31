# Technical Notes - Font Investigation

## MkDocs Material Font Loading Mechanism

### How It Works

1. **mkdocs.yml configuration:**
   ```yaml
   font:
     text: Inter
     code: Fira Code
   ```

2. **Generated HTML:**
   ```html
   <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inter:300,300i,400,400i,700,700i%7CFira+Code:400,400i,700,700i&display=fallback">
   <style>:root{--md-text-font:"Inter";--md-code-font:"Fira Code"}</style>
   ```

3. **The Problem:**
   - The inline `<style>` tag comes AFTER `extra.css`
   - It overrides any `--md-text-font` or `--md-code-font` set in custom CSS
   - This happens even when `code:` is omitted (defaults to Roboto Mono)

## CSS Specificity Hierarchy

```
1. !important                    (Highest - use sparingly)
2. Inline styles                 (style="...")
3. IDs                           (#id)
4. Classes/attributes/pseudo     (.class, [attr], :hover)
5. Elements                      (div, p, html)
```

## Why `@import` Failed

```css
/* This blocks rendering of the ENTIRE CSS file */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono...');

/* None of this applies until the font loads */
:root {
  --md-primary-fg-color: #8839ef;
  /* ... all other variables ... */
}
```

## Why Template Override Works

```html
<!-- In <head>, loads asynchronously -->
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono..." rel="stylesheet">

<!-- Later in <head>, doesn't block -->
<link rel="stylesheet" href="stylesheets/extra.css">
```

## Solutions Considered

| Solution | Pros | Cons | Status |
|----------|------|------|--------|
| `@import` in CSS | Simple | Blocks CSS parsing | ❌ Rejected |
| Template override | Non-blocking | Requires custom template | ✅ Implemented |
| `!important` rules | Overrides inline styles | Messy, hard to maintain | ✅ Implemented |
| Self-host font | Full control | More setup required | ⏸️ Not tried |
| Use different font | Easy | Not JetBrains Mono | ⏸️ Not tried |

## Google Fonts API Versions

### v1 (what MkDocs uses)
```
https://fonts.googleapis.com/css?family=Font+Name:weights
```
- Space in name causes issues
- Limited weight options
- No variable fonts

### v2 (what we use in template)
```
https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap
```
- Better URL encoding
- More weight options
- Supports variable fonts
- Better caching

## File Structure for Local Development

```
VibeLearning/
├── mkdocs.yml              # Local dev config
├── overrides/              # Template overrides
│   └── main.html          # Font loading template
├── stylesheets/
│   └── extra.css          # Custom styles with !important
├── docs/                   # Copied from root for local testing
├── venv/                   # Virtual environment
└── site/                   # Built site (gitignored)
```

## Key Lessons

1. **MkDocs Material injects inline styles** - always check generated HTML
2. **CSS `@import` is render-blocking** - avoid in production CSS
3. **`<link>` tags load asynchronously** - preferred for fonts
4. **`!important` is necessary** when fighting inline styles
5. **Hard refresh (Ctrl+Shift+R)** - essential when testing CSS changes

## References

- MkDocs Material: https://squidfunk.github.io/mkdocs-material/
- CSS @import: https://developer.mozilla.org/en-US/docs/Web/CSS/@import
- Google Fonts: https://developers.google.com/fonts/docs/css2
