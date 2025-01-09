'''
Fibonacci Numbers (Memoization)

Our recursive fibonacci function from the previous exercise isn't very efficient. It starts slowing down with an nth argument value somewhere around 35-60, depending on your system.
One way to improve the performance of our recursive fibonacci function (and other recursive functions) is to use memoization.

Memoization is an approach that involves saving a computed answer for future reuse, instead of computing it from scratch every time it is needed.
In the case of our recursive fibonacci function, using memoization saves calls to fibonacci(nth - 2) because the necessary values have already been computed by the recursive calls to fibonacci(nth - 1).

For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.

Hint: One approach to memoization is to use a lookup table, such as an object, for storing and accessing previously computed values.
'''

fib_nums = {}
def fibonacci(n):
    if n <= 2:
        return 1
    fib_nums[n] = fibonacci(n - 2)
    return fibonacci(n - 1) + fib_nums[n]

# ^ this is not any faster than regular recursion

# LS version

fib_nums = {}
def fibonacci(n):
    if n <= 2:
        return 1
    elif n in fib_nums:
        return fib_nums[n]
    else:
        fib_nums[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib_nums[n]




'''print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)        # True
print(fibonacci(3) == 2)        # True
print(fibonacci(4) == 3)        # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True'''
# print(fibonacci(20) == 6765)     # True

print(fibonacci(150))
