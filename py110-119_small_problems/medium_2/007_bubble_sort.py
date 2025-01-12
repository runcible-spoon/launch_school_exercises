'''
Bubble Sort

Bubble Sort is one of the simplest sorting algorithms available. It is not an efficient algorithm, so developers rarely use it in real code.
However, it is an excellent exercise for student developers. In this exercise, you will write a function that sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list.
On each pass, the two values of each pair of consecutive elements are compared.
If the first value is greater than the second, the two elements are swapped.
This process is repeated until a complete pass is made without performing any swaps.
At that point, the list is completely sorted.

6 	2 	7 	1 	4 	Start: compare 6 > 2? Yes
2 	6 	7 	1 	4 	Swap
2 	6 	7 	1 	4 	6 > 7? No (no swap)
2 	6 	7 	1 	4 	7 > 1? Yes
2 	6 	1 	7 	4 	Swap
2 	6 	1 	7 	4 	7 > 4? Yes
2 	6 	1 	4 	7 	Swap

2 	6 	1 	4 	7 	2 > 6? No
2 	6 	1 	4 	7 	6 > 1? Yes
2 	1 	6 	4 	7 	Swap
2 	1 	6 	4 	7 	6 > 4? Yes
2 	1 	4 	6 	7 	Swap
2 	1 	4 	6 	7 	6 > 7? No

2 	1 	4 	6 	7 	2 > 1? Yes
1 	2 	4 	6 	7 	Swap
1 	2 	4 	6 	7 	2 > 4? No
1 	2 	4 	6 	7 	4 > 6? No
1 	2 	4 	6 	7 	6 > 7? No

1 	2 	4 	6 	7 	1 > 2? No
1 	2 	4 	6 	7 	2 > 4? No
1 	2 	4 	6 	7 	4 > 6? No
1 	2 	4 	6 	7 	6 > 7? No
1 	2 	4 	6 	7 	No swaps; all done; sorted

We can stop iterating the first time we make a pass through the list without making any swaps since that means the entire list is sorted.

For further information -- including pseudo-code that demonstrates the algorithm, as well as a minor optimization technique -- see the Bubble Sort Wikipedia page.

Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above.
The sorting should be done "in-place" -- that is, the function should mutate the list.
You may assume that the list contains at least two elements.
'''

'''
Problem:
- input: list of sortable values with at least two elements
- output: mutated list, sorted

Data structure:
- work with original list

Algorithm:
- Sorted list = any element > next element
- While list is not sorted:
    for element, next element in lst:
        - if element > next element:
            - element lst position = next element lst position
            - next element lst position = element lst position
- return sorted list
'''

'''def bubble_sort(lst):
    length = len(lst)

    while True:
        swapped = False
        for i in range(length - 1):
            current = lst[i]
            nxt = lst[i + 1]

            if current <= nxt:
                continue

            current, nxt = nxt, current
            swapped = True

        if not swapped:
            break'''

# LS solution
def bubble_sort(lst):
    while True:
        swapped = False
        for idx in range(1, len(lst)):
            if lst[idx - 1] <= lst[idx]:
                continue

            lst[idx - 1], lst[idx] = lst[idx], lst[idx - 1]
            swapped = True

        if not swapped:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True
