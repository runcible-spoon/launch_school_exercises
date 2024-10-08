'''
Write a function that takes a short line of text and prints it within a box.
'''

def print_in_box(string):
    number_of_dashes = len(string) + 2
    empty_line = ' ' * number_of_dashes
    
    print(f"+{'-' * number_of_dashes}+")
    print(f"|{empty_line}|")
    print(f"| {string} |")
    print(f"|{empty_line}|")
    print(f"+{'-' * number_of_dashes}+")
          


print_in_box('To boldly go where no one has gone before.')

'''
Output for Example 1

+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+
'''

#print_in_box('')

'''Output for Example 2

+--+
|  |
|  |
|  |
+--+
'''



'''
Further Exploration

Modify this function so that it truncates the message if it doesn't fit 
inside a maximum width provided as a second argument (the width is the 
width of the box itself). You may assume no maximum if the second argument 
is omitted.
'''


def print_in_box(string, max_width):
    horizontal_rule = f'+-{"-" * max_width}-+'
    empty_line = f'| {" " * max_width} |'

    if len(string) > max_width:
        string = string[:max_width]

    print(horizontal_rule)
    print(empty_line)
    print(f'| {string} |')
    print(empty_line)
    print(horizontal_rule)


print_in_box('To boldly go where no one has gone before.', 10)


'''
For a challenging but fun exercise, try word wrapping messages that are 
too long to fit, so that they appear on multiple lines but are still 
contained within the box. This isn't an easy problem, but it's doable 
with basic Python.
'''

def print_in_box(message, max_width):
    HORIZONTAL_RULE = f'+-{"-" * max_width}-+'
    message_line = f'| {message} |'
    EMPTY_LINE = f'| {" " * max_width} |'

    print(HORIZONTAL_RULE)
    print(EMPTY_LINE)

    if len(message) <= max_width:
        print(message_line)
        print(EMPTY_LINE)
        print(HORIZONTAL_RULE)

    else:
        number_of_overruns = (len(message) // max_width) + 1

        if len(message) > max_width:
            for _ in range(number_of_overruns):
                if len(message) < max_width:
                    spaces_from_right = max_width - len(message)
                    message_line = f'| {message[:max_width]}{" " * spaces_from_right} |'
                    print(message_line)
                    break
                
                message_line = f'| {message[:max_width]} |'
                print(message_line)
                message = message[max_width:]

        print(EMPTY_LINE)
        print(HORIZONTAL_RULE)

print_in_box('To boldly go where no one has gone before.', 20)
