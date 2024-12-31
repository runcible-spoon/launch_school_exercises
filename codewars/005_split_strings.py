def solution(s):
    s_is_odd = len(s) % 2
    
    result = []

    i = 0
    while i < len(s):
        try:
            result.append(s[i] + s[i + 1])
            i += 2
        except IndexError:
            break
    
    if s_is_odd:
        result.append(list(s).pop() + '_')
    
    return result

     

print(solution("asdfadsf") == ['as', 'df', 'ad', 'sf'])
print(solution("asdfads") == ['as', 'df', 'ad', 's_'])
print(solution("") == [])
print(solution('x') == ['x_'])
