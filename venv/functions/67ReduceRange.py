from functools import reduce

l1 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, range(1, 101))
print(result)

# 5050
