#!/bin/bash
# Branching - Examples
#
# This script demonstrates Git branching commands.
# Create a test directory first:
#   mkdir branch-demo && cd branch-demo

echo "=== Branching Examples ==="
echo "Create a test directory first:"
echo "  mkdir branch-demo && cd branch-demo"
echo ""

# =============================================================================
# 1. Setup Repository
# =============================================================================

echo "--- 1. Setup Repository ---"
echo ""
echo "# Initialize repository"
echo "git init"
echo ""
echo "# Create initial file"
echo "echo 'main line 1' > main.txt"
echo "git add main.txt"
echo "git commit -m 'Initial commit on main'"
echo ""

# =============================================================================
# 2. Listing Branches
# =============================================================================

echo "--- 2. Listing Branches ---"
echo ""
echo "# Show all branches"
echo "git branch"
echo ""
echo "# Show branches with commit info"
echo "git branch -v"
echo ""

# =============================================================================
# 3. Creating Branches
# =============================================================================

echo "--- 3. Creating Branches ---"
echo ""
echo "# Create a new branch"
echo "git branch feature-a"
echo ""
echo "# List branches (notice * on main)"
echo "git branch"
echo ""
echo "# Create and switch in one command"
echo "git checkout -b feature-b"
echo "# Or (Git 2.23+):"
echo "# git switch -c feature-b"
echo ""

# =============================================================================
# 4. Switching Branches
# =============================================================================

echo "--- 4. Switching Branches ---"
echo ""
echo "# Switch to branch feature-a"
echo "git checkout feature-a"
echo "# Or: git switch feature-a"
echo ""
echo "# Add content on feature-a"
echo "echo 'feature-a content' > feature.txt"
echo "git add feature.txt"
echo "git commit -m 'Add feature.txt on feature-a'"
echo ""
echo "# Check we're on feature-a"
echo "git branch -v"
echo ""

# =============================================================================
# 5. Work on Multiple Branches
# =============================================================================

echo "--- 5. Work on Multiple Branches ---"
echo ""
echo "# Switch to feature-b"
echo "git checkout feature-b"
echo ""
echo "# Add different content on feature-b"
echo "echo 'feature-b content' > feature.txt"
echo "git add feature.txt"
echo "git commit -m 'Add feature.txt on feature-b'"
echo ""
echo "# Switch back to main"
echo "git checkout main"
echo ""
echo "# Add content on main"
echo "echo 'main line 2' >> main.txt"
echo "git add main.txt"
echo "git commit -m 'Update main.txt'"
echo ""

# =============================================================================
# 6. Viewing Branch History
# =============================================================================

echo "--- 6. Viewing Branch History ---"
echo ""
echo "# Show commits on main"
echo "git log --oneline main"
echo ""
echo "# Show commits on feature-a"
echo "git log --oneline feature-a"
echo ""
echo "# Show commits on feature-b"
echo "git log --oneline feature-b"
echo ""
echo "# Show all branches with graph"
echo "git log --oneline --graph --all"
echo ""

# =============================================================================
# 7. Comparing Branches
# =============================================================================

echo "--- 7. Comparing Branches ---"
echo ""
echo "# Compare main with feature-a"
echo "git diff main feature-a"
echo ""
echo "# Show commits in feature-a not in main"
echo "git log main..feature-a --oneline"
echo ""
echo "# Show files changed between branches"
echo "git diff --name-only main feature-a"
echo ""

# =============================================================================
# 8. Renaming Branches
# =============================================================================

echo "--- 8. Renaming Branches ---"
echo ""
echo "# Rename current branch (make sure you're on feature-a)"
echo "git checkout feature-a"
echo "git branch -m feature-a-renamed"
echo ""
echo "# List branches to see rename"
echo "git branch"
echo ""
echo "# Rename back (you can rename other branches too)"
echo "git branch -m feature-a-renamed feature-a"
echo ""

# =============================================================================
# 9. Deleting Branches
# =============================================================================

echo "--- 9. Deleting Branches ---"
echo ""
echo "# Create a test branch"
echo "git branch test-branch"
echo "git branch"
echo ""
echo "# Delete unmerged branch (safe delete)"
echo "git branch -d test-branch"
echo "git branch"
echo ""

# =============================================================================
# 10. Merging Branches (Preview)
# =============================================================================

echo "--- 10. Merging Branches (Preview) ---"
echo ""
echo "# Merge feature-a into main"
echo "git checkout main"
echo "git merge feature-a"
echo ""
echo "# The merge creates a merge commit"
echo "git log --oneline --graph"
echo ""

# =============================================================================
# 11. Detached HEAD
# =============================================================================

echo "--- 11. Detached HEAD ---"
echo ""
echo "# Checkout a specific commit (detached HEAD)"
echo "git checkout HEAD~1"
echo ""
echo "# See we're in detached HEAD state"
echo "git status"
echo ""
echo "# Create a new branch from here"
echo "git checkout -b from-old-commit"
echo ""
echo "# Back to normal state"
echo "git checkout main"
echo ""

# =============================================================================
# 12. Viewing Branch Differences
# =============================================================================

echo "--- 12. Viewing Branch Differences ---"
echo ""
echo "# Show what's unique to each branch"
echo "git log --left-right main...feature-b --oneline"
echo ""
echo "# View file content from different branch"
echo "git show main:main.txt"
echo "git show feature-a:feature.txt"
echo ""

# =============================================================================
# 13. Branch Aliases
# =============================================================================

echo "--- 13. Branch Aliases ---"
echo ""
echo "# Common aliases"
echo "git config --global alias.co checkout"
echo "git config --global alias.br branch"
echo "git config --global alias.st status"
echo ""
echo "# Now you can use short forms"
echo "git br -v"
echo "git st"
echo ""

# =============================================================================
# 14. Branch from Tag
# =============================================================================

echo "--- 14. Branch from Tag ---"
echo ""
echo "# Create a tag on current commit"
echo "git tag v1.0"
echo ""
echo "# Create branch from tag"
echo "git branch maintenance v1.0"
echo "git branch"
echo ""

# =============================================================================
# 15. Tracking Remote Branches
# =============================================================================

echo "--- 15. Tracking Remote Branches ---"
echo ""
echo "# After cloning, you get remote tracking branches"
echo "git branch -r"
echo ""
echo "# Create local branch that tracks remote"
echo "git checkout -b local-main origin/main"
echo ""
echo "# Show tracking information"
echo "git branch -vv"
echo ""

# =============================================================================
# Cleanup Instructions
# =============================================================================

echo ""
echo "=== To clean up demo directory ==="
echo "cd .. && rm -rf branch-demo"
echo ""
