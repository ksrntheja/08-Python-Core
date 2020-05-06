# Merging of collections

# List Merging
# 1
l1 = [10, 20]
l2 = [30, 40]
l3 = l1 + l2
print(l3, type(l3))
# 2 - variable length arguments
l3 = [*l1, *l2]
print(l3, type(l3))

print()

# Tuple Merging
# 1
t1 = (10, 20)
t2 = (30, 40)
t3 = t1 + t2
print(t3, type(t3))
# 2 - variable length arguments
t3 = (*t1, *t2)
print(t3, type(t3))

print()

# Set Merging
# 1
s1 = {10, 20}
s2 = {30, 40, 10}
s3 = s1 + s2
# Traceback (most recent call last):
#   File "/Code/venv/advancedcollections/MergingOfCollections.py", line <>, in <module>
#     s3 = s1 + s2
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# 2 - variable length arguments
s3 = {*s1, *s2}
print(s3, type(s3))

print()

# SeDictt Merging
# 1
d1 = {100: 'A', 200: 'B'}
d2 = {300: 'C', 400: 'D', 100: 'AA'}
# d3 = d1 + d2
# Traceback (most recent call last):
#   File "/Code/venv/advancedcollections/MergingOfCollections.py", line <>, in <module>
#     d3 = d1 + d2
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# 2 - key word arguments
# d3 = {**d1, **d2}
d3 = {*d1, *d2}
print(d3, type(d3))
d3 = {**d1, **d2}
print(d3, type(d3))

# [10, 20, 30, 40] <class 'list'>
# [10, 20, 30, 40] <class 'list'>
#
# (10, 20, 30, 40) <class 'tuple'>
# (10, 20, 30, 40) <class 'tuple'>
#
# {20, 40, 10, 30} <class 'set'>
#
# {400, 100, 200, 300} <class 'set'>
# {100: 'AA', 200: 'B', 300: 'C', 400: 'D'} <class 'dict'>
