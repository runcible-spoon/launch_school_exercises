'''
Shadow

We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?

Original:

def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)

Bug: shadowing builtin sum function

Debugged:'''

def sum_factors(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_factors(numbers, 2) == 20)
