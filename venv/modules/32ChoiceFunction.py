from random import *

l = ['AA', 'BB', 'CC', 'DD', 'EE']
for i in range(5):
    print(choice(l))

print()

t = ('AA', 'BB', 'CC', 'DD', 'EE')
for i in range(5):
    print(choice(t))

print()

s = 'ABCDE'
for i in range(5):
    print(choice(s))

print()

# s = {'AA', 'BB', 'CC', 'DD', 'EE'}
# for i in range(5):
#     print(choice(s))

# Traceback (most recent call last):
#   File "/Code/venv/modules/32ChoiceFunction.py", line <>, in <module>
#     print(choice(s))
#   File "/usr/lib/python3.6/random.py", line 261, in choice
#     return seq[i]
# TypeError: 'set' object does not support indexing

# d = {'AA': 10, 'BB': 20}
# print(type(d)) <class 'dict'>
# for i in range(5):
#     print(choice(d))
# Traceback (most recent call last):
#   File "/Code/venv/modules/32ChoiceFunction.py", line <>, in <module>
#     print(choice(d))
#   File "/usr/lib/python3.6/random.py", line 261, in choice
#     return seq[i]
# KeyError: 1

# EE
# DD
# DD
# BB
# CC
#
# CC
# EE
# BB
# AA
# AA
#
# D
# D
# C
# A
# C
