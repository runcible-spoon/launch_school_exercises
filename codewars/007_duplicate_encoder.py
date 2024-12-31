def duplicate_encode(word):
    
    characters = list(word.casefold())

    paren_string = '' 

    for character in characters:
        if characters.count(character) > 1:
            paren_string += ')'
        else:
            paren_string += '('
    
    return paren_string

print(duplicate_encode("din") == "(((")
print(duplicate_encode("recede") == "()()()")
print(duplicate_encode("Success") == ")())())")
print(duplicate_encode("(( @") == "))((")
