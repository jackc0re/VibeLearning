"""
Intermediate Exercise 6: File I/O
=================================
Practice reading and writing text files, JSON, CSV, and pathlib.
All files live in a system temp folder, never in the repository.
"""

import shutil
import tempfile

print("=" * 50)
print("EXERCISE 6: File I/O")
print("=" * 50)

workdir = tempfile.mkdtemp(prefix="vl_file_io_")
print(f"\nAll exercise files go into: {workdir}")


# =============================================================================
# EXERCISE 6.1: Writing and Reading Text Files
# =============================================================================
print("\n--- Exercise 6.1: Writing and Reading Text Files ---")
"""
Inside workdir:
- Write three lines to notes.txt using a with block
- Read the whole file back with .read()
- Read it again as a list with .readlines()
- Confirm the round trip preserved the content
"""


# Your code below:
# notes = ...
# lines = [...]

# Test (uncomment after implementing)
# with open(notes, "w", encoding="utf-8") as f:
#     f.write("\n".join(lines) + "\n")


# =============================================================================
# EXERCISE 6.2: Processing a File Line by Line
# =============================================================================
print("\n--- Exercise 6.2: Processing a File Line by Line ---")
"""
Inside workdir:
- Write a small log file: one "LEVEL message" entry per line
- Count the total lines and the ERROR lines by iterating the
  open file object directly (one line in memory at a time)
"""


# Your code below:
# log_path = ...
# entries = [...]


# =============================================================================
# EXERCISE 6.3: Working with JSON
# =============================================================================
print("\n--- Exercise 6.3: Working with JSON ---")
"""
Inside workdir:
- Save a profile dict (name, level, skills list) to profile.json
  with json.dump
- Load it back with json.load
- Verify the loaded data equals the original
"""

import json


# Your code below:
# profile_path = ...
# profile = {...}


# =============================================================================
# EXERCISE 6.4: Working with CSV
# =============================================================================
print("\n--- Exercise 6.4: Working with CSV ---")
"""
Inside workdir:
- Write rows (name, score) with csv.writer (remember newline="")
- Read them back with csv.DictReader
- Compute and print the average score
"""

import csv


# Your code below:
# scores_path = ...
# rows = [...]


# =============================================================================
# EXERCISE 6.5: Path Manipulation with pathlib
# =============================================================================
print("\n--- Exercise 6.5: Path Manipulation with pathlib ---")
"""
Using pathlib.Path:
- Create the nested folder reports/2026 inside workdir
  (mkdir with parents=True)
- Write annual.txt into it
- Inspect a path's .name and .suffix
- List every file under workdir recursively with rglob
"""

from pathlib import Path


# Your code below:
# reports_dir = ...


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 6.1
print("\n--- Solution 6.1 ---")

notes = Path(workdir) / "notes.txt"
lines = ["Shopping list:", "- apples", "- oat milk"]

with open(notes, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

with open(notes, "r", encoding="utf-8") as f:
    whole = f.read()

with open(notes, "r", encoding="utf-8") as f:
    as_lines = f.readlines()

expected = "\n".join(lines) + "\n"
print(f"Wrote {notes.name}: {whole!r}")
print(f"readlines found {len(as_lines)} lines")
print(f"Round trip intact: {whole == expected}")

# SOLUTION 6.2
print("\n--- Solution 6.2 ---")

log_path = Path(workdir) / "server.log"
entries = [
    "INFO server started",
    "INFO request received",
    "ERROR disk full",
    "INFO request received",
    "ERROR timeout",
    "WARNING slow response",
]
with open(log_path, "w", encoding="utf-8") as f:
    for entry in entries:
        f.write(entry + "\n")

total = 0
errors = 0
with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        total += 1
        if line.startswith("ERROR"):
            errors += 1

print(f"Scanned {log_path.name} line by line")
print(f"Found {total} lines and {errors} errors")

# SOLUTION 6.3
print("\n--- Solution 6.3 ---")

profile_path = Path(workdir) / "profile.json"
profile = {"name": "Sam", "level": 3, "skills": ["sql", "regex"]}

with open(profile_path, "w", encoding="utf-8") as f:
    json.dump(profile, f, indent=2)

with open(profile_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"Loaded: {loaded}")
print(f"Round trip intact: {loaded == profile}")

# SOLUTION 6.4
print("\n--- Solution 6.4 ---")

scores_path = Path(workdir) / "scores.csv"
rows = [["name", "score"], ["Ada", 91], ["Linus", 78], ["Grace", 99]]

with open(scores_path, "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(rows)

with open(scores_path, "r", encoding="utf-8", newline="") as f:
    records = list(csv.DictReader(f))

scores = [int(record["score"]) for record in records]
print(f"Records: {records}")
print(f"Average score: {sum(scores) / len(scores):.1f}")

# SOLUTION 6.5
print("\n--- Solution 6.5 ---")

reports_dir = Path(workdir) / "reports" / "2026"
reports_dir.mkdir(parents=True, exist_ok=True)
report = reports_dir / "annual.txt"
report.write_text("Revenue: lots\n", encoding="utf-8")

print(f"Created {report}")
print(f"  name: {report.name}, suffix: {report.suffix}")

all_files = sorted(path for path in Path(workdir).rglob("*") if path.is_file())
print("Files under the temp folder:")
for path in all_files:
    print(f"  {path.relative_to(workdir)}")

# CLEANUP
print("\n--- Cleanup ---")
shutil.rmtree(workdir, ignore_errors=True)
if Path(workdir).exists():
    print(f"Cleanup FAIL: {workdir} still present")
else:
    print(f"Cleanup PASS: removed {workdir}")

print("\n" + "=" * 50)
print("Great job! Move on to 07_design_patterns.py")
print("=" * 50)
