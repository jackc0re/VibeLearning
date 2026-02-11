# 🏆 Personal Journal - Challenges

Extend your personal journal with these additional features. Each challenge builds on the core project and teaches new skills.

---

## Challenge 1: Mood Statistics Visualization 📊

**Difficulty:** ⭐⭐  
**Time:** 1-2 hours  
**Skills:** Data analysis, string formatting

### Description

Add a visual representation of mood distribution over time. Display a text-based bar chart showing how often each mood appears.

### Requirements

1. Add a method to count moods by time period (week, month, all time)
2. Display a horizontal bar chart using ASCII characters
3. Show percentage for each mood
4. Allow filtering by date range

### Example Output

```
==================================================
           MOOD STATISTICS (Last 30 Days)
==================================================

Happy     ████████████████ 45% (9 entries)
Neutral   ████████████ 35% (7 entries)
Excited   ██████ 15% (3 entries)
Sad       ██ 5% (1 entry)

Total entries: 20
==================================================
```

### Hints

- Use `collections.Counter` for easy counting
- Calculate percentages: `(count / total) * 100`
- Use string multiplication for bars: `"█" * bar_length`

---

## Challenge 2: Word Count Goals 📝

**Difficulty:** ⭐⭐  
**Time:** 1-2 hours  
**Skills:** Goal tracking, date calculations

### Description

Set and track daily or weekly word count goals. Show progress and streaks.

### Requirements

1. Allow users to set a daily word count goal
2. Track words written per day
3. Display current streak (consecutive days meeting goal)
4. Show progress bar for today's goal
5. Save goal settings to a config file

### Example Output

```
==================================================
           WORD COUNT GOALS
==================================================

Daily Goal: 500 words

Today's Progress:
[████████░░░░░░░░░░░░] 320/500 words (64%)

Current Streak: 5 days 🔥
Best Streak: 12 days

This Week: 2,450 words
Average: 350 words/day
==================================================
```

### Hints

- Store goals in a separate `config.json` file
- Use `datetime.date.today()` for daily tracking
- Calculate streaks by checking consecutive dates

---

## Challenge 3: Entry Templates 📋

**Difficulty:** ⭐⭐  
**Time:** 1-2 hours  
**Skills:** File I/O, string templates

### Description

Create reusable templates for different types of journal entries.

### Requirements

1. Create a `templates/` directory
2. Support template files with placeholders
3. Allow users to select a template when creating an entry
4. Fill in placeholders with user input
5. Include 3+ default templates

### Template Format

```
# Daily Review
Date: {date}

## What went well today?
{went_well}

## What could have been better?
{improve}

## Tomorrow's priorities
{priorities}

## Mood: {mood}
```

### Example Output

```
Available Templates:
1. Daily Review
2. Gratitude Log
3. Weekly Reflection
4. Goal Setting

Select template (1-4): 1

Filling template 'Daily Review'...
What went well today? I finished my project
What could have been better? I didn't exercise
Tomorrow's priorities: Go for a run, read for 30 mins
Mood: happy
```

### Hints

- Use Python's `string.Template` or `.format()`
- Store templates as `.txt` files
- Parse placeholders like `{variable_name}`

---

## Challenge 4: Backup System 💾

**Difficulty:** ⭐⭐  
**Time:** 1 hour  
**Skills:** File operations, shutil

### Description

Automatically backup journal entries to prevent data loss.

### Requirements

1. Create automatic backups before saving changes
2. Keep last 5 backup files
3. Allow manual backup creation
4. Support restoring from backup
5. Add backup management to menu

### Example Output

```
==================================================
           BACKUP MANAGEMENT
==================================================

Available Backups:
1. entries_backup_20260210_143022.json (2.3 KB)
2. entries_backup_20260209_120000.json (2.1 KB)
3. entries_backup_20260208_090000.json (1.8 KB)

Options:
1. Create Backup Now
2. Restore from Backup
3. Delete Old Backups
4. Back to Main Menu
==================================================
```

### Hints

- Use `shutil.copy2()` for copying files
- Name backups with timestamp: `entries_backup_YYYYMMDD_HHMMSS.json`
- Store in a `backups/` subdirectory

---

## Challenge 5: Import Feature 📥

**Difficulty:** ⭐⭐⭐  
**Time:** 2-3 hours  
**Skills:** File parsing, data validation

### Description

Import entries from external text files.

### Requirements

1. Import from plain text files
2. Parse date, title, and content from file
3. Handle various date formats
4. Support bulk import from directory
5. Validate and preview before importing

### Supported Formats

```
# Format 1: Simple
Date: 2026-02-10
Title: My Day
Content here...

# Format 2: Markdown
# My Day
2026-02-10

Content here...

# Format 3: Plain
[2026-02-10] My Day
Content here...
```

### Hints

- Use regex to parse different formats
- Try multiple date formats with `datetime.strptime()`
- Show preview before confirming import

---

## Challenge 6: Password Protection 🔐

**Difficulty:** ⭐⭐⭐  
**Time:** 2-3 hours  
**Skills:** hashlib, cryptography concepts

### Description

Add password protection to encrypt journal entries.

### Requirements

1. Set a master password on first run
2. Encrypt entries before saving
3. Decrypt when loading (requires password)
4. Use Python's `hashlib` for password hashing
5. Use simple encryption for content

### Implementation Notes

```python
import hashlib
import base64

def hash_password(password):
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def simple_encrypt(text, key):
    """Simple XOR encryption (for learning purposes)."""
    # Note: Use proper encryption in production!
    encrypted = []
    for i, char in enumerate(text):
        key_char = key[i % len(key)]
        encrypted.append(chr(ord(char) ^ ord(key_char)))
    return base64.b64encode(''.join(encrypted).encode()).decode()

def simple_decrypt(encrypted_text, key):
    """Decrypt XOR encrypted text."""
    decoded = base64.b64decode(encrypted_text).decode()
    decrypted = []
    for i, char in enumerate(decoded):
        key_char = key[i % len(key)]
        decrypted.append(chr(ord(char) ^ ord(key_char)))
    return ''.join(decrypted)
```

### Security Note

This is for educational purposes only. For real applications, use libraries like `cryptography` or `fernet`.

---

## Challenge 7: Daily Reminders ⏰

**Difficulty:** ⭐⭐  
**Time:** 1-2 hours  
**Skills:** Time handling, notifications

### Description

Set daily reminders to write in your journal.

### Requirements

1. Set preferred reminder time
2. Show reminder message when app opens
3. Track last entry date
4. Display "days since last entry" warning
5. Optional: System notification (using `subprocess`)

### Example Output

```
==================================================
           JOURNAL REMINDER
==================================================

⏰ Reminder: It's time to write in your journal!

Your preferred writing time: 21:00
Current time: 20:58

You haven't written today yet.
Your last entry was 2 days ago.

Would you like to create a new entry? (yes/no):
==================================================
```

### Hints

- Store reminder settings in `config.json`
- Compare current time with reminder time
- Use `datetime.datetime.now()` for current time

---

## Challenge 8: Multi-Journal Support 📚

**Difficulty:** ⭐⭐⭐⭐  
**Time:** 3-4 hours  
**Skills:** Architecture, file management

### Description

Support multiple journals for different purposes (work, personal, dreams, etc.).

### Requirements

1. Create and name multiple journals
2. Switch between journals
3. Each journal has its own file
4. List all journals with entry counts
5. Set a default journal

### Example Output

```
==================================================
           JOURNAL SELECTION
==================================================

Your Journals:
1. 📓 Personal (15 entries) [DEFAULT]
2. 💼 Work (8 entries)
3. 💭 Dreams (3 entries)
4. 📚 Learning (12 entries)

Options:
1-4. Select Journal
5. Create New Journal
6. Delete Journal
7. Set Default
==================================================
```

### Hints

- Store journal metadata in `journals_index.json`
- Each journal is a separate `entries_<name>.json` file
- Track current journal in the app state

---

## 🎯 Challenge Completion Tracker

| # | Challenge | Status |
|---|-----------|--------|
| 1 | Mood Statistics | [ ] |
| 2 | Word Count Goals | [ ] |
| 3 | Entry Templates | [ ] |
| 4 | Backup System | [ ] |
| 5 | Import Feature | [ ] |
| 6 | Password Protection | [ ] |
| 7 | Daily Reminders | [ ] |
| 8 | Multi-Journal | [ ] |

---

## 💡 Tips for Completing Challenges

1. **Start small** — Implement basic functionality first
2. **Test often** — Run your code after each change
3. **Read errors** — Error messages tell you what's wrong
4. **Use the docs** — Python documentation is your friend
5. **Have fun** — These challenges are meant to be enjoyable!

---

**Good luck with your challenges! 🚀**
