from functools import reduce

l1 = [1, 2, 3, 4, 5]


def function(x, y):
    print(x, y)
    return x + y


result = reduce(function, l1)
# result = reduce(lambda x, y: x + y, l1)
print(result)

print()

result = reduce(lambda x, y: print(x, y), l1)
print(result)

# 1 2
# 3 3
# 6 4
# 10 5
# 15
#
# 1 2
# None 3
# None 4
# None 5
# None
