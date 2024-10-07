'''
Write a program that prompts the user for two 
positive numbers (floating-point), then prints the 
results of the following operations on those two numbers: 
addition, subtraction, product, quotient, floor quotient, remainder, and power
 
Do not worry about validating the input.

==> Enter the first number:
3.141529
==> Enter the second number:
2.718282
==> 3.141529 + 2.718282 = 5.859811
==> 3.141529 - 2.718282 = 0.42324699999999993
==> 3.141529 * 2.718282 = 8.539561733178
==> 3.141529 / 2.718282 = 1.1557038600115808
==> 3.141529 // 2.718282 = 1.0
==> 3.141529 % 2.718282 = 0.42324699999999993
==> 3.141529 ** 2.718282 = 22.45792517468373
'''

def floating_point_arithmetic():
    float1 = float(input("Enter the first number: "))
    float2 = float(input("Enter the second number: "))

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y,
        '**': lambda x, y: x ** y,
        }

    for key in operations:
        print(f"{float1} {key} {float2} = {operations[key](float1, float2)}")


floating_point_arithmetic()
