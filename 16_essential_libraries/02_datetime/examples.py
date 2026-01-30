"""
Datetime Module - Examples
==========================
Working with dates, times, and timezones.
"""

print("=" * 60)
print("DATETIME MODULE - Examples")
print("=" * 60)

from datetime import datetime, date, time, timedelta
from zoneinfo import ZoneInfo

# =============================================================================
# CREATING DATES AND TIMES
# =============================================================================
print("\n--- Creating Dates and Times ---\n")

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Type: {type(now)}")

# Current date only
today = date.today()
print(f"\nToday's date: {today}")
print(f"Year: {today.year}, Month: {today.month}, Day: {today.day}")

# Creating specific datetime
new_year = datetime(2025, 1, 1, 0, 0, 0)
print(f"\nNew Year 2025: {new_year}")

# Creating time objects
lunch = time(12, 30)
print(f"\nLunch time: {lunch}")

# =============================================================================
# WORKING WITH TIMEDELTA
# =============================================================================
print("\n--- Working with Timedelta ---\n")

now = datetime.now()

# Add/subtract time
one_week_later = now + timedelta(weeks=1)
three_days_ago = now - timedelta(days=3)
in_2_hours = now + timedelta(hours=2)

print(f"Now: {now}")
print(f"One week later: {one_week_later}")
print(f"Three days ago: {three_days_ago}")
print(f"In 2 hours: {in_2_hours}")

# Calculate duration between two dates
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
duration = end_date - start_date

print(f"\nDays in 2024: {duration.days}")
print(f"Total seconds: {duration.total_seconds()}")
print(f"Weeks: {duration.days / 7:.1f}")

# Combined timedelta
complex_duration = timedelta(days=1, hours=2, minutes=30)
print(f"\nComplex duration: {complex_duration}")

# =============================================================================
# FORMATTING DATES
# =============================================================================
print("\n--- Formatting Dates (strftime) ---\n")

now = datetime.now()

# Various formats
formats = [
    ("%Y-%m-%d", "ISO Date"),
    ("%d/%m/%Y", "European Date"),
    ("%m/%d/%Y", "US Date"),
    ("%B %d, %Y", "Full Date"),
    ("%A, %B %d", "Weekday and Date"),
    ("%H:%M:%S", "24-hour Time"),
    ("%I:%M %p", "12-hour Time"),
    ("%Y-%m-%d %H:%M:%S", "Full Timestamp"),
]

for fmt, description in formats:
    print(f"{description:20}: {now.strftime(fmt)}")

# =============================================================================
# PARSING DATES
# =============================================================================
print("\n--- Parsing Dates (strptime) ---\n")

date_strings = [
    ("2024-03-15", "%Y-%m-%d"),
    ("15/03/2024", "%d/%m/%Y"),
    ("March 15, 2024", "%B %d, %Y"),
    ("15-03-2024 14:30:00", "%d-%m-%Y %H:%M:%S"),
]

for date_str, fmt in date_strings:
    parsed = datetime.strptime(date_str, fmt)
    print(f"'{date_str}' -> {parsed}")

# ISO format parsing
iso_date = "2024-03-15T14:30:00"
parsed_iso = datetime.fromisoformat(iso_date)
print(f"\nISO format '{iso_date}' -> {parsed_iso}")

# =============================================================================
# TIMEZONE HANDLING
# =============================================================================
print("\n--- Timezone Handling ---\n")

# Create timezone-aware datetime
utc_now = datetime.now(ZoneInfo("UTC"))
print(f"UTC now: {utc_now}")

# Different timezones
timezones = [
    "America/New_York",
    "America/Los_Angeles",
    "Europe/London",
    "Europe/Paris",
    "Asia/Tokyo",
    "Australia/Sydney",
]

print("\nCurrent time in different cities:")
for tz_name in timezones:
    tz_time = utc_now.astimezone(ZoneInfo(tz_name))
    print(f"  {tz_name:25}: {tz_time.strftime('%Y-%m-%d %H:%M %Z')}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n--- Practical Examples ---\n")

# Example 1: Age Calculator
def calculate_age(birth_date):
    """Calculate age in years from birth date."""
    today = date.today()
    years = today.year - birth_date.year
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1
    return years

birth_date = date(1990, 5, 15)
age = calculate_age(birth_date)
print(f"Born {birth_date}: {age} years old")

# Example 2: Countdown to Event
def days_until(event_date):
    """Calculate days until an event."""
    today = date.today()
    delta = event_date - today
    return delta.days

christmas = date(2025, 12, 25)
days = days_until(christmas)
print(f"\nDays until Christmas 2025: {days}")

# Example 3: Business Days Calculator (simplified)
def add_business_days(start_date, days):
    """Add business days (Mon-Fri) to a date."""
    current = start_date
    added = 0
    while added < days:
        current += timedelta(days=1)
        if current.weekday() < 5:  # Monday = 0, Friday = 4
            added += 1
    return current

today_date = date.today()
future_business = add_business_days(today_date, 10)
print(f"\n10 business days from today: {future_business}")

# Example 4: Meeting Scheduler Across Timezones
def schedule_meeting(utc_time, attendees_timezones):
    """Show meeting time in different timezones."""
    print(f"\nMeeting scheduled for (UTC): {utc_time}")
    print("Local times:")
    for tz_name in attendees_timezones:
        local_time = utc_time.astimezone(ZoneInfo(tz_name))
        print(f"  {tz_name:20}: {local_time.strftime('%Y-%m-%d %H:%M %Z')}")

meeting_utc = datetime(2025, 6, 15, 14, 0, 0, tzinfo=ZoneInfo("UTC"))
attendees = ["America/New_York", "Europe/London", "Asia/Tokyo"]
schedule_meeting(meeting_utc, attendees)

# Example 5: Timestamp Conversion
def timestamp_to_datetime(timestamp):
    """Convert Unix timestamp to datetime."""
    return datetime.fromtimestamp(timestamp)

def datetime_to_timestamp(dt):
    """Convert datetime to Unix timestamp."""
    return int(dt.timestamp())

current_timestamp = int(datetime.now().timestamp())
print(f"\nCurrent timestamp: {current_timestamp}")
converted = timestamp_to_datetime(current_timestamp)
print(f"Converted back: {converted}")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
