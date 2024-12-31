'''
You come across the following code. 

What errors does it raise for the given examples and what exactly do the error messages mean?
'''

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

# error message:
# TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given

# as written. "numbers" doesn't mean more than one arg. if you want more, either comma them out or take a list as an arg.
