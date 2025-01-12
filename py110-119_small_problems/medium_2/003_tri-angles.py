'''
Tri-Angles

A triangle is classified as follows:

    Right: One angle is a right angle (exactly 90 degrees).
    Acute: All three angles are less than 90 degrees.
    Obtuse: One angle is greater than 90 degrees.

To be a valid triangle, the sum of the angles must be exactly 180 degrees, and every angle must be greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to worry about floating point errors. You may also assume that the arguments are in degrees.
'''

def triangle(angle1, angle2, angle3):
    VALID_ANGLE_SUM = 180
    MINIMUM_ANGLE = 0
    RIGHT = 90

    angles = [angle1, angle2, angle3]

    if sum(angles) != VALID_ANGLE_SUM or any(angle == MINIMUM_ANGLE for angle in angles):
        return 'invalid'
    if any(angle == RIGHT for angle in angles):
        return 'right'
    if all(angle < RIGHT for angle in angles):
        return 'acute'
    else:
        return 'obtuse'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
