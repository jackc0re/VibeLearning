# 🐍 Python Setup Guide

This guide will help you install Python on your computer.

---

## Step 1: Check if Python is Already Installed

Open your terminal/command prompt and type:

```bash
python --version
```

or

```bash
python3 --version
```

If you see something like `Python 3.11.5`, you're already set! Skip to [02_running_code.md](02_running_code.md).

---

## Step 2: Download Python

### 🪟 Windows

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click the big yellow "Download Python 3.x.x" button
3. Run the installer
4. **IMPORTANT:** Check the box that says **"Add Python to PATH"**
5. Click "Install Now"

### 🍎 macOS

**Option A: Official Installer**
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the macOS installer
3. Run the `.pkg` file and follow the prompts

**Option B: Using Homebrew** (recommended if you have Homebrew)
```bash
brew install python
```

### 🐧 Linux

Most Linux distributions come with Python. If not:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip
```

---

## Step 3: Verify Installation

Open a **new** terminal window and run:

```bash
python --version
```

You should see:
```
Python 3.x.x
```

Also verify pip (Python's package manager):
```bash
pip --version
```

---

## Step 4: Choose a Code Editor

You'll need a place to write your code. Here are great options:

### VS Code (Recommended for Beginners)
- **Free** and powerful
- Great Python support
- Download: [code.visualstudio.com](https://code.visualstudio.com/)
- Install the "Python" extension after installing VS Code

### PyCharm Community Edition
- **Free** version available
- Specifically designed for Python
- Download: [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)

### Other Options
- **Sublime Text** — Lightweight and fast
- **Atom** — Free and customizable
- **IDLE** — Comes with Python (basic but sufficient to start)

---

## Step 5: Test Your Setup

Create a file called `hello.py` with this content:

```python
print("Hello, VibeLearning! 🚀")
print("Python is working correctly!")
```

Run it:
```bash
python hello.py
```

You should see:
```
Hello, VibeLearning! 🚀
Python is working correctly!
```

---

## Troubleshooting

### "python" command not found
- **Windows:** Reinstall Python and make sure "Add to PATH" is checked
- **macOS/Linux:** Try `python3` instead of `python`

### Permission denied
- **macOS/Linux:** You may need `sudo` for installation
- **Windows:** Run the installer as Administrator

### Old Python version
- Make sure you downloaded Python 3.x (not Python 2.x)
- Python 2 is outdated and not recommended

---

## ✅ Ready?

Once Python is installed and working, move on to **[02_running_code.md](02_running_code.md)** to learn different ways to run your code!
