s = 'theja'
# s.reverse()
# AttributeError: 'str' object has no attribute 'reverse'
r = reversed(s)
print(r)
print(type(r))
print(s)
for x in r:
    print(x)

# <reversed object at 0x7f76cae99b38>
# <class 'reversed'>
# theja
# a
# j
# e
# h
# t
