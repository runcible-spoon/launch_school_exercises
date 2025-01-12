'''
Merge Sorted Lists

Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in ascending sorted order. You may assume that the lists contain either all integer values or all string values.

You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.
'''

'''
Problem:
- input: two lists of any lengths that contain either all integers or all strings. each list comes pre-sorted
- output: a single new sorted list built by individually adding elements from each list, not by adding one list to the other and sorting


Data structure:
- dictionaries where index is key, list element is value for both input lists
- new list

Algorithm:
- if either list is empty, return both lists added to each other
- list1 index, list2 index = 0
- while length(new list) < len(list1) +  len(list2):
    - if one_dict[one_index] < two_dict[two_index]:
        - append one_dict[one_index] to new_list
        - if one_index < len(lst1):
            - one_index += 1
    - else:
        - append two_dict[two_index] to new list
        - if two_index < len(lst2):
            - two_index += 1
    - increment the index of the list with the lower element by one

- return the new list
'''


def merge(lst1, lst2):
    if not lst1 or not lst2:
        return lst1 + lst2

    new_list = []

    one_dict = {index: lst1[index] for index in range(len(lst1))}
    two_dict = {index: lst2[index] for index in range(len(lst2))}

    one_index = 0
    two_index = 0

    hit_end_of_list = False

    while len(new_list) < len(lst1) + len(lst2):

        if one_dict[one_index] < two_dict[two_index]:

            if hit_end_of_list:
                new_list.extend(lst2[two_index:])
                break

            new_list.append(one_dict[one_index])

            if (one_index, lst1[one_index]) != list(one_dict.items())[-1]:
                one_index += 1

            else:
                hit_end_of_list = True

        else:
            if hit_end_of_list:
                new_list.extend(lst1[one_index:])
                break

            new_list.append(two_dict[two_index])

            if (two_index, lst2[two_index]) != list(two_dict.items())[-1]:
                two_index += 1

            else:
                hit_end_of_list = True

    return new_list


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)
