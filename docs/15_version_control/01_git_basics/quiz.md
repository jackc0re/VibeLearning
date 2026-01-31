# 🧠 Git Basics Quiz

---

## Question 1
What command initializes a new Git repository?

- A) `git start`
- B) `git init`
- C) `git create`
- D) `git new`

<details>
<summary>Show Answer</summary>

**B)** `git init` creates a new Git repository in the current directory by setting up a `.git` folder.

</details>

---

## Question 2
What is the "staging area" in Git?

- A) A folder where files are stored
- B) An area where you prepare files before committing
- C) The remote repository
- D) A backup of your code

<details>
<summary>Show Answer</summary>

**B)** The staging area (or index) is where you place files using `git add` to prepare them for the next commit. It gives you control over what goes into each commit.

</details>

---

## Question 3
What does `git status` show?

- A) Your commit history
- B) Which files are tracked, modified, staged, or untracked
- C) Differences between commits
- D) Your Git configuration

<details>
<summary>Show Answer</summary>

**B)** `git status` shows the current state of your working directory and staging area, indicating which files are new, modified, staged, or untracked.

</details>

---

## Question 4
What does `git add .` do?

- A) Adds all files to the repository
- B) Stages all files in the current directory
- C) Commits all changes
- D) Creates a new branch

<details>
<summary>Show Answer</summary>

**B)** `git add .` stages all files (new, modified, deleted) in the current directory and subdirectories, preparing them for the next commit.

</details>

---

## Question 5
What is the purpose of a commit message?

- A) To make the commit look professional
- B) To explain what changes were made and why
- C) To encrypt the commit
- D) It's not required

<details>
<summary>Show Answer</summary>

**B)** Commit messages explain what changes were made and why. Good messages help you and others understand the history of the project when reviewing commits.

</details>

---

## Question 6
What does `git log` display?

- A) Current working directory files
- B) Commit history with author, date, and message
- C) Differences between files
- D) Git configuration settings

<details>
<summary>Show Answer</summary>

**B)** `git log` displays the commit history, showing each commit's hash, author, date, and message.

</details>

---

## Question 7
What is the difference between `git diff` and `git diff --staged`?

- A) They show the same thing
- B) `git diff` shows working directory changes, `--staged` shows staged changes
- C) `git diff` shows staged changes, `--staged` shows working directory
- D) `git diff` only works on .txt files

<details>
<summary>Show Answer</summary>

**B)** `git diff` shows differences between your working directory and the staging area. `git diff --staged` shows differences between the staging area and the last commit.

</details>

---

## Question 8
What is `.gitignore` used for?

- A) To ignore errors in Git
- B) To specify files that Git should not track
- C) To hide commits from history
- D) To disable Git commands

<details>
<summary>Show Answer</summary>

**B)** `.gitignore` contains patterns for files and directories that Git should ignore, such as build artifacts, dependencies, and sensitive files.

</details>

---

## Question 9
What does `git mv old.txt new.txt` do?

- A) Copies the file
- B) Moves the file and tells Git about the rename
- C) Deletes the old file
- D) Creates a symbolic link

<details>
<summary>Show Answer</summary>

**B)** `git mv` moves/renames a file and stages the change, allowing Git to track it as a rename rather than a delete followed by an add.

</details>

---

## Question 10
What does `git restore --staged file.txt` do?

- A) Deletes the file
- B) Unstages the file while keeping changes
- C) Discards changes in the file
- D) Restores the file from trash

<details>
<summary>Show Answer</summary>

**B)** `git restore --staged` removes a file from the staging area (unstages it) while keeping the changes in your working directory.

</details>

---

## Question 11
Which command shows the last 3 commits?

- A) `git log -3`
- B) `git log --last 3`
- C) `git show 3`
- D) `git log --head 3`

<details>
<summary>Show Answer</summary>

**A)** `git log -3` displays only the last 3 commits in the history.

</details>

---

## Question 12
What does `git commit --amend` do?

- A) Creates a new commit
- B) Modifies the most recent commit
- C) Deletes the last commit
- D) Merges two commits

<details>
<summary>Show Answer</summary>

**B)** `git commit --amend` allows you to modify the most recent commit, either to add forgotten staged changes or to edit the commit message.

</details>

---

## Question 13
What is the difference between a tracked and untracked file?

- A) Tracked files are on a remote server
- B) Tracked files are known to Git, untracked are not
- C) Tracked files are larger
- D) Untracked files cannot be committed

<details>
<summary>Show Answer</summary>

**B)** Tracked files are files that Git knows about (either in the staging area or in a previous commit). Untracked files are new files that Git hasn't been told to track yet.

</details>

---

## Question 14
What does `HEAD` refer to in Git?

- A) The beginning of your repository
- B) A reference to your current commit/branch
- C) The main branch
- D) The remote repository

<details>
<summary>Show Answer</summary>

**B)** `HEAD` is a reference pointing to the current branch and commit you have checked out. It's essentially a "you are here" pointer.

</details>

---

## Question 15
Which command creates an empty commit?

- A) `git commit --empty`
- B) `git commit -m ""`
- C) `git commit --allow-empty -m "message"`
- D) `git commit --none`

<details>
<summary>Show Answer</summary>

**C)** `git commit --allow-empty -m "message"` creates a commit with no changes, which can be useful for triggering CI pipelines or documenting decisions.

</details>

---

[Back to Git Basics README](README.md) | [Back to Exercises](exercises.md)
