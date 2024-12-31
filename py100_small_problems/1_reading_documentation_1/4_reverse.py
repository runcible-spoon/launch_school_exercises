# Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

string = 'Hello, world'

print(repr(reversed(string))) # WRONG. str are immutable. Create a reversed string from an existing one with slicing:

string = 'Hello, world'
reversed_string = string[::-1]
print(reversed_string)
