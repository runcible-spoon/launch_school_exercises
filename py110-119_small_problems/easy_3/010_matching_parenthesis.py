'''
Matching Parenthesis?

Write a function that takes a string as an argument and returns True
if all parentheses in the string are properly balanced, False otherwise.

To be properly balanced, parentheses must occur in matching '(' and ')' pairs.
Note that balanced pairs must start with a (, not a ).
'''
# chatgpt-enhanced while loop solution
def is_balanced(string):
    parentheses = [char for char in string if char in ['(', ')']]

    idx = 0
    while idx < len(parentheses) - 1:  # Ensure at least two elements to compare

        if parentheses[idx] == '(' and parentheses[idx + 1] == ')':

            parentheses.pop(idx)       # Remove '('
            parentheses.pop(idx)       # Remove ')' (same index after pop)
            idx = max(idx - 1, 0)      # Step back to check previous pairs

        else:
            idx += 1                   # Move to the next character

        print(f'idx: {idx}, parentheses: {parentheses} ')

    return not parentheses  # True if empty (balanced), False otherwise


# chatgpt from scratch solution
def is_balanced(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)  # Push opening parenthesis onto the stack
        elif char == ')':
            if not stack:       # No matching opening parenthesis
                return False
            stack.pop()         # Pop the last opening parenthesis from the stack

    return not stack  # True if the stack is empty, False otherwise

# count up for opens, down for closeds (leaning on ls solution)
def is_balanced(string):
    opens = 0
    for char in string:
        if char == '(':
            opens += 1
        elif char == ')':
            opens -= 1
        if opens < 0:
            return False
    return opens == 0

# my original:
    for parenthesis in parentheses:
        if parenthesis == '(':
            opens += 1
    for parenthesis in parentheses:
        if parenthesis == ')':
            opens -= 1
            if opens < 0:
                print('went negative')
                return False

    print('finished loops', parentheses, opens)
    return not opens

print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
