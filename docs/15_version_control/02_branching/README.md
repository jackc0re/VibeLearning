# 🌿 Branching

**Branching** allows you to work on multiple versions of your code simultaneously, enabling parallel development and experimentation.

---

## ✅ What is a Branch?

A branch is an independent line of development. Think of it as a parallel workspace where you can make changes without affecting other work.

```
main (production) ────●──────────────●────
                     │
feature/login (branch)●──●──●─────
```

---

## ✅ Why Use Branches?

- **Isolate features** - Work on new features without breaking production
- **Bug fixes** - Fix urgent bugs without disturbing ongoing work
- **Experiments** - Try new ideas safely; discard if they don't work
- **Code review** - Prepare branches for review before merging
- **Releases** - Maintain separate release branches

---

## ✅ Default Branch

Traditionally called `master`, now commonly called `main`. This is your main production-ready branch.

---

## ✅ Listing Branches

```bash
# List all local branches
git branch

# List all branches (including remote)
git branch -a

# List branches with latest commit info
git branch -v

# Show branches in color and with merge status
git branch --color
```

---

## ✅ Creating Branches

```bash
# Create a new branch but stay on current branch
git branch feature-login

# Create and switch to the new branch
git checkout -b feature-login

# Or with git switch (newer command)
git switch -c feature-login

# Create branch from a specific commit
git branch feature-login abc1234

# Create branch from a specific tag
git branch v2.0 v2.0.0
```

---

## ✅ Switching Branches

```bash
# Switch to an existing branch
git checkout feature-login

# Or with git switch (newer command, Git 2.23+)
git switch feature-login

# Switch to the previous branch
git checkout -

# Or
git switch -
```

**Important:** Switching branches updates your working directory to match the target branch's files. Uncommitted changes may block switching.

---

## ✅ Renaming Branches

```bash
# Rename current branch
git branch -m new-name

# Rename a specific branch
git branch -m old-name new-name

# Renaming while checked out
git branch -m feature-login feature-auth
```

---

## ✅ Deleting Branches

```bash
# Delete a local branch (must be merged or safe to delete)
git branch -d feature-login

# Force delete a branch (even if not merged)
git branch -D feature-login

# Delete a remote branch
git push origin --delete feature-login

# Or push with : syntax
git push origin :feature-login
```

---

## ✅ Tracking Branches

A tracking branch connects a local branch to a remote branch:

```bash
# Create branch that tracks a specific remote branch
git checkout -b local-name origin/remote-name

# Set tracking for existing branch
git branch --set-upstream-to=origin/main main

# Show tracking info
git branch -vv
```

---

## ✅ Viewing Branch History

```bash
# Show commits in current branch only
git log main..feature-login

# Show commits in both branches
git log --oneline --graph --all

# Show differences between branches
git diff main feature-login

# Show files changed between branches
git diff --name-only main feature-login
```

---

## ✅ HEAD Reference

`HEAD` points to your current location:

```bash
# HEAD usually points to a branch
HEAD -> main -> commit

# Detached HEAD: points directly to a commit
HEAD -> commit (not a branch)
```

```bash
# See what HEAD points to
git symbolic-ref HEAD

# See what commit HEAD points to
git rev-parse HEAD
```

---

## ✅ Detached HEAD State

When `HEAD` points directly to a commit (not a branch), you're in "detached HEAD" state:

```bash
# Checkout a specific commit (detached HEAD)
git checkout abc1234

# Make changes and create a new branch
git checkout -b hotfix

# Now HEAD -> hotfix -> commit (normal state)
```

**Use cases:**
- Inspecting old commits
- Creating branches from specific points
- Testing specific states

---

## ✅ Branch Naming Conventions

| Pattern | Purpose | Example |
|---------|---------|---------|
| `feature-*` | New features | `feature-login`, `feature-dark-mode` |
| `bugfix-*` | Bug fixes | `bugfix-memory-leak` |
| `hotfix-*` | Urgent production fixes | `hotfix-critical-security` |
| `release-*` | Release preparation | `release-v2.1` |
| `fix-*` | Simple fixes | `fix-typo`, `fix-formatting` |
| `refactor-*` | Code refactoring | `refactor-auth-module` |
| `test-*` | Experimental | `test-new-algorithm` |
| `docs-*` | Documentation | `docs-api-guide` |

---

## ✅ Typical Branch Workflow

```bash
# 1. Start on main
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature-user-profile

# 3. Make changes and commits
git add .
git commit -m "Add user profile page"

# 4. Merge back to main (when done)
git checkout main
git merge feature-user-profile

# 5. Delete feature branch
git branch -d feature-user-profile
```

---

## ✅ Comparing Branches

```bash
# Show commits in branch A not in branch B
git log branchB..branchA

# Show commits unique to each branch
git log --left-right branchB...branchA

# View file changes between branches
git diff main feature-login

# View file content at a branch
git show feature-login:app.py
```

---

## ✅ Saving Work When Switching

If you have uncommitted changes:

```bash
# Stash changes temporarily
git stash

# Switch branches
git checkout main

# Work on main...

# Return to feature branch
git checkout feature-login

# Restore stashed changes
git stash pop
```

---

## ✅ Best Practices

1. **Short-lived branches** - Keep branches small and focused
2. **Descriptive names** - Use clear, purposeful branch names
3. **Clean up** - Delete merged branches regularly
4. **Update frequently** - Rebase or merge main into your branch often
5. **Atomic commits** - Make small, focused commits on branches
6. **No commits on main** - Keep main clean; do work on branches

---

## 🔍 Key Takeaways

- Branches enable parallel development without conflicts
- `git branch` creates, lists, renames, and deletes branches
- `git checkout` or `git switch` changes your current branch
- Feature branches should be short-lived and focused
- Use consistent naming conventions
- Clean up merged branches to keep your repository clean

---

[Back: Module 15 README](../README.md) | [Previous: Git Basics](../01_git_basics/) | [Next: Merging](../03_merging/)
