def narcissistic(value):
    digits = [ int(digit) for digit in list(str(value)) ]

    return True if value == sum( [ digit ** len(digits) for digit in digits ] ) else False

print(narcissistic(7) == True) # '7 is narcissistic'
print(narcissistic(371) == True) # '371 is narcissistic'


print(narcissistic(122) == False) # '122 is not narcissistic'
print(narcissistic(4887) == False) # '4887 is not narcissistic'
