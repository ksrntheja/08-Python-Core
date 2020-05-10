def f01(*n, x):
    print('x :', x, type(x))
    print('n :', n, type(n))


# f01(1)
# Traceback (most recent call last):
#   File "/Code/venv/functions/25VariableLengthArgv.py", line <>, in <module>
#     f01(1)
# TypeError: f01() missing 1 required keyword-only argument: 'x'
# f01(1, 2)
# TypeError: f01() missing 1 required keyword-only argument: 'x'
# f01(1, 2, 3)
# TypeError: f01() missing 1 required keyword-only argument: 'x'
f01()
# TypeError: f01() missing 1 required keyword-only argument: 'x'
