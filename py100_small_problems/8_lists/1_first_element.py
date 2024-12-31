'''
Write a function that returns the first element of a 
list provided as an argument. For example:
'''

def first(list):
    if list:
        return list[0]
    else:
        return None


print(first(['Earth', 'Moon', 'Mars']))  # Earth
