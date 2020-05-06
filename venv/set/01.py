s = {}
print(s, type(s))

s = set()
print(s, type(s))
print(s.add(10))
s.add('z')
s.add('A')
s.add(20)
print(s.add(10))

print(s)

# print(s[0])
# Traceback (most recent call last):
#   File "/Code/venv/set/01.py", line <>, in <module>
#     print(s[0])
# TypeError: 'set' object does not support indexing

# print(s[1:3])
#  Traceback (most recent call last):
#   File "/Code/venv/set/01.py", line <>, in <module>
#     print(s[1:3])
# TypeError: 'set' object is not subscriptable

# {} <class 'dict'>
# set() <class 'set'>
# None
# None
# {10, 'A', 20, 'z'}
