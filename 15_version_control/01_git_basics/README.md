# 🎯 Git Basics

**Git basics** covers the fundamental commands for tracking changes in your project.

---

## ✅ Initializing a Repository

```bash
# Create a new repository in current directory
git init

# Creates a .git directory that tracks everything
```

This creates:
- `.git/` folder (hidden directory with all Git data)
- A way to track all files in the current folder

---

## ✅ Git's Three States

Git has three main states:

```
Working Directory  →  Staging Area  →  Repository
    (modified)          (staged)         (committed)
```

1. **Working Directory** - Your actual files
2. **Staging Area (Index)** - Files prepared for commit
3. **Repository** - Committed snapshots (history)

---

## ✅ Checking Status

```bash
# See which files are changed, staged, or untracked
git status
```

Output shows:
- **Untracked files** - New files Git doesn't know about
- **Modified files** - Files changed but not staged
- **Staged changes** - Files ready to be committed

---

## ✅ Staging Files

```bash
# Stage a specific file
git add filename.py

# Stage all files in current directory
git add .

# Stage all tracked files (skip untracked)
git add -u

# Interactive staging (select parts of files)
git add -i

# Patch mode (stage specific lines)
git add -p filename.py
```

---

## ✅ Committing Changes

```bash
# Commit staged changes with a message
git commit -m "Add user authentication feature"

# Commit all modified tracked files (skip git add)
git commit -am "Fix bug in login logic"

# Edit the commit message before committing
git commit

# Empty commit (useful for triggering CI)
git commit --allow-empty -m "Trigger build"
```

**Good commit messages:**
- Start with a verb: `Add`, `Fix`, `Update`, `Refactor`
- Keep the first line under 50 characters
- Use imperative mood: "Add feature" not "Added feature"
- Add details after a blank line if needed

---

## ✅ Viewing History

```bash
# Show commit history
git log

# Show compact history (one line per commit)
git log --oneline

# Show history with a graph
git log --graph --oneline

# Show last N commits
git log -3

# Show history for a specific file
git log filename.py

# Show changes in each commit
git log -p

# Show who changed what and when
git log --stat
```

---

## ✅ Viewing Differences

```bash
# Show differences between working directory and staging
git diff

# Show differences between staging and last commit
git diff --staged

# Show differences between working directory and last commit
git diff HEAD

# Show differences for a specific file
git diff filename.py

# Show differences between two commits
git diff commit1 commit2
```

---

## ✅ Ignoring Files

Create `.gitignore` to exclude files from tracking:

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Environment
.env
*.env

# Build
dist/
build/
*.egg-info/
```

---

## ✅ Removing and Moving Files

```bash
# Stage removal of a file (keeps working copy)
git rm filename.py

# Remove file from Git but keep locally
git rm --cached filename.py

# Move/rename a file (Git tracks the rename)
git mv old.py new.py

# These are equivalent to:
rm filename.py
git add filename.py
```

---

## ✅ Undoing Changes

```bash
# Unstage a file (keep changes)
git restore --staged filename.py

# Discard changes in working directory
git restore filename.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert a commit (create new commit that undoes it)
git revert commit-hash
```

---

## ✅ Best Practices

1. **Commit often** - Small, focused commits are easier to understand
2. **Write clear messages** - Future you (and others) will thank you
3. **Stage selectively** - Only commit related changes together
4. **Ignore artifacts** - Use `.gitignore` for generated files
5. **Review before committing** - `git diff` and `git status`

---

## 🔍 Key Takeaways

- Git tracks changes in three states: working, staging, repository
- `git add` moves changes to staging area
- `git commit` saves staged changes as a snapshot
- `git status` shows the current state
- `git log` shows commit history
- Use `.gitignore` to exclude files

---

[Back: Module 15 README](../README.md) | [Next: Branching](../02_branching/)
