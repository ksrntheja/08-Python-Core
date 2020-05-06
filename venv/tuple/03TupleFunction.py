l = [10, 20, 30, ]
print(l, type(l))
t = tuple(l)
print(t, type(t))

s = 'Hello,'
print(s, type(s))
t = tuple(s)
print(t, type(t))

r = range(1, 11, 2)
print(r, type(r))
t = tuple(r)
print(t, type(t))

t = tuple(10)

# [10, 20, 30] <class 'list'>
# (10, 20, 30) <class 'tuple'>
# Hello, <class 'str'>
# ('H', 'e', 'l', 'l', 'o', ',') <class 'tuple'>
# range(1, 11, 2) <class 'range'>
# (1, 3, 5, 7, 9) <class 'tuple'>
# Traceback (most recent call last):
#   File "/Code/venv/tuple/03TupleFunction.py", line <>, in <module>
#     t = tuple(10)
# TypeError: 'int' object is not iterable
