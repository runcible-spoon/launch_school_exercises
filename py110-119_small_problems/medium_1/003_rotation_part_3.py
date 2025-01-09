'''
Rotation (Part 3)

Take the number                                                                             735291

and rotate it by one digit to the left, getting                                             352917

Next, keep the first digit fixed in place and rotate the remaining digits to get            329175

Keep the first two digits fixed in place and rotate again to get                            321759

Keep the first three digits fixed in place and rotate again to get                          321597

Finally, keep the first four digits fixed in place and rotate the final two digits to get   321579

The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer.

You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.
'''

def rotate_rightmost_digits(num, digit_count):
    string_num = str(num)

    target_digit = string_num[-digit_count]

    target_digit_location = string_num.index(target_digit)

    first_section = string_num[:target_digit_location]

    second_section = string_num[target_digit_location + 1:]

    new_string_num = ''.join([first_section, second_section, target_digit])

    return int(new_string_num)

def max_rotation(num):
    string_num = str(num)
    for index in range(len(string_num), 0, -1):
        string_num = rotate_rightmost_digits(string_num, index)
    return string_num

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
