'''
Write a function that checks whether a string is empty or not. For example:
'''

def is_empty(string):
    return False if string else True


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True
