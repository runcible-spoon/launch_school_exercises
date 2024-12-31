'''
The destinations list contains a list of travel destinations.
'''
'''
Write a function that, without using the built-in in operator, 
checks whether a specific destination is included within destinations. 

For example: When checking whether 'Barcelona' is contained in destinations, 
the expected output is True, whereas the expected output for 
'Nashville' is False.
'''


destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']



def contains(element, lst):
    for item in lst:
        if item == element:
            return True

    return False


print(contains(destinations, 'Barcelona'))
print(contains(destinations, 'Nashville')) 
