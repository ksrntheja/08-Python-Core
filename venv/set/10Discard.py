s = {40, 10, 30, 20}
print(s, type(s))
print(s.discard(30))
print(s, type(s))
print(s.discard(50))
print(s, type(s))

# {40, 10, 20, 30} <class 'set'>
# None
# {40, 10, 20} <class 'set'>
# None
# {40, 10, 20} <class 'set'>
