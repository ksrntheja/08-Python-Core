s = set()
s.add(10)
print(s, type(s))
# s.add(10, 20, 30)
# Traceback (most recent call last):
#   File "/Code/venv/set/08Functions.py", line <>, in <module>
#     s.add(10, 20, 30)
# TypeError: add() takes exactly one argument (3 given)
# s.update(10)
# Traceback (most recent call last):
#   File "/Code/venv/set/08Functions.py", line <>, in <module>
#     s.update(10)
# TypeError: 'int' object is not iterable
# s.update(10, )
s.update((10, ))
print(s, type(s))
s.update(range(1, 10, 2), range(0, 10, 2))
print(s, type(s))

# {10} <class 'set'>
# {10} <class 'set'>
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} <class 'set'>
