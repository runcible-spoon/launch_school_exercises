'''
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.
'''

def repeater(string):
    return ''.join([ char + char for char in string ])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")
