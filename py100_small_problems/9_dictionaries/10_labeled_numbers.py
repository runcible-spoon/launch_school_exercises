'''
Use a for loop to iterate over the numbers dictionary and print each element's key/value pair.

expected output: 

A high number is 100.
A medium number is 50.
A low number is 10.
'''

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for element in numbers.items():
    print(f'A {element[0]} number is {element[1]}')
