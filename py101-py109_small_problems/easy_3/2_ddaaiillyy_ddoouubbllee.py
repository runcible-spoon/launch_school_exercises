'''Write a function that takes a string argument and returns a new string 
that contains the value of the original string with all consecutive duplicate 
characters collapsed into a single character.
'''

def crunch(text):
    new_text = ''
    previous_char = ''

    for char in text:
        if char != previous_char:
            new_text += char
        previous_char = char

    return new_text




# These examples should all print True
print(crunch('abc') == 'abc')
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
