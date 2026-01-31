"""
Datetime Module - Exercises
===========================
Practice problems for working with dates and times.
"""

print("=" * 60)
print("DATETIME MODULE - Exercises")
print("=" * 60)

from datetime import datetime, date, time, timedelta
from zoneinfo import ZoneInfo

# =============================================================================
# EXERCISE 1: Days Between Dates
# =============================================================================
print("\n--- Exercise 1: Days Between Dates ---\n")
"""
Write a function that calculates the number of days between two dates.

Example:
    days_between(date(2024, 1, 1), date(2024, 1, 10)) -> 9
"""

def days_between(date1, date2):
    """
    Calculate the absolute number of days between two dates.
    """
    # Your code here
    pass  # TODO: Implement

# Test
# print(days_between(date(2024, 1, 1), date(2024, 1, 10)))
# print(days_between(date(2024, 3, 1), date(2024, 3, 15)))

# =============================================================================
# EXERCISE 2: Date Parser
# =============================================================================
print("\n--- Exercise 2: Date Parser ---\n")
"""
Write a function that can parse dates in various formats and return
a standard datetime object.

Supported formats:
    - "2024-03-15" (YYYY-MM-DD)
    - "15/03/2024" (DD/MM/YYYY)
    - "March 15, 2024" (Month DD, YYYY)
    - "15-Mar-2024" (DD-Mon-YYYY)

If the format is not recognized, return None.
"""

def parse_date(date_string):
    """
    Parse a date string in various formats and return a datetime object.
    Returns None if format is not recognized.
    """
    # Your code here
    # Try different formats using strptime
    pass  # TODO: Implement

# Test
# print(parse_date("2024-03-15"))
# print(parse_date("15/03/2024"))
# print(parse_date("March 15, 2024"))
# print(parse_date("15-Mar-2024"))
# print(parse_date("not a date"))

# =============================================================================
# EXERCISE 3: Time Until Birthday
# =============================================================================
print("\n--- Exercise 3: Time Until Birthday ---\n")
"""
Write a function that calculates how many days until the next occurrence
of a given birthday.

If the birthday has already passed this year, calculate for next year.

Example:
    If today is March 1, 2024:
    - time_until_birthday(date(1990, 5, 15)) -> days until May 15, 2024
    - time_until_birthday(date(1990, 2, 15)) -> days until Feb 15, 2025
"""

def time_until_birthday(birth_date):
    """
    Calculate days until the next occurrence of this birth date.
    birth_date is a date object.
    """
    # Your code here
    # Get today's date
    # Check if birthday has passed this year
    # Calculate days until next birthday
    pass  # TODO: Implement

# Test (adjust based on current date)
# print(time_until_birthday(date(1990, 12, 25)))
# print(time_until_birthday(date(1990, 1, 1)))

# =============================================================================
# EXERCISE 4: Work Hours Calculator
# =============================================================================
print("\n--- Exercise 4: Work Hours Calculator ---\n")
"""
Given a list of (start_time, end_time) tuples representing work sessions,
calculate the total hours worked.

Times are strings in "HH:MM" 24-hour format.

Example:
    work_sessions = [
        ("09:00", "17:00"),
        ("09:00", "12:30"),
    ]
    result: 11.5 hours
"""

def calculate_work_hours(work_sessions):
    """
    Calculate total hours from a list of (start, end) time tuples.
    Times are in "HH:MM" format.
    """
    # Your code here
    # Parse each time string
    # Calculate duration for each session
    # Sum all durations and convert to hours
    pass  # TODO: Implement

# Test
# sessions = [("09:00", "17:00"), ("09:00", "12:30"), ("13:00", "18:00")]
# print(calculate_work_hours(sessions))

# =============================================================================
# EXERCISE 5: Meeting Scheduler
# =============================================================================
print("\n--- Exercise 5: Meeting Scheduler ---\n")
"""
Write a function that finds available meeting slots given:
- A list of busy periods (start_datetime, end_datetime)
- Meeting duration (in minutes)
- Search range (start_date, end_date)
- Working hours (start_hour, end_hour)

Return a list of available slots (datetime, datetime) within working hours.
"""

def find_available_slots(busy_periods, duration_minutes,
                         search_start, search_end,
                         work_start_hour=9, work_end_hour=17):
    """
    Find available meeting slots.

    Args:
        busy_periods: List of (start, end) datetime tuples
        duration_minutes: Required meeting duration
        search_start, search_end: Date range to search
        work_start_hour, work_end_hour: Working hours

    Returns:
        List of (start, end) datetime tuples for available slots
    """
    # Your code here
    # This is a challenging problem!
    # Hint: Create time slots and check against busy periods
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 6: Age in Different Units
# =============================================================================
print("\n--- Exercise 6: Age in Different Units ---\n")
"""
Write a function that calculates age from a birth date and returns it in:
- Years
- Months (approximate)
- Days
- Hours
- Minutes

Return a dictionary with all these values.
"""

def detailed_age(birth_date):
    """
    Calculate detailed age information from birth date.
    Returns a dictionary with years, months, days, hours, minutes.
    """
    # Your code here
    # Calculate years
    # Estimate months
    # Calculate exact days, hours, minutes
    pass  # TODO: Implement

# Test
# birth = date(1990, 5, 15)
# print(detailed_age(birth))

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# =============================================================================
# SOLUTION 1: Days Between Dates
# =============================================================================
print("\n--- Solution 1: Days Between Dates ---\n")

def days_between_solution(date1, date2):
    return abs((date2 - date1).days)

print(days_between_solution(date(2024, 1, 1), date(2024, 1, 10)))
print(days_between_solution(date(2024, 3, 1), date(2024, 3, 15)))

# =============================================================================
# SOLUTION 2: Date Parser
# =============================================================================
print("\n--- Solution 2: Date Parser ---\n")

def parse_date_solution(date_string):
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%d-%b-%Y",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    return None

print(parse_date_solution("2024-03-15"))
print(parse_date_solution("15/03/2024"))
print(parse_date_solution("March 15, 2024"))
print(parse_date_solution("15-Mar-2024"))
print(parse_date_solution("not a date"))

# =============================================================================
# SOLUTION 3: Time Until Birthday
# =============================================================================
print("\n--- Solution 3: Time Until Birthday ---\n")

def time_until_birthday_solution(birth_date):
    today = date.today()
    next_birthday = birth_date.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    return (next_birthday - today).days

print(f"Days until Dec 25: {time_until_birthday_solution(date(1990, 12, 25))}")
print(f"Days until Jan 1: {time_until_birthday_solution(date(1990, 1, 1))}")

# =============================================================================
# SOLUTION 4: Work Hours Calculator
# =============================================================================
print("\n--- Solution 4: Work Hours Calculator ---\n")

def calculate_work_hours_solution(work_sessions):
    total_seconds = 0

    for start_str, end_str in work_sessions:
        start = datetime.strptime(start_str, "%H:%M")
        end = datetime.strptime(end_str, "%H:%M")
        duration = end - start
        total_seconds += duration.total_seconds()

    return total_seconds / 3600  # Convert to hours

sessions = [("09:00", "17:00"), ("09:00", "12:30"), ("13:00", "18:00")]
print(f"Total hours: {calculate_work_hours_solution(sessions):.1f}")

# =============================================================================
# SOLUTION 5: Meeting Scheduler (Simplified)
# =============================================================================
print("\n--- Solution 5: Meeting Scheduler ---\n")

def find_available_slots_solution(busy_periods, duration_minutes,
                                   search_start, search_end,
                                   work_start_hour=9, work_end_hour=17):
    duration = timedelta(minutes=duration_minutes)
    available_slots = []

    current_date = search_start
    while current_date <= search_end:
        # Create working hours for this day
        day_start = datetime.combine(current_date, time(work_start_hour, 0))
        day_end = datetime.combine(current_date, time(work_end_hour, 0))

        # Simple approach: check middle of day if not busy
        slot_start = day_start
        while slot_start + duration <= day_end:
            slot_end = slot_start + duration

            # Check if slot conflicts with busy periods
            is_available = True
            for busy_start, busy_end in busy_periods:
                if slot_start < busy_end and slot_end > busy_start:
                    is_available = False
                    break

            if is_available:
                available_slots.append((slot_start, slot_end))
                break  # Just find one per day for simplicity

            slot_start += timedelta(minutes=30)

        current_date += timedelta(days=1)

    return available_slots

# Test
busy = [
    (datetime(2024, 6, 1, 9, 0), datetime(2024, 6, 1, 11, 0)),
    (datetime(2024, 6, 1, 14, 0), datetime(2024, 6, 1, 16, 0)),
]
slots = find_available_slots_solution(busy, 60, date(2024, 6, 1), date(2024, 6, 3))
print(f"Available 1-hour slots: {slots}")

# =============================================================================
# SOLUTION 6: Age in Different Units
# =============================================================================
print("\n--- Solution 6: Age in Different Units ---\n")

def detailed_age_solution(birth_date):
    today = date.today()

    # Calculate years
    years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1

    # Calculate total days
    total_days = (today - birth_date).days

    # Estimate months
    months = years * 12 + today.month - birth_date.month
    if today.day < birth_date.day:
        months -= 1

    # Calculate hours and minutes
    hours = total_days * 24
    minutes = hours * 60

    return {
        "years": years,
        "months": months,
        "days": total_days,
        "hours": hours,
        "minutes": minutes,
    }

birth = date(1990, 5, 15)
age_info = detailed_age_solution(birth)
for unit, value in age_info.items():
    print(f"  {unit}: {value:,}")

print("\n" + "=" * 60)
print("Exercises complete!")
print("=" * 60)
