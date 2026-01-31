# Font Layout Issue Investigation

**Status:** 🔍 In Progress  
**Date:** 2026-01-30  
**Issue:** Changing code font to JetBrains Mono causes entire site layout to break

---

## Problem Summary

When attempting to change the code font from `Fira Code` to `JetBrains Mono`, the entire website's layout becomes broken:

- Elements appear smaller than intended
- Border radius on elements (tables, buttons) is wrong
- Code blocks display at incorrect sizes
- Sidebar navigation becomes too large or too small
- "Back to top" button displays incorrectly

---

## Root Cause Analysis

### Initial Hypothesis (WRONG)
Initially suspected Google Fonts API v1 vs v2 issue with `@import` being render-blocking.

### Actual Root Cause
**MkDocs Material injects inline CSS that overrides custom CSS variables.**

In the generated HTML, MkDocs adds:
```html
<style>:root{--md-text-font:"Inter";--md-code-font:"Roboto Mono"}</style>
```

This inline style appears AFTER `extra.css` is loaded, overriding the custom `--md-code-font` variable defined in the stylesheet.

---

## Attempted Solutions

### Attempt 1: CSS `@import` (FAILED)
Removed `code:` font from `mkdocs.yml` and used:
```css
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono...');
```

**Result:** CSS became render-blocking, entire stylesheet failed to apply until font loaded.

### Attempt 2: Template Override with `<link>` (PARTIAL SUCCESS)
Created `overrides/main.html` to load font via `<link>` tag in HTML head:
```html
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono..." rel="stylesheet">
```

**Result:** Font loads, but MkDocs inline style still overrides CSS variables.

### Attempt 3: CSS `!important` Rules (CURRENT STATE - PARTIAL)
Added `!important` to critical style rules to override MkDocs defaults.

**Current Fixes Applied:**
- ✅ `font-family` in code blocks uses `!important`
- ✅ Table border-radius uses `!important`
- ✅ Back-to-top button dimensions use `!important`
- ✅ Navigation font sizes adjusted

---

## Current Issues Remaining

Based on user feedback screenshots:

### Issue 1: Back to Top Button ✅ FIXED
- **Problem:** Shows text "Back" instead of just arrow icon, misaligned
- **Status:** Fixed - added positioning rules (right: 2rem, bottom: 2rem)
- **See:** `ui-layout-issues.md` for details

### Issue 2: Left Sidebar Navigation ✅ FIXED
- **Problem:** Font size too large, width too wide (marked "make smaller")
- **Status:** Reduced font to 0.8rem, width set to 240px
- **See:** `ui-layout-issues.md` for details

### Issue 3: Right Sidebar (TOC) ✅ FIXED
- **Problem:** Width too wide (marked "make smaller")
- **Status:** Width reduced to 220px, font size 0.75rem
- **See:** `ui-layout-issues.md` for details

### Issue 4: Search Bar ✅ FIXED
- **Problem:** Width too narrow (marked "too small")
- **Status:** Added min-width: 200px, max-width: 400px
- **See:** `ui-layout-issues.md` for details

### Issue 5: Layout Scaling
- **Problem:** Overall scaling feels "off" compared to original
- **Status:** Fixed via sidebar width adjustments - see `ui-layout-issues.md`

---

## Files Modified

| File | Change |
|------|--------|
| `mkdocs.yml` | Removed `code:` font, added `custom_dir: overrides` |
| `stylesheets/extra.css` | Multiple `!important` rules added, font size adjustments |
| `overrides/main.html` | Template override for font loading |
| `requirements.txt` | Created for local development |
| `serve.sh`, `build.sh`, `deploy.sh`, `clean.sh` | Helper scripts created |

---

## Technical Details

### MkDocs Font Loading Behavior

MkDocs Material generates this inline style automatically:
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inter:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&display=fallback">
<style>:root{--md-text-font:"Inter";--md-code-font:"Roboto Mono"}</style>
```

Even when `code:` is omitted from `mkdocs.yml`, it defaults to `Roboto Mono`.

### CSS Specificity Issues

The inline `<style>` tag has equal specificity to external CSS, but because it appears AFTER the external CSS in the DOM, it takes precedence.

**Selector Specificity Comparison:**
- `:root` selector = 0,1,0 (1 element)
- `html` selector = 0,1,0 (1 element)  
- Inline style = 1,0,0,0 (highest)

Using `!important` is currently the only way to override the inline style.

---

## Recommended Next Steps

1. **Test current state:** Verify the latest fixes resolve the layout issues
2. **Compare with original:** Check if layout now matches the pre-font-change version
3. **Fine-tune sizes:** Adjust specific font sizes if still not right
4. **Consider alternative:** Use a different monospaced font that's in Google Fonts v1 API
5. **Long-term fix:** Submit issue to MkDocs Material about font override behavior

---

## Related Links

- MkDocs Material Font Documentation: https://squidfunk.github.io/mkdocs-material/setup/changing-the-fonts/
- CSS Specificity: https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity
- Google Fonts v2 API: https://developers.google.com/fonts/docs/css2

---

## Local Testing Commands

```bash
# Start development server
./serve.sh

# Build for testing
./build.sh

# Deploy to GitHub Pages
./deploy.sh

# Clean build artifacts
./clean.sh
```

Server URL: http://127.0.0.1:8000/VibeLearning/
