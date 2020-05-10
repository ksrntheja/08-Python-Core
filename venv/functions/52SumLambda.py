s = lambda a, b: a + b
# PEP 8: E731 do not assign a lambda expression, use a def
print('{} + {} is {}'.format(1, 2, s(1, 2)))

# 1 + 2 is 3
