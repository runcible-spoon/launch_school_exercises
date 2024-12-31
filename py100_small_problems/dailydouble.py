# Write a function that takes a string argument and returns a 
# new string that contains the value of the original string 
# with all consecutive duplicate characters collapsed into 
# a single character

'''
P (Understand the Problem)
Input: string
Output: string

Consecutive duplicate characters:
is the next character the same as the current character?

Collapsed into single char: 
Keep just one of the consecutive duplicate characters

Find consecutive duplicate values and remove all but 1 of them. 
Return the remaining values as a string.

E (Examples and test cases)
Rules: 
    - do not remove non-consecutive repeated characters
    - rules apply to all char types (e.g., digits, letters)
    - case irrelevant
    - spaces are chars
    - if input empty, return empty str
    - order of characters must be preserved 

D (Data structure)
- List of characters from input string
- list to store characters for the output string


A (Algorithm)
Step by step: 
    - Create an empty list, output
    - Iterate over the input current_char
    - Check if current_char is the same as the last item in output
    - If they're different, append current_char to output
    - Convert the output to a string and return it
'''

def crunch(string):
    output = []

    for character in string:
        if len(output) == 0:
            output.append(character)
        elif character != output[-1]:
            output.append(character)

    return ''.join(output)
