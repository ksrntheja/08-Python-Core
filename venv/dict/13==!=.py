a = {100: 'A', 200: 'B'}
b = {300: 'C', 400: 'D'}
c = {200: 'B', 100: 'A'}

print(id(a))
print(id(b))
print(id(c))

print(a == b)
print(a != b)
print(a == c)

# 139760391145512
# 139760391145584
# 139760391145944
# False
# True
# True
