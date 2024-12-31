def spin_words(sentence):
    spun_words = []
    for word in sentence.split():
        if len(word) >= 5:
            spun_words.append(word[::-1])
        else:
            spun_words.append(word)

    spun_words = ' '.join(spun_words)

    return spun_words

print(spin_words("Welcome") == "emocleW")
print(spin_words("to") == "to")
print(spin_words("CodeWars") == "sraWedoC")

print(spin_words("Hey fellow warriors") == "Hey wollef sroirraw")
print(spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes")
