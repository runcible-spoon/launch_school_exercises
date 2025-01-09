'''
Staggered Case (Part 2)

Modify the function from the previous exercise so it ignores non-alphabetic characters
when determining whether it should uppercase or lowercase each letter.

The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.
'''
def staggered_case(string):
    result = ''
    alpha_index = 0
    for char in string:
        if char.isalpha():
            if alpha_index % 2 == 0:
                char = char.upper()
            else:
                char = char.lower()
            alpha_index += 1
        result += char

    return result

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
