'''Write a function that takes a year as input and returns the century. 
The return value should be a string that begins with the century number, 
and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000 
comprise the 20th century.
Examples'''



'''

numbers that receive st, nd, or rd:
1, 2, 3, 21, 22, 23, 31, 32, 33, ....



'''



def century(year):
    
    suffix1 = 'st'
    suffix2 = 'nd'
    suffix3 = 'rd'
    suffix_n = 'th'
    
    if year % 100 == 0:
        century = str(year // 100)
    else:
        century = str((year // 100) + 1)

    last_digit = int(century[-1])

    if len(century) == 1:
        if last_digit == 1:
            return(f'{century}{suffix1}')
        elif last_digit == 2:
            return(f'{century}{suffix2}')
        elif last_digit == 3:
            return(f'{century}{suffix3}')
        else:
            return(f'{century}{suffix_n}')
    else:
        if int(century[-2]) == 1:
            return(f'{century}{suffix_n}')
        else:
            if last_digit == 1:
                return(f'{century}{suffix1}')
            elif last_digit == 2:
                return(f'{century}{suffix2}')
            elif last_digit == 3:
                return(f'{century}{suffix3}')
            else:
                return(f'{century}{suffix_n}')





print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
