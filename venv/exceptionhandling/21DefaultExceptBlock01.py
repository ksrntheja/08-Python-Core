try:
    x = int(input('Enter first  number:'))
    y = int(input('Enter second number:'))
    print('x/y ->', x / y)
except ZeroDivisionError:
    print('ZeroDivisionError: division by zero')
except ValueError:
    print('ValueError')
except:
    print("Default Except:Plz provide valid input only")

# Enter first  number:10
# Enter second number:0
# ZeroDivisionError: division by zero

# Enter first  number:ten
# ValueError
