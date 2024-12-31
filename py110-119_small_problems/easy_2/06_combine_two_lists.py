'''
Write a function that combines two lists passed as arguments and returns a
new list that contains all elements from both list arguments, with each
element taken in alternation.

You may assume that both input lists are non-empty, and that they have
the same number of elements.
'''

def interleave(lst1, lst2):
    new_lst = []
    for index, lst1_element in enumerate(lst1):
         new_lst.append(lst1_element)
         for _ in lst2:
              new_lst.append(lst2[index])
              break
    return new_lst


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

'''Further Exploration

Can you solve this problem using the zip function?'''
def interleave(lst1, lst2):
    return [ elem for sublist in zip(lst1, lst2) for elem in sublist ]

print(interleave(list1, list2) == expected)
