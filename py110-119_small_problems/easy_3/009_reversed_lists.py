'''
Reversed Lists

Write a function that takes a list as an argument and reverses its elements, in place.
That is, mutate the list passed into the function.
The returned object should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).
'''

def reverse_list(lst):
    reverse_indices = [ num - 1 for num in (range(len(lst), 0, -1)) ]

    staging_lst = []
    for idx in reverse_indices:
        staging_lst.append(lst[idx])

    lst.clear()

    for elem in staging_lst:
        lst.append(elem)

    return lst

'''list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True'''


# ls

def reverse_list(lst):
    first = 0
    last = -1

    while first < (len(lst)):
        lst[first], lst[last] = lst[last], lst[first]
        print(f'lst[first] {first} {lst[first]}, lst[last] {last} {lst[last]} = lst[last] {last} {lst[last]}, lst[first] {first} {lst[first]}')
        first += 1
        last -= 1
        print(lst)

    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True
