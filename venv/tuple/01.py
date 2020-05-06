t = (10, 'theja', 20, 10)
print(t, type(t))

t = 10, 'theja', 20, 10
print(t, type(t))

print('t[0] ->', t[0])
print('t[-1] ->', t[-1])

t[0] = 777

# (10, 'theja', 20, 10) <class 'tuple'>
# (10, 'theja', 20, 10) <class 'tuple'>
# t[0] -> 10
# t[-1] -> 10
# Traceback (most recent call last):
#   File "/Code/venv/tuple/01.py", line <>, in <module>
#     t[0] = 777
# TypeError: 'tuple' object does not support item assignment
