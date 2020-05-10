def f01(*n, x):
    print('x :', x, type(x))
    print('n :', n, type(n))


f01(x=1)
print()
f01(1, 2, x=3)
print()
# f01(x=1, 2)
#   File "/Code/venv/functions/26VariableLengthArgv.py", line <>
#     f01(x=1, 2)
#             ^
# SyntaxError: positional argument follows keyword argument
print()
f01()

# x : 1 <class 'int'>
# n : () <class 'tuple'>
#
# x : 3 <class 'int'>
# n : (1, 2) <class 'tuple'>
#
#
# Traceback (most recent call last):
#   File "/Code/venv/functions/26VariableLengthArgv.py", line <>, in <module>
#     f01()
# TypeError: f01() missing 1 required keyword-only argument: 'x'
