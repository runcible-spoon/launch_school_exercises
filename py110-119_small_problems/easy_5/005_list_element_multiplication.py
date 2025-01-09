'''
List Element Multiplication

Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.
'''

def multiply_items(lst1, lst2):
    return [ lst1[idx] * lst2[idx] for idx in range(len(lst1)) ]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True
