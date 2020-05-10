l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
l3 = [1, 2, 3, 4, 5]

l = list(map(lambda x, y, z: x + y + z, l1, l2, l3))
print(l)

# [3, 6, 9, 12, 15]
