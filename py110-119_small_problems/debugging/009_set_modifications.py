'''
Set Modifications

We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?'''

'''data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)
'''
# bug: set is changing size during iteration

# debugged:

data_set = {1, 2, 3, 4, 5}

new_set = set()

new_set.add(1)
print(new_set)

data_set.add(6)
print(data_set)

for item in data_set:
    if item % 2 != 0:
        new_set.add(item)

print(new_set)
