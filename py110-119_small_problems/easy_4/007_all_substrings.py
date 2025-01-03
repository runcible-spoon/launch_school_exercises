'''
All Substrings

Write a function that returns a list of all substrings of a string.
Order the returned list by where in the string the substring begins.

This means that all substrings that start at index position 0 should come first,
then all substrings that start at index position 1, and so on.

Since multiple substrings will occur at each position,
return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:
'''

def leading_substrings(string):
    return [ string[:index + 1] for index in range(len(string)) ]

def substrings(string):
    return [ substring for index in range(len(string)) for substring in leading_substrings(string[index:]) ]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
