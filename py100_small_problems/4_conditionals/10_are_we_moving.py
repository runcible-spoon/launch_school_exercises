'''
Determine what the following code snippet prints. 

First solve it in your head or on paper, then run it in your Python environment to check the result.
'''

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# expeted output: True

'''
Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:
'''

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)

# No parentheses needed. Has to evaluate L to R because it's already in precedence order.
