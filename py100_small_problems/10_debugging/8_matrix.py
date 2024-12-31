'''
We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game. 


However, we encountered an issue, as whenever we change a value in one nested list, 
all nested lists are affected. 

Can you fix the code?
'''

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"

print('', matrix[0], '\n', matrix[1], '\n', matrix[2]) 

# [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
