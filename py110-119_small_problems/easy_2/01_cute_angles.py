'''
Write a function that takes a floating point number representing an 
angle between 0 and 360 degrees and returns a string representing 
that angle in degrees, minutes, and seconds. You should use a degree 
symbol (°) to represent degrees, a single quote (') to represent minutes, 
and a double quote (") to represent seconds. There are 60 minutes in a 
degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:
'''
DEGREE = "\u00B0"

def dms(angle):

    if angle == int(angle):
        return f"{angle}{DEGREE}00'00\""
    
    
    degrees_rounded = int(angle)
    degree_remainder = angle - degrees_rounded

    minutes = degree_remainder * 60
    minutes_rounded = int(minutes)
    minutes_remainder = minutes - minutes_rounded

    seconds = minutes_remainder * 60
    seconds_rounded = int(seconds)

    angle = f"{degrees_rounded}{DEGREE}{minutes_rounded:02}'{seconds_rounded:02}\""

    return angle or "0°00'00\""



# All of these examples should print True
print(dms(76.73) == "76°43'48\"")
print(dms(30) == "30°00'00\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
