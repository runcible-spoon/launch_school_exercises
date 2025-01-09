'''
Rotation (Part 1)

Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

    If the input is an empty list, return an empty list.
    If the input is not a list, return None.

Review the test cases below, then implement the solution accordingly.
All of these examples should print True'''

def rotate_list(lst=None):
    if lst is None or type(lst) is not list:
        return None

    if not lst:
        return lst

    rotated_lst = []
    for elem in lst[1:]:
        rotated_lst.append(elem)
    rotated_lst.append(lst[0])

    return rotated_lst

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
