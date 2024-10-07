'''
Build a program that randomly generates and prints Teddy's age. 

To get the age, you should generate a random number between 20 and 100, 
inclusive.

Example Output
Teddy is 69 years old!
'''

import random


def teddy_age():
    return f"Teddy is {random.randint(20, 100)} years old!"

print(teddy_age())
