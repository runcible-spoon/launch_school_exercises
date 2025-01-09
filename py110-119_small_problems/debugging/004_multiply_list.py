'''
Key Check

You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising an error. Why is that? How would you fix this code?
'''

#original

'''def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))'''

#bug: keyerror
#debugged

def get_key_value(my_dict, key):
    return my_dict.get(key, None)

print(get_key_value({"a": 1}, "b"))
