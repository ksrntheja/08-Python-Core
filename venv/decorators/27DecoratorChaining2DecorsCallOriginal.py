def decor1(func):
    def inner1():
        print('decor1 execution')
        func()

    return inner1


def decor2(func):
    def inner2():
        print('decor2 execution')
        f()

    return inner2


@decor2
@decor1
def f():
    print('Original function')


f()

# /usr/bin/python3.6 /Code/venv/decorators/27DecoratorChaining2DecorsCallOriginal.py
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# decor2 execution
# Traceback (most recent call last):
#   File "/Code/venv/decorators/27DecoratorChaining2DecorsCallOriginal.py", line <>, in <module>
#     f()
#   File "/Code/venv/decorators/27DecoratorChaining2DecorsCallOriginal.py", line <>, in inner2
#     f()
#   File "/Code/venv/decorators/27DecoratorChaining2DecorsCallOriginal.py", line <>, in inner2
#     f()
#   File "/Code/venv/decorators/27DecoratorChaining2DecorsCallOriginal.py", line <>, in inner2
#     f()
#   [Previous line repeated 994 more times]
#   File "/Code/venv/decorators/27DecoratorChaining2DecorsCallOriginal.py", line <>, in inner2
#     print('decor2 execution')
# RecursionError: maximum recursion depth exceeded while calling a Python object
# 
# Process finished with exit code 1
