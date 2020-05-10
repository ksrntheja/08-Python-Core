def f01(x, *n):
    print('x :', x, type(x))
    print('n :', n, type(n))


f01(1)
print()
f01(1, 2)
print()
f01(1, 2, 3)
print()
f01()

# x : 1 <class 'int'>
# n : () <class 'tuple'>
#
# x : 1 <class 'int'>
# n : (2,) <class 'tuple'>
#
# x : 1 <class 'int'>
# n : (2, 3) <class 'tuple'>
#
# Traceback (most recent call last):
#   File "/Code/venv/functions/24VariableLengthArgv.py", line <>, in <module>
#     f01()
# TypeError: f01() missing 1 required positional argument: 'x'
