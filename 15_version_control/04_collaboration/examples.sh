#!/bin/bash
# Collaboration - Examples
#
# This script demonstrates Git collaboration commands.
# Requires an actual GitHub/GitLab account to fully test.
#
# Setup: Create a test repository on GitHub first, then:
#   git clone https://github.com/your-username/test-repo.git
#   cd test-repo

echo "=== Collaboration Examples ==="
echo "These commands assume you have a GitHub/GitLab account."
echo "Replace 'your-username' and 'repo-name' with actual values."
echo ""

# =============================================================================
# 1. Cloning a Repository
# =============================================================================

echo "--- 1. Cloning a Repository ---"
echo ""
echo "# Clone a repository"
echo "git clone https://github.com/your-username/repo-name.git"
echo ""
echo "# Clone into a specific directory"
echo "git clone https://github.com/your-username/repo-name.git my-dir"
echo ""
echo "# Clone a specific branch"
echo "git clone -b develop https://github.com/your-username/repo-name.git"
echo ""
echo "# Clone using SSH"
echo "git clone git@github.com:your-username/repo-name.git"
echo ""

# =============================================================================
# 2. Viewing Remotes
# =============================================================================

echo "--- 2. Viewing Remotes ---"
echo ""
echo "# Show all remotes"
echo "git remote"
echo ""
echo "# Show remotes with URLs"
echo "git remote -v"
echo ""
echo "# Show details for origin"
echo "git remote show origin"
echo ""

# =============================================================================
# 3. Adding Remotes
# =============================================================================

echo "--- 3. Adding Remotes ---"
echo ""
echo "# Add a remote (when not cloned)"
echo "git remote add origin https://github.com/your-username/repo-name.git"
echo ""
echo "# Add upstream (for forked repos)"
echo "git remote add upstream https://github.com/original-owner/repo-name.git"
echo ""

# =============================================================================
# 4. Fetching Changes
# =============================================================================

echo "--- 4. Fetching Changes ---"
echo ""
echo "# Fetch all changes from origin"
echo "git fetch origin"
echo ""
echo "# Fetch a specific branch"
echo "git fetch origin main"
echo ""
echo "# Fetch from all remotes"
echo "git fetch --all"
echo ""
echo "# Fetch and prune deleted remote branches"
echo "git fetch --prune"
echo ""

# =============================================================================
# 5. Pulling Changes
# =============================================================================

echo "--- 5. Pulling Changes ---"
echo ""
echo "# Pull from default remote/branch"
echo "git pull"
echo ""
echo "# Pull from specific remote/branch"
echo "git pull origin main"
echo ""
echo "# Pull with rebase (linear history)"
echo "git pull --rebase"
echo ""
echo "# Pull without auto-commit"
echo "git pull --no-commit"
echo ""

# =============================================================================
# 6. Pushing Changes
# =============================================================================

echo "--- 6. Pushing Changes ---"
echo ""
echo "# Push current branch"
echo "git push"
echo ""
echo "# Push to specific remote/branch"
echo "git push origin main"
echo ""
echo "# Push and set upstream (first time)"
echo "git push -u origin feature-login"
echo ""
echo "# Push all branches"
echo "git push --all"
echo ""
echo "# Push all tags"
echo "git push --tags"
echo ""

# =============================================================================
# 7. Force Pushing
# =============================================================================

echo "--- 7. Force Pushing ---"
echo ""
echo "# Force push (overwrites remote!)"
echo "git push --force"
echo ""
echo "# Safer force push (checks if remote changed)"
echo "git push --force-with-lease"
echo ""

# =============================================================================
# 8. Working with Remote Branches
# =============================================================================

echo "--- 8. Working with Remote Branches ---"
echo ""
echo "# List remote branches"
echo "git branch -r"
echo ""
echo "# List all branches (local and remote)"
echo "git branch -a"
echo ""
echo "# Checkout a remote branch"
echo "git checkout feature-login"
echo "# This creates local branch tracking origin/feature-login"
echo ""

# =============================================================================
# 9. Setting Upstream
# =============================================================================

echo "--- 9. Setting Upstream ---"
echo ""
echo "# Set upstream for current branch"
echo "git branch --set-upstream-to=origin/main main"
echo ""
echo "# Or use -u flag when pushing"
echo "git push -u origin feature-xyz"
echo ""
echo "# Show tracking information"
echo "git branch -vv"
echo ""

# =============================================================================
# 10. Forking Workflow
# =============================================================================

echo "--- 10. Forking Workflow ---"
echo ""
echo "# 1. Fork repository on GitHub (web UI)"
echo ""
echo "# 2. Clone your fork"
echo "git clone https://github.com/YOUR-USERNAME/repo.git"
echo "cd repo"
echo ""
echo "# 3. Add upstream (original repository)"
echo "git remote add upstream https://github.com/ORIGINAL-OWNER/repo.git"
echo ""
echo "# 4. Create feature branch"
echo "git checkout -b feature-new-stuff"
echo ""
echo "# 5. Make changes and commit"
echo "git add ."
echo "git commit -m 'Add new feature'"
echo ""
echo "# 6. Push to your fork"
echo "git push -u origin feature-new-stuff"
echo ""
echo "# 7. Create Pull Request on GitHub (web UI)"
echo ""

# =============================================================================
# 11. Syncing Fork with Upstream
# =============================================================================

echo "--- 11. Syncing Fork with Upstream ---"
echo ""
echo "# Fetch latest from upstream"
echo "git fetch upstream"
echo ""
echo "# Update local main branch"
echo "git checkout main"
echo "git merge upstream/main"
echo ""
echo "# Update your fork"
echo "git push origin main"
echo ""
echo "# Update feature branch"
echo "git checkout feature-xyz"
echo "git rebase upstream/main"
echo "git push origin feature-xyz"
echo ""

# =============================================================================
# 12. Team Collaboration Workflow
# =============================================================================

echo "--- 12. Team Collaboration Workflow ---"
echo ""
echo "# Start from latest main"
echo "git checkout main"
echo "git pull origin main"
echo ""
echo "# Create feature branch"
echo "git checkout -b feature-xyz"
echo ""
echo "# Work and commit"
echo "# ... make changes ..."
echo "git add ."
echo "git commit -m 'Add feature'"
echo ""
echo "# Keep branch updated"
echo "git fetch origin"
echo "git rebase origin/main"
echo ""
echo "# Push and create PR"
echo "git push -u origin feature-xyz"
echo ""

# =============================================================================
# 13. Resolving PR Conflicts
# =============================================================================

echo "--- 13. Resolving PR Conflicts ---"
echo ""
echo "# Fetch latest main"
echo "git fetch origin"
echo ""
echo "# Rebase branch onto main"
echo "git checkout feature-xyz"
echo "git rebase origin/main"
echo ""
echo "# Resolve conflicts"
echo "# ... edit files ..."
echo "git add ."
echo "git rebase --continue"
echo ""
echo "# Force push (history rewritten)"
echo "git push --force-with-lease origin feature-xyz"
echo ""

# =============================================================================
# 14. Changing Remote URL
# =============================================================================

echo "--- 14. Changing Remote URL ---"
echo ""
echo "# View current remote URL"
echo "git remote get-url origin"
echo ""
echo "# Change from HTTPS to SSH"
echo "git remote set-url origin git@github.com:username/repo.git"
echo ""
echo "# Change from SSH to HTTPS"
echo "git remote set-url origin https://github.com/username/repo.git"
echo ""

# =============================================================================
# 15. Deleting Remote Branches
# =============================================================================

echo "--- 15. Deleting Remote Branches ---"
echo ""
echo "# Delete remote branch"
echo "git push origin --delete feature-login"
echo ""
echo "# Or use colon syntax"
echo "git push origin :feature-login"
echo ""
echo "# Delete remote tag"
echo "git push origin --delete v1.0"
echo ""

# =============================================================================
# 16. Managing Remotes
# =============================================================================

echo "--- 16. Managing Remotes ---"
echo ""
echo "# Rename a remote"
echo "git remote rename origin github"
echo ""
echo "# Remove a remote"
echo "git remote remove origin"
echo ""
echo "# Prune remote references locally"
echo "git remote prune origin"
echo ""

# =============================================================================
# 17. Viewing Differences with Remote
# =============================================================================

echo "--- 17. Viewing Differences with Remote ---"
echo ""
echo "# See unpushed commits"
echo "git log origin/main..main"
echo ""
echo "# See commits on remote not in local"
echo "git log main..origin/main"
echo ""
echo "# See file differences"
echo "git diff origin/main"
echo ""

# =============================================================================
# 18. Git LFS (Large File Storage)
# =============================================================================

echo "--- 18. Git LFS ---"
echo ""
echo "# Install Git LFS (one time)"
echo "git lfs install"
echo ""
echo "# Track large files by extension"
echo "git lfs track '*.psd'"
echo "git lfs track '*.mp4'"
echo "git lfs track '*.zip'"
echo ""
echo "# Track specific files"
echo "git lfs track 'data/*.csv'"
echo ""
echo "# View tracked patterns"
echo "git lfs track"
echo ""
echo "# Commit .gitattributes"
echo "git add .gitattributes"
echo "git commit -m 'Configure Git LFS'"
echo ""

# =============================================================================
# 19. SSH Key Setup (One Time)
# =============================================================================

echo "--- 19. SSH Key Setup ---"
echo ""
echo "# Generate new SSH key"
echo "ssh-keygen -t ed25519 -C 'your-email@example.com'"
echo ""
echo "# Add SSH key to ssh-agent"
echo "eval \$(ssh-agent -s)"
echo "ssh-add ~/.ssh/id_ed25519"
echo ""
echo "# Copy SSH public key"
echo "cat ~/.ssh/id_ed25519.pub"
echo ""
echo "# Add key to GitHub: Settings > SSH and GPG keys > New SSH key"
echo ""

# =============================================================================
# 20. Personal Access Token (for HTTPS)
# =============================================================================

echo "--- 20. Personal Access Token ---"
echo ""
echo "# Create PAT on GitHub:"
echo "# Settings > Developer Settings > Personal access tokens"
echo "# Generate new token with 'repo' scope"
echo ""
echo "# Use token as password when pushing"
echo "git push"
echo "# Username: your-username"
echo "# Password: ghp_xxxxxxxxxxxxxxxxxxxxxxxxx"
echo ""

# =============================================================================
# Notes
# =============================================================================

echo ""
echo "=== Notes ==="
echo "- These examples assume an existing remote repository"
echo "- Replace URLs and branch names with your actual values"
echo "- Some commands require a GitHub/GitLab account"
echo "- Test commands in a test repository first"
echo ""
echo "=== Cleanup ==="
echo "cd .. && rm -rf test-repo"
echo ""
