s = {x * x for x in range(1, 6)}
print(s, type(s))

s = {2 ** x for x in range(1, 6)}
print(s, type(s))

# {1, 4, 9, 16, 25} <class 'set'>
# {32, 2, 4, 8, 16} <class 'set'>
