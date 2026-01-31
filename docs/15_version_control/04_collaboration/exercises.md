# 📝 Collaboration Exercises

Practice working with remote repositories and collaborating with others.

> **Note:** Many of these exercises require an actual GitHub/GitLab account and remote repository.

---

## Exercise 1: Cloning a Repository

**Goal:** Clone a remote repository to your local machine.

1. Create a repository on GitHub/GitLab (or use an existing one)
2. Clone it to your local machine
3. List the files in the cloned directory
4. Check which remote is configured
5. View the remote URL

<details>
<summary>Show Solution</summary>

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# List files
ls -la

# Check remote
git remote
git remote -v

# View remote URL
git remote get-url origin
```

</details>

---

## Exercise 2: Pushing Changes

**Goal:** Make local changes and push them to the remote.

1. Clone a repository (or use existing)
2. Create a new file `hello.txt`
3. Add and commit the file
4. Push the changes to the remote
5. Verify the changes are on GitHub/GitLab

<details>
<summary>Show Solution</summary>

```bash
cd your-repo

echo "Hello, World!" > hello.txt
git add hello.txt
git commit -m "Add hello.txt"

git push

# Verify on GitHub/GitLab web UI
```

</details>

---

## Exercise 3: Pulling Changes

**Goal:** Pull changes made by someone else (or yourself on another machine).

1. Make changes on GitHub/GitLab web UI (or another machine)
2. On your local machine, fetch the changes
3. Merge the changes into your local branch
4. Use `git pull` as a shortcut
5. Verify your local files are updated

<details>
<summary>Show Solution</summary>

```bash
cd your-repo

# Make a change on GitHub web UI (e.g., add a file)

# Fetch changes
git fetch origin

# View what's new
git log origin/main

# Pull changes (fetch + merge)
git pull origin main

# Verify
cat new-file.txt
```

</details>

---

## Exercise 4: Setting Upstream Branch

**Goal:** Configure a local branch to track a remote branch.

1. Create a new local branch `feature`
2. Make a commit on the branch
3. Push and set upstream
4. Verify the tracking relationship
5. Push with just `git push` (no arguments)

<details>
<summary>Show Solution</summary>

```bash
cd your-repo

git checkout -b feature
echo "feature" > feature.txt
git add feature.txt
git commit -m "Add feature"

git push -u origin feature

# Verify tracking
git branch -vv

# Now can push with just:
git push
```

</details>

---

## Exercise 5: Working with Multiple Remotes

**Goal:** Add and work with multiple remotes.

1. Clone a repository
2. Add a second remote called `upstream`
3. List all remotes with URLs
4. Fetch from both remotes
5. Compare the branches

<details>
<summary>Show Solution</summary>

```bash
cd your-repo

git remote add upstream https://github.com/original-owner/repo.git

git remote -v

git fetch origin
git fetch upstream

# Compare branches
git log origin/main..upstream/main
```

</details>

---

## Exercise 6: Remote Branches

**Goal:** Work with remote branches.

1. Fetch all branches from origin
2. List all remote branches
3. Checkout a remote branch
4. Make changes and push to a new remote branch
5. Delete the remote branch

<details>
<summary>Show Solution</summary>

```bash
cd your-repo

git fetch origin
git branch -r

git checkout origin/develop
# Creates local 'develop' branch

git checkout -b my-feature
echo "new feature" > new.txt
git add new.txt
git commit -m "Add feature"
git push -u origin my-feature

# Delete remote branch
git push origin --delete my-feature
```

</details>

---

## Exercise 7: Resolving Pull Conflicts

**Goal:** Handle conflicts when pulling changes.

1. Make a local change to a file
2. Make a conflicting change on GitHub web UI
3. Try to pull (will conflict)
4. Resolve the conflict
5. Complete the merge
6. Push the resolution

<details>
<summary>Show Solution</summary>

```bash
cd your-repo

echo "local change" > conflict.txt
git add conflict.txt
git commit -m "Local change"

# On GitHub, edit conflict.txt to say "remote change"
# and commit via web UI

git pull origin main
# Conflict!

# Edit conflict.txt to resolve
echo "resolved" > conflict.txt

git add conflict.txt
git commit -m "Resolve conflict"
git push origin main
```

</details>

---

## Exercise 8: Pull Request Workflow

**Goal:** Create a pull request using the proper workflow.

1. Fork a repository (or use your own)
2. Clone your fork
3. Add upstream remote
4. Create a feature branch
5. Make changes and push to your fork
6. Create a pull request on GitHub/GitLab

<details>
<summary>Show Solution</summary>

```bash
# 1. Fork on GitHub web UI

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/repo.git
cd repo

# 3. Add upstream
git remote add upstream https://github.com/ORIGINAL-OWNER/repo.git

# 4. Create feature branch
git checkout -b feature-new-stuff

# 5. Make changes
echo "new feature" > feature.txt
git add feature.txt
git commit -m "Add new feature"

# 6. Push to your fork
git push -u origin feature-new-stuff

# 7. Create PR on GitHub web UI
```

</details>

---

## Exercise 9: Syncing a Fork

**Goal:** Keep your fork updated with the original repository.

1. Fork a repository and clone it
2. Make a local branch with some changes
3. Fetch from upstream
4. Merge upstream changes into your main
5. Push updated main to your fork
6. Update your feature branch

<details>
<summary>Show Solution</summary>

```bash
cd repo

git checkout -b feature
echo "my work" > work.txt
git add work.txt
git commit -m "My work"

git fetch upstream
git checkout main
git merge upstream/main
git push origin main

git checkout feature
git rebase upstream/main
# If conflicts, resolve them
git push origin feature --force-with-lease
```

</details>

---

## Exercise 10: Team Collaboration

**Goal:** Simulate team workflow with pull requests.

1. Create two branches: `feature-a` and `feature-b`
2. Make changes on each branch
3. Push both branches
4. Create pull requests for each
5. Merge one of the pull requests
6. Update the other branch before merging

<details>
<summary>Show Solution</summary>

```bash
cd repo

git checkout -b feature-a
echo "feature A" > a.txt
git add a.txt
git commit -m "Feature A"
git push -u origin feature-a

git checkout main
git checkout -b feature-b
echo "feature B" > b.txt
git add b.txt
git commit -m "Feature B"
git push -u origin feature-b

# Create PRs on GitHub web UI
# Merge feature-a PR

# Update feature-b
git checkout feature-b
git fetch origin
git rebase origin/main
git push origin feature-b --force-with-lease
# Now merge feature-b PR
```

</details>

---

## Exercise 11: SSH Key Setup

**Goal:** Set up SSH keys for authentication.

1. Generate a new SSH key
2. Add it to the ssh-agent
3. Copy the public key
4. Add the key to GitHub/GitLab
5. Clone a repository using SSH

<details>
<summary>Show Solution</summary>

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C 'your-email@example.com'
# Press Enter for defaults

# Add to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub

# On GitHub: Settings > SSH and GPG keys > New SSH key
# Paste the key

# Clone using SSH
git clone git@github.com:your-username/repo.git
```

</details>

---

## Exercise 12: Personal Access Token

**Goal:** Use a Personal Access Token for HTTPS authentication.

1. Generate a Personal Access Token on GitHub
2. Use it to authenticate when pushing
3. Configure Git to remember credentials (optional)
4. Push to verify it works

<details>
<summary>Show Solution</summary>

```bash
# Generate PAT on GitHub:
# Settings > Developer Settings > Personal access tokens
# Select 'repo' scope
# Copy the token (starts with ghp_)

# Clone or work with HTTPS repo
git clone https://github.com/username/repo.git
cd repo

# Make changes
echo "test" > test.txt
git add test.txt
git commit -m "Test"

# Push (will prompt for password)
git push
# Username: your-username
# Password: paste-the-token-here

# Optional: Configure credential helper
git config --global credential.helper store
# Next push will save credentials (use carefully!)
```

</details>

---

## Exercise 13: Viewing Remote Differences

**Goal:** Compare local and remote branches.

1. Make some local commits without pushing
2. Fetch the remote
3. See what commits are unpushed
4. See what commits are new on remote
5. View file differences

<details>
<summary>Show Solution</summary>

```bash
cd repo

# Make local commits
echo "local" > local.txt
git add local.txt
git commit -m "Local change"

# Fetch remote
git fetch origin

# View differences
git log origin/main..main  # Unpushed
git log main..origin/main  # New on remote
git diff origin/main  # File differences
```

</details>

---

## Exercise 14: Pruning Remote Branches

**Goal:** Clean up deleted remote branches locally.

1. Delete a remote branch on GitHub
2. Fetch to see local tracking branches still exist
3. Prune to remove stale remote references
4. Verify cleanup

<details>
<summary>Show Solution</summary>

```bash
cd repo

# Delete a branch on GitHub web UI
# (or: git push origin --delete feature)

# Fetch - remote tracking branch still shows
git fetch origin
git branch -r  # Still shows deleted branch

# Prune remote references
git fetch --prune

# Verify
git branch -r  # Deleted branch is gone

# Or prune for specific remote
git remote prune origin
```

</details>

---

## Exercise 15: Git LFS

**Goal:** Set up Git LFS for large files.

1. Install Git LFS
2. Configure tracking for large file types
3. Add a large file to the repository
4. Push to verify LFS is working
5. Clone in a new location to test

<details>
<summary>Show Solution</summary>

```bash
# Install Git LFS (one time)
git lfs install

# Track file types
git lfs track '*.zip'
git lfs track '*.psd'
git lfs track '*.mp4'

# Commit .gitattributes
git add .gitattributes
git commit -m "Configure LFS"

# Add a large file
# (Create or copy a large file here)
cp /path/to/large/file.zip large.zip
git add large.zip
git commit -m "Add large file"
git push

# Clone in new location to test
git clone https://github.com/username/repo.git test-clone
cd test-clone
git lfs ls-files  # Show LFS files
```

</details>

---

[Back to Collaboration README](README.md) | [Next: Collaboration Quiz](quiz.md)
