# 📝 Git Basics Exercises

Practice the fundamental Git commands to build muscle memory.

---

## Exercise 1: First Repository

**Goal:** Create your first Git repository and make a commit.

1. Create a new directory called `my-first-repo`
2. Initialize it as a Git repository
3. Create a file named `README.md` with content about your project
4. Stage the file
5. Commit it with a descriptive message
6. Verify the commit was created

<details>
<summary>Show Solution</summary>

```bash
mkdir my-first-repo
cd my-first-repo
git init
echo "# My First Project" > README.md
git add README.md
git commit -m "Initial commit: Add README"
git log --oneline
```

</details>

---

## Exercise 2: Multiple Commits

**Goal:** Make several commits with different changes.

1. Create a Python file `calculator.py` with a simple function
2. Commit it
3. Add another function to the file
4. Stage and commit the change
5. Modify an existing function
6. Commit the modification
7. View the commit history

<details>
<summary>Show Solution</summary>

```bash
# Create initial file
cat > calculator.py << 'EOF'
def add(a, b):
    return a + b
EOF

git add calculator.py
git commit -m "Add addition function"

# Add second function
cat >> calculator.py << 'EOF'

def subtract(a, b):
    return a - b
EOF

git add calculator.py
git commit -m "Add subtraction function"

# Modify first function
sed -i 's/return a + b/return a + b  # Basic addition/' calculator.py

git add calculator.py
git commit -m "Add comment to add function"

git log --oneline
```

</details>

---

## Exercise 3: Understanding Git States

**Goal:** Understand the three Git states (working, staging, repository).

1. Create a file `data.txt` with some content
2. Check status (should be untracked)
3. Stage the file
4. Check status (should be staged)
5. Modify the file (add more content)
6. Check status (show both staged and modified)
7. View the difference in the staging area
8. View the difference in the working directory
9. Commit the staged changes
10. Check status again

<details>
<summary>Show Solution</summary>

```bash
echo "line 1" > data.txt
git status

git add data.txt
git status

echo "line 2" >> data.txt
git status

git diff --staged
git diff

git commit -m "Add data.txt with first line"
git status
```

</details>

---

## Exercise 4: Selective Staging

**Goal:** Stage only specific changes, not everything.

1. Create a file `notes.txt` with multiple paragraphs
2. Modify the file in two different places
3. Stage only one of the modifications using `git add -p`
4. Commit that change
5. Stage and commit the remaining change
6. Verify both commits are in history

<details>
<summary>Show Solution</summary>

```bash
cat > notes.txt << 'EOF'
Important note 1
Another note
Final note
EOF

git add notes.txt
git commit -m "Initial notes"

# Modify in two places
sed -i 's/note 1/note 1 (updated)/' notes.txt
sed -i 's/Final note/Final note (changed)/' notes.txt

# Stage only first change
git add -p notes.txt
# Type 'y' for first hunk, 'n' for second hunk

git commit -m "Update first note"

# Stage and commit remaining change
git add notes.txt
git commit -m "Update final note"

git log --oneline
```

</details>

---

## Exercise 5: Creating .gitignore

**Goal:** Set up proper `.gitignore` for a Python project.

1. Create a `.gitignore` file with patterns for:
   - Python cache files (`*.pyc`, `__pycache__/`)
   - Virtual environments (`venv/`, `.venv/`)
   - IDE files (`.vscode/`, `.idea/`)
   - Log files (`*.log`)
2. Create some files that match these patterns
3. Check that they are not tracked by Git
4. Create a legitimate file and verify it IS tracked
5. Commit your `.gitignore`

<details>
<summary>Show Solution</summary>

```bash
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
*.pyo
.venv/
venv/
.vscode/
.idea/
*.log
EOF

# Create ignored files
touch test.pyc
mkdir -p __pycache__
touch __pycache__/module.pyc
mkdir venv
touch venv/config.txt
touch debug.log

# Create tracked file
echo "# Project" > README.md

git status  # Should only show .gitignore and README.md
git add .gitignore README.md
git commit -m "Add .gitignore and README"
```

</details>

---

## Exercise 6: Viewing History

**Goal:** Practice viewing and understanding commit history.

1. Create at least 5 commits with different changes
2. View the full commit log
3. View the compact log (one line per commit)
4. View the log with a graph
5. View the last 3 commits
6. View the changes made in each commit using `git log -p`
7. View the commit with statistics (which files changed)

<details>
<summary>Show Solution</summary>

```bash
# Create multiple commits
for i in {1..5}; do
  echo "Content $i" >> file.txt
  git add file.txt
  git commit -m "Add content $i"
done

# View history
git log
git log --oneline
git log --graph --oneline
git log -3
git log -p
git log --stat
```

</details>

---

## Exercise 7: Renaming Files

**Goal:** Use `git mv` to rename files properly.

1. Create a file `oldname.py` with some content
2. Commit it
3. Rename it to `newname.py` using `git mv`
4. Commit the rename
5. Verify that Git tracked the rename (not delete + add)
6. Check the file's history follows the rename

<details>
<summary>Show Solution</summary>

```bash
echo "def func(): pass" > oldname.py
git add oldname.py
git commit -m "Add oldname.py"

git mv oldname.py newname.py
git commit -m "Rename oldname.py to newname.py"

# Verify rename is tracked
git log --follow --oneline newname.py
git log -1 --name-status  # Shows 'R100 oldname.py -> newname.py'
```

</details>

---

## Exercise 8: Undoing Changes

**Goal:** Practice different ways to undo changes.

1. Create and commit a file
2. Modify the file but don't stage it
3. Discard the working directory changes
4. Modify and stage the file
5. Unstage it (keep the changes)
6. Make a commit you want to undo
7. Revert the commit (creates a new commit that undoes it)

<details>
<summary>Show Solution</summary>

```bash
echo "original" > test.txt
git add test.txt
git commit -m "Add test.txt"

# Modify and discard
echo "modified" >> test.txt
git diff test.txt
git restore test.txt

# Stage and unstage
echo "staged" >> test.txt
git add test.txt
git restore --staged test.txt
git status

# Make a commit to revert
git commit -am "Add staged content"
git log --oneline

# Revert the last commit
git revert HEAD
git log --oneline
```

</details>

---

## Exercise 9: Amending Commits

**Goal:** Fix the most recent commit.

1. Create a commit
2. Realize you forgot to include a file
3. Add the file
4. Amend the previous commit to include the new file
5. Realize your commit message is wrong
6. Amend just the commit message

<details>
<summary>Show Solution</summary>

```bash
echo "content" > file1.txt
git add file1.txt
git commit -m "Typo in mesage"

# Forgot to add another file
echo "more content" > file2.txt
git add file2.txt
git commit --amend --no-edit

# Fix commit message
git commit --amend -m "Add files"

git log --oneline -1
```

</details>

---

## Exercise 10: Complete Workflow

**Goal:** Put it all together in a realistic workflow.

1. Initialize a new repository
2. Create a Python project structure:
   - `main.py` - entry point
   - `utils.py` - utility functions
   - `tests/` directory with `test_utils.py`
   - Proper `.gitignore`
3. Make meaningful commits as you build:
   - Initial project setup
   - Add main function
   - Add utilities
   - Add tests
4. Review your commit history
5. Clean up any untracked files

<details>
<summary>Show Partial Solution</summary>

```bash
mkdir python-project
cd python-project
git init

# .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.venv/
EOF

git add .gitignore
git commit -m "Initial setup: Add .gitignore"

# main.py
cat > main.py << 'EOF'
def main():
    print("Hello!")
if __name__ == '__main__':
    main()
EOF

git add main.py
git commit -m "Add main entry point"

# Continue adding utils, tests...
```

</details>

---

[Back to Git Basics README](README.md) | [Next: Git Basics Quiz](quiz.md)
