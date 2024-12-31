def array_diff(a, b):
    cleaned_list = []

    for element in a:
        if element not in b:
            cleaned_list.append(element)

    return cleaned_list


print(array_diff([1,2],[1]) == [2])
print(array_diff([1,2,2,2,3],[2]) == [1,3])
