s = {40, 10, 30, 20}
print(s, type(s))
print(s.pop())
print(s, type(s))
print(s.pop())
print(s, type(s))
print(s.pop())
print(s, type(s))
print(s.pop())
print(s, type(s))
print(s.pop())
print(s, type(s))

# {40, 10, 20, 30} <class 'set'>
# 40
# {10, 20, 30} <class 'set'>
# 10
# {20, 30} <class 'set'>
# 20
# {30} <class 'set'>
# 30
# set() <class 'set'>
# Traceback (most recent call last):
#   File "/Code/venv/set/10Pop.py", line <>, in <module>
#     print(s.pop())
# KeyError: 'pop from an empty set'
