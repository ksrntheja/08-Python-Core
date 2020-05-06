t = (40, 10, 30, 20)
print(t)
r = reversed(t)
print(r)
t1 = tuple(r)
print(t1)

print()

t = (40, 10, 30, 20)
# t.sort()
# Traceback (most recent call last):
#   File "/Code/venv/tuple/13Functions-02.py", line <>, in <module>
#     t.sort()
# AttributeError: 'tuple' object has no attribute 'sort'
t1 = sorted(t)
print(t1, type(t1))
print(t)

t1 = sorted(t, reverse=True)
print(t1, type(t1))
print(t)

# (40, 10, 30, 20)
# <reversed object at 0x7fe0e047a438>
# (20, 30, 10, 40)
#
# [10, 20, 30, 40] <class 'list'>
# (40, 10, 30, 20)
# [40, 30, 20, 10] <class 'list'>
# (40, 10, 30, 20)
