print('''list of tuples
tuple of tuples
set of tuples''')

l = [(100, 'A'), (200, 'B'), (300, 'C')]
print(l, type(l))
print(l[0], type(l[0]))
print(l[1], type(l[1]))
print(l[2], type(l[2]))
d = dict(l)
print(d, type(d))

print()

# l = [(100, 'A', 'B'), (200, 'B', 'B'), (300, 'C', 'C')]
# print(l, type(l))
# d = dict(l)
# Traceback (most recent call last):
#   File "/Code/venv/dict/02CreatedictFunction.py", line <>, in <module>
#     d = dict(l)
# ValueError: dictionary update sequence element #0 has length 3; 2 is required

t = ((100, 'A'), (200, 'B'), (300, 'C'))
print(t, type(t))
print(t[0], type(t[0]))
print(t[1], type(t[1]))
print(t[2], type(t[2]))
d = dict(t)
print(d, type(d))

print()

s = {(100, 'A'), (200, 'B'), (300, 'C')}
print(s, type(s))
d = dict(s)
print(d, type(d))

print()
print()

print('''list of lists
tuple of lists
# set of lists - Error - List Objects cannot be added to Set''')

l = [[100, 'A'], [200, 'B'], [300, 'C']]
print(l, type(l))
print(l[0], type(l[0]))
print(l[1], type(l[1]))
print(l[2], type(l[2]))
d = dict(l)
print(d, type(d))

print()

t = ([100, 'A'], [200, 'B'], [300, 'C'])
print(t, type(t))
print(t[0], type(t[0]))
print(t[1], type(t[1]))
print(t[2], type(t[2]))
d = dict(t)
print(d, type(d))

print()

# s = {[100, 'A'], [200, 'B'], [300, 'C']}
# print(s, type(s))
# d = dict(s)
# print(d, type(d))
# Traceback (most recent call last):
#   File "/Code/venv/dict/02CreateDictFunction.py", line 65, in <module>
#     s = {[100, 'A'], [200, 'B'], [300, 'C']}
# TypeError: unhashable type: 'list'

print()
print()

print('''list of sets
tuple of sets
set of sets''')

l = [{100, 'A'}, {200, 'B'}, {300, 'C'}]
print(l, type(l))
print(l[0], type(l[0]))
print(l[1], type(l[1]))
print(l[2], type(l[2]))
d = dict(l)
print(d, type(d))

print()

t = ({100, 'A'}, {200, 'B'}, {300, 'C'})
print(t, type(t))
print(t[0], type(t[0]))
print(t[1], type(t[1]))
print(t[2], type(t[2]))
d = dict(t)
print(d, type(d))

print()

# s = {{100, 'A'}, {200, 'B'}, {300, 'C'}}
# print(s, type(s))
# d = dict(s)
# print(d, type(d))
# Traceback (most recent call last):
#   File "/Code/venv/dict/02CreateDictFunction.py", line 101, in <module>
#     s = {{100, 'A'}, {200, 'B'}, {300, 'C'}}
# TypeError: unhashable type: 'set'


# list of tuples
# tuple of tuples
# set of tuples
# [(100, 'A'), (200, 'B'), (300, 'C')] <class 'list'>
# (100, 'A') <class 'tuple'>
# (200, 'B') <class 'tuple'>
# (300, 'C') <class 'tuple'>
# {100: 'A', 200: 'B', 300: 'C'} <class 'dict'>
#
# ((100, 'A'), (200, 'B'), (300, 'C')) <class 'tuple'>
# (100, 'A') <class 'tuple'>
# (200, 'B') <class 'tuple'>
# (300, 'C') <class 'tuple'>
# {100: 'A', 200: 'B', 300: 'C'} <class 'dict'>
#
# {(100, 'A'), (300, 'C'), (200, 'B')} <class 'set'>
# {100: 'A', 300: 'C', 200: 'B'} <class 'dict'>
#
#
# list of lists
# tuple of lists
# # set of lists - Error - List Objects cannot be added to Set
# [[100, 'A'], [200, 'B'], [300, 'C']] <class 'list'>
# [100, 'A'] <class 'list'>
# [200, 'B'] <class 'list'>
# [300, 'C'] <class 'list'>
# {100: 'A', 200: 'B', 300: 'C'} <class 'dict'>
#
# ([100, 'A'], [200, 'B'], [300, 'C']) <class 'tuple'>
# [100, 'A'] <class 'list'>
# [200, 'B'] <class 'list'>
# [300, 'C'] <class 'list'>
# {100: 'A', 200: 'B', 300: 'C'} <class 'dict'>
#
#
#
# list of sets
# tuple of sets
# set of sets
# [{'A', 100}, {200, 'B'}, {300, 'C'}] <class 'list'>
# {'A', 100} <class 'set'>
# {200, 'B'} <class 'set'>
# {300, 'C'} <class 'set'>
# {'A': 100, 200: 'B', 300: 'C'} <class 'dict'>
#
# ({'A', 100}, {200, 'B'}, {300, 'C'}) <class 'tuple'>
# {'A', 100} <class 'set'>
# {200, 'B'} <class 'set'>
# {300, 'C'} <class 'set'>
# {'A': 100, 200: 'B', 300: 'C'} <class 'dict'>
