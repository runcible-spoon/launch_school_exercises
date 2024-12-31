def max_sequence(array):
    if not array or all(element < 0 for element in array):
        return 0
    else:
        pos_sum = sum([ num for num in array if num > 0 ])
        print(pos_sum)
     #   for i, num in enumerate(array):
     
                


# print(max_sequence([]) == 0)

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)

# print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]) == 0)

# print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]) == 155)
