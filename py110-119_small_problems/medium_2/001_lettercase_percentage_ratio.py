'''
Lettercase Percentage Ratio

Write a function that takes a string and returns a dictionary containing the following three properties:

    the percentage of characters in the string that are lowercase letters
    the percentage of characters that are uppercase letters
    the percentage of characters that are neither

All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.
'''

def letter_percentages(string):

    percent_dict = {
        'lowercase': [],
        'uppercase': [],
        'neither':   [],
    }

    for char in string:
        if char.isalpha() and char == char.lower():
            percent_dict['lowercase'].append(char)
        elif char.isalpha() and char == char.upper():
            percent_dict['uppercase'].append(char)
        else:
            percent_dict['neither'].append(char)

    percent_dict['lowercase'] = f"{100 * (len(percent_dict['lowercase']) / len(string)):.2f}"
    percent_dict['uppercase'] = f"{100 * (len(percent_dict['uppercase']) / len(string)):.2f}"
    percent_dict['neither'] = f"{100 * (len(percent_dict['neither']) / len(string)):.2f}"

    return percent_dict

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}

print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
