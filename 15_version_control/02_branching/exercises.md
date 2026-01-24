# 📝 Branching Exercises

Practice creating and managing Git branches.

---

## Exercise 1: Create Your First Branch

**Goal:** Create a new branch and make changes on it.

1. Initialize a repository and make an initial commit
2. Create a new branch called `feature-login`
3. Switch to the new branch
4. Create a file `login.py` with a simple login function
5. Commit the file
6. Switch back to `main` and verify the file is not there

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex1 && cd branch-ex1
git init
echo "initial" > main.txt
git add main.txt
git commit -m "Initial commit"

git branch feature-login
git checkout feature-login

echo "def login(): pass" > login.py
git add login.py
git commit -m "Add login function"

git checkout main
ls  # login.py should not exist here
```

</details>

---

## Exercise 2: Multiple Feature Branches

**Goal:** Work with multiple branches simultaneously.

1. Create three branches: `feature-a`, `feature-b`, `feature-c`
2. On `feature-a`, create a file with "Content A"
3. On `feature-b`, create a file with "Content B"
4. On `feature-c`, create a file with "Content C"
5. List all branches
6. Switch between branches and verify each branch has only its file

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex2 && cd branch-ex2
git init
echo "initial" > main.txt
git add main.txt
git commit -m "Initial commit"

git checkout -b feature-a
echo "Content A" > file.txt
git add file.txt
git commit -m "Add content A"

git checkout -b feature-b
echo "Content B" > file.txt
git add file.txt
git commit -m "Add content B"

git checkout -c feature-c
echo "Content C" > file.txt
git add file.txt
git commit -m "Add content C"

# Verify each branch
git checkout feature-a && cat file.txt
git checkout feature-b && cat file.txt
git checkout feature-c && cat file.txt
```

</details>

---

## Exercise 3: Renaming Branches

**Goal:** Practice renaming branches.

1. Create a branch with a typo: `fetaure-products` (note typo)
2. Make a commit on that branch
3. Rename it to the correct name `feature-products`
4. Verify the rename worked
5. Also rename it to `product-list`

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex3 && cd branch-ex3
git init
git commit --allow-empty -m "Initial"

git branch fetaure-products
git branch  # Show the typo

git checkout fetaure-products
git commit --allow-empty -m "Work on branch"

git branch -m feature-products
git branch  # Should show corrected name

git branch -m product-list
git branch  # Show new name
```

</details>

---

## Exercise 4: Deleting Branches

**Goal:** Practice deleting branches.

1. Create and work on a branch `temp-branch`
2. Make a commit
3. Switch back to `main`
4. Delete `temp-branch`
5. Try deleting a branch that hasn't been merged (use `-D`)

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex4 && cd branch-ex4
git init
git commit --allow-empty -m "Initial"

git checkout -b temp-branch
echo "temp" > temp.txt
git add temp.txt
git commit -m "Add temp file"

git checkout main
git branch  # Show branches

git branch -d temp-branch
git branch  # Should be gone

# Create another test branch
git checkout -b will-delete
git commit --allow-empty -m "Test"

git checkout main
git branch -D will-delete  # Force delete even if not merged
```

</details>

---

## Exercise 5: Comparing Branches

**Goal:** Understand differences between branches.

1. On `main`, create commits with 3 different files
2. Create `feature` branch from `main`
3. Make 2 new commits on `feature`
4. Make 1 new commit on `main`
5. Show commits unique to `feature`
6. Show commits unique to `main`
7. View the file differences between branches

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex5 && cd branch-ex5
git init

# 3 commits on main
for i in 1 2 3; do
  echo "file $i" > file$i.txt
  git add file$i.txt
  git commit -m "Add file $i"
done

# Create feature branch
git checkout -b feature

# 2 commits on feature
echo "feature 1" > feat1.txt
git add feat1.txt
git commit -m "Add feat1"

echo "feature 2" > feat2.txt
git add feat2.txt
git commit -m "Add feat2"

# 1 commit on main
git checkout main
echo "main new" > new.txt
git add new.txt
git commit -m "Add new on main"

# Compare
git log main..feature --oneline
git log feature..main --oneline
git diff main feature
```

</details>

---

## Exercise 6: Detached HEAD

**Goal:** Work with detached HEAD state.

1. Make several commits on `main`
2. Checkout the second-to-last commit (HEAD~1)
3. Verify you're in detached HEAD state
4. Create a new branch from this detached state
5. Switch to the new branch and make a change

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex6 && cd branch-ex6
git init

for i in 1 2 3; do
  echo "line $i" >> file.txt
  git add file.txt
  git commit -m "Commit $i"
done

# Go to detached HEAD
git checkout HEAD~1
git status  # Shows detached HEAD

# Create branch from here
git checkout -b old-version
git status  # Normal state now

echo "old version change" >> file.txt
git add file.txt
git commit -m "Modify old version"
```

</details>

---

## Exercise 7: Branch History

**Goal:** View and understand branch history.

1. Create `main` with 3 commits
2. Create `feature` from `main`
3. Add 2 commits to `feature`
4. Show all commits on all branches with graph
5. Show commits in `feature` not in `main`
6. Show commits in `main` not in `feature`
7. View the content of a specific file from `feature` while on `main`

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex7 && cd branch-ex7
git init

# 3 commits on main
for i in 1 2 3; do
  echo "main $i" >> main.txt
  git add main.txt
  git commit -m "Main commit $i"
done

# Feature branch
git checkout -b feature

# 2 commits on feature
for i in 1 2; do
  echo "feature $i" >> feature.txt
  git add feature.txt
  git commit -m "Feature commit $i"
done

# View history
git log --oneline --graph --all
git log main..feature --oneline
git log feature..main --oneline
git checkout main
git show feature:feature.txt
```

</details>

---

## Exercise 8: Branch Naming Convention

**Goal:** Practice good branch naming.

1. Create branches with proper naming:
   - A new feature branch
   - A bugfix branch
   - A documentation branch
   - A hotfix branch
2. List all branches to see them

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex8 && cd branch-ex8
git init
git commit --allow-empty -m "Initial"

git checkout -b feature-user-authentication
git checkout main

git checkout -b bugfix-login-validation
git checkout main

git checkout -b docs-api-reference
git checkout main

git checkout -b hotfix-security-patch

git branch
```

</details>

---

## Exercise 9: Switching with Uncommitted Changes

**Goal:** Handle switching branches with uncommitted work.

1. Create and commit a file on `main`
2. Switch to a new branch
3. Modify the file but don't commit
4. Try to switch back to `main` (should work if file wasn't changed on main)
5. Modify the file on both branches
6. Try to switch between branches (should fail)
7. Use stash to save changes and switch

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex9 && cd branch-ex9
git init
echo "original" > data.txt
git add data.txt
git commit -m "Initial"

git checkout -b feature
echo "feature change" >> data.txt
# No commit yet
git checkout main  # Should work if you haven't changed main

git checkout feature
echo "more" >> data.txt
git checkout main
echo "main change" >> data.txt

# Now try to switch (will fail)
git checkout feature  # Error!

# Stash and switch
git stash
git checkout feature
git stash pop
```

</details>

---

## Exercise 10: Branch from Tag

**Goal:** Create branches from tags.

1. Make several commits on `main`
2. Create a tag `v1.0` on the third commit
3. Create a `maintenance` branch from this tag
4. Make a fix on the maintenance branch
5. Continue work on `main` (making newer commits)
6. Verify both branches diverged from the tag

<details>
<summary>Show Solution</summary>

```bash
mkdir branch-ex10 && cd branch-ex10
git init

# Create 5 commits
for i in 1 2 3 4 5; do
  echo "v1.0.$i" >> app.txt
  git add app.txt
  git commit -m "Version 1.0.$i"
done

# Tag the 3rd commit
git tag v1.0 HEAD~2

# Create maintenance branch from tag
git branch maintenance v1.0

# Make fix on maintenance
git checkout maintenance
echo "fix" >> app.txt
git add app.txt
git commit -m "Hotfix for v1.0"

# Continue on main
git checkout main
echo "v1.1 features" >> app.txt
git add app.txt
git commit -m "Add v1.1 features"

# View divergence
git log --oneline --graph --all
```

</details>

---

[Back to Branching README](README.md) | [Next: Branching Quiz](quiz.md)
