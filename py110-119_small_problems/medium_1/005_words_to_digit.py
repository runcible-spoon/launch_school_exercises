'''
Word to Digit

Write a function that takes a string as an argument and returns that string with every occurrence of a "number word"
-- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.
'''

def word_to_digit(string):
    number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    split_string = string.split()

    new_string = []

    for word in split_string:
        if word in number_words:
            new_string.append(str(number_words.index(word)))
        else:
            new_string.append(word)

    return ' '.join( new_string )

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4") # Should print True

'''Further Exploration
Can you solve this problem if the individual words can end with punctuation?

You can get the list of all punctuation characters from the string.punctuation variable in the string module
This is trickier than it sounds. This is a problem where regular expressions can greatly simplify the solution. If you're interested, you can read our Regular Expressions book.'''

import string

NUMBER_WORDS = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
PUNCTUATION = tuple(string.punctuation)

def word_to_digit(string):
    split_string = string.split()
    new_string = []

    for word in split_string:
        if word in NUMBER_WORDS:
            new_string.append(str(NUMBER_WORDS.index(word)))
        elif word.endswith(PUNCTUATION) and word[:-1] in NUMBER_WORDS:
                     new_string.append(f'{str(NUMBER_WORDS.index(word[:-1]))}{word[-1]}')
        else:
            new_string.append(word)

    return ' '.join(new_string)


message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.") # Should print True
