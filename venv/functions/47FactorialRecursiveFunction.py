def factorial(n):
    print('Exe for {}'.format(n))
    if n < 2:
        result = 1
    else:
        result = n * factorial(n - 1)
    print('Returning for {} -> {}'.format(n, result))
    return result


n = int(input('Enter number:'))
print('Factorial of {} is {}'.format(n, factorial(n)))

# Enter number:5
# Exe for 5
# Exe for 4
# Exe for 3
# Exe for 2
# Exe for 1
# Returning for 1 -> 1
# Returning for 2 -> 2
# Returning for 3 -> 6
# Returning for 4 -> 24
# Returning for 5 -> 120
# Factorial of 5 is 120
