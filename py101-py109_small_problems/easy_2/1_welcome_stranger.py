'''Create a function that takes 2 arguments, a list and a dictionary. 
The list will contain 2 or more elements that, when joined with spaces, 
will produce a person's name. The dictionary will contain two keys,
"title" and "occupation", and the appropriate values. 

 Your function should return a greeting that uses the person's 
 full name, and mentions the person's title.
 '''

def greetings(lst, dictionary):
    name = ' '.join(lst)

    title_occupation = dictionary["title"] + " " + dictionary["occupation"]

    article = "an" if dictionary["title"].startswith(('a','e','i','o','u')) else "a"

    return(f'Hello, {name}! '
           f'Nice to have {article} {title_occupation} around.')



greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)

# Hello, John Q Doe! Nice to have a Master Plumber around.
