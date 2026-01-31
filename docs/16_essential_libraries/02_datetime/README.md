# 📅 Datetime Module

> **Working with dates, times, and timezones in Python**

---

## 🎯 Learning Objectives

By the end of this section, you'll understand:
- How to create and manipulate dates and times
- The difference between `datetime`, `date`, `time`, and `timedelta`
- How to format dates as strings and parse strings to dates
- Working with timezones using `zoneinfo` (Python 3.9+)

---

## 📆 The datetime Classes

Python's `datetime` module provides several key classes:

| Class | Represents | Example |
|-------|------------|---------|
| `datetime` | Date and time | `2024-01-15 14:30:00` |
| `date` | Date only | `2024-01-15` |
| `time` | Time only | `14:30:00` |
| `timedelta` | Duration | `5 days, 3:30:00` |

---

## 🕐 Creating Dates and Times

### Current Date/Time

```python
from datetime import datetime, date, time

# Get current datetime
now = datetime.now()
print(now)  # 2024-01-15 14:30:45.123456

# Get current date
today = date.today()
print(today)  # 2024-01-15

# Create specific datetime
meeting = datetime(2024, 3, 15, 10, 30)
print(meeting)  # 2024-03-15 10:30:00
```

### Creating Time Objects

```python
from datetime import time

# Create a time object
lunch_time = time(12, 30, 0)
print(lunch_time)  # 12:30:00

# With microseconds
precise_time = time(14, 30, 45, 123456)
print(precise_time)  # 14:30:45.123456
```

---

## ➕ Working with Timedeltas

`timedelta` represents a duration — the difference between two dates or times.

### Real-World Analogy

Think of `timedelta` as a rubber band that can stretch between two points in time.

```python
from datetime import datetime, timedelta

now = datetime.now()

# Add time
future = now + timedelta(days=7)
past = now - timedelta(hours=3)

# Calculate difference
deadline = datetime(2024, 12, 31)
time_left = deadline - now

print(f"Days until deadline: {time_left.days}")
print(f"Total seconds: {time_left.total_seconds()}")
```

### Common timedelta Arguments

```python
timedelta(days=1)           # 1 day
timedelta(hours=2)          # 2 hours
timedelta(minutes=30)       # 30 minutes
timedelta(weeks=1)          # 7 days
timedelta(days=1, hours=2)  # Combined
```

---

## 🔤 Formatting and Parsing

### strftime - Format datetime to string

```python
from datetime import datetime

now = datetime.now()

# Common formats
print(now.strftime("%Y-%m-%d"))           # 2024-01-15
print(now.strftime("%d/%m/%Y"))           # 15/01/2024
print(now.strftime("%B %d, %Y"))          # January 15, 2024
print(now.strftime("%I:%M %p"))           # 02:30 PM
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-01-15 14:30:00
```

### Common Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | 2024 |
| `%m` | Month (01-12) | 01 |
| `%d` | Day (01-31) | 15 |
| `%H` | Hour 24h (00-23) | 14 |
| `%I` | Hour 12h (01-12) | 02 |
| `%M` | Minute (00-59) | 30 |
| `%S` | Second (00-59) | 45 |
| `%p` | AM/PM | PM |
| `%A` | Weekday name | Monday |
| `%B` | Month name | January |

### strptime - Parse string to datetime

```python
from datetime import datetime

date_string = "2024-03-15 14:30:00"
parsed = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed)  # 2024-03-15 14:30:00

# ISO format (convenient!)
iso_string = "2024-03-15T14:30:00"
parsed_iso = datetime.fromisoformat(iso_string)
print(parsed_iso)  # 2024-03-15 14:30:00
```

---

## 🌍 Working with Timezones

Python 3.9+ includes the `zoneinfo` module for timezone handling.

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# Create datetime with timezone
ny_time = datetime.now(ZoneInfo("America/New_York"))
print(ny_time)  # 2024-01-15 09:30:00-05:00

# Convert between timezones
tokyo_time = ny_time.astimezone(ZoneInfo("Asia/Tokyo"))
print(tokyo_time)  # 2024-01-15 23:30:00+09:00

# UTC is always available
utc_now = datetime.now(ZoneInfo("UTC"))
```

### Common Timezone Names

| Timezone | Description |
|----------|-------------|
| `UTC` | Coordinated Universal Time |
| `America/New_York` | US Eastern |
| `America/Los_Angeles` | US Pacific |
| `Europe/London` | UK |
| `Europe/Paris` | Central Europe |
| `Asia/Tokyo` | Japan |
| `Asia/Shanghai` | China |
| `Australia/Sydney` | Eastern Australia |

---

## ⚠️ Common Mistakes

1. **Confusing month and day** - Americans use MM/DD/YYYY, most of the world uses DD/MM/YYYY
2. **Forgetting timezones** - Always be aware if your datetime is naive (no timezone) or aware
3. **Modifying datetime objects** - They are immutable; operations return new objects
4. **Off-by-one in months** - Months are 1-12, not 0-11

---

## 📝 Quick Reference

```python
from datetime import datetime, date, time, timedelta
from zoneinfo import ZoneInfo

# Current time
now = datetime.now()

# Create specific datetime
dt = datetime(2024, 3, 15, 10, 30)

# Add/subtract time
future = now + timedelta(days=7)

# Format
date_str = now.strftime("%Y-%m-%d")

# Parse
dt = datetime.strptime("2024-03-15", "%Y-%m-%d")

# Timezone aware
aware = datetime.now(ZoneInfo("UTC"))
```

---

## 🎓 Next Steps

Run `examples.py` to see datetime in action, then try `exercises.py`!
