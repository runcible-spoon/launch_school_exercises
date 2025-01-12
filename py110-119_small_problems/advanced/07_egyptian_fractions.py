'''
Egyptian Fractions

A Rational Number is any number that can be represented as the result of the division between two integers, e.g., 1/3, 3/2, 22/7, etc.
The number to the left is called the numerator, and the number to the right is called the denominator.

A Unit Fraction is a rational number where the numerator is 1.

An Egyptian Fraction is the sum of a series of distinct unit fractions (no two are the same), such as:

1   1    1    1
- + - + -- + --
2   3   13   15

Every positive rational number can be written as an Egyptian fraction. For example:

    1   1   1   1
2 = - + - + - + -
    1   2   3   6

Write two functions: one that takes a Rational number as an argument,
and returns a list of the denominators that are part of an Egyptian Fraction representation of the number,
and another that takes a list of numbers in the same format, and calculates the resulting Rational number.

You will need to use the Fraction class provided by the fractions module.

Every rational number can be expressed as an Egyptian Fraction.
In fact, every rational number can be expressed as an Egyptian Fraction in an infinite number of different ways.
Thus, the first group of examples may not show the same values as your solution.
They do, however, show the expected form of the solution.
The remaining examples merely demonstrate that the output of egyptian can be reversed by unegyptian.

For more info on Egyptian Fractions, see this page.
'''

'''
Problem:
- input: reduced fraction where numerator can be larger than denominator
- output: list of n... where each n is the denomintor of a unit fraction and the list sums to input fraction

Data structure:
- output list of denominators
- dictionary of "ones"? where each dict key represents a 1 in input fraction's value

Algorithm:
- while sum of unit fractions as represented denominators list is less than the value of input fraction:
    - if adding 1/n to denominator list does not put the sum value above input fraction value, add it to the list
    - n += 1
'''

from fractions import Fraction

def unegyptian(denominator_list):
    return sum([Fraction(1, denominator)
                for denominator in denominator_list])

def egyptian(rational_number):
    unit_fractions = []
    denominator = 1

    while unegyptian(unit_fractions) < rational_number:
        if (unegyptian(unit_fractions) + Fraction(1, denominator)
           > rational_number):
            denominator += 1
        else:
            unit_fractions.append(denominator)
            denominator += 1

    return unit_fractions


'''from fractions import Fraction

def egyptian(rational_number):
    unit_fractions = []
    denominator = 1

    while sum(unit_fractions) != rational_number:
        if sum(unit_fractions) + Fraction(1, denominator) <= rational_number:
            unit_fractions.append(Fraction(1, denominator))
        denominator += 1
    return [ unit_fraction.denominator for unit_fraction in unit_fractions ]

def unegyptian(egyptian):
    return sum([ Fraction(1, denominator) for denominator in egyptian])'''

# LS solution
'''from fractions import Fraction

def egyptian(target_value):
    denominators = []
    unit_denominator = 1
    while target_value != 0:
        unit_fraction = Fraction(1, unit_denominator)
        if unit_fraction <= target_value:
            target_value -= unit_fraction
            denominators.append(unit_denominator)

        unit_denominator += 1

    return denominators

def unegyptian(denominators):
    return sum([Fraction(1, d) for d in denominators])'''

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)) == [1, 2, 3, 6]) # True
print(egyptian(Fraction(137, 60)) == [1, 2, 3, 4, 5])  # True
print(egyptian(Fraction(3, 1)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]) # True


# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))
