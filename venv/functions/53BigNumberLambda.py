s = lambda a, b: a if a > b else b
# PEP 8: E731 do not assign a lambda expression, use a def
print('Bigger of ({},{}) is {}'.format(10, 20, s(10, 20)))
print('Bigger of ({},{}) is {}'.format(20, 10, s(20, 10)))

# Bigger of (10,20) is 20
# Bigger of (20,10) is 20
