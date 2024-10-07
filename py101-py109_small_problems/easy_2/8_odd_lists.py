'''Write a function that returns a list that contains every other element of a 
list that is passed in as an argument. The values in the returned list 
should be those values that are in the 1st, 3rd, 5th, and so on elements 
of the argument list.'''

def oddities(lst):
    odd_list = []
    i = 0
    while i < len(lst):
        if i == 0 or i % 2 == 0:
            odd_list.append(lst[i])
        i += 1
    return odd_list


'''
ls

def oddities(lst):
    result = []
    for idx in range(len(lst)):
        if idx % 2 == 0:
            result.append(lst[idx])

    return result
'''

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True


'''
Bonus question: Try to solve the problem using list slicing.
'''



def odditites_slicing(lst):
    return(list(lst[::2]))


print(odditites_slicing([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(odditites_slicing([1, 2, 3, 4]) == [1, 3])        # True
print(odditites_slicing(["abc", "def"]) == ['abc'])     # True
print(odditites_slicing([123]) == [123])                # True
print(odditites_slicing([]) == [])                      # True


'''
Further Exploration

Write a companion function that returns the 2nd, 4th, 6th, and so on 
elements of a list.

Try to solve this differently from the exercise described above.
'''

def oddities_even(lst):
    return [ i for i in lst if lst.index(i) % 2 != 0 ]

print(oddities_even([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities_even([1, 2, 3, 4]) == [1, 3])        # True
print(oddities_even(["abc", "def"]) == ['abc'])     # True
print(oddities_even([123]) == [123])                # True
print(oddities_even([]) == [])                      # True
