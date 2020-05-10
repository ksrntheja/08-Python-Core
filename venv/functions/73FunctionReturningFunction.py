def outer():
    print('outer function started')

    def inner():
        print('inner function execution')

    print('outer function returning inner function')
    return inner()


f = outer()
print(f)
f()
f()
f()

# outer function started
# outer function returning inner function
# inner function execution
# None
# Traceback (most recent call last):
#   File "/Code/venv/functions/73FunctionReturningFunction.py", line <>, in <module>
#     f()
# TypeError: 'NoneType' object is not callable
