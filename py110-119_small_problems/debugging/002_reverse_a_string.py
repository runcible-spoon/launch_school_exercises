'''
Reverse a String

You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected output. Explain the bug, and provide a solution.
'''

# original

'''
def reverse_string(string):
    for char in string:
        string = char + string

    return string

print(reverse_string("hello") == "olleh")
'''

# bug: we're prepending the iterated-to character to the full string with each loop. we're left with a reversed string followed by the original.

# debugged

def reverse_string(string):
    new_str = []
    for char in string:
        new_str.insert(0, char)

    return ''.join(new_str)


print(reverse_string("hello") == "olleh")
