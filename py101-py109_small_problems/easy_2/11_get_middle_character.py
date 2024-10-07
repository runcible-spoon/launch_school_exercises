'''
Write a function that takes a non-empty non_empty_string argument and returns the 
middle character(s) of the non_empty_string. If the non_empty_string has an odd length, you 
should return exactly one character. If the non_empty_string has an even length, 
you should return exactly two characters.
'''

def center_of(string):
    length_is_odd = len(string) % 2 != 0
    
    string_elements = list(string)

    middle_character = string_elements[(len(string) // 2)]
    middle_character_minus_one = string_elements[(len(string) // 2) - 1]
    
    return middle_character if length_is_odd else middle_character_minus_one + middle_character



print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
