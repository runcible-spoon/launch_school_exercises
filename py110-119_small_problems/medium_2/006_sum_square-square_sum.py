'''
Sum Square - Square Sum

Write a function that computes the difference between
the square of the sum of the first count positive integers and
the sum of the squares of the first count positive integers.
'''

def sum_square_difference(num):
    num_range = range(1, num + 1)
    return (sum(num_range)**2) - sum([num**2 for num in num_range])

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

'''
Further Exploration
What will happen if you replace sum_ with sum every place it occurs?
'''

def sum_square_difference(count):
    sum = sum(range(1, count + 1))

    sum_of_squares = 0
    for i in range(1, count + 1):
        sum_of_squares += i**2

    return sum**2 - sum_of_squares

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

'''
UnboundLocalError: cannot access local variable 'sum' where it is not associated with a value

function sum() is now shadowed by variable sum and python interprets function calls as variable references.
'''
