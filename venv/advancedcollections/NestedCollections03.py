s = {(10, 20, 30)}
print(s)
# s = {(10, 20, 30), [40, 50, 60]}
# Traceback (most recent call last):
#   File "/Code/venv/advancedcollections/NestedCollections03.py", line <>, in <module>
#     s = {(10, 20, 30), [40, 50, 60]}
# TypeError: unhashable type: 'list'

print()

d = {(10, 20): 'items'}
print(type(d), d)

# d = {(10, 20): 'items', [30, 40]: 'items'}
# Traceback (most recent call last):
#   File "/Code/venv/advancedcollections/NestedCollections03.py", line <>, in <module>
#     d = {(10, 20): 'items', [30, 40]: 'items'}
# TypeError: unhashable type: 'list'

d = {(10, 20): 'items', (30, 40): [50, 60]}
print(type(d), d)

# {(10, 20, 30)}
#
# <class 'dict'> {(10, 20): 'items'}
# <class 'dict'> {(10, 20): 'items', (30, 40): [50, 60]}
