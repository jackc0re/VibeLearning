# 🧠 Merging Quiz

---

## Question 1
What is a fast-forward merge?

- A) A very fast merge operation
- B) Moving the branch pointer forward when no divergence exists
- C) Merging multiple branches at once
- D) A merge that automatically resolves all conflicts

<details>
<summary>Show Answer</summary>

**B)** A fast-forward merge happens when the target branch hasn't diverged, so Git simply moves the branch pointer forward. No merge commit is created.

</details>

---

## Question 2
What creates a merge commit?

- A) Fast-forward merge
- B) Three-way merge when both branches have commits
- C) Any merge operation
- D) Only when conflicts occur

<details>
<summary>Show Answer</summary>

**B)** A three-way merge creates a merge commit when both branches have new commits that need to be combined. It merges the histories into a new commit.

</details>

---

## Question 3
What does `git merge --abort` do?

- A) Deletes the merged branch
- B) Cancels the merge and restores pre-merge state
- C) Continues the merge after fixing conflicts
- D) Creates a new branch

<details>
<summary>Show Answer</summary>

**B)** `git merge --abort` cancels the current merge operation and restores your repository to the state it was in before the merge was attempted.

</details>

---

## Question 4
When does a merge conflict occur?

- A) When branches have different file names
- B) When both branches modified the same part of a file differently
- C) When one branch is ahead of the other
- D) When merging with `--squash`

<details>
<summary>Show Answer</summary>

**B)** Merge conflicts occur when both branches have changed the same lines in a file and Git cannot automatically determine which changes to keep.

</details>

---

## Question 5
What do the markers `<<<<<<< HEAD` and `>>>>>>> feature` mean?

- A) Git comments
- B) Markers showing where conflicts are
- C) Branch names
- D) File separators

<details>
<summary>Show Answer</summary>

**B)** These are conflict markers showing where the conflicting changes begin and end. `<<<<<<< HEAD` starts the current branch's changes, `=======` separates them, and `>>>>>>> feature` ends with the other branch's changes.

</details>

---

## Question 6
What is a squash merge?

- A) Deleting commits
- B) Combining all branch commits into one on the target branch
- C) Resolving conflicts automatically
- D) Merging multiple branches at once

<details>
<summary>Show Answer</summary>

**B)** A squash merge combines all commits from the source branch into a single commit on the target branch, keeping the history clean on the main branch.

</details>

---

## Question 7
What does `git cherry-pick` do?

- A) Picks the best merge strategy
- B) Applies specific commits from one branch to another
- C) Deletes specific commits
- D) Shows commit history

<details>
<summary>Show Answer</summary>

**B)** `git cherry-pick` applies a specific commit (or commits) from one branch onto your current branch, useful for bringing specific fixes or features.

</details>

---

## Question 8
What is the difference between merge and rebase?

- A) Merge creates commits, rebase doesn't
- B) Rebase creates linear history, merge preserves branch history
- C) Merge is for files, rebase is for directories
- D) They are the same thing

<details>
<summary>Show Answer</summary>

**B)** Merge preserves the true history with merge commits showing branch points. Rebase rewrites the feature branch's commits on top of the target, creating a linear history.

</details>

---

## Question 9
What does `git merge --no-ff` do?

- A) Aborts the merge
- B) Always creates a merge commit, even for fast-forward cases
- C) Merges without conflicts
- D) Merges only certain files

<details>
<summary>Show Answer</summary>

**B)** `--no-ff` forces Git to create a merge commit even when a fast-forward is possible, preserving the feature branch history.

</details>

---

## Question 10
What command shows all merge commits?

- A) `git log --merges`
- B) `git log --all-merges`
- C) `git show merges`
- D) `git log -m`

<details>
<summary>Show Answer</summary>

**A)** `git log --merges` displays only merge commits in your history, filtering out regular commits.

</details>

---

## Question 11
What is an octopus merge?

- A) Merging with 8 branches
- B) Merging multiple branches at once
- C) A conflict resolution tool
- D) A rebase strategy

<details>
<summary>Show Answer</summary>

**B)** An octopus merge is when you merge multiple branches into your current branch in a single command: `git merge branch1 branch2 branch3`.

</details>

---

## Question 12
What does `git merge -s ours` do?

- A) Uses the default merge strategy
- B) Keeps your current branch's version of all conflicts
- C) Uses the other branch's version
- D) Creates a new merge strategy

<details>
<summary>Show Answer</summary>

**B)** `-s ours` tells Git to always keep the current branch's version when conflicts occur, essentially ignoring changes from the branch being merged.

</details>

---

## Question 13
What is a merge base?

- A) The first commit in a repository
- B) The common ancestor commit of two branches
- C) The merge commit
- D) The main branch

<details>
<summary>Show Answer</summary>

**B)** The merge base is the most recent common ancestor commit between two branches. It's the point where the branches diverged.

</details>

---

## Question 14
What does `git mergetool` do?

- A) Shows merge conflicts
- B) Opens an external tool to help resolve conflicts
- C) Automatically resolves conflicts
- D) Shows the merge graph

<details>
<summary>Show Answer</summary>

**B)** `git mergetool` launches an external visual merge tool (like vimdiff, kdiff3, or VS Code) to help you see and resolve conflicts more easily.

</details>

---

## Question 15
What does `git revert -m 1` mean?

- A) Revert the first commit
- B) Keep the first parent when reverting a merge
- C) Merge with 1 strategy
- D) Revert with 1 commit

<details>
<summary>Show Answer</summary>

**B)** When reverting a merge commit, `-m 1` means "keep the first parent," which is usually the branch you merged into. It tells Git which side of the merge to keep.

</details>

---

[Back to Merging README](README.md) | [Back to Exercises](exercises.md)
