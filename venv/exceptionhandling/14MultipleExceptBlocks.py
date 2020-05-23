try:
    x = int(input('Enter first  number:'))
    y = int(input('Enter second number:'))
    print('x/y ->', x / y)
except ZeroDivisionError:
    print("Can't divide with 2")
except ValueError:
    print('Please provide int value only')

# Enter first  number:10
# Enter second number:0
# Can't divide with 2

# Enter first  number:19
# Enter second number:ten
# Please provide int value only
