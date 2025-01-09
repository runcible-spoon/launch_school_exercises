'''
Mutable Default Arguments

We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly.

How would you fix this code?

original:

def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])


# bug: both print statements are referencing the same list
# debugged:'''

def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
