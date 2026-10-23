# Git Cheatsheet

Quick reference for everyday Git: status checks, branching, merging, undo recipes, stash, and `.gitignore`.

---

## Everyday Commands

| Command | What it does |
|---------|--------------|
| `git status` | Show changed/staged files and current branch |
| `git add file.txt` | Stage one file |
| `git add .` | Stage everything in the current folder |
| `git commit -m "Add login form"` | Save staged changes as a commit |
| `git log --oneline` | Compact history (one line per commit) |
| `git log -p file.txt` | History of one file, with the diffs |
| `git diff` | Changes not yet staged |
| `git diff --staged` | Changes staged but not yet committed |
| `git clone <url>` | Copy a remote repo to your machine |
| `git pull` | Fetch and merge remote changes |
| `git push` | Upload your commits to the remote |

```bash
# The basic loop you'll repeat all day
git status              # What changed?
git add .               # Stage it
git commit -m "Describe the change"   # Snapshot it
git push                # Share it
```

> **Tip:** run `git status` before and after everything. It always tells you
> exactly where you are and what Git thinks is going on.

---

## Branch & Merge Workflow

```bash
git branch feature-login       # Create a branch
git switch feature-login       # Move to it (older syntax: git checkout)
git switch -c feature-signup   # Create AND switch in one step
git branch                     # List branches (* marks the current one)

# ... make commits on the branch ...

git switch main                # Go back to main
git merge feature-login        # Bring the branch's work into main
git branch -d feature-login    # Delete the merged branch
```

### Resolving a Merge Conflict in 3 Steps

When both branches edit the same lines, Git stops and marks the file:

```
<<<<<<< HEAD
This is your version
=======
This is their version
>>>>>>> feature-login
```

1. **Edit the file** — keep the code you want (often a mix of both) and delete
   the `<<<<<<<`, `=======`, `>>>>>>>` markers.
2. **Stage it:** `git add file.txt` — this tells Git "conflict resolved".
3. **Finish:** `git commit` — Git writes the merge commit for you.

(Changed your mind mid-conflict? `git merge --abort` puts everything back.)

---

## Undo Recipes

| Situation | Command | Result |
|-----------|---------|--------|
| Messed up a file, **not staged** | `git restore file.txt` | Discard the edits |
| Staged something by accident | `git restore --staged file.txt` | Unstage (edits kept) |
| Committed too early | `git reset --soft HEAD~1` | Undo commit, changes **staged** |
| Committed too early | `git reset --mixed HEAD~1` | Undo commit, changes **unstaged** |
| "Nuke" the last commit | `git reset --hard HEAD~1` | Undo commit **and delete the changes** ⚠️ |
| Commit is already pushed/shared | `git revert <hash>` | New commit that undoes it — safe for shared history |

### `reset --soft` vs `--mixed` vs `--hard`

| Mode | Commit removed? | Changes in working tree? | Changes staged? |
|------|-----------------|--------------------------|-----------------|
| `--soft` | ✅ Yes | ✅ Kept | ✅ Yes |
| `--mixed` (default) | ✅ Yes | ✅ Kept | ❌ No |
| `--hard` | ✅ Yes | ❌ Deleted | ❌ No |

### The Golden Rule of Undo

- **Local only?** `reset` is fine — it rewrites history nobody else has.
- **Already pushed?** Use `revert` — it never rewrites history, so your
  teammates' copies stay valid.

---

## Stash: Park Your Work

Need to switch branches but your half-finished code won't compile?

```bash
git stash              # Park the changes (working tree goes clean)
git stash pop          # Come back and re-apply them
git stash list         # See all stashes
git stash apply        # Re-apply but keep a copy in the stash
```

> Stashes are a scratchpad, not storage. Pop them soon or lose track of them.

---

## `.gitignore` Essentials

A `.gitignore` file at the repo root lists patterns Git should never track:

```gitignore
# Comments start with a hash
__pycache__/
*.pyc              # * matches anything
.env               # Secrets never belong in Git
venv/
build/             # Trailing / = a directory
debug.log
!keep.log          # ! = exception (track this one anyway)
```

- Each line is a pattern; blank lines are ignored.
- `*.log` ignores all logs; `!important.log` un-ignores one specific file.
- **`.gitignore` only affects untracked files.** If a file is already
  committed, add it to `.gitignore` *and* run
  `git rm --cached file.txt` to stop tracking it.

---

## Quick Reference

| I want to... | Command |
|--------------|---------|
| See what changed | `git status` / `git diff` |
| Save my work | `git add . && git commit -m "msg"` |
| Try an idea safely | `git switch -c new-idea` |
| Combine branches | `git merge branch-name` |
| Unstage a file | `git restore --staged file.txt` |
| Undo local commit | `git reset --soft HEAD~1` |
| Undo a pushed commit | `git revert <hash>` |
| Park half-done work | `git stash` |
| Stop tracking a file | `git rm --cached file.txt` |

---

**Learn more:** [Version Control module](../../15_version_control/README.md) ·
[Git basics](../../15_version_control/01_git_basics/README.md) ·
[Branching](../../15_version_control/02_branching/README.md) ·
[Merging](../../15_version_control/03_merging/README.md) ·
[Collaboration](../../15_version_control/04_collaboration/README.md)

**Back to [Resources](../README.md)**
