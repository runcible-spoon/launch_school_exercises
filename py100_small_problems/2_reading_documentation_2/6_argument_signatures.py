# How many arguments does the str.join method expect? What happens if you call it with fewer or more arguments?

# str.join expects one argument: an iterable. 

iterable = ['h', 'e', 'l', 'l', 'o']

joined_iterable = ''.join(iterable)

print(joined_iterable)
