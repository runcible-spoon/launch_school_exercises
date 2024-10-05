'''
Write a function that takes one integer argument and returns True 
when the number's absolute value is odd, False otherwise.
'''

def absolute_value_odd(integer):

    if abs(integer) % 2 != 0:
        return True
    elif abs(integer) % 2 == 0:
        return False
    
print(absolute_value_odd(int(input())))


# ls solution

def is_odd(number):
    return abs(number) % 2 == 1
