def outer():
    print('outer function started')

    def inner():
        print('inner function execution')

    inner()
    inner()
    inner()
    print('outer function completed')


outer()
inner()

# outer function started
# inner function execution
# inner function execution
# inner function execution
# outer function completed
# Traceback (most recent call last):
#   File "/Code/venv/decorators/04NestedFunctionsCallInnerFunction.py", line <>, in <module>
#     inner()
# NameError: name 'inner' is not defined
