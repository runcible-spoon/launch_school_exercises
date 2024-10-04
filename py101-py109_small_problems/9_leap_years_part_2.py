'''
In the previous exercise, we assumed that the Gregorian calendar has been 
in continuous use since the year 1. However, the Gregorian calendar 
wasn't adopted until much later; prior to that, much of the world used
the Julian calendar, which observed leap year every 4 years.

in 1752, England, Ireland, and the British colonies all switched to 
the Gregorian calendar. Update the function from the previous exercise 
so it uses the Julian calendar prior to 1752, and the Gregorian calendar 
starting in 1752.
'''

def is_leap_year(year):
    year = abs(int(year))

    if year < 1752:
        return True if year % 4 == 0 else False
    else:
        return True if (
            (year % 400 == 0) or 
            ((year % 4 == 0) and (year % 100 != 0))
        ) else False


# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)

'''
Further Exploration

Different regions adopted the Gregorian calendar at different times. 
Investigate when it was adopted in various countries and how that transition 
was managed. Consider how this would impact the leap year calculation and 
potentially adjust the solution based on the country of reference.

'''
