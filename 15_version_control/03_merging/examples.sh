#!/bin/bash
# Merging - Examples
#
# This script demonstrates Git merging commands.
# Create a test directory first:
#   mkdir merge-demo && cd merge-demo

echo "=== Merging Examples ==="
echo "Create a test directory first:"
echo "  mkdir merge-demo && cd merge-demo"
echo ""

# =============================================================================
# 1. Setup Repository with Branches
# =============================================================================

echo "--- 1. Setup Repository ---"
echo ""
echo "# Initialize repository"
echo "git init"
echo ""
echo "# Create initial commit on main"
echo "echo 'line 1' > file.txt"
echo "git add file.txt"
echo "git commit -m 'Initial commit'"
echo ""
echo "# Create feature branch"
echo "git checkout -b feature"
echo "echo 'feature content' >> file.txt"
echo "git add file.txt"
echo "git commit -m 'Add feature content'"
echo ""
echo "# Return to main and add more content"
echo "git checkout main"
echo "echo 'main content' >> file.txt"
echo "git add file.txt"
echo "git commit -m 'Add main content'"
echo ""

# =============================================================================
# 2. Fast-Forward Merge
# =============================================================================

echo "--- 2. Fast-Forward Merge ---"
echo ""
echo "# Fast-forward merge (main hasn't diverged from feature)"
echo "git checkout feature-a  # Assume main is behind"
echo "git checkout main"
echo "git merge feature-a"
echo "# No merge commit created, just moved pointer"
echo ""

# =============================================================================
# 3. Three-Way Merge
# =============================================================================

echo "--- 3. Three-Way Merge ---"
echo ""
echo "# Three-way merge (both branches have commits)"
echo "git checkout main"
echo "git merge feature"
echo "# Creates merge commit"
echo ""
echo "# View merge commit"
echo "git log --graph --oneline"
echo ""

# =============================================================================
# 4. Merge with Custom Message
# =============================================================================

echo "--- 4. Merge with Custom Message ---"
echo ""
echo "# Merge with custom message"
echo "git merge another-branch -m \"Integrate user management feature\""
echo ""

# =============================================================================
# 5. No Fast-Forward Merge
# =============================================================================

echo "--- 5. No Fast-Forward Merge ---"
echo ""
echo "# Always create merge commit (even if fast-forward possible)"
echo "git merge feature --no-ff -m \"Merge feature branch\""
echo ""
echo "# This preserves feature history on main"
echo "git log --graph --oneline"
echo ""

# =============================================================================
# 6. Merge Conflict Example
# =============================================================================

echo "--- 6. Merge Conflict ---"
echo ""
echo "# Simulate conflict:"
echo "# On main:"
echo "git checkout main"
echo "echo 'main version' > conflict.txt"
echo "git add conflict.txt"
echo "git commit -m 'Add conflict.txt with main version'"
echo ""
echo "# On feature:"
echo "git checkout feature"
echo "echo 'feature version' > conflict.txt"
echo "git add conflict.txt"
echo "git commit -m 'Add conflict.txt with feature version'"
echo ""
echo "# Try to merge (will conflict)"
echo "git checkout main"
echo "git merge feature"
echo "# CONFLICT: file.txt"
echo ""

# =============================================================================
# 7. Viewing Conflicts
# =============================================================================

echo "--- 7. Viewing Conflicts ---"
echo ""
echo "# Check merge status"
echo "git status"
echo ""
echo "# See conflicted files"
echo "git diff --name-only --diff-filter=U"
echo ""
echo "# View the conflict in file"
echo "# File shows:"
echo "# <<<<<<< HEAD"
echo "# main version"
echo "# ======="
echo "# feature version"
echo "# >>>>>>> feature"
echo ""

# =============================================================================
# 8. Resolving Conflicts
# =============================================================================

echo "--- 8. Resolving Conflicts ---"
echo ""
echo "# Edit the file to resolve conflict"
echo "# Remove markers and keep desired content"
echo "echo 'resolved version' > conflict.txt"
echo ""
echo "# Stage resolved file"
echo "git add conflict.txt"
echo ""
echo "# Complete merge"
echo "git commit"
echo ""

# =============================================================================
# 9. Aborting Merge
# =============================================================================

echo "--- 9. Aborting Merge ---"
echo ""
echo "# Cancel merge, return to pre-merge state"
echo "git merge --abort"
echo ""
echo "# Status shows 'Not currently on any branch' if in middle of merge"
echo ""

# =============================================================================
# 10. Squash Merge
# =============================================================================

echo "--- 10. Squash Merge ---"
echo ""
echo "# Combine all branch commits into one"
echo "git checkout main"
echo "git merge --squash feature"
echo ""
echo "# All feature changes are staged, but not committed"
echo "# Create one commit"
echo "git commit -m \"Add login feature (complete)\""
echo ""
echo "# Result: one clean commit, no branch history on main"
echo "git log --oneline"
echo ""

# =============================================================================
# 11. Cherry-Picking
# =============================================================================

echo "--- 11. Cherry-Picking ---"
echo ""
echo "# Apply specific commit from another branch"
echo "git checkout main"
echo "git cherry-pick abc1234"
echo ""
echo "# Apply multiple commits"
echo "git cherry-pick abc1234 def5678"
echo ""
echo "# Cherry-pick without committing"
echo "git cherry-pick --no-commit abc1234"
echo ""

# =============================================================================
# 12. Rebase Merge (Two-Step)
# =============================================================================

echo "--- 12. Rebase Merge ---"
echo ""
echo "# Update feature with latest main"
echo "git checkout feature"
echo "git rebase main"
echo ""
echo "# Now merge into main (fast-forward)"
echo "git checkout main"
echo "git merge feature"
echo ""
echo "# Result: Linear history, no merge commit"
echo "git log --graph --oneline"
echo ""

# =============================================================================
# 13. Merge Strategies
# =============================================================================

echo "--- 13. Merge Strategies ---"
echo ""
echo "# Specify merge strategy"
echo "git merge feature -s recursive"
echo ""
echo "# Use ours strategy (keep current version)"
echo "git merge feature -s ours"
echo ""
echo "# Use theirs strategy (keep other version)"
echo "git merge feature -s theirs"
echo ""

# =============================================================================
# 14. Octopus Merge
# =============================================================================

echo "--- 14. Octopus Merge ---"
echo ""
echo "# Merge multiple branches at once"
echo "git checkout main"
echo "git merge feature-a feature-b feature-c"
echo ""
echo "# Creates one merge commit with all branches"
echo "git log --graph --oneline"
echo ""

# =============================================================================
# 15. Viewing Merge History
# =============================================================================

echo "--- 15. Viewing Merge History ---"
echo ""
echo "# Show merge commits only"
echo "git log --merges"
echo ""
echo "# Show first parent (main line)"
echo "git log --first-parent"
echo ""
echo "# Show merge base (common ancestor)"
echo "git merge-base main feature"
echo ""

# =============================================================================
# 16. Using Merge Tool
# =============================================================================

echo "--- 16. Using Merge Tool ---"
echo ""
echo "# Configure merge tool"
echo "git config --global merge.tool vimdiff"
echo ""
echo "# Open merge tool for conflicts"
echo "git mergetool"
echo ""
echo "# After resolving in tool"
echo "git add conflict-file.txt"
echo "git commit"
echo ""

# =============================================================================
# 17. Undoing Merge
# =============================================================================

echo "--- 17. Undoing Merge ---"
echo ""
echo "# Undo last merge (keep changes as uncommitted)"
echo "git reset --soft HEAD~1"
echo ""
echo "# Undo last merge (discard changes)"
echo "git reset --hard HEAD~1"
echo ""
echo "# Revert a merge commit"
echo "git revert -m 1 merge-commit-hash"
echo ""

# =============================================================================
# 18. Checking Merge Status
# =============================================================================

echo "--- 18. Checking Merge Status ---"
echo ""
echo "# During merge, see what's happening"
echo "git status"
echo ""
echo "# View what would be merged"
echo "git diff main...feature"
echo ""
echo "# View what will be merged into main"
echo "git diff main feature"
echo ""

# =============================================================================
# Cleanup Instructions
# =============================================================================

echo ""
echo "=== To clean up demo directory ==="
echo "cd .. && rm -rf merge-demo"
echo ""
