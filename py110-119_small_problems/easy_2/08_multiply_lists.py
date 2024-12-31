'''
Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains
the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain
the same number of elements.
'''

def multiply_list(lst1, lst2):
    product_list = []

    for lst1_idx, num in enumerate(lst1):
        product_list.append(num * lst2[lst1_idx])

    return product_list


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
