'''
What happens if we take the list ['fish', 'and', 'chips'] and try to access the element at index position 10? 
First try to determine what will happen by consulting the documentation, 
then verify your understanding in the Python REPL.
'''

fish_list = ['fish', 'and', 'chips']

# raises ValueError. Avoid by asking python if element in list first

print(fish_list.index(10))
# ValueError: 10 is not in list


# WRONG

# Not ValueError, IndexError. Done through bracket notation.

print(fish_list[10])
# IndexError: list index out of range
