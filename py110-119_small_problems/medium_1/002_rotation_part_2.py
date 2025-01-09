'''
Rotation (Part 2)

Write a function that rotates the last count digits of a number.

To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.
'''

def rotate_rightmost_digits(num, digit_count):
    string_num = str(num)

    target_digit = string_num[-digit_count]

    target_digit_location = string_num.index(target_digit)

    first_section = string_num[:target_digit_location]

    second_section = string_num[target_digit_location + 1:]

    new_string_num = ''.join([first_section, second_section, target_digit])

    return int(new_string_num)


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True



# ls

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)

def rotate_string(string):
    return string[1:] + string[0]
