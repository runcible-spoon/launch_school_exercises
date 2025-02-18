'''
The time of day can be represented as the number of minutes before or after midnight.
If the number of minutes is positive, the time is after midnight.
If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm).
Your function should work with any integer input.

You may not use Python's datetime module.
Disregard Daylight Savings and Standard Time and other complications.
'''

def time_of_day(num):
    if num == 0:
        return "00:00"

    elif num < 0:
        while num < 0:
            num += 1440

    elif num > 0:
        while num > 1440:
            num -= 1440

    hour_component = num // 60
    minute_component = num % 60

    output = f'{hour_component:02d}:{minute_component:02d}'

    return output

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
