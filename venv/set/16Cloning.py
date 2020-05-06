s1 = {10, 20, 30}
s2 = s1.copy()
print(s1)
print(s2)
print(s1.discard(10))
print(s2.discard(20))
print(s1)
print(s2)

# {10, 20, 30}
# {10, 20, 30}
# None
# None
# {20, 30}
# {10, 30}
