class Test:
    def __init__(self):
        print('no-arg constructor')

    def __init__(self, a):
        print('one-arg constructor')

    def __init__(self, a, b):
        print('two-arg constructor')


# t = Test()
# Traceback (most recent call last):
#   File "/Code/venv/oops/144ConstructorOverloadingVariableLengthArgv.py", line <>, in <module>
#     t = Test()
# TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
# t = Test(10)
# Traceback (most recent call last):
#   File "/Code/venv/oops/144ConstructorOverloadingVariableLengthArgv.py", line <>, in <module>
#     t = Test(10)
# TypeError: __init__() missing 1 required positional argument: 'b'
t = Test(10, 20)

# two-arg constructor
