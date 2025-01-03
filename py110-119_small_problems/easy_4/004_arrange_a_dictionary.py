'''
Arrange a Dictionary

Given a dictionary, return its keys sorted by the values associated with each key.
'''

def get_value(key):
    return my_dict[key]

def order_by_value(dictionary):
    return sorted(list(my_dict.keys()), key=get_value)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
