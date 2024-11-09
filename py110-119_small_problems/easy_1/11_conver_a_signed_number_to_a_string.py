
'''
In the previous exercise, you developed a function that converts 
non-negative numbers to strings. In this exercise, you're going to 
extend that function by adding the ability to represent negative 
numbers as well.

Write a function that takes an integer and converts it to a string 
representation.

You may not use any of the standard conversion functions available in 
Python, such as str. You may, however, use integer_to_string from the 
previous exercise.
'''

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def signed_integer_to_string(number):
    result = ''

    negative = False

    if number < 0:
        negative = True

    if number == 0:
        return '0'

    number = abs(number)
    
    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return '+' + result if not negative else '-' + result



print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True


# ls 

def signed_integer_to_string(number):
    if number < 0:
        return f"-{integer_to_string(-number)}"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return "0"
