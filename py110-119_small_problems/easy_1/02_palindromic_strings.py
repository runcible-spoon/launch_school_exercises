'''
Write a function that returns True if the string passed as an argument 
is a palindrome, False otherwise. 

A palindrome reads the same forwards and backwards. 

For this problem, the case matters and all characters matter.
'''


def string_length_even(string):
    return len(string) % 2 == 0

def divide_string(string):
    half_string = len(string) // 2

    first_half = string[0:half_string]

    if string_length_even(string):
        second_half = string[half_string:]
    else:
        second_half = string[half_string + 1:]
    
    return first_half, second_half

def are_halves_equal(first_half, second_half):
    return first_half == second_half[::-1]

def is_palindrome(string):
    return are_halves_equal(*divide_string((string)))

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)


# ls solution

def is_palindrome(s):
    return s == s[::-1]
