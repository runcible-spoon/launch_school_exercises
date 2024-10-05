'''
Write a function that takes two strings as arguments, determines the 
length of the two strings, and then returns the result of 
concatenating the shorter string, the longer string, and the 
shorter string once again. You may assume that the strings 
are of different lengths.
'''

def get_strings():
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    return str1, str2

def order_strings(str1, str2):
    if len(str1) > len(str2):
        longer_string = str1
        shorter_string = str2
    else:
        longer_string = str2
        shorter_string = str1

    return shorter_string, longer_string

def short_long_short(shorter_string, longer_string):
    return shorter_string + longer_string + shorter_string

def main():
    str1, str2 = get_strings()

    shorter_string, longer_string = order_strings(str1, str2)

    print(short_long_short(shorter_string, longer_string))

main()

'''
# These examples should all print True

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
'''
