'''
Multiply List

You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.
'''

# original

'''def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])'''


# bug: doing augmented assignment on lst's items.
# debugged

def multiply_list(lst):
    return [ num * 2 for num in lst ]

print(multiply_list([1, 2, 3]) == [2, 4, 6])
