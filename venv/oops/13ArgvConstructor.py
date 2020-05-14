class Constructor:
    def __init__(self):
        print('No argv Constructor execution...')

    def __init__(self, x):
        print('One argv Constructor execution...', x)


# c01 = Constructor()
#  Traceback (most recent call last):
#   File "/Code/venv/oops/13ArgvConstructor.py", line <>, in <module>
#     c01 = Constructor()
# TypeError: __init__() missing 1 required positional argument: 'x'
c02 = Constructor(10)
