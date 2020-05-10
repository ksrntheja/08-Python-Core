def sub(a, b):
    print(a - b)


a = 10
b = 20
print('{} - {} is '.format(a, b), end='')
sub(a=a, b=b)
print('{} - {} is [sub(b=b, a=a)] '.format(b, a), end='')
sub(b=b, a=a)

sub(a=a)

# 10 - 20 is -10
# 20 - 10 is [sub(b=b, a=a)] -10
# Traceback (most recent call last):
#   File "/Code/venv/functions/14KeywordArgv.py", line <>, in <module>
#     sub(a=a)
# TypeError: sub() missing 1 required positional argument: 'b'
