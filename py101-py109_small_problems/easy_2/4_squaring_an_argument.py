'''
Using the multiply function from the "Multiplying Two Numbers" 
exercise, write a function that computes the square of its 
argument (the square is the result of multiplying a 
number by itself).
'''

def multiply(factor1, factor2):
    return factor1 * factor2

def square(root):
    return multiply(root, root)


print(square(5) == 25)   # True
print(square(-8) == 64)  # True

'''
Further Exploration

Suppose we want to generalize this function to a "power to the n" 
type function: cubed, to the 4th power, to the 5th, etc. 

How would we go about doing so while still using the multiply function?
'''

def exponentiate(root, power):
    product = root

    for _ in range(1, power):
        product = multiply(product, root)

    return product


print(exponentiate(2, 3) == 8)
print(exponentiate(-8, 4) == 4096)
