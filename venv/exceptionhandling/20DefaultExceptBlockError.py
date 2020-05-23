try:
    x = int(input('Enter first  number:'))
    y = int(input('Enter second number:'))
    print('x/y ->', x / y)

except:
    print("Default Except:Plz provide valid input only")
except ZeroDivisionError:
    print('ZeroDivisionError: division by zero')

#   File "/Code/venv/exceptionhandling/20DefaultExceptBlockError.py", line <>
#     print('x/y ->', x / y)
#                        ^
# SyntaxError: default 'except:' must be last
