'''
Madlibs is a simple game where you create a story template with "blanks" for 
words. You, or another player, then construct a list of words and place them 
into the story, creating an often silly or funny story as a result.

Create a simple madlib program that prompts for a noun, a verb, an adverb, 
and an adjective, and injects them into a story that you create.
'''

def madlibs():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    adverb = input("Enter an adverb: ")
    verb = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter a third noun: ")

    story = f'Your {adjective} {noun} {adverb} {verb} the {noun2} out of my {noun3}.'
    print(story)

madlibs()

'''Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly

Expected Output

Do you walk your blue dog quickly? That's hilarious!
The blue dog walks quickly over the lazy dog.
The dog quickly walks up to Joe's blue turtle.
'''
