def f(arg1, arg2, arg3=4, arg4=8):
    print(arg1, arg2, arg3, arg4)


f(3, 2)
f(10, 20, 30, 40)
f(25, 50, arg4=100)
f(arg4=2, arg1=3, arg2=4)

# f()
# Traceback (most recent call last):
#   File "/Code/venv/functions/32.py", line <>, in <module>
#     f()
# TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'

# f(arg3=10, arg4=20, 30, 40)
#   File "/Code/venv/functions/32.py", line <>
#     f(arg3=10, arg4=20, 30, 40)
#                        ^
# SyntaxError: positional argument follows keyword argument

# f(4, 5, arg2=6)
# Traceback (most recent call last):
#   File "/Code/venv/functions/32.py", line <>, in <module>
#     f(4, 5, arg2=6)
# TypeError: f() got multiple values for argument 'arg2'

# f(4, 5, arg3=5, arg5=6)
# Traceback (most recent call last):
#   File "/Code/venv/functions/32.py", line <>, in <module>
#     f(4, 5, arg3=5, arg5=6)
# TypeError: f() got an unexpected keyword argument 'arg5'


# 3 2 4 8
# 10 20 30 40
# 25 50 4 100
# 3 4 4 2
