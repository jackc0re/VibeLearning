# ▶️ Running Python Code

There are several ways to run Python code. Understanding them will make your learning journey smoother.

---

## Method 1: Running a Python File

This is the most common way to run Python programs.

### Steps:
1. Create a file with a `.py` extension (e.g., `my_program.py`)
2. Write your Python code in the file
3. Open terminal/command prompt
4. Navigate to the file's directory
5. Run: `python my_program.py`

### Example:

Create `greet.py`:
```python
name = "World"
print(f"Hello, {name}!")
```

Run it:
```bash
python greet.py
```

Output:
```
Hello, World!
```

---

## Method 2: Python Interactive Mode (REPL)

REPL = **R**ead-**E**valuate-**P**rint-**L**oop

Great for quick experiments and testing small pieces of code.

### How to Start:
```bash
python
```

You'll see:
```
Python 3.x.x (...)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Try It:
```python
>>> 2 + 2
4
>>> print("Hello!")
Hello!
>>> name = "Python"
>>> f"I love {name}"
'I love Python'
>>> exit()  # To leave
```

---

## Method 3: Running Code in Your Editor

Most modern editors can run Python directly.

### VS Code:
1. Open your `.py` file
2. Click the ▶️ (Play) button in the top-right
3. Or press `Ctrl+F5` (Windows) / `Cmd+F5` (Mac)

### PyCharm:
1. Open your `.py` file
2. Right-click → "Run 'filename'"
3. Or press `Shift+F10`

---

## Method 4: Jupyter Notebooks

Interactive notebooks that mix code, output, and documentation.

### Install:
```bash
pip install jupyter
```

### Start:
```bash
jupyter notebook
```

This opens in your browser where you can create `.ipynb` files.

Great for:
- Data science
- Learning (see code + results together)
- Experimentation

---

## Which Method Should You Use?

| Situation | Recommended Method |
|-----------|-------------------|
| Learning concepts | REPL or Jupyter |
| Writing real programs | Python files + Editor |
| Quick calculations | REPL |
| Sharing code | Python files |
| Data analysis | Jupyter Notebooks |

---

## Common Commands Reference

```bash
# Run a Python file
python filename.py

# Start interactive mode
python

# Check Python version
python --version

# Install a package
pip install package_name

# List installed packages
pip list
```

---

## 💡 Tips

1. **Always save your file** before running it
2. **Use meaningful file names** like `calculator.py` not `test1.py`
3. **Don't name your files** after Python modules (e.g., don't create `random.py`)
4. **Read error messages** — they usually tell you what's wrong

---

## ✅ Next Step

Now that you know how to run Python code, learn **[how to use this repository](03_using_this_repo.md)** effectively!
