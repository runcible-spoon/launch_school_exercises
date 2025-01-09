'''
List Deduplication

A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements is lost. How can we preserve the order?'''

'''data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed'''


data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]

new_data = []

for num in data:
    if num not in new_data:
        new_data.append(num)

print(new_data == [4, 2, 1, 3]) # order not guaranteed
