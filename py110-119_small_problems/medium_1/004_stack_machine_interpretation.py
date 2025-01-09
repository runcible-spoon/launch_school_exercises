'''
Stack Machine Interpretation

This problem takes a while to describe, which also gives a feeling of great complexity. The solution, however, is surprising in its overall lack of complexity. While it may take a while for you to come up with an appropriate mental model, and may also take considerably longer than other exercises in this section, go ahead and give it a try anyway.

A stack is a list of values that grows and shrinks dynamically. A stack may be implemented as a list that uses two list methods: list.append and list.pop. In most languages, we would use a list.push method instead of list.append, but Python uses list.append instead. Thus, we can talk of pushing things to the stack (adding them to the top of the stack) and popping them from the stack (removing the topmost stack item).

A stack-and-register programming language is a language that uses a stack instead of variables for all of its data. Each operation in the language operates on a register, which can be thought of as the current value. The register is not part of the stack.

An operation that requires two values pops the topmost item from the stack (i.e., the operation removes the most recently pushed value from the stack), operates on the popped value and the register value, then stores the result back in the register.

This sounds complex, but the behavior is straightforward to walk through manually. Consider a MULT operation in a stack-and-register language. It pops the topmost value from the stack, multiplies the popped value with the current value in the register, then replaces the register content with the result value. For example, suppose we start with a stack of [3, 6, 4] (where 4 is the topmost item in the stack) and a register value of 7, the MULT operation mutates the stack to [3, 6] (the 4 is popped), and the result of the multiplication, 28, is left in the register. If we do another MULT at this point, the stack is mutated to [3], and the register is left with the value 168.

Write a function that implements a miniature stack-and-register-based programming language that has the following commands (also called operations or tokens):

    n: Place an integer value, n, in the register. Do not modify the stack.
    PUSH : Push the current register value onto the stack. Leave the value in the register.
    ADD : Pop a value from the stack and add it to the register value, storing the result in the register.
    SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.
    MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.
    DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
    REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
    POP : Remove the topmost item from the stack and place it in the register.
    PRINT : Print the register value.

All operations are integer operations (which is only important with DIV and REMAINDER).

Programs will be supplied to your language function via a string argument.
Your function may assume that all arguments are valid programs
i.e., they will not do anything like trying to pop a non-existent value from the stack, and they won't contain any unknown tokens.

Initialize the stack and register to the values [] and 0, respectively.
'''

'''
PEDAC

Problem:
- Create a minilang function that receives single pre-validadted input string and performs integer functions encoded in that string.
- Create a stack that can store values via a PUSH function and return the "topmost" (most recently PUSHed) via a POP function.
- Create a dynamic register that represents the "working" variable.

Examples:
- See test cases

Data structure / Algorithm:
- Split input string into constituent tokens. Tokens are independent and have no "memory" or associations with the token ahead or behind, except in the context of variable storage within the program.
- Based on token, which can be an integer or one of 8 keywords, perform the corresponding action on the stack and register.
    - Input handling:
        - IF input.isdigit() or input[0] = '-' and input[1:].isdigit() --> perform n() function
        - IF input is PUSH, ADD, SUB... perform corresponding function
    - N function:
        - passed number and the register
        - register = number
        - return register
    - PUSH function:
        -
- Calculate a final register value based on all tokens in input.
- Return final value.


Further Exploration

Refactor the minilang function to include some error handling.
In particular, the function should detect and report empty stack conditions (trying to use a value from the stack when there are no values), and invalid tokens in the program.

Ideally, the function should return an error message if an error occurs, or None if the program runs successfully.

'''

def stack_pop(stack):
    if not stack:
        print('Cannot pop from empty stack.')
        return

    return stack.pop()

def minilang(command):

    register = 0
    stack = []

    tokens = command.split()

    for token in tokens:

        if token == 'PRINT':
            print(register)

        elif token.isdigit() or token.startswith('-') and token[1:].isdigit():
            register = int(token)

        elif token == 'PUSH':
            stack.append(register)

        elif token == 'POP':
            register = stack_pop(stack)

        elif token == 'ADD':
            register = register + stack_pop(stack)
        elif token == 'SUB':
            register = register - stack_pop(stack)
        elif token == 'MULT':
            register = register * stack_pop(stack)
        elif token == 'DIV':
            register = register // stack_pop(stack)
        elif token == 'REMAINDER':
            register = register % stack_pop(stack)

        else:
            print("Invalid token.")


minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

minilang('dfsdfsdf')
# prints 'invalid token' error message

minilang('POP')
# prints 'stack empty' error message
