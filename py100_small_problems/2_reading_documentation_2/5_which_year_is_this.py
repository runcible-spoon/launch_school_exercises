'''
The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.
'''
from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]
'''
What is the difference between the year attribute and the isocalendar method?
'''

print(today_year, iso_year)

# iso_year is taking date.today() as an input for isocalendar() at position zero in its named tuple: year, week weekday.

# LS solution: the ISO calendar is also different from Gregorian.
