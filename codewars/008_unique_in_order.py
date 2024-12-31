def unique_in_order(sequence):
    lst = []
    previous_char = ''

    for char in sequence:
        if char != previous_char:
            lst.append(char)
            
        previous_char = char

    return lst

print(unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B'])
print(unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3])
print(unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3])
