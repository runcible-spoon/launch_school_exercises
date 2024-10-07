'''
Write a function that returns the next to last word in the string argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two words.
'''

def penultimate(str):
    words = str.split(' ')
    if len(words) <= 2:
        return words[0]
    else:
        return words[-2]
    
# ls: doesn't need conditional

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
