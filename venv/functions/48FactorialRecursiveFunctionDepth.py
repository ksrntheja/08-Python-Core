count = 0


def factorial(n):
    print('Exe for {}'.format(n))
    global count
    count = count + 1
    if n < 2:
        result = 1
    else:
        result = n * factorial(n - 1)
    print('Returning for {} -> {}'.format(n, result))
    return result


n = int(input('Enter number:'))
print('Factorial of {} is {}'.format(n, factorial(n)))
print(count)

# Python recursion depth is 994
#
#   [Previous line repeated 994 more times]
#
# RecursionError: maximum recursion depth exceeded while calling a Python object
