x = int(input('Enter first   number:'))
y = int(input('Enter second  number:'))
print('x/y :', x / y)

# Enter first   number:10
# Enter second  number:5
# x/y : 2.0

# Enter first   number:10
# Enter second  number:0
# Traceback (most recent call last):
#   File "/Code/venv/exceptionhandling/05UserInputRuntimeError.py", line <>, in <module>
#     print('x/y :', x / y)
# ZeroDivisionError: division by zero

# Enter first   number:ten
# Traceback (most recent call last):
#   File "/Code/venv/exceptionhandling/05UserInputRuntimeError.py", line <>, in <module>
#     x = int(input('Enter first   number:'))
# ValueError: invalid literal for int() with base 10: 'ten'
