try:
    x = int(input('Enter first  number:'))
    y = int(input('Enter second number:'))
    print('x/y ->', x / y)
except (ZeroDivisionError, ValueError) as msg:
    print('Exception class:', msg.__class__.__name__)
    print('Plz Provide valid numbers only and problem is:', msg)

# Enter first  number:10
# Enter second number:0
# Exception class: ZeroDivisionError
# Plz Provide valid numbers only and problem is: division by zero

# Enter first  number:10
# Enter second number:ten
# Exception class: ValueError
# Plz Provide valid numbers only and problem is: invalid literal for int() with base 10: 'ten'
