def dig_pow(n, p):
    
    digits = [ int(num) for num in str(n)]

    summation = 0
    for i in digits:
        summation += i ** p
        p += 1
    
    k, k_mod = divmod(summation, n)
    
    return k if not k_mod else -1


print(dig_pow(89, 1) == 1)
print(dig_pow(92, 1) == -1)
print(dig_pow(46288, 3) == 51)
print(dig_pow(41, 5) == 25)
print(dig_pow(114, 3) == 9)
print(dig_pow(8, 3) == 64)
