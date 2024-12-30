
'''
Further Exploration

Our solution only works with positive numbers in the range of 0 to 360 
(inclusive). Can you refactor it so that it works with any positive or 
negative number?

Our solution has the following results for inputs outside the range 0-360:
'''


'''print(dms(-1) == "-1°00'00\"")  # True
print(dms(400) == "400°00'00\"")   # True
print(dms(-40) == "-40°00'00\"")  # True
print(dms(-420) == "-420°00'00\"") # True'''


'''
Since degrees are normally restricted to the range 0-360, can you modify the 
code so it returns a value in the appropriate range when the input is less 
than 0 or greater than 360?
'''

DEGREE = "\u00B0"

def dms(angle):

    if -360 <= angle < 0:
        angle += 360
    
    elif angle < -360:
        angle = 360 - (abs(angle) - 360)
    
    elif angle > 360:
        angle -= 360
    
    degrees_rounded = int(angle)
    degree_remainder = angle - degrees_rounded

    minutes = degree_remainder * 60
    minutes_rounded = int(minutes)
    minutes_remainder = minutes - minutes_rounded

    seconds = minutes_remainder * 60
    seconds_rounded = int(seconds)

    angle = f"{degrees_rounded}{DEGREE}{minutes_rounded:02}'{seconds_rounded:02}\""

    return angle or "0°00'00\""

print(dms(-1) == "359°00'00\"") # True
print(dms(400) == "40°00'00\"")  # True
print(dms(-40) == "320°00'00\"")  # True
print(dms(-420) == "300°00'00\"") # True
