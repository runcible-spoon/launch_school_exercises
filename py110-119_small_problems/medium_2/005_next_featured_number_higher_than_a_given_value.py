'''
Next Featured Number Higher than a Given Value

A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each.
For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

NOTE: The largest possible featured number is 9876543201.
'''

'''
Problem:
- input: integer
- output: the integer that is next in the sequence of numbers that satisfies all three conditions:
    - 1) odd
    - 2) multiple of seven
    - 3) each digit is unique
    - 4) is not larger than 9876543201

Data structure:
- num is continually added to or otherwise anipulated until reaching final state where it evaluates as a 'featured number'

Algorithm:
- Take num as input
- If num is > the maximum possible featured number:
    - return error msg
- while True:
    - add 1 to num, in case num is already a featured num

    - if resulting num is even:
        - add 1

    - If num is not divisible by 7:
        - integer divide number by seven
        - add 1 to result
        - multiply result by 7

    - if num is divisible by 7, is odd, and all digits are unique:
        - return num

'''

#LS solution
def to_odd_multiple_of_7(number):
    number += 1
    while number % 2 == 0 or number % 7 != 0:
        number += 1

    return number

def all_unique(number):
    digits = list(str(number))
    return len(digits) == len(set(digits))

def next_featured(number):
    MAX_FEATURED = 9876543201
    featured_num = to_odd_multiple_of_7(number)

    while featured_num <= MAX_FEATURED:
        if all_unique(featured_num):
            return featured_num

        featured_num += 14

    return "There is no possible number that fulfills those requirements."

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True

print(next_featured(1029) == 1043)              # True
print(next_featured(999_999) == 1_023_547)         # True
print(next_featured(999_999_987) == 1_023_456_987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
