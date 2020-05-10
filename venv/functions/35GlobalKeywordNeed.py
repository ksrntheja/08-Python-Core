a = 10


def f01():
    a = 20
    # Shadows name 'a' from outer scope
    print(a)
    a = 30
    print(a)


def f02():
    print(a)


f01()
f02()

# 20
# 30
# 10
