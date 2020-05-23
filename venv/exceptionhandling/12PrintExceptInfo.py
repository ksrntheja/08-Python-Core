try:
    print(10 / 0)
# except (ZeroDivisionError) as msg:
# Remove redundant parentheses
except (ZeroDivisionError) as msg:
    print('Exception type is:', type(msg))
    print('Exception type is:', msg.__class__)
    print('Exception class name is:', msg.__class__.__name__)
    print('Exception description is:', msg)

# Exception type is: <class 'ZeroDivisionError'>
# Exception type is: <class 'ZeroDivisionError'>
# Exception class name is: ZeroDivisionError
# Exception description is: division by zero
