d = {100: 'A', 200: 'B', 300: 'C'}
keys = d.keys()
print(keys, type(keys))
for key in keys:
    print(key)

print()

values = d.values()
print(values, type(values))
for value in values:
    print(value)

# dict_keys([100, 200, 300]) <class 'dict_keys'>
# 100
# 200
# 300
#
# dict_values(['A', 'B', 'C']) <class 'dict_values'>
# A
# B
# C
