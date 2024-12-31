'''
Loop over the elements of the fish_list list below, logging each one. 
Terminate the loop immediately after printing the string 'Nemo'.
'''

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    if fish == 'Nemo':
        print(fish)
        break
    print(fish)


# or...

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break


'''
Can you achieve the same result using a while loop? What would the code look like?
'''

fish_index = 0

while fish_index < len(fish_list):
    print(fish_list[fish_index])
    if fish_list[fish_index] == 'Nemo':
        break
    fish_index += 1
