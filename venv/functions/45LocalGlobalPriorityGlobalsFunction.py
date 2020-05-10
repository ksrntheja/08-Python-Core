a = 10


def f01():
    a = 999
    print(a)
    print(globals())
    print(globals().get('a'))
    print(globals()['a'])


def f02():
    print(a)


f01()
f02()

# 999
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fd0a163e358>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Code/venv/functions/44LocalGlobalPriorityGlobalsFunction.py', '__cached__': None, 'a': 10, 'f01': <function f01 at 0x7fd0a167c0d0>, 'f02': <function f02 at 0x7fd09f876a60>}
# 10
# 10
# 10
