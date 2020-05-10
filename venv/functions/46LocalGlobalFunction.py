a = 10


def sum(a, b):
    return a + b


def sumGlobal(a, b):
    return globals()['a'] + b


# def sumGlobal02(a, b):
#     global a
#     a = 100
#     return a + b
#   File "/Code/venv/functions/46LocalGlobalFunction.py", line <>
#     global a
#     ^
# SyntaxError: name 'a' is parameter and global


print('a + 20 = {}'.format(sum(a, 20)))
print('100 + 20 = {}'.format(sum(100, 20)))

print('100 + 20 = {} [Global sum]'.format(sumGlobal(100, 20)))

# a + 20 = 30
# 100 + 20 = 120
# 100 + 20 = 30 [Global sum]
