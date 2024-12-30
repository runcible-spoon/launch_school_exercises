'''
Write a function that takes a list as an argument and returns a 
list that contains two elements, both of which are lists. Put the 
first half of the original list elements in the first element of 
the return value and put the second half in the second element. 

If the original list contains an odd number of elements, place the 
middle element in the first half list.
'''

def halvsies(lst):
    if len(lst) % 2 != 0:
        half1 = [ elem for elem in lst[:(len(lst) // 2) + 1 ] ]
        half2 = [ elem for elem in lst[len(lst) // 2 + 1: ] ]
    else:
        half1 = [ elem for elem in lst[:len(lst) // 2 ] ]
        half2 = [ elem for elem in lst[len(lst) // 2:] ]

    return [ half1, half2 ]


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
