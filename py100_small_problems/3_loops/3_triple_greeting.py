# Write a loop that prints the value of the greeting variable three times.

greeting = 'Aloha!'

print((greeting + ' ') * 3)

i = 0
while i < 3:
    print(greeting)
    i += 1


# or...

for _ in range(3):
    print(greeting)
