'''Write a function that counts the number of occurrences of each element in a given list.
Once counted, print each element alongside the number of occurrences.
Consider the words case sensitive e.g. ("suv" != "SUV").'''

def count_occurrences(collection):
    dct = { word: collection.count(word) for word in collection }

    for word, count in dct.items():
        print(f"{word} => {count}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

# count_occurrences(vehicles)

# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2


# Further Exploration
'''Try to solve the problem when words are case insensitive, e.g. "suv" and "SUV" represent the same vehicle type.'''

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'suv', 'suv', 'TRUCK', 'truck',
            'motorcycle', 'MOTORCYCLE', 'car', 'truck']

def count_occurrences_case_insensitive(collection):
    lower_collection = [ word.lower() for word in collection ]

    dct = { word: lower_collection.count(word) for word in lower_collection}

    for word, count in dct.items():
        print(f"{word} => {count}")

count_occurrences_case_insensitive(vehicles)
