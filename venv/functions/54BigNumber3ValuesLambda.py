s = lambda a, b, c: a if a > b and a > c else b if b > c else c
# PEP 8: E731 do not assign a lambda expression, use a def
print('Bigger of ({},{},{}) is {}'.format(10, 20, 30, s(10, 20, 30)))
print('Bigger of ({},{},{}) is {}'.format(20, 100, 5, s(20, 100, 5)))
print('Bigger of ({},{},{}) is {}'.format(-10, -20, -30, s(-10, -20, -30)))

# Bigger of (10,20,30) is 30
# Bigger of (20,100,5) is 100
# Bigger of (-10,-20,-30) is -10
