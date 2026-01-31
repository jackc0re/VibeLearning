# 📁 Pathlib Module - Quiz

Test your knowledge of pathlib!

---

## Question 1
**Which operator is used to join paths in pathlib?**

A) `+`
B) `/`
C) `//`
D) `|`

<details>
<summary>Click for answer</summary>

**B) `/`**

The `/` operator is overloaded to join path components: `Path('a') / 'b' / 'c'`.
</details>

---

## Question 2
**What does `Path('document.txt').stem` return?**

A) `'document.txt'`
B) `'document'`
C) `'.txt'`
D) `''`

<details>
<summary>Click for answer</summary>

**B) `'document'`**

`stem` is the filename without the extension.
</details>

---

## Question 3
**How do you read the entire contents of a text file using pathlib?**

A) `Path('file.txt').read()`
B) `Path('file.txt').read_text()`
C) `Path('file.txt').load()`
D) `Path('file.txt').content()`

<details>
<summary>Click for answer</summary>

**B) `Path('file.txt').read_text()`**

`read_text()` reads the entire file as a string. For binary: `read_bytes()`.
</details>

---

## Question 4
**What is the purpose of `mkdir(parents=True)`?**

A) Create directory with parent permissions
B) Create directory and all parent directories if they don't exist
C) Create only parent directories
D) Create directory inside parent

<details>
<summary>Click for answer</summary>

**B) Create directory and all parent directories if they don't exist**

`parents=True` creates the full path like `mkdir -p` in bash.
</details>

---

## Question 5
**Which method finds all Python files recursively in a directory?**

A) `Path('.').glob('*.py')`
B) `Path('.').rglob('*.py')`
C) `Path('.').find('*.py')`
D) `Path('.').search('*.py')`

<details>
<summary>Click for answer</summary>

**B) `Path('.').rglob('*.py')`**

`rglob` is recursive glob - searches subdirectories too.
</details>

---

## Question 6
**What does `Path('file.txt').exists()` check?**

A) If path is a file
B) If path is a directory
C) If path exists (file or directory)
D) If path is absolute

<details>
<summary>Click for answer</summary>

**C) If path exists (file or directory)**

`exists()` returns True for any existing path, whether file or directory.
</details>

---

## Question 7
**How do you get the parent directory of a Path?**

A) `path.parent()`
B) `path.parent`
C) `path.get_parent()`
D) `path.up()`

<details>
<summary>Click for answer</summary>

**B) `path.parent`**

It's a property, not a method. Use `path.parents[i]` for higher ancestors.
</details>

---

## Question 8
**What is returned by `Path.cwd()`?**

A) Home directory
B) Current working directory
C) Root directory
D) Temp directory

<details>
<summary>Click for answer</summary>

**B) Current working directory**

`cwd()` = Current Working Directory. For home: `Path.home()`.
</details>

---

## Question 9
**What does `path.with_suffix('.json')` do?**

A) Adds .json to the path
B) Replaces the extension with .json
C) Checks if extension is .json
D) Returns path as JSON string

<details>
<summary>Click for answer</summary>

**B) Replaces the extension with .json**

Returns a new Path with the extension changed.
</details>

---

## Question 10
**Which is the preferred way to iterate over directory contents in pathlib?**

A) `os.listdir(path)`
B) `Path(path).iterdir()`
C) `Path(path).list()`
D) `Path(path).contents()`

<details>
<summary>Click for answer</summary>

**B) `Path(path).iterdir()`**

`iterdir()` yields Path objects for each item in the directory.
</details>

---

**How did you do?** Check `examples.py` for more practice!
