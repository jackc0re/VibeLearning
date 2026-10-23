# 📦 Module 15: Version Control

**Version control** is a system that records changes to files over time, allowing you to recall specific versions later. It's essential for collaborative development and tracking project history.

This module covers:
- **Git basics** - Initializing, staging, committing changes
- **Branching** - Working on multiple versions simultaneously
- **Merging** - Combining changes from different branches
- **Collaboration** - Working with remotes and teams

> **Estimated Time:** 6-8 hours
> **Prerequisites:** Modules 01-08
> **Level:** ⭐⭐⭐ Intermediate

---

## 📚 Topics Covered

| # | Topic | Description | Key Concepts |
|---|-------|-------------|--------------|
| 01 | [Git Basics](01_git_basics/README.md) | Core Git commands | `init`, `add`, `commit`, `status`, `log` |
| 02 | [Branching](02_branching/README.md) | Creating and managing branches | `branch`, `checkout`, `switch`, `HEAD` |
| 03 | [Merging](03_merging/README.md) | Combining changes | `merge`, `rebase`, conflicts |
| 04 | [Collaboration](04_collaboration/README.md) | Working with remotes | `clone`, `push`, `pull`, `remote` |

---

## 🎯 Learning Goals

By the end of this module, you should be able to:

- Initialize a **Git repository** and track changes.
- Use **staging area** to selectively commit changes.
- Create and switch between **branches** for parallel development.
- **Merge** branches and resolve conflicts.
- Work with **remote repositories** (GitHub, GitLab).
- Use Git for **collaboration** with a team.

---

## 📂 Module Structure

```
15_version_control/
├── README.md
├── 01_git_basics/
│   ├── README.md
│   ├── examples.sh
│   ├── exercises.md
│   └── quiz.md
├── 02_branching/
│   ├── README.md
│   ├── examples.sh
│   ├── exercises.md
│   └── quiz.md
├── 03_merging/
│   ├── README.md
│   ├── examples.sh
│   ├── exercises.md
│   └── quiz.md
└── 04_collaboration/
    ├── README.md
    ├── examples.sh
    ├── exercises.md
    └── quiz.md
```

---

## 🧠 What is Version Control?

Version control helps you:
- **Track history** - See who changed what and when
- **Revert changes** - Go back to previous versions
- **Collaborate** - Work with others without conflicts
- **Experiment** - Try new ideas safely on branches
- **Backup** - Keep remote copies of your work

---

## 💡 Git vs Other Tools

| Tool | Type | Use Case |
|------|------|----------|
| **Git** | Distributed | Most projects, teams, open source |
| **SVN** | Centralized | Legacy systems, some enterprises |
| **Mercurial** | Distributed | Similar to Git, less popular |

Git is the industry standard and what we'll focus on.

---

## 🔧 Setting Up Git

```bash
# Install Git (if not already installed)
# Windows: https://git-scm.com/download/win
# macOS: brew install git
# Linux: sudo apt install git

# Configure your identity
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Check your configuration
git config --list
```

---

## 📝 Common Git Workflow

1. **Initialize** - `git init`
2. **Stage changes** - `git add file.py`
3. **Commit changes** - `git commit -m "message"`
4. **Check status** - `git status`
5. **View history** - `git log`

---

**Start here:** [01_git_basics](01_git_basics/README.md)
