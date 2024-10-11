'''Given a string that consists of some words and an assortment of 
non-alphabetic characters, write a function that returns that string 
with all of the non-alphabetic characters replaced by spaces. 

If one or more non-alphabetic characters occur in a row, you should 
nly have one space in the result (i.e., the result string should 
never have consecutive spaces).
'''

def clean_up(string):
    clean_string = ''
    for char in string:
        if char.isalpha():
            clean_string += char
        else:
            clean_string += ' '
    

    previous_char = ''
    space_stripped_string = ''

    for char in clean_string:
        if char != previous_char:
            space_stripped_string += char

        previous_char = char

    return(space_stripped_string)


print(clean_up("---what's my +*& line?") == " what s my line ") # True
