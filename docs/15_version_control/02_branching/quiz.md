# 🧠 Branching Quiz

---

## Question 1
What command creates a new branch?

- A) `git new branch`
- B) `git branch branch-name`
- C) `git create branch-name`
- D) `git checkout -new branch-name`

<details>
<summary>Show Answer</summary>

**B)** `git branch branch-name` creates a new branch. Use `git checkout -b` or `git switch -c` to create and switch in one command.

</details>

---

## Question 2
What does the asterisk (*) next to a branch name mean?

- A) The branch is deleted
- B) The branch is the current/active branch
- C) The branch has uncommitted changes
- D) The branch is merged

<details>
<summary>Show Answer</summary>

**B)** The asterisk (*) indicates which branch is currently checked out (active). This is your "HEAD" branch.

</details>

---

## Question 3
What happens when you switch branches?

- A) All files in your directory are deleted
- B) The working directory updates to match the target branch's files
- C) Only the .git folder changes
- D) Nothing changes until you commit

<details>
<summary>Show Answer</summary>

**B)** Switching branches updates your working directory to reflect the state of the files on the target branch. It replaces the files with the versions from that branch.

</details>

---

## Question 4
What is "detached HEAD" state?

- A) HEAD has been deleted
- B) HEAD points directly to a commit instead of a branch
- C) HEAD is merged into main
- D) HEAD is in a remote repository

<details>
<summary>Show Answer</summary>

**B)** Detached HEAD means HEAD is pointing directly to a specific commit rather than a branch. This happens when you checkout a specific commit hash or tag.

</details>

---

## Question 5
What command deletes a branch?

- A) `git delete branch-name`
- B) `git branch -d branch-name`
- C) `git rm branch-name`
- D) `git branch -remove branch-name`

<details>
<summary>Show Answer</summary>

**B)** `git branch -d branch-name` deletes a branch. Use `-D` (capital D) to force delete even if the branch hasn't been merged.

</details>

---

## Question 6
What is a good naming convention for a new feature branch?

- A) `fix-bug`
- B) `feature-dark-mode`
- C) `branch-1`
- D) `new-thing`

<details>
<summary>Show Answer</summary>

**B)** `feature-dark-mode` follows the convention of prefixing with `feature-` followed by a descriptive name. Other good examples: `feature-login`, `feature-api-integration`.

</details>

---

## Question 7
What does `git diff main feature` show?

- A) Files that differ between main and feature branches
- B) Only new files in feature
- C) The commit history
- D) Merged files only

<details>
<summary>Show Answer</summary>

**A)** `git diff main feature` shows the differences in file contents between the main branch and the feature branch.

</details>

---

## Question 8
How do you create and switch to a branch in one command?

- A) `git new -b feature`
- B) `git checkout -b feature`
- C) `git branch -switch feature`
- D) `git create feature`

<details>
<summary>Show Answer</summary>

**B)** `git checkout -b feature` creates a new branch and immediately switches to it. Alternatively, use `git switch -c feature` (Git 2.23+).

</details>

---

## Question 9
What does `git branch -v` show?

- A) Version of Git
- B) Branches with commit message and hash
- C) Very long branch list
- D) Visual graph of branches

<details>
<summary>Show Answer</summary>

**B)** `git branch -v` shows branches along with the latest commit hash and message for each branch.

</details>

---

## Question 10
What is the default branch name in modern Git?

- A) `master`
- B) `main`
- C) `primary`
- D) `default`

<details>
<summary>Show Answer</summary>

**B)** The default branch is now commonly called `main`. Historically it was called `master`, but the community has shifted to `main` for inclusivity.

</details>

---

## Question 11
What does `git checkout -` do?

- A) Deletes a branch
- B) Switches to the previous branch
- C) Shows branch differences
- D) Creates a new branch

<details>
<summary>Show Answer</summary>

**B)** `git checkout -` switches you back to the previous branch you were on, similar to how `cd -` works for directories.

</details>

---

## Question 12
What is a short-lived branch?

- A) A branch that was quickly deleted
- B) A branch created for a specific task and merged quickly
- C) A branch with few commits
- D) A branch on a different computer

<details>
<summary>Show Answer</summary>

**B)** Short-lived branches are feature branches that exist only for the duration of a specific task (a few hours to days) before being merged and deleted.

</details>

---

## Question 13
How do you rename the current branch?

- A) `git rename new-name`
- B) `git branch -m new-name`
- C) `git mv current new-name`
- D) `git branch --rename new-name`

<details>
<summary>Show Answer</summary>

**B)** `git branch -m new-name` renames the current branch. You can also rename another branch: `git branch -m old-name new-name`.

</details>

---

## Question 14
What does `git log main..feature` show?

- A) All commits in main
- B) All commits in feature
- C) Commits in feature that are not in main
- D) Commits common to both

<details>
<summary>Show Answer</summary>

**C)** `git log main..feature` shows commits that exist in the feature branch but not in the main branch (the "tip" of feature's work).

</details>

---

## Question 15
Why create a branch from a tag?

- A) To delete the tag
- B) To make bug fixes for a specific release version
- C) To rename the tag
- D) To create a new tag

<details>
<summary>Show Answer</summary>

**B)** Creating a branch from a tag allows you to make bug fixes for a specific release version while continuing development on main. This is common for "maintenance" or "hotfix" branches.

</details>

---

[Back to Branching README](README.md) | [Back to Exercises](exercises.md)
