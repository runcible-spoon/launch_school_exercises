'''
Write a function that checks whether a string starts with a specific prefix.
'''

def starts_with(string, string_prefix):
    return True if string_prefix in string else False


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

# or,,,,

def starts_with(string, string_prefix):
    return string.startswith(string_prefix)
