def f1(func):
    func()


def f2():
    print('We cannot call f2 function directly')


f1(f2)

# filter(function, list)
# map(function, list)
# reduce(function, list)

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(n):
    return n % 2 == 0


print(filter(is_even, l))
even = list(filter(is_even, l))
print(even)

# We cannot call f2 function directly
# <filter object at 0x7fb49d285ba8>
# [0, 2, 4, 6, 8, 10]
