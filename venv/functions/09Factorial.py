def factorial(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial


number = int(input('Enter a number: '))
print('{} factorial = {}'.format(number, factorial(number)))

# Enter a number: 8
# 8 factorial = 40320
