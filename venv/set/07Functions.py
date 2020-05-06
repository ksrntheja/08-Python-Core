s = {10, 20, 30, 40, 10}
print(s, len(s))

s = {10, 20, 30}
print(s.add(40))
print(s.add(10))
print(s)

s = {10, 20}
l = [30, 40]
s.update(l)
print(s, type(s))
s.update(range(1, 6), 'thejaji')
print(s, type(s))
t = (10, 80)
print(s.update(t))
print(s, type(s))

# {40, 10, 20, 30} 4
# None
# None
# {40, 10, 20, 30}
# {40, 10, 20, 30} <class 'set'>
# {1, 2, 3, 4, 5, 't', 'e', 40, 'a', 10, 'h', 'i', 20, 'j', 30} <class 'set'>
# None
# {1, 2, 3, 4, 5, 't', 'e', 40, 'a', 10, 'h', 'i', 80, 20, 'j', 30} <class 'set'>
