'''
Building on your solutions from the previous exercises, 
write a function local_greet that takes a locale as input, and returns a greeting. 

The locale lets us greet people from different countries appropriately, even when they share a common language, 
for example:
'''

'''

def greet(lang_code, region_code):
    lang = [
            'en', 'fr', 'br', 'pt', 'de', 'sv', 'af'
        ]
    
    region = [
            'US', 'GB', 'AU', 'CA', 'MA', 'PT', 'BR', 'DE', 'SV', 'AF'
        ]
    
    greetings = [ 
        'Hi!', 'Ello gov!', 'Gday!', 'Salut!', 'Olá!', 'Hallo!', 'Hej!', 'Haai!'
        ] 
    

list_of_dicts = [
        {'lang': 'en', 'region': 'US', 'greeting': 'Hi!'},
        {'lang': 'en', 'region': 'GB', 'greeting': 'Ello gov!'},
        {'lang': 'en', 'region': 'AU', 'greeting': 'Gday!'},
        {'lang': 'fr', 'region': 'CA', 'greeting': 'Salut!'},
        {'lang': 'fr', 'region': 'MA', 'greeting': 'Salut!'},
        {'lang': 'fr', 'region': 'MA', 'greeting': 'Salut!'},
        {'lang': 'br', 'region': 'PT', 'greeting': 'Olá!'},
        {'lang': 'pt', 'region': 'BR', 'greeting': 'Olá!'},
        {'lang': 'de', 'region': 'DE', 'greeting': 'Hallo!'},
        {'lang': 'sv', 'region': 'SV', 'greeting': 'Hej!'},
        {'lang': 'af', 'region': 'AF', 'greeting': 'Haai!'},
]

'''

def extract_language(locale):
    return locale.split('_')[0]


def extract_region(locale):
    return locale[3:5]




def local_greet(locale):
    if extract_language(locale) == 'en':
        if extract_region(locale) == 'US':
            return 'Hey!'
        elif extract_region(locale) == 'GB':
            return 'Ello gov!'
        else:
            return 'Gday!'
    elif extract_language(locale) == 'fr':
        return 'Salut!'
    elif extract_language(locale) == 'pt':
        if extract_region(locale) == 'PT':
            return 'Olá!'
        elif extract_region(locale) == 'BR':
            return 'Olá!'



print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

'''
Distinguish greetings for English speaking countries like the US, UK, Canada, or Australia in your implementation, 
and feel free to fall back on the language-specific greetings in all other cases, for example:
'''

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

'''
When implementing local_greet, make sure you re-use your extract_language, extract_region, 
and greet functions from the previous exercises.

If you're interested, you can find a list of locales here.
'''
