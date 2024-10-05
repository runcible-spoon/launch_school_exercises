'''
Write a program that asks the user to enter an integer greater than 0, 
then asks whether the user wants to determine the sum or the product of 
all numbers between 1 and the entered integer, inclusive.

Example 1

Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.

Example 2

Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.

Further Exploration

Suppose the input was a list of space separated integers instead of 
just a single integer? How would your compute_sum and compute_product 
functions change?
'''

def get_integer():
    print("Please enter an integer greater than 0: ")
    integer = input()

    while not is_input_valid(integer):
        print("Invalid input.\nEnter an integer greater than 0: ")
        integer = input()

    return int(integer)

def is_input_valid(input):
    try:
        int(input)
    except ValueError:
        return False
    
    return int(input) > 0

def get_operation():
    print('Enter "s" to compute the sum, or "p" to compute the product. ')
    operation = input().lower()

    while not operation or operation not in ('s', 'p'):
        print("Invalid operation. (s) for sum, (p) for product. ")
        operation = input().lower()
    
    match operation:
        case 's':
            return 'sum'
        case 'p':
            return 'product'


def add(integer):
    sum = 0
    for num in range(1, integer + 1):
        sum += num
        print(sum)

    return sum

def multiply(integer):
    product = 1
    for num in range(1, integer + 1):
        product *= num
        print(product)

    return product

def perform_operation(operation, integer):
    match operation:
        case 'sum':
            return add(integer)
        case 'product':
            return multiply(integer)
        
def display_results(integer, operation, result):
    print(f"The {operation} of the integers between 1 and {integer} is {result}.")
        
def main():
    integer = get_integer()

    operation = get_operation()

    result = perform_operation(operation, integer)

    display_results(integer, operation, result)

# main()


# further exploration

def get_integer_list():
    print("enter a space-separated list of integers: ")
    string_list = input().split(" ")

    integer_list = []

    for string in string_list:
        integer_list.append(int(string))
        
    return integer_list

def add_list(lst):
    sum = 0
    for num in lst:
        sum += num
    
    return sum

def multiply_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product


def perform_operation_on_list(operation, integer_list):
    match operation:
        case 'sum':
            return add_list(integer_list)
        case 'product':
            return multiply_list(integer_list)
        
def display_results_of_list(integer_list, operation, result):
    print(f"The {operation} of the integers between 1 and {integer_list} is {result}.")

def main_2():
    integer_list = get_integer_list()

    operation = get_operation()

    result = perform_operation_on_list(operation, integer_list)

    display_results_of_list(integer_list, operation, result)

main_2()
