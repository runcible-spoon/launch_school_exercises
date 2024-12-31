'''
Use Python's control structures to create a function that takes an ISO 639-1 
language code and returns a greeting in that language. 

You can take the examples below or add whatever languages you like.
'''

def greet(code):
    lang_codes = {
        'en': 'Hi!',
        'fr': 'Salut!',
        'pt': 'Olá!',
        'de': 'Hallo!',
        'sv': 'Hej!',
        'af': 'Haai!',
    }
    return lang_codes[code]

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
