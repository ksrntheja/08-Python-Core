try:
    x = int(input('Enter first  number:'))
    y = int(input('Enter second number:'))
    print('x/y ->', x / y)
except ArithmeticError:
    print('ArithmeticError')
except ZeroDivisionError:
    print('ZeroDivisionError')

# Enter first  number:10
# Enter second number:0
# ArithmeticError
