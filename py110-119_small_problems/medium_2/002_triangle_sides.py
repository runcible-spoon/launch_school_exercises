'''
Triangle Sides

A triangle is classified as follows:

    Equilateral: All three sides have the same length.
    Isosceles: Two sides have the same length, while the third is different.
    Scalene: All three sides have different lengths.

To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side,
and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four
strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.
'''
def triangle(side1, side2, side3):
    sorted_sides = sorted([side1, side2, side3])
    valid_side_ratios = sum(sorted_sides[:2]) > sorted_sides[2]

    if (not side1 or not side2 or not side3) or not valid_side_ratios:
        return 'invalid'
    if side1 == side2 == side3:
        return 'equilateral'
    if side1 != side2 != side3:
        return 'scalene'
    else:
        return 'isosceles'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
print(triangle(0, 0, 0) == "invalid") # True
