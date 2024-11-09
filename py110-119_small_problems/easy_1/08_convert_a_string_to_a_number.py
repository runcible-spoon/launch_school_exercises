'''
Write a function that takes a string of digits and returns the 
appropriate number as an integer. You may not use any of the standard 
conversion functions available in Python, such as int. Your function 
should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry 
about invalid characters; assume all characters are numeric.
'''

def string_to_integer(string):
    digits = []
    for char in string:
        char = conversion(char)
        digits.append(char)

    digits_reversed = digits[::-1]

    zeroed_digits = []

    for num in digits_reversed:
        num =  add_zeroes(digits_reversed, num)
        zeroed_digits.append(num)

    return sum(zeroed_digits)

def conversion(digit):
    match digit:
        case '0':
            return 0
        case '1':
            return 1
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9

def add_zeroes(reversed_list, number):
    for idx, num in enumerate(reversed_list):
        if num == number:
            number = number * (10 ** idx)
    
    return number

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True


# ls 

def string_to_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0
    for char in s:
        value = (10 * value) + DIGITS[char]

    return value


'''Further Exploration

Write a hexadecimal_to_integer function that converts a string representing 
a hexadecimal number to its integer value. Hexadecimal numbers use base 
16 instead of 10, and the characters A, B, C, D, E and F (and the lowercase 
equivalents) correspond to decimal values of 10-15.
'''


def hexadecimal_to_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'a': 10,
        'B': 11,
        'b': 11,
        'C': 12,
        'c': 12,
        'D': 13,
        'd': 13,
        'E': 14,
        'e': 14,
        'F': 15,
        'f': 15,
    }

    value = 0
    for char in s:
        value = (16 * value) + DIGITS[char]

    return value


print(hexadecimal_to_integer('4D9f') == 19871)  # True
