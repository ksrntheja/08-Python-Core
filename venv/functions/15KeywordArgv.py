def sub(a, b):
    print(a - b)


a = 10
b = 20
print('sub(10, 20) ', end='')
sub(10, 20)
print('sub(a=10, b=20) ', end='')
sub(a=10, b=20)
print('sub(10, b=20) ', end='')
sub(10, b=20)

# print('sub(a=10, 20) ', end='')
# sub(a=10, 20)
#   File "/Code/venv/functions/15KeywordArgv.py", line <>
#     sub(a=10, 20)
#              ^
# SyntaxError: positional argument follows keyword argument

# sub(10, 20) -10
# sub(a=10, b=20) -10
# sub(10, b=20) -10
