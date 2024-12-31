def pig_it(text):
    pig_latined_string = ''
    for word in text.split():
        if len(word) == 1 and word.isalnum(): 
            pig_latined_string += word + 'ay '
        elif not word.isalnum():
            pig_latined_string += word
        else:
            pig_latined_string += word[1:] + word[0] + 'ay '

    return pig_latined_string.rstrip()


print(pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay')
print(pig_it('This is my string') == 'hisTay siay ymay tringsay')
