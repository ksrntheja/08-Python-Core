l = [1, 2, 3, 4, 5]


def doubleIt(x):
    return 2 * x


print(map(doubleIt, l))
l = list(map(doubleIt, l))
print(l)

# <map object at 0x7f9029928438>
# [2, 4, 6, 8, 10]
