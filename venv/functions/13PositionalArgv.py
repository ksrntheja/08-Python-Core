def sub(a, b):
    print(a - b)


a = 10
b = 20
print('{} - {} is '.format(a, b), end='')
sub(a, b)
print('{} - {} is '.format(b, a), end='')
sub(b, a)

sub(a)

# 10 - 20 is -10
# 20 - 10 is 10
# Traceback (most recent call last):
#   File "/Code/venv/functions/13PositionalArgv.py", line <>, in <module>
#     sub(a)
# TypeError: sub() missing 1 required positional argument: 'b'
