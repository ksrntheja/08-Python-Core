def outer():
    print('outer function started')

    def inner():
        print('inner function execution')

    print('outer function calling inner function')
    inner()


outer()
print('Done')
inner()

# outer function started
# outer function calling inner function
# inner function execution
# Done
# Traceback (most recent call last):
#   File "/Code/venv/functions/71FunctionAliasingDelete01.py", line <>, in <module>
#     inner()
# NameError: name 'inner' is not defined
