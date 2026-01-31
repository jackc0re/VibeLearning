# 📝 Merging Exercises

Practice merging branches and resolving conflicts.

---

## Exercise 1: Fast-Forward Merge

**Goal:** Perform a simple fast-forward merge.

1. Create a repository with an initial commit on `main`
2. Create a new branch `feature`
3. Make one commit on `feature`
4. Switch back to `main` (no new commits)
5. Merge `feature` into `main`
6. Verify it was a fast-forward (no merge commit)

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex1 && cd merge-ex1
git init
echo "initial" > main.txt
git add main.txt
git commit -m "Initial commit"

git checkout -b feature
echo "feature" > feature.txt
git add feature.txt
git commit -m "Add feature"

git checkout main
git merge feature
git log --oneline --graph  # Should show linear history
```

</details>

---

## Exercise 2: Three-Way Merge

**Goal:** Create a merge commit when both branches have diverged.

1. Create initial commit on `main`
2. Create `feature` branch
3. Make a commit on `feature`
4. Switch to `main` and make a different commit
5. Merge `feature` into `main`
6. View the merge commit and graph

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex2 && cd merge-ex2
git init
echo "base" > file.txt
git add file.txt
git commit -m "Base commit"

git checkout -b feature
echo "feature" >> file.txt
git add file.txt
git commit -m "Feature commit"

git checkout main
echo "main" >> file.txt
git add file.txt
git commit -m "Main commit"

git merge feature
git log --oneline --graph --all
```

</details>

---

## Exercise 3: Resolve Simple Conflict

**Goal:** Create and resolve a merge conflict.

1. On `main`, create `data.txt` with content "main version"
2. Create `feature` branch
3. On `feature`, modify `data.txt` to "feature version"
4. Commit on both branches
5. Try to merge `feature` into `main`
6. Resolve the conflict to keep "feature version"
7. Complete the merge

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex3 && cd merge-ex3
git init

git checkout -b main
echo "main version" > data.txt
git add data.txt
git commit -m "Add data.txt"

git checkout -b feature
echo "feature version" > data.txt
git add data.txt
git commit -m "Change to feature version"

git checkout main
git merge feature  # Conflict!

# Edit data.txt to keep desired content
echo "feature version" > data.txt

git add data.txt
git commit -m "Merge feature, keeping feature version"
```

</details>

---

## Exercise 4: Resolve Multi-Line Conflict

**Goal:** Resolve conflicts with multiple conflicting lines.

1. Create `config.py` with multiple settings on `main`
2. Create `feature` branch
3. Modify different lines on both branches
4. Create a conflict
5. Resolve by keeping some lines from each branch
6. Complete the merge

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex4 && cd merge-ex4
git init

# Main version
cat > config.py << 'EOF'
DEBUG = True
PORT = 8000
HOST = 'localhost'
EOF
git add config.py
git commit -m "Initial config"

git checkout -b feature

# Feature version
cat > config.py << 'EOF'
DEBUG = False
PORT = 8080
HOST = '0.0.0.0'
EOF
git add config.py
git commit -m "Update config"

git checkout main

# Modify main
cat > config.py << 'EOF'
DEBUG = True
PORT = 9000
HOST = 'localhost'
SSL = False
EOF
git add config.py
git commit -m "Add SSL setting"

# Merge and resolve
git merge feature  # Conflict!
# Edit config.py to combine settings:
# DEBUG = False
# PORT = 9000
# HOST = '0.0.0.0'
# SSL = False

git add config.py
git commit -m "Merge config changes"
```

</details>

---

## Exercise 5: Abort a Merge

**Goal:** Cancel a merge when you're not ready to complete it.

1. Create branches that will conflict
2. Start a merge that creates conflicts
3. Instead of resolving, abort the merge
4. Verify the repository is back to pre-merge state

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex5 && cd merge-ex5
git init

git checkout -b main
echo "main" > data.txt
git add data.txt
git commit -m "Main version"

git checkout -b feature
echo "feature" > data.txt
git add data.txt
git commit -m "Feature version"

git checkout main
git merge feature  # Conflict!

git merge --abort
git status  # Should be clean
```

</details>

---

## Exercise 6: Squash Merge

**Goal:** Merge a feature branch as a single commit.

1. Create `feature` branch
2. Make 3 separate commits on `feature`
3. Switch to `main`
4. Squash merge `feature` into `main`
5. Verify only one commit appears on `main`

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex6 && cd merge-ex6
git init
git commit --allow-empty -m "Initial"

git checkout -b feature

for i in 1 2 3; do
  echo "feature $i" >> feature.txt
  git add feature.txt
  git commit -m "Feature commit $i"
done

git checkout main
git merge --squash feature
git commit -m "Add complete feature"

git log --oneline main  # Should show 1 commit, not 3
git log --oneline feature  # Still shows 3 commits
```

</details>

---

## Exercise 7: No Fast-Forward Merge

**Goal:** Force a merge commit even when fast-forward is possible.

1. Create a simple `feature` branch
2. Merge with `--no-ff` flag
3. Compare history with and without `--no-ff`

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex7 && cd merge-ex7
git init
git commit --allow-empty -m "Initial"

git checkout -b feature
echo "feature" > file.txt
git add file.txt
git commit -m "Add feature"

git checkout main
git merge --no-ff feature -m "Merge feature"

git log --oneline --graph  # Shows merge commit
```

</details>

---

## Exercise 8: Rebase Merge

**Goal:** Create a linear history using rebase.

1. Create `main` with 2 commits
2. Create `feature` from `main`
3. Add 2 commits to `feature`
4. Add 1 commit to `main`
5. Rebase `feature` onto `main`
6. Merge (should be fast-forward now)
7. View the linear history

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex8 && cd merge-ex8
git init

# Main commits
for i in 1 2; do
  echo "main $i" >> main.txt
  git add main.txt
  git commit -m "Main $i"
done

git checkout -b feature

# Feature commits
for i in 1 2; do
  echo "feature $i" >> feature.txt
  git add feature.txt
  git commit -m "Feature $i"
done

# Another main commit
git checkout main
echo "main 3" >> main.txt
git add main.txt
git commit -m "Main 3"

# Rebase and merge
git checkout feature
git rebase main
git checkout main
git merge feature  # Fast-forward

git log --oneline --graph
```

</details>

---

## Exercise 9: Cherry-Pick

**Goal:** Apply specific commits from one branch to another.

1. Create `feature` branch with 3 commits
2. Note the commit hashes
3. Switch to `main`
4. Cherry-pick only the middle commit from `feature`
5. Verify that only that commit was applied

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex9 && cd merge-ex9
git init
git commit --allow-empty -m "Initial"

git checkout -b feature

for i in 1 2 3; do
  echo "feature $i" >> feature.txt
  git add feature.txt
  git commit -m "Feature $i"
done

# Get commit hashes
git log --oneline feature  # Note hash of middle commit

git checkout main
git cherry-pick <middle-commit-hash>

git log --oneline  # Shows only one feature commit
```

</details>

---

## Exercise 10: Multiple Branch Merge

**Goal:** Merge multiple branches at once.

1. Create `main` with initial content
2. Create three feature branches: `feature-a`, `feature-b`, `feature-c`
3. Each branch adds a different file
4. Merge all three into `main` in one command
5. View the octopus merge commit

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex10 && cd merge-ex10
git init
echo "main" > main.txt
git add main.txt
git commit -m "Initial"

git checkout -b feature-a
echo "A" > a.txt
git add a.txt
git commit -m "Add A"

git checkout main
git checkout -b feature-b
echo "B" > b.txt
git add b.txt
git commit -m "Add B"

git checkout main
git checkout -b feature-c
echo "C" > c.txt
git add c.txt
git commit -m "Add C"

git checkout main
git merge feature-a feature-b feature-c
git log --oneline --graph
```

</details>

---

## Exercise 11: Merge with Custom Message

**Goal:** Create merges with meaningful messages.

1. Create a `feature` branch
2. Merge with a descriptive custom message
3. View the commit to see your message

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex11 && cd merge-ex11
git init
git commit --allow-empty -m "Initial"

git checkout -b feature
echo "feature" > file.txt
git add file.txt
git commit -m "Add feature"

git checkout main
git merge feature -m "Merge user authentication feature"

git log -1 --format=%B
```

</details>

---

## Exercise 12: View Merge Base

**Goal:** Find the common ancestor between branches.

1. Create `main` with several commits
2. Create `feature` from an older commit
3. Find the merge base
4. Compare main and feature to the merge base

<details>
<summary>Show Solution</summary>

```bash
mkdir merge-ex12 && cd merge-ex12
git init

# Create commits
for i in 1 2 3; do
  echo "commit $i" >> file.txt
  git add file.txt
  git commit -m "Commit $i"
done

# Create feature from commit 2
git checkout HEAD~1
git checkout -b feature

# Add to feature
echo "feature" >> feature.txt
git add feature.txt
git commit -m "Feature"

# Find merge base (should be commit 2)
git merge-base main feature

# See differences
git diff $(git merge-base main feature)..main
git diff $(git merge-base main feature)..feature
```

</details>

---

[Back to Merging README](README.md) | [Next: Merging Quiz](quiz.md)
