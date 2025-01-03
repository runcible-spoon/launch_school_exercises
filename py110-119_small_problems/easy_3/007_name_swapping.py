'''
Write a function that takes a string argument consisting of a first name, a space, and a last name.
The function should return a new string consisting of the last name, a comma, a space, and the first name.

You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").
'''

def swap_name(name):
    return f'{name.split()[1]}, {name.split()[0]}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# ls

def swap_name(name):
    return ', '.join(name.split()[::-1])


'''Further Exploration
Suppose the named person has one or more middle names? Refactor the current solution so it can accommodate this. The middle names should be listed after the first name:'''

def swap_name(name):
    first_and_middle_names = name.split()[:-1]
    last_name = name.split()[-1]
    joined_first_and_middle_names = ' '.join(first_and_middle_names)
    joined_full_name = f'{last_name}, {joined_first_and_middle_names}'

    return f'{name.split()[-1]}, {' '.join(name.split()[:-1])}'

print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
