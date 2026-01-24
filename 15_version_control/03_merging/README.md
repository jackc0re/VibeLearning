# 🔀 Merging

**Merging** is the process of integrating changes from different branches, combining work from multiple developers or features.

---

## ✅ What is a Merge?

A merge combines the histories of two branches, creating a new commit that includes changes from both.

```
main:  A---B---D
feature:     \---C

After merge:
main:  A---B---D---E  (merge commit)
feature:     \---C---/
```

---

## ✅ Fast-Forward Merge

When the target branch hasn't diverged, Git simply moves the pointer forward:

```
main:    A---B
feature:      \---C

Fast-forward merge:
main:    A---B---C
feature:      \---/
```

```bash
# Fast-forward merge (no new commit created)
git checkout main
git merge feature
```

---

## ✅ Three-Way Merge

When both branches have new commits, Git creates a merge commit:

```
main:    A---B---D
feature:      \---C

Three-way merge:
main:    A---B---D---E  (merge commit)
feature:      \---C---/
```

```bash
# Three-way merge (creates merge commit)
git checkout main
git merge feature
```

---

## ✅ Basic Merge

```bash
# Switch to the branch that will receive changes
git checkout main

# Merge the feature branch into main
git merge feature-login

# View merge result
git log --graph --oneline
```

---

## ✅ Merge Messages

```bash
# Default merge commit message
git merge feature-login
# Git opens editor with default message:
# Merge branch 'feature-login' into main

# Custom merge message
git merge feature-login -m "Merge login feature"

# No merge commit (for fast-forward)
git merge feature-login --no-ff
```

---

## ✅ Merge Strategies

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| `recursive` | Default strategy | Most cases |
| `resolve` | Simpler, older | Simple merges |
| `octopus` | Merge multiple branches | Release merges |
| `ours` | Keep current branch's version | Ignoring other changes |
| `subtree` | Include subproject | Subproject merges |

```bash
# Specify merge strategy
git merge feature -s recursive

# Use ours strategy (keep current)
git merge feature -s ours

# Merge multiple branches at once
git merge feature-a feature-b feature-c
```

---

## ✅ Merge Conflicts

When both branches changed the same part of a file differently, Git can't decide automatically:

```python
<<<<<<< HEAD
print("Main branch version")
=======
print("Feature branch version")
>>>>>>> feature-login
```

---

## ✅ Resolving Conflicts

```bash
# 1. Run merge
git merge feature-login

# 2. Git shows conflict
CONFLICT (content): Merge conflict in file.py

# 3. View conflicts
git status

# 4. Open file and resolve manually
# Edit the file to keep desired code
# Remove <<<<<<< HEAD, =======, >>>>>>> markers

# 5. Stage resolved file
git add file.py

# 6. Complete merge
git commit
```

---

## ✅ Aborting a Merge

If you want to cancel a merge:

```bash
# Abort the merge, return to pre-merge state
git merge --abort
```

This restores your working directory to before the merge was attempted.

---

## ✅ Checking Merge Status

```bash
# See merge status
git status

# Show merge conflicts
git diff --name-only --diff-filter=U

# View conflicted file
git diff file.py
```

---

## ✅ Merge Tools

Use external tools to help resolve conflicts:

```bash
# Use configured merge tool
git mergetool

# Configure merge tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd "code --wait $MERGED"

# Available tools: vimdiff, kdiff3, opendiff, etc.
git config --global merge.tool vimdiff
```

---

## ✅ Squash Merging

Combine all branch commits into a single commit on main:

```bash
# Squash merge (no branch history on main)
git checkout main
git merge --squash feature-login
git commit -m "Add login feature"

# Result: one clean commit on main
```

**Benefits:**
- Cleaner history on main
- Feature branch commits stay on feature branch
- Easier to revert entire feature

---

## ✅ Cherry-Picking

Apply specific commits from one branch to another:

```bash
# Apply a specific commit
git cherry-pick abc1234

# Apply multiple commits
git cherry-pick abc1234 def5678

# Cherry-pick without committing
git cherry-pick --no-commit abc1234
```

**When to use:**
- Apply a hotfix to release branch
- Bring specific fix to other branch
- Revert a specific commit

---

## ✅ Rebase vs Merge

**Merge:**
- Preserves true history
- Creates merge commits
- Better for teams/public history

```bash
git checkout main
git merge feature
```

**Rebase:**
- Linear history (no merge commits)
- Rewrites feature branch commits
- Better for personal branches

```bash
git checkout feature
git rebase main
git checkout main
git merge feature  # Fast-forward now
```

---

## ✅ Rebase Merging

A two-step process for cleaner history:

```bash
# 1. Update feature branch with latest main
git checkout feature
git rebase main

# 2. Merge into main (fast-forward)
git checkout main
git merge feature
```

Result is a linear history without merge commits.

---

## ✅ Viewing Merge History

```bash
# Show merge commits
git log --merges

# Show graph of merges
git log --graph --oneline --all

# Show first parent (main line)
git log --first-parent

# Show merge base
git merge-base main feature
```

---

## ✅ Undoing Merges

```bash
# Undo last merge (keep changes)
git reset --soft HEAD~1

# Undo last merge (discard changes)
git reset --hard HEAD~1

# Revert a merge commit
git revert -m 1 abc1234
```

**Note:** `-m 1` means "keep the first parent" (the branch you merged into).

---

## ✅ Best Practices

1. **Keep branches short** - Shorter branches have fewer conflicts
2. **Update frequently** - Rebase/merge main into your branch often
3. **Small commits** - Easier to understand during conflicts
4. **Review before merge** - Use `git diff` to see what will change
5. **Test after merge** - Verify everything works
6. **Clean merge commits** - Write clear merge messages

---

## ✅ Typical Merge Workflow

```bash
# 1. Update main
git checkout main
git pull origin main

# 2. Update feature branch
git checkout feature-login
git pull origin main  # Or: git rebase main

# 3. Merge into main
git checkout main
git merge feature-login

# 4. Resolve conflicts if any
# ... edit files ...
git add .
git commit

# 5. Push merged result
git push origin main

# 6. Delete merged branch
git branch -d feature-login
```

---

## 🔍 Key Takeaways

- Merging combines branches; fast-forward for simple cases
- Three-way merge creates a merge commit when both branches have changes
- Conflicts happen when same lines change differently
- Resolve conflicts by editing files, staging, and committing
- Use `git merge --abort` to cancel a merge
- Squash merging creates cleaner history
- Rebase creates linear history vs merge's branch history

---

[Back: Module 15 README](../README.md) | [Previous: Branching](../02_branching/) | [Next: Collaboration](../04_collaboration/)
