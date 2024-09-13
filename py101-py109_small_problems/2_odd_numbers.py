'''
Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

Bonus Question: Can you solve the problem by iterating over just the odd numbers?
'''

def print_odd_to_99():
    for i in range(100):
        if i % 2 == 1:
            print(i, '\n')

print_odd_to_99()

def iterate_only_the_odds():
    odds = [ i for i in range(100) if i % 2 == 1 ]
    for i in odds:
        print(i, '\n')

iterate_only_the_odds()

# ls solutions

for number in range(1, 100):
    if number % 2 == 1:
        print(number)


for number in range(1, 100, 2):
    print(number)


'''
Further Exploration: Consider adding a way for the user to specify the starting 
and ending values of the odd numbers printed.
'''

def print_only_odds(start_value, end_value):
    for number in range(int(start_value), int(end_value) + 1):
        if number % 2 == 1:
            print(number)
