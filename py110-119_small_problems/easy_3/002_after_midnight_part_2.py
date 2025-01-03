'''
As seen in the previous exercise, the time of day can be represented
as the number of minutes before or after midnight.

If the number of minutes is positive, the time is after midnight.
If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and
return the number of minutes before and after midnight, respectively.
Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.
Disregard Daylight Savings and Standard Time and other irregularities.
'''

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def get_hours_and_minutes(time):
    hours = int(time[:2])
    minutes = int(time[3:])
    return hours, minutes

def after_midnight(time):
    hours, minutes = get_hours_and_minutes(time)
    total = ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY
    return total

def before_midnight(time):
    total = after_midnight(time)
    minutes_to_midnight = MINUTES_PER_DAY - total
    if minutes_to_midnight == MINUTES_PER_DAY:
        minutes_to_midnight = 0

    return minutes_to_midnight

'''print(after_midnight("00:00"), after_midnight("00:00") == 0)     # True
print(before_midnight("00:00"), before_midnight("00:00") == 0)    # True
print(after_midnight("12:34"), after_midnight("12:34") == 754)   # True
print(before_midnight("12:34"), before_midnight("12:34") == 686)  # True
print(after_midnight("24:00"), after_midnight("24:00") == 0)     # True
print(before_midnight("24:00"), before_midnight("24:00") == 0)    # True'''

'''
Further Exploration
How would these functions change if you could use the Python's datetime.datetime class?
'''

from datetime import timedelta

def after_midnight(time):
    hours, minutes = get_hours_and_minutes(time)
    delta = timedelta(hours=hours, minutes=minutes)
    delta


def before_midnight(time):
    hours, minutes = get_hours_and_minutes(time)
    delta = timedelta(hours=hours, minutes=minutes)
    delta


print(after_midnight("00:00"))
print(before_midnight("00:00"))    # True
print(after_midnight("12:34"))   # True
print(before_midnight("12:34"))  # True
print(after_midnight("24:00"))     # True
print(before_midnight("24:00"))    # True
