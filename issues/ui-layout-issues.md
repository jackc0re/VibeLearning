# UI Layout Issues - 2026-01-30

**Status:** ✅ IMPLEMENTED - CSS Added  
**Date Fixed:** 2026-01-30  
**Related to:** Font Layout Investigation (#continuing)  

---

## Issues Identified from Screenshot [Image 2]

### Issue 1: Search Bar Too Narrow
**Location:** Header navigation bar  
**Problem:** Search input field appears much narrower than it should be, looks cramped  
**Current CSS:** Lines 522-539 in `stylesheets/extra.css` has basic styling but no width/max-width  
**Root Cause:** Likely missing width/max-width properties, or overridden by MkDocs defaults

### Issue 2: Back-to-Top Button Misaligned
**Location:** Right side of content area (floating button)  
**Problem:** The circular "back to top" button is positioned incorrectly - not aligned with page content  
**Current CSS:** Lines 498-517 has positioning rules but may need adjustment  
**Annotation:** "not aligned" - button appears off-center or wrong position

### Issue 3: Left Sidebar Too Wide
**Location:** Left navigation sidebar ("FOUNDATIONS" menu)  
**Problem:** Sidebar takes up too much horizontal space  
**Current CSS:** `.md-nav { font-size: 0.85rem; }` at line 440  
**Annotation:** "make smaller" - likely referring to width, not just font size

### Issue 4: Right Sidebar Too Wide
**Location:** Right TOC sidebar ("ON THIS PAGE")  
**Problem:** Table of contents sidebar is too wide  
**Current CSS:** `.md-nav--secondary .md-nav__link { font-size: 0.8rem; }` at line 688  
**Annotation:** "make smaller" - likely needs width reduction

---

## Proposed Fixes

### Fix 1: Search Bar Width
```css
.md-search {
  max-width: 400px !important;
}

.md-search__form {
  min-width: 200px !important;
}
```

### Fix 2: Back-to-Top Button Positioning
```css
.md-top {
  right: 1.5rem !important;
  bottom: 1.5rem !important;
  position: fixed !important;
  z-index: 100 !important;
}
```

### Fix 3 & 4: Sidebar Widths
```css
/* Left sidebar */
.md-sidebar--primary {
  width: 240px !important;
}

/* Right sidebar */
.md-sidebar--secondary {
  width: 220px !important;
}
```

---

## CSS to Add to `stylesheets/extra.css`

```css
/* ============================================================================
   LAYOUT FIXES - Width and Positioning Adjustments
   ============================================================================ */

/* Fix 1: Search bar width */
.md-search {
  max-width: 400px !important;
  flex-grow: 1 !important;
}

.md-search__form {
  min-width: 200px !important;
}

/* Fix 2: Back-to-top button positioning */
.md-top {
  right: 2rem !important;
  bottom: 2rem !important;
  position: fixed !important;
  z-index: 10 !important;
  /* Ensure proper centering of icon */
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

/* Fix 3: Left sidebar width */
.md-sidebar--primary {
  width: 240px !important;
  min-width: 240px !important;
}

@media screen and (min-width: 769px) {
  .md-sidebar--primary {
    width: 240px !important;
  }
}

/* Fix 4: Right sidebar (TOC) width */
.md-sidebar--secondary {
  width: 220px !important;
  min-width: 220px !important;
}

@media screen and (min-width: 1220px) {
  .md-sidebar--secondary {
    width: 220px !important;
  }
}

/* Also reduce content area max-width to accommodate narrower sidebars if needed */
.md-content {
  max-width: none !important;
}

/* Adjust sidebar font sizes to be even smaller */
.md-sidebar--primary .md-nav {
  font-size: 0.8rem !important;
}

.md-sidebar--secondary .md-nav {
  font-size: 0.75rem !important;
}

.md-sidebar--secondary .md-nav__title {
  font-size: 0.75rem !important;
}
```

---

## Testing Steps

1. ✅ CSS has been added to `docs/stylesheets/extra.css` (lines 790-852)
2. ✅ **STRONGER OVERRIDES added** (lines 853-900) - Uses `body` prefix for higher specificity
3. Run `./serve.sh` to start the development server (or hard refresh if already running)
4. Hard refresh browser (**Ctrl+Shift+R** or **Cmd+Shift+R**) to clear cache
5. Verify the fixes:
   - [ ] Search bar width is now ~200-400px (previously too narrow)
   - [ ] Back-to-top button is positioned correctly at bottom-right (2rem from edges)
   - [ ] Left sidebar width reduced to 240px (previously wider)
   - [ ] Right sidebar width reduced to 220px (previously wider)
   - [ ] Sidebar font sizes are smaller (0.8rem left, 0.75rem right)
   - [ ] Content area remains readable with adjusted sidebars

**IMPORTANT:** If you don't see changes after hard refresh, try:
- Restarting the server completely (stop with Ctrl+C, then run `./serve.sh`)
- Opening browser DevTools (F12) → Network tab → Disable cache checkbox → refresh
- Check in an incognito/private browsing window

---

## Additional Notes

- MkDocs Material uses responsive breakpoints at 768px and 1220px
- Default sidebar widths in MkDocs Material are typically ~250-300px
- The `!important` flags are necessary because MkDocs injects inline styles
- Consider testing at various screen widths (desktop, tablet, mobile)

---

## Related Files

- `stylesheets/extra.css` - Main stylesheet (needs updates)
- `mkdocs.yml` - Configuration
- `overrides/main.html` - Font loading template

