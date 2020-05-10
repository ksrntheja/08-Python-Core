def factorial(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial


for i in range(1, 6):
    print('{} factorial = {}'.format(i, factorial(i)))

# 1 factorial = 1
# 2 factorial = 2
# 3 factorial = 6
# 4 factorial = 24
# 5 factorial = 120
