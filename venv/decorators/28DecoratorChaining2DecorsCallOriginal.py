def decor1(func):
    def inner1():
        print('decor1 execution')
        f()

    return inner1


def decor2(func):
    def inner2():
        print('decor2 execution')
        func()

    return inner2


@decor2
@decor1
def f():
    print('Original function')


f()

# /usr/bin/python3.6 /Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# decor1 execution
# decor2 execution
# Traceback (most recent call last):
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 23, in <module>
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 4, in inner1
#     f()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 12, in inner2
#     func()
#   File "/Code/venv/decorators/28DecoratorChaining2DecorsCallOriginal.py", line 3, in inner1
#     print('decor1 execution')
# RecursionError: maximum recursion depth exceeded while calling a Python object
# 
# Process finished with exit code 1
