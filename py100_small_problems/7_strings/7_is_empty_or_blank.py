'''
Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. For example:
'''

def is_empty_or_blank(string):
    return False if string.isalnum() else True

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
