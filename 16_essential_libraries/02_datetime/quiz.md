# 📅 Datetime Module - Quiz

Test your knowledge of dates, times, and timezones!

---

## Question 1
**What does `datetime.now()` return?**

A) Current date only
B) Current time only
C) Current date and time
D) Current timestamp

<details>
<summary>Click for answer</summary>

**C) Current date and time**

`datetime.now()` returns a datetime object with the current local date and time.
</details>

---

## Question 2
**What is the output of `timedelta(days=1, hours=2).total_seconds()`?**

A) 86400
B) 93600
C) 7200
D) 3600

<details>
<summary>Click for answer</summary>

**B) 93600**

1 day = 86400 seconds, 2 hours = 7200 seconds. Total = 93600 seconds.
</details>

---

## Question 3
**Which format code produces a 4-digit year in strftime?**

A) `%y`
B) `%Y`
C) `%m`
D) `%d`

<details>
<summary>Click for answer</summary>

**B) `%Y`**

`%Y` gives 4-digit year (2024), `%y` gives 2-digit year (24).
</details>

---

## Question 4
**How do you parse "15/03/2024" into a datetime object?**

A) `datetime.parse("15/03/2024", "%d/%m/%Y")`
B) `datetime.strptime("15/03/2024", "%d/%m/%Y")`
C) `datetime.fromisoformat("15/03/2024")`
D) `datetime("15/03/2024")`

<details>
<summary>Click for answer</summary>

**B) `datetime.strptime("15/03/2024", "%d/%m/%Y")`**

`strptime` (string parse time) converts strings to datetime using format codes.
</details>

---

## Question 5
**In Python's datetime, what day of the week is Monday?**

A) 0
B) 1
C) 6
D) 7

<details>
<summary>Click for answer</summary>

**B) 0**

Monday is 0, Tuesday is 1, ..., Sunday is 6.
</details>

---

## Question 6
**Which module should you use for timezone handling in Python 3.9+?**

A) `pytz`
B) `datetime.timezone`
C) `zoneinfo`
D) `time`

<details>
<summary>Click for answer</summary>

**C) `zoneinfo`**

`zoneinfo` is the recommended module for timezones in Python 3.9+ (PEP 615).
</details>

---

## Question 7
**What happens when you subtract two datetime objects?**

A) Raises TypeError
B) Returns a timedelta object
C) Returns an integer (days)
D) Returns a float (seconds)

<details>
<summary>Click for answer</summary>

**B) Returns a timedelta object**

Subtracting datetimes gives you a timedelta representing the duration between them.
</details>

---

## Question 8
**How do you get today's date (without time)?**

A) `datetime.now()`
B) `datetime.today()`
C) `date.today()`
D) `datetime.now().date()`

<details>
<summary>Click for answer</summary>

**C) `date.today()`** or **D) `datetime.now().date()`**

Both work! `date.today()` is the most direct way.
</details>

---

## Question 9
**What is the output format of `datetime.isoformat()`?**

A) "2024-03-15 14:30:00"
B) "2024-03-15T14:30:00"
C) "15/03/2024 14:30:00"
D) "March 15, 2024 2:30 PM"

<details>
<summary>Click for answer</summary>

**B) "2024-03-15T14:30:00"**

ISO format uses 'T' as the separator between date and time.
</details>

---

## Question 10
**Can datetime objects be modified in place?**

A) Yes, using assignment like `dt.year = 2025`
B) No, they are immutable
C) Yes, but only the time components
D) Only using the `replace()` method

<details>
<summary>Click for answer</summary>

**B) No, they are immutable**

Datetime objects are immutable. Use `replace()` to create a new object with modified values.
</details>

---

**How did you do?** Check `examples.py` for more practice!
