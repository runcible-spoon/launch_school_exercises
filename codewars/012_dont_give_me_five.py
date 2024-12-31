def dont_give_me_five(start,end):
    lst = list(range(start, end + 1))
    str_list = []
    for element in lst:
        str_list.append(str(element))
    
    lst = [ num for num in str_list if '5' not in num ]

    n = len(lst)
    return n   # amount of numbers


print(dont_give_me_five(1,9) == 8)
print(dont_give_me_five(4,17) == 12)
