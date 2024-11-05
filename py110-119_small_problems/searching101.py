'''Write a program that solicits six (6) numbers from the user and 
prints a message that describes whether the sixth number appears 
among the first five.

Example 1

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Example 2

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.'''


def get_numbers():
    num_list = []
    for idx in range(6):
        num_list += input(f"Enter number {idx + 1} of 6: ")
      
    return num_list

def is_in_set(num_list):
    for num in num_list[0:5]:
        if num == num_list[-1]:
            return True

    return False

def display_result(result, num_list):
    if result:
        print(f"{num_list[-1]} is in {num_list}.")
    else: 
        print(f"{num_list[-1]} is not in {num_list}.")


def main():
    num_list = get_numbers()

    result = is_in_set(num_list)

    display_result(result, num_list)
    
main()


'''Further Exploration

Suppose we alter the problem to look for a number that satisfies a 
condition (e.g., a number greater than 25) instead of a specific 
number? Would the current solution still work? Why or why not?
'''
