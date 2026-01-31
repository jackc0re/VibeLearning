# 🤝 Collaboration

**Collaboration** involves working with remote repositories and other developers using Git.

---

## ✅ Remote Repositories

A remote is a version of your project hosted on the internet or network:

```
Local Repository           Remote Repository
  (your computer)           (GitHub/GitLab)
         ↓                          ↑
      push / pull                fetch / pull
```

---

## ✅ Common Git Hosts

| Platform | URL |
|----------|-----|
| GitHub | https://github.com |
| GitLab | https://gitlab.com |
| Bitbucket | https://bitbucket.org |

---

## ✅ Adding Remotes

```bash
# Add a remote
git remote add origin https://github.com/username/repo.git

# Add a remote with a different name
git remote add upstream https://github.com/original-owner/repo.git

# View remote URL
git remote get-url origin

# Change remote URL
git remote set-url origin https://github.com/username/new-repo.git
```

---

## ✅ Listing Remotes

```bash
# Show all remotes
git remote

# Show remotes with URLs
git remote -v

# Show details for a specific remote
git remote show origin
```

---

## ✅ Cloning a Repository

```bash
# Clone a repository
git clone https://github.com/username/repo.git

# Clone into a specific directory
git clone https://github.com/username/repo.git my-directory

# Clone a specific branch
git clone -b develop https://github.com/username/repo.git

# Clone with SSH (requires SSH key)
git clone git@github.com:username/repo.git
```

Cloning creates:
- A local repository
- A remote named `origin`
- All branches as remote-tracking branches

---

## ✅ Fetching Changes

Download changes from remote without merging:

```bash
# Fetch all changes from origin
git fetch origin

# Fetch a specific branch
git fetch origin main

# Fetch all remotes
git fetch --all

# Fetch and prune deleted remote branches
git fetch --prune
```

Fetch updates your remote-tracking branches (`origin/main`, `origin/feature`) but doesn't change your local branches.

---

## ✅ Pulling Changes

Fetch and merge in one command:

```bash
# Pull from origin (default branch)
git pull

# Pull from a specific remote/branch
git pull origin main

# Pull with rebase instead of merge
git pull --rebase

# Pull without committing merge automatically
git pull --no-commit
```

---

## ✅ Pushing Changes

Upload your commits to a remote:

```bash
# Push current branch to remote
git push

# Push to a specific remote/branch
git push origin main

# Push all branches
git push --all

# Push tags
git push --tags

# Force push (use carefully!)
git push --force

# Force push with lease (safer)
git push --force-with-lease
```

---

## ✅ Setting Upstream Branch

Connect a local branch to track a remote branch:

```bash
# Push and set upstream
git push -u origin feature-login

# Set upstream without pushing
git branch --set-upstream-to=origin/feature-login feature-login

# Show tracking information
git branch -vv
```

After setting upstream, `git push` and `git pull` use the default remote/branch.

---

## ✅ Viewing Remote Branches

```bash
# List remote branches
git branch -r

# Show remote and local branches
git branch -a

# Checkout a remote branch
git checkout feature-login
# Creates local branch tracking origin/feature-login

# Or explicitly:
git checkout -b feature-login origin/feature-login
```

---

## ✅ Forking Workflow

For contributing to open source:

1. **Fork** - Create your copy of the repository
2. **Clone** - Clone your fork locally
3. **Create branch** - Work on a feature branch
4. **Commit & push** - Push to your fork
5. **Pull Request** - Request to merge into original repo

```bash
# 1. Fork on GitHub (web UI)

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/repo.git
cd repo

# 3. Add original as upstream
git remote add upstream https://github.com/ORIGINAL-OWNER/repo.git

# 4. Create feature branch
git checkout -b feature-new-stuff

# 5. Commit changes
git add .
git commit -m "Add new feature"

# 6. Push to your fork
git push -u origin feature-new-stuff

# 7. Create Pull Request on GitHub (web UI)

# 8. Update with upstream changes
git fetch upstream
git rebase upstream/main
git push origin feature-new-stuff
```

---

## ✅ Pull Requests / Merge Requests

Propose changes for review before merging:

**Pull Request (PR) Workflow:**
1. Push feature branch to remote
2. Create PR on GitHub/GitLab
3. Discuss changes with team
4. Make requested changes
5. Get approval
6. Merge into main
7. Delete feature branch

```bash
# Prepare PR
git checkout -b feature-xyz
# ... work ...
git push -u origin feature-xyz

# Then create PR on web UI
```

---

## ✅ Code Review Process

```
Developer           PR Platform            Reviewer
   |                     |                      |
   |-- push branch ----->|                      |
   |                     |-- notify --------->  |
   |                     |<-- comments -------- |
   |<-- comments -------|                      |
   |-- push updates --->|                      |
   |                     |-- notify --------->  |
   |                     |<-- approve -------- |
   |                     |-- merge -----------> |
```

---

## ✅ Syncing with Fork

Keep your fork updated with the original repository:

```bash
# Add upstream remote (once)
git remote add upstream https://github.com/ORIGINAL-OWNER/repo.git

# Fetch latest from upstream
git fetch upstream

# Update your local main branch
git checkout main
git merge upstream/main

# Update your fork on GitHub
git push origin main

# Or update feature branch
git checkout feature-xyz
git rebase upstream/main
git push origin feature-xyz
```

---

## ✅ Collaborating on the Same Repo

For teams working on the same repository:

```bash
# 1. Always start from latest main
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature-xyz

# 3. Work and commit
# ... make changes ...
git add .
git commit -m "Add feature"

# 4. Keep branch updated
git fetch origin
git rebase origin/main

# 5. Push and create PR
git push -u origin feature-xyz

# 6. After merge, update and delete branch
git checkout main
git pull origin main
git branch -d feature-xyz
```

---

## ✅ Handling Merge Conflicts in PR

When your PR has conflicts with main:

```bash
# 1. Fetch latest main
git fetch origin

# 2. Rebase your branch
git checkout feature-xyz
git rebase origin/main

# 3. Resolve conflicts
# ... edit files ...
git add .
git rebase --continue

# 4. Force push (you rewrote history)
git push --force-with-lease origin feature-xyz
```

---

## ✅ SSH vs HTTPS

| Protocol | HTTPS | SSH |
|----------|-------|-----|
| Auth | Username/password | SSH key |
| Setup | None | Generate SSH key |
| Security | Good | Better |
| Use | Simple scripts | Frequent pushes |

```bash
# HTTPS clone
git clone https://github.com/username/repo.git

# SSH clone
git clone git@github.com:username/repo.git
```

---

## ✅ Personal Access Tokens

For GitHub with HTTPS, use Personal Access Tokens (PAT):

1. Go to GitHub Settings → Developer Settings → Personal Access Tokens
2. Generate a new token
3. Use token as password when pushing

```bash
git push
# Username: your-username
# Password: ghp_xxxxxxxxxxxxxxxxxxxx
```

---

## ✅ Git LFS (Large File Storage)

For large files (videos, datasets, etc.):

```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.psd"
git lfs track "*.mp4"

# Commit .gitattributes
git add .gitattributes
git commit -m "Track large files"

# Now use Git normally
git add largefile.psd
git commit -m "Add design file"
git push
```

---

## ✅ Best Practices

1. **Pull before push** - Always sync before pushing
2. **Write good PR descriptions** - Explain what and why
3. **Keep PRs small** - Easier to review
4. **Respond to feedback** - Address reviewer comments
5. **Delete merged branches** - Keep repository clean
6. **Use branches** - Never work directly on main
7. **Sync frequently** - Reduce merge conflicts

---

## ✅ Common Collaboration Commands

```bash
# Daily workflow
git checkout main
git pull origin main
git checkout -b feature
# ... work ...
git push -u origin feature

# Syncing
git fetch --all
git status

# Review
git log --graph --oneline origin/main...feature
git diff origin/main
```

---

## 🔍 Key Takeaways

- Remote repositories enable collaboration via push/pull
- `git clone` copies a remote repository locally
- `git fetch` downloads without merging
- `git pull` = fetch + merge
- `git push` uploads your commits
- PRs/MRs are how teams review and merge code
- Forking is for contributing to open source
- Always sync before working

---

[Back: Module 15 README](../README.md) | [Previous: Merging](../03_merging/)
