l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 100, 1000, 10000, 100000]
l = list(map(lambda x, y: x * y, l1, l2))
print(l)

l1 = [1]
l2 = [10, 100, 1000]
l = list(map(lambda x, y: x * y, l1, l2))
print(l)

# [10, 200, 3000, 40000, 500000]
# [10]
