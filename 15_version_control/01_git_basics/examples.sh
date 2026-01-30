#!/bin/bash
# Git Basics - Examples
#
# This script demonstrates basic Git commands.
# NOTE: These are example commands. Do not run this entire script
# at once - read each section and try commands manually.
#
# Setup: Create a temporary directory to experiment
#   mkdir git-demo && cd git-demo

echo "=== Git Basics Examples ==="
echo "Create a test directory first:"
echo "  mkdir git-demo && cd git-demo"
echo ""

# =============================================================================
# 1. Initialize Repository
# =============================================================================

echo "--- 1. Initialize Repository ---"
echo ""
echo "# Create a new Git repository"
echo "git init"
echo ""
echo "# Check Git status"
echo "git status"
echo ""

# =============================================================================
# 2. Create and Stage Files
# =============================================================================

echo "--- 2. Create and Stage Files ---"
echo ""
echo "# Create a Python file"
echo "cat > hello.py << EOF"
echo "def greet():"
echo "    print('Hello, World!')"
echo ""
echo "if __name__ == '__main__':"
echo "    greet()"
echo "EOF"
echo ""
echo "# Check status (file is untracked)"
echo "git status"
echo ""
echo "# Stage the file"
echo "git add hello.py"
echo ""
echo "# Check status (file is now staged)"
echo "git status"
echo ""

# =============================================================================
# 3. First Commit
# =============================================================================

echo "--- 3. First Commit ---"
echo ""
echo "# Commit the staged file"
echo "git commit -m 'Initial commit: Add hello.py'"
echo ""
echo "# View the commit history"
echo "git log"
echo ""
echo "# View compact history"
echo "git log --oneline"
echo ""

# =============================================================================
# 4. Making Changes
# =============================================================================

echo "--- 4. Making Changes ---"
echo ""
echo "# Modify the file"
echo "cat > hello.py << EOF"
echo "def greet(name='World'):"
echo "    print(f'Hello, {name}!')"
echo ""
echo "def farewell():"
echo "    print('Goodbye!')"
echo ""
echo "if __name__ == '__main__':"
echo "    greet()"
echo "    farewell()"
echo "EOF"
echo ""
echo "# Check status (file is modified)"
echo "git status"
echo ""
echo "# See what changed"
echo "git diff"
echo ""

# =============================================================================
# 5. Staging Changes
# =============================================================================

echo "--- 5. Staging Changes ---"
echo ""
echo "# Stage the changes"
echo "git add hello.py"
echo ""
echo "# Check status (file is staged)"
echo "git status"
echo ""
echo "# See what's staged"
echo "git diff --staged"
echo ""

# =============================================================================
# 6. Second Commit
# =============================================================================

echo "--- 6. Second Commit ---"
echo ""
echo "# Commit the changes"
echo "git commit -m 'Add name parameter and farewell function'"
echo ""
echo "# View history"
echo "git log --oneline"
echo ""

# =============================================================================
# 7. Viewing Differences
# =============================================================================

echo "--- 7. Viewing Differences ---"
echo ""
echo "# Compare working directory with last commit"
echo "git diff HEAD"
echo ""
echo "# View changes in a specific commit"
echo "git show HEAD"
echo ""
echo "# View changes between two commits"
echo "git diff HEAD~1 HEAD"
echo ""

# =============================================================================
# 8. Working with Multiple Files
# =============================================================================

echo "--- 8. Working with Multiple Files ---"
echo ""
echo "# Create another file"
echo "cat > utils.py << EOF"
echo "def add(a, b):"
echo "    return a + b"
echo ""
echo "def multiply(a, b):"
echo "    return a * b"
echo "EOF"
echo ""
echo "# Stage both files"
echo "git add ."
echo ""
echo "# Check what will be committed"
echo "git status"
echo ""
echo "# Commit both files"
echo "git commit -m 'Add utility functions for math operations'"
echo ""
echo "# View history"
echo "git log --oneline"
echo ""

# =============================================================================
# 9. Staging Selectively
# =============================================================================

echo "--- 9. Staging Selectively ---"
echo ""
echo "# Modify both files"
echo "echo 'print(\"Loaded\")' >> utils.py"
echo "echo '# Main entry point' >> hello.py"
echo ""
echo "# Check status"
echo "git status"
echo ""
echo "# Stage only one file"
echo "git add hello.py"
echo ""
echo "# Check status (hello.py staged, utils.py not)"
echo "git status"
echo ""

# =============================================================================
# 10. .gitignore File
# =============================================================================

echo "--- 10. .gitignore File ---"
echo ""
echo "# Create .gitignore"
echo "cat > .gitignore << EOF"
echo "# Python cache"
echo "__pycache__/"
echo "*.pyc"
echo ""
echo "# Virtual environments"
echo ".venv/"
echo "venv/"
echo ""
echo "# IDE"
echo ".vscode/"
echo ""
echo "# Logs"
echo "*.log"
echo "EOF"
echo ""
echo "# Create a file that matches .gitignore pattern"
echo "touch test.log"
echo ""
echo "# Check status (test.log is not shown)"
echo "git status"
echo ""

# =============================================================================
# 11. Moving and Renaming Files
# =============================================================================

echo "--- 11. Moving and Renaming Files ---"
echo ""
echo "# Rename a file using git mv"
echo "git mv hello.py main.py"
echo ""
echo "# Check status (Git tracks it as a rename)"
echo "git status"
echo ""
echo "# Commit the rename"
echo "git commit -m 'Rename hello.py to main.py'"
echo ""
echo "# View history (file history is preserved)"
echo "git log --oneline --follow main.py"
echo ""

# =============================================================================
# 12. Viewing Commit Details
# =============================================================================

echo "--- 12. Viewing Commit Details ---"
echo ""
echo "# Show detailed commit info"
echo "git show HEAD"
echo ""
echo "# Show file stats in commits"
echo "git log --stat"
echo ""
echo "# Show who changed what"
echo "git log --pretty=format:'%h - %an, %ar : %s'"
echo ""

# =============================================================================
# 13. Short History Commands
# =============================================================================

echo "--- 13. Short History Commands ---"
echo ""
echo "# Common short forms"
echo "git st      # git status"
echo "git co      # git checkout"
echo "git br      # git branch"
echo "git ci      # git commit"
echo ""
echo "# (Note: These require alias configuration)"
echo ""
echo "# Add aliases to your git config:"
echo "git config --global alias.st status"
echo "git config --global alias.co checkout"
echo "git config --global alias.br branch"
echo "git config --global alias.ci commit"
echo ""

# =============================================================================
# 14. Cleaning Up
# =============================================================================

echo "--- 14. Cleaning Up ---"
echo ""
echo "# View untracked files"
echo "git clean -n"
echo ""
echo "# Remove untracked files (dry run first!)"
echo "git clean -f"
echo ""
echo "# Remove untracked directories"
echo "git clean -fd"
echo ""

# =============================================================================
# Cleanup Instructions
# =============================================================================

echo ""
echo "=== To clean up demo directory ==="
echo "cd .. && rm -rf git-demo"
echo ""
