'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

a = 7

def my_function(b):
    b += 10
    return b

print(my_function(a))
print(a)

# output: 17 
# WRONG: a immutable. b += creates b and assigns it 10. a stays the same. 
