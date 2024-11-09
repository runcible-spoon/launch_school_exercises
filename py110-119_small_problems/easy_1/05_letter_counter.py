'''Write a function that takes a string consisting of zero or more 
space-separated words and returns a dictionary that shows the number 
of words of different sizes.

Words consist of any sequence of non-space characters.
'''

def word_sizes(string):

    list_of_all_lengths = [ len(word) for word in string.split() ]
    unordered_occurences = set()
    ordered_occurences = []
    count_of_length_instances = {}

    for num in list_of_all_lengths:
        if num not in unordered_occurences:
            unordered_occurences.add(num)
            ordered_occurences.append(num)
        
    for num in ordered_occurences:
        counter = 0
        for instance in list_of_all_lengths:
            if num == instance:
                counter += 1
    
        count_of_length_instances[num] = counter

    return count_of_length_instances
    

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})


# ls 

def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        word_size = len(word)
        if word_size not in counts:
            counts[word_size] = 0

        counts[word_size] += 1

    return counts
