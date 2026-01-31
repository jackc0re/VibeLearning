# Local Development Guide

This guide explains how to set up and run the VibeLearning documentation site locally before pushing to GitHub.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Quick Start

The easiest way to get started is using the provided helper scripts:

### 1. Start Local Server (Development Mode)

```bash
./serve.sh
```

This will:
- Create a virtual environment (if not exists)
- Install all dependencies
- Set up the docs directory
- Start the local server at `http://127.0.0.1:8000/VibeLearning/`

The server supports **live reload** - changes to markdown files will automatically refresh the browser.

### 2. Build Static Site

```bash
./build.sh
```

This will:
- Build the static site to `./site/` directory
- Report any build errors
- Show you how to view the built site

### 3. Deploy to GitHub Pages

```bash
./deploy.sh
```

This will:
- Build the site with production configuration
- Deploy to the `gh-pages` branch
- Restore local development configuration after deployment

### 4. Clean Build Artifacts

```bash
./clean.sh
```

This removes:
- `site/` - Built static files
- `docs/` - Temporary docs directory for local testing
- Python cache files
- Backup files

## Manual Setup (Advanced)

If you prefer to set up manually:

### Step 1: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Docs Directory

For local testing, MkDocs requires a `docs/` subdirectory:

```bash
mkdir -p docs
cp README.md docs/
cp -r [0-9]* docs/
cp -r Resources docs/
cp -r stylesheets docs/
```

### Step 4: Run Local Server

```bash
mkdocs serve --dev-addr=127.0.0.1:8000
```

Visit: `http://127.0.0.1:8000/VibeLearning/`

## Project Structure for Local Development

```
VibeLearning/
├── venv/                   # Virtual environment (auto-created)
├── docs/                   # Docs directory for local testing (auto-created)
│   ├── README.md
│   ├── 01_foundations/
│   ├── 02_data_structures/
│   └── ...
├── site/                   # Built static site (auto-created)
├── stylesheets/
│   └── extra.css          # Custom styles
├── mkdocs.yml             # Local dev config (uses docs/)
├── requirements.txt       # Python dependencies
├── serve.sh              # Start dev server
├── build.sh              # Build static site
├── deploy.sh             # Deploy to GitHub Pages
└── clean.sh              # Clean build artifacts
```

## Configuration Differences

### Local Development (`mkdocs.yml`)

```yaml
docs_dir: docs      # Use subdirectory
site_dir: site
```

### GitHub Pages Deployment

For GitHub Pages, the configuration uses `docs_dir: .` (root directory) because the site is built directly from the repository root.

The `deploy.sh` script automatically switches configurations during deployment.

## Troubleshooting

### Port Already in Use

If port 8000 is busy, use a different port:

```bash
./serve.sh 8080
```

### Emoji Extension Error

The emoji extension is currently disabled due to compatibility issues with Python 3.14. This doesn't affect the site's functionality.

### Font Not Loading

If JetBrains Mono doesn't load properly:
1. Check your internet connection
2. Clear browser cache
3. Check browser console for CSS errors

### Build Warnings

You may see warnings about:
- Excluded files (.py, .sh) being linked
- Relative links not being recognized
- Navigation items not included

These are expected and don't affect the site's functionality.

## Testing Checklist

Before pushing to GitHub, verify:

- [ ] Site builds without errors (`./build.sh`)
- [ ] Local server runs (`./serve.sh`)
- [ ] Custom CSS loads correctly
- [ ] JetBrains Mono font appears in code blocks
- [ ] Layout looks correct (no broken sizing/rounding)
- [ ] Navigation works properly
- [ ] Dark/light mode toggle works
- [ ] Search functionality works

## Git Workflow

1. Make changes to content
2. Test locally with `./serve.sh`
3. Build and verify with `./build.sh`
4. Commit changes: `git add . && git commit -m "Your message"`
5. Push to GitHub: `git push origin main`
6. Deploy to Pages: `./deploy.sh` (if not using GitHub Actions)

## Notes

- The `docs/` directory is for local testing only - it's in `.gitignore`
- The `site/` directory is also in `.gitignore`
- Always use the helper scripts to ensure consistent setup
