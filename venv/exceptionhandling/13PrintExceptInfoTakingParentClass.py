try:
    x = int(input('Enter first  number:'))
    y = int(input('Enter second number:'))
    print('x/y ->', x / y)
except BaseException as msg:
    print('Exception type is:', type(msg))
    print('Exception type is:', msg.__class__)
    print('Exception class name is:', msg.__class__.__name__)
    print('Exception description is:', msg)

# Enter first  number:10
# Enter second number:2
# x/y -> 5.0

# Enter first  number:10
# Enter second number:0
# Exception type is: <class 'ZeroDivisionError'>
# Exception type is: <class 'ZeroDivisionError'>
# Exception class name is: ZeroDivisionError
# Exception description is: division by zero

# Enter first  number:10
# Enter second number:two
# Exception type is: <class 'ValueError'>
# Exception type is: <class 'ValueError'>
# Exception class name is: ValueError
# Exception description is: invalid literal for int() with base 10: 'two'
